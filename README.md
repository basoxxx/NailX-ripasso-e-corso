# NailX · Corso di ricostruzione unghie

Sito statico (HTML/CSS/JS, nessuna build) con un corso completo di ricostruzione unghie in italiano,
dal livello base all'avanzato:

- **12 moduli / 37 lezioni**, incluse due lezioni tutorial complete (gel e acrilico su cartina): anatomia e patologie, igiene e normativa (HEMA, divieto TPO 2025, L. 1/1990),
  sistemi (gel, acrilico, polygel, semipermanente, fibra, lampade), attrezzatura, preparazione, tip,
  cartina e apex, limatura e forme, french/baby boomer/nail art, refill e rimozione, problemi e soluzioni,
  professione e business. Ogni lezione cita le fonti.
- **40 illustrazioni tutorial SVG** generate da `tools/gen_svg.py`, con sequenze passo-passo (gel, acrilico,
  semipermanente, soft gel tips, fibra, french, refill, limatura) e zoom al clic.
- **22 esercizi pratici** con procedimento, auto-valutazione ed errori frequenti.
- **Quiz** per modulo + esame finale da 40 domande (soglia 80%).
- **Glossario** con ricerca.
- **Attestato di fine corso** (`attestato.html`): si sblocca con tutte le lezioni completate e l'esame finale
  superato (≥ 80%); riporta nome, data, codice, esito dell'esame, ore stimate e, in una seconda pagina, il
  dettaglio di moduli, quiz ed esercizi svolti. Si stampa/salva in PDF o si scarica come PNG.
- Progressi salvati nel browser (localStorage), tema chiaro/scuro, layout responsive.

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

> Materiale didattico a scopo formativo: non sostituisce la formazione abilitante prevista dalla legge
> né il parere medico.
