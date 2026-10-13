/* NailX – configurazione dell'area online (Supabase).
 * Lascia vuoti i campi per usare il sito solo in locale (progressi nel browser,
 * attestato non verificabile). Per attivare login, sincronizzazione e attestati
 * verificabili segui docs/SUPABASE.md e incolla qui i due valori PUBBLICI del progetto.
 * NON inserire mai la chiave "service_role": è segreta.
 */
window.NAILX_CONFIG = window.NAILX_CONFIG || {
  supabaseUrl: '',        // es. 'https://abcdefghijklmno.supabase.co'
  supabaseAnonKey: '',    // chiave "anon public" (Project Settings → API)
  privacyVersion: '2026-10' // aggiornala quando cambi l'informativa privacy
};
