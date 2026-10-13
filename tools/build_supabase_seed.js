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

// Stato attuale del catalogo nel database = somma di tutte le migrazioni "catalogo" già scritte.
// La nuova migrazione contiene solo le righe nuove o cambiate e i "delete" delle righe tolte dal corso.
const TABLES = {
  course_lessons: {
    head: 'insert into public.course_lessons (key, minutes) values',
    tail: 'on conflict (key) do update set minutes = excluded.minutes;', col: 'key', num: false
  },
  course_exercises: {
    head: 'insert into public.course_exercises (id, title, n_checks, minutes) values',
    tail: 'on conflict (id) do update set title = excluded.title, n_checks = excluded.n_checks, minutes = excluded.minutes;', col: 'id', num: false
  },
  exam_questions: {
    head: 'insert into public.exam_questions (id, module, question, options, answer, explanation) values',
    tail: 'on conflict (id) do update set module = excluded.module, question = excluded.question, options = excluded.options,\n' +
      '  answer = excluded.answer, explanation = excluded.explanation;', col: 'id', num: true
  }
};
const rowKey = (line) => { const m = /^  \((\d+),|^  \('((?:[^']|'')*)'/.exec(line); return m ? (m[1] || m[2].replace(/''/g, "'")) : null; };
const state = {};
Object.keys(TABLES).forEach((t) => { state[t] = new Map(); });
for (const f of fs.readdirSync(DIR).filter((f) => /_nailx_catalogo\.sql$/.test(f)).sort()) {
  const sql = fs.readFileSync(path.join(DIR, f), 'utf8');
  for (const [t, cfg] of Object.entries(TABLES)) {
    const sec = (sql.split('insert into public.' + t + ' ')[1] || '').split('\non conflict')[0];
    sec.split('\n').slice(1).forEach((l) => { const k = rowKey(l); if (k !== null) state[t].set(k, l.replace(/,$/, '')); });
    for (const m of sql.matchAll(new RegExp('delete from public\\.' + t + ' where ' + cfg.col + ' in \\(([^;]*)\\);', 'g'))) {
      [...m[1].matchAll(/'((?:[^']|'')*)'|(\d+)/g)].forEach((x) => state[t].delete(x[2] || x[1].replace(/''/g, "'")));
    }
    for (const m of sql.matchAll(new RegExp('delete from public\\.' + t + ' where id > (\\d+);', 'g'))) {
      [...state[t].keys()].filter((k) => +k > +m[1]).forEach((k) => state[t].delete(k));
    }
  }
}

const want = { course_lessons: [], course_exercises: [], exam_questions: [] };
D.modules.forEach((m) => m.lessons.forEach((l) => want.course_lessons.push(`  (${q(m.id + '/' + l.id)}, ${l.min || 10})`)));
D.exercises.forEach((e) => {
  const min = parseInt((/(\d+)/.exec(e.time) || [0, 0])[1], 10);
  want.course_exercises.push(`  (${q(e.id)}, ${q(e.title)}, ${e.checks.length}, ${min})`);
});
let id = 0;
D.modules.forEach((m) => (D.quiz[m.id] || []).forEach((x) => {
  id++;
  want.exam_questions.push(`  (${id}, ${q(m.id)}, ${q(x.q)}, ${j(x.o)}, ${x.a}, ${q(x.e || '')})`);
}));

// impronta del catalogo completo (serve a capire se è cambiato qualcosa)
const full = Object.entries(TABLES).map(([t, c]) => c.head + '\n' + want[t].join(',\n') + '\n' + c.tail).join('\n\n');
let body = '';
for (const [t, cfg] of Object.entries(TABLES)) {
  const keys = new Set(want[t].map(rowKey));
  const changed = want[t].filter((l) => state[t].get(rowKey(l)) !== l);
  const gone = [...state[t].keys()].filter((k) => !keys.has(k));
  if (changed.length) body += cfg.head + '\n' + changed.join(',\n') + '\n' + cfg.tail + '\n';
  if (gone.length) body += `delete from public.${t} where ${cfg.col} in (${gone.map((k) => (cfg.num ? k : q(k))).join(', ')});\n`;
  if (changed.length || gone.length) body += '\n';
}
const lessons = want.course_lessons;

const hash = crypto.createHash('sha256').update(full).digest('hex').slice(0, 16);
const existing = fs.readdirSync(DIR).filter((f) => /_nailx_catalogo\.sql$/.test(f)).sort();
const last = existing.length ? fs.readFileSync(path.join(DIR, existing[existing.length - 1]), 'utf8') : '';
const nLessons = lessons.length;
if (last.includes('-- catalogo: ' + hash) || !body) {
  console.log(`Catalogo invariato (${nLessons} lezioni, ${D.exercises.length} esercizi, ${id} domande): nessuna nuova migrazione.`);
  process.exit(0);
}
const ts = process.env.NAILX_MIGRATION_VERSION || new Date().toISOString().replace(/[-:T]/g, '').slice(0, 14);
const name = `${ts}_nailx_catalogo.sql`;
fs.writeFileSync(path.join(DIR, name),
  '-- Generato da tools/build_supabase_seed.js: non modificare a mano.\n' +
  '-- Catalogo del corso NailX (lezioni, esercizi, domande d\'esame).\n' +
  '-- catalogo: ' + hash + '\n\n' + body.trimEnd() + '\n');
console.log(`Creata supabase/migrations/${name}: catalogo di ${nLessons} lezioni, ${D.exercises.length} esercizi, ${id} domande (solo le righe cambiate).`);
