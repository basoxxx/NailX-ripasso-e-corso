#!/usr/bin/env bash
# Esegue i test dello schema su un PostgreSQL locale (non su Supabase):
# simulatore minimo di Supabase + tutte le migrazioni in ordine + test di sicurezza.
# Uso: PGHOST=/percorso/socket PGPORT=5432 PGUSER=postgres supabase/tests/run.sh
set -euo pipefail
cd "$(dirname "$0")/../.."
DB=nailx_test
psql -q -c "drop database if exists $DB" -c "create database $DB"
OUT=$(mktemp)
for f in supabase/tests/supabase_stub.sql $(ls supabase/migrations/*.sql | sort) supabase/tests/test.sql; do
  psql -q -d "$DB" -v ON_ERROR_STOP=1 -f "$f" >>"$OUT" 2>&1 || { cat "$OUT"; echo "FALLITO: $f"; exit 1; }
done
grep -E "OK" "$OUT"; echo "Tutti i test sono passati."
