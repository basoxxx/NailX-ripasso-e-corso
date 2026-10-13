-- NailX · profilo alla registrazione ed esame finale corretto dal server
-- Migrazione applicata al progetto Supabase; guida in docs/SUPABASE.md

create or replace function public.handle_new_user()
returns trigger language plpgsql security definer set search_path = public as $$
begin
  insert into public.profiles (id, privacy_version, privacy_accepted_at)
  values (
    new.id,
    new.raw_user_meta_data ->> 'privacy_version',
    case when new.raw_user_meta_data ? 'privacy_version' then now() end
  )
  on conflict (id) do nothing;
  return new;
end $$;

create trigger on_auth_user_created
  after insert on auth.users for each row execute function public.handle_new_user();

create or replace function public.start_exam()
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  uid uuid := auth.uid();
  ids int[];
  att uuid;
begin
  if uid is null then raise exception 'Accesso richiesto' using errcode = '28000'; end if;
  -- massimo 10 tentativi nelle ultime 24 ore
  if (select count(*) from exam_attempts where user_id = uid and started_at > now() - interval '24 hours') >= 10 then
    raise exception 'Hai raggiunto il limite di 10 tentativi in 24 ore: riprova domani.' using errcode = 'P0001';
  end if;
  select array_agg(id) into ids from (select id from exam_questions order by random() limit 40) q;
  if ids is null then raise exception 'Domande d''esame non caricate (migrazione catalogo)' using errcode = 'P0001'; end if;
  insert into exam_attempts (user_id, question_ids) values (uid, ids) returning id into att;
  return jsonb_build_object(
    'attempt_id', att,
    'questions', (select jsonb_agg(jsonb_build_object('id', q.id, 'question', q.question, 'options', q.options) order by array_position(ids, q.id))
                  from exam_questions q where q.id = any (ids))
  );
end $$;

create or replace function public.submit_exam(p_attempt uuid, p_answers jsonb)
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  uid uuid := auth.uid();
  a exam_attempts;
  n_ok int := 0;
  n int;
  results jsonb;
begin
  if uid is null then raise exception 'Accesso richiesto' using errcode = '28000'; end if;
  select * into a from exam_attempts where id = p_attempt and user_id = uid for update;
  if not found then raise exception 'Tentativo non trovato' using errcode = 'P0001'; end if;
  if a.submitted_at is not null then raise exception 'Tentativo già consegnato' using errcode = 'P0001'; end if;
  if a.started_at < now() - interval '90 minutes' then raise exception 'Tempo scaduto: avvia un nuovo esame' using errcode = 'P0001'; end if;

  n := cardinality(a.question_ids);
  select count(*) into n_ok from exam_questions q
   where q.id = any (a.question_ids) and (p_answers ->> q.id::text) ~ '^\d+$' and (p_answers ->> q.id::text)::int = q.answer;

  select jsonb_agg(jsonb_build_object(
           'id', q.id,
           'correct', coalesce((p_answers ->> q.id::text) ~ '^\d+$' and (p_answers ->> q.id::text)::int = q.answer, false),
           'answer', q.answer, 'explanation', q.explanation) order by array_position(a.question_ids, q.id))
    into results from exam_questions q where q.id = any (a.question_ids);

  update exam_attempts set submitted_at = now(), score = round(100.0 * n_ok / n) where id = a.id;
  return jsonb_build_object('score', round(100.0 * n_ok / n), 'correct', n_ok, 'total', n, 'results', results);
end $$;

revoke all on function public.handle_new_user()        from public, anon, authenticated;
revoke all on function public.start_exam()             from public, anon, authenticated;
revoke all on function public.submit_exam(uuid, jsonb) from public, anon, authenticated;
grant execute on function public.start_exam()             to authenticated;
grant execute on function public.submit_exam(uuid, jsonb) to authenticated;
