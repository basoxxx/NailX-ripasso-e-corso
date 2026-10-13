-- =====================================================================
-- NailX · schema (migrazione Supabase)
-- Applicata in automatico dall'integrazione GitHub di Supabase ("Deploy to production"),
-- oppure a mano incollandola nel SQL Editor. Guida: docs/SUPABASE.md
-- =====================================================================

-- ---------------------------------------------------------------------
-- Profili: uno per utente, creato automaticamente alla registrazione
-- ---------------------------------------------------------------------
create table if not exists public.profiles (
  id                  uuid primary key references auth.users (id) on delete cascade,
  full_name           text check (full_name is null or char_length(full_name) between 3 and 60),
  privacy_version     text,
  privacy_accepted_at timestamptz,
  created_at          timestamptz not null default now()
);

-- Progressi del corso (lezioni, checklist esercizi, quiz di modulo, flashcard…)
-- salvati come documento JSON, sincronizzato dal sito.
create table if not exists public.progress (
  user_id    uuid primary key references auth.users (id) on delete cascade,
  data       jsonb not null default '{}'::jsonb check (pg_column_size(data) < 200000),
  updated_at timestamptz not null default now()
);

-- ---------------------------------------------------------------------
-- Catalogo del corso (generato da tools/build_supabase_seed.js → seed.sql)
-- ---------------------------------------------------------------------
create table if not exists public.course_lessons (
  key     text primary key,          -- "modulo/lezione"
  minutes int  not null default 10
);

create table if not exists public.course_exercises (
  id       text primary key,
  title    text not null,
  n_checks int  not null,
  minutes  int  not null default 0
);

-- Domande dell'esame finale: le risposte NON sono leggibili dal sito,
-- la correzione avviene solo nella funzione submit_exam().
create table if not exists public.exam_questions (
  id          int primary key,
  module      text not null,
  question    text not null,
  options     jsonb not null,
  answer      smallint not null,
  explanation text
);

create table if not exists public.exam_attempts (
  id           uuid primary key default gen_random_uuid(),
  user_id      uuid not null references auth.users (id) on delete cascade,
  question_ids int[] not null,
  started_at   timestamptz not null default now(),
  submitted_at timestamptz,
  score        int
);
create index if not exists exam_attempts_user_idx on public.exam_attempts (user_id, started_at desc);

create table if not exists public.certificates (
  code          text primary key,
  user_id       uuid not null unique references auth.users (id) on delete cascade,
  full_name     text not null,
  issued_at     timestamptz not null default now(),
  updated_at    timestamptz not null default now(),
  final_score   int  not null,
  lessons_done  int  not null,
  lessons_total int  not null,
  exercises     jsonb not null default '[]'::jsonb,   -- [{id,title}]
  module_quiz   jsonb not null default '{}'::jsonb,   -- {modulo: punteggio}
  hours         int  not null,
  revoked       boolean not null default false
);

-- ---------------------------------------------------------------------
-- Row Level Security: ognuno vede e modifica solo i propri dati
-- ---------------------------------------------------------------------
alter table public.profiles         enable row level security;
alter table public.progress         enable row level security;
alter table public.course_lessons   enable row level security;
alter table public.course_exercises enable row level security;
alter table public.exam_questions   enable row level security;
alter table public.exam_attempts    enable row level security;
alter table public.certificates     enable row level security;

drop policy if exists "profilo: lettura propria" on public.profiles;
create policy "profilo: lettura propria" on public.profiles
  for select to authenticated using (id = auth.uid());
drop policy if exists "profilo: modifica propria" on public.profiles;
create policy "profilo: modifica propria" on public.profiles
  for update to authenticated using (id = auth.uid()) with check (id = auth.uid());

drop policy if exists "progressi: lettura propria" on public.progress;
create policy "progressi: lettura propria" on public.progress
  for select to authenticated using (user_id = auth.uid());
drop policy if exists "progressi: inserimento proprio" on public.progress;
create policy "progressi: inserimento proprio" on public.progress
  for insert to authenticated with check (user_id = auth.uid());
drop policy if exists "progressi: modifica propria" on public.progress;
create policy "progressi: modifica propria" on public.progress
  for update to authenticated using (user_id = auth.uid()) with check (user_id = auth.uid());

drop policy if exists "catalogo lezioni: lettura" on public.course_lessons;
create policy "catalogo lezioni: lettura" on public.course_lessons for select to authenticated using (true);
drop policy if exists "catalogo esercizi: lettura" on public.course_exercises;
create policy "catalogo esercizi: lettura" on public.course_exercises for select to authenticated using (true);

drop policy if exists "tentativi: lettura propria" on public.exam_attempts;
create policy "tentativi: lettura propria" on public.exam_attempts
  for select to authenticated using (user_id = auth.uid());

drop policy if exists "attestato: lettura propria" on public.certificates;
create policy "attestato: lettura propria" on public.certificates
  for select to authenticated using (user_id = auth.uid());

-- exam_questions: nessuna policy e nessun permesso → nessun accesso diretto dal sito.
revoke all on public.exam_questions from anon, authenticated;
-- certificates / exam_attempts: scritture solo tramite le funzioni qui sotto.

-- Il nome sull'attestato si cambia solo con issue_certificate();
-- la data di accettazione privacy non può essere falsificata dal client.
revoke update on public.profiles from authenticated;
grant update (full_name) on public.profiles to authenticated;

-- ---------------------------------------------------------------------
-- Profilo creato alla registrazione (accettazione privacy dai metadati)
-- ---------------------------------------------------------------------
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

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users for each row execute function public.handle_new_user();

-- ---------------------------------------------------------------------
-- Esame finale corretto dal server
-- ---------------------------------------------------------------------
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
  if ids is null then raise exception 'Domande d''esame non caricate (seed.sql)' using errcode = 'P0001'; end if;
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

-- ---------------------------------------------------------------------
-- Rilascio dell'attestato: i requisiti sono verificati qui, non nel browser
-- ---------------------------------------------------------------------
create or replace function public.issue_certificate(p_full_name text)
returns public.certificates language plpgsql security definer set search_path = public as $$
declare
  uid uuid := auth.uid();
  name text := regexp_replace(btrim(coalesce(p_full_name, '')), '\s+', ' ', 'g');
  pdata jsonb;
  total int; done int; best int;
  ex jsonb; mins int; mq jsonb;
  c certificates;
  new_code text;
begin
  if uid is null then raise exception 'Accesso richiesto' using errcode = '28000'; end if;
  if char_length(name) < 3 or char_length(name) > 60 then
    raise exception 'Il nome deve avere tra 3 e 60 caratteri' using errcode = 'P0001';
  end if;

  select coalesce(data, '{}'::jsonb) into pdata from progress where user_id = uid;
  pdata := coalesce(pdata, '{}'::jsonb);

  select count(*) into total from course_lessons;
  select count(*) into done from course_lessons l where (pdata -> 'lessons') ? l.key;
  if total = 0 or done < total then
    raise exception 'Requisito mancante: lezioni completate % su %', done, total using errcode = 'P0001';
  end if;

  select max(score) into best from exam_attempts where user_id = uid and submitted_at is not null;
  if coalesce(best, 0) < 80 then
    raise exception 'Requisito mancante: esame finale con almeno l''80%% (miglior risultato: %)', coalesce(best, 0) using errcode = 'P0001';
  end if;

  -- esercizi con checklist completa al 100%
  select coalesce(jsonb_agg(jsonb_build_object('id', e.id, 'title', e.title) order by e.id), '[]'::jsonb),
         coalesce(sum(e.minutes), 0)
    into ex, mins
    from course_exercises e
   where jsonb_typeof(pdata -> 'checks' -> e.id) = 'array'
     and (select count(*) from jsonb_array_elements(pdata -> 'checks' -> e.id) v where v = 'true'::jsonb) >= e.n_checks;

  select coalesce(jsonb_object_agg(k, v), '{}'::jsonb) into mq
    from jsonb_each(coalesce(pdata -> 'quiz', '{}'::jsonb)) as t(k, v)
   where k <> 'final' and jsonb_typeof(v) = 'number';

  mins := mins + (select coalesce(sum(minutes), 0) from course_lessons);

  update profiles set full_name = name where id = uid;

  select * into c from certificates where user_id = uid;
  if found then
    update certificates
       set full_name = name, final_score = greatest(final_score, best), lessons_done = done, lessons_total = total,
           exercises = ex, module_quiz = mq, hours = greatest(1, round(mins / 60.0)), updated_at = now()
     where user_id = uid returning * into c;
  else
    loop
      new_code := 'NX-' || to_char(now(), 'YYYY') || '-' || upper(substr(replace(gen_random_uuid()::text, '-', ''), 1, 8));
      exit when not exists (select 1 from certificates where code = new_code);
    end loop;
    insert into certificates (code, user_id, full_name, final_score, lessons_done, lessons_total, exercises, module_quiz, hours)
    values (new_code, uid, name, best, done, total, ex, mq, greatest(1, round(mins / 60.0)))
    returning * into c;
  end if;
  return c;
end $$;

-- Verifica pubblica: espone solo i dati stampati sull'attestato
create or replace function public.verify_certificate(p_code text)
returns jsonb language sql stable security definer set search_path = public as $$
  select case when c.code is null then jsonb_build_object('valid', false)
  else jsonb_build_object(
    'valid', not c.revoked, 'revoked', c.revoked, 'code', c.code, 'full_name', c.full_name,
    'issued_at', c.issued_at, 'final_score', c.final_score, 'lessons_done', c.lessons_done,
    'lessons_total', c.lessons_total, 'hours', c.hours,
    'exercises', (select coalesce(jsonb_agg(x -> 'title'), '[]'::jsonb) from jsonb_array_elements(c.exercises) x))
  end
  from (select 1) d left join certificates c on c.code = upper(btrim(p_code));
$$;

-- Diritto all'oblio: l'utente cancella account e tutti i dati collegati
create or replace function public.delete_my_account()
returns void language plpgsql security definer set search_path = public, auth as $$
begin
  if auth.uid() is null then raise exception 'Accesso richiesto' using errcode = '28000'; end if;
  delete from auth.users where id = auth.uid();
end $$;

-- Permessi sulle funzioni
revoke all on function public.start_exam()                 from public;
revoke all on function public.submit_exam(uuid, jsonb)     from public;
revoke all on function public.issue_certificate(text)      from public;
revoke all on function public.delete_my_account()          from public;
revoke all on function public.verify_certificate(text)     from public;
revoke all on function public.handle_new_user()            from public;
grant execute on function public.start_exam()             to authenticated;
grant execute on function public.submit_exam(uuid, jsonb) to authenticated;
grant execute on function public.issue_certificate(text)  to authenticated;
grant execute on function public.delete_my_account()      to authenticated;
grant execute on function public.verify_certificate(text) to anon, authenticated;
