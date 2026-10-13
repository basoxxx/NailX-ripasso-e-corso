-- NailX · rilascio e verifica pubblica dell'attestato
-- Migrazione applicata al progetto Supabase; guida in docs/SUPABASE.md

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

revoke all on function public.issue_certificate(text)  from public, anon, authenticated;
revoke all on function public.verify_certificate(text) from public, anon, authenticated;
grant execute on function public.issue_certificate(text)  to authenticated;
grant execute on function public.verify_certificate(text) to anon, authenticated;
