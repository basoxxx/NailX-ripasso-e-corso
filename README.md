# NailX · Corso di ricostruzione unghie

Sito statico (HTML/CSS/JS, nessuna build) con un corso completo di ricostruzione unghie in italiano,
dal livello base all'avanzato:

- **16 moduli / 49 lezioni** (base → avanzato), incluse lezioni tutorial complete (gel e acrilico su cartina),
  onicofagia e unghie difficili, cover e colori, pedicure, nail art avanzata e gare: anatomia e patologie, igiene e normativa (HEMA, divieto TPO 2025, L. 1/1990),
  sistemi (gel, acrilico, polygel, semipermanente, fibra, lampade), attrezzatura, preparazione, tip,
  cartina e apex, limatura e forme, french/baby boomer/nail art, refill e rimozione, problemi e soluzioni,
  professione e business. Ogni lezione cita le fonti.
- **48 illustrazioni tutorial SVG** generate da `tools/gen_svg.py`, con sequenze passo-passo (gel, acrilico,
  semipermanente, soft gel tips, fibra, french, refill, limatura) e zoom al clic.
- **28 esercizi pratici** (con confronto tra la propria foto e la tavola, la foto resta sul dispositivo) con procedimento, auto-valutazione ed errori frequenti.
- **Quiz** per modulo + esame finale da 40 domande (soglia 80%).
- **Video YouTube** selezionati e verificati, caricati solo al clic.
- **Ripasso rapido**: flashcard, schede riassuntive stampabili, quiz a tempo.
- **Glossario** con ricerca; i termini sono spiegati direttamente nelle lezioni.
- **Attestato di fine corso** (`attestato.html`): si sblocca con tutte le lezioni completate e l'esame finale
  superato (≥ 80%); riporta nome, data, codice, esito dell'esame, ore stimate e, in una seconda pagina, il
  dettaglio di moduli, quiz ed esercizi svolti. Si stampa/salva in PDF o si scarica come PNG.
- **Stato del corso automatico**: lezioni completate a fine lettura, prossimo passo suggerito, stato dei moduli, percentuale sempre visibile.
- Progressi salvati nel browser (localStorage), tema chiaro/scuro, layout responsive.

## Area online (facoltativa): login e attestati verificabili

Con **Supabase** si attivano login via e-mail, progressi sincronizzati, esame corretto dal server e attestati
con codice e QR code verificabili su `verifica.html`. Il database è descritto dalle migrazioni in `supabase/migrations/`,
già applicate al progetto Supabase collegato (regione UE); il sito è collegato tramite `assets/js/config.js`.
Guida: [`docs/SUPABASE.md`](docs/SUPABASE.md). Privacy: `privacy.html` e [`docs/GDPR.md`](docs/GDPR.md).

## Pubblicare su GitHub Pages

1. Unisci il branch in `main`.
2. *Settings → Pages → Build and deployment → Source: **GitHub Actions***.
3. Il workflow `.github/workflows/pages.yml` pubblica il sito a ogni push su `main`.

In alternativa: *Source: Deploy from a branch*, cartella `/ (root)`.

## Sviluppo locale

```bash
python3 -m http.server 8000   # poi apri http://localhost:8000
python3 tools/gen_svg.py      # rigenera le illustrazioni in assets/img/
```

I contenuti (lezioni, esercizi, quiz, glossario) sono tutti in `assets/js/data.js`.
Dopo averli modificati esegui `node tools/build_supabase_seed.js`: se il catalogo è cambiato crea una nuova migrazione Supabase.

> Materiale didattico a scopo formativo: non sostituisce la formazione abilitante prevista dalla legge
> né il parere medico.
