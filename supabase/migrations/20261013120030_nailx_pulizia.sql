-- =====================================================================
-- NailX · conservazione dei dati (GDPR, informativa punto 5)
-- Gli account senza accessi da 24 mesi vengono cancellati insieme a
-- progressi, tentativi d'esame e attestato (cascade). Pianificazione
-- settimanale con pg_cron, se l'estensione è disponibile nel progetto.
-- =====================================================================

create or replace function public.cleanup_inactive_accounts()
returns integer language plpgsql security definer set search_path = public, auth as $$
declare n integer;
begin
  delete from auth.users u
   where coalesce(u.last_sign_in_at, u.created_at) < now() - interval '24 months';
  get diagnostics n = row_count;
  return n;
end $$;

revoke all on function public.cleanup_inactive_accounts() from public;
revoke all on function public.cleanup_inactive_accounts() from anon, authenticated;

do $$
begin
  if exists (select 1 from pg_available_extensions where name = 'pg_cron') then
    create extension if not exists pg_cron;
    perform cron.schedule('nailx-pulizia-account-inattivi', '17 3 * * 0', 'select public.cleanup_inactive_accounts()');
  else
    raise notice 'pg_cron non disponibile: esegui periodicamente select public.cleanup_inactive_accounts();';
  end if;
exception when others then
  raise notice 'Pianificazione con pg_cron non riuscita (%): esegui periodicamente select public.cleanup_inactive_accounts();', sqlerrm;
end $$;
