-- NailX · regole di accesso (RLS)
-- Migrazione applicata al progetto Supabase; guida in docs/SUPABASE.md

-- Ognuna vede e modifica solo i propri dati
create policy "profilo: lettura propria" on public.profiles
  for select to authenticated using (id = auth.uid());
create policy "profilo: modifica propria" on public.profiles
  for update to authenticated using (id = auth.uid()) with check (id = auth.uid());
create policy "progressi: lettura propria" on public.progress
  for select to authenticated using (user_id = auth.uid());
create policy "progressi: inserimento proprio" on public.progress
  for insert to authenticated with check (user_id = auth.uid());
create policy "progressi: modifica propria" on public.progress
  for update to authenticated using (user_id = auth.uid()) with check (user_id = auth.uid());
create policy "catalogo lezioni: lettura" on public.course_lessons for select to authenticated using (true);
create policy "catalogo esercizi: lettura" on public.course_exercises for select to authenticated using (true);
create policy "tentativi: lettura propria" on public.exam_attempts
  for select to authenticated using (user_id = auth.uid());
create policy "attestato: lettura propria" on public.certificates
  for select to authenticated using (user_id = auth.uid());

-- il nome sull'attestato si cambia solo con issue_certificate(); la data privacy non è modificabile
revoke update on public.profiles from authenticated;
grant update (full_name) on public.profiles to authenticated;
