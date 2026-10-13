-- NailX · permessi sulle tabelle
-- Migrazione applicata al progetto Supabase; guida in docs/SUPABASE.md

-- Permessi espliciti per il sito (ruolo authenticated): i progetti Supabase recenti non li
-- concedono in automatico alle tabelle nuove. Le righe restano filtrate dalle regole RLS.
grant usage on schema public to anon, authenticated;
grant select on public.profiles to authenticated;
grant update (full_name) on public.profiles to authenticated;
grant select, insert, update on public.progress to authenticated;
grant select on public.course_lessons to authenticated;
grant select on public.course_exercises to authenticated;
grant select on public.exam_attempts to authenticated;
grant select on public.certificates to authenticated;
