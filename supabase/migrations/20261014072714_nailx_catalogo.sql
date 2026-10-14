-- Generato da tools/build_supabase_seed.js: non modificare a mano.
-- Catalogo del corso NailX (lezioni, esercizi, domande d'esame).
-- catalogo: 83cb3e763a592dda

insert into public.exam_questions (id, module, question, options, answer, explanation) values
  (141, 'onicofagia', 'Su un''unghia a pinza dolorante l''onicotecnica:', '["Accentua la curva a C","Fa il pinching","Indirizza a medico o podologo","Applica acrilico spesso"]'::jsonb, 2, 'La deformità comprime i tessuti: non si forza.'),
  (145, 'onicofagia', 'Su un''unghia rosicchiata resta uno spazio tra lamina e cartina. Cosa succede?', '["Niente","Il prodotto cola sotto e crea uno scalino debole e \"mordibile\"","Il gel polimerizza più in fretta","La curva a C migliora"]'::jsonb, 1, 'La cartina deve essere a filo del bordo, anche se il bordo quasi non c''è.'),
  (177, 'arte-gare', 'La "vista a tunnel" valuta soprattutto:', '["La smile line","La curva a C","Il colore","La lucentezza"]'::jsonb, 1, 'Si guarda l''unghia dalla punta.'),
  (183, 'arte-gare', 'Nella scheda Nailympia 2026 French Twist 3 forme, quanto vale l''apex?', '["30 punti da solo","15 punti, valutato con la curva a C dallo stesso giudice","5 punti","Non è valutato"]'::jsonb, 1, 'Il giudice 3 assegna 15 punti alla curva a C e 15 all''apex: 30 in tutto.')
on conflict (id) do update set module = excluded.module, question = excluded.question, options = excluded.options,
  answer = excluded.answer, explanation = excluded.explanation;
