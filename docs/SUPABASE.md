# Attivare l'area online (Supabase)

Senza questa configurazione il sito funziona comunque: i progressi restano nel browser e
l'attestato è "in autovalutazione". Con Supabase si attivano login via e-mail, progressi
sincronizzati, esame corretto dal server, attestato con QR code verificabile e area account (GDPR).

Il database è descritto da **migrazioni** in [`supabase/migrations/`](../supabase/migrations):

| File | Contenuto |
|---|---|
| `…_nailx_schema.sql` | tabelle, regole di sicurezza (RLS), esame, attestati, verifica, cancellazione account |
| `…_nailx_pulizia.sql` | cancellazione automatica degli account inattivi da 24 mesi (GDPR) |
| `…_nailx_catalogo.sql` | lezioni, esercizi e domande d'esame (generato da `tools/build_supabase_seed.js`) |

Le voci dei menu di Supabase e GitHub possono cambiare nome: se non trovi una voce, cercala nella loro documentazione.

## 1. Integrazione GitHub (applica il database da sola)

Hai già collegato il repository a Supabase. Controlla in **Supabase → Project Settings → Integrations → GitHub**:

- repository: `basoxxx/NailX-ripasso-e-corso`
- *Supabase directory / working directory*: `.` (la cartella `supabase/` è nella radice)
- *Production branch*: `main`
- **Deploy to production: attivo**

Da quel momento, ogni volta che una pull request viene unita su `main`, Supabase applica in automatico
le migrazioni nuove. Le migrazioni già applicate non vengono rieseguite.

> **Alternativa manuale** (se non vuoi attivare il deploy automatico): apri **SQL Editor** e incolla
> ed esegui i file di `supabase/migrations/` **in ordine di nome**, uno per volta.

## 2. Accesso via e-mail

1. **Authentication → Sign In / Providers**: provider **Email** attivo.
2. **Authentication → URL Configuration**:
   - *Site URL*: `https://basoxxx.github.io/NailX-ripasso-e-corso/`
   - *Redirect URLs*: `https://basoxxx.github.io/NailX-ripasso-e-corso/accedi.html`
3. *(Consigliato)* **Authentication → Emails → Magic Link**: e-mail in italiano, per esempio:

   ```html
   <h2>Accedi al corso NailX</h2>
   <p>Premi il pulsante per accedere al tuo account. Il link vale una sola volta.</p>
   <p><a href="{{ .ConfirmationURL }}">Accedi a NailX</a></p>
   <p>Se non hai chiesto tu l'accesso, ignora questa e-mail.</p>
   ```

4. **Prima di aprire alle allieve**: il servizio e-mail incluso in Supabase invia pochissime e-mail all'ora
   ed è pensato per le prove. Configura un **SMTP personalizzato** (*Authentication → Emails → SMTP Settings*).

Queste impostazioni non passano dall'integrazione GitHub: vanno fatte una volta dalla dashboard.

## 3. Collegare il sito (2 valori pubblici)

In **Supabase → Project Settings → API** (o *API Keys*) copia **Project URL** e la chiave **pubblica**
(*anon public* oppure *publishable*). Poi scegli **uno** dei due modi:

**A. Variabili del repository (consigliato, nessun file da modificare)**
GitHub → repository → **Settings → Secrets and variables → Actions → scheda Variables → New repository variable**:

| Nome | Valore |
|---|---|
| `SUPABASE_URL` | `https://xxxxxxxx.supabase.co` |
| `SUPABASE_ANON_KEY` | la chiave pubblica |

Poi **Actions → Deploy GitHub Pages → Run workflow** (o un qualsiasi push su `main`): il workflow scrive
la configurazione nel sito pubblicato.

**B. File di configurazione**: incolla i due valori in [`assets/js/config.js`](../assets/js/config.js) e fai commit.

> Sono valori pubblici: la sicurezza è garantita dalle regole del database. **Non usare mai la chiave
> `service_role` / secret**, né nelle variabili né nel codice.

## 4. Prova

1. Apri il sito → **Accedi** → inserisci la tua e-mail → apri il link ricevuto.
2. Segna qualche lezione, apri il sito da un altro dispositivo con la stessa e-mail: i progressi ci sono.
3. Completa le lezioni, supera l'**esame finale** (≥ 80%), registra l'**attestato**, inquadra il QR code.

## Manutenzione

- **Hai modificato lezioni, esercizi o quiz?** Esegui `node tools/build_supabase_seed.js`: se il catalogo
  è cambiato crea una nuova migrazione `…_nailx_catalogo.sql`. Committala: al merge su `main` Supabase la applica.
- **Revocare un attestato** (SQL Editor):
  `update public.certificates set revoked = true where code = 'NX-2026-XXXXXXXX';`
- **Pulizia account inattivi**: pianificata ogni domenica con `pg_cron` se disponibile; altrimenti esegui
  ogni tanto `select public.cleanup_inactive_accounts();` nel SQL Editor.
- **Progetti gratuiti in pausa**: Supabase mette in pausa i progetti gratuiti inattivi; in quel caso login e
  verifica non funzionano finché non riattivi il progetto dalla dashboard.

## Cosa garantisce (e cosa no)

- L'attestato si ottiene solo se il **server** verifica tutte le lezioni completate e un esame superato.
- L'esame è corretto sul server, non si può consegnare due volte; massimo 10 tentativi in 24 ore.
- Le domande d'esame sono le stesse dei quiz dei moduli: è un esame "a libro aperto".
- Il completamento delle lezioni è registrato dal sito (in automatico a fine lezione), non verificato da una persona.

## Test in locale (per sviluppatori)

```bash
PGHOST=/percorso/socket PGPORT=5432 PGUSER=postgres supabase/tests/run.sh
```

Applica un simulatore minimo di Supabase e tutte le migrazioni su un PostgreSQL locale, poi verifica
isolamento tra utenti, esame, attestato, verifica pubblica, limite tentativi, cancellazione e pulizia.
