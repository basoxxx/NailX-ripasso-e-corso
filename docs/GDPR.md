# Checklist GDPR per il titolare del sito

L'informativa è in [`privacy.html`](../privacy.html). È una **bozza**: va completata e,
idealmente, rivista da un consulente privacy. Questa checklist riassume cosa resta da fare.
Non è consulenza legale.

## Prima di attivare le registrazioni

- [ ] **Completa `privacy.html`**: sostituisci tutti i campi tra `[parentesi quadre]`:
  titolare, indirizzo, e-mail privacy, data, regione Supabase, tempi di conservazione, strumenti di trasferimento.
- [ ] **Regione UE** del progetto Supabase (vedi `docs/SUPABASE.md`).
- [ ] **Accordo con Supabase (DPA)**: verifica nella dashboard o sul sito di Supabase come accettare/scaricare
  il *Data Processing Addendum* e conservane una copia.
- [ ] **SMTP**: se usi un fornitore e-mail esterno, verifica il suo DPA e aggiungilo all'informativa.
- [ ] **Conservazione**: decidi cosa fare degli account inattivi (es. cancellazione dopo 24 mesi con preavviso)
  e indicalo nell'informativa. Se lo prevedi, ricordati di applicarlo davvero.
- [ ] **Registro dei trattamenti** (art. 30 GDPR): annota finalità, categorie di dati, destinatari,
  trasferimenti, tempi e misure di sicurezza. Le voci dell'informativa sono un buon punto di partenza.
- [ ] **Età minima**: il modulo di accesso chiede di dichiarare almeno 14 anni; se il tuo pubblico è solo
  maggiorenne puoi alzare il limite (testo in `assets/js/cloud.js` e nell'informativa).

## Già implementato nel sito

- Corso utilizzabile **senza account** e senza invio di dati.
- **Consenso informato all'account**: casella obbligatoria con link all'informativa; la versione accettata e la
  data vengono registrate nel profilo (non modificabili dal browser).
- **Minimizzazione**: si chiedono solo e-mail e, per l'attestato, il nome.
- **Foto degli esercizi** elaborate solo nel browser, mai caricate.
- **Nessun cookie di profilazione o analytics**; solo archiviazione locale tecnica (elencata nell'informativa).
- **Video YouTube** caricati solo dopo il clic, dal dominio `youtube-nocookie.com`.
- **Diritti degli interessati** dalla pagina Account: *Scarica i miei dati* (accesso/portabilità, JSON)
  ed *Elimina account* (cancellazione immediata di account, progressi, tentativi e attestato).
- **Sicurezza**: Row Level Security (ognuna vede solo i propri dati), risposte d'esame non leggibili dal sito,
  verifica pubblica che espone solo i dati stampati sull'attestato.

## Quando succede qualcosa

- **Richieste degli interessati** (rettifica, opposizione, revisione umana dell'esame…): rispondi entro un mese.
- **Violazione dei dati** (data breach): valuta il rischio e, se necessario, notifica il Garante entro 72 ore
  (art. 33) e, nei casi gravi, avvisa le persone coinvolte (art. 34). Tieni traccia di ogni incidente.
- **Modifiche all'informativa**: aggiorna la versione in `privacy.html` **e** `privacyVersion` in
  `assets/js/config.js`; per modifiche sostanziali avvisa chi ha un account.
