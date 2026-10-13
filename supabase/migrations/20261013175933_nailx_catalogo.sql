-- Generato da tools/build_supabase_seed.js: non modificare a mano.
-- Catalogo del corso NailX (lezioni, esercizi, domande d'esame).
-- catalogo: fef00c43607652e8

insert into public.exam_questions (id, module, question, options, answer, explanation) values
  (28, 'sistemi', 'Come indurisce l''acrilico?', '["In lampada UV","Per reazione chimica tra liquido e polvere, senza lampada","Con l''acetone","Con l''attivatore spray"]'::jsonb, 1, 'Il perossido di benzoile nella polvere e l''accelerante nel liquido avviano la reazione a temperatura ambiente.'),
  (80, 'cartina', 'Quanto è spesso, indicativamente, il bordo libero finito?', '["Come un foglio di carta","Sottile: circa come una carta di credito (0,8–1 mm)","5 mm","Non conta"]'::jsonb, 1, 'Più spesso si impiglia, più sottile si scheggia.')
on conflict (id) do update set module = excluded.module, question = excluded.question, options = excluded.options,
  answer = excluded.answer, explanation = excluded.explanation;
