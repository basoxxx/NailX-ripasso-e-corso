# NailX · Corso di ricostruzione unghie

Sito statico (HTML/CSS/JS, nessuna build) con un corso completo di ricostruzione unghie in italiano,
dal livello base all'avanzato:

- **12 moduli / 35 lezioni**: anatomia e patologie, igiene e normativa (HEMA, divieto TPO 2025, L. 1/1990),
  sistemi (gel, acrilico, polygel, semipermanente, fibra, lampade), attrezzatura, preparazione, tip,
  cartina e apex, limatura e forme, french/baby boomer/nail art, refill e rimozione, problemi e soluzioni,
  professione e business. Ogni lezione cita le fonti.
- **24 illustrazioni tutorial SVG** generate da `tools/gen_svg.py`.
- **18 esercizi pratici** con procedimento, auto-valutazione ed errori frequenti.
- **Quiz** per modulo + esame finale da 40 domande (soglia 80%).
- **Glossario** con ricerca.
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
