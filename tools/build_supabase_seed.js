#!/usr/bin/env node
/* Genera supabase/seed.sql dal contenuto del corso (assets/js/data.js).
 * Uso: node tools/build_supabase_seed.js
 * Rieseguilo (e ricarica seed.sql su Supabase) ogni volta che cambi lezioni, esercizi o quiz.
 */
'use strict';
const fs = require('fs');
const path = require('path');

global.window = {};
require(path.join(__dirname, '..', 'assets', 'js', 'data.js'));
const D = global.window.NAILX;

const q = (v) => "'" + String(v).replace(/'/g, "''") + "'";
const j = (v) => q(JSON.stringify(v)) + '::jsonb';

let sql = '-- Generato da tools/build_supabase_seed.js: non modificare a mano.\n' +
  '-- Esegui dopo schema.sql (SQL Editor di Supabase).\n\nbegin;\n\n';

sql += 'delete from public.course_lessons;\n';
sql += 'insert into public.course_lessons (key, minutes) values\n' +
  D.modules.flatMap((m) => m.lessons.map((l) => `  (${q(m.id + '/' + l.id)}, ${l.min || 10})`)).join(',\n') + ';\n\n';

sql += 'delete from public.course_exercises;\n';
sql += 'insert into public.course_exercises (id, title, n_checks, minutes) values\n' +
  D.exercises.map((e) => {
    const min = parseInt((/(\d+)/.exec(e.time) || [0, 0])[1], 10);
    return `  (${q(e.id)}, ${q(e.title)}, ${e.checks.length}, ${min})`;
  }).join(',\n') + ';\n\n';

// Le domande d'esame mantengono id stabili: modulo + posizione
sql += 'delete from public.exam_questions;\n';
let id = 0;
const rows = [];
D.modules.forEach((m) => {
  (D.quiz[m.id] || []).forEach((x) => {
    id++;
    rows.push(`  (${id}, ${q(m.id)}, ${q(x.q)}, ${j(x.o)}, ${x.a}, ${q(x.e || '')})`);
  });
});
sql += 'insert into public.exam_questions (id, module, question, options, answer, explanation) values\n' + rows.join(',\n') + ';\n\n';
sql += 'commit;\n';

const out = path.join(__dirname, '..', 'supabase', 'seed.sql');
fs.writeFileSync(out, sql);
console.log(`seed.sql: ${D.modules.reduce((a, m) => a + m.lessons.length, 0)} lezioni, ${D.exercises.length} esercizi, ${id} domande`);
