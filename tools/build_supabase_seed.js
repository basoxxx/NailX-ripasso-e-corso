#!/usr/bin/env node
/* Genera la migrazione Supabase con il catalogo del corso (lezioni, esercizi, domande d'esame)
 * a partire da assets/js/data.js.
 *
 * Uso: node tools/build_supabase_seed.js
 *
 * Le migrazioni già applicate non vengono rieseguite: se il catalogo è cambiato lo script crea
 * una NUOVA migrazione (supabase/migrations/<timestamp>_nailx_catalogo.sql) che l'integrazione
 * GitHub di Supabase applicherà al prossimo merge su main. Se nulla è cambiato non fa niente.
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

let body = 'delete from public.course_lessons;\n';
body += 'insert into public.course_lessons (key, minutes) values\n' +
  D.modules.flatMap((m) => m.lessons.map((l) => `  (${q(m.id + '/' + l.id)}, ${l.min || 10})`)).join(',\n') + ';\n\n';
body += 'delete from public.course_exercises;\n';
body += 'insert into public.course_exercises (id, title, n_checks, minutes) values\n' +
  D.exercises.map((e) => {
    const min = parseInt((/(\d+)/.exec(e.time) || [0, 0])[1], 10);
    return `  (${q(e.id)}, ${q(e.title)}, ${e.checks.length}, ${min})`;
  }).join(',\n') + ';\n\n';
let id = 0;
const rows = [];
D.modules.forEach((m) => (D.quiz[m.id] || []).forEach((x) => {
  id++;
  rows.push(`  (${id}, ${q(m.id)}, ${q(x.q)}, ${j(x.o)}, ${x.a}, ${q(x.e || '')})`);
}));
body += 'delete from public.exam_questions;\n';
body += 'insert into public.exam_questions (id, module, question, options, answer, explanation) values\n' + rows.join(',\n') + ';\n';

const hash = crypto.createHash('sha256').update(body).digest('hex').slice(0, 16);
const existing = fs.readdirSync(DIR).filter((f) => /_nailx_catalogo\.sql$/.test(f)).sort();
const last = existing.length ? fs.readFileSync(path.join(DIR, existing[existing.length - 1]), 'utf8') : '';
const lessons = D.modules.reduce((a, m) => a + m.lessons.length, 0);
if (last.includes('-- catalogo: ' + hash)) {
  console.log(`Catalogo invariato (${lessons} lezioni, ${D.exercises.length} esercizi, ${id} domande): nessuna nuova migrazione.`);
  process.exit(0);
}
const ts = new Date().toISOString().replace(/[-:T]/g, '').slice(0, 14);
const name = `${ts}_nailx_catalogo.sql`;
fs.writeFileSync(path.join(DIR, name),
  '-- Generato da tools/build_supabase_seed.js: non modificare a mano.\n' +
  '-- Catalogo del corso NailX (sostituisce integralmente quello precedente).\n' +
  '-- catalogo: ' + hash + '\n\n' + body);
console.log(`Creata supabase/migrations/${name}: ${lessons} lezioni, ${D.exercises.length} esercizi, ${id} domande.`);
