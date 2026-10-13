# Attivare l'area online (Supabase)

Senza questa configurazione il sito funziona comunque: i progressi restano nel browser e
l'attestato è "in autovalutazione" (non verificabile). Con Supabase si attivano:

- **login via e-mail** con link magico (senza password);
- **progressi sincronizzati** su tutti i dispositivi;
- **esame finale corretto dal server** (le risposte non sono nel browser durante l'esame);
- **attestato registrato** con codice e **QR code**, verificabile da chiunque su `verifica.html`;
- **area account** con download dei propri dati ed eliminazione dell'account (GDPR).

Tempo richiesto: circa 15 minuti. Serve un account gratuito su [supabase.com](https://supabase.com).
Le voci di menu di Supabase possono cambiare nome nel tempo: se non trovi una voce, cercala nella documentazione di Supabase.

## 1. Crea il progetto

1. Accedi a Supabase e crea un **nuovo progetto**.
2. Scegli una **regione nell'Unione europea** (per esempio *Central EU – Frankfurt*): serve anche per la privacy.
3. Imposta una password del database e conservala in un posto sicuro (non serve al sito).

## 2. Crea le tabelle

1. Apri **SQL Editor → New query**.
2. Incolla tutto il contenuto di [`supabase/schema.sql`](../supabase/schema.sql) e premi **Run**.
3. Nuova query: incolla [`supabase/seed.sql`](../supabase/seed.sql) e premi **Run**.
   Carica lezioni, esercizi e le 89 domande d'esame.

## 3. Configura l'accesso via e-mail

1. **Authentication → Sign In / Providers**: verifica che il provider **Email** sia attivo.
2. **Authentication → URL Configuration**:
   - *Site URL*: l'indirizzo del sito, per esempio `https://basoxxx.github.io/NailX-ripasso-e-corso/`
   - *Redirect URLs*: aggiungi `https://basoxxx.github.io/NailX-ripasso-e-corso/accedi.html`
     (e, per le prove in locale, `http://localhost:8000/accedi.html`).
3. *(Consigliato)* **Authentication → Emails → Magic Link**: traduci l'e-mail in italiano, per esempio:

   ```html
   <h2>Accedi al corso NailX</h2>
   <p>Premi il pulsante per accedere al tuo account. Il link vale una sola volta.</p>
   <p><a href="{{ .ConfirmationURL }}">Accedi a NailX</a></p>
   <p>Se non hai chiesto tu l'accesso, ignora questa e-mail.</p>
   ```

4. **Importante per l'uso reale**: il servizio e-mail incluso in Supabase è pensato solo per le prove
   (invia pochissime e-mail all'ora). Prima di aprire il corso alle allieve configura un **SMTP personalizzato**
   (*Authentication → Emails → SMTP Settings*) con un fornitore di e-mail transazionali.

## 4. Collega il sito

1. Apri **Project Settings → API** (o *API Keys*) e copia:
   - **Project URL** (es. `https://abcdefghijklmno.supabase.co`);
   - la chiave **pubblica** (*anon public* oppure *publishable*).
2. Incollali in [`assets/js/config.js`](../assets/js/config.js):

   ```js
   window.NAILX_CONFIG = window.NAILX_CONFIG || {
     supabaseUrl: 'https://abcdefghijklmno.supabase.co',
     supabaseAnonKey: 'la-tua-chiave-pubblica',
     privacyVersion: '2026-10'
   };
   ```

3. Fai commit e push: GitHub Pages pubblica la nuova versione.

> La chiave pubblica può stare nel sito: la sicurezza è garantita dalle regole del database
> (ognuna vede solo i propri dati). **Non inserire mai la chiave `service_role` / secret**: dà accesso a tutto.

## 5. Prova

1. Apri il sito → **Accedi** → inserisci la tua e-mail → apri il link ricevuto.
2. Segna qualche lezione, apri il sito da un altro dispositivo con la stessa e-mail: i progressi ci sono.
3. Completa le lezioni, supera l'**esame finale** (≥ 80%), registra l'**attestato** e prova il QR code.

## Manutenzione

- **Hai modificato lezioni, esercizi o quiz?** Esegui `node tools/build_supabase_seed.js` e ricarica
  `supabase/seed.sql` nel SQL Editor. Gli attestati già rilasciati non cambiano.
- **Revocare un attestato** (SQL Editor):
  `update public.certificates set revoked = true where code = 'NX-2026-XXXXXXXX';`
- **Progetti gratuiti in pausa**: Supabase mette in pausa i progetti del piano gratuito dopo un periodo
  di inattività; in quel caso login e verifica non funzionano finché non riattivi il progetto dalla dashboard.
  Per un uso continuativo valuta un piano a pagamento.
- **Backup**: verifica la politica di backup del tuo piano e indicala nell'informativa privacy.

## Cosa garantisce (e cosa no)

- L'attestato si ottiene solo se il **server** verifica tutte le lezioni completate e un esame superato.
- L'esame è corretto sul server e non si può consegnare due volte; massimo 10 tentativi al giorno.
- Le domande d'esame sono le stesse dei quiz dei moduli: è un esame "a libro aperto",
  pensato per verificare lo studio, non un esame di Stato.
- Il completamento delle lezioni è dichiarato dall'allieva (non si può verificare che le abbia lette).

## Test in locale (per sviluppatori)

`supabase/tests/` contiene un simulatore minimo di Supabase e i test di sicurezza dello schema
(isolamento tra utenti, esame, attestato, verifica, cancellazione). Con un PostgreSQL locale:

```bash
PGHOST=/percorso/socket PGPORT=5432 PGUSER=postgres supabase/tests/run.sh
```
