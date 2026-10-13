#!/usr/bin/env node
/* Genera la migrazione Supabase con il catalogo del corso (lezioni, esercizi, domande d'esame)
 * a partire da assets/js/data.js.
 *
 * Uso: node tools/build_supabase_seed.js
 *
 * Le migrazioni già applicate non vengono rieseguite: se il catalogo è cambiato lo script crea
 * una NUOVA migrazione (supabase/migrations/<timestamp>_nailx_catalogo.sql) da applicare al
 * progetto (SQL Editor di Supabase o connettore). Se nulla è cambiato non fa niente.
 * Le righe vengono aggiornate (upsert) e quelle non più presenti nel corso rimosse.
 */
'use strict';
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

global.window = {};
require(path.join(__dirname, '..', 'assets', 'js', 'data.js'));
const D = global.window.NAILX;
const DIR = path.join(__dirname, '..', 'supabase', 'migrations');

const q = (v) => "'" + String(v).replace(/'/g, "''") + "'";
const j = (v) => q(JSON.stringify(v)) + '::jsonb';

// catalogo precedente: le righe da cancellare si calcolano rispetto all'ultima migrazione,
// così una migrazione contiene un "delete" solo quando qualcosa è stato davvero tolto dal corso
const prevFiles = fs.readdirSync(DIR).filter((f) => /_nailx_catalogo\.sql$/.test(f)).sort();
const prev = prevFiles.length ? fs.readFileSync(path.join(DIR, prevFiles[prevFiles.length - 1]), 'utf8') : '';
const section = (table) => (prev.split('insert into public.' + table)[1] || '').split('on conflict')[0];
const prevKeys = (table) => [...section(table).matchAll(/^  \('((?:[^']|'')*)'/gm)].map((m) => m[1].replace(/''/g, "'"));
const prevMaxQ = Math.max(0, ...[...section('exam_questions').matchAll(/^  \((\d+),/gm)].map((m) => +m[1]));

const lessons = D.modules.flatMap((m) => m.lessons.map((l) => [m.id + '/' + l.id, l.min || 10]));
const goneLessons = prevKeys('course_lessons').filter((k) => !lessons.some(([x]) => x === k));
let body = 'insert into public.course_lessons (key, minutes) values\n' +
  lessons.map(([k, m]) => `  (${q(k)}, ${m})`).join(',\n') + '\non conflict (key) do update set minutes = excluded.minutes;\n' +
  (goneLessons.length ? `delete from public.course_lessons where key in (${goneLessons.map(q).join(', ')});\n` : '') + '\n';
body += 'insert into public.course_exercises (id, title, n_checks, minutes) values\n' +
  D.exercises.map((e) => {
    const min = parseInt((/(\d+)/.exec(e.time) || [0, 0])[1], 10);
    return `  (${q(e.id)}, ${q(e.title)}, ${e.checks.length}, ${min})`;
  }).join(',\n') + '\non conflict (id) do update set title = excluded.title, n_checks = excluded.n_checks, minutes = excluded.minutes;\n';
const goneEx = prevKeys('course_exercises').filter((k) => !D.exercises.some((e) => e.id === k));
body += (goneEx.length ? `delete from public.course_exercises where id in (${goneEx.map(q).join(', ')});\n` : '') + '\n';
let id = 0;
const rows = [];
D.modules.forEach((m) => (D.quiz[m.id] || []).forEach((x) => {
  id++;
  rows.push(`  (${id}, ${q(m.id)}, ${q(x.q)}, ${j(x.o)}, ${x.a}, ${q(x.e || '')})`);
}));
body += 'insert into public.exam_questions (id, module, question, options, answer, explanation) values\n' + rows.join(',\n') +
  '\non conflict (id) do update set module = excluded.module, question = excluded.question, options = excluded.options,\n' +
  '  answer = excluded.answer, explanation = excluded.explanation;\n' +
  (prevMaxQ > id ? `delete from public.exam_questions where id > ${id};\n` : '');

const hash = crypto.createHash('sha256').update(body).digest('hex').slice(0, 16);
const existing = fs.readdirSync(DIR).filter((f) => /_nailx_catalogo\.sql$/.test(f)).sort();
const last = existing.length ? fs.readFileSync(path.join(DIR, existing[existing.length - 1]), 'utf8') : '';
const nLessons = lessons.length;
if (last.includes('-- catalogo: ' + hash)) {
  console.log(`Catalogo invariato (${nLessons} lezioni, ${D.exercises.length} esercizi, ${id} domande): nessuna nuova migrazione.`);
  process.exit(0);
}
const ts = process.env.NAILX_MIGRATION_VERSION || new Date().toISOString().replace(/[-:T]/g, '').slice(0, 14);
const name = `${ts}_nailx_catalogo.sql`;
fs.writeFileSync(path.join(DIR, name),
  '-- Generato da tools/build_supabase_seed.js: non modificare a mano.\n' +
  '-- Catalogo del corso NailX (lezioni, esercizi, domande d\'esame).\n' +
  '-- catalogo: ' + hash + '\n\n' + body);
console.log(`Creata supabase/migrations/${name}: ${nLessons} lezioni, ${D.exercises.length} esercizi, ${id} domande.`);
