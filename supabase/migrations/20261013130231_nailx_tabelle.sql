-- NailX · tabelle e Row Level Security
-- Migrazione applicata al progetto Supabase; guida in docs/SUPABASE.md

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
-- Catalogo del corso (dati: migrazione …_nailx_catalogo.sql, generata da tools/build_supabase_seed.js)
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

-- exam_questions: nessuna policy e nessun permesso: le risposte non sono leggibili dal sito
revoke all on public.exam_questions from anon, authenticated;
