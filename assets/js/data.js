/* NailX – contenuti del corso.
 * Struttura: modules[] → lessons[] (html), exercises[], quiz{moduleId: [...]}, glossary[].
 * Per aggiungere una lezione basta inserire un oggetto nell'array "lessons" del modulo.
 */
(function () {
  'use strict';
  function F(src, cap) {
    return '<figure><img src="assets/img/' + src + '" alt="' + cap.replace(/"/g, '&quot;') + '" loading="lazy"><figcaption>' + cap + '</figcaption></figure>';
  }
  function B(type, title, body) {
    return '<div class="box ' + type + '"><strong class="t">' + title + '</strong>' + body + '</div>';
  }

  var modules = [
    /* ------------------------------------------------------------------ 1 */
    {
      id: 'anatomia', summary: ["La matrice produce la lamina: un danno può essere permanente.", "Si rimuove solo la cuticola (morta); eponichio e iponichio sono vivi e si proteggono.", "Il punto di stress è dove il bordo libero si stacca dal letto: lì sopra va l'apex.", "L'unghia cresce circa 3 mm al mese: refill ogni 3–4 settimane.", "Micosi, paronichia, onicolisi, macchia verde, banda scura nuova: non lavorare e indirizzare al medico."], n: 1, level: 'base', title: 'Anatomia e patologie dell\'unghia',
      desc: 'Com\'è fatta l\'unghia, come cresce e quando non si deve lavorare.',
      lessons: [
        {
          id: 'struttura', simple: "L'unghia che vedi è una \"piastrella\" dura che nasce da una radice nascosta sotto la pelle (la matrice). Proteggi sempre la radice e la pelle intorno.", title: 'Struttura dell\'unghia', min: 8,
          html: `
<p>Conoscere l'anatomia serve a capire <strong>dove</strong> appoggiare il prodotto, <strong>dove</strong> costruire la struttura e quali zone non vanno mai toccate.</p>
${F('anatomia-alto.svg', 'Le parti visibili dell\'unghia, vista dall\'alto.')}
${F('anatomia-sezione.svg', 'Sezione laterale: matrice, letto, lamina e iponichio.')}
<h2>Le parti principali</h2>
<table>
<tr><th>Parte</th><th>Cos'è</th><th>Cosa significa per l'onicotecnica</th></tr>
<tr><td><strong>Matrice</strong></td><td>Tessuto vivo che produce la lamina. Si trova sotto la piega prossimale; la <em>lunula</em> ne è la parte visibile.</td><td>Un danno alla matrice (pressione, fresa sulla zona cuticolare) può deformare l'unghia <strong>per sempre</strong>.</td></tr>
<tr><td><strong>Lamina ungueale</strong></td><td>Cheratina dura, senza nervi né vasi. Isola il letto dal calore.</td><td>Se viene assottigliata con la lima isola meno: aumenta il rischio di <em>picco di calore</em> in lampada.</td></tr>
<tr><td><strong>Letto ungueale</strong></td><td>Tessuto molto vascolarizzato su cui scorre la lamina.</td><td>Mai forzare il distacco della lamina (curva a C troppo stretta, leve in rimozione).</td></tr>
<tr><td><strong>Iponichio</strong></td><td>Cresta di pelle sotto il bordo libero: barriera contro i patogeni.</td><td>Non va mai spinto né raschiato.</td></tr>
<tr><td><strong>Eponichio</strong></td><td>Piega di pelle <em>viva</em> alla base dell'unghia.</td><td>Non si taglia: si arretra con delicatezza.</td></tr>
<tr><td><strong>Cuticola</strong></td><td>Pellicina <em>morta</em> che si stacca dall'eponichio e aderisce alla lamina.</td><td>Va rimossa: se resta sulla lamina (pterigio) è la prima causa di sollevamento.</td></tr>
<tr><td><strong>Pieghe e solchi laterali</strong></td><td>La pelle ai lati della lamina.</td><td>Il prodotto non deve mai toccarle.</td></tr>
<tr><td><strong>Bordo libero</strong></td><td>La parte di lamina che sporge oltre il polpastrello.</td><td>Va sempre <em>sigillato</em> con il prodotto.</td></tr>
<tr><td><strong>Punto di stress</strong></td><td>Il punto in cui il bordo libero si stacca dal letto (ai lati, sulla linea del sorriso).</td><td>È lì sopra che va costruito l'<strong>apex</strong>.</td></tr>
</table>
${B('tip', 'Da ricordare', 'Si rimuove solo ciò che è morto (cuticola). Tutto ciò che è vivo (eponichio, iponichio, pieghe) si protegge.')}
`,
          sources: ['https://www.my-personaltrainer.it/fisiologia/unghie.html']
        },
        {
          id: 'crescita', title: 'Crescita e tempi di ricrescita', min: 4,
          html: `
<p>L'unghia della mano cresce in media <strong>circa 0,1 mm al giorno</strong>, cioè <strong>circa 3 mm al mese</strong> (i valori normali vanno da circa 1,8 a 4,5 mm/mese). In un anno sono circa 3,6 cm. Le unghie dei piedi crescono più lentamente, a meno della metà della velocità (circa 1,6 mm al mese).</p>
<h2>Perché ci interessa</h2>
<ul>
<li>Dopo <strong>3–4 settimane</strong> compare una fascia di ricrescita alla base e l'apex si è spostato in avanti.</li>
<li>Il peso della ricostruzione non è più bilanciato sopra il punto di stress: aumentano rotture e sollevamenti.</li>
<li>Per questo si programma il <strong>refill</strong> (riempimento) ogni 3–4 settimane: lo vedremo nel modulo 10.</li>
</ul>
${F('refill.svg', 'La ricrescita sposta in avanti l\'apex: per questo serve il refill.')}
${B('info', 'Curiosità', 'Alcuni siti italiani riportano "365 mm all\'anno": è un errore. Il valore corretto è circa 36 mm all\'anno.')}
`,
          sources: ['https://qualcherisposta.it/quanto-tempo-per-ricrescita-unghie']
        },
        {
          id: 'controindicazioni', simple: "Se l'unghia sembra malata, infiammata o cambia colore, non si lavora: si consiglia il medico.", title: 'Patologie e controindicazioni', min: 7,
          html: `
<p>L'onicotecnica <strong>non fa diagnosi</strong>, ma deve riconoscere i segnali che impongono di <strong>non lavorare</strong> e di indirizzare la cliente al medico (dermatologo o podologo).</p>
<table>
<tr><th>Condizione</th><th>Come si riconosce</th><th>Cosa fare</th></tr>
<tr><td><strong>Onicomicosi</strong> (micosi)</td><td>Unghia ispessita, opaca, giallastra o friabile.</td><td>Controindicazione assoluta: è contagiosa. Rifiuta il servizio, disinfetta tutto ciò che è stato toccato, invia allo specialista.</td></tr>
<tr><td><strong>Paronichia</strong></td><td>Infezione attorno all'unghia: rossore, gonfiore, dolore, pus.</td><td>Non lavorare, mai spremere. Invia subito al medico.</td></tr>
<tr><td><strong>Onicolisi</strong></td><td>La lamina si stacca dal letto (zona biancastra).</td><td>Se la causa non è nota, sospendi fino al parere medico: nello spazio si accumulano umidità e germi.</td></tr>
<tr><td><strong>Macchia verde</strong> sotto la ricostruzione</td><td>Chiazza verde/scura, spesso sotto un sollevamento.</td><td>È un'infezione batterica (Pseudomonas), non "muffa". Rimuovi il prodotto e invia al medico.</td></tr>
<tr><td><strong>Banda scura nuova</strong> sulla lamina</td><td>Striscia bruna/nera longitudinale comparsa da poco.</td><td>Segnala subito al medico (può essere un segno da valutare con urgenza).</td></tr>
<tr><td>Altre</td><td>Unghia incarnita infiammata, ferite aperte, eczema/dermatite in corso, allergia nota agli acrilati.</td><td>Non lavorare sulla zona; per l'allergia non usare prodotti acrilici/gel.</td></tr>
</table>
${B('warn', 'Documenta sempre', 'Sulla scheda cliente annota data, cosa hai osservato, il servizio rifiutato e il consiglio di rivolgersi al medico.')}
`,
          sources: ['https://open-exam-prep.com/study-guides/ks-nail-technician/nail-skin-science/nail-diseases-contraindications',
            'https://open-exam-prep.com/study-guides/mn-nail-technician/nail-disorders-diseases-assessment/nail-diseases-infections-referrals']
        }
      ]
    },
    /* ------------------------------------------------------------------ 2 */
    {
      id: 'igiene', summary: ["Detersione → disinfezione → sterilizzazione (autoclave classe B, con registro).", "Lime in carta e buffer sono monouso.", "DPI: nitrile, FFP2, occhiali, aspiratore da tavolo; ventilare.", "HEMA solo per uso professionale (Reg. UE 2020/1682); TPO vietato dal 1/9/2025 (Reg. UE 2025/877).", "Il prodotto non polimerizzato non deve mai toccare la pelle.", "In Italia serve la qualifica di estetista (L. 1/1990) e la SCIA per lavorare in proprio."], n: 2, level: 'base', title: 'Igiene, sicurezza e normativa',
      desc: 'Sanificare, disinfettare, sterilizzare; DPI, allergie e regole UE e italiane.',
      lessons: [
        {
          id: 'livelli', title: 'Sanificazione, disinfezione, sterilizzazione', min: 6,
          html: `
${F('igiene.svg', 'I tre livelli di trattamento igienico.')}
<ul>
<li><strong>Detersione e sanificazione</strong>: tolgono lo sporco visibile e riducono la carica microbica. Si usano su mani, superfici e strumenti prima degli altri passaggi.</li>
<li><strong>Disinfezione</strong>: con prodotti chimici elimina la maggior parte dei patogeni. Per strumenti non sterilizzabili e superfici.</li>
<li><strong>Sterilizzazione</strong>: elimina ogni forma di vita, spore comprese. In pratica si fa in <strong>autoclave di classe B</strong> (norma EN 13060), adatta anche a strumenti cavi e porosi come punte per fresa. Ogni ciclo va registrato (stampa o registro) e conservato.</li>
</ul>
<h2>Protocollo per ogni cliente</h2>
<ol class="steps">
<li>Igienizza le tue mani e quelle della cliente.</li>
<li>Usa strumenti metallici <strong>sterilizzati</strong> in busta, aperta davanti alla cliente.</li>
<li>Lime in carta e buffer sono <strong>monouso</strong> (o si regalano alla cliente).</li>
<li>A fine servizio: detergi, disinfetta, poi sterilizza gli strumenti; disinfetta il piano di lavoro e la lampada.</li>
</ol>
${F('ciclo-sterilizzazione.svg', 'Il ciclo completo degli strumenti dopo ogni cliente.')}
${B('danger', 'Controlli reali', 'I NAS controllano i centri: in un caso a Trento un centro è stato sospeso e multato di 3.000 € per mancanza di procedure di sterilizzazione.')}
`,
          sources: ['https://www.puntosicuro.it/vigilanza-controllo-C-66/vigilanza-nei-centri-estetici-la-sicurezza-dei-clienti-AR-16787/',
            'https://www.ladige.it/territori/trento/controlli-del-nas-a-trento-chiuso-un-centro-estetico-multa-da-3000-euro-wedq1kmt']
        },
        {
          id: 'dpi', title: 'DPI, polveri e vapori', min: 5,
          html: `
<h2>Dispositivi di protezione</h2>
${F('dpi.svg', 'I DPI da usare a ogni servizio.')}
<ul>
<li><strong>Guanti in nitrile</strong>: il lattice non protegge dai monomeri.</li>
<li><strong>Mascherina FFP2</strong> durante la limatura.</li>
<li><strong>Occhiali</strong> protettivi.</li>
<li><strong>Aspiratore da tavolo</strong> per polveri e vapori (raccomandato anche dal NIOSH).</li>
</ul>
<h2>I rischi dell'aria</h2>
<ul>
<li>Le <strong>polveri di limatura</strong> irritano occhi, pelle e vie respiratorie.</li>
<li>Il monomero standard dell'acrilico è l'<strong>EMA</strong> (etil metacrilato). L'<strong>MMA</strong> (metil metacrilato) è vietato dalla FDA per le unghie dal 1974 ma si trova ancora in prodotti economici: evitalo.</li>
<li>Uno studio su saloni di Boston ha rilevato più CO₂, composti organici volatili e polveri sottili dove entra meno aria esterna: <strong>ventila</strong> e tieni i flaconi chiusi.</li>
</ul>
`,
          sources: ['https://cdc.gov/niosh/docs/99-112', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6325001',
            'https://dudley.gov.uk/business/environmental-health/health-and-safety/nail-bar-safety']
        },
        {
          id: 'allergie-ue', simple: "Il gel e l'acrilico liquidi possono dare allergia se toccano la pelle. Finché restano sull'unghia e sono induriti bene, il rischio è basso.", title: 'Allergie agli acrilati e regole UE (HEMA, TPO)', min: 7,
          html: `
<p>I (met)acrilati contenuti in gel e acrilici possono provocare una <strong>allergia da contatto</strong> che, una volta comparsa, è permanente. Il rischio è basso finché il prodotto resta sulla lamina; diventa concreto quando il prodotto <strong>non polimerizzato tocca la pelle</strong>.</p>
${B('danger', 'Due regole d\'oro', '1) Il prodotto non deve mai toccare la pelle della cliente. 2) Non toccare mai gel o monomero non polimerizzati a mani nude.')}
<h2>HEMA e di-HEMA TMHDC – Reg. UE 2020/1682</h2>
<ul>
<li>Ammessi solo nei prodotti per unghie e solo per <strong>uso professionale</strong>.</li>
<li>In etichetta: «Solo per uso professionale» e «Può provocare una reazione allergica».</li>
<li>In vigore dal 2021 (immissione sul mercato dal 3 giugno, messa a disposizione dal 3 settembre 2021).</li>
</ul>
<h2>Divieto di TPO e DMTA – Reg. UE 2025/877</h2>
<ul>
<li>Dal <strong>1° settembre 2025</strong> sono vietati in tutti i cosmetici il fotoiniziatore <strong>TPO</strong> e la <strong>DMTA</strong>, classificati tossici per la riproduzione (CMR 1B).</li>
<li>Il divieto vale anche per l'uso professionale e per le scorte già presenti in salone.</li>
<li>Esistono alternative (per esempio TPO-L, BAPO): <strong>controlla l'INCI</strong> di ogni prodotto in uso.</li>
</ul>
${B('info', 'In pratica', 'Fai un inventario: elimina i prodotti con TPO in etichetta e conserva le schede tecniche e di sicurezza dei prodotti che usi.')}
`,
          sources: ['https://eur-lex.europa.eu/eli/reg/2020/1682/oj/eng',
            'https://certifico.com/chemicals/legislazione-chemicals/312-legislazione-cosmetici/23967-regolamento-ue-2025-877',
            'https://www.money.it/divieto-tpo-e-dmta-negli-smalti-le-regole-per-professionisti-e-centri-estetici',
            'https://coslaw.eu/ingredients-in-the-spotlight-tpo/']
        },
        {
          id: 'normativa-italia', title: 'Chi può lavorare in Italia', min: 5,
          html: `
<p>In Italia la ricostruzione unghie rientra nell'attività di <strong>estetista</strong>, regolata dalla <strong>Legge 4 gennaio 1990 n. 1</strong> e dalle leggi regionali. L'onicotecnico non ha (ancora) una figura professionale nazionale autonoma: esistono proposte di legge nazionali e regionali, ma non risultano approvate.</p>
${B('warn', 'Attenzione agli attestati', 'Un corso privato o un "attestato di onicotecnica" da solo non abilita ad aprire un\'attività in proprio. Verifica sempre le regole della tua Regione.')}
<h2>Come si ottiene la qualifica di estetista</h2>
<ul>
<li>Corso regionale <strong>biennale</strong> (circa 900 ore l'anno) + un anno di specializzazione o di inserimento in impresa + esame; oppure</li>
<li>un periodo di lavoro qualificato come dipendente + un corso teorico (almeno 300 ore) + esame.</li>
</ul>
<h2>Aprire l'attività</h2>
<p>Si presenta la <strong>SCIA</strong> al Comune/SUAP, che verifica requisiti professionali e igienico-sanitari. Valgono inoltre i regolamenti comunali.</p>
`,
          sources: ['https://www.mo.camcom.it/promozione/sportello-genesi/schede-informative/estetista-scheda-informativa',
            'https://www.regione.veneto.it/web/attivita-produttive/professione-estetista',
            'https://documenti.camera.it/leg18/dossier/pdf/AP0107.pdf']
        }
      ]
    },
    /* ------------------------------------------------------------------ 3 */
    {
      id: 'sistemi', summary: ["Gel: base, costruttore, sigillante; mono, bi o trifasico.", "Acrilico: monomero + polvere, perla media ≈1,5:1.", "Polygel: pasta + slip solution, indurisce in lampada.", "Semipermanente: colore 2–3 settimane, non dà struttura.", "Lampada abbinata ai fotoiniziatori del gel; LED con picco ~385–405 nm."], n: 3, level: 'base', title: 'Materiali e sistemi',
      desc: 'Gel UV/LED, acrilico, polygel, semipermanente, soft gel tips, fibra e lampade.',
      lessons: [
        {
          id: 'panoramica', title: 'Panoramica dei sistemi', min: 4,
          html: `
${F('sistemi.svg', 'I quattro sistemi principali a confronto.')}
<p>Non esiste un sistema "migliore": la scelta dipende dalle unghie della cliente, dalla lunghezza richiesta e dalla mano dell'operatrice. Molte professioniste ne padroneggiano almeno due.</p>
<table>
<tr><th>Sistema</th><th>Indurisce con</th><th>Rimozione</th><th>Ideale per</th></tr>
<tr><td>Gel costruttore (hard gel)</td><td>Lampada UV/LED</td><td>Limatura</td><td>Ricostruzioni, lunghezze medie</td></tr>
<tr><td>Soft gel / BIAB</td><td>Lampada</td><td>Acetone</td><td>Coperture, rinforzo, lunghezze corte</td></tr>
<tr><td>Acrilico</td><td>Aria (reazione liquido + polvere)</td><td>Acetone o limatura</td><td>Lunghezze estreme, sculpting, 3D</td></tr>
<tr><td>Polygel</td><td>Lampada</td><td>Limatura / acetone (dipende dal prodotto)</td><td>Chi vuole tempo di lavoro illimitato</td></tr>
<tr><td>Semipermanente</td><td>Lampada</td><td>Acetone</td><td>Colore su unghia naturale (2–3 settimane)</td></tr>
<tr><td>Soft gel tips</td><td>Lampada</td><td>Acetone</td><td>Allungamento veloce</td></tr>
<tr><td>Fibra di vetro / seta</td><td>Resina + attivatore</td><td>Acetone</td><td>Riparazioni, rinforzi sottili</td></tr>
</table>
`,
          sources: ['https://www.beyondpolish.com/blogs/news/gel-x-vs-builder-gel-vs-poly-gel', 'https://c8nailsupply.com/blogs/news/builder-gel-vs-hard-gel-vs-polygel']
        },
        {
          id: 'gel', simple: "Il gel è un \"miele\" che resta morbido finché non lo metti sotto la lampada: lì diventa duro.", title: 'Il gel UV/LED', min: 7,
          html: `
<h2>Componenti</h2>
<ul>
<li><strong>Base / bonder</strong>: crea l'aggancio alla lamina.</li>
<li><strong>Costruttore (builder)</strong>: dà struttura e lunghezza. Può essere autolivellante o ad alta viscosità; esistono versioni trasparenti, rosa e "cover" (camouflage).</li>
<li><strong>Sigillante (top)</strong>: protegge e lucida; con o senza strato di dispersione (la patina appiccicosa che si toglie con il cleaner).</li>
</ul>
<h2>Monofasico, bifasico, trifasico</h2>
<ul>
<li><strong>Monofasico</strong>: un solo gel fa da base, costruttore e sigillante. Veloce.</li>
<li><strong>Bifasico</strong>: base+costruttore in un prodotto, più un sigillante.</li>
<li><strong>Trifasico</strong>: tre prodotti separati, più controllo su ogni fase.</li>
</ul>
<h2>Pro e contro</h2>
<p><strong>+</strong> nessun odore, autolivellante, finitura lucida. <strong>−</strong> rischio di picco di calore con strati spessi; rischio allergia se il gel non polimerizza del tutto.</p>
${B('tip', 'Consiglio', 'Stendi strati sottili e rispetta i tempi della scheda tecnica: uno strato troppo spesso polimerizza solo in superficie e fa grinze.')}
`,
          sources: ['https://areasosta.com/faq/che-differenza-ce-tra-gel-monofasico-e-trifasico']
        },
        {
          id: 'acrilico', videos: [{"id": "2vezvcjA-cc", "title": "Consigli utili sul sistema acrilico per le unghie", "channel": "Accademia Nails", "lang": "IT"}], simple: "Con l'acrilico mescoli un liquido e una polvere sul pennello: si forma una pallina che indurisce da sola all'aria.", title: 'L\'acrilico (liquido e polvere)', min: 6,
          html: `
<p>L'acrilico unisce un <strong>monomero liquido</strong> (EMA) e un <strong>polimero in polvere</strong>: la reazione avviene all'aria, senza lampada. Si raccoglie una "perla" con il pennello (misura 8–12) bagnato di monomero.</p>
${F('perla-acrilico.svg', 'La consistenza della perla dipende dal rapporto liquido/polvere.')}
<ul>
<li><strong>Perla media (≈1,5:1)</strong>: lucida, bombata, resta in forma qualche secondo senza colare. È quella giusta.</li>
<li><strong>Perla bagnata (≈2:1)</strong>: cola nei solchi, ritira, lascia monomero non reagito sulla pelle (rischio allergia).</li>
<li><strong>Perla asciutta (≈1:1)</strong>: granulosa, poca adesione, bolle e porosità.</li>
</ul>
<p><strong>+</strong> il sistema più resistente sulle lunghezze lunghe, ottimo per sculpting e 3D. <strong>−</strong> odore, vapori, tempi di lavorazione da gestire.</p>
`,
          sources: ['https://open-exam-prep.com/study-guides/ca-nail-technician/chemical-nail-services-enhancements/liquid-powder-acrylic-systems']
        },
        {
          id: 'polygel-altri', videos: [{"id": "7Y2eF_L9cgs", "title": "Tutorial semipermanente in 9 step per principianti", "channel": "Nail Couture Italia", "lang": "IT"}, {"id": "z-NbcApd4Y8", "title": "Come applicare le soft gel tips", "channel": "Proglow Italia", "lang": "IT"}], title: 'Polygel, semipermanente, soft gel tips e fibra', min: 7,
          html: `
<h2>Polygel (acrygel)</h2>
<p>Pasta ibrida tra acrilico e gel: si modella con il pennello inumidito di <em>slip solution</em> e indurisce in lampada. <strong>+</strong> tempo di lavoro illimitato, leggero, niente monomero liquido. <strong>−</strong> curva di apprendimento; sollevamenti se la preparazione è scarsa.</p>
<h2>Semipermanente (gel polish)</h2>
<p>Base → colore → top, ognuno in lampada; dura 2–3 settimane e si rimuove con acetone. <strong>Non allunga</strong> e non dà struttura.</p>
${F('tut-semipermanente.svg', 'Semipermanente passo passo: due strati sottili di colore e bordo libero sigillato.')}
<h2>Soft gel tips</h2>
<ol class="steps">
<li>Preparazione, opacizzazione con grana 180, disidratante e primer.</li>
<li>Scelta della misura da solco a solco.</li>
<li>Gel adesivo dentro il tip, applicazione partendo dalla zona cuticolare (senza toccarla), polimerizzazione.</li>
<li>Rifinitura e top. Rimozione con acetone puro.</li>
</ol>
${F('tut-soft-gel-tips.svg', 'Soft gel tips passo passo.')}
<h2>Fibra di vetro e seta</h2>
<p>Un tessuto viene impregnato di resina e indurito con un attivatore. La fibra di vetro è più resistente, la seta più invisibile. Usa l'attivatore <strong>a pennello</strong> più che spray: l'eccesso provoca calore.</p>
${F('tut-fibra.svg', 'Rinforzo in fibra passo passo.')}
`,
          sources: ['https://sophiecress.com/blog/gel-x-nails-a-step', 'https://nailknowledge.org/knowledge-base/fibreglass-systems']
        },
        {
          id: 'lampade', simple: "Ogni gel \"si accende\" con una certa luce: usa la lampada consigliata per quel gel.", title: 'Lampade UV e LED', min: 5,
          html: `
${F('lampade.svg', 'Bande di emissione tipiche delle lampade.')}
<ul>
<li><strong>UV classica</strong>: circa 300–410 nm, picco intorno a 365 nm; polimerizza in circa 2 minuti.</li>
<li><strong>LED</strong>: circa 375–425 nm, picco intorno a 385–405 nm; 30–60 s per gli strati sottili, 60–90 s per il costruttore.</li>
<li><strong>Dual UV/LED</strong>: due picchi (es. 365 + 405 nm), molto diffuse.</li>
</ul>
${F('lampada-posizione.svg', 'Mano piatta e dita tutte dentro la lampada; il pollice si polimerizza a parte.')}
${B('warn', 'I watt non dicono tutto', 'Conta l\'abbinamento tra le lunghezze d\'onda della lampada e i fotoiniziatori del gel. Usa la lampada consigliata dal produttore: con una lampada sbagliata il gel può restare sotto-polimerizzato (allergie) o scaldare troppo.')}
`,
          sources: ['https://scratchmagazine.co.uk/feature/heat-spikes-in-gel-nail-services-why-they-happen-how-to-avoid-them']
        }
      ]
    },
    /* ------------------------------------------------------------------ 4 */
    {
      id: 'attrezzatura', summary: ["Grana bassa = più abrasiva; sulla lamina naturale 180–240.", "Carburo solo sul prodotto; diamantate su unghia naturale e cuticola.", "Fresa: 5.000–10.000 RPM alla cuticola, punta sempre in movimento.", "Pennelli: piatto/ovale per gel, 8–12 per acrilico, liner per i dettagli."], n: 4, level: 'base', title: 'Attrezzatura',
      desc: 'Lime e grane, fresa elettrica e punte, pennelli, tip e cartine.',
      lessons: [
        {
          id: 'lime', title: 'Lime e grane', min: 4,
          html: `
${F('lime-grane.svg', 'Più il numero è basso, più la lima è abrasiva.')}
<table>
<tr><th>Grana</th><th>Uso</th></tr>
<tr><td>80–100</td><td>Accorciare, togliere materiale artificiale</td></tr>
<tr><td>100/180</td><td>Dare forma alla ricostruzione</td></tr>
<tr><td>180–240</td><td>Unghia naturale, opacizzare, rifinire</td></tr>
<tr><td>240+ / buffer</td><td>Levigare e lucidare</td></tr>
</table>
${B('danger', 'Mai sulla lamina naturale', 'Non usare grane grosse sull\'unghia naturale: va solo opacizzata, non assottigliata.')}
`,
          sources: ['https://www.my-personaltrainer.it/bellezza/limare-le-unghie-c-e-un-modo-giusto-per-farlo.html']
        },
        {
          id: 'fresa', simple: "La fresa è un trapanino per unghie: velocità bassa vicino alla pelle e punta sempre in movimento.", title: 'Fresa elettrica e punte', min: 7,
          html: `
${F('punte-fresa.svg', 'Forme delle punte, codici colore e velocità indicative.')}
<ul>
<li><strong>Punte in carburo</strong>: solo sul prodotto artificiale.</li>
<li><strong>Punte diamantate</strong>: unghia naturale e zona cuticolare (meglio se "di sicurezza", con punta arrotondata).</li>
<li><strong>Codici colore</strong> (variano tra marchi): giallo extra-fine, rosso fine, blu media, verde grossa, nero extra-grossa.</li>
</ul>
<h2>Velocità indicative</h2>
<ul>
<li>Cuticola e unghia naturale: 5.000–10.000 RPM</li>
<li>Sfumare la superficie: 10.000–15.000 RPM</li>
<li>Rimuovere prodotto: 15.000–25.000 RPM</li>
</ul>
${B('warn', 'Sicurezza', 'Pressione leggera e punta sempre in movimento: fermarsi in un punto crea calore da attrito e solchi. La manicure a secco ("russa") con fresa è una tecnica avanzata che richiede formazione specifica.')}
`,
          sources: ['https://www.katiebarnesacademy.com/blogs/e-filing/e-file-bit-grit-guide',
            'https://purespadirect.com/blogs/pure-spa-direct-blog/e-file-bit-guide-for-nail-techs-shapes-grits-and-safe-use-for-speed-cuticle-care-your-cuticles-will-thank-you']
        },
        {
          id: 'kit', title: 'Kit di partenza', min: 5,
          html: `
<h2>Attrezzature</h2>
<ul>
<li>Lampada UV/LED (meglio dual) e aspiratore da tavolo</li>
<li>Fresa con punte diamantate e in carburo</li>
<li>Autoclave di classe B (o sterilizzazione esterna documentata) e vasca per disinfettanti</li>
<li>Mano da allenamento e ruota di tip per esercitarti</li>
</ul>
<h2>Prodotti e consumabili</h2>
<ul>
<li>Disidratante, primer acido e senza acido, base, costruttore (trasparente, rosa, cover), sigillante, cleaner, acetone</li>
<li>Tip di varie misure, tagliatip, colla, cartine (forms)</li>
<li>Pennelli per gel e per acrilico (misura 8–12), pennellini per nail art, dotter</li>
<li>Lime 100/180/240, buffer, spingicuticole, tronchesine, bastoncini d'arancio</li>
<li>Olio per cuticole, DPI (nitrile, FFP2, occhiali)</li>
</ul>
${F('pennelli.svg', 'I pennelli principali e il loro uso.')}
${F('tip-tipi.svg', 'Tip con incavo, a contatto e scala delle misure.')}
${B('tip', 'Consiglio d\'acquisto', 'Scegli un sistema completo di un solo produttore per iniziare: base, gel e lampada sono studiati per funzionare insieme.')}
`,
          sources: []
        }
      ]
    },
    /* ------------------------------------------------------------------ 5 */
    {
      id: 'preparazione', summary: ['Igiene → consulenza → cuticola → opacizza → polvere → disidratante → primer.', 'Si rimuove solo la cuticola (pelle morta sulla lamina); il vero pterigio non si tocca.', 'Opacizzare = togliere la lucidità con grana 180–240, non assottigliare.', 'Primer: pennello quasi asciutto, solo sulla lamina, ad almeno 1 mm dalla pelle.', 'Dopo il disidratante non toccare più la lamina.'], n: 5, level: 'base', title: 'Preparazione dell\'unghia',
      desc: 'Il passaggio che decide se la ricostruzione tiene o si solleva.',
      lessons: [
        {
          id: 'passaggi', videos: [{"id": "tyZfOTu6T70", "title": "Nail prep: passaggi di preparazione unghie", "channel": "Proglow Italia", "lang": "IT"}], simple: 'Prima di costruire, l\'unghia deve essere sana, pulita, senza pellicine, leggermente ruvida e senza grasso: così il prodotto si "aggrappa" e non si solleva.', title: 'I passaggi della preparazione', min: 12,
          html: `
<p>La preparazione è la parte <strong>meno spettacolare</strong> del lavoro, ma è quella che decide se la ricostruzione dura tre settimane o si solleva dopo tre giorni. Quasi tutti i sollevamenti (<em>lifting</em>) nascono qui: una pellicina dimenticata, un po' di polvere, un velo di sebo.</p>
<p>L'obiettivo è semplice: ottenere una lamina <strong>sana, pulita, asciutta e leggermente opaca</strong>, senza averla assottigliata e senza aver ferito la pelle.</p>
<h2>I nemici dell'adesione</h2>
<table>
<tr><th>Nemico</th><th>Da dove viene</th><th>Come si elimina</th></tr>
<tr><td><strong>Pelle morta (cuticola)</strong> sulla lamina</td><td>Si stacca dall'eponichio e "viaggia" sull'unghia mentre cresce</td><td>Arretrare e rimuovere con spingicuticole/curette</td></tr>
<tr><td><strong>Lucidità</strong></td><td>La superficie naturale della lamina è liscia</td><td>Opacizzare con grana fine (180–240)</td></tr>
<tr><td><strong>Polvere</strong></td><td>Limatura</td><td>Pennello pulito, poi salvietta che non lascia pelucchi</td></tr>
<tr><td><strong>Sebo e umidità</strong></td><td>La pelle produce olio di continuo; l'unghia contiene acqua</td><td>Disidratante, e niente dita sulla lamina dopo</td></tr>
<tr><td><strong>Residui di olio o crema</strong></td><td>Prodotti della cliente o della manicure</td><td>Lavaggio mani con sapone non grasso prima di iniziare</td></tr>
</table>
<h2>La sequenza completa</h2>
${F('prep-sequenza-perche.svg', 'Ogni passaggio ha un perché: saltarne uno rovina quelli dopo.')}
<ol class="steps">
<li><strong>Igiene</strong>: lava e igienizza le tue mani e quelle della cliente; usa strumenti sterilizzati e lime nuove. <em>Perché</em>: lavori vicino alla pelle e ai tessuti vivi; un graffio con uno strumento sporco può infettarsi.</li>
<li><strong>Consulenza e controllo</strong>: guarda unghie e pelle. Se vedi arrossamenti, gonfiori, pus, macchie verdi, distacco della lamina o segni di micosi <strong>non lavorare</strong> e consiglia un medico. <em>Perché</em>: la ricostruzione chiude e nasconde il problema e può peggiorarlo.</li>
<li><strong>Togli il vecchio prodotto</strong> (smalto, semipermanente) e accorcia il bordo libero se serve, con grana 180–240. <em>Perché</em>: si costruisce solo su lamina pulita; un bordo libero troppo lungo fa da leva.</li>
<li><strong>Arretra la cuticola</strong> con lo spingicuticole tenuto quasi piatto, senza forza. <em>Perché</em>: libera la lamina e ti mostra dove finisce la pelle viva.</li>
<li><strong>Rimuovi la cuticola</strong> (la pellicina morta rimasta attaccata alla lamina) con la curette o con lo spingicuticole a lama piatta. Taglia con la tronchesina solo le pellicine già staccate. <em>Perché</em>: il prodotto steso sulla pelle morta si stacca insieme a lei.</li>
<li><strong>Opacizza</strong> tutta la lamina con grana fine (180–240), con leggerezza, finché non resta nessuna zona lucida. <em>Perché</em>: la superficie leggermente ruvida offre più presa; ma la lamina non va assottigliata.</li>
<li><strong>Elimina la polvere</strong> con un pennello pulito e passa una salvietta senza pelucchi con il disidratante/cleaner. <em>Perché</em>: la polvere resta intrappolata sotto il prodotto e crea bolle e sollevamenti.</li>
<li><strong>Disidratante</strong> su tutta la lamina. <em>Perché</em>: toglie sebo e umidità superficiale.</li>
<li><strong>Primer</strong> (se il tuo sistema lo prevede): pochissimo, solo sulla lamina. Poi parti subito con la base o il prodotto.</li>
</ol>
${B('info', 'Che cosa cambia tra gel e acrilico?', 'La sequenza è la stessa. Cambiano il tipo di primer (vedi lezione "Disidratante e primer") e a volte la grana suggerita dal produttore: alcuni marchi indicano 150 con pressione minima, altri 180 o 240. Segui sempre le istruzioni del tuo sistema.')}
<h2>Quanto tempo ci vuole?</h2>
<p>All'inizio una preparazione completa su 10 dita può richiedere 30–40 minuti. Con la pratica scende a 10–15 minuti. Non cercare la velocità prima della precisione: un passaggio saltato oggi è un refill anticipato domani.</p>
<h2>Errori frequenti</h2>
${F('prep-errori.svg', 'Quattro errori di preparazione che causano sollevamenti.')}
<table>
<tr><th>Errore</th><th>Cosa succede</th><th>Come evitarlo</th></tr>
<tr><td>Pellicina residua vicino alla cuticola o nei solchi</td><td>Sollevamento alla base già nei primi giorni</td><td>Controlla con luce radente prima di continuare</td></tr>
<tr><td>Lamina limata troppo (zone sottili, "solchi")</td><td>Unghia flessibile, dolore, picco di calore in lampada</td><td>Grana fine, pochi passaggi leggeri, nessuna pressione</td></tr>
<tr><td>Polvere lasciata nei solchi laterali</td><td>Bolle e distacchi ai lati</td><td>Pennello + salvietta, guardando anche i lati</td></tr>
<tr><td>Dita sulla lamina dopo il disidratante</td><td>Il sebo rovina l'adesione</td><td>Tieni il dito della cliente per i lati, mai sopra</td></tr>
<tr><td>Preparare tutte e 10 le unghie e lavorare piano</td><td>Nel frattempo l'unghia si "riumidifica"</td><td>Da principiante: prepara e costruisci una mano alla volta</td></tr>
</table>
${B('warn', 'Da non fare', 'Non toccare la lamina con le dita dopo il disidratante: il sebo della pelle riduce l\'adesione. Se succede, ripassa il disidratante.')}
${B('danger', 'Pelle viva', 'Eponichio, pieghe laterali e iponichio sono vivi: non si tagliano e non si limano. Un taglio è una porta aperta per le infezioni.')}
${B('tip', 'Il test della luce radente', 'Inclina il dito sotto la lampada da tavolo: le zone ancora lucide riflettono la luce, i residui di pellicina appaiono come un velo opaco e "sollevato" vicino alla cuticola.')}
`,
          sources: ['https://www.nsinails.com.au/blogs/news/nail-preparation',
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/nail-sculpting-forms',
            'https://www.katiebarnesacademy.com/blogs/preparation/what-is-the-difference-between-acid-free-and-acid-based-nail-primer',
            'https://www.homeofnailart.com/blogs/knowledge-hub/mastering-the-art-of-nail-filing-a-comprehensive-guide-for-professional-nail-technicians']
        },
        {
          id: 'zona-cuticolare', simple: 'Spingi indietro la pelle con delicatezza, togli solo la pellicina morta che è rimasta sull\'unghia e lascia stare la pelle viva.', title: 'La zona cuticolare passo passo', min: 9,
          html: `
<p>La zona cuticolare è il punto in cui iniziano quasi tutti i sollevamenti. Ed è anche la zona più delicata: lì sotto c'è la <strong>matrice</strong>, che produce l'unghia. Serve precisione, non forza.</p>
<h2>Tre parole da non confondere</h2>
<table>
<tr><th>Termine</th><th>Che cos'è</th><th>Che cosa fai</th></tr>
<tr><td><strong>Eponichio</strong></td><td>La piega di pelle <em>viva</em> alla base dell'unghia</td><td>La arretri con delicatezza. Non si taglia.</td></tr>
<tr><td><strong>Cuticola</strong></td><td>Una pellicina <em>morta</em>, sottile e trasparente, che si stacca dall'eponichio e resta attaccata alla lamina</td><td>La rimuovi completamente dalla lamina.</td></tr>
<tr><td><strong>Pterigio (vero)</strong></td><td>Una condizione <em>anomala</em>: la pelle si salda alla lamina e "avanza" con lei, spesso a forma di triangolo, dopo traumi, ustioni o malattie</td><td><strong>Non lo tocchi</strong>: niente taglio, niente lima. Consigli un medico (dermatologo).</td></tr>
</table>
${F('pterigio-vero.svg', 'Cuticola normale (si rimuove) e vero pterigio (non si tocca).')}
${B('info', 'Attenzione ai nomi', 'Nei saloni italiani si sente spesso "togliere il pterigio" per dire "togliere la cuticola dalla lamina". Nei manuali professionali (Milady) però pterigio e cuticola sono due cose diverse: il vero pterigio è un disturbo e non è di competenza dell\'onicotecnica. In questo corso usiamo "cuticola" per la pellicina da togliere.')}
<h2>Gli strumenti</h2>
<ul>
<li><strong>Spingicuticole</strong> (metallo, sterilizzato): una estremità piatta per arretrare, l'altra a lama/curette per sollevare la pellicina dalla lamina.</li>
<li><strong>Bastoncino d'arancio</strong>: alternativa morbida, monouso.</li>
<li><strong>Tronchesina per pellicine</strong>: solo per tagliare i pezzetti di pelle morta già staccati, mai la pelle viva.</li>
<li><strong>Emolliente per cuticole</strong> (facoltativo): ammorbidisce. Va eliminato completamente prima di opacizzare, perché lascia residui.</li>
</ul>
<h2>Procedimento</h2>
${F('cuticola-step.svg', 'Zona cuticolare in quattro passaggi.')}
<ol class="steps">
<li><strong>Arretra l'eponichio</strong>: spingicuticole a estremità piatta, tenuto <strong>quasi parallelo alla lamina</strong> (circa 30–45°), con piccoli movimenti circolari dal centro verso i lati. Nessuna forza. <em>Perché</em>: se tieni lo strumento dritto "graffi" la lamina e premi sulla matrice.</li>
<li><strong>Solleva la cuticola</strong>: con la curette o con la lama dello spingicuticole, sempre piatta sulla lamina, "raschia" la pellicina trasparente da cuticola verso la punta. Lavora anche nei solchi laterali.</li>
<li><strong>Taglia solo ciò che pende</strong>: con la tronchesina elimina le pellicine morte già staccate. Se sanguina, hai tagliato pelle viva.</li>
<li><strong>Controlla</strong>: con luce radente non deve restare nessun velo opaco sulla lamina. Elimina ogni residuo di emolliente.</li>
</ol>
${B('tip', 'Asciutto o bagnato?', 'Per la ricostruzione molte formatrici preferiscono lavorare la cuticola "a secco" o con poco prodotto: l\'acqua entra nella lamina, la gonfia e poi, asciugando, può favorire i sollevamenti. Se usi acqua o emolliente, aspetta che l\'unghia sia ben asciutta e disidrata con cura.')}
<h2>Errori frequenti</h2>
<ul>
<li><strong>Troppa forza</strong>: lascia solchi sulla lamina o, nel tempo, linee e deformazioni (pressione sulla matrice).</li>
<li><strong>Tagliare l'eponichio</strong>: la pelle ricresce più spessa e dura e si rischiano infezioni.</li>
<li><strong>Dimenticare i solchi laterali</strong>: il sollevamento parte spesso dagli angoli.</li>
<li><strong>Lasciare l'emolliente</strong>: è oleoso e impedisce l'adesione.</li>
</ul>
${B('danger', 'Quando fermarsi', 'Pelle arrossata, gonfia, calda, dolorante o con pus (paronichia), oppure un vero pterigio: non lavorare e consiglia un medico.')}
`,
          sources: ['https://www.oregon.gov/oha/PH/HLO/Documents/Practice_Clarification_Nail_Pterygium.pdf',
            'https://nailknowledge.org/?p=97772',
            'https://www.nsinails.com.au/blogs/news/nail-preparation']
        },
        {
          id: 'opacizzazione', simple: 'Con una lima fine togli solo la lucidità dell\'unghia, come quando si carteggia appena un mobile prima di verniciarlo. Non devi consumarla.', title: 'Opacizzare senza assottigliare', min: 7,
          html: `
<p>Opacizzare significa <strong>togliere la lucidità</strong> della lamina per creare una superficie con microscopici graffi dove il prodotto si possa "agganciare". Non significa togliere spessore.</p>
<h2>Perché non bisogna assottigliare</h2>
<ul>
<li>La lamina <strong>protegge il letto ungueale dal calore</strong>: più è sottile, più la cliente sente il bruciore in lampada (picco di calore).</li>
<li>Una lamina sottile <strong>si piega</strong>: il prodotto rigido sopra non la segue e si stacca.</li>
<li>Lo spessore perso <strong>non si recupera</strong>: bisogna aspettare che l'unghia ricresca (mesi).</li>
</ul>
<h2>Quale grana</h2>
<table>
<tr><th>Grana</th><th>Uso sulla lamina naturale</th></tr>
<tr><td>80–100</td><td><strong>Mai</strong>: solo sul prodotto artificiale</td></tr>
<tr><td>150</td><td>Alcuni produttori la indicano per opacizzare, ma solo con pressione minima. Per una principiante è facile esagerare</td></tr>
<tr><td><strong>180</strong></td><td>La scelta più diffusa per opacizzare e accorciare</td></tr>
<tr><td>240 / buffer fine</td><td>Unghie sottili o sensibili; rifinitura</td></tr>
</table>
${B('info', 'Le fonti non sono tutte uguali', 'I marchi danno indicazioni diverse (da 150 a 240). Il punto comune è: grana fine, pressione leggera, pochi passaggi. Per iniziare usa 180 o 240.')}
<h2>Dove opacizzare</h2>
${F('opacizzazione-zone.svg', 'Le zone da non dimenticare: base, solchi laterali e bordo libero.')}
<ol class="steps">
<li><strong>Zona cuticolare</strong>: piccoli movimenti con l'estremità della lima o un buffer stretto, seguendo la curva della cuticola. Qui i sollevamenti sono più frequenti.</li>
<li><strong>Lati</strong>: inclina leggermente la lima per raggiungere la lamina vicino ai solchi, senza limare la pelle.</li>
<li><strong>Centro</strong>: movimenti leggeri dalla cuticola verso la punta, seguendo la curva dell'unghia.</li>
<li><strong>Bordo libero</strong>: opacizza anche lo spessore del bordo; dovrà essere sigillato dal prodotto.</li>
<li><strong>Controlla</strong> con luce radente: nessun punto lucido, nessuna striscia più profonda.</li>
</ol>
${F('opacizzazione-controllo.svg', 'Il controllo con la luce: lucida, opaca giusta, troppo limata.')}
<h2>Errori frequenti</h2>
<ul>
<li><strong>Insistere sempre nello stesso punto</strong> (spesso al centro): crea una zona sottile.</li>
<li><strong>Usare la lima "di forma" 100/180 per comodità</strong>: troppo aggressiva sulla lamina.</li>
<li><strong>Dimenticare la base e i lati</strong>: proprio dove partono i sollevamenti.</li>
<li><strong>Riutilizzare la lima</strong>: le lime in carta sono monouso; una lima consumata costringe a premere di più.</li>
</ul>
${B('warn', 'Segnali che hai limato troppo', 'La cliente sente caldo o dolore, vedi una zona più rosa o più trasparente, l\'unghia si piega premendo la punta. Fermati: su quella mano usa strati più sottili e polimerizzazioni con il metodo "flash and pull".')}
`,
          sources: ['https://www.nsinails.com.au/blogs/news/nail-preparation',
            'https://www.homeofnailart.com/blogs/knowledge-hub/mastering-the-art-of-nail-filing-a-comprehensive-guide-for-professional-nail-technicians',
            'https://open-exam-prep.com/study-guides/oh-nail-technician/artificial-nail-services/sculptured-acrylic-nails',
            'https://www.youngnails.com/blogs/news/how-to-use-nail-forms']
        },
        {
          id: 'primer', videos: [{"id": "TFk5uRlLXdA", "title": "Liquidi di preparazione: nomi e differenze", "channel": "Accademia Nails", "lang": "IT"}], simple: 'Il disidratante asciuga l\'unghia e toglie il grasso; il primer fa da "ponte" tra unghia e prodotto. Ne basta pochissimo, solo sull\'unghia.', title: 'Disidratante e primer', min: 10,
          html: `
<p>Dopo l'opacizzazione la lamina è ruvida e pulita, ma contiene ancora un po' di <strong>umidità</strong> e di <strong>sebo</strong>. Qui entrano in gioco due liquidi diversi, che non si sostituiscono a vicenda.</p>
<h2>Disidratante (nail prep, prep, cleanser)</h2>
<ul>
<li><strong>Che cosa fa</strong>: toglie sebo e umidità superficiale dalla lamina. Evapora in pochi secondi.</li>
<li><strong>Come si usa</strong>: una passata su tutta la lamina, compresi lati e bordo libero, con pennellino o salvietta senza pelucchi.</li>
<li><strong>Quando</strong>: dopo aver tolto la polvere, <em>prima</em> del primer o della base.</li>
<li><strong>Segnale</strong>: l'unghia diventa leggermente biancastra/opaca. Se vedi strisce lucide, ripassa.</li>
</ul>
<h2>Primer: acido o senza acido?</h2>
${F('primer-acido-vs-senza.svg', 'Sezione al microscopio: il primer acido incide, quello senza acido fa da biadesivo.')}
<table>
<tr><th></th><th>Primer acido</th><th>Primer senza acido (bonder)</th></tr>
<tr><td><strong>Come funziona</strong></td><td>Contiene acido metacrilico: "incide" la superficie con microfori dove il prodotto si aggrappa</td><td>Fa da "nastro biadesivo" chimico tra lamina e prodotto; modifica per breve tempo il pH della lamina</td></tr>
<tr><td><strong>Aspetto da asciutto</strong></td><td>Bianco gessoso, opaco</td><td>Resta leggermente appiccicoso (dipende dal marchio)</td></tr>
<tr><td><strong>Quando si usa</strong></td><td>Acrilico tradizionale, unghie molto grasse o con sollevamenti ripetuti</td><td>Gel e uso quotidiano; spesso anche con l'acrilico moderno</td></tr>
<tr><td><strong>Rischi</strong></td><td>Corrosivo: ustioni chimiche su pelle e occhi; ripetuto assottiglia la lamina</td><td>Meno aggressivo, ma resta un prodotto con acrilati: mai sulla pelle</td></tr>
<tr><td><strong>Tempi</strong></td><td>Applica il prodotto solo quando è asciutto (bianco gessoso)</td><td>Asciuga in circa 40–60 secondi; l'effetto cala dopo circa 20 minuti</td></tr>
</table>
<h2>Come si applica il primer</h2>
${F('primer-quantita.svg', 'La quantità giusta: pennello quasi asciutto, piccoli tocchi, lontano dalla pelle.')}
<ol class="steps">
<li><strong>Scarica il pennello</strong> sul bordo del flacone: deve essere quasi asciutto.</li>
<li><strong>Tocca la lamina</strong> al centro e distribuisci con piccoli tocchi, restando ad <strong>almeno 1 mm</strong> da cuticola e solchi laterali.</li>
<li><strong>Solo sulla lamina naturale</strong>: non sul tip, non sulla pelle.</li>
<li><strong>Lascia asciugare</strong> il tempo indicato dal produttore.</li>
<li><strong>Una mano alla volta</strong>: se il lavoro su una mano dura più di 20 minuti circa, applica il primer senza acido mano per mano.</li>
</ol>
${B('warn', 'Più primer non vuol dire più tenuta', 'Un eccesso di primer forma uno strato che riduce l\'adesione invece di aumentarla. Se un\'unghia si solleva sempre, cerca prima la causa nella preparazione (pellicina, polvere, contatto con la pelle), non nel primer.')}
<h2>Errori frequenti</h2>
<table>
<tr><th>Errore</th><th>Conseguenza</th></tr>
<tr><td>Primer al posto del disidratante</td><td>Sebo e umidità restano: adesione scarsa</td></tr>
<tr><td>Primer sulla pelle</td><td>Irritazione, ustione (acido), rischio di sensibilizzazione</td></tr>
<tr><td>Primer sul tip</td><td>Può rovinare/crepare la plastica e non serve</td></tr>
<tr><td>Più passate di primer acido</td><td>Lamina assottigliata e sensibile</td></tr>
<tr><td>Flacone contaminato (pennello toccato su polvere o pelle)</td><td>Il prodotto funziona peggio: chiudi sempre il flacone</td></tr>
<tr><td>Mescolare marchi diversi</td><td>Incompatibilità: segui un solo sistema</td></tr>
</table>
${B('danger', 'Pelle e occhi', 'Il primer non deve mai toccare la pelle. Se il primer acido finisce in un occhio, sciacqua subito con acqua corrente per almeno 15 minuti e rivolgiti a un medico. Lavora con occhiali di protezione.')}
${B('info', 'Semipermanente', 'Molti sistemi di semipermanente non richiedono primer: la base ha già la funzione di aggancio. Usa il primer solo se il produttore lo prevede.')}
`,
          sources: ['https://www.katiebarnesacademy.com/blogs/preparation/what-is-the-difference-between-acid-free-and-acid-based-nail-primer',
            'https://www.nsinails.com.au/blogs/news/nail-preparation',
            'https://open-exam-prep.com/study-guides/oh-nail-technician/artificial-nail-services/sculptured-acrylic-nails',
            'https://purespadirect.com/blogs/pure-spa-direct-blog/how-to-use-nail-primer-dehydrator-ndash-the-secret-weapons-for-flawless-long-lasting-nail-art']
        }
      ]
    },
    /* ------------------------------------------------------------------ 6 */
    {
      id: 'tip', summary: ['Il tip copre da solco a solco senza toccare la pelle: se sei tra due misure, prendi la più grande e lima i lati.', 'Incavo su non più di metà lamina; appoggio a ~45° e discesa lenta, tieni 5–10 s.', 'Taglia solo a colla asciutta; fondi solo la plastica con lima fine tenuta piatta.', 'Primer solo sull\'unghia naturale, mai sul tip.', 'Sul tip si costruisce comunque l\'apex in zona 2.'], n: 6, level: 'inter', title: 'Ricostruzione su tip',
      desc: 'Scegliere, applicare, tagliare e fondere il tip; copertura in gel.',
      lessons: [
        {
          id: 'misura', simple: 'Il tip giusto è largo esattamente quanto l\'unghia, da un lato all\'altro, senza appoggiarsi sulla pelle.', title: 'Scegliere e adattare il tip', min: 8,
          html: `
<p>Un tip sbagliato rovina tutto il lavoro: se è stretto lascia scoperti i lati e si crepa, se è largo preme sulle pieghe laterali, fa male e si solleva. Prima di incollare, si <strong>misura e si adatta</strong>.</p>
<h2>Com'è fatto un tip</h2>
${F('tip-anatomia.svg', 'Le parti del tip: incavo, punto d\'arresto, zona di contatto.')}
<ul>
<li><strong>Incavo (well)</strong>: la parte più sottile, che si appoggia sull'unghia naturale e si incolla.</li>
<li><strong>Punto d'arresto (stop)</strong>: il "gradino" che si appoggia contro il bordo libero.</li>
<li><strong>Zona di contatto</strong>: tutta la superficie dell'incavo che tocca la lamina. È lì che si forma il legame.</li>
<li><strong>Corpo del tip</strong>: la parte che crea l'allungamento.</li>
</ul>
<h2>Tipi di tip</h2>
<table>
<tr><th>Tipo</th><th>Caratteristiche</th><th>Quando</th></tr>
<tr><td><strong>Incavo pieno (full well)</strong></td><td>Incavo lungo: massima superficie di contatto, più lavoro di fusione</td><td>Corsi ed esami; unghie normali</td></tr>
<tr><td><strong>Mezzo incavo (half well)</strong></td><td>Incavo corto: meno plastica sulla lamina, si fonde più in fretta</td><td>Salone, quando si vuole velocità</td></tr>
<tr><td><strong>A contatto / senza incavo</strong></td><td>Si appoggia di testa al bordo libero, niente da fondere</td><td>Con copertura scolpita, lavori veloci</td></tr>
<tr><td><strong>Trasparente, naturale, bianco (french)</strong></td><td>Cambia solo il colore</td><td>Trasparente per cover/colore, bianco per french veloce</td></tr>
</table>
${F('tip-tipi.svg', 'Tipi di tip e scala delle misure.')}
<h2>Le misure</h2>
<p>I tip sono numerati di solito da <strong>0 (il più largo, pollice)</strong> a <strong>9 o 10 (il più stretto, mignolo)</strong>; alcuni marchi arrivano a 00–11. La larghezza in millimetri di ogni numero <strong>cambia da marca a marca</strong>: usa la tabella del tuo produttore. In genere una cliente usa 3–5 misure diverse e le due mani non sono identiche.</p>
<h2>Come misurare</h2>
<ol class="steps">
<li><strong>Prova a secco</strong>, senza colla, appoggiando il tip sul bordo libero.</li>
<li><strong>Guarda dall'alto</strong>: i bordi del tip devono arrivare esattamente ai solchi laterali, da solco a solco.</li>
<li><strong>Guarda dal davanti</strong>: la curva del tip deve seguire quella dell'unghia. Un'unghia molto curva spesso richiede una misura in più.</li>
<li><strong>Se sei tra due misure</strong>, scegli la più grande e lima i lati del tip <em>prima</em> di incollarlo, finché combacia.</li>
<li><strong>Prepara tutti e 10 i tip in ordine</strong> sul tavolo (da pollice a mignolo) prima di iniziare a incollare.</li>
</ol>
${F('tip-misura-errori.svg', 'Troppo stretto, giusto, troppo largo: vista frontale.')}
<h2>Adattare il tip</h2>
${F('tip-adattare.svg', 'Come adattare un tip: lati e incavo.')}
<ul>
<li><strong>Lati troppo larghi</strong>: lima la plastica del tip ai lati, seguendo la sua curva, mai la pelle della cliente.</li>
<li><strong>Incavo troppo lungo</strong>: l'incavo non dovrebbe coprire <strong>più di metà della lamina</strong>. Accorcialo con lima o forbicine, dando una forma che segua la curva della cuticola.</li>
<li><strong>Unghia corta o morsicata</strong>: preferisci un tip a mezzo incavo o accorcia molto l'incavo; valuta in alternativa la cartina.</li>
</ul>
${B('info', 'Più grande o più piccolo?', 'La maggior parte delle guide consiglia la misura più grande da limare ai lati. Alcuni manuali d\'esame preferiscono la più piccola: il punto in comune è che il tip finale deve essere largo come l\'unghia e non deve mai poggiare sulla pelle.')}
${B('warn', 'Mai forzare', 'Un tip troppo stretto "aperto a forza" tende a tornare alla sua forma e tira la lamina: crepe ai lati e sollevamenti.')}
`,
          sources: ['https://open-exam-prep.com/study-guides/oh-nail-technician/artificial-nail-services/nail-tips-application',
            'https://open-exam-prep.com/study-guides/wa-nail-technician/tips-wraps-sculpting/nail-tips',
            'https://evernail.shop/en/blogs/contents/howtomeasurenailtipsize']
        },
        {
          id: 'applicazione', videos: [{"id": "mCY3EVijhjw", "title": "Come applicare una tip dopo aver preparato l'unghia", "channel": "Naio Nails IT", "lang": "IT"}, {"id": "hJCElOAO23k", "title": "Ricostruzione unghie con tip in gel", "channel": "Mondo NAILS", "lang": "IT"}], simple: 'Un velo di colla nell\'incavo, appoggi il tip inclinato contro il bordo dell\'unghia e lo abbassi piano, come si chiude una porta: così l\'aria esce e non restano bolle.', title: 'Applicazione del tip', min: 10,
          html: `
${F('tip-applicazione.svg', 'Applicazione del tip in quattro passaggi.')}
<p>Il tip è un'unghia di plastica preformata (spesso in ABS) che si incolla sul bordo libero per creare la lunghezza. Da solo è fragile: va <strong>sempre coperto</strong> con gel, acrilico o fibra.</p>
<h2>Prima di iniziare</h2>
<ul>
<li>Preparazione completa dell'unghia (cuticola, opacizzazione, polvere, disidratante). <strong>Non mettere olio</strong>.</li>
<li>Bordo libero corto e regolare: il punto d'arresto del tip deve appoggiarsi su un bordo dritto.</li>
<li>Tip già misurati e adattati, disposti in ordine.</li>
<li>Colla per tip (cianoacrilato, a pennellino o a beccuccio) o gel adesivo, secondo il sistema.</li>
</ul>
<h2>Procedimento</h2>
${F('tip-incollaggio-45.svg', 'Il movimento "a porta che si chiude": dall\'appoggio a 45° alla discesa lenta.')}
<ol class="steps">
<li><strong>Colla</strong>: un velo sottile nell'incavo (e, se il produttore lo indica, un velo sul bordo libero). Riempi l'incavo senza fare gocce. <em>Perché</em>: troppa colla intrappola aria, cola sulla pelle e indebolisce il legame.</li>
<li><strong>Appoggio a circa 45°</strong>: porta il punto d'arresto contro il bordo libero, con il tip inclinato.</li>
<li><strong>Abbassa lentamente</strong>: "fai rotolare" il tip verso la lamina; la colla avanza e spinge fuori l'aria. <em>Perché</em>: se lo appoggi piatto subito, la colla si chiude su tutti i lati e restano bolle.</li>
<li><strong>Tieni fermo 5–10 secondi</strong> con pressione leggera e uniforme, controllando l'asse. Non muoverlo per "provare" se tiene.</li>
<li><strong>Controlla</strong>: dall'alto (in asse con il dito), dal davanti (curva uguale all'unghia), in trasparenza (niente bolle chiare sotto l'incavo).</li>
<li><strong>Elimina subito</strong> eventuale colla sui lati con un bastoncino, prima che indurisca.</li>
</ol>
${B('tip', 'Ordine di lavoro', 'Incolla tutti i tip di una mano, poi passa al taglio e alla fusione: la colla ha il tempo di indurire bene.')}
<h2>Che cosa controllare</h2>
<table>
<tr><th>Controllo</th><th>Giusto</th><th>Sbagliato</th></tr>
<tr><td>Larghezza</td><td>Da solco a solco</td><td>Lati scoperti o tip sulla pelle</td></tr>
<tr><td>Asse</td><td>Prosegue la linea del dito</td><td>Ruotato verso il pollice o verso il mignolo</td></tr>
<tr><td>Profilo</td><td>Prosegue la lamina, né in su né in giù</td><td>Punta che "scende" o "sale"</td></tr>
<tr><td>Bolle</td><td>Nessuna</td><td>Macchie chiare sotto l'incavo</td></tr>
</table>
${F('tip-errori-applicazione.svg', 'Tre errori di applicazione: bolla, fuori asse, inclinato.')}
<h2>Errori frequenti</h2>
<ul>
<li><strong>Bolla sotto l'incavo</strong>: il tip va tolto (ammorbidendo con acetone, mai a strappo) e riapplicato. Una bolla diventa un sollevamento e un punto dove si raccoglie umidità.</li>
<li><strong>Tip storto</strong>: si nota sempre di più man mano che allunghi. Correggilo subito.</li>
<li><strong>Colla sulla pelle</strong>: non tirare; ammorbidisci e rimuovi con delicatezza.</li>
</ul>
${B('danger', 'Mai a strappo', 'Un tip incollato non si toglie mai facendo leva o strappando: si strappano anche strati di lamina.')}
`,
          sources: ['https://open-exam-prep.com/study-guides/oh-nail-technician/artificial-nail-services/nail-tips-application',
            'https://open-exam-prep.com/study-guides/wa-nail-technician/tips-wraps-sculpting/nail-tips',
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/nail-tips']
        },
        {
          id: 'fusione', simple: 'Tagli il tip alla lunghezza giusta e poi limi solo la plastica finché non senti più lo scalino: l\'unghia vera non si tocca.', title: 'Taglio e fusione del tip', min: 8,
          html: `
<h2>1. Il taglio</h2>
${F('tip-taglio.svg', 'Il tagliatip: lama perpendicolare, taglio solo a colla asciutta.')}
<ol class="steps">
<li><strong>Aspetta che la colla sia indurita</strong>. <em>Perché</em>: tagliando con la colla fresca il tip si sposta e il legame si rompe.</li>
<li><strong>Decidi la lunghezza</strong>: per una principiante e per l'uso quotidiano, il bordo libero finale non dovrebbe superare circa <strong>metà della lunghezza del letto ungueale</strong>.</li>
<li><strong>Taglia</strong> con il tagliatip tenuto perpendicolare al tip, lasciando 1–2 mm in più per la limatura. Su tip molto curvi entra dai lati invece di schiacciare il centro.</li>
<li><strong>Uniforma</strong>: taglia tutti i tip della mano alla stessa lunghezza, poi rifinisci con la lima.</li>
</ol>
<h2>2. La fusione (blending)</h2>
<p>Fondere significa eliminare il <strong>gradino</strong> tra la fine dell'incavo e l'unghia naturale, così il prodotto passa sopra in modo liscio.</p>
${F('tip-fusione-step.svg', 'Fusione in sezione: dal gradino alla superficie continua, senza toccare la lamina.')}
<ol class="steps">
<li><strong>Lima fine</strong> (180–240), tenuta <strong>piatta</strong> sulla linea di contatto, non di taglio.</li>
<li><strong>Movimenti leggeri</strong> avanti e indietro solo sulla plastica dell'incavo, spostando sempre la lima. <em>Perché</em>: fermarsi in un punto crea un solco.</li>
<li><strong>Controlla con il dito e con la luce</strong>: lo scalino non si deve sentire né vedere.</li>
<li><strong>Opacizza tutto il tip</strong> leggermente, così la copertura aderisce anche sulla plastica.</li>
<li><strong>Elimina la polvere</strong> e disidrata la parte naturale.</li>
</ol>
<table>
<tr><th>Metodo</th><th>Pro</th><th>Contro</th></tr>
<tr><td><strong>Lima fine</strong></td><td>Controllo totale, nessun solvente</td><td>Serve pratica per non toccare la lamina</td></tr>
<tr><td><strong>Tip blender</strong> (liquido solvente)</td><td>Ammorbidisce la plastica e accelera la fusione</td><td>Solvente: può deformare o macchiare il tip; va usato pochissimo e solo sulla plastica</td></tr>
<tr><td><strong>Tip a contatto</strong></td><td>Non c'è niente da fondere</td><td>Legame più piccolo; serve una copertura ben costruita</td></tr>
</table>
${B('danger', 'La regola d\'oro', 'Si lima solo la plastica. Limare l\'unghia naturale durante la fusione la rende sottile, flessibile e sensibile al calore: è uno degli errori più frequenti e dannosi.')}
${B('warn', 'Il segno a "smile"', 'Se vedi una lunetta più chiara o più scavata dove finiva l\'incavo, hai limato la lamina. Fermati e non insistere su quel punto.')}
`,
          sources: ['https://open-exam-prep.com/study-guides/oh-nail-technician/artificial-nail-services/nail-tips-application',
            'https://open-exam-prep.com/study-guides/wa-nail-technician/tips-wraps-sculpting/nail-tips',
            'https://www.salongeek.com/threads/blending-with-file-or-tip-blender-liquid.61963/']
        },
        {
          id: 'copertura', simple: 'Il tip da solo è fragile: lo copri con il gel e costruisci una piccola "gobba" (apex) sopra il punto in cui l\'unghia si stacca dal dito.', title: 'Costruzione in gel sul tip', min: 11,
          html: `
<p>Il tip dà la <strong>lunghezza</strong>, la copertura dà la <strong>resistenza</strong>. Senza struttura la plastica si piega e si spezza proprio sopra il punto di stress.</p>
${F('tip-overlay-sezione.svg', 'Sezione: gel sottile alla cuticola, apex sopra il punto di stress, sottile in punta.')}
<h2>Procedimento</h2>
${F('tip-gel-step.svg', 'Copertura in gel sul tip in sei passaggi.')}
<ol class="steps">
<li><strong>Disidratante e primer</strong> solo sull'unghia naturale. <em>Perché</em>: il primer sul tip non serve e può rovinare la plastica.</li>
<li><strong>Base sottile</strong> su unghia e tip, a circa 1 mm dalla pelle (mai a contatto), sigillando il bordo libero. Polimerizza per il tempo indicato.</li>
<li><strong>Strato di aggancio</strong> (facoltativo, "slip layer"): un velo sottilissimo di costruttore su tutta l'unghia, non polimerizzato, aiuta la perla a scivolare.</li>
<li><strong>Perla al centro</strong>: prendi una perla di costruttore, appoggiala in zona 2 (poco dietro la linea dove finiva l'unghia naturale), accompagnala verso la cuticola senza toccare la pelle e poi "falla galleggiare" verso la punta.</li>
<li><strong>Capovolgi la mano</strong> della cliente per qualche secondo (da 5–10 secondi fino a circa 30, secondo la fluidità del gel): la gravità porta il gel verso il centro e forma l'apex. Riguarda di profilo e polimerizza.</li>
<li><strong>Secondo strato</strong> se l'apex non è abbastanza alto o se l'unghia è lunga; sigilla ogni volta il bordo libero.</li>
<li><strong>Rifinitura</strong>: cleaner sullo strato di dispersione, limatura (lunghezza, lati, punta, superficie), polvere via, top e polimerizzazione, olio.</li>
</ol>
<h2>Spessori indicativi</h2>
<table>
<tr><th>Zona</th><th>Spessore</th><th>Perché</th></tr>
<tr><td>Zona 3 (cuticola)</td><td>Sottilissimo, "a filo"</td><td>Si fonde con l'unghia e non si vede il gradino quando ricresce</td></tr>
<tr><td>Zona 2 (apex)</td><td>Il punto più spesso</td><td>Regge la leva della lunghezza</td></tr>
<tr><td>Zona 1 (bordo)</td><td>Circa 1–1,5 mm, come una carta di credito</td><td>Più spesso si nota e si impiglia; più sottile si scheggia</td></tr>
</table>
${B('tip', 'Perla piccola, poi aggiungi', 'Meglio due perle piccole che una grande: una perla grande, capovolgendo la mano, può colare verso i lati o la pelle.')}
<h2>Errori frequenti</h2>
<ul>
<li><strong>Copertura piatta</strong>: il tip si spezza dove finiva l'unghia naturale.</li>
<li><strong>Apex troppo avanti</strong>: fa da leva e tende a staccare l'unghia.</li>
<li><strong>Gel sulla pelle</strong>: sollevamenti e rischio di allergia. Pulisci prima di polimerizzare.</li>
<li><strong>Bordo libero non sigillato</strong>: lo strato si stacca dalla punta.</li>
<li><strong>Strati troppo spessi</strong>: picco di calore in lampada.</li>
</ul>
${B('warn', 'Controlla sempre di profilo', 'Prima di ogni polimerizzazione guarda la mano di lato: la linea deve salire dolcemente dalla cuticola, avere il punto più alto sopra il punto di stress e scendere verso la punta.')}
`,
          sources: ['https://www.ellisons.co.uk/blog/how-to-build-the-perfect-apex-with-the-gelbottle-inc',
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/nail-sculpting-forms',
            'https://www.katiebarnesacademy.com/blogs/preparation/what-is-the-difference-between-acid-free-and-acid-based-nail-primer']
        }
      ]
    },
    /* ------------------------------------------------------------------ 7 */
    {
      id: 'cartina', summary: ['Cartina a filo del bordo libero, in asse e in livello (né in su né in giù).', 'Zona 3 sottile (≈1 mm dalla pelle, mai sulla pelle), zona 2 apex, zona 1 ≈1–1,5 mm in punta.', 'Apex sopra il punto di stress: più lunga l\'unghia, più conta. Controlla sempre di profilo.', 'Bordo libero al massimo circa metà del letto ungueale.', 'Curva a C: segue l\'unghia naturale; pinching mai doloroso.'], n: 7, level: 'inter', title: 'Ricostruzione su cartina e apex',
      desc: 'Posizionare la cartina, costruire le 3 zone, l\'apex e la curva a C.',
      lessons: [
        {
          id: 'posizionamento', simple: 'La cartina è il "pavimento" su cui costruisci l\'allungamento: deve stare attaccata sotto l\'unghia, dritta e alla stessa altezza dell\'unghia.', title: 'Posizionare la cartina', min: 10,
          html: `
<p>Nella ricostruzione su cartina non c'è un tip: l'allungamento si costruisce "nel vuoto" sopra un supporto. La forma finale dipende moltissimo da come metti la cartina: <strong>una cartina storta dà un'unghia storta</strong>, e nessuna lima la raddrizza del tutto.</p>
<h2>Tipi di cartina</h2>
<table>
<tr><th>Tipo</th><th>Caratteristiche</th></tr>
<tr><td><strong>Cartine adesive monouso</strong> (carta o plastica)</td><td>Le più usate; hanno una griglia per misurare la lunghezza e una linea centrale. Si buttano dopo l'uso.</td></tr>
<tr><td><strong>Cartine riutilizzabili</strong> (metallo, teflon, plastica rigida)</td><td>Rigide, curve; vanno pulite e disinfettate dopo ogni cliente. Più difficili da adattare.</td></tr>
<tr><td><strong>Cartine per gel trasparenti</strong></td><td>Lasciano passare la luce della lampada anche da sotto.</td></tr>
</table>
<h2>Procedimento</h2>
${F('cartina-step.svg', 'Posizionare la cartina in quattro passaggi.')}
<ol class="steps">
<li><strong>Accorcia e prepara</strong> il bordo libero naturale: corto e regolare (lascia un piccolo bordo bianco se c'è). <em>Perché</em>: un bordo irregolare lascia spazi tra unghia e cartina.</li>
<li><strong>Stacca la cartina</strong> e piegala leggermente tra le dita per darle una curva simile a quella dell'unghia (curva a C).</li>
<li><strong>Adatta l'apertura</strong>: se il foro non segue la forma del bordo libero, ritaglialo con le forbicine.</li>
<li><strong>Infila</strong> la cartina sotto il bordo libero finché tocca l'unghia <strong>senza spazi</strong>, ma senza spingerla dentro l'iponichio (la pelle sotto l'unghia). <em>Perché</em>: spinta troppo fa male e ferisce un tessuto vivo.</li>
<li><strong>Allinea</strong> la linea centrale della cartina con il centro del dito, guardando dall'alto.</li>
<li><strong>Controlla il livello</strong> di profilo: la cartina deve continuare la linea della lamina, né verso il basso né verso l'alto.</li>
<li><strong>Chiudi le alette</strong>: prima unisci le due alette sotto il polpastrello, poi fai aderire i lati ai <em>lati</em> del dito, senza avvolgere tutta la falange. <em>Perché</em>: se attacchi tutto alla nocca, quando il dito si piega la cartina si stacca.</li>
</ol>
<h2>I tre controlli</h2>
${F('cartina.svg', 'Dall\'alto: cartina corretta, spazio sotto il bordo, fuori asse.')}
${F('cartina-livello.svg', 'Di profilo: cartina troppo bassa, giusta, troppo alta.')}
<table>
<tr><th>Vista</th><th>Che cosa guardi</th><th>Se è sbagliata</th></tr>
<tr><td><strong>Dall'alto</strong></td><td>Linea centrale della cartina = asse del dito; nessuno spazio tra bordo libero e cartina</td><td>Unghia storta; prodotto che cola sotto il bordo</td></tr>
<tr><td><strong>Di profilo</strong></td><td>La cartina prosegue la lamina in linea retta</td><td>Troppo bassa: allungamento che "cade". Troppo alta: punta all'insù (ski-jump)</td></tr>
<tr><td><strong>Dal davanti</strong></td><td>Curva della cartina simile alla curva dell'unghia, simmetrica</td><td>Curva a C storta o piatta</td></tr>
</table>
${B('tip', 'Come correggere', 'Per raddrizzare una cartina non staccarla tutta: muovi le alette nella direzione della correzione. Le scanalature (linee di crescita) della lamina sono una guida migliore del bordo libero, che può essere irregolare.')}
${B('warn', 'Errore classico', 'Uno spazio tra cartina e bordo libero fa colare il prodotto sotto l\'unghia: crea sollevamenti e un "gradino" difficile da correggere.')}
<h2>Errori frequenti</h2>
<ul>
<li><strong>Cartina ruotata verso il pollice</strong>: è l'errore più comune su anulare e mignolo. Guarda la mano dall'alto con le dita dritte.</li>
<li><strong>Alette chiuse in modo diverso</strong>: curva asimmetrica.</li>
<li><strong>Cartina spinta contro la pelle</strong>: dolore e prodotto steso male.</li>
<li><strong>Bordo libero non preparato</strong>: polvere e sebo anche sotto il bordo impediscono la saldatura.</li>
</ul>
`,
          sources: ['https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/nail-sculpting-forms',
            'https://www.youngnails.com/blogs/news/how-to-use-nail-forms',
            'https://www.nailpro.com/how-to-customize-nail-forms/']
        },
        {
          id: 'adattare-cartina', simple: 'Non tutte le unghie sono uguali: a volte devi ritagliare la cartina perché si appoggi bene, senza spazi e senza far male.', title: 'Adattare la cartina alle unghie difficili', min: 8,
          html: `
<p>La cartina standard è pensata per un'unghia "media": bordo libero regolare, curva normale, iponichio normale. Quando l'unghia è diversa, la cartina va <strong>tagliata su misura</strong>. Lo scopo resta sempre lo stesso: niente spazi, in asse, in livello, senza dolore.</p>
${F('cartina-adattata.svg', 'Quattro modi di ritagliare la cartina.')}
<table>
<tr><th>Situazione</th><th>Problema</th><th>Come adattare</th></tr>
<tr><td><strong>Unghia corta o morsicata</strong> (bordo dritto, niente bordo libero)</td><td>L'apertura curva della cartina lascia spazi ai lati</td><td>Taglia a metà la linguetta centrale e applicala dritta sotto il bordo; in alternativa ritaglia un'apertura dritta</td></tr>
<tr><td><strong>Unghia quadrata e larga</strong></td><td>Il foro è troppo stretto</td><td>Allarga l'apertura con le forbicine; per unghie molto larghe alcune formatrici usano due cartine unite</td></tr>
<tr><td><strong>Iponichio lungo</strong> (pelle che arriva sotto il bordo)</td><td>La cartina preme sulla pelle: dolore sulla linea del sorriso</td><td>Ritaglia un incavo curvo più profondo nel punto di contatto, così la cartina appoggia senza premere</td></tr>
<tr><td><strong>Unghia a pinza</strong> (molto curva)</td><td>La cartina resta più piatta dell'unghia</td><td>Piega di più la cartina prima di applicarla; segui la curva naturale, non forzarla ad aprirsi</td></tr>
<tr><td><strong>Ski-jump</strong> (punta che sale)</td><td>Seguendo il bordo, l'allungamento salirebbe</td><td>Segui le linee di crescita della lamina e posiziona la cartina un po' più in basso del bordo, per correggere il profilo</td></tr>
<tr><td><strong>Unghia che scende</strong> (bordo che punta in basso)</td><td>L'allungamento cadrebbe</td><td>Porta la cartina in linea con la lamina (non con il bordo), riempiendo l'eventuale spazio sotto con prodotto in più passaggi sottili</td></tr>
</table>
${F('cartina-ritaglio-step.svg', 'Esempio passo-passo: ritagliare l\'incavo per un iponichio lungo.')}
<ol class="steps">
<li><strong>Prova a secco</strong> la cartina e chiedi alla cliente se sente pressione.</li>
<li><strong>Segna</strong> con una matita dove la cartina tocca la pelle.</li>
<li><strong>Ritaglia</strong> una piccola curva in più in quel punto, poco per volta.</li>
<li><strong>Riprova</strong> finché la cartina tocca il bordo libero senza premere.</li>
<li><strong>Chiudi</strong> le alette e fai i tre controlli (alto, profilo, fronte).</li>
</ol>
${B('info', 'Quando la cartina non basta', 'Su unghie molto morsicate o con letto ungueale molto corto, a volte serve prima ricostruire il letto (vedi modulo "Onicofagia e unghie difficili"). Non promettere lunghezze che l\'unghia non può reggere.')}
${B('danger', 'Il dolore è un segnale', 'Se la cliente sente dolore con la cartina, è troppo spinta o preme su pelle viva. Togli e adatta: costruire sopra un punto doloroso non è mai accettabile.')}
`,
          sources: ['https://www.youngnails.com/blogs/news/how-to-use-nail-forms',
            'https://www.salongeek.com/threads/fitting-forms-with-high-hyponychium-advice-please.329807/',
            'https://www.nailpro.com/how-to-customize-nail-forms/',
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/nail-sculpting-forms']
        },
        {
          id: 'zone-apex', videos: [{"id": "Tx3lwXOS0L0", "title": "Do's and Don'ts of Apex Structure", "channel": "YoungNailsInc", "lang": "EN"}, {"id": "PD1qHAO3cvk", "title": "How to Build the Perfect Apex", "channel": "Liz Means Business", "lang": "EN"}], simple: 'Immagina un ponte: dove l\'unghia lascia il dito (punto di stress) serve il pilastro più alto, cioè l\'apex. Alla base e in punta il prodotto è sottile.', title: 'Le tre zone e l\'apex', min: 11,
          html: `
<p>Un'unghia allungata funziona come una <strong>leva</strong>: ogni volta che la punta urta qualcosa, la forza si scarica nel punto in cui l'unghia si stacca dal dito, il <strong>punto di stress</strong>. Per questo la ricostruzione non ha lo stesso spessore ovunque: è divisa in tre zone.</p>
${F('zone-costruzione.svg', 'Le tre zone di costruzione.')}
<h2>Le tre zone</h2>
<table>
<tr><th>Zona</th><th>Dove</th><th>Spessore</th><th>Perché</th></tr>
<tr><td><strong>Zona 1</strong> – bordo libero</td><td>Dall'allungamento fino alla linea del sorriso</td><td>Sottile e uniforme: circa 1–1,5 mm (come una carta di credito)</td><td>Più spesso si impiglia e sembra finto; più sottile si scheggia</td></tr>
<tr><td><strong>Zona 2</strong> – apex</td><td>Centro dell'unghia, sopra il punto di stress</td><td>La parte più spessa</td><td>Regge la leva della lunghezza</td></tr>
<tr><td><strong>Zona 3</strong> – zona cuticolare</td><td>Vicino a cuticola e solchi laterali</td><td>Sottilissima, sfumata "a zero"</td><td>Il prodotto deve fondersi con la lamina e non toccare mai la pelle</td></tr>
</table>
${F('zone-spessori-sezione.svg', 'Sezione longitudinale e trasversale: dove il prodotto è spesso e dove è sottile.')}
<h2>Il margine dalla pelle</h2>
<p>In zona 3 il prodotto si ferma a <strong>circa 1 mm</strong> da cuticola e solchi laterali (le fonti indicano da 0,5 a 1,5 mm; i manuali americani 1/16 di pollice, circa 1,6 mm) e non deve mai toccare la pelle. Questa sottile striscia di lamina scoperta non si vede a fine lavoro ma evita il contatto con la pelle, prima causa di sollevamenti e di allergie.</p>
<h2>Dove sta esattamente l'apex</h2>
<ul>
<li>Dall'alto: al <strong>centro</strong> dell'unghia, tra i due lati.</li>
<li>Di profilo: sopra il <strong>punto di stress</strong>, cioè all'incirca nel terzo posteriore-centrale dell'unghia intera (letto + allungamento).</li>
<li>È un <strong>punto</strong> morbido, non una "fascia" spessa che attraversa tutta l'unghia.</li>
</ul>
${F('apex-confronto.svg', 'Apex corretto e due errori tipici.')}
<table>
<tr><th>Errore</th><th>Che cosa succede</th></tr>
<tr><td><strong>Unghia piatta</strong> (nessun apex)</td><td>Si crepa o si spezza al centro, sulla linea del punto di stress</td></tr>
<tr><td><strong>Apex troppo avanti</strong></td><td>Fa da leva: tende a staccare l'unghia dal letto</td></tr>
<tr><td><strong>Apex troppo indietro / gobba alla cuticola</strong></td><td>Aspetto grosso, sollevamenti alla base, nessun sostegno dove serve</td></tr>
<tr><td><strong>Apex spostato su un lato</strong></td><td>L'unghia si rompe sul lato più sottile</td></tr>
</table>
<h2>Come controllarlo</h2>
${F('apex-controllo-viste.svg', 'Controllo dell\'apex da tre punti di vista.')}
<ol class="steps">
<li><strong>Di profilo</strong>: la linea sale dolcemente dalla cuticola, raggiunge il punto più alto sopra il punto di stress e scende in modo regolare verso la punta.</li>
<li><strong>Dal davanti</strong> (guardando la punta verso di te): lo spessore è uguale a destra e a sinistra, la curva è regolare.</li>
<li><strong>Dall'alto, con luce</strong>: il riflesso della lampada scorre senza "salti" e mostra il punto più alto al centro.</li>
<li><strong>Dal basso</strong>: il bordo libero è sottile e uniforme.</li>
</ol>
${B('tip', 'Il trucco del riflesso', 'Ruota lentamente il dito sotto la lampada: una striscia di luce continua e regolare indica una superficie ben costruita; una luce che si spezza indica avvallamenti o gobbe.')}
`,
          sources: ['https://open-exam-prep.com/study-guides/oh-nail-technician/artificial-nail-services/sculptured-acrylic-nails',
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/nail-sculpting-forms',
            'https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-file-different-nail-shapes',
            'https://www.scratchmagazine.co.uk/blog/simply-salon-nails-perfecting-proper-nail-structure/']
        },
        {
          id: 'proporzioni', simple: 'Più lunga è l\'unghia, più forte deve essere la struttura. Per un risultato equilibrato, la punta non dovrebbe superare circa metà della lunghezza del letto.', title: 'Lunghezza e proporzioni', min: 7,
          html: `
<p>Prima di costruire si decide la <strong>lunghezza</strong>. Non è solo una questione di gusto: la lunghezza cambia la leva sul punto di stress e quindi la struttura necessaria.</p>
<h2>La regola della metà</h2>
${F('lunghezza-proporzioni.svg', 'Proporzioni: bordo libero fino a circa metà del letto ungueale.')}
<ul>
<li>Misura il <strong>letto ungueale</strong> (la parte rosa, dalla cuticola alla linea del sorriso).</li>
<li>Per un'unghia equilibrata e resistente, il <strong>bordo libero</strong> (la parte che sporge) non dovrebbe superare circa <strong>metà</strong> di questa lunghezza.</li>
<li>Alcune formatrici preferiscono circa <strong>un terzo</strong> per un aspetto più naturale, soprattutto nel french con bianco molto acceso.</li>
<li>Su letti ungueali corti si può "allungare il letto" con gel/polvere cover rosa, invece di aggiungere bianco.</li>
</ul>
${B('info', 'Regole, non leggi', 'Le fonti professionali indicano un massimo di metà letto, alcune di un terzo. Nelle gare e negli stili "moda" le lunghezze possono essere molto maggiori, ma richiedono strutture e apex più importanti.')}
<h2>Più lunghezza = più struttura</h2>
${F('apex-lunghezza.svg', 'Unghia corta e unghia lunga: l\'apex cresce e resta sopra il punto di stress.')}
<table>
<tr><th>Lunghezza</th><th>Struttura</th><th>Adatta a</th></tr>
<tr><td>Corta (bordo ≤ 1/3 del letto)</td><td>Apex leggero, quasi naturale</td><td>Chi lavora molto con le mani, prime clienti</td></tr>
<tr><td>Media (circa 1/2 del letto)</td><td>Apex ben visibile di profilo</td><td>Uso quotidiano in salone</td></tr>
<tr><td>Lunga (oltre 1/2)</td><td>Apex alto, curva a C più marcata</td><td>Clienti abituate, eventi, gare</td></tr>
</table>
<h2>Come decidere con la cliente</h2>
<ol class="steps">
<li><strong>Chiedi</strong> che lavoro fa, se usa tastiera o attrezzi, se fa sport.</li>
<li><strong>Guarda il letto ungueale</strong>: corto, lungo, morsicato?</li>
<li><strong>Proponi</strong> una lunghezza di partenza prudente: si può allungare al refill successivo.</li>
<li><strong>Segna</strong> la lunghezza sulla griglia della cartina, uguale per tutte le dita (il pollice può essere leggermente più lungo e il mignolo leggermente più corto, a parità di aspetto).</li>
</ol>
${B('warn', 'Prima volta', 'Alla prima ricostruzione la cliente non è abituata: una lunghezza eccessiva aumenta il rischio di urti, rotture e traumi al letto ungueale.')}
`,
          sources: ['https://www.salongeek.com/threads/choosing-the-correct-length-for-balance-and-beauty.11417/',
            'https://www.scratchmagazine.co.uk/blog/simply-salon-nails-perfecting-proper-nail-structure/',
            'https://open-exam-prep.com/study-guides/oh-nail-technician/artificial-nail-services/sculptured-acrylic-nails']
        },
        {
          id: 'curva-c', simple: 'Guardando l\'unghia dalla punta deve sembrare un piccolo arco, come una "C" sdraiata. Un arco regge più di una lastra piatta.', title: 'La curva a C (pinching)', min: 9,
          html: `
${F('curva-c.svg', 'La curva a C vista dal bordo libero.')}
<p>La curva a C è la curvatura <strong>trasversale</strong> della ricostruzione, cioè da un lato all'altro, vista dalla punta. Come un foglio di carta che, piegato ad arco, regge un peso che da piatto non reggerebbe, la curva dà <strong>resistenza laterale</strong> e un aspetto naturale e slanciato.</p>
<h2>Quanta curva?</h2>
<p>La curva si misura spesso come <strong>percentuale di un cerchio</strong>: 50% = mezzo cerchio.</p>
${F('curva-c-percentuali.svg', 'Curva a C espressa in percentuale di cerchio.')}
<table>
<tr><th>Curva</th><th>Dove si usa</th></tr>
<tr><td>Bassa (circa 25–35%)</td><td>Unghie naturalmente piatte, unghie corte</td></tr>
<tr><td>Media (circa 35–45%)</td><td>Uso quotidiano in salone</td></tr>
<tr><td>Alta (circa 50–55%)</td><td>Gare, unghie lunghe</td></tr>
</table>
${B('info', 'Valori indicativi', 'Le guide d\'esame americane citano circa 35–45% per il lavoro in salone; le riviste di settore indicano circa 50–55% per le gare. Non esiste un valore valido per tutti: si parte sempre dalla curva naturale della cliente e si cerca che sia uguale su tutte e dieci le unghie.')}
<h2>Tre modi per ottenere la curva</h2>
<ol class="steps">
<li><strong>Con la cartina</strong>: dai la curva giusta alla cartina prima di costruire. È il metodo più sicuro per le principianti.</li>
<li><strong>Con il prodotto</strong>: lati paralleli e spessore uniforme in sezione aiutano la curva.</li>
<li><strong>Con il pinching</strong>: una pressione laterale controllata mentre il prodotto è ancora un po' morbido.</li>
</ol>
<h2>Pinching passo passo</h2>
${F('curva-c-pinching-step.svg', 'Pinching: posizione delle dita, momento giusto, controllo frontale.')}
<ol class="steps">
<li><strong>Il momento</strong>: <em>acrilico</em> quando ha perso la lucidità ma è ancora leggermente morbido; <em>gel</em> dopo una polimerizzazione brevissima (flash cure, pochi secondi secondo il produttore), poi si completa la polimerizzazione.</li>
<li><strong>Dove</strong>: pollici o pinzetta sui lati dell'allungamento, all'altezza del punto di stress o poco più avanti, mai sopra la lamina naturale.</li>
<li><strong>Come</strong>: pressione uguale sui due lati, per pochi secondi, chiedendo alla cliente come si sente.</li>
<li><strong>Controlla</strong> dal davanti: curva simmetrica, nessuna crepa ai lati.</li>
</ol>
${B('danger', 'Mai dolore', 'Il pinching non deve far male né staccare la lamina dal letto. Se la cliente sente dolore, smetti subito: una curva forzata su un\'unghia piatta può causare onicolisi.')}
<h2>Errori frequenti</h2>
<ul>
<li><strong>Pinching troppo tardi</strong> (acrilico già duro): crepe sui lati.</li>
<li><strong>Pressione diversa sui due lati</strong>: curva storta, unghia che "gira".</li>
<li><strong>Pinching sul letto ungueale</strong>: dolore e rischio di distacco.</li>
<li><strong>Curve diverse tra le dita</strong>: la mano sembra disordinata.</li>
</ul>
${B('tip', 'Strumenti', 'Esistono pinzette e "bastoncini per curva a C". Le pinze trasparenti sono preferibili con il gel perché lasciano passare la luce. In alcune gare le pinze sono vietate: controlla sempre il regolamento.')}
`,
          sources: ['https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/nail-sculpting-forms',
            'https://open-exam-prep.com/study-guides/oh-nail-technician/artificial-nail-services/sculptured-acrylic-nails',
            'https://www.nailpro.com/technique/article/21156099/competition-technique-how-to-pre-shape-a-c-curve',
            'https://purespadirect.com/blogs/pure-spa-direct-blog/how-to-achieve-the-perfect-c-curve-using-professional-pinching-tools-a-nail-techs-guide-to-strength-style']
        },
        {
          id: 'tutorial-gel', videos: [{"id": "ilkQqQbeCQQ", "title": "Ricostruzione unghie con cartine e gel: ogni passaggio spiegato", "channel": "Valeriya Nails", "lang": "IT"}, {"id": "jOJjB8vjEg0", "title": "Sculpting Gel Nails – Step by Step", "channel": "Nail Career Education", "lang": "EN"}], simple: 'Prepari l\'unghia, metti la cartina, disegni la punta con il gel, costruisci l\'apex, togli la cartina e limi: un passaggio alla volta, con la lampada dopo ogni strato.', title: 'Tutorial completo: gel su cartina', min: 14,
          html: `
<p>Questo tutorial mette insieme tutto ciò che hai studiato: preparazione, cartina, tre zone, apex e rifinitura. Esercitati prima su una mano da allenamento. I tempi di polimerizzazione dipendono dal tuo gel e dalla tua lampada: <strong>usa sempre quelli del produttore</strong>.</p>
${F('tut-gel-cartina.svg', 'Ricostruzione in gel su cartina in otto passaggi.')}
<h2>Materiale</h2>
<ul>
<li>Lime 180/240 e 100/180, buffer, pennello per polveri, spingicuticole</li>
<li>Disidratante, primer, base, gel costruttore (trasparente, rosa o cover), top, cleaner, olio</li>
<li>Cartine, pennello piatto o ovale per gel, lampada abbinata al gel</li>
<li>Guanti in nitrile, salviette senza pelucchi</li>
</ul>
<h2>Procedimento</h2>
<ol class="steps">
<li><strong>Prepara</strong>: igiene, cuticola, opacizzazione 180–240, polvere via, disidratante e primer solo sulla lamina.</li>
<li><strong>Cartina</strong>: a filo del bordo libero, in asse e in livello, alette chiuse. Fai i tre controlli.</li>
<li><strong>Base</strong>: uno strato sottile su tutta la lamina e sul bordo libero, a circa 1 mm dalla pelle. Polimerizza.</li>
<li><strong>Zona 1 – disegna la punta</strong> (vedi figura sotto): con poco costruttore traccia l'allungamento sulla cartina, sottile, con i lati dritti e paralleli che proseguono i solchi laterali, alla lunghezza scelta. Polimerizza brevemente (o completamente, secondo il produttore). <em>Perché</em>: la punta sottile e già indurita fa da "pavimento" per lo strato strutturale.</li>
<li><strong>Zona 2 – la perla</strong>: appoggia una perla di gel al centro, sopra il punto di stress. Accompagnala verso la cuticola fermandoti a circa 1 mm dalla pelle, poi verso la punta e i lati senza premere.</li>
<li><strong>Capovolgi</strong> la mano per alcuni secondi (circa 5–10; fino a 30 con gel densi): il gel scorre verso l'apex. Rigira la mano, controlla di profilo e dal davanti, poi polimerizza.</li>
<li><strong>Se serve</strong>, ripeti con una seconda perla piccola per alzare l'apex.</li>
<li><strong>Togli la cartina</strong>: apri le alette, stringi leggermente la cartina e sfilala verso il basso. Se vuoi più curva, fai il pinching dopo un flash cure (prima della polimerizzazione completa dello strato strutturale).</li>
<li><strong>Cleaner</strong> sullo strato di dispersione, poi <strong>limatura</strong>: lunghezza, lati, punta, superficie, sotto il bordo libero (vedi modulo "Limatura e forme").</li>
<li><strong>Top</strong>: steso sottile, sigillando anche il bordo libero; polimerizza, cleaner se il top non è "no-wipe", olio sulle cuticole.</li>
</ol>
${F('tut-gel-zona1.svg', 'Zona 1 in gel: lati dritti che proseguono i solchi, lunghezza segnata sulla griglia.')}
${F('tut-gel-flip.svg', 'Il "capovolgimento": la gravità porta il gel verso l\'apex.')}
${F('zone-spessori-sezione.svg', 'Controllo finale: sottile alla cuticola, spesso sull\'apex, sottile in punta.')}
<h2>Problemi durante il lavoro</h2>
<table>
<tr><th>Problema</th><th>Causa probabile</th><th>Rimedio</th></tr>
<tr><td>Il gel cola nei solchi</td><td>Perla troppo grande o gel troppo fluido; mano capovolta troppo a lungo</td><td>Perle più piccole; pulisci con un pennello prima della lampada</td></tr>
<tr><td>Bruciore in lampada</td><td>Strato spesso, lamina sottile</td><td>Togli la mano qualche secondo e rientra ("flash and pull"); strati più sottili</td></tr>
<tr><td>Allungamento storto dopo aver tolto la cartina</td><td>Cartina fuori asse</td><td>Correggi in limatura; la prossima volta controlla dall'alto</td></tr>
<tr><td>Bolle</td><td>Pennello agitato o gel mescolato con forza</td><td>Movimenti lenti, gel a temperatura ambiente</td></tr>
</table>
${B('tip', 'Checklist finale', 'Profilo con apex sopra il punto di stress · curva a C regolare · zona cuticolare pulita e sottile · bordo libero sottile (≈1–1,5 mm) e sigillato · lati dritti · nessuna sbavatura sulla pelle.')}
`,
          sources: ['https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/nail-sculpting-forms',
            'https://www.ellisons.co.uk/blog/how-to-build-the-perfect-apex-with-the-gelbottle-inc',
            'https://www.nsinails.com.au/blogs/news/nail-preparation']
        },
        {
          id: 'tutorial-acrilico', videos: [{"id": "yVuhQ9Nh43M", "title": "Tutorial applicazione acrilico", "channel": "Nail Couture Italia", "lang": "IT"}, {"id": "-xLyP7jYlMA", "title": "Come realizzare un allungamento in acrilico", "channel": "Nailover International", "lang": "IT"}], simple: 'Con l\'acrilico mescoli un liquido e una polvere con il pennello: si forma una pallina (perla) che indurisce all\'aria. Lavori zona per zona: punta, centro, base.', title: 'Tutorial completo: acrilico su cartina', min: 14,
          html: `
<p>Con l'acrilico il prodotto indurisce all'aria: lavora con ordine e con la perla giusta. Indossa guanti in nitrile, occhiali e accendi l'aspiratore. Usa solo monomeri <strong>EMA</strong> professionali (mai MMA).</p>
<h2>La perla: il rapporto liquido/polvere</h2>
${F('perla-acrilico.svg', 'Prima di iniziare: controlla la consistenza della perla.')}
<table>
<tr><th>Perla</th><th>Rapporto liquido : polvere</th><th>Comportamento</th></tr>
<tr><td><strong>Asciutta</strong></td><td>circa 1 : 1</td><td>Granulosa, opaca, difficile da stendere; indurisce troppo in fretta; fragile e si solleva</td></tr>
<tr><td><strong>Media</strong> ✓</td><td>circa 1,5 : 1</td><td>Lucida, bombata, resta "a cupola" sul pennello per qualche secondo; si lavora bene</td></tr>
<tr><td><strong>Bagnata</strong></td><td>circa 2 : 1</td><td>Cola nei solchi e verso la cuticola, si ritira (shrinkage), aumenta il rischio di sensibilizzazione</td></tr>
</table>
${B('info', 'Dipende dal sistema', 'Il rapporto 1,5 : 1 è un riferimento per molti sistemi EMA, non una legge: ogni marchio formula il suo monomero per un certo rapporto. Leggi le istruzioni del produttore.')}
<h2>Procedimento</h2>
${F('tut-acrilico.svg', 'Ricostruzione in acrilico su cartina in sei passaggi.')}
<ol class="steps">
<li><strong>Prepara</strong> l'unghia e posiziona la cartina (vedi lezioni precedenti). Primer solo sulla lamina; se è acido, aspetta che sia bianco gessoso.</li>
<li><strong>Zona 1</strong>: immergi il pennello nel monomero, scaricalo sul bordo del dappen, tocca la polvere (bianca per il french, trasparente o rosa per il naturale) e appoggia la perla sulla cartina all'altezza del bordo libero.</li>
<li><strong>Modella la punta</strong> con il ventre del pennello, picchiettando e accarezzando: lunghezza, lati dritti e paralleli, spessore uniforme. Per il french disegna la smile line con la punta del pennello.</li>
<li><strong>Zona 2</strong>: perla media al centro, sopra il punto di stress. Fondila verso la zona 1 e verso i lati: qui costruisci l'apex.</li>
<li><strong>Zona 3</strong>: perla piccola e leggermente più umida, stesa sottilissima verso la cuticola, fermandoti a circa 1 mm dalla pelle e dai solchi.</li>
<li><strong>Pinching</strong> quando il prodotto ha perso la lucidità ma è ancora leggermente morbido.</li>
<li><strong>Verifica l'indurimento</strong>: battendo con il manico del pennello devi sentire un "click" secco.</li>
<li><strong>Togli la cartina</strong> e <strong>lima</strong>: lunghezza, lati, punta, superficie; controlla l'apex di profilo. Leviga, togli la polvere, top o lucidatura, olio.</li>
</ol>
${F('acrilico-pennello-carico.svg', 'Come si carica il pennello: immergi, scarica, tocca la polvere, aspetta la perla.')}
${F('perla-zone-acrilico.svg', 'Dove appoggiare le tre perle e quanto devono essere grandi.')}
${B('warn', 'Pulizia del pennello', 'Pulisci il pennello nel monomero e asciugalo su carta tra una perla e l\'altra; non toccare mai il monomero con la pelle. Il monomero usato va eliminato secondo le istruzioni, non rimesso nel flacone.')}
<h2>Errori frequenti</h2>
<table>
<tr><th>Errore</th><th>Conseguenza</th><th>Correzione</th></tr>
<tr><td>Perla bagnata in zona 3</td><td>Cola sulla cuticola: sollevamento e rischio di allergia</td><td>Perla più asciutta, scarica il pennello</td></tr>
<tr><td>Perla asciutta in zona 1</td><td>Bolle, opacità, punta fragile</td><td>Più monomero nel pennello</td></tr>
<tr><td>Prodotto sulla pelle o sulla cuticola</td><td>Sollevamento in pochi giorni</td><td>Rimuovi subito con il pennello pulito, prima che indurisca</td></tr>
<tr><td>Apex piatto o troppo avanti</td><td>Crepa al centro o leva sul letto</td><td>Perla di zona 2 centrata sopra il punto di stress</td></tr>
<tr><td>Troppo prodotto in una volta su unghia sottile</td><td>Calore durante l'indurimento</td><td>Perle più piccole, lavoro per strati</td></tr>
</table>
`,
          sources: ['https://open-exam-prep.com/study-guides/oh-nail-technician/artificial-nail-services/sculptured-acrylic-nails',
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/nail-sculpting-forms',
            'https://nsinails.com.au/blogs/news/mix-ratio-l-p',
            'https://www.katiebarnesacademy.com/blogs/nail-structure-application/understanding-acrylic-chemistry-mix-ratio']
        }
      ]
    },
    /* ------------------------------------------------------------------ 8 */
    {
      id: 'limatura', summary: ['Squoval: tra le forme più resistenti; mandorla: slancia il dito.', 'Ordine: lunghezza → lati → punta → superficie → sotto il bordo → rifinitura.', 'Lati dritti e paralleli; punta dai lati verso il centro, in una sola direzione.', 'Unghia naturale: grana 180–240; 100/180 solo sul prodotto.', 'Controlla da 4 punti di vista: alto, profilo, fronte, sotto.'], n: 8, level: 'inter', title: 'Limatura e forme',
      desc: 'Le forme dell\'unghia e la tecnica di limatura per un risultato pulito.',
      lessons: [
        {
          id: 'forme', videos: [{"id": "a4NPD2HqrRc", "title": "Limatura: forma quadrata, mandorla e squoval", "channel": "Aerrenails", "lang": "IT"}, {"id": "z3OaoVY-jAM", "title": "Limatura ovale delle unghie", "channel": "Accademia Nails", "lang": "IT"}], simple: 'La forma si sceglie con la cliente guardando le sue dita e il suo stile di vita: più la forma è appuntita, più è delicata.', title: 'Le forme dell\'unghia', min: 10,
          html: `
${F('forme.svg', 'Le forme principali.')}
<p>La forma dell'unghia si decide <strong>prima</strong> di costruire: cambia come metti la cartina, dove fai l'apex e come limi. Una buona forma è <strong>simmetrica</strong>, adatta al dito e alle abitudini della cliente.</p>
<h2>Le forme principali</h2>
<table>
<tr><th>Forma</th><th>Com'è</th><th>Effetto sul dito</th><th>Resistenza</th><th>Consigliata per</th></tr>
<tr><td>Quadrata</td><td>Lati paralleli, punta dritta, angoli netti</td><td>Accorcia e allarga visivamente</td><td>Buona al centro, angoli che si impigliano e si scheggiano</td><td>Dita lunghe e sottili</td></tr>
<tr><td>Squoval</td><td>Quadrata con angoli smussati</td><td>Neutro</td><td>Tra le più resistenti</td><td>Quasi tutte; chi usa molto le mani</td></tr>
<tr><td>Tonda</td><td>Segue la curva del polpastrello</td><td>Naturale</td><td>Molto pratica: pochi punti che si impigliano</td><td>Unghie corte, uomini, sport</td></tr>
<tr><td>Ovale</td><td>Lati paralleli che si chiudono in un arco morbido</td><td>Allunga leggermente</td><td>Buona</td><td>Effetto elegante, dita corte</td></tr>
<tr><td>Mandorla</td><td>Lati che convergono, punta arrotondata più stretta dell'ovale</td><td>Slancia molto</td><td>Media: la punta è più stretta</td><td>Dita corte o larghe</td></tr>
<tr><td>Stiletto</td><td>Lati dritti che si incontrano a punta</td><td>Molto slanciante</td><td>La più delicata</td><td>Look deciso; richiede lunghezza e struttura</td></tr>
<tr><td>Ballerina / coffin</td><td>Lati che si restringono, punta piatta</td><td>Slancia</td><td>Media; richiede lunghezza</td><td>Lunghezze medio-lunghe</td></tr>
<tr><td>Lipstick</td><td>Punta tagliata in obliquo come un rossetto</td><td>Moda</td><td>Media</td><td>Look moda</td></tr>
<tr><td>Edge</td><td>Base quadrata con una cresta centrale e angoli appuntiti</td><td>Moda, scultoreo</td><td>Delicata; tecnica avanzata</td><td>Gare, look moda</td></tr>
</table>
${B('info', 'Nomi che cambiano', 'Alcune forme hanno descrizioni diverse a seconda delle fonti (per esempio la lipstick o la differenza tra ovale e mandorla). Quando una cliente chiede una forma "di moda", fatti mostrare una foto.')}
<h2>Come scegliere con la cliente</h2>
${F('forme-scelta-dita.svg', 'La stessa forma su dita diverse: come cambia l\'effetto.')}
<ol class="steps">
<li><strong>Abitudini</strong>: lavora con le mani, usa la tastiera, fa sport? Più è attiva, più conviene squoval, tonda o ovale corta.</li>
<li><strong>Dita</strong>: dita corte o larghe si slanciano con ovale e mandorla; dita lunghe e sottili stanno bene anche quadrate.</li>
<li><strong>Cuticola</strong>: molte formatrici consigliano di riprendere la forma della cuticola nella punta (cuticola tonda → punta tonda/ovale; cuticola squadrata → squoval).</li>
<li><strong>Letto ungueale</strong>: forme a punta (mandorla, stiletto, ballerina) richiedono lunghezza; su letti corti diventano fragili.</li>
<li><strong>Prima volta</strong>: proponi una forma semplice; si può cambiare al refill.</li>
</ol>
${F('forme-resistenza.svg', 'Dalla più resistente alla più delicata.')}
<h2>Esempio: ottenere una mandorla</h2>
${F('forme-limatura-step.svg', 'Dalla quadrata alla mandorla in quattro passaggi.')}
${B('tip', 'Scegli con la cliente', 'Considera lavoro, abitudini e forma del letto ungueale: una stiletto lunga non è adatta a chi lavora molto con le mani.')}
${B('warn', 'Le forme si costruiscono, non solo si limano', 'Una forma riesce bene se la prepari già con la cartina e con il prodotto (lati dritti, apex al posto giusto). La lima rifinisce: se il prodotto è stato messo male, limando assottigli i punti sbagliati.')}
`,
          sources: ['https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-file-different-nail-shapes',
            'https://www.makeup.com/your-nail-shape-guide',
            'https://www.livethatglow.com/nail-shape-guide/',
            'https://www.my-personaltrainer.it/bellezza/qual-e-la-forma-di-unghie-che-slancia-le-dita-e-resiste-davvero-agli-urti-senza-spezzarsi.html']
        },
        {
          id: 'forme-step', simple: 'Quasi tutte le forme partono da una quadrata: prima fai lati dritti e punta dritta, poi togli gli angoli quanto serve per arrivare alla forma voluta.', title: 'Limare le forme passo passo', min: 12,
          html: `
<p>Il metodo più semplice per una principiante è <strong>partire sempre da una base quadrata</strong>, con lati dritti e paralleli e la punta dritta. Da lì, togliendo gli angoli in modo diverso, si arriva a tutte le altre forme.</p>
${B('tip', 'Prima di iniziare', 'Segna il centro della punta con un puntino (pennarello o una goccia di gel polimerizzata): è il riferimento per la simmetria. Lavora con lima 100/180 sul prodotto e rifinisci con 180.')}
<h2>La base: la quadrata</h2>
${F('quadrata-step.svg', 'La quadrata: punta dritta, lati paralleli, angoli netti.')}
<ol class="steps">
<li><strong>Punta</strong>: lima perfettamente dritta, perpendicolare all'asse del dito, guardando dall'alto.</li>
<li><strong>Lati</strong>: lima tenuta piatta e parallela al solco laterale; i due lati devono essere paralleli tra loro e proseguire i solchi.</li>
<li><strong>Arco inferiore</strong>: gira il dito di lato e controlla che la linea sotto l'allungamento sia dritta, senza "pance".</li>
<li><strong>Angoli</strong>: netti e uguali.</li>
</ol>
<h2>Squoval</h2>
<ol class="steps">
<li>Parti dalla quadrata.</li>
<li>Inclina la lima <strong>sotto ogni angolo</strong> e con 2–3 passate leggere smussalo.</li>
<li>Controlla che i due angoli abbiano la stessa curva.</li>
</ol>
<h2>Ovale e tonda</h2>
${F('ovale-step.svg', 'Ovale: dai lati verso il centro, seguendo la curva della cuticola.')}
<ol class="steps">
<li>Parti dalla quadrata, con il puntino al centro.</li>
<li>Tieni la lima a circa <strong>45°</strong> rispetto alla punta e lima <strong>da un lato verso il centro</strong>, in una sola direzione.</li>
<li>Ripeti dall'altro lato con lo stesso numero di passate.</li>
<li>Arrotonda la punta: per la <em>tonda</em> segui la curva del polpastrello e resta corta; per l'<em>ovale</em> lascia i lati paralleli più lunghi e chiudi con un arco morbido, specchio della cuticola.</li>
</ol>
<h2>Mandorla e stiletto</h2>
${F('stiletto-step.svg', 'Mandorla e stiletto: lati che convergono sull\'asse.')}
<ol class="steps">
<li>Parti dalla quadrata e traccia l'asse centrale.</li>
<li>Lima un lato in diagonale verso il puntino centrale, poi l'altro con <strong>lo stesso angolo</strong>.</li>
<li><strong>Mandorla</strong>: arrotonda la punta, che resta più stretta di un'ovale.</li>
<li><strong>Stiletto</strong>: continua finché i lati si incontrano a punta; tieni i lati dritti, non "a pancia". Gira il dito di lato e mantieni dritto anche l'arco inferiore.</li>
</ol>
<h2>Ballerina (coffin)</h2>
${F('ballerina-step.svg', 'Ballerina: lati che si restringono e punta dritta.')}
<ol class="steps">
<li>Parti da una quadrata lunga.</li>
<li>Lima i due lati in diagonale verso il centro, come per una stiletto, ma <strong>fermati prima</strong>.</li>
<li>Taglia la punta dritta, perpendicolare all'asse, con lima tenuta a 90°.</li>
<li>Controlla: lati uguali, punta centrata, angoli netti e uguali.</li>
</ol>
${B('info', 'La forma dipende anche dal profilo', 'Nelle forme a punta (mandorla, stiletto, ballerina) l\'arco superiore deve scendere dritto dall\'apex alla punta: limare solo dall\'alto senza guardare il profilo crea punte deboli.')}
<h2>Errori frequenti</h2>
<table>
<tr><th>Errore</th><th>Causa</th><th>Correzione</th></tr>
<tr><td>Punta spostata da un lato</td><td>Un lato limato più dell'altro</td><td>Usa il puntino al centro; conta le passate</td></tr>
<tr><td>Lati "a pancia"</td><td>Lima inclinata o che ruota</td><td>Lima piatta, polso fermo</td></tr>
<tr><td>Forme diverse sulle 10 dita</td><td>Nessun confronto</td><td>Allinea le dita e guarda la mano intera ogni 2–3 unghie</td></tr>
<tr><td>Stiletto che si spezza</td><td>Punta troppo sottile, arco inferiore limato</td><td>Mantieni spessore verso la punta; costruisci la forma già con il prodotto</td></tr>
</table>
`,
          sources: ['https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-file-different-nail-shapes',
            'https://www.homeofnailart.com/blogs/knowledge-hub/mastering-the-art-of-nail-filing-a-comprehensive-guide-for-professional-nail-technicians',
            'https://www.scratchmagazine.co.uk/blog/simply-salon-nails-filing-different-nail-shapes/']
        },
        {
          id: 'tecnica', videos: [{"id": "UGpcsTGXAUI", "title": "Sculpting Gel Nails – Advanced Filing", "channel": "Nail Career Education", "lang": "EN"}], simple: 'Lima sempre nello stesso ordine: lunghezza, lati, punta, superficie, sotto il bordo. Movimenti leggeri, in una direzione, senza segare.', title: 'Tecnica di limatura', min: 11,
          html: `
<p>La limatura trasforma una costruzione "grezza" in un'unghia pulita e simmetrica. Ma la lima non fa miracoli: se la struttura è sbagliata, limando si assottigliano i punti deboli. Lavora con <strong>ordine</strong>, <strong>leggerezza</strong> e controlla spesso.</p>
<h2>Come tenere lima e dito</h2>
${F('lima-presa.svg', 'Presa della lima e del dito della cliente.')}
<ul>
<li><strong>La lima</strong>: tienila con pollice da un lato e due-tre dita dall'altro, senza stringere; il polso resta morbido. Il movimento parte dal braccio, non solo dalle dita.</li>
<li><strong>Il dito della cliente</strong>: tienilo tra pollice e indice ai lati, sotto la prima falange, senza toccare la superficie dell'unghia. Con il pollice puoi tirare leggermente indietro la pelle del solco laterale per vedere meglio dove limi.</li>
<li><strong>Il supporto</strong>: il polso della cliente appoggia su un cuscinetto, così né tu né lei sostenete il peso della mano.</li>
</ul>
<h2>Quale lima per cosa</h2>
<table>
<tr><th>Lima</th><th>Uso</th></tr>
<tr><td>100/180</td><td>Accorciare e dare forma al <strong>prodotto</strong></td></tr>
<tr><td>180</td><td>Rifinire forma e superficie, "lucidare" la struttura</td></tr>
<tr><td>180/240 – buffer</td><td>Levigare prima del top; lavorare vicino alla pelle</td></tr>
<tr><td>Mai</td><td>Grane 80–100 sull'unghia naturale</td></tr>
</table>
<h2>La sequenza</h2>
${F('limatura-sequenza.svg', 'La sequenza di limatura in sei passaggi.')}
<ol class="steps">
<li><strong>Lunghezza</strong>: accorcia con 100/180 tenendo la lima perpendicolare alla punta. Porta tutte le unghie alla lunghezza decisa prima di fare la forma. <em>Perché</em>: la forma si decide sulla lunghezza finale.</li>
<li><strong>Lati</strong>: lima piatta e parallela al solco laterale, dalla punta verso la base, senza entrare nel solco. I due lati devono essere dritti, paralleli e uguali.</li>
<li><strong>Punta</strong>: forma la punta (vedi "Limare le forme passo passo"), dai lati verso il centro, sempre nella stessa direzione.</li>
<li><strong>Superficie</strong>: movimenti lunghi e leggeri dalla zona cuticolare verso la punta, seguendo la curva come se "rotolassi" la lima da un lato all'altro. Rendi sottile la zona 3, mantieni l'apex, assottiglia la zona 1. Controlla di profilo.</li>
<li><strong>Zona cuticolare</strong>: con la parte stretta della lima o un buffer, sfuma il prodotto fino a renderlo invisibile, senza toccare la pelle.</li>
<li><strong>Sotto il bordo libero</strong>: pulisci con la lima inclinata, togliendo sbavature e residui.</li>
<li><strong>Rifinitura</strong>: buffer, polvere via con pennello, cleaner e top.</li>
</ol>
${F('limatura-direzioni.svg', 'Direzioni di limatura: lati, punta, superficie.')}
<h2>Perché "in una direzione"</h2>
<ul>
<li>Il movimento a "sega" (avanti e indietro veloce) <strong>scalda</strong> per attrito e sul bordo naturale tende a sfibrare e aprire gli strati.</li>
<li>Una direzione sola dà <strong>più controllo</strong>: sai sempre quanto stai togliendo e da che parte.</li>
<li>Sul prodotto artificiale si possono usare movimenti avanti-indietro controllati, ma sempre <strong>leggeri</strong> e con la lima in movimento.</li>
</ul>
${F('limatura-arco-profilo.svg', 'Profilo: arco superiore dall\'apex alla punta, arco inferiore dritto.')}
<h2>Errori frequenti</h2>
<table>
<tr><th>Errore</th><th>Conseguenza</th><th>Come evitarlo</th></tr>
<tr><td>Limare dentro il solco</td><td>Pelle tagliata, dolore, infezioni</td><td>Tira indietro la pelle con il pollice e tieni la lima parallela</td></tr>
<tr><td>Lima inclinata sui lati</td><td>Lati obliqui, unghia che sembra larga o storta</td><td>Lima piatta; controlla dal davanti</td></tr>
<tr><td>Limare troppo l'apex</td><td>Unghia piatta: si rompe</td><td>Controlla il profilo ogni poche passate</td></tr>
<tr><td>Premere troppo</td><td>Calore, fastidio, solchi</td><td>Lascia lavorare la grana; cambia lima se è consumata</td></tr>
<tr><td>Dimenticare sotto il bordo</td><td>Sbavature visibili e taglienti</td><td>Ultimo controllo dal basso</td></tr>
</table>
${B('warn', 'Controlla da 4 punti di vista', 'Dall\'alto (simmetria), di profilo (apex), dal davanti (curva a C) e dal basso (pulizia del bordo). Vedi la lezione "Controllo finale e simmetria".')}
${B('info', 'Postura', 'Schiena appoggiata, spalle rilassate, piano di lavoro all\'altezza dei gomiti e luce buona: ogni ora alzati, muovi polsi e collo. La limatura manuale è un movimento ripetitivo: proteggi le tue mani.')}
`,
          sources: ['https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-file-different-nail-shapes',
            'https://www.homeofnailart.com/blogs/knowledge-hub/mastering-the-art-of-nail-filing-a-comprehensive-guide-for-professional-nail-technicians',
            'https://open-exam-prep.com/study-guides/pa-nail-technician/manicure-pedicure-foundations/manicure-pedicure-procedures',
            'https://www.katiebarnesacademy.com/blogs/allergies-and-nail-tech-protection/why-how-to-take-care-of-yourself-at-the-nail-desk']
        },
        {
          id: 'controllo-simmetria', simple: 'Prima di mettere il top guarda ogni unghia da quattro lati e poi tutta la mano insieme: le unghie devono sembrare "sorelle".', title: 'Controllo finale e simmetria', min: 8,
          html: `
<p>Il controllo finale è ciò che separa un lavoro "fatto" da un lavoro "ben fatto". È lo stesso controllo che fanno i giudici nelle gare: <strong>struttura, simmetria, pulizia, uniformità</strong>.</p>
<h2>I quattro punti di vista</h2>
${F('controllo-4-viste.svg', 'Le quattro viste del controllo finale.')}
<table>
<tr><th>Vista</th><th>Come guardi</th><th>Che cosa controlli</th></tr>
<tr><td><strong>Dall'alto</strong></td><td>Dito dritto, verso di te</td><td>Lati dritti e paralleli, forma simmetrica, punta centrata, zona cuticolare pulita</td></tr>
<tr><td><strong>Di profilo</strong></td><td>Dito girato di lato, all'altezza degli occhi</td><td>Apex sopra il punto di stress, nessuna gobba alla base, arco inferiore dritto</td></tr>
<tr><td><strong>Dal davanti</strong></td><td>Punta dell'unghia verso i tuoi occhi</td><td>Curva a C regolare e simmetrica, spessore uguale ai lati</td></tr>
<tr><td><strong>Dal basso</strong></td><td>Palmo verso l'alto</td><td>Bordo pulito, niente sbavature, spessore uniforme, lati dritti</td></tr>
</table>
<h2>La simmetria con l'asse</h2>
${F('simmetria-asse.svg', 'L\'asse del dito: punta centrata e lati uguali.')}
<ol class="steps">
<li><strong>Immagina una linea</strong> che parte dal centro della cuticola e prosegue lungo il dito.</li>
<li><strong>La punta</strong> (o il centro della punta) deve cadere su quella linea.</li>
<li><strong>I due lati</strong> devono essere a uguale distanza dalla linea, come immagini allo specchio.</li>
<li><strong>Se un lato è più largo</strong>, lima solo quel lato, poche passate alla volta, e ricontrolla.</li>
</ol>
<h2>Uniformità della mano</h2>
${F('mano-uniformita.svg', 'Le dieci unghie devono avere lunghezza, forma e curva coerenti.')}
<ul>
<li><strong>Lunghezza</strong>: l'aspetto deve essere uniforme; il pollice può essere un po' più lungo, il mignolo un po' più corto.</li>
<li><strong>Forma</strong>: la stessa su tutte le dita, con la stessa "apertura" degli angoli o della punta.</li>
<li><strong>Curva a C</strong>: simile su tutte, guardando le dita affiancate dalla punta.</li>
<li><strong>Smile line</strong> (se french): stessa altezza e profondità.</li>
</ul>
${B('tip', 'Il trucco del pugno', 'Chiedi alla cliente di chiudere la mano a pugno con le unghie verso di te: vedi tutte le punte allineate e scopri subito curve e lunghezze diverse.')}
<h2>Checklist prima del top</h2>
<ol class="steps">
<li>Nessuna polvere nei solchi e sotto il bordo.</li>
<li>Zona cuticolare sfumata, nessun gradino al tatto.</li>
<li>Nessun prodotto sulla pelle.</li>
<li>Superficie liscia: passa il polpastrello, non devi sentire righe.</li>
<li>Le quattro viste sono corrette su tutte le dita.</li>
</ol>
${B('warn', 'Non correggere con il top', 'Il top è sottile e lucido: mette in risalto i difetti invece di nasconderli. Correggi con la lima prima.')}
`,
          sources: ['https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/nail-sculpting-forms',
            'https://www.scratchmagazine.co.uk/blog/simply-salon-nails-perfecting-proper-nail-structure/',
            'https://www.scratchmagazine.co.uk/wp-content/uploads/2026/01/Nailympia-2026-Scoresheet_French-Twist-3-shape-challenge.pdf']
        }
      ]
    },
    /* ------------------------------------------------------------------ 9 */
    {
      id: 'decorazioni', summary: ["Smile line simmetrica e con la stessa profondità sui lati.", "Baby boomer: sfumatura graduale, strati sottili.", "Incapsulato: decorazione tra due strati trasparenti.", "Nail art base: dotting, striping, stamping."], n: 9, level: 'inter', title: 'French, baby boomer e nail art',
      desc: 'Smile line, sfumature, incapsulati e tecniche base di decorazione.',
      lessons: [
        {
          id: 'french', videos: [{"id": "7Bwz_1rcTuA", "title": "How to Create the Perfect French Smile Line", "channel": "Naio Nails", "lang": "EN"}, {"id": "hf6JqVGkwV4", "title": "Technique to Shaping Beautiful Smile Lines", "channel": "Nail Career Education", "lang": "EN"}], title: 'Il french e la smile line', min: 6,
          html: `
${F('smile-line.svg', 'Smile line corrette ed errate.')}
${F('tut-french.svg', 'French passo passo.')}
<p>Il french classico ha la punta bianca separata dal rosa da una <strong>linea del sorriso</strong> (smile line) netta, <strong>simmetrica</strong> e con la stessa profondità sui due lati. Oggi è diffusa anche la variante a "V".</p>
<h2>Tecniche</h2>
<ul>
<li><strong>Gel bianco</strong> steso con il pennello e rifinito.</li>
<li><strong>Polvere acrilica bianca</strong> modellata con la perla.</li>
<li><strong>Dipinto</strong> con gel colorato o semipermanente su una base già costruita.</li>
</ul>
${B('tip', 'Trucco', 'Disegna prima i due "punti" laterali alla stessa altezza, poi collega con una curva. Capovolgi la mano della cliente per controllare la simmetria.')}
`,
          sources: []
        },
        {
          id: 'baby-boomer', videos: [{"id": "0L3JT8K-fx8", "title": "Baby boomer in gel: tutorial dettagliato", "channel": "Nail Couture Italia", "lang": "IT"}, {"id": "GamgGumobZE", "title": "Tutorial baby boomer con builder gel", "channel": "Crystal Nails Italia", "lang": "IT"}], title: 'Baby boomer', min: 4,
          html: `
${F('baby-boomer.svg', 'Baby boomer in tre passaggi.')}
<p>È un "french sfumato": il colore passa gradualmente dal rosa/nude della base al bianco della punta, senza linea netta.</p>
<ol class="steps">
<li>Stendi una base nude/rosa coprente.</li>
<li>Applica il bianco solo sulla punta (gel, polvere acrilica o colore).</li>
<li>Sfuma verso la cuticola con un pennello asciutto o una spugnetta, a strati sottili.</li>
</ol>
`,
          sources: []
        },
        {
          id: 'nail-art', videos: [{"id": "td7E52DtfMc", "title": "Come realizzare un effetto cat eye", "channel": "The Pink Glove Nails", "lang": "IT"}], title: 'Incapsulati e nail art di base', min: 5,
          html: `
${F('nail-art.svg', 'Dotting, striping, incapsulato e stamping.')}
<ul>
<li><strong>Incapsulato</strong>: glitter, foglia oro o fiori secchi chiusi tra due strati di prodotto trasparente.</li>
<li><strong>Dotting</strong>: puntini con il dotter (varia la pressione e la dimensione della sfera).</li>
<li><strong>Striping</strong>: linee con il pennello fine, partendo da una mano ben appoggiata.</li>
<li><strong>Stamping</strong>: disegno trasferito da una piastra incisa con un tampone.</li>
<li>Altre tecniche: adesivi e transfer, effetto cromo/specchio, gel 3D, pittura one-stroke.</li>
</ul>
${B('tip', 'Spessore', 'Le decorazioni non devono creare gobbe: incapsula con prodotto sufficiente e rifinisci la superficie prima del top.')}
`,
          sources: []
        }
      ]
    },
    /* ------------------------------------------------------------------ 10 */
    {
      id: 'manutenzione', summary: ["Refill ogni 3–4 settimane.", "Elimina tutte le parti sollevate prima di riempire.", "Soak-off: acetone + stagnola 10–15 min, senza fare leva.", "Hard gel: si rimuove limando, lasciando un velo sulla lamina."], n: 10, level: 'inter', title: 'Refill e rimozione',
      desc: 'Riempimento ogni 3–4 settimane e rimozione senza danni.',
      lessons: [
        {
          id: 'refill', videos: [{"id": "A3-Xnv5PTSs", "title": "Refill: tutorial e tutto quello che c'è da sapere", "channel": "Babina_90_Nails", "lang": "IT"}, {"id": "Be30VBjQ254", "title": "Tutorial completo refill unghie in gel", "channel": "Nailfor Professional", "lang": "IT"}], simple: "Dopo qualche settimana l'unghia è cresciuta e la ricostruzione si è spostata in avanti: il refill la rimette in equilibrio.", title: 'Il refill (riempimento)', min: 6,
          html: `
${F('refill.svg', 'Profilo prima, durante e dopo la ricrescita.')}
${F('refill-step.svg', 'Il refill visto dall\'alto, passo passo.')}
<p>Il refill si fa ogni <strong>3–4 settimane</strong>: riporta l'apex nella posizione corretta e copre la ricrescita.</p>
<ol class="steps">
<li>Accorcia la lunghezza.</li>
<li>Assottiglia il vecchio prodotto ed <strong>elimina tutte le parti sollevate</strong>.</li>
<li>Prepara la ricrescita come un'unghia naturale (cuticola, opacizzazione, disidratante, primer).</li>
<li>Ricostruisci l'apex sopra il punto di stress, rifinisci e sigilla.</li>
</ol>
${B('danger', 'Mai coprire un sollevamento', 'Sotto un sollevamento possono esserci umidità e batteri: va rimosso del tutto prima di riempire.')}
`,
          sources: ['https://dilei.it/bellezza/cose-e-quanto-costa-il-refill-delle-unghie-in-gel/637264/']
        },
        {
          id: 'rimozione', videos: [{"id": "60O2H65aZfA", "title": "Rimozione sicura del gel in 7 step", "channel": "Nail Couture Italia", "lang": "IT"}, {"id": "k4gk4ZWEvB0", "title": "Come togliere il semipermanente con acetone", "channel": "Semilac Italia", "lang": "IT"}], title: 'La rimozione', min: 5,
          html: `
${F('rimozione.svg', 'Rimozione soak-off.')}
<h2>Soak-off (soft gel, semipermanente, acrilico, molti polygel)</h2>
<ol class="steps">
<li>Opacizza o assottiglia lo strato superiore.</li>
<li>Applica cotone imbevuto di acetone e avvolgi nella stagnola: 10–15 minuti (fino a circa 30 per spessori alti).</li>
<li>Rimuovi il prodotto ammorbidito con un bastoncino, <strong>senza grattare né fare leva</strong>.</li>
<li>Finisci con olio per cuticole.</li>
</ol>
<h2>File-off (hard gel)</h2>
<p>Lima a mano o con fresa fino a lasciare un velo sottile sulla lamina, <strong>senza arrivare all'unghia naturale</strong>.</p>
`,
          sources: ['https://www.marionnaud.it/m-life/tutorial/come-togliere-unghie-gel']
        }
      ]
    },
    /* ------------------------------------------------------------------ 11 */
    {
      id: 'problemi', summary: ["Lifting: quasi sempre preparazione o contatto con la pelle.", "Rotture: apex assente o nel posto sbagliato.", "Picco di calore: strati spessi, lamina sottile, lampada non abbinata → flash and pull.", "Bolle, grinze, ingiallimento: strati sottili e polimerizzazione completa.", "Sotto-polimerizzato = rischio allergia."], n: 11, level: 'avanz', title: 'Problemi e soluzioni',
      desc: 'Sollevamenti, rotture, picchi di calore, bolle, grinze e ingiallimento.',
      lessons: [
        {
          id: 'lifting', simple: "Se il prodotto si stacca, quasi sempre l'unghia non era preparata bene o il prodotto ha toccato la pelle.", title: 'Il sollevamento (lifting)', min: 6,
          html: `
${F('lifting.svg', 'Dove nasce il sollevamento e perché.')}
<p>È il problema più frequente. Quasi sempre dipende dalla <strong>preparazione</strong> o dal <strong>contatto del prodotto con la pelle</strong>.</p>
<h2>Soluzioni</h2>
<ul>
<li>Rimuovi cuticola e pterigio con cura.</li>
<li>Non saltare disidratante e primer.</li>
<li>Lascia circa 1,5 mm dalla pelle e dai solchi laterali.</li>
<li>Sigilla il bordo libero a ogni strato.</li>
<li>Rispetta il rapporto liquido/polvere e i tempi di polimerizzazione.</li>
<li>Rispetta i tempi del refill.</li>
</ul>
`,
          sources: ['https://semilac.co.uk/blogs/news/gel-lifting-and-yellowing-root-causes-and-salon-floor-fixes',
            'https://purespadirect.com/blogs/pure-spa-direct-blog/gel-polish-lifting-troubleshooting-20-causes-prep-lamps-products-and-client-habits-a-nail-tech-39-s-guide-to-perfect-manicures']
        },
        {
          id: 'calore-rotture', simple: "Il gel, indurendo, scalda. Strati sottili e mano fuori dalla lampada qualche secondo evitano il bruciore.", title: 'Rotture e picchi di calore', min: 7,
          html: `
<h2>Rotture e crepe</h2>
<p>Cause: apex assente o nel posto sbagliato, zona 2 troppo sottile, lunghezza eccessiva. Soluzione: ricostruisci l'apex sopra il punto di stress e adegua la lunghezza.</p>
<h2>Picco di calore (heat spike)</h2>
<p>La polimerizzazione è una reazione che <strong>produce calore</strong>. La cliente sente bruciore in lampada.</p>
<ul>
<li><strong>Cause</strong>: strati spessi; lamina assottigliata dalla limatura; lampada troppo potente o non abbinata al gel; troppo attivatore sulla resina.</li>
<li><strong>Soluzioni</strong>: strati sottili, gel a basso calore, modalità low-heat della lampada, tecnica <em>flash and pull</em> (togliere la mano qualche secondo e rimetterla), non assottigliare la lamina.</li>
</ul>
${F('lampada-posizione.svg', 'Flash and pull: uscire qualche secondo dalla lampada tiene il calore sotto la soglia di bruciore.')}
${B('danger', 'Unghia "bruciata"', 'Picchi di calore ripetuti e limatura eccessiva possono danneggiare il letto ungueale (onicolisi, infezioni). Fermati, rimuovi il prodotto, consiglia il medico.')}
`,
          sources: ['https://scratchmagazine.co.uk/feature/heat-spikes-in-gel-nail-services-why-they-happen-how-to-avoid-them',
            'https://www.nsinails.com.au/blogs/news/understand-nail-damages-heat-spikes-lifting-issues']
        },
        {
          id: 'difetti', title: 'Bolle, grinze, ingiallimento', min: 6,
          html: `
${F('problemi.svg', 'Riconosci il difetto.')}
<table>
<tr><th>Problema</th><th>Cause</th><th>Soluzione</th></tr>
<tr><td>Bolle</td><td>Gel agitato; perla troppo asciutta; mano troppo vicina ai LED</td><td>Mescola il gel senza scuoterlo; rapporto corretto; posiziona bene la mano</td></tr>
<tr><td>Grinze</td><td>Strato spesso polimerizzato solo in superficie</td><td>Strati sottili, tempi e lampada corretti</td></tr>
<tr><td>Ingiallimento</td><td>UV/sole, calore, formulazione, nicotina, top non polimerizzato del tutto</td><td>Top anti-ingiallimento, polimerizzazione completa</td></tr>
<tr><td>Sotto/sovra-esposizione</td><td>Tempi o lampada non compatibili</td><td>Sotto-polimerizzato = rischio allergia; sovra-esposto = fragile e caldo. Segui la scheda tecnica</td></tr>
<tr><td>Reazione allergica</td><td>Contatto ripetuto della pelle con prodotto non polimerizzato</td><td>Interrompi e invia al medico; guanti in nitrile e niente contatto per l'operatrice</td></tr>
</table>
`,
          sources: ['https://www.scratchmagazine.co.uk/feature/causes-of-bubbles-in-lp-gel-nail-enhancements', 'https://nailknowledge.org/?p=44956']
        }
      ]
    },
    /* ------------------------------------------------------------------ 12 */
    {
      id: 'professione', summary: ["Scheda cliente con salute, allergie, abitudini e consenso privacy.", "Consigli post-trattamento scritti e data del refill.", "Prezzi indicativi: ricostruzione 50–80 €, refill 20–35 €.", "Gare: struttura, simmetria, pulizia e smile line."], n: 12, level: 'avanz', title: 'Professione e business',
      desc: 'Consulenza, scheda cliente, consigli post-trattamento, prezzi e carriera.',
      lessons: [
        {
          id: 'consulenza', title: 'Consulenza e scheda cliente', min: 6,
          html: `
<p>Ogni nuovo servizio inizia con una consulenza. La scheda cliente protegge la cliente e te.</p>
${F('scheda-cliente.svg', 'Esempio di scheda cliente.')}
<h2>Cosa annotare</h2>
<ul>
<li><strong>Dati e consenso</strong> al trattamento dei dati personali (GDPR).</li>
<li><strong>Salute</strong>: allergie (acrilati, lattice), farmaci, diabete, chemioterapia, gravidanza, patologie dell'unghia.</li>
<li><strong>Abitudini</strong>: onicofagia, lavori manuali, mani spesso in acqua.</li>
<li><strong>Valutazione</strong>: stato della lamina, forma del letto ungueale.</li>
<li><strong>Servizio</strong>: prodotti e lotti usati, foto prima/dopo, eventuale rifiuto e motivazione.</li>
</ul>
`,
          sources: []
        },
        {
          id: 'aftercare', title: 'Consigli post-trattamento', min: 3,
          html: `
<ul>
<li>Olio per cuticole tutti i giorni.</li>
<li>Guanti per pulizie e lavori domestici.</li>
<li>Non usare le unghie come attrezzi; non tirare o staccare il prodotto da sola.</li>
<li>Rispettare la data del refill.</li>
<li>Tornare subito in caso di sollevamenti, dolore o arrossamento.</li>
</ul>
${B('tip', 'Dallo per iscritto', 'Un biglietto con i consigli e la data del prossimo appuntamento riduce i problemi e fidelizza.')}
`,
          sources: []
        },
        {
          id: 'business', title: 'Prezzi e carriera', min: 6,
          html: `
<h2>Prezzi indicativi in Italia</h2>
<table>
<tr><th>Servizio</th><th>Fascia indicativa</th></tr>
<tr><td>Ricostruzione completa</td><td>50–80 € (fino a 100–140 € in centri di fascia alta)</td></tr>
<tr><td>Ricostruzione su unghie rosicchiate</td><td>90–100 €</td></tr>
<tr><td>Refill</td><td>20–35 € (media circa 30 €)</td></tr>
</table>
<p class="muted"><small>Valori raccolti da articoli 2021–2025: non sono listini ufficiali e variano molto per città e zona.</small></p>
<h2>Percorsi professionali</h2>
<ul>
<li>Onicotecnica in centro estetico o nail bar</li>
<li>Libera professionista (con qualifica di estetista e SCIA)</li>
<li>Educator / formatrice per un marchio</li>
<li>Nail artist per moda, editoria e fotografia</li>
<li>Tecnico-commerciale per aziende del settore</li>
</ul>
<h2>Gare</h2>
<p>Le competizioni (per esempio il circuito <strong>Nailympia</strong>) hanno categorie come Salon Nails, Stiletto, Gel Polish e Fantasy, su più livelli (Novice, Apprentice, Master). I giudici valutano struttura (apex, curva a C, simmetria), pulizia della zona cuticolare, smile line e precisione: proprio ciò che hai studiato in questo corso.</p>
`,
          sources: ['https://tattoomuse.it/wiki/quanto-costa-il-gel-per-le-unghie-dallestetista',
            'https://www.scratchmagazine.co.uk/events/nailympia-sicily-2026/',
            'https://www.scratchmagazine.co.uk/news/nailympia-germany-2025-the-results/']
        }
      ]
    },
    /* ------------------------------------------------------------------ 13 */
    {
      id: 'onicofagia', n: 13, level: 'avanz', title: 'Onicofagia e unghie difficili',
      summary: ['Ferite, pus, gonfiore o distacco della lamina: non si lavora, si consiglia il medico.', 'Su unghie rosicchiate meglio la cartina, adattata e tirata verso il basso.', 'Il letto artificiale si crea con gel cover davvero coprente.', 'Lunghezza corta e tonda; all\'inizio appuntamenti ogni 2 settimane.', 'Cucchiaio, ski-jump, pinza, piatta: si adatta la costruzione, non si forza l\'unghia.'],
      desc: 'Unghie rosicchiate, a cucchiaio, ski-jump, a pinza, piatte, sottili o grasse.',
      lessons: [
        {
          id: 'onicofagia-valutazione', title: 'Unghie rosicchiate: valutazione e limiti', min: 6,
          simple: 'Chi si mangia le unghie spesso ha piccole ferite: prima devono guarire, poi si può costruire.',
          videos: [{ id: 'pW5BXeGSUSE', title: 'Ricostruzione su onicofagica: 3 metodi step by step', channel: 'Elena Santucci', lang: 'IT' }],
          html: `
<p>L'<strong>onicofagia</strong> (mangiarsi le unghie) può causare dolore, sanguinamento, arrossamento del letto ungueale e danni alla cuticola. Queste piccole lesioni facilitano infezioni come la <strong>paronichia</strong>.</p>
${B('danger', 'Quando NON lavorare', 'Ferite aperte, pellicine strappate che sanguinano, gonfiore, pus, dolore persistente o unghia staccata dal letto (onicolisi): rimanda la seduta e consiglia il dermatologo.')}
<h2>Cosa valutare</h2>
<ul>
<li>Quanto letto ungueale è rimasto.</li>
<li>Se davanti all'unghia c'è un "cuscinetto" di pelle rialzata (l'iponichio che si è sollevato).</li>
<li>Lo stato della cuticola e lo spessore della lamina.</li>
<li>Se l'abitudine è ancora attiva.</li>
</ul>
<p>Se l'abitudine è compulsiva, può aiutare un percorso con uno specialista (per esempio la terapia cognitivo-comportamentale): l'onicotecnica può suggerire alla cliente di parlarne con il medico, senza fare diagnosi.</p>
`,
          sources: ['https://www.my-personaltrainer.it/salute-benessere/onicofagia-conseguenze-terapia.html',
            'https://www.my-personaltrainer.it/salute/mangiarsi-le-unghie-perche-non-e-solo-un-vizio-e-quali-sono-i-rischi-per-la-salute.html']
        },
        {
          id: 'onicofagia-costruzione', title: 'Costruire su unghie rosicchiate', min: 8,
          simple: 'Dove l\'unghia manca, la "disegni" con un gel color pelle: così sembra più lunga.',
          videos: [{ id: 'eZlxtMxLUZQ', title: 'Ricostruzione onicofagia', channel: 'Nails education', lang: 'IT' }],
          html: `
${F('onicofagia.svg', 'Ricostruzione su unghie rosicchiate in quattro passaggi.')}
<ol class="steps">
<li><strong>Prepara</strong> come sempre: igiene, cuticole, opacizzazione leggera, sgrassaggio.</li>
<li><strong>Adatta la cartina</strong> con le forbici alla forma di ogni dito, falla aderire bene e <strong>tirala verso il basso</strong>: spinge indietro la pelle rialzata e crea spazio per l'allungamento.</li>
<li><strong>Letto artificiale</strong>: con un <em>gel cover</em> davvero coprente prolunga il letto oltre quello naturale. Molti rosa "coprenti" non lo sono abbastanza: verifica controluce.</li>
<li><strong>Bordo libero</strong> corto, con apex centrato; non sovraccaricare di prodotto.</li>
<li><strong>Forma</strong> corta e arrotondata: è più difficile da mordicchiare delle punte.</li>
</ol>
${B('info', 'Tip o cartina?', 'Su unghie molto corte la cartina si adatta meglio: il tip ha bisogno di una superficie minima di incollaggio e su una lamina corta e irregolare tende a staccarsi (indicazione di prassi).')}
<h2>Aspettative e appuntamenti</h2>
<ul>
<li>All'inizio sono utili appuntamenti <strong>ogni 2 settimane</strong>: la ricrescita si vede presto.</li>
<li>Il recupero richiede mesi: l'unghia della mano cresce circa 3,5 mm al mese.</li>
<li>Aftercare: olio per cuticole ogni giorno, guanti per le pulizie, una limetta in borsa da usare al posto dei denti.</li>
</ul>
`,
          sources: ['https://silcare.com/en/blog/how-to-deal-with-a-clients-bitten-nails-step-by-step-reconstruction-of-bitten-nails-1716549279.html',
            'https://nailsmag.epubxp.com/i/317565/52', 'https://bionumbers.hms.harvard.edu/bionumber.aspx?id=112380']
        },
        {
          id: 'unghie-difficili', title: 'Unghie a cucchiaio, ski-jump, a pinza, piatte', min: 8,
          simple: 'Ogni unghia ha la sua forma: tu non la "raddrizzi", la accompagni con la costruzione giusta.',
          html: `
${F('unghie-difficili.svg', 'Quattro unghie difficili e la strategia di costruzione.')}
<table>
<tr><th>Unghia</th><th>Come si riconosce</th><th>Strategia (prassi)</th></tr>
<tr><td><strong>A cucchiaio</strong> (coilonichia)</td><td>Lamina concava che "trattiene una goccia d'acqua". La causa più frequente è la carenza di ferro.</td><td>Livella prima la conca con un velo di builder, poi costruisci un apex regolare; cartina in asse con il dito. Se è comparsa da poco, consiglia un controllo medico.</td></tr>
<tr><td><strong>Ski-jump</strong></td><td>Il bordo libero punta verso l'alto.</td><td>Accorcia l'unghia naturale; tip o cartina leggermente inclinati verso il basso; più prodotto in zona 2; riequilibri frequenti.</td></tr>
<tr><td><strong>A pinza / a tegola</strong></td><td>I lati si chiudono verso la punta e stringono il letto (più frequente sui piedi).</td><td>Curva a C moderata, <strong>niente pinching</strong>, lati non stretti. Se c'è dolore o infiammazione: medico o podologo.</td></tr>
<tr><td><strong>Piatta e larga</strong></td><td>Poca curvatura trasversale.</td><td>Crea la curva a C con la cartina ben modellata, lati paralleli o leggermente convergenti, apex centrato; evita la quadrata troppo larga.</td></tr>
<tr><td><strong>Sottile e morbida</strong></td><td>Si piega e si sfalda.</td><td>Limatura minima, base flessibile (rubber o builder), lunghezza contenuta.</td></tr>
<tr><td><strong>Grassa</strong></td><td>Sebo abbondante: il gel si ritira e si solleva.</td><td>Disidratante e primer adatti al sistema, sgrassa di nuovo subito prima della base, non toccare la lamina.</td></tr>
</table>
${B('tip', 'Regola sull\'apex', 'Più l\'allungamento è lungo, più l\'apex si sposta verso la cuticola, ma senza creare una gobba: un apex troppo avanti fa piegare il bordo libero.')}
`,
          sources: ['https://dermnetnz.org/cases/what-can-cause-these-flattened-nails', 'https://en.wikipedia.org/wiki/Pincer_nail',
            'https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-fit-nail-forms-to-different-nail-shapes']
        }
      ]
    },
    /* ------------------------------------------------------------------ 14 */
    {
      id: 'cover-colori', n: 14, level: 'inter', title: 'Cover, camouflage e gel colorati',
      summary: ['Il gel cover allunga otticamente il letto ungueale e copre le imperfezioni.', 'Il cover deve essere coprente: controlla controluce che non ci siano "finestre".', 'Sottotono freddo → rosa; caldo → pesca/nude caldo; neutro → beige (indicazione pratica).', 'Colori opposti sul cerchio cromatico si neutralizzano (viola ↔ giallo).', 'Gel pigmentati: strati sottili, perché il pigmento assorbe la luce della lampada.'],
      desc: 'Allungare otticamente il letto, scegliere il nude giusto e lavorare i colori.',
      lessons: [
        {
          id: 'cover', title: 'Gel cover e allungamento ottico del letto', min: 7,
          simple: 'Il cover è un gel color pelle: lo stendi oltre il letto naturale e l\'unghia sembra più lunga.',
          videos: [{ id: 'ZuU5bu30h5w', title: 'Allungamento del letto ungueale con cover gel UV', channel: 'TheArtisticnail', lang: 'IT' },
            { id: 'yEfVHzpPlwY', title: 'Ricostruzione e refill con cover costruttori', channel: 'Elena Santucci', lang: 'IT' }],
          html: `
${F('cover-letto.svg', 'Il cover prolunga visivamente il letto ungueale.')}
<p>Il gel <strong>cover</strong> (detto anche make-up o camouflage) è un costruttore pigmentato in tonalità pelle: rosa, nude, pesca, beige. Si usa per <strong>allungare otticamente il letto ungueale</strong> e coprire piccole imperfezioni.</p>
${B('info', 'Attenzione al termine', 'In questo corso "allungamento del letto ungueale" indica solo l\'effetto estetico ottenuto con il cover sopra un allungamento (tip o cartina). Non si interviene sul letto naturale.')}
<ol class="steps">
<li>Allunga con tip o cartina.</li>
<li>Stendi il cover fino alla lunghezza di letto desiderata: deve essere <strong>coprente</strong>. I cover più densi aiutano a costruire la curva a C e non colano nei solchi.</li>
<li>Per un french, prima il cover, poi disegna la smile line con il bianco.</li>
<li>Non scendere troppo con la smile line negli angoli, altrimenti si vedono zone trasparenti.</li>
</ol>
<p class="muted"><small>Da non confondere con gli smalti "effetto correttore", semitrasparenti e lattiginosi, che servono solo ad attenuare piccole discromie.</small></p>
`,
          sources: ['https://emmi-nail.codext.de/nageldesign/ratgeber/ratgeber-gele-alles-uber-covergel.html',
            'https://www.my-personaltrainer.it/bellezza/unghie-effetto-correttore-il-trend-concealer-nails-del-2026-per-una-manicure-naturale-e-perfetta.html']
        },
        {
          id: 'colori', title: 'Teoria del colore e scelta del nude', min: 6,
          simple: 'Il nude giusto è quello che sull\'unghia "sparisce" e sembra il prolungamento del tuo letto naturale.',
          html: `
${F('colori-sottotono.svg', 'Cerchio cromatico e scelta del cover.')}
<h2>Il cerchio cromatico</h2>
<p>I colori <strong>complementari</strong> stanno uno di fronte all'altro (rosso/verde, blu/arancio, giallo/viola) e si neutralizzano a vicenda. Per questo un pigmento leggermente violaceo attenua l'effetto giallo, come nei correttori.</p>
<h2>Scegliere il cover (indicazione pratica)</h2>
<ul>
<li><strong>Sottotono freddo</strong> (riflessi rosati, vene bluastre al polso): rosa o rosa-beige.</li>
<li><strong>Sottotono caldo</strong> (riflessi dorati o olivastri, vene verdastre): pesca o nude caldo.</li>
<li><strong>Sottotono neutro</strong>: nude beige.</li>
</ul>
${B('tip', 'Prova pratica', 'Stendi un campione su un tip appoggiato all\'unghia e guardalo alla luce naturale. Confronta con il letto ungueale, non con la pelle del dorso della mano.')}
`,
          sources: ['https://www.my-personaltrainer.it/bellezza/unghie-effetto-correttore-il-trend-concealer-nails-del-2026-per-una-manicure-naturale-e-perfetta.html']
        },
        {
          id: 'gel-colorati', title: 'Gel colorati, pigmenti e polimerizzazione', min: 6,
          simple: 'Più un gel è colorato, più "blocca" la luce: per questo va steso a strati sottili.',
          html: `
<ul>
<li><strong>Gel colorato da costruzione</strong>: denso, dà struttura. <strong>Semipermanente</strong>: fluido, strati sottili sopra la base, nessuna struttura.</li>
<li><strong>Coprenti</strong> (più pigmento, 1–2 strati) e <strong>traslucidi</strong> (jelly, lasciano vedere sotto).</li>
</ul>
${B('warn', 'Pigmenti e lampada', 'I pigmenti assorbono la luce UV: arriva meno luce al gel sotto. Con strati spessi o molto pigmentati la parte profonda resta sotto-polimerizzata e allungare i tempi non basta. Stendi strati sottili e segui la scheda tecnica del gel con la sua lampada.')}
<h2>Problemi comuni</h2>
<table>
<tr><th>Problema</th><th>Causa probabile</th><th>Cosa fare</th></tr>
<tr><td>Striature</td><td>Normale al primo strato di molti colori</td><td>Il secondo strato sottile uniforma</td></tr>
<tr><td>Ritiro dai bordi</td><td>Olio sulla lamina, primer ancora umido sui lati, lampada non compatibile</td><td>Sgrassa, lascia asciugare, usa la lampada del sistema</td></tr>
<tr><td>Colore non uniforme</td><td>Spessori irregolari, pigmento non rimescolato, prodotto sulle cuticole</td><td>Mescola il vasetto, strati uniformi, margine dalla pelle</td></tr>
</table>
`,
          sources: ['https://nailknowledge.org/blog/mastering-uv-gel-application-insights-into-pigments',
            'https://nailknowledge.org/blog/unveiling-the-hazards-of-thick-uv-gel-application',
            'https://purespadirect.com/blogs/pure-spa-direct-blog/back-to-basics-2013-week-2-gelish-pure-spa-direct']
        }
      ]
    },
    /* ------------------------------------------------------------------ 15 */
    {
      id: 'piedi', n: 15, level: 'inter', title: 'Pedicure e piedi',
      summary: ['Le unghie dei piedi crescono a meno della metà della velocità di quelle delle mani (≈1,6 contro ≈3,5 mm al mese).', 'Taglio dritto con angoli appena smussati: previene l\'unghia incarnita.', 'Mai coprire un\'unghia con sospetta micosi: medico o podologo.', 'Cliente diabetica con ferite o perdita di sensibilità: niente servizio, invio al podologo.', 'Pediluvio individuale o disinfettato con il tempo di contatto indicato.', 'Unghie incarnite, ispessite, deformi: competenza del podologo, non dell\'estetista.'],
      desc: 'Semipermanente e piccoli ripristini sui piedi, igiene, controindicazioni e limiti.',
      lessons: [
        {
          id: 'piedi-differenze', title: 'Unghie dei piedi: differenze e taglio', min: 5,
          simple: 'Sui piedi l\'unghia cresce piano e si taglia dritta, così non entra nella pelle.',
          videos: [{ id: 'RoFFFE8Nbec', title: 'Tutorial semipermanente piedi', channel: 'Aerrenails', lang: 'IT' },
            { id: '2NuJhMyN4VI', title: 'Semipermanente ai piedi: tutti i passaggi', channel: 'Deby Cannavò', lang: 'IT' }],
          html: `
${F('piede-taglio.svg', 'Taglio corretto e velocità di crescita.')}
<ul>
<li><strong>Crescita</strong>: in uno studio su giovani adulti le unghie delle mani crescevano in media 3,47 mm al mese, quelle dei piedi 1,62 mm al mese, cioè meno della metà. Il semipermanente sui piedi dura di più.</li>
<li>La lamina è più spessa e curva e subisce la pressione delle scarpe.</li>
<li><strong>Taglio dritto</strong>, con angoli appena smussati, per ridurre il rischio di unghia incarnita. Ammorbidisci prima l'unghia (pediluvio tiepido) e usa un tronchesino da piedi.</li>
<li>Non accorciare troppo, soprattutto l'alluce, e non scavare i lati.</li>
</ul>
`,
          sources: ['https://bionumbers.hms.harvard.edu/bionumber.aspx?id=112380', 'https://www.aad.org/public/everyday-care/nail-care-secrets/basics/how-to-trim-nails']
        },
        {
          id: 'piedi-igiene', title: 'Igiene, micosi e piede diabetico', min: 7,
          simple: 'Sui piedi i funghi sono comuni: se l\'unghia sembra malata non si copre, si manda dal medico o dal podologo.',
          html: `
<h2>Micosi e piede d'atleta</h2>
<ul>
<li>L'<strong>onicomicosi</strong> è frequente: gli studi di popolazione indicano circa il 5–10% delle persone, con valori più alti negli anziani.</li>
<li>Circa un terzo delle persone con onicomicosi ha anche il <strong>piede d'atleta</strong> (tinea pedis), che prospera in ambienti caldi e umidi come i pediluvi.</li>
</ul>
${B('danger', 'Regola', 'Mai coprire con gel o semipermanente un\'unghia con sospetta micosi (gialla o bianca, ispessita, friabile, sollevata). Sospendi il servizio e consiglia medico o podologo.')}
<h2>Pediluvio</h2>
<ol class="steps">
<li>Usa una vaschetta individuale o monouso, oppure una vasca senza tubature (pipeless), più facile da pulire.</li>
<li>Tra una cliente e l'altra: svuota, togli i residui con detergente, risciacqua.</li>
<li>Disinfetta con un prodotto attivo anche sui funghi, rispettando il <strong>tempo di contatto</strong> indicato in etichetta, poi risciacqua e asciuga. Annota sul registro.</li>
</ol>
<p class="muted"><small>Nei pediluvi con tubature di ricircolo sono stati isolati micobatteri (studio dei CDC in California): un motivo in più per preferire vaschette semplici.</small></p>
<h2>Cliente diabetica</h2>
<ul>
<li>Niente servizio in presenza di ferite, ulcere, infezioni o perdita di sensibilità (neuropatia).</li>
<li>Acqua tiepida, mai calda: la cliente potrebbe non percepire il calore.</li>
<li>Nessun taglio di pelle o cuticole, nessuno strumento tagliente.</li>
<li>Prima di qualsiasi trattamento estetico è consigliabile la valutazione del podologo.</li>
</ul>
`,
          sources: ['https://pmc.ncbi.nlm.nih.gov/articles/PMC7109406', 'https://jddonline.com/articles/dermatology/S1545961615S0032X',
            'https://open-exam-prep.com/study-guides/or-nail-technician/basic-nail-care-service-procedures/pedicuring-procedures-sanitation',
            'https://scratchmagazine.co.uk/feature/pedicure-tips-how-nail-techs-can-safely-support-clients-with-diabetes']
        },
        {
          id: 'piedi-competenze', title: 'Pedicure estetica: protocollo e confini con il podologo', min: 6,
          simple: 'L\'estetista si occupa della bellezza del piede sano; ciò che fa male o sembra malato è compito del podologo o del medico.',
          html: `
${F('pedicure-protocollo.svg', 'Protocollo di pedicure estetica.')}
<h2>Chi fa cosa in Italia</h2>
<table>
<tr><th></th><th>Estetista (L. 1/1990)</th><th>Podologo (DM 666/1994)</th></tr>
<tr><td>Natura</td><td>Prestazioni a scopo estetico sulla superficie del corpo</td><td>Professione sanitaria con laurea abilitante e albo</td></tr>
<tr><td>Unghie</td><td>Piede sano: taglio, limatura, semipermanente, piccoli ripristini estetici</td><td>Unghie ispessite, deformi e incarnite; segnala al medico i casi fuori dalla sua competenza</td></tr>
<tr><td>Escluso</td><td>Prestazioni con finalità terapeutica: micosi, unghie incarnite, verruche, ulcere, piede diabetico a rischio</td><td>—</td></tr>
</table>
${B('warn', 'Calli e lame', 'L\'uso di lame o bisturi su calli e duroni è considerato a rischio e diversi regolamenti regionali e comunali lo escludono o lo limitano: verifica le regole del tuo territorio.')}
<h2>Ricostruzione sui piedi</h2>
<p>Solo piccoli ripristini estetici su unghia <strong>sana</strong> (per esempio un bordo spezzato da un trauma già guarito): strato sottile e flessibile, lunghezza a filo del polpastrello, forma dritta. Mai sopra un'unghia sospetta, ispessita, dolorante o incarnita.</p>
`,
          sources: ['https://cislfp.it/wp-content/uploads/2018/10/d.-m.-666-1994-podologo.pdf',
            'https://www.mo.camcom.it/sportello-genesi/sportello-genesi/modulistica/estetista-scheda-informativa',
            'https://www.comune.cuneo.it/fileadmin/comune_cuneo/content/amm_organiz/attivita_promozionali_produttive/regolamenti/Regolamento_att_acconciatore_estetista.pdf']
        }
      ]
    },
    /* ------------------------------------------------------------------ 16 */
    {
      id: 'arte-gare', n: 16, level: 'avanz', title: 'Nail art avanzata e gare',
      summary: ['Chrome: polvere strofinata sul top no-wipe polimerizzato, poi sigilla i bordi.', 'Cat-eye: magnete prima di polimerizzare lo strato magnetico.', 'One-stroke: pennello piatto caricato con due colori, metà e metà per iniziare.', 'Incapsulato: l\'apex si costruisce sopra la decorazione.', 'Gare: leggi il regolamento dell\'edizione; gel non polimerizzato = squalifica.', 'Giudizio alla cieca: curva C, apex, bordo sottile, smile line, pulizia.'],
      desc: 'Chrome, cat-eye, ombré, one-stroke, 3D e preparazione alle competizioni.',
      lessons: [
        {
          id: 'effetti', title: 'Effetti: chrome, cat-eye, ombré, foil', min: 7,
          simple: 'Molti effetti speciali si fanno sopra un top "no-wipe": prima lo indurisci, poi ci strofini o appoggi la decorazione.',
          videos: [{ id: 'qqr7eqjLYTg', title: 'Chrome Mirror Powder Nail Application', channel: 'Beetles Gel Polish', lang: 'EN' },
            { id: '1x0Oc9gD7GY', title: 'Smalto cat eye: come si applica', channel: 'Estetista Shop', lang: 'IT' }],
          html: `
${F('nail-art-effetti.svg', 'Chrome, cat-eye e one-stroke.')}
<h2>Chrome (effetto specchio)</h2>
<ol class="steps">
<li>Stendi il <strong>top no-wipe</strong> e polimerizza (tempo come da scheda tecnica).</li>
<li>Strofina un velo sottile di polvere con spugnetta o pennello in silicone fino all'effetto specchio.</li>
<li>Togli l'eccesso, sigilla i bordi e applica il top finale.</li>
</ol>
<p>Rende di più su colori scuri o neri.</p>
<h2>Cat-eye (gel magnetico)</h2>
<p>Stendi lo strato magnetico e, <strong>prima di polimerizzare</strong>, avvicina il magnete per orientare le particelle; polimerizza quando l'effetto ti piace. Usa un top sottile: uno spesso fa da "lente" e distorce la linea.</p>
<h2>Ombré e foil (prassi)</h2>
<ul>
<li><strong>Ombré con spugnetta</strong>: due colori affiancati sulla spugna, picchiettati in più passaggi leggeri; poi top.</li>
<li><strong>Ombré in gel</strong>: sfuma i due colori con un pennello piatto pulito prima della lampada.</li>
<li><strong>Foil</strong>: colla specifica o gel lasciato appiccicoso, premi il foil, strappa con un colpo secco e sigilla senza trascinarlo.</li>
</ul>
`,
          sources: ['https://www.scratchmagazine.co.uk/nail_art/cat-eye-chrome-nail-art-tutorial/']
        },
        {
          id: 'one-stroke-3d', title: 'One-stroke, 3D e incapsulato', min: 6,
          simple: 'Nel one-stroke un solo colpo di pennello disegna un petalo già sfumato, perché il pennello porta due colori.',
          videos: [{ id: 'Plp5F1qk40Y', title: 'One stroke flower nail art for beginners', channel: 'Dorota Palicka Nails', lang: 'EN' }],
          html: `
<h2>One-stroke</h2>
<ol class="steps">
<li>Pennello piatto sintetico (n. 2–3) inumidito e tamponato.</li>
<li>Intingi un angolo in un colore e l'angolo opposto nell'altro; per iniziare carica <strong>circa metà e metà</strong>.</li>
<li>Muovi avanti e indietro sempre nello stesso punto della tavolozza per sfumare; il colore deve arrivare a circa 3/4 delle setole, mai nella ghiera.</li>
<li>Parti sul filo del pennello, premi per allargare, ruota su un angolo e solleva: una piccola torsione finale crea la punta del petalo.</li>
<li>Esercitati prima su carta; impugna vicino alla ghiera con il mignolo appoggiato.</li>
</ol>
<h2>3D e incapsulato (prassi)</h2>
<ul>
<li><strong>3D</strong>: gel da modellare o acrilico colorato; modella petali e fiocchi, polimerizza a strati e fissa con builder. Tieni basso lo spessore.</li>
<li><strong>Incapsulato</strong>: la decorazione va tra due strati trasparenti e l'<strong>apex si costruisce sopra</strong>, così la struttura resta corretta.</li>
</ul>
`,
          sources: ['https://www.nailpro.com/technique/article/21155084/tips-on-one-stroke-painting']
        },
        {
          id: 'gare', title: 'Prepararsi a una gara', min: 8,
          simple: 'In gara conta la precisione: unghie tutte uguali, pulite e costruite bene, nel tempo stabilito.',
          videos: [{ id: 'Tx3lwXOS0L0', title: 'Do\'s and Don\'ts of Apex Structure', channel: 'YoungNailsInc', lang: 'EN' }],
          html: `
${F('gara-scheda.svg', 'Criteri di giudizio e vista a tunnel.')}
${B('warn', 'Prima regola', 'Le regole cambiano per sede e per anno: leggi sempre il regolamento dell\'edizione a cui ti iscrivi.')}
<h2>Tempi di esempio (Nailympia Sicily)</h2>
<table>
<tr><th>Categoria</th><th>Tempo</th></tr>
<tr><td>Gel Polish Manicure (due mani)</td><td>45 min</td></tr>
<tr><td>Salon Nails (una mano, 5 unghie)</td><td>60 min</td></tr>
<tr><td>French Tip &amp; Overlay</td><td>75 min</td></tr>
<tr><td>French Sculpture</td><td>90 min</td></tr>
<tr><td>Stiletto · French Twist</td><td>120 min</td></tr>
</table>
<h2>Regole tipiche</h2>
<ul>
<li>Modelle maggiorenni, che restano finché tutti i giudici le hanno viste.</li>
<li>Vietati tip o cartine preparati in anticipo e prodotti senza etichetta originale.</li>
<li>Gel non polimerizzato a fine gara o pulizia dopo lo stop: <strong>squalifica</strong>. Toccare le unghie della modella dopo l'inizio del briefing: penalità (−5 punti in un regolamento 2026).</li>
</ul>
<h2>Come si giudica</h2>
<p>Il giudizio è <strong>alla cieca</strong>. Si valutano struttura, curva C (vista "a tunnel"), posizione dell'apex, sottigliezza del bordo libero, smile line, pulizia della zona cuticolare, superficie e finitura. In una scheda 2026 (French Twist) la maggior parte dei criteri valeva 15 punti e la sezione dell'apex 30.</p>
<h2>Piano di allenamento (8–12 settimane, prassi)</h2>
<ol class="steps">
<li>Settimane 1–4: una mano completa a settimana su modella, cronometrata, con foto di profilo, a tunnel e dall'alto.</li>
<li>Settimane 5–8: allena i punti deboli visti nelle foto (per esempio 20 smile line su tip).</li>
<li>Ultime settimane: simulazioni complete con 10 minuti in meno del tempo di gara, kit definitivo, prova al tavolo con la modella.</li>
</ol>
`,
          sources: ['https://www.nailympia.com/sicily/rules/', 'https://www.nailympia.com/china/rules/',
            'https://www.scratchmagazine.co.uk/feature/the-importance-of-rules-questions/']
        }
      ]
    }
  ];

  /* ==================================================================== ESERCIZI */
  var exercises = [
    { id: 'es-onicofagia', module: 'onicofagia', level: 'avanz', title: 'Letto artificiale su unghia corta', time: '60 min', img: 'onicofagia.svg', caption: 'Valuta, cartina, cover, bordo corto.', imgs: ['cover-letto.svg'],
      goal: 'Simulare la ricostruzione su unghie rosicchiate con un letto artificiale in cover.',
      materials: ['Mano da allenamento', 'Pennarello', 'Cartine e forbici', 'Base, gel cover, builder trasparente o bianco', 'Lampada e lime'],
      steps: ['Segna con il pennarello un letto naturale di 5–6 mm su ogni dito.', 'Adatta la cartina rifilandola: aderente e senza spazi.', 'Base sottile; costruisci il letto artificiale in cover 2–3 mm oltre il segno e polimerizza.', 'Bordo libero corto con apex centrato; lima una forma tonda o squoval corta e applica il top.'],
      checks: ['Smile line simmetrica e uguale sulle 5 dita', 'Cover opaco, senza zone trasparenti', 'Bordo libero sottile', 'Apex visibile di profilo ma senza gobba', 'Nessun prodotto sulla cuticola'],
      mistakes: ['Cover poco coprente', 'Allungamento troppo lungo per un\'unghia rosicchiata'] },
    { id: 'es-difficili', module: 'onicofagia', level: 'avanz', title: 'Riconosci le unghie difficili', time: '25 min', img: 'unghie-difficili.svg', caption: 'Cucchiaio, ski-jump, pinza, piatta.',
      goal: 'Associare ogni forma difficile alla strategia di costruzione corretta.',
      materials: ['Foto di mani (con permesso) o la tua mano', 'Quaderno'],
      steps: ['Osserva 10 unghie dall\'alto, di profilo e dalla punta.', 'Classificale: normale, cucchiaio, ski-jump, pinza, piatta, sottile, grassa.', 'Per ognuna scrivi la strategia: posizione dell\'apex, cartina, curva a C.', 'Segna i casi in cui consiglieresti un controllo medico.'],
      checks: ['Ho osservato da tre punti di vista', 'Ho indicato una strategia per ogni unghia', 'Ho riconosciuto i casi da inviare al medico', 'Non ho previsto pinching su unghie a pinza'],
      mistakes: ['Forzare la curva su un\'unghia a pinza', 'Seguire la conca del cucchiaio con la cartina'] },
    { id: 'es-cover', module: 'cover-colori', level: 'inter', title: 'Cartella colori dei cover', time: '40 min', img: 'colori-sottotono.svg', caption: 'Sottotono e cover.', imgs: ['cover-letto.svg'],
      goal: 'Scegliere il cover giusto e stenderlo coprente in strati sottili.',
      materials: ['3 tip su supporto', 'Gel cover rosa, nude e pesca', 'Lampada', 'Quaderno'],
      steps: ['Stendi su ogni tip un cover diverso in 2 strati sottili, polimerizzando ogni strato come da scheda tecnica.', 'Annota per ogni cover strati e tempi necessari per coprire.', 'Appoggia i tip sull\'unghia di una compagna e scegli il più adatto alla luce naturale.', 'Su mano finta costruisci un letto allungato di 2 mm con quel cover.'],
      checks: ['Cover opaco controluce', 'Nessuna striatura dopo il secondo strato', 'Nessun ritiro sui lati', 'La tonalità si fonde con il letto naturale'],
      mistakes: ['Strati spessi di gel pigmentato', 'Scegliere il colore con la luce artificiale'] },
    { id: 'es-pedicure', module: 'piedi', level: 'inter', title: 'Protocollo pedicure con semipermanente', time: '60 min', img: 'pedicure-protocollo.svg', caption: 'Anamnesi, ispezione, pediluvio, taglio, cuticola, colore.', imgs: ['piede-taglio.svg'],
      goal: 'Eseguire una pedicure estetica sicura con semipermanente.',
      materials: ['Scheda anamnesi', 'Vaschetta monouso o disinfettata', 'Tronchesino e lime monouso', 'Base, colore, top, lampada', 'Registro di disinfezione'],
      steps: ['Compila l\'anamnesi: diabete, circolazione, farmaci, micosi pregresse.', 'Ispeziona unghie e pelle: se qualcosa è sospetto, fermati e consiglia medico o podologo.', 'Pediluvio tiepido, taglio dritto, angoli appena smussati; arretra la cuticola senza tagli.', 'Opacizza, sgrassa, base, due strati sottili di colore e top; poi disinfetta la postazione e annota sul registro.'],
      checks: ['Anamnesi completa', 'Nessun taglio della pelle', 'Alluce dritto senza lati scavati', 'Colore senza sbavature', 'Vaschetta disinfettata e registrata'],
      mistakes: ['Coprire un\'unghia sospetta', 'Acqua troppo calda'] },
    { id: 'es-effetti', module: 'arte-gare', level: 'inter', title: 'Chrome, cat-eye e one-stroke', time: '60 min', img: 'nail-art-effetti.svg', caption: 'Tre effetti da provare.',
      goal: 'Realizzare tre effetti avanzati su tip.',
      materials: ['Tip neri o scuri', 'Top no-wipe e polvere chrome', 'Gel magnetico e magnete', 'Pennello piatto n. 2–3 e due colori'],
      steps: ['Chrome: top no-wipe, lampada, strofina la polvere, sigilla i bordi e top.', 'Cat-eye: strato magnetico, magnete prima della lampada, top sottile.', 'One-stroke: 5 petali su carta, poi un fiore su un tip.', 'Fotografa i tre tip e confrontali con le tavole.'],
      checks: ['Chrome uniforme a specchio', 'Bordi sigillati', 'Linea cat-eye netta', 'Petali sfumati con punta definita'],
      mistakes: ['Polvere chrome su top non polimerizzato', 'Top spesso sul cat-eye'] },
    { id: 'es-gara', module: 'arte-gare', level: 'avanz', title: 'Simulazione Salon Nails (60 min)', time: '60 min', img: 'gara-scheda.svg', caption: 'Valutati come in gara.', imgs: ['zone-costruzione.svg', 'curva-c.svg'],
      goal: 'Costruire 5 unghie da gara nel tempo stabilito e valutarle con una scheda.',
      materials: ['Modella o mano da allenamento', 'Kit completo con prodotti etichettati', 'Timer'],
      steps: ['Avvia il timer: nessun contatto con le unghie prima del via.', 'Preparazione, cartine o tip, costruzione in gel con apex coerente.', 'Limatura: forma uguale sulle 5 unghie; colore o french e una piccola decorazione.', 'Fermati allo scadere senza pulire; fotografa e valutati con la scheda.'],
      checks: ['Curva C uniforme vista a tunnel', 'Apex nella stessa posizione su tutte', 'Bordo libero sottile e uniforme', 'Zona cuticolare pulita', 'Tempo rispettato'],
      mistakes: ['Correggere dopo lo stop', 'Unghie di lunghezze diverse'] },
    { id: 'es-semipermanente', module: 'sistemi', level: 'base', title: 'Semipermanente perfetto', time: '45 min', img: 'tut-semipermanente.svg', caption: 'I sei passaggi del semipermanente.',
      goal: 'Stendere un semipermanente pulito, sottile e sigillato sul bordo libero.',
      materials: ['Mano da allenamento o modella', 'Base, colore e top', 'Lampada', 'Cleaner e olio'],
      steps: ['Prepara le unghie come nel modulo 5.', 'Base sottile e lampada.', 'Due strati sottili di colore, ognuno in lampada.', 'Top passando anche sul bordo libero, lampada, cleaner se serve, olio.'],
      checks: ['Nessuna sbavatura sulla pelle', 'Colore uniforme senza zone chiare', 'Bordo libero sigillato', 'Superficie liscia senza grinze'],
      mistakes: ['Strati di colore troppo spessi (grinze)', 'Prodotto sulle cuticole (sollevamenti)'] },
    { id: 'es-acrilico', module: 'cartina', level: 'avanz', title: 'Ricostruzione completa in acrilico', time: '90 min', img: 'tut-acrilico.svg', caption: 'Zona 1, zona 2, zona 3, pinching, limatura.', imgs: ['perla-acrilico.svg', 'zone-costruzione.svg'],
      goal: 'Costruire 5 unghie in acrilico su cartina con struttura corretta.',
      materials: ['Mano da allenamento', 'Cartine', 'Monomero e polveri', 'Pennello 8–12', 'Lime', 'DPI e aspiratore'],
      steps: ['Posiziona le cartine.', 'Costruisci zona 1, zona 2 e zona 3 come nel tutorial.', 'Fai il pinching al momento giusto.', 'Lima e confronta di profilo con la tavola delle zone.'],
      checks: ['Cinque unghie della stessa lunghezza', 'Apex sopra il punto di stress su tutte', 'Zona cuticolare sottile e pulita', 'Nessuna bolla o porosità'],
      mistakes: ['Perla troppo bagnata in zona 3', 'Saltare il controllo di profilo'] },
    { id: 'es-softgel', module: 'sistemi', level: 'inter', title: 'Applica i soft gel tips', time: '40 min', img: 'tut-soft-gel-tips.svg', caption: 'Misura, gel adesivo, applicazione, lampada.',
      goal: 'Applicare soft gel tips ben aderenti e senza bolle.',
      materials: ['Mano da allenamento', 'Soft gel tips', 'Gel adesivo', 'Lampada LED', 'Disidratante e primer'],
      steps: ['Scegli e prepara le misure per tutte le dita.', 'Prepara le unghie (180, disidratante, primer).', 'Gel adesivo nel tip, applica dalla zona cuticolare, flash, poi lampada completa.', 'Rifinisci e applica il top.'],
      checks: ['Ogni tip copre da solco a solco', 'Nessuna bolla sotto il tip', 'Tip non a contatto con la cuticola', 'Tutti in asse'],
      mistakes: ['Disidratazione insufficiente', 'Tip appoggiato sulla pelle'] },
    { id: 'es-fibra', module: 'sistemi', level: 'inter', title: 'Riparazione in fibra', time: '30 min', img: 'tut-fibra.svg', caption: 'Taglia, resina, attivatore, lima.',
      goal: 'Rinforzare o riparare un\'unghia con la fibra senza spessori.',
      materials: ['Tip da allenamento con una crepa', 'Fibra di vetro o seta', 'Resina', 'Attivatore a pennello', 'Lima 180'],
      steps: ['Taglia la fibra a forma dell\'unghia.', 'Fissala con la resina coprendo la crepa.', 'Applica poco attivatore a pennello.', 'Lima per eliminare i bordi e sigilla.'],
      checks: ['Il tessuto non si vede ai bordi', 'Nessun gradino', 'La crepa è coperta', 'Ho usato poco attivatore'],
      mistakes: ['Troppo attivatore (calore)', 'Fibra che tocca la pelle'] },
    { id: 'es-anatomia', module: 'anatomia', level: 'base', title: 'Disegna e nomina l\'anatomia', time: '20 min', img: 'anatomia-alto.svg', caption: 'Confronta il tuo disegno con questa tavola.',
      goal: 'Memorizzare le parti dell\'unghia e la loro funzione.',
      materials: ['Foglio e matite colorate', 'La tua mano come modello'],
      steps: ['Disegna un dito visto dall\'alto e di lato, senza guardare la tavola.', 'Scrivi i nomi di almeno 8 parti.', 'Accanto a ogni parte scrivi in una riga cosa significa per il tuo lavoro.', 'Confronta con la tavola e correggi in rosso.'],
      checks: ['Ho nominato matrice, lamina, letto, iponichio', 'Ho distinto eponichio (vivo) e cuticola (morta)', 'Ho indicato il punto di stress', 'Ho collegato ogni parte a una regola pratica'],
      mistakes: ['Confondere eponichio e cuticola', 'Dimenticare l\'iponichio sotto il bordo libero'] },
    { id: 'es-postazione', imgs: ['ciclo-sterilizzazione.svg', 'dpi.svg'], module: 'igiene', level: 'base', title: 'Allestisci una postazione sicura', time: '30 min', img: 'igiene.svg', caption: 'I tre livelli igienici.',
      goal: 'Preparare e riordinare la postazione con un protocollo igienico completo.',
      materials: ['Disinfettante per superfici e strumenti', 'Buste di sterilizzazione', 'Lime monouso', 'DPI', 'Aspiratore'],
      steps: ['Disinfetta il piano e la lampada.', 'Disponi gli strumenti sterilizzati in busta chiusa.', 'Prepara lime nuove e DPI.', 'Simula il fine servizio: detergi, disinfetta e prepara per l\'autoclave; compila il registro.'],
      checks: ['Ho separato pulito e sporco', 'Le lime usate sono state eliminate o consegnate', 'Ho indossato nitrile e FFP2', 'Ho registrato il ciclo di sterilizzazione'],
      mistakes: ['Riutilizzare lime in carta', 'Aprire le buste sterili in anticipo'] },
    { id: 'es-forme', imgs: ['forme-limatura-step.svg'], module: 'limatura', level: 'base', title: 'Lima 8 forme su una ruota di tip', time: '45 min', img: 'forme.svg', caption: 'Le forme da riprodurre.',
      goal: 'Controllare la lima e ottenere forme simmetriche.',
      materials: ['Ruota di tip', 'Lima 100/180 e 180/240', 'Matita'],
      steps: ['Traccia con la matita l\'asse centrale di ogni tip.', 'Lima ogni tip in una forma diversa seguendo la tavola.', 'Controlla la simmetria piegando a metà con lo sguardo lungo l\'asse.', 'Ripeti le forme meno riuscite.'],
      checks: ['Le forme sono simmetriche rispetto all\'asse', 'Gli angoli della squoval sono uguali', 'La punta della mandorla è centrata', 'I lati della ballerina sono dritti'],
      mistakes: ['Limare avanti e indietro come una sega', 'Perdere l\'asse e ottenere forme storte'] },
    { id: 'es-limatura', imgs: ['forme-limatura-step.svg'], module: 'limatura', level: 'base', title: 'Direzioni di limatura su mano finta', time: '30 min', img: 'limatura-direzioni.svg', caption: 'Lati, punta, superficie.',
      goal: 'Automatizzare i movimenti corretti di limatura.',
      materials: ['Mano da allenamento con tip', 'Lima 180/240', 'Buffer'],
      steps: ['Lima i lati con la lima parallela al solco.', 'Lima la punta dai lati verso il centro.', 'Leviga la superficie con movimenti lunghi dalla base alla punta.', 'Rifinisci sotto il bordo libero.'],
      checks: ['Non ho mai limato dentro il solco', 'Ho usato movimenti in una sola direzione', 'La superficie è liscia al tatto', 'Il bordo è pulito sotto'],
      mistakes: ['Inclinare la lima creando lati obliqui', 'Premere troppo'] },
    { id: 'es-prep', module: 'preparazione', level: 'base', title: 'Preparazione completa su 10 dita', time: '40 min', img: 'prep-sequenza-perche.svg', caption: 'La sequenza della preparazione, ogni passaggio con il suo perché.', imgs: ['cuticola-step.svg', 'prep-errori.svg'],
      goal: 'Eseguire la preparazione in modo ordinato e ripetibile.',
      materials: ['Mano da allenamento o modella', 'Spingicuticole', 'Lima 180/240', 'Pennello per polveri', 'Disidratante e primer'],
      steps: ['Segui la sequenza su ogni dito, sempre nello stesso ordine.', 'Cronometra il tempo totale.', 'Controlla con una luce radente che non resti pellicina sulla lamina.', 'Ripeti cercando di ridurre il tempo senza saltare passaggi.'],
      checks: ['Nessun residuo di cuticola sulla lamina', 'Lamina opaca in modo uniforme ma non assottigliata', 'Primer solo sulla lamina, mai sulla pelle', 'Tempo sotto i 30 minuti'],
      mistakes: ['Toccare la lamina con le dita dopo il disidratante', 'Troppo primer'] },
    { id: 'es-perla', imgs: ['tut-acrilico.svg'], module: 'sistemi', level: 'inter', title: 'Allenati sulla perla di acrilico', time: '30 min', img: 'perla-acrilico.svg', caption: 'Bagnata, media, asciutta.',
      goal: 'Riconoscere e riprodurre il rapporto liquido/polvere corretto.',
      materials: ['Pennello per acrilico 8–12', 'Monomero e polvere', 'Tip o foglio di plastica', 'DPI e aspiratore'],
      steps: ['Fai volutamente una perla bagnata, una media e una asciutta e appoggiale sul foglio.', 'Osserva come si comportano dopo 10 secondi.', 'Fai 10 perle medie di seguito.', 'Prova a stenderne una su un tip senza farla colare.'],
      checks: ['So distinguere a occhio le tre perle', 'Le mie perle medie sono lucide e bombate', 'Non colano dopo l\'appoggio', 'Ho lavorato con guanti e aspirazione'],
      mistakes: ['Pennello troppo bagnato', 'Toccare il monomero a mani nude'] },
    { id: 'es-tip', imgs: ['tip-tipi.svg'], module: 'tip', level: 'inter', title: 'Applica e fondi 10 tip', time: '45 min', img: 'tip-applicazione.svg', caption: 'Misura, incolla, taglia, fondi.',
      goal: 'Applicare tip in asse, senza bolle e con fusione invisibile.',
      materials: ['Mano da allenamento', 'Tip con incavo', 'Colla', 'Tagliatip', 'Lima 180'],
      steps: ['Scegli la misura per ogni dito.', 'Incolla a 45° abbassando lentamente.', 'Taglia tutti i tip alla stessa lunghezza.', 'Fondi la linea di contatto.'],
      checks: ['Ogni tip copre da solco a solco', 'Nessuna bolla visibile', 'Tutti alla stessa lunghezza', 'Linea di contatto invisibile al tatto'],
      mistakes: ['Tip troppo stretto che spacca i lati', 'Limare l\'unghia naturale durante la fusione'] },
    { id: 'es-cartina', module: 'cartina', level: 'inter', title: 'Posiziona la cartina 10 volte', time: '20 min', img: 'cartina.svg', caption: 'In asse e a filo.',
      goal: 'Posizionare la cartina in asse e senza spazi.',
      materials: ['Cartine', 'Mano da allenamento o la tua mano'],
      steps: ['Posiziona la cartina su ogni dito.', 'Controlla dall\'alto l\'asse e di lato il contatto con il bordo libero.', 'Togli e riposiziona finché è perfetta.', 'Fotografa le dieci cartine e confrontale.'],
      checks: ['Nessuno spazio sotto il bordo libero', 'Asse allineato al dito', 'Alette chiuse sotto il polpastrello', 'Curva della cartina coerente con l\'unghia'],
      mistakes: ['Cartina troppo bassa', 'Cartina ruotata verso il pollice'] },
    { id: 'es-apex', module: 'cartina', level: 'inter', title: 'Costruisci l\'apex in gel', time: '60 min', img: 'zone-costruzione.svg', caption: 'Zona 3 sottile, zona 2 struttura, zona 1 sottile.', imgs: ['tut-gel-cartina.svg', 'zone-spessori-sezione.svg'],
      goal: 'Costruire una struttura con apex sopra il punto di stress.',
      materials: ['Tip o cartina su mano da allenamento', 'Gel costruttore', 'Pennello per gel', 'Lampada'],
      steps: ['Stendi una base sottile e polimerizza.', 'Metti una perla di gel in zona 2 e accompagnala verso le zone 1 e 3.', 'Capovolgi la mano qualche secondo per far scendere il gel verso l\'apex, poi polimerizza.', 'Lima e controlla di profilo.'],
      checks: ['Apex sopra il punto di stress', 'Zona cuticolare sottile e a circa 1 mm dalla pelle', 'Punta sottile e uniforme', 'Spessore uguale da lato a lato'],
      mistakes: ['Gobba alla cuticola', 'Unghia piatta senza struttura'] },
    { id: 'es-curva-c', module: 'cartina', level: 'avanz', title: 'Curva a C con pinching', time: '45 min', img: 'curva-c.svg', caption: 'Curve bassa, media, alta.',
      goal: 'Ottenere una curva a C regolare senza stressare l\'unghia.',
      materials: ['Mano da allenamento', 'Cartine', 'Gel o acrilico', 'Pinzette per pinching (facoltative)'],
      steps: ['Costruisci 3 unghie su cartina.', 'Pizzica la prima poco, la seconda di più, la terza molto, nel momento giusto.', 'Guardale dal bordo libero e confronta con la tavola.', 'Annota il tempo in cui il pinching ha funzionato meglio.'],
      checks: ['Le curve sono simmetriche', 'Nessuna crepa sui lati', 'Ho riconosciuto il momento giusto per pizzicare', 'Ho rispettato la curva naturale'],
      mistakes: ['Pizzicare troppo tardi (crepe)', 'Pizzicare in modo asimmetrico'] },
    { id: 'es-french', imgs: ['tut-french.svg'], module: 'decorazioni', level: 'inter', title: 'Smile line su 10 tip', time: '40 min', img: 'smile-line.svg', caption: 'Simmetrica, netta, stessa profondità.',
      goal: 'Disegnare smile line simmetriche e uguali tra loro.',
      materials: ['Ruota di tip', 'Gel bianco o colore bianco', 'Pennello fine', 'Cleaner'],
      steps: ['Segna i due punti laterali alla stessa altezza.', 'Collega con una curva continua.', 'Riempi il bianco fino alla punta.', 'Confronta le 10 smile line: devono sembrare uguali.'],
      checks: ['Ogni smile line è simmetrica', 'Linea netta senza sbavature', 'Profondità uguale su tutte', 'Bianco uniforme e coprente'],
      mistakes: ['Smile line piatta', 'Lati a altezze diverse'] },
    { id: 'es-babyboomer', module: 'decorazioni', level: 'inter', title: 'Baby boomer sfumato', time: '40 min', img: 'baby-boomer.svg', caption: 'Dal nude al bianco.',
      goal: 'Creare una sfumatura graduale senza linee.',
      materials: ['Tip', 'Gel nude e bianco (o polveri)', 'Pennello piatto o spugnetta'],
      steps: ['Stendi la base nude.', 'Applica il bianco sulla punta.', 'Sfuma verso la cuticola a strati sottili.', 'Sigilla con top.'],
      checks: ['Non si vede nessuna linea netta', 'La sfumatura è graduale', 'Lo spessore resta sottile', 'Tutte le unghie hanno la stessa altezza di sfumatura'],
      mistakes: ['Troppo bianco: sembra un french sbavato', 'Strati spessi che creano gobbe'] },
    { id: 'es-nailart', module: 'decorazioni', level: 'base', title: 'Dotting e striping', time: '30 min', img: 'nail-art.svg', caption: 'Tecniche di base.',
      goal: 'Controllare pressione e precisione del gesto.',
      materials: ['Tip colorati', 'Dotter di varie misure', 'Pennello striper', 'Colori/gel'],
      steps: ['Fai una fila di 10 puntini uguali con lo stesso dotter.', 'Fai puntini decrescenti dal più grande al più piccolo.', 'Traccia 5 linee parallele con lo striper.', 'Crea un piccolo fiore con 5 puntini e un centro.'],
      checks: ['Puntini della stessa misura', 'Linee dritte e parallele', 'Spessore costante della linea', 'Composizione centrata'],
      mistakes: ['Ricaricare il dotter in modo diverso a ogni punto', 'Mano non appoggiata'] },
    { id: 'es-refill', imgs: ['refill-step.svg'], module: 'manutenzione', level: 'avanz', title: 'Refill simulato', time: '60 min', img: 'refill.svg', caption: 'Riporta l\'apex sopra il punto di stress.',
      goal: 'Eseguire un refill completo riequilibrando la struttura.',
      materials: ['Mano da allenamento con ricostruzione', 'Lima 100/180', 'Fresa (facoltativa)', 'Gel'],
      steps: ['Simula la ricrescita limando via 3 mm di prodotto alla base.', 'Accorcia e assottiglia il vecchio prodotto.', 'Prepara la "ricrescita" e ricostruisci l\'apex.', 'Rifinisci e confronta il profilo con la tavola.'],
      checks: ['Nessuna parte sollevata rimasta', 'Nessun gradino tra vecchio e nuovo', 'Apex di nuovo sopra il punto di stress', 'Lunghezza riportata a quella iniziale'],
      mistakes: ['Coprire un sollevamento', 'Aggiungere prodotto senza togliere il vecchio: unghia sempre più spessa'] },
    { id: 'es-rimozione', imgs: ['dpi.svg'], module: 'manutenzione', level: 'base', title: 'Rimozione soak-off', time: '30 min', img: 'rimozione.svg', caption: 'Opacizza, acetone, stagnola, bastoncino.',
      goal: 'Rimuovere il prodotto senza danneggiare la lamina.',
      materials: ['Tip con semipermanente o soft gel', 'Acetone', 'Cotone', 'Stagnola', 'Bastoncino d\'arancio', 'Olio'],
      steps: ['Opacizza il top.', 'Applica cotone con acetone e avvolgi.', 'Attendi 10–15 minuti.', 'Spingi via il prodotto, poi olio.'],
      checks: ['Ho opacizzato senza limare a fondo', 'Ho rispettato i tempi', 'Non ho grattato né fatto leva', 'Ho finito con olio'],
      mistakes: ['Strappare il prodotto non ancora ammorbidito', 'Usare l\'acetone su pelle irritata'] },
    { id: 'es-fresa', module: 'attrezzatura', level: 'avanz', title: 'Controllo della fresa su tip', time: '40 min', img: 'punte-fresa.svg', caption: 'Punte, colori e velocità.',
      goal: 'Usare la fresa con pressione leggera e velocità adeguate.',
      materials: ['Fresa', 'Punta cilindro in carburo', 'Tip con gel', 'DPI e aspiratore'],
      steps: ['Imposta 10.000 RPM e sfuma la superficie di un tip con la punta parallela.', 'Passa a 15.000–20.000 RPM per rimuovere prodotto da un secondo tip.', 'Mantieni la punta sempre in movimento.', 'Controlla al tatto che non ci siano solchi.'],
      checks: ['Nessun solco o "anello"', 'Nessun surriscaldamento', 'Punta sempre in movimento', 'Ho usato carburo solo sul prodotto'],
      mistakes: ['Fermarsi in un punto', 'Inclinare la punta e scavare'] },
    { id: 'es-diagnosi', imgs: ['lifting.svg', 'lampada-posizione.svg'], module: 'problemi', level: 'avanz', title: 'Diagnosi dei difetti', time: '25 min', img: 'problemi.svg', caption: 'Riconosci il difetto.',
      goal: 'Associare ogni difetto alla sua causa e soluzione.',
      materials: ['Foto dei tuoi lavori (o lavori di prova)', 'Quaderno'],
      steps: ['Raccogli 10 foto dei tuoi lavori, anche di profilo.', 'Per ognuna indica eventuali difetti (lifting, crepe, bolle, grinze, ingiallimento).', 'Scrivi la causa più probabile.', 'Scrivi cosa cambierai la prossima volta.'],
      checks: ['Ho analizzato tutte le 10 foto', 'Per ogni difetto ho indicato una causa', 'Per ogni causa ho indicato un correttivo', 'Ho ripetuto un lavoro applicando il correttivo'],
      mistakes: ['Dare la colpa al prodotto prima di controllare la preparazione'] },
    { id: 'es-consulenza', module: 'professione', level: 'inter', title: 'Consulenza simulata', time: '20 min', img: 'scheda-cliente.svg', caption: 'Usa una scheda come questa.',
      goal: 'Condurre una consulenza completa e compilare la scheda cliente.',
      materials: ['Scheda cliente stampata', 'Una persona che faccia la cliente'],
      steps: ['Chiedi dati, consenso privacy e informazioni di salute.', 'Valuta l\'unghia e le abitudini.', 'Proponi sistema, forma e lunghezza spiegando il perché.', 'Spiega i consigli post-trattamento e fissa il refill.'],
      checks: ['Ho chiesto di allergie e farmaci', 'Ho valutato le controindicazioni', 'Ho motivato la scelta del sistema', 'Ho dato i consigli post-trattamento'],
      mistakes: ['Saltare le domande sulla salute', 'Accettare una lunghezza non adatta alle abitudini della cliente'] },
    { id: 'es-luce-radente', module: 'preparazione', level: 'base', title: 'Il controllo con la luce radente', time: '25 min', img: 'cuticola-step.svg', caption: 'Arretra, solleva, taglia solo ciò che pende, controlla.', imgs: ['opacizzazione-controllo.svg', 'pterigio-vero.svg'],
      goal: 'Imparare a vedere pellicine residue e zone lucide prima di costruire.',
      materials: ['Mano da allenamento con unghie naturali o modella', 'Spingicuticole e curette sterilizzati', 'Lima 180/240 nuova', 'Lampada da tavolo orientabile', 'Pennello per polveri', 'Pennarello lavabile'],
      steps: ['Lavora la zona cuticolare su 5 dita seguendo i 4 passaggi.', 'Opacizza solo metà di ogni unghia (sinistra) e lascia l\'altra lucida.', 'Inclina la lampada a luce radente e confronta le due metà: impara a riconoscere il riflesso.', 'Segna con il pennarello ogni residuo di pellicina che vedi, poi eliminalo e ricontrolla.', 'Completa l\'opacizzazione e ricontrolla tutte le unghie.'],
      checks: ['Distinguo a colpo d\'occhio lucido e opaco', 'Nessun residuo nei solchi laterali', 'Nessuna zona più sottile o rosata', 'Non ho mai tagliato pelle viva'],
      mistakes: ['Controllare solo dall\'alto, con luce diretta', 'Opacizzare insistendo al centro'] },
    { id: 'es-tip-misura', module: 'tip', level: 'base', title: 'Misura e adatta i tip per 10 dita', time: '30 min', img: 'tip-anatomia.svg', caption: 'Incavo, punto d\'arresto, zona di contatto.', imgs: ['tip-misura-errori.svg', 'tip-adattare.svg'],
      goal: 'Scegliere la misura giusta per ogni dito e adattare lati e incavo senza colla.',
      materials: ['Mano da allenamento o la tua mano', 'Scatola di tip con misure 0–9', 'Lima 180', 'Forbicine o lima per accorciare l\'incavo', 'Foglio e penna'],
      steps: ['Prova a secco ogni misura sul pollice partendo dalla più larga e scendi finché il tip copre esattamente da solco a solco.', 'Ripeti per tutte le 10 dita e annota i numeri su un foglio (mano destra e sinistra).', 'Su almeno 3 dita prendi la misura più grande e lima i lati del tip finché combacia.', 'Accorcia gli incavi che superano metà unghia.', 'Disponi i tip in ordine sul tavolo come se dovessi incollarli.'],
      checks: ['Ogni tip copre da solco a solco senza toccare la pelle', 'La curva del tip segue quella dell\'unghia (vista frontale)', 'Nessun incavo oltre metà lamina', 'Ho annotato le misure delle due mani'],
      mistakes: ['Scegliere un tip stretto e allargarlo a forza', 'Limare la pelle invece del tip'] },
    { id: 'es-cartina-adattata', module: 'cartina', level: 'inter', title: 'Cartine su misura', time: '30 min', img: 'cartina-adattata.svg', caption: 'Unghia corta, larga, iponichio lungo, unghia curva.', imgs: ['cartina-livello.svg', 'cartina-ritaglio-step.svg'],
      goal: 'Adattare la cartina a unghie diverse mantenendola a filo, in asse e in livello.',
      materials: ['Cartine adesive', 'Forbicine', 'Matita', 'Mano da allenamento con tip tagliati a lunghezze diverse', 'Specchietto o telefono per foto di profilo'],
      steps: ['Prepara 4 dita della mano da allenamento: un bordo cortissimo e dritto, uno largo e quadrato, uno molto curvo, uno normale.', 'Adatta una cartina per ciascuno seguendo la tavola.', 'Fotografa ogni dito dall\'alto, di profilo e dal davanti.', 'Confronta le foto con la tavola del livello e correggi spostando le alette.'],
      checks: ['Nessuno spazio tra bordo e cartina', 'Linea centrale in asse con il dito', 'Di profilo la cartina prosegue la lamina', 'Alette chiuse sotto il polpastrello e sui lati'],
      mistakes: ['Ritagliare troppo in una volta sola', 'Staccare tutta la cartina invece di correggere con le alette'] },
    { id: 'es-simmetria', module: 'limatura', level: 'inter', title: 'Controllo da 4 viste su una mano intera', time: '40 min', img: 'controllo-4-viste.svg', caption: 'Alto, profilo, fronte, sotto.', imgs: ['simmetria-asse.svg', 'mano-uniformita.svg'],
      goal: 'Ottenere 5 unghie uguali tra loro e simmetriche, controllandole da quattro punti di vista.',
      materials: ['Mano da allenamento con 5 tip o ricostruzioni', 'Lime 100/180 e 180', 'Buffer', 'Pennarello lavabile', 'Telefono per foto'],
      steps: ['Segna con il pennarello l\'asse e il centro della punta di ogni unghia.', 'Porta tutte le unghie alla stessa lunghezza, poi lima la forma ovale seguendo la sequenza.', 'Fotografa ogni unghia dall\'alto, di profilo, dal davanti e dal basso.', 'Fotografa la mano intera e la mano "a pugno" vista dalle punte.', 'Correggi i difetti trovati e rifai le foto.'],
      checks: ['Punte centrate sull\'asse', 'Lati dritti e paralleli', 'Arco inferiore dritto su tutte', 'Curve a C simili guardando le punte affiancate'],
      mistakes: ['Correggere un lato senza ricontrollare l\'altro', 'Guardare solo dall\'alto'] }
  ];

  /* ==================================================================== QUIZ
   * q = domanda, o = opzioni, a = indice della risposta corretta, e = spiegazione */
  var quiz = {
    onicofagia: [
      { q: 'Quale situazione è una controindicazione su unghie rosicchiate?', o: ['Unghie corte', 'Presenza di pus e gonfiore', 'Cuticole secche', 'Lamina sottile'], a: 1, e: 'Infezione o infiammazione richiedono il medico, non una ricostruzione.' },
      { q: 'Perché si tira la cartina verso il basso su un\'unghia rosicchiata?', o: ['Per risparmiare prodotto', 'Per spingere indietro la pelle rialzata e fare spazio all\'allungamento', 'Per accorciare il letto', 'Per evitare il top'], a: 1, e: 'Crea spazio per l\'allungamento davanti all\'unghia.' },
      { q: 'La causa più frequente della coilonichia (unghia a cucchiaio) è:', o: ['Carenza di ferro', 'Trauma da lima', 'Smalto scuro', 'Acetone'], a: 0, e: 'Se compare da poco, si consiglia un controllo medico.' },
      { q: 'Con un\'unghia ski-jump, cosa si fa prima di applicare il tip?', o: ['Si allunga di più', 'Si riduce la lunghezza naturale', 'Si lucida', 'Si applica il top'], a: 1, e: 'Altrimenti il tip segue la curva verso l\'alto.' },
      { q: 'Su un\'unghia a pinza dolorante l\'onicotecnica:', o: ['Accentua la curva C', 'Fa il pinching', 'Indirizza a medico o podologo', 'Applica acrilico spesso'], a: 2, e: 'La deformità comprime i tessuti: non si forza.' },
      { q: 'Su unghie grasse il ritiro del gel è legato soprattutto a:', o: ['Lampada nuova', 'Olio residuo sulla lamina', 'Colori chiari', 'Cartine di carta'], a: 1, e: 'Disidratante, primer adatto e nuovo sgrassaggio prima della base.' }
    ],
    'cover-colori': [
      { q: 'A cosa serve principalmente il gel cover?', o: ['Lucidare', 'Allungare otticamente il letto ungueale e coprire imperfezioni', 'Sgrassare', 'Ammorbidire le cuticole'], a: 1, e: 'È un costruttore pigmentato color pelle.' },
      { q: 'Perché i gel molto pigmentati vanno stesi sottili?', o: ['Per risparmiare', 'Perché il pigmento assorbe la luce e gli strati profondi polimerizzano male', 'Per un effetto opaco', 'Non serve'], a: 1, e: 'Con strati spessi la parte profonda resta sotto-polimerizzata.' },
      { q: 'Il primo strato di un colore appare striato. È:', o: ['Un difetto del prodotto', 'Normale: il secondo strato uniforma', 'Segno di lampada rotta', 'Da rimuovere sempre'], a: 1, e: 'Molti colori coprono al secondo strato sottile.' },
      { q: 'Quale NON è una causa di ritiro dai bordi?', o: ['Olio sulla lamina', 'Primer ancora umido sui lati', 'Lampada non compatibile', 'Uso di una cartina di carta'], a: 3, e: 'Le prime tre sono cause tipiche di ritiro.' },
      { q: 'Il colore complementare del giallo, che lo neutralizza, è:', o: ['Viola', 'Verde', 'Arancio', 'Rosso'], a: 0, e: 'Sono opposti sul cerchio cromatico.' },
      { q: 'Per un french con camouflage, la sequenza consigliata è:', o: ['Bianco prima, cover dopo', 'Cover prima, poi la smile line', 'Solo top', 'Solo bianco'], a: 1, e: 'Si disegna la smile line sopra il cover.' }
    ],
    piedi: [
      { q: 'Rispetto alle mani, le unghie dei piedi crescono:', o: ['Più velocemente', 'Alla stessa velocità', 'A meno della metà della velocità', 'Non crescono'], a: 2, e: 'Circa 1,6 contro 3,5 mm al mese in uno studio su giovani adulti.' },
      { q: 'Per prevenire l\'unghia incarnita si taglia:', o: ['A punta', 'Molto corta e tonda', 'Dritta, angoli appena smussati', 'Scavando i lati'], a: 2, e: 'Indicazione dei dermatologi (AAD).' },
      { q: 'Un\'unghia gialla, ispessita e friabile:', o: ['Si copre con gel colorato', 'Si lima fino ad assottigliarla', 'Non si tratta: si consiglia medico o podologo', 'Si ricostruisce in acrilico'], a: 2, e: 'Possibile micosi: controindicazione.' },
      { q: 'Chi tratta le unghie incarnite in Italia?', o: ['L\'estetista', 'L\'onicotecnica', 'Il podologo (o il medico)', 'Chiunque abbia una lima'], a: 2, e: 'Il podologo è una professione sanitaria (DM 666/1994).' },
      { q: 'Cliente diabetica con una ferita al piede che non guarisce:', o: ['Pedicure con lama', 'Pediluvio caldo', 'Niente servizio, invio a medico o podologo', 'Semipermanente rinforzato'], a: 2, e: 'Rischio di lesioni non percepite e infezioni.' },
      { q: 'La L. 1/1990 esclude dall\'attività di estetista:', o: ['La manicure estetica', 'Le prestazioni con finalità terapeutica', 'Il trucco', 'Il massaggio estetico'], a: 1, e: 'L\'estetista lavora a scopo estetico.' }
    ],
    'arte-gare': [
      { q: 'Su cosa si applica la polvere chrome?', o: ['Gel colorato non polimerizzato', 'Top no-wipe polimerizzato', 'Base appiccicosa', 'Lamina nuda'], a: 1, e: 'Poi si sigillano i bordi e si mette il top.' },
      { q: 'Nel cat-eye il magnete si usa:', o: ['Dopo il top', 'Prima di polimerizzare lo strato magnetico', 'Dopo la polimerizzazione', 'Non serve'], a: 1, e: 'Le particelle si orientano finché il gel è fluido.' },
      { q: 'Nel one-stroke, per iniziare, il pennello piatto si carica:', o: ['Con un solo colore', 'Circa metà e metà con due colori', 'Fino alla ghiera', 'Asciutto'], a: 1, e: 'Il colore non deve entrare nella ghiera.' },
      { q: 'In gara, il gel non polimerizzato a fine prova comporta:', o: ['−5 punti', 'Nessuna penalità', 'Squalifica', 'Un bonus'], a: 2, e: 'È una regola tipica dei regolamenti Nailympia.' },
      { q: 'La "vista a tunnel" valuta soprattutto:', o: ['La smile line', 'La curva C', 'Il colore', 'La lucentezza'], a: 1, e: 'Si guarda l\'unghia dalla punta.' },
      { q: 'In un\'unghia con decorazione incapsulata, l\'apex:', o: ['Non serve', 'Si costruisce sopra la decorazione', 'Va alla cuticola', 'Si sostituisce con glitter'], a: 1, e: 'La struttura deve restare corretta.' }
    ],
    anatomia: [
      { q: 'Quale parte produce la lamina ungueale?', o: ['Il letto ungueale', 'La matrice', 'L\'iponichio', 'L\'eponichio'], a: 1, e: 'La matrice è il tessuto vivo che produce la lamina; la lunula ne è la parte visibile.' },
      { q: 'Cosa si rimuove durante la preparazione?', o: ['L\'eponichio', 'La cuticola (pelle morta sulla lamina)', 'L\'iponichio', 'Le pieghe laterali'], a: 1, e: 'Si rimuove solo la cuticola morta; eponichio e iponichio sono tessuti vivi.' },
      { q: 'Dove si trova il punto di stress?', o: ['Alla base, sotto la cuticola', 'Dove il bordo libero si stacca dal letto', 'Al centro della lunula', 'Sotto la matrice'], a: 1, e: 'È la zona in cui il bordo libero lascia il letto: lì sopra va l\'apex.' },
      { q: 'Quanto cresce in media un\'unghia della mano?', o: ['Circa 3 mm al mese', 'Circa 1 cm al mese', 'Circa 1 mm all\'anno', 'Circa 365 mm all\'anno'], a: 0, e: 'Circa 0,1 mm al giorno, cioè 3 mm al mese.' },
      { q: 'Una cliente ha un\'unghia ispessita, giallastra e friabile. Cosa fai?', o: ['Copro con un gel coprente', 'Lavoro solo sulle altre dita', 'Rifiuto il servizio, disinfetto e la invio allo specialista', 'Limo via la parte malata'], a: 2, e: 'Il sospetto di onicomicosi è una controindicazione assoluta.' },
      { q: 'Una macchia verde sotto la ricostruzione indica di solito…', o: ['Muffa innocua', 'Un\'infezione batterica (Pseudomonas)', 'Un colore difettoso', 'Una reazione alla lampada'], a: 1, e: 'È un\'infezione batterica: rimuovi il prodotto e invia al medico.' },
      { q: 'Perché non si deve assottigliare la lamina naturale?', o: ['Perché diventa lucida', 'Perché isola meno dal calore e si indebolisce', 'Perché cresce più veloce', 'Non c\'è nessun motivo'], a: 1, e: 'Una lamina sottile espone a picchi di calore e danni.' }
    ],
    igiene: [
      { q: 'Quale trattamento elimina anche le spore?', o: ['Sanificazione', 'Disinfezione', 'Sterilizzazione', 'Detersione'], a: 2, e: 'Solo la sterilizzazione (autoclave) elimina ogni forma di vita.' },
      { q: 'Quale autoclave è adatta a strumenti cavi e porosi come le punte per fresa?', o: ['Classe N', 'Classe B', 'Qualsiasi forno', 'Sterilizzatrice a sfere'], a: 1, e: 'L\'autoclave di classe B (EN 13060) gestisce carichi cavi e porosi.' },
      { q: 'Quali guanti proteggono dai monomeri?', o: ['Lattice', 'Vinile', 'Nitrile', 'Cotone'], a: 2, e: 'Il lattice non protegge dai monomeri: usa il nitrile.' },
      { q: 'Dal 1° settembre 2025 nell\'UE è vietato nei cosmetici…', o: ['L\'HEMA', 'Il TPO', 'L\'acetone', 'L\'EMA'], a: 1, e: 'Il Reg. UE 2025/877 vieta TPO e DMTA, anche per uso professionale e per le scorte.' },
      { q: 'L\'HEMA nei prodotti per unghie è…', o: ['Vietato del tutto', 'Libero per tutti', 'Ammesso solo per uso professionale con avvertenze', 'Ammesso solo nei top'], a: 2, e: 'Reg. UE 2020/1682: uso professionale, con avvertenza sulle reazioni allergiche.' },
      { q: 'Quando è concreto il rischio di allergia agli acrilati?', o: ['Quando il prodotto polimerizzato è sulla lamina', 'Quando il prodotto non polimerizzato tocca la pelle', 'Solo con la lampada LED', 'Mai'], a: 1, e: 'Il contatto della pelle con prodotto non polimerizzato sensibilizza.' },
      { q: 'In Italia la ricostruzione unghie in proprio richiede…', o: ['Solo un attestato privato', 'La qualifica di estetista e la SCIA', 'Nessun requisito', 'La partita IVA e basta'], a: 1, e: 'Rientra nell\'attività di estetista (L. 1/1990); l\'apertura avviene con SCIA.' }
    ],
    sistemi: [
      { q: 'Il gel monofasico…', o: ['Non ha bisogno di lampada', 'Fa da base, costruttore e sigillante', 'Si usa solo per il french', 'È un tipo di acrilico'], a: 1, e: 'Un solo prodotto per tutte e tre le fasi.' },
      { q: 'Come indurisce l\'acrilico?', o: ['In lampada UV', 'All\'aria, per reazione tra liquido e polvere', 'Con l\'acetone', 'Con l\'attivatore spray'], a: 1, e: 'Monomero e polimero reagiscono all\'aria.' },
      { q: 'Una perla di acrilico troppo bagnata…', o: ['È la più resistente', 'Cola nei solchi e lascia monomero sulla pelle', 'È granulosa', 'Non aderisce'], a: 1, e: 'Troppo liquido = colature, ritiro e rischio allergia.' },
      { q: 'Il polygel si lavora con…', o: ['Monomero liquido', 'Slip solution e pennello, poi lampada', 'Acqua', 'Colla per tip'], a: 1, e: 'Si modella con slip solution e indurisce in lampada.' },
      { q: 'Il semipermanente…', o: ['Allunga l\'unghia', 'Dà colore per 2–3 settimane ma non struttura', 'Si toglie solo con la fresa', 'Non va in lampada'], a: 1, e: 'Colore su unghia naturale, nessuna struttura.' },
      { q: 'Per scegliere la lampada conta soprattutto…', o: ['Il numero di watt', 'Il colore della lampada', 'L\'abbinamento tra lunghezze d\'onda e fotoiniziatori del gel', 'La marca'], a: 2, e: 'Usa la lampada adatta al tuo sistema.' },
      { q: 'Picco di emissione tipico di una lampada LED per unghie?', o: ['250 nm', '365 nm soltanto', '385–405 nm', '500 nm'], a: 2, e: 'I LED emettono intorno a 385–405 nm.' }
    ],
    attrezzatura: [
      { q: 'Quale grana è la più abrasiva?', o: ['80', '180', '240', 'Buffer'], a: 0, e: 'Numero più basso = grana più grossa.' },
      { q: 'Quale grana usi sull\'unghia naturale?', o: ['80–100', '100/180', '180–240', 'Carburo'], a: 2, e: '180–240 per opacizzare senza assottigliare.' },
      { q: 'Le punte in carburo si usano…', o: ['Sulla cuticola', 'Solo sul prodotto artificiale', 'Sull\'unghia naturale', 'Per lucidare'], a: 1, e: 'Sulla lamina naturale e sulla cuticola si usano punte diamantate.' },
      { q: 'Velocità indicativa per lavorare in zona cuticolare?', o: ['5.000–10.000 RPM', '20.000–25.000 RPM', '30.000 RPM', 'Massima'], a: 0, e: 'Velocità basse e pressione leggera vicino alla pelle.' },
      { q: 'Perché la punta della fresa deve restare in movimento?', o: ['Per lucidare meglio', 'Per evitare calore da attrito e solchi', 'Per consumare meno', 'Non è necessario'], a: 1, e: 'Fermarsi in un punto scalda e scava.' }
    ],
    preparazione: [
      { q: 'Qual è la prima causa di sollevamento?', o: ['La lampada', 'Una preparazione non accurata', 'Il colore', 'La forma'], a: 1, e: 'Pellicine residue (cuticola), polvere, sebo e umidità sono i nemici dell\'adesione.' },
      { q: 'L\'opacizzazione dell\'unghia naturale serve a…', o: ['Assottigliarla', 'Togliere la lucidità', 'Accorciarla', 'Sbiancarla'], a: 1, e: 'Si toglie solo la lucidità, mai spessore.' },
      { q: 'L\'ordine corretto è…', o: ['Primer → disidratante', 'Disidratante → primer', 'Solo primer', 'Top → primer'], a: 1, e: 'Prima si disidrata, poi si applica il primer.' },
      { q: 'Il primer acido è indicato soprattutto per…', o: ['Semipermanente', 'Acrilico e unghie difficili', 'Top coat', 'Rimozione'], a: 1, e: 'Va usato in quantità minima e solo sulla lamina.' },
      { q: 'Dopo il disidratante…', o: ['Tocco la lamina per controllare', 'Non tocco più la lamina con le dita', 'Lavo le mani della cliente', 'Applico olio'], a: 1, e: 'Il sebo delle dita riduce l\'adesione.' },
      { q: 'Il vero pterigio è…', o: ['La pellicina morta da togliere sempre', 'Una condizione anomala in cui la pelle si salda alla lamina: non si tocca', 'Il bordo libero', 'Un tipo di primer'], a: 1, e: 'Cuticola e pterigio non sono la stessa cosa: il vero pterigio va indirizzato al medico.' },
      { q: 'Con quale angolo tieni lo spingicuticole per arretrare l\'eponichio?', o: ['Dritto, a 90° sulla lamina', 'Quasi piatto, circa 30–45°', 'Capovolto', 'Non importa'], a: 1, e: 'Uno strumento dritto graffia la lamina e preme sulla matrice.' },
      { q: 'Quale grana NON si usa mai sulla lamina naturale?', o: ['240', '180', '100', 'Buffer fine'], a: 2, e: 'Le grane 80–100 servono solo per il prodotto artificiale.' },
      { q: 'Come deve essere il pennello del primer prima di applicarlo?', o: ['Ben carico', 'Quasi asciutto', 'Bagnato di acetone', 'Pulito con olio'], a: 1, e: 'L\'eccesso di primer riduce l\'adesione e rischia di toccare la pelle.' },
      { q: 'Il primer senza acido si applica…', o: ['Su lamina e tip', 'Solo sulla lamina naturale, ad almeno 1 mm dalla pelle', 'Sulla pelle intorno per proteggerla', 'Dopo la base'], a: 1, e: 'Mai su tip e pelle; poi si parte con base o prodotto.' },
      { q: 'Il primer acido è pronto per il prodotto quando…', o: ['È ancora bagnato e lucido', 'È asciutto e appare bianco gessoso', 'Dopo un giorno', 'Dopo il top'], a: 1, e: 'Si lavora sul primer acido asciutto.' }
    ],
    tip: [
      { q: 'Come scegli la misura del tip?', o: ['Il più piccolo possibile', 'Deve coprire da solco a solco', 'Sempre la misura 5', 'In base al colore'], a: 1, e: 'Se sei tra due misure scegli la più grande e lima i lati.' },
      { q: 'Con quale angolo si appoggia il tip?', o: ['90°', 'Circa 45°, poi si abbassa', '0°, piatto subito', '180°'], a: 1, e: 'Abbassandolo lentamente l\'aria esce e non si formano bolle.' },
      { q: 'Durante il blending del tip…', o: ['Limo anche l\'unghia naturale', 'Fondo solo la linea di contatto del tip', 'Uso la grana 80 sulla lamina', 'Uso acetone'], a: 1, e: 'Non si lima l\'unghia naturale.' },
      { q: 'I tip "a contatto"…', o: ['Hanno un incavo da fondere', 'Non hanno incavo e non vanno fusi', 'Si applicano senza colla', 'Sono solo per i piedi'], a: 1, e: 'Non c\'è zona d\'incavo da fondere.' },
      { q: 'Quanto può coprire al massimo l\'incavo del tip?', o: ['Tutta la lamina fino alla cuticola', 'Circa metà della lamina', 'Solo 1 mm', 'Non importa'], a: 1, e: 'Se l\'incavo è più lungo si accorcia prima di incollare.' },
      { q: 'Per quanto tempo tieni premuto il tip dopo averlo abbassato?', o: ['Non serve tenerlo', 'Circa 5–10 secondi, fermo', '2 minuti', 'Finché la cliente sente caldo'], a: 1, e: 'Muoverlo mentre la colla indurisce indebolisce il legame.' },
      { q: 'Quando si taglia il tip?', o: ['Prima di incollarlo, sempre', 'Quando la colla è indurita', 'Mentre la colla è ancora liquida', 'Dopo il top'], a: 1, e: 'A colla fresca il tip si sposta e il legame si rompe.' },
      { q: 'Come tieni la lima durante la fusione?', o: ['Di taglio, premendo', 'Piatta, solo sulla plastica, in movimento', 'Ferma su un punto', 'Sulla pelle'], a: 1, e: 'Ferma o di taglio crea solchi; sulla lamina la assottiglia.' },
      { q: 'Dove applichi il primer in una ricostruzione su tip?', o: ['Su tutto il tip', 'Solo sulla lamina naturale', 'Sulla pelle', 'Non si usa mai'], a: 1, e: 'Sul tip non serve e può rovinare la plastica.' },
      { q: 'Che cosa indica una macchia chiara sotto l\'incavo dopo l\'incollaggio?', o: ['Una bolla d\'aria: il tip va riapplicato', 'Che la colla è perfetta', 'Una micosi', 'Il punto di stress'], a: 0, e: 'Una bolla diventa un sollevamento.' }
    ],
    cartina: [
      { q: 'Dove va costruito l\'apex?', o: ['Alla cuticola', 'Sopra il punto di stress', 'Sulla punta', 'Ovunque'], a: 1, e: 'In zona 2, sopra il punto di stress.' },
      { q: 'Quanto margine lasci dalla pelle in zona cuticolare?', o: ['Nessuno', 'Circa 1 mm', '5 mm', '1 cm'], a: 1, e: 'Circa 1 mm (le fonti indicano 0,5–1,5 mm): il prodotto non deve mai toccare la pelle.' },
      { q: 'Cosa succede se la cartina lascia uno spazio sotto il bordo libero?', o: ['Niente', 'Il prodotto cola sotto e crea sollevamenti', 'L\'unghia è più robusta', 'Si polimerizza prima'], a: 1, e: 'La cartina va a filo del bordo libero.' },
      { q: 'Una ricostruzione piatta, senza apex…', o: ['È più naturale e resistente', 'Si rompe facilmente', 'Non si solleva mai', 'Dura di più'], a: 1, e: 'Senza struttura non regge la lunghezza.' },
      { q: 'Quando si pizzica il gel per la curva a C?', o: ['Prima di stenderlo', 'Dopo una breve polimerizzazione (flash cure)', 'Dopo il top', 'Mai'], a: 1, e: 'Per l\'acrilico invece mentre non è del tutto indurito.' },
      { q: 'La zona 3 deve essere…', o: ['La più spessa', 'Sottilissima', 'Bianca', 'Lucida'], a: 1, e: 'Sottile in zona cuticolare, struttura in zona 2.' },
      { q: 'Di profilo, la cartina corretta…', o: ['È inclinata verso il basso', 'Prosegue in linea la lamina naturale', 'È inclinata verso l\'alto', 'È verticale'], a: 1, e: 'Verso il basso l\'allungamento cade, verso l\'alto si ottiene uno ski-jump.' },
      { q: 'Le alette della cartina si fissano…', o: ['Avvolgendo tutta la nocca', 'Unendole sotto il polpastrello e sui lati del dito', 'Sopra l\'unghia', 'Non si fissano'], a: 1, e: 'Sulla nocca si staccano quando il dito si piega.' },
      { q: 'Una cliente con iponichio lungo sente dolore con la cartina. Cosa fai?', o: ['Spingo di più', 'Ritaglio un incavo più profondo nel punto di contatto', 'Continuo comunque', 'Uso un primer acido'], a: 1, e: 'La cartina deve toccare il bordo libero senza premere sulla pelle viva.' },
      { q: 'Quanto è spesso, indicativamente, il bordo libero finito?', o: ['Come un foglio di carta', 'Circa 1–1,5 mm, come una carta di credito', '5 mm', 'Non conta'], a: 1, e: 'Più spesso si impiglia, più sottile si scheggia.' },
      { q: 'Una perla di acrilico media ha un rapporto liquido/polvere di circa…', o: ['1 : 1', '1,5 : 1', '3 : 1', '1 : 3'], a: 1, e: '1 : 1 è asciutta, 2 : 1 bagnata; il valore esatto dipende dal sistema.' },
      { q: 'Per un risultato equilibrato il bordo libero non dovrebbe superare circa…', o: ['Il doppio del letto ungueale', 'Metà della lunghezza del letto ungueale', '1 mm', 'La lunghezza del dito'], a: 1, e: 'Più lunghezza significa più leva sul punto di stress.' }
    ],
    limatura: [
      { q: 'Quale forma è considerata tra le più resistenti?', o: ['Stiletto', 'Squoval', 'Lipstick', 'Ballerina'], a: 1, e: 'Gli angoli smussati riducono il rischio di rotture.' },
      { q: 'Quale forma slancia di più il dito?', o: ['Quadrata', 'Mandorla', 'Tonda', 'Squoval'], a: 1, e: 'I lati convergenti allungano visivamente il dito.' },
      { q: 'Come si limano i lati?', o: ['Con la lima parallela al solco laterale', 'Entrando nel solco', 'Con la grana 80', 'In diagonale'], a: 0, e: 'Senza entrare nel solco.' },
      { q: 'Il movimento corretto della lima è…', o: ['Avanti e indietro veloce', 'In una sola direzione', 'Circolare con forza', 'Casuale'], a: 1, e: 'Il movimento a "sega" scalda e sfibra.' },
      { q: 'Da quanti punti di vista controlli la ricostruzione?', o: ['Solo dall\'alto', 'Alto, profilo, fronte e sotto', 'Solo di profilo', 'Non serve controllare'], a: 1, e: 'Simmetria, apex, curva a C e pulizia del bordo.' },
      { q: 'In quale ordine si lima una ricostruzione?', o: ['Superficie, punta, lunghezza, lati', 'Lunghezza, lati, punta, superficie, sotto il bordo', 'Solo superficie', 'Punta, cuticola, lunghezza'], a: 1, e: 'La forma si decide sulla lunghezza finale; la superficie si rifinisce dopo.' },
      { q: 'Da dove si parte per ottenere quasi tutte le forme?', o: ['Da una stiletto', 'Da una base quadrata con lati paralleli', 'Da una forma tonda', 'Dalla lipstick'], a: 1, e: 'Togliendo gli angoli in modo diverso si arriva alle altre forme.' },
      { q: 'Come si tiene il dito della cliente durante la limatura?', o: ['Con un dito appoggiato sull\'unghia', 'Ai lati della prima falange, senza toccare la superficie', 'Per la punta dell\'unghia', 'Non si tiene'], a: 1, e: 'Toccare la superficie lascia sebo e impedisce di vedere.' },
      { q: 'Per la ballerina (coffin)…', o: ['I lati si allargano verso la punta', 'I lati si restringono e la punta è dritta', 'La punta è tonda', 'È una quadrata corta'], a: 1, e: 'Si restringe come una stiletto ma ci si ferma prima e si taglia la punta dritta.' },
      { q: 'Perché si segna un puntino al centro della punta prima di limare?', o: ['Per decorare', 'Come riferimento per la simmetria', 'Per il primer', 'Per misurare la grana'], a: 1, e: 'La punta deve cadere sull\'asse del dito.' },
      { q: 'Il top può correggere piccoli difetti di limatura?', o: ['Sì, li nasconde', 'No: il top lucido li mette in risalto', 'Solo sui lati', 'Solo con due strati'], a: 1, e: 'Si corregge con la lima prima del top.' }
    ],
    decorazioni: [
      { q: 'Una buona smile line è…', o: ['Asimmetrica', 'Simmetrica e con la stessa profondità sui lati', 'Piatta', 'Sfumata'], a: 1, e: 'Simmetria e nettezza sono i criteri principali.' },
      { q: 'Il baby boomer è…', o: ['Un french con linea netta', 'Una sfumatura dal nude al bianco', 'Un tipo di gel', 'Una forma'], a: 1, e: 'È un french sfumato.' },
      { q: 'L\'incapsulato consiste nel…', o: ['Chiudere decorazioni tra due strati trasparenti', 'Mettere glitter sul top', 'Usare solo colori', 'Dipingere con il dotter'], a: 0, e: 'Le decorazioni restano protette dentro il prodotto.' },
      { q: 'Lo stamping usa…', o: ['Una piastra incisa e un tampone', 'Una fresa', 'Un attivatore', 'Solo pennelli'], a: 0, e: 'Il disegno viene trasferito dalla piastra.' }
    ],
    manutenzione: [
      { q: 'Ogni quanto si consiglia il refill?', o: ['Ogni settimana', 'Ogni 3–4 settimane', 'Ogni 3 mesi', 'Mai'], a: 1, e: 'Dopo 3–4 settimane l\'apex si è spostato in avanti.' },
      { q: 'Durante il refill le parti sollevate…', o: ['Si coprono con prodotto nuovo', 'Si eliminano completamente', 'Si incollano', 'Si lasciano'], a: 1, e: 'Sotto un sollevamento possono esserci umidità e batteri.' },
      { q: 'Quanto tempo serve in genere per il soak-off?', o: ['1 minuto', '10–15 minuti', '2 ore', '24 ore'], a: 1, e: 'Fino a circa 30 minuti per spessori alti.' },
      { q: 'L\'hard gel si rimuove…', o: ['Con acetone', 'Limando, lasciando un velo sulla lamina', 'Strappandolo', 'Con acqua calda'], a: 1, e: 'Non si scioglie in acetone.' },
      { q: 'Dopo la rimozione…', o: ['Si gratta la lamina', 'Si applica olio per cuticole', 'Si mette subito un nuovo gel senza preparare', 'Si lima con grana 80'], a: 1, e: 'Nutrire la zona aiuta la pelle e la lamina.' }
    ],
    problemi: [
      { q: 'Quale NON è una causa di sollevamento?', o: ['Pterigio non rimosso', 'Prodotto a contatto con la pelle', 'Bordo libero sigillato', 'Refill in ritardo'], a: 2, e: 'Sigillare il bordo libero previene il sollevamento.' },
      { q: 'Il picco di calore è favorito da…', o: ['Strati sottili', 'Strati spessi e lamina assottigliata', 'Gel a basso calore', 'Lampada in low-heat'], a: 1, e: 'La polimerizzazione è esotermica: strati spessi = più calore.' },
      { q: 'La tecnica "flash and pull" serve a…', o: ['Accelerare la polimerizzazione', 'Ridurre il calore percepito', 'Rimuovere il gel', 'Lucidare'], a: 1, e: 'Si toglie la mano dalla lampada qualche secondo e la si rimette.' },
      { q: 'Le grinze sul gel indicano di solito…', o: ['Strato troppo spesso polimerizzato solo in superficie', 'Troppo primer', 'Lima sbagliata', 'Smile line storta'], a: 0, e: 'Strati sottili e tempi corretti risolvono il problema.' },
      { q: 'Un gel sotto-polimerizzato aumenta il rischio di…', o: ['Ingiallimento soltanto', 'Allergia', 'Unghie più dure', 'Nessun problema'], a: 1, e: 'Il monomero non reagito sensibilizza la pelle.' },
      { q: 'Una rottura in zona 2 dipende spesso da…', o: ['Apex assente o mal posizionato', 'Troppo olio', 'Colore scuro', 'Top lucido'], a: 0, e: 'La struttura deve reggere il punto di stress.' }
    ],
    professione: [
      { q: 'Cosa NON serve nella scheda cliente?', o: ['Allergie', 'Farmaci e patologie', 'Il colore preferito dell\'auto', 'Consenso privacy'], a: 2, e: 'La scheda raccoglie dati utili alla sicurezza del servizio.' },
      { q: 'Quale consiglio dai dopo il trattamento?', o: ['Usare le unghie per aprire le lattine', 'Olio per cuticole ogni giorno e guanti per i lavori domestici', 'Staccare da sola il prodotto', 'Saltare il refill'], a: 1, e: 'Cura quotidiana e protezione allungano la durata.' },
      { q: 'Prezzo indicativo di un refill in Italia?', o: ['5 €', '20–35 €', '150 €', '300 €'], a: 1, e: 'Valori indicativi da articoli recenti; variano per zona.' },
      { q: 'Nelle gare i giudici valutano soprattutto…', o: ['Il prezzo', 'Struttura, simmetria, pulizia e smile line', 'La marca dei prodotti', 'La velocità di pagamento'], a: 1, e: 'Apex, curva a C, simmetria e pulizia sono decisivi.' }
    ]
  };

  /* ==================================================================== GLOSSARIO */
  var glossary = [
    { t: 'Onicofagia', d: 'Abitudine di mangiarsi le unghie.' },
    { t: 'Coilonichia', d: 'Unghia a cucchiaio, concava; spesso legata a carenza di ferro.' },
    { t: 'Unghia a pinza (a tegola)', d: 'Unghia con curvatura trasversale accentuata che stringe il letto ungueale.' },
    { t: 'Ski-jump', d: 'Unghia il cui bordo libero punta verso l\'alto.' },
    { t: 'Letto ungueale artificiale', d: 'Prolungamento ottico del letto realizzato con gel cover oltre il letto naturale.' },
    { t: 'Gel cover (camouflage)', d: 'Costruttore pigmentato in tonalità pelle, coprente.' },
    { t: 'Sottotono', d: 'Tonalità di fondo della pelle: fredda, calda o neutra.' },
    { t: 'Colori complementari', d: 'Colori opposti sul cerchio cromatico, che si neutralizzano a vicenda.' },
    { t: 'Shrinkage (ritiro)', d: 'Contrazione del gel durante la polimerizzazione, visibile come distacco dai bordi.' },
    { t: 'Sottopolimerizzazione', d: 'Indurimento incompleto, spesso negli strati profondi o troppo pigmentati.' },
    { t: 'Tinea pedis', d: 'Piede d\'atleta: infezione fungina della pelle del piede.' },
    { t: 'Onicocriptosi', d: 'Unghia incarnita: di competenza del podologo o del medico.' },
    { t: 'Podologo', d: 'Professionista sanitario che tratta le patologie di unghie e piede.' },
    { t: 'Pediluvio pipeless', d: 'Vasca senza tubature di ricircolo, più facile da pulire e disinfettare.' },
    { t: 'Top no-wipe', d: 'Sigillante senza strato di dispersione, che non va sgrassato.' },
    { t: 'Polvere chrome', d: 'Pigmento finissimo che crea l\'effetto specchio se strofinato sul top.' },
    { t: 'Cat-eye', d: 'Gel con particelle metalliche orientabili con un magnete.' },
    { t: 'One-stroke', d: 'Pittura con pennello piatto caricato con due colori, per petali e foglie sfumati.' },
    { t: 'Giudizio alla cieca', d: 'Valutazione di gara senza sapere chi ha eseguito il lavoro.' },
    { t: 'Apex', d: 'Il punto più alto della ricostruzione, in zona 2, costruito sopra il punto di stress per dare resistenza.' },
    { t: 'Autoclave classe B', d: 'Sterilizzatrice a vapore (EN 13060) adatta a strumenti cavi e porosi; elimina anche le spore.' },
    { t: 'Baby boomer', d: 'French sfumato: passaggio graduale dal rosa/nude al bianco.' },
    { t: 'BIAB / soft gel', d: 'Gel costruttore che si rimuove con acetone, usato per coperture e rinforzi.' },
    { t: 'Blending', d: 'Fusione della linea di contatto tra tip e unghia naturale.' },
    { t: 'Bordo libero', d: 'Parte della lamina che sporge oltre il polpastrello.' },
    { t: 'Builder (costruttore)', d: 'Gel che dà struttura e lunghezza alla ricostruzione.' },
    { t: 'Carburo', d: 'Materiale delle punte per fresa da usare solo sul prodotto artificiale.' },
    { t: 'Cartina (form)', d: 'Supporto adesivo posizionato sotto il bordo libero per costruire l\'allungamento.' },
    { t: 'Cleaner', d: 'Liquido che rimuove lo strato di dispersione del gel.' },
    { t: 'Curva a C', d: 'Curvatura trasversale della ricostruzione vista dal bordo libero.' },
    { t: 'Cuticola', d: 'Pellicina morta che si stacca dall\'eponichio e aderisce alla lamina; va rimossa. L\'eponichio, invece, è pelle viva e non si taglia.' },
    { t: 'Disidratante', d: 'Prodotto che toglie umidità e sebo dalla lamina prima del primer.' },
    { t: 'Dotting', d: 'Tecnica di nail art a puntini con il dotter.' },
    { t: 'EMA', d: 'Etil metacrilato: monomero standard dell\'acrilico per unghie.' },
    { t: 'Eponichio', d: 'Piega di pelle viva alla base dell\'unghia; non si taglia.' },
    { t: 'Flash cure', d: 'Polimerizzazione brevissima per fissare il gel prima di proseguire (es. prima del pinching).' },
    { t: 'Flash and pull', d: 'Togliere e rimettere la mano in lampada per ridurre il picco di calore.' },
    { t: 'French', d: 'Unghia con punta bianca separata dalla base da una smile line netta.' },
    { t: 'HEMA', d: 'Metacrilato usato nei gel; nell\'UE ammesso solo per uso professionale (Reg. 2020/1682).' },
    { t: 'Heat spike (picco di calore)', d: 'Bruciore in lampada dovuto alla reazione esotermica della polimerizzazione.' },
    { t: 'Iponichio', d: 'Cresta di pelle sotto il bordo libero che protegge dai patogeni.' },
    { t: 'Incapsulato', d: 'Decorazione chiusa tra due strati di prodotto trasparente.' },
    { t: 'Lamina ungueale', d: 'La placca dura di cheratina che chiamiamo comunemente unghia.' },
    { t: 'Letto ungueale', d: 'Tessuto vascolarizzato su cui poggia la lamina.' },
    { t: 'Lifting (sollevamento)', d: 'Distacco del prodotto dalla lamina, di solito in zona cuticolare o laterale.' },
    { t: 'Lunula', d: 'Mezzaluna chiara alla base dell\'unghia: la parte visibile della matrice.' },
    { t: 'Matrice', d: 'Tessuto vivo che produce la lamina; un danno può essere permanente.' },
    { t: 'MMA', d: 'Metil metacrilato: monomero da evitare, vietato dalla FDA per le unghie.' },
    { t: 'Monomero', d: 'Il liquido del sistema acrilico.' },
    { t: 'Onicolisi', d: 'Distacco della lamina dal letto ungueale.' },
    { t: 'Onicomicosi', d: 'Infezione fungina dell\'unghia: controindicazione assoluta al servizio.' },
    { t: 'Paronichia', d: 'Infezione dei tessuti attorno all\'unghia, con rossore e gonfiore.' },
    { t: 'Perla', d: 'Pallina di acrilico raccolta con il pennello; la consistenza dipende dal rapporto liquido/polvere.' },
    { t: 'Pinching', d: 'Pressione laterale per creare la curva a C.' },
    { t: 'Polygel', d: 'Pasta ibrida tra acrilico e gel che si modella con slip solution e indurisce in lampada.' },
    { t: 'Primer', d: 'Promotore di adesione: acido (incide la lamina) o senza acido (effetto biadesivo).' },
    { t: 'Pterigio', d: 'Condizione anomala in cui la pelle (eponichio) si salda alla lamina e avanza con lei. Non si taglia né si spinge: si indirizza al medico. Da non confondere con la cuticola.' },
    { t: 'Punto di stress', d: 'Zona in cui il bordo libero si stacca dal letto ungueale.' },
    { t: 'Refill', d: 'Riempimento della ricrescita ogni 3–4 settimane, con riequilibrio della struttura.' },
    { t: 'SCIA', d: 'Segnalazione certificata di inizio attività da presentare al Comune/SUAP.' },
    { t: 'Semipermanente', d: 'Smalto in gel che polimerizza in lampada e dura 2–3 settimane.' },
    { t: 'Slip solution', d: 'Liquido per lavorare il polygel con il pennello senza che si attacchi.' },
    { t: 'Smile line', d: 'Linea che separa la parte bianca del french dal resto dell\'unghia.' },
    { t: 'Soak-off', d: 'Rimozione con acetone, cotone e stagnola.' },
    { t: 'Squoval', d: 'Forma quadrata con angoli arrotondati.' },
    { t: 'Strato di dispersione', d: 'Patina appiccicosa che resta su alcuni gel dopo la polimerizzazione.' },
    { t: 'Striping', d: 'Tecnica di nail art a linee con pennello sottile.' },
    { t: 'Tip', d: 'Unghia artificiale preformata da incollare sul bordo libero.' },
    { t: 'TPO', d: 'Fotoiniziatore vietato nei cosmetici UE dal 1° settembre 2025 (Reg. 2025/877).' },
    { t: 'Zone 1-2-3', d: 'Bordo libero (1), apex/struttura (2) e zona cuticolare (3) della ricostruzione.' },
    { t: 'Curette', d: 'Strumento a cucchiaino affilato con cui si solleva la cuticola dalla lamina, tenuto piatto.' },
    { t: 'Spingicuticole', d: 'Strumento metallico con un\'estremità piatta per arretrare l\'eponichio e una a lama per sollevare la cuticola.' },
    { t: 'Opacizzazione', d: 'Rimozione della sola lucidità della lamina con grana fine (180–240) per migliorare l\'adesione, senza assottigliare.' },
    { t: 'Luce radente', d: 'Luce che arriva molto inclinata sulla superficie: evidenzia zone lucide, pellicine e avvallamenti.' },
    { t: 'Bonder', d: 'Altro nome del primer senza acido: promotore di adesione con effetto biadesivo.' },
    { t: 'Acido metacrilico', d: 'Componente del primer acido: incide la lamina ed è corrosivo per pelle e occhi.' },
    { t: 'Emolliente per cuticole', d: 'Prodotto che ammorbidisce la pelle morta; va eliminato del tutto prima di opacizzare.' },
    { t: 'Incavo (well)', d: 'Parte sottile del tip che si incolla sull\'unghia naturale; non dovrebbe coprire più di metà lamina.' },
    { t: 'Punto d\'arresto (stop)', d: 'Gradino del tip che si appoggia contro il bordo libero naturale.' },
    { t: 'Zona di contatto', d: 'Superficie del tip che tocca la lamina e forma il legame con la colla.' },
    { t: 'Cianoacrilato', d: 'La colla per tip: indurisce in pochi secondi a contatto con l\'umidità.' },
    { t: 'Tagliatip', d: 'Tronchesino a lama dritta per accorciare il tip senza crepare la plastica.' },
    { t: 'Tip blender', d: 'Solvente che ammorbidisce la plastica del tip per facilitare la fusione; si usa pochissimo e solo sul tip.' },
    { t: 'ABS', d: 'Plastica rigida con cui sono fatti molti tip.' },
    { t: 'Slip layer', d: 'Velo sottilissimo di gel non polimerizzato su cui la perla di costruttore scivola meglio.' },
    { t: 'Livello della cartina', d: 'Allineamento della cartina con la lamina vista di profilo: né verso il basso né verso l\'alto.' },
    { t: 'Linee di crescita', d: 'Sottili scanalature longitudinali della lamina: guida per allineare cartina e allungamento.' },
    { t: 'Rapporto liquido/polvere', d: 'Proporzione tra monomero e polimero nella perla di acrilico; media circa 1,5 : 1.' },
    { t: 'Dappen', d: 'Piccolo contenitore con coperchio per il monomero durante il lavoro in acrilico.' },
    { t: 'Linea del sorriso naturale', d: 'Il confine tra letto ungueale rosa e bordo libero bianco dell\'unghia naturale.' },
    { t: 'Letto ungueale (lunghezza)', d: 'Distanza tra cuticola e linea del sorriso: riferimento per decidere la lunghezza dell\'allungamento.' },
    { t: 'Arco superiore', d: 'Linea del profilo dell\'unghia dall\'apex alla punta.' },
    { t: 'Arco inferiore', d: 'Linea sotto l\'allungamento vista di profilo; deve essere dritta, senza "pance".' },
    { t: 'Lati paralleli', d: 'I due lati dell\'allungamento dritti e alla stessa distanza dall\'asse, in prosecuzione dei solchi laterali.' },
    { t: 'Asse del dito', d: 'Linea immaginaria dal centro della cuticola lungo il dito: riferimento per la simmetria.' },
    { t: 'Ballerina (coffin)', d: 'Forma con lati che si restringono e punta dritta.' },
    { t: 'Mandorla', d: 'Forma con lati convergenti e punta arrotondata più stretta dell\'ovale.' },
    { t: 'Stiletto', d: 'Forma a punta con lati dritti; la più delicata.' },
    { t: 'Buffer', d: 'Blocchetto o lima morbida a grana fine per levigare la superficie.' }
  ];

  // esercizi ordinati secondo l'ordine dei moduli
  var order = {};
  modules.forEach(function (m, i) { order[m.id] = i; });
  exercises.sort(function (a, b) { return order[a.module] - order[b.module]; });

  window.NAILX = { modules: modules, exercises: exercises, quiz: quiz, glossary: glossary };
})();
