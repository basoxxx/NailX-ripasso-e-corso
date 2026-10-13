-- Test dello schema NailX su un PostgreSQL che simula Supabase (vedi docs/SUPABASE.md).
-- Ogni controllo stampa OK oppure solleva un errore.
\set ON_ERROR_STOP 1
set client_min_messages = notice;

-- utenti di prova
insert into auth.users (id, email, raw_user_meta_data) values
  ('11111111-1111-1111-1111-111111111111', 'anna@example.com', '{"privacy_version":"2026-10"}'),
  ('22222222-2222-2222-2222-222222222222', 'bea@example.com',  '{}');

do $$ begin
  assert (select privacy_version from profiles where id = '11111111-1111-1111-1111-111111111111') = '2026-10', 'profilo/privacy';
  assert (select privacy_accepted_at from profiles where id = '22222222-2222-2222-2222-222222222222') is null, 'privacy assente';
  raise notice 'OK trigger profilo';
end $$;

-- ===== anonimo: niente domande d'esame, niente dati personali
set role anon;
do $$ begin
  begin perform * from exam_questions; raise exception 'anon legge domande'; exception when insufficient_privilege then null; end;
  begin assert (select count(*) from profiles) = 0, 'anon vede profili'; exception when insufficient_privilege then null; end;
  begin assert (select count(*) from certificates) = 0, 'anon vede attestati'; exception when insufficient_privilege then null; end;
  begin assert (select count(*) from progress) = 0, 'anon vede progressi'; exception when insufficient_privilege then null; end;
  assert (verify_certificate('NX-0000-XXXX') ->> 'valid')::boolean = false, 'verifica codice inesistente';
  begin perform start_exam(); raise exception 'anon avvia esame'; exception when insufficient_privilege then null; end;
  raise notice 'OK anonimo';
end $$;
reset role;

-- ===== Anna (autenticata)
set role authenticated;
select set_config('request.jwt.claim.sub', '11111111-1111-1111-1111-111111111111', false);
do $$ declare r jsonb; c certificates; a uuid; ans jsonb := '{}'; qid int;
begin
  -- domande non leggibili direttamente nemmeno da autenticata
  begin perform * from exam_questions; raise exception 'autenticata legge le risposte';
  exception when insufficient_privilege then null; end;
  -- non può falsificare la data privacy
  begin update profiles set privacy_accepted_at = now() - interval '1 year'; raise exception 'privacy falsificabile';
  exception when insufficient_privilege then null; end;
  update profiles set full_name = 'Anna Test';
  -- non può scrivere un attestato da sola
  begin insert into certificates (code, user_id, full_name, final_score, lessons_done, lessons_total, hours)
        values ('NX-FAKE', auth.uid(), 'x', 100, 1, 1, 1); raise exception 'insert attestato permesso';
  exception when insufficient_privilege then null; end;

  -- requisiti mancanti
  begin perform issue_certificate('Anna Rossi'); raise exception 'attestato senza requisiti';
  exception when raise_exception then null; end;

  -- progressi: tutte le lezioni + 2 esercizi completi
  insert into progress (user_id, data) values (auth.uid(), jsonb_build_object(
    'lessons', (select jsonb_object_agg(key, 1) from course_lessons),
    'checks', jsonb_build_object('es-apex', '[true,true,true,true]'::jsonb, 'es-french', '[true,false,true,true]'::jsonb),
    'quiz', '{"anatomia": 100, "final": 100}'::jsonb));

  -- esame: risposte sbagliate → bocciata
  r := start_exam();
  a := (r ->> 'attempt_id')::uuid;
  assert jsonb_array_length(r -> 'questions') = 40, 'esame 40 domande';
  assert not (r -> 'questions' -> 0 ? 'answer'), 'risposta esposta';
  r := submit_exam(a, '{}'::jsonb);
  assert (r ->> 'score')::int = 0, 'punteggio zero';
  begin perform submit_exam(a, '{}'::jsonb); raise exception 'doppia consegna';
  exception when raise_exception then null; end;
  begin perform issue_certificate('Anna Rossi'); raise exception 'attestato con esame bocciato';
  exception when raise_exception then null; end;
end $$;

-- risposte corrette (lette come superutente, simulando chi studia davvero)
reset role;
create temp table key as select id, answer from exam_questions;
grant select on key to authenticated;
set role authenticated;
do $$ declare r jsonb; a uuid; ans jsonb; c certificates;
begin
  r := start_exam(); a := (r ->> 'attempt_id')::uuid;
  select jsonb_object_agg(q ->> 'id', k.answer) into ans
    from jsonb_array_elements(r -> 'questions') q join key k on k.id = (q ->> 'id')::int;
  r := submit_exam(a, ans);
  assert (r ->> 'score')::int = 100, 'punteggio 100';
  assert (r -> 'results' -> 0 ? 'explanation'), 'spiegazioni';

  c := issue_certificate('  Anna   Rossi ');
  assert c.full_name = 'Anna Rossi', 'nome normalizzato';
  assert c.final_score = 100 and c.lessons_done = c.lessons_total, 'dati attestato';
  assert jsonb_array_length(c.exercises) = 1, 'solo esercizi completi al 100%';
  assert c.code ~ '^NX-\d{4}-[0-9A-F]{8}$', 'formato codice';
  -- rigenerare mantiene lo stesso codice
  assert (issue_certificate('Anna Maria Rossi')).code = c.code, 'codice stabile';
  perform set_config('nx.code', c.code, false);
  raise notice 'OK flusso Anna, codice %', c.code;
end $$;
reset role;

-- ===== Bea non vede i dati di Anna
set role authenticated;
select set_config('request.jwt.claim.sub', '22222222-2222-2222-2222-222222222222', false);
do $$ begin
  assert (select count(*) from progress) = 0, 'Bea vede progressi altrui';
  assert (select count(*) from certificates) = 0, 'Bea vede attestati altrui';
  assert (select count(*) from exam_attempts) = 0, 'Bea vede tentativi altrui';
  assert (select count(*) from profiles) = 1, 'Bea vede solo il suo profilo';
  update progress set data = '{}' where user_id = '11111111-1111-1111-1111-111111111111';
  assert not found, 'Bea modifica progressi altrui';
  raise notice 'OK isolamento tra utenti';
end $$;
reset role;

-- ===== verifica pubblica
set role anon;
do $$ declare v jsonb; begin
  v := verify_certificate(lower(current_setting('nx.code')));
  assert (v ->> 'valid')::boolean and v ->> 'full_name' = 'Anna Maria Rossi', 'verifica pubblica';
  assert not (v ? 'user_id'), 'verifica espone user_id';
  raise notice 'OK verifica pubblica';
end $$;
reset role;

-- ===== limite tentativi
set role authenticated;
select set_config('request.jwt.claim.sub', '22222222-2222-2222-2222-222222222222', false);
do $$ declare i int; begin
  for i in 1..10 loop perform start_exam(); end loop;
  begin perform start_exam(); raise exception 'limite tentativi non applicato';
  exception when raise_exception then null; end;
  raise notice 'OK limite tentativi';
end $$;

-- ===== cancellazione account (diritto all'oblio)
select set_config('request.jwt.claim.sub', '11111111-1111-1111-1111-111111111111', false);
select delete_my_account();
reset role;
do $$ begin
  assert not exists (select 1 from auth.users where id = '11111111-1111-1111-1111-111111111111'), 'utente non cancellato';
  assert not exists (select 1 from progress where user_id = '11111111-1111-1111-1111-111111111111'), 'progressi rimasti';
  assert not exists (select 1 from certificates where user_id = '11111111-1111-1111-1111-111111111111'), 'attestato rimasto';
  raise notice 'OK cancellazione account';
end $$;

-- ===== conservazione: cancellazione account inattivi da 24 mesi
insert into auth.users (id, email, created_at, last_sign_in_at) values
  ('33333333-3333-3333-3333-333333333333', 'vecchia@example.com', now() - interval '3 years', now() - interval '25 months'),
  ('44444444-4444-4444-4444-444444444444', 'attiva@example.com',  now() - interval '3 years', now() - interval '2 months');
do $$ declare n int; begin
  n := cleanup_inactive_accounts();
  assert not exists (select 1 from auth.users where id = '33333333-3333-3333-3333-333333333333'), 'inattiva non cancellata';
  assert exists (select 1 from auth.users where id = '44444444-4444-4444-4444-444444444444'), 'attiva cancellata per errore';
  raise notice 'OK pulizia account inattivi (%)', n;
end $$;
set role authenticated;
do $$ begin
  begin perform cleanup_inactive_accounts(); raise exception 'pulizia invocabile dal sito';
  exception when insufficient_privilege then null; end;
  raise notice 'OK pulizia non invocabile dal sito';
end $$;
reset role;
