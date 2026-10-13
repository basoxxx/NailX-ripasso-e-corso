# GDPR: cosa è fatto e cosa resta da fare

L'informativa è in [`privacy.html`](../privacy.html), compilata con titolare **Diego Basolo** e contatto
**diegobasolo@gmail.com**. Questo documento non è consulenza legale: per un'attività strutturata
è comunque consigliata una revisione da parte di un consulente privacy.

## Fatto

- **Informativa completa** (artt. 13-14): titolare, dati, finalità e basi giuridiche, conservazione,
  destinatari, trasferimenti extra-UE, video YouTube, cookie e archiviazione locale, età minima, diritti, reclamo al Garante.
- **Corso utilizzabile senza account** e senza invio di dati.
- **Accettazione dell'informativa** obbligatoria per creare l'account: versione e data registrate nel profilo,
  non modificabili dal browser; dichiarazione di età minima (14 anni).
- **Minimizzazione**: solo e-mail e, per l'attestato, il nome.
- **Foto degli esercizi** elaborate solo nel browser.
- **Nessun cookie di profilazione o analytics**; video YouTube caricati solo dopo il clic (youtube-nocookie.com).
- **Diritti** dalla pagina Account: *Scarica i miei dati* (JSON) ed *Elimina account* (cancellazione immediata).
- **Conservazione**: account inattivi da 24 mesi cancellati automaticamente (migrazione `…_nailx_pulizia.sql`).
- **Sicurezza**: Row Level Security, risposte d'esame non leggibili dal sito, verifica pubblica limitata ai dati dell'attestato.

## Da fare una volta (dalla dashboard di Supabase)

- [ ] Verifica che la **regione del progetto sia nell'Unione europea** (l'informativa lo dichiara).
      Se non lo è, scrivimelo e aggiorno il testo.
- [ ] Accetta/scarica il **Data Processing Addendum (DPA)** di Supabase e conservane una copia.
- [ ] Se configuri un **SMTP** esterno, conserva anche il suo DPA.
- [ ] Tieni un semplice **registro dei trattamenti** (art. 30): puoi copiare le tabelle dei punti 2, 3, 5 e 6 dell'informativa.

## Quando succede qualcosa

- **Richieste** (accesso, rettifica, revisione umana dell'esame…): rispondi entro un mese a diegobasolo@gmail.com.
- **Violazione dei dati**: se c'è rischio per le persone, notifica il Garante entro 72 ore (art. 33) e,
  nei casi gravi, avvisa le interessate (art. 34). Annota ogni incidente.
- **Modifiche all'informativa**: aggiorna versione e data in `privacy.html` **e** `privacyVersion`
  in `assets/js/config.js`; per modifiche sostanziali avvisa chi ha un account.
