-- NailX · cancellazione account (GDPR)
-- Migrazione applicata al progetto Supabase; guida in docs/SUPABASE.md

-- Diritto all'oblio: l'utente autenticato cancella il proprio account e i dati collegati (cascade)
create or replace function public.delete_my_account()
returns void language plpgsql security definer set search_path = public, auth as $$
begin
  if auth.uid() is null then raise exception 'Accesso richiesto' using errcode = '28000'; end if;
  delete from auth.users where id = auth.uid();
end $$;

revoke all on function public.delete_my_account() from public, anon, authenticated;
grant execute on function public.delete_my_account() to authenticated;
