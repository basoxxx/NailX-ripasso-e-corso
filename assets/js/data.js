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
      id: 'decorazioni', summary: ["Smile line netta, simmetrica, con la stessa profondità sui lati e su tutte le dita.", "Il bianco si stende in strati sottili: i pigmenti schermano la luce.", "Varianti: reverse (sempre a circa 1 mm dalla pelle), V, micro e french colorato.", "Baby boomer: sfumatura graduale, si sfuma con il pennello, non con la lima.", "Incapsulato: decorazione tra due strati trasparenti, apex sopra.", "Stamping: smalto dedicato, raschietto a 45°, tampone rotolato, lavoro veloce."], n: 9, level: 'inter', title: 'French, baby boomer e nail art',
      desc: 'Smile line, varianti del french, sfumature, incapsulati e tecniche base di decorazione.',
      lessons: [
        {
          id: 'french', videos: [{"id": "7Bwz_1rcTuA", "title": "How to Create the Perfect French Smile Line", "channel": "Naio Nails", "lang": "EN"}, {"id": "hf6JqVGkwV4", "title": "Technique to Shaping Beautiful Smile Lines", "channel": "Nail Career Education", "lang": "EN"}], simple: "Il french è una punta bianca separata dal rosa da una curva netta, la smile line. Deve essere uguale sui due lati e uguale su tutte e dieci le dita.", title: 'Il french e la smile line', min: 14,
          html: `
<p>Il <strong>french</strong> è la decorazione più richiesta e anche la più "spietata": un errore di simmetria si vede da lontano. Il bianco della punta è separato dal rosa del letto ungueale da una curva chiamata <strong>smile line</strong> (linea del sorriso).</p>
${F('smile-line.svg', 'Smile line corrette ed errate.')}
<h2>Le parole del french</h2>
<table>
<tr><th>Termine</th><th>Che cos'è</th></tr>
<tr><td><strong>Smile line</strong></td><td>La curva che separa il bianco dal rosa.</td></tr>
<tr><td><strong>Punti laterali</strong> (o "ali")</td><td>I due punti dove la smile line tocca i lati dell'unghia.</td></tr>
<tr><td><strong>Punto centrale</strong></td><td>Il centro della curva: il punto della smile line più vicino alla punta.</td></tr>
<tr><td><strong>Profondità</strong></td><td>La differenza di altezza tra i punti laterali e il punto centrale. Più è grande, più la curva è "profonda".</td></tr>
<tr><td><strong>Pink &amp; white</strong></td><td>French scolpito: rosa (o cover) per il letto, bianco per la punta, entrambi come struttura.</td></tr>
</table>
<h2>Come deve essere una smile line corretta</h2>
<ul>
<li><strong>Netta</strong>: il passaggio bianco/rosa è una linea pulita, senza sbavature né "denti".</li>
<li><strong>Simmetrica</strong>: i due punti laterali sono alla stessa altezza.</li>
<li><strong>Proporzionata</strong>: la profondità sta bene con la forma dell'unghia. Una regola usata dagli educator è <strong>ripetere la curva della cuticola</strong>: la smile "fa eco" alla linea in basso, come un'immagine allo specchio.</li>
<li><strong>Uguale su tutte le dita</strong>: guardando le dieci unghie insieme, le smile line sembrano gemelle.</li>
<li><strong>Allunga il letto</strong>: la smile non deve per forza seguire il bordo libero naturale della cliente. Spesso si disegna un po' più in alto per far sembrare il letto più lungo.</li>
</ul>
${F('smile-line-profondita.svg', 'Piatta, corretta, troppo profonda: la curva giusta ha la stessa profondità (d) della curva della cuticola.')}
${B('info', 'Perché la profondità conta', 'Una smile line troppo piatta fa sembrare l\'unghia più larga e corta. Una troppo profonda la fa sembrare "appuntita" e innaturale. La curva che ripete la cuticola è la più armoniosa per la maggior parte delle unghie.')}
<h2>Quattro modi di fare il french</h2>
<table>
<tr><th>Tecnica</th><th>Come si fa</th><th>Vantaggi</th><th>Limiti</th></tr>
<tr><td><strong>Dipinto</strong> (gel colorato o semipermanente bianco)</td><td>Su una base già costruita e polimerizzata, con pennello liner o piatto</td><td>Il più facile per iniziare; si corregge prima della lampada</td><td>Il bianco non dà struttura; serve più di uno strato sottile</td></tr>
<tr><td><strong>Gel bianco scolpito</strong> (pink &amp; white in gel)</td><td>Builder bianco sulla punta (spesso su cartina o tip), poi rosa/cover sopra</td><td>Bianco durevole, smile "dentro" la struttura</td><td>Richiede controllo del pennello e della consistenza</td></tr>
<tr><td><strong>Acrilico bianco</strong></td><td>Perla di polvere bianca posata e premuta fino alla smile</td><td>Smile molto netta e veloce per chi è esperta</td><td>Serve un ottimo controllo della perla (rapporto liquido/polvere)</td></tr>
<tr><td><strong>Tip french o stencil</strong></td><td>Tip con punta già bianca, o adesivi guida</td><td>Veloce, uniforme</td><td>Smile fissa, non personalizzata sulla cliente</td></tr>
</table>
<h2>Passo passo: french dipinto in gel (metodo dei punti guida)</h2>
${F('french-punti-guida.svg', 'Metodo dei punti guida: centro, due punti laterali alla stessa altezza, collega dal lato al centro, riempi e sigilla.')}
<ol class="steps">
<li><strong>Prepara e costruisci</strong> come sempre (preparazione, base, eventuale struttura) e polimerizza. <em>Perché</em>: il french dipinto è solo colore, la resistenza la dà la struttura sotto.</li>
<li><strong>Scegli l'altezza</strong> della smile guardando tutte e dieci le dita: la decidi una volta e la ripeti.</li>
<li><strong>Segna il punto centrale</strong> con la punta del pennello: è il centro della curva, il punto della smile più vicino alla punta.</li>
<li><strong>Segna i due punti laterali</strong> sui bordi dell'unghia, più vicini alla cuticola, alla <strong>stessa altezza</strong> su entrambi i lati. <em>Perché</em>: la differenza di altezza tra i punti laterali e il centro crea la profondità.</li>
<li><strong>Collega</strong> ogni punto laterale al centro con un movimento unico e fluido, prima un lato poi l'altro. Ruota il dito della cliente invece di storcere il polso.</li>
<li><strong>Riempi</strong> fino al bordo e <strong>sigilla il bordo libero</strong> (passa il pennello anche sullo spessore della punta).</li>
<li><strong>Correggi prima della lampada</strong>: un pennello piatto pulito, appena inumidito di cleaner, "taglia" la linea e toglie le sbavature.</li>
<li><strong>Polimerizza</strong> e, se il bianco è trasparente, ripeti con un secondo strato sottile sopra la stessa linea.</li>
<li><strong>Top coat</strong> su tutta l'unghia, bordo libero compreso; polimerizza e, se serve, togli lo strato di dispersione.</li>
</ol>
${F('tut-french.svg', 'French passo passo.')}
${B('tip', 'Controlla la simmetria', 'Capovolgi la mano della cliente e guarda le unghie "a testa in giù": l\'occhio vede subito il lato più alto. Poi confronta le dita a coppie (indice con anulare, medio da solo, mignolo più piccolo ma con la stessa curva).')}
${B('warn', 'Il bianco va steso sottile', 'I pigmenti bianchi schermano la luce della lampada (effetto ombrello): uno strato spesso si indurisce in superficie ma resta morbido sotto. Meglio due strati sottili polimerizzati bene che uno spesso.')}
<h2>French scolpito (pink &amp; white): l'essenziale</h2>
<ul>
<li>Il bianco si posa sulla punta come <strong>zona 1</strong> della costruzione; poi il rosa o il cover costruisce zona 2 e zona 3 con l'<strong>apex</strong> sopra il punto di stress.</li>
<li>In acrilico la perla bianca si appoggia un po' <strong>lontano</strong> da dove vuoi la smile e si spinge in avanti con piccoli tocchi: premendola, il prodotto avanza.</li>
<li>Una perla troppo bagnata dà un bianco trasparente e difficile da controllare; troppo asciutta non si stende e crea bolle.</li>
</ul>
<h2>Errori frequenti</h2>
<table>
<tr><th>Errore</th><th>Causa probabile</th><th>Come correggere</th></tr>
<tr><td>Smile piatta</td><td>Punti laterali quasi alla stessa altezza del centro (poca profondità)</td><td>Segna i punti laterali più vicini alla cuticola; ripeti la curva della cuticola</td></tr>
<tr><td>Lati ad altezze diverse</td><td>Dito ruotato, punti segnati "a occhio"</td><td>Segna i punti guida; controlla a mano capovolta</td></tr>
<tr><td>Bianco striato o trasparente</td><td>Strato troppo sottile o pennello sporco di colore</td><td>Secondo strato sottile; pennello pulito</td></tr>
<tr><td>Grinze sul bianco</td><td>Strato troppo spesso</td><td>Strati sottili, polimerizzazione completa</td></tr>
<tr><td>Bordo libero che si scheggia</td><td>Bordo non sigillato</td><td>Passa colore e top sullo spessore della punta</td></tr>
<tr><td>Smile diversa su ogni dito</td><td>Altezza decisa dito per dito</td><td>Decidi l'altezza prima e usa la stessa per tutte</td></tr>
</table>
`,
          sources: ['https://www.scratchmagazine.co.uk/feature/how-to-create-a-crisp-smile-line-with-the-gel-system',
            'https://www.scratchmagazine.co.uk/nail_art/classic-french-manicure-using-gel',
            'https://www.scratchmagazine.co.uk/nail_art/how-to-perfect-a-french-tip',
            'https://www.opi.com/professionals/gelcolor-french-manicure-application',
            'https://www.salongeek.com/threads/how-do-you-do-your-smile-line-using-gel.86701/',
            'https://nailknowledge.org/blog/uv-curing-why-thin-layers-matter-for-perfect-nails']
        },
        {
          id: 'french-varianti', simple: "Il french si può reinventare: la mezzaluna alla base (reverse), la punta a V, una linea sottilissima (micro) o un colore al posto del bianco. Le regole restano le stesse: simmetria e linea netta.", title: 'Varianti del french: reverse, V, micro, colorato', min: 9,
          html: `
<p>Una volta che sai fare una smile line pulita, puoi cambiare <strong>forma</strong>, <strong>posizione</strong> o <strong>colore</strong> del french. Le regole non cambiano: simmetria, linea netta, stessa misura su tutte le dita.</p>
${F('french-varianti.svg', 'Classico, a V, micro, reverse, colorato e doppio.')}
<table>
<tr><th>Variante</th><th>Com'è</th><th>Su quale unghia sta meglio</th><th>Difficoltà</th></tr>
<tr><td><strong>V-french</strong> (chevron)</td><td>Due linee dritte che si incontrano al centro a punta</td><td>Mandorla, stiletto; slancia le dita</td><td>Media: le due linee devono avere la stessa inclinazione</td></tr>
<tr><td><strong>Micro french</strong></td><td>Linea sottilissima solo sul bordo libero</td><td>Unghie corte; look naturale</td><td>Media: serve un pennello liner molto fine</td></tr>
<tr><td><strong>French colorato</strong></td><td>Un colore al posto del bianco</td><td>Tutte</td><td>Come il classico</td></tr>
<tr><td><strong>Doppio french</strong></td><td>Una seconda linea sottile sotto la smile</td><td>Unghie medio-lunghe</td><td>Alta: due curve parallele</td></tr>
<tr><td><strong>Reverse french</strong> (mezzaluna)</td><td>Un arco di colore alla base, vicino alla cuticola</td><td>Tutte; ricorda la lunula</td><td>Alta: si lavora vicinissimo alla pelle</td></tr>
</table>
<h2>Reverse french passo passo (gel o semipermanente)</h2>
${F('reverse-french-step.svg', 'Reverse french: base e colore, arco dal centro verso i lati, margine di circa 1 mm dalla pelle, top opaco con mezzaluna lucida.')}
<ol class="steps">
<li>Prepara, applica la base e due strati sottili del colore di fondo, polimerizzando ogni strato.</li>
<li>Con un pennello liner, disegna l'<strong>arco alla base</strong> partendo dal <strong>centro</strong> e andando verso i lati: così la curva resta regolare.</li>
<li>Lascia sempre il <strong>margine libero</strong> dalla pelle: circa <strong>1 mm</strong> (le fonti indicano 0,5–1,5 mm). Il colore non deve mai toccare la pelle.</li>
<li>Pulisci le sbavature prima della lampada con un pennello pulito; polimerizza.</li>
<li>Ripeti l'arco per coprire meglio, poi top coat.</li>
<li>Variante elegante: top <strong>opaco</strong> su tutta l'unghia lasciando <strong>lucida</strong> solo la mezzaluna.</li>
</ol>
${B('warn', 'Vicino alla pelle', 'Nel reverse french il colore sta vicino alla cuticola. Se tocca la pelle non polimerizza bene: rischio di sollevamento e di allergia. Pulisci sempre prima della lampada.')}
<h2>V-french in tre mosse</h2>
<ol class="steps">
<li>Segna il <strong>punto centrale</strong> della V.</li>
<li>Traccia una linea dritta da un lato al punto centrale, poi dall'altro lato con la <strong>stessa inclinazione</strong>.</li>
<li>Riempi verso la punta, sigilla il bordo libero, top.</li>
</ol>
${B('tip', 'Allenati su tip', 'Disegna 10 V-french e 10 reverse su una ruota di tip prima di proporli: confronta le unghie a coppie e cerca la stessa misura.')}
`,
          sources: ['https://www.opi.com/nail-art/glow-with-the-flow',
            'https://www.opi.com/professionals/gelcolor-french-manicure-application',
            'https://www.scratchmagazine.co.uk/feature/how-to-reverse-french-using-halos-polibuild',
            'https://www.design4nails.co.uk/?p=285413']
        },
        {
          id: 'baby-boomer', videos: [{"id": "0L3JT8K-fx8", "title": "Baby boomer in gel: tutorial dettagliato", "channel": "Nail Couture Italia", "lang": "IT"}, {"id": "GamgGumobZE", "title": "Tutorial baby boomer con builder gel", "channel": "Crystal Nails Italia", "lang": "IT"}], simple: "Il baby boomer è un french senza linea: il bianco della punta sfuma piano piano nel rosa. La sfumatura si fa con il pennello, a strati sottili.", title: 'Baby boomer', min: 10,
          html: `
<p>Il <strong>baby boomer</strong> è un "french sfumato": il colore passa in modo graduale dal nude/rosa della base al bianco della punta, <strong>senza una linea netta</strong>. È una sfumatura <em>verticale</em> (dalla cuticola alla punta); quando si usano altri colori si parla in genere di <em>ombré</em>.</p>
${F('baby-boomer.svg', 'Baby boomer in tre passaggi.')}
<h2>Quale materiale scegliere</h2>
<table>
<tr><th>Materiale</th><th>Come si sfuma</th><th>Vantaggi</th><th>Attenzione a</th></tr>
<tr><td><strong>Semipermanente</strong></td><td>Pennello liner o pennello piatto pulito, prima della lampada</td><td>Facile, sottile, ideale per allenarsi</td><td>Dura come un semipermanente: 2–3 settimane</td></tr>
<tr><td><strong>Gel builder</strong> (bianco lattiginoso + cover/milky pink)</td><td>Pennello che "tira" il bianco verso l'alto e il cover sopra il bianco</td><td>Struttura e colore insieme</td><td>Limare poco: la lima "taglia" la sfumatura</td></tr>
<tr><td><strong>Acrilico</strong> (polvere bianca + cover)</td><td>Perle di consistenza diversa, sfumate con il pennello</td><td>Veloce per chi conosce la perla</td><td>Serve un buon controllo del rapporto liquido/polvere</td></tr>
<tr><td><strong>Spugnetta</strong></td><td>Bianco picchiettato in più passaggi leggeri</td><td>Sfumatura molto morbida</td><td>Pulire bene la pelle prima della lampada</td></tr>
</table>
${B('tip', 'Colori semitrasparenti', 'Per iniziare scegli un bianco lattiginoso e un nude semitrasparente: si sfumano molto più facilmente di un bianco coprente e perdonano gli errori.')}
<h2>Passo passo in gel builder</h2>
${F('baby-boomer-step.svg', 'Baby boomer in gel: bianco sulla punta, sfuma verso l\'alto, cover sopra con apex, top.')}
<ol class="steps">
<li><strong>Prepara</strong> l'unghia e applica la base; polimerizza.</li>
<li>Posa il <strong>bianco lattiginoso</strong> sulla punta, in uno strato sottile.</li>
<li><strong>Sfuma verso l'alto</strong> con il pennello pulito e asciutto, con colpi leggeri e brevi, fermandoti circa a metà unghia. <em>Perché</em>: colpi brevi creano passaggi graduali; un colpo lungo trascina il bianco e crea una striscia.</li>
<li>Polimerizza.</li>
<li>Costruisci la <strong>struttura</strong> (apex in zona 2) con il gel cover o milky pink, e passa leggermente l'eccesso <strong>sopra</strong> il bianco: il bianco "affiora" sotto un velo rosato.</li>
<li>Polimerizza, togli lo strato di dispersione.</li>
<li><strong>Lima con delicatezza</strong> solo per la forma. <em>Perché</em>: se limi molto sulla zona sfumata la assottigli e la sfumatura diventa a macchie.</li>
<li><strong>Top coat</strong> e bordo libero sigillato.</li>
</ol>
<h2>Versione in semipermanente</h2>
<ol class="steps">
<li>Base e polimerizzazione.</li>
<li>Bianco sulla metà superiore dell'unghia.</li>
<li>Con un pennello liner pulito "rompi" il bordo inferiore del bianco con piccoli movimenti in su e in giù; polimerizza.</li>
<li>Nude su tutta l'unghia; se serve, prima della lampada, tira un po' di nude dentro il bianco con il pennello. Polimerizza.</li>
<li>Ripeti bianco e nude finché la sfumatura è uniforme, poi top.</li>
</ol>
${F('sfumatura-errori.svg', 'Sfumatura corretta ed errori tipici: linea visibile, troppo bianco, gobba sulla punta.')}
<h2>Errori frequenti</h2>
<table>
<tr><th>Errore</th><th>Perché succede</th><th>Rimedio</th></tr>
<tr><td>Si vede una linea</td><td>Bianco troppo coprente, sfumato poco</td><td>Bianco lattiginoso, più passaggi brevi</td></tr>
<tr><td>Sembra un french sbavato</td><td>Troppo bianco o sfumatura troppo corta</td><td>Meno prodotto, sfuma più in alto</td></tr>
<tr><td>Gobba sulla punta</td><td>Strati spessi sovrapposti</td><td>Strati sottili; controlla il profilo</td></tr>
<tr><td>Sfumatura a macchie</td><td>Limatura troppo forte sulla zona sfumata</td><td>La sfumatura si fa con il pennello, non con la lima</td></tr>
<tr><td>Altezza diversa sulle dita</td><td>Nessun riferimento</td><td>Decidi un'altezza (per esempio metà unghia) e ripetila</td></tr>
</table>
`,
          sources: ['https://pinkgellac.com/blogs/news/baby-boomer-nails',
            'https://salongeek.com/threads/baby-boomer-nails.323883',
            'https://onglesdor.com/en/blog/make-your-babyboomer-with-oh-blush-gel-and-powder.html']
        },
        {
          id: 'nail-art', videos: [{"id": "td7E52DtfMc", "title": "Come realizzare un effetto cat eye", "channel": "The Pink Glove Nails", "lang": "IT"}], simple: "La nail art di base usa pochi attrezzi: dotter per i puntini, pennello sottile per le linee, piastra e tampone per lo stamping. La decorazione non deve mai rovinare la struttura.", title: 'Incapsulati e nail art di base', min: 14,
          html: `
<p>La <strong>nail art</strong> trasforma una ricostruzione in un piccolo disegno. Le tecniche di base sono quattro: <strong>incapsulato</strong>, <strong>dotting</strong>, <strong>striping</strong> e <strong>stamping</strong>. Gli effetti speciali (chrome, cat-eye, one-stroke) sono nel modulo <em>Nail art avanzata e gare</em>.</p>
${F('nail-art.svg', 'Dotting, striping, incapsulato e stamping.')}
<h2>Gli attrezzi</h2>
<table>
<tr><th>Attrezzo</th><th>A cosa serve</th><th>Consiglio</th></tr>
<tr><td><strong>Dotter</strong></td><td>Puntini, cuori, fiori</td><td>Usa almeno 3 misure di sfera</td></tr>
<tr><td><strong>Pennello liner / striper</strong></td><td>Linee sottili e lunghe</td><td>Setole lunghe per linee dritte, corte per i dettagli</td></tr>
<tr><td><strong>Piastra da stamping</strong></td><td>Disegni incisi da trasferire</td><td>Pulisci la piastra subito dopo ogni uso</td></tr>
<tr><td><strong>Raschietto</strong> (scraper)</td><td>Toglie lo smalto in eccesso dalla piastra</td><td>Bordo dritto e liscio</td></tr>
<tr><td><strong>Tampone</strong> (stamper)</td><td>Raccoglie il disegno e lo posa sull'unghia</td><td>Morbido e pulito, senza polvere</td></tr>
<tr><td><strong>Pinzetta / bastoncino</strong></td><td>Posare glitter grandi, foglia, strass</td><td>Bastoncino appena inumidito di top per "pescare"</td></tr>
</table>
<h2>Regola d'oro: la decorazione non rovina la struttura</h2>
<p>Una decorazione appoggiata sopra un'unghia finita crea una <strong>gobba</strong> che si aggancia ovunque e si scheggia. Per questo le decorazioni in rilievo si <strong>incapsulano</strong> e, quando si costruisce, l'<strong>apex va sopra la decorazione</strong>.</p>
${F('incapsulato-sezione.svg', 'Incapsulato in sezione: base, decorazione piatta, prodotto trasparente con apex sopra, top. Errore: bordo scoperto.')}
<h2>Incapsulato passo passo</h2>
<ol class="steps">
<li>Prepara e costruisci uno strato sottile di base o builder; polimerizza.</li>
<li>Scegli decorazioni <strong>piatte e asciutte</strong> (glitter, foglia, fiori secchi ben essiccati, carta decorativa).</li>
<li>Posale con il bastoncino o la pinzetta; fissale con un velo di prodotto trasparente e un breve flash in lampada.</li>
<li>Copri tutto con builder trasparente: la decorazione deve essere <strong>completamente chiusa</strong>, bordi compresi.</li>
<li>Costruisci l'<strong>apex sopra la decorazione</strong>, controlla il profilo e polimerizza.</li>
<li>Lima con cautela: se la lima "scopre" la decorazione, aggiungi prodotto e ripeti.</li>
<li>Top coat e bordo libero sigillato.</li>
</ol>
${B('warn', 'Niente bordi scoperti', 'Un bordo di glitter o di fiore che esce dal prodotto trattiene sporco e acqua, si stacca e può far sollevare tutta la ricostruzione. Se lo senti con il polpastrello, va coperto.')}
<h2>Dotting (puntini)</h2>
${F('dotting-striping-presa.svg', 'Presa corretta: dotter verticale e mignolo appoggiato; pennello liner trascinato verso di te.')}
<ol class="steps">
<li>Metti una goccia di colore sulla tavolozza.</li>
<li>Intingi il dotter tenendolo <strong>verticale</strong> e appoggialo sull'unghia senza premere.</li>
<li>Per puntini uguali, <strong>ricarica a ogni punto</strong>; per puntini decrescenti, fai più punti con una sola carica.</li>
<li>Pulisci la sfera con una salvietta tra un colore e l'altro.</li>
</ol>
<h2>Striping (linee)</h2>
<ol class="steps">
<li>Appoggia il mignolo della tua mano sul tavolo o sulla mano della cliente: <strong>mano ferma = linea ferma</strong>.</li>
<li>Carica il pennello solo nella parte finale delle setole.</li>
<li>Appoggia la punta, poi <strong>trascina</strong> il pennello verso di te con pressione costante. Non "spingere" in avanti.</li>
<li>Per linee lunghe guarda il punto di arrivo, non la punta del pennello.</li>
</ol>
<h2>Stamping passo passo</h2>
${F('stamping-step.svg', 'Stamping: smalto sulla piastra, raschia a 45°, raccogli rotolando, posa rotolando, sigilla.')}
<ol class="steps">
<li>Prepara tutto prima: lo smalto da stamping <strong>asciuga in pochi secondi</strong>.</li>
<li>Stendi lo smalto da stamping (più denso e coprente di uno smalto normale) sul disegno della piastra.</li>
<li>Passa il <strong>raschietto a circa 45°</strong> con un solo movimento deciso: lo smalto resta solo nelle incisioni.</li>
<li>Subito dopo, <strong>rotola il tampone</strong> sul disegno con un movimento unico. Non strisciare.</li>
<li>Posiziona il tampone sopra l'unghia e <strong>rotolalo da un lato all'altro</strong>.</li>
<li>Pulisci i bordi della pelle e sigilla con un top compatibile con il prodotto usato.</li>
</ol>
${B('tip', 'Pressione', 'Troppa pressione sul tampone spinge lo smalto fuori dalle incisioni e il disegno "si allarga"; troppo poca lascia buchi. Fai prove su un tip prima di lavorare sulla cliente.')}
<h2>Adesivi e transfer</h2>
<ul>
<li><strong>Adesivi (sticker)</strong>: si posano su colore polimerizzato, si premono bene ai bordi e si sigillano con top su tutta la superficie.</li>
<li><strong>Transfer / foil</strong>: si usano con una colla dedicata o su gel lasciato appiccicoso; si preme il foil e lo si strappa con un colpo secco (vedi modulo avanzato).</li>
</ul>
<h2>Errori frequenti</h2>
<table>
<tr><th>Errore</th><th>Causa</th><th>Rimedio</th></tr>
<tr><td>Puntini di misure diverse</td><td>Ricarica irregolare del dotter</td><td>Una carica per ogni punto</td></tr>
<tr><td>Linea tremolante</td><td>Mano non appoggiata, pennello spinto</td><td>Mignolo appoggiato, pennello trascinato</td></tr>
<tr><td>Disegno da stamping incompleto</td><td>Smalto già secco, troppa poca pressione</td><td>Lavora più veloce; prova la pressione</td></tr>
<tr><td>Gobba sull'incapsulato</td><td>Decorazione spessa, apex sotto la decorazione</td><td>Decorazioni piatte, apex sopra</td></tr>
<tr><td>Decorazione che si stacca</td><td>Bordi non coperti</td><td>Copri tutto e sigilla il bordo libero</td></tr>
</table>
`,
          sources: ['https://www.nailpro.com/technique/article/21157379/howto-master-nail-stamping',
            'https://www.scratchmagazine.co.uk/nail_art/cat-eye-chrome-nail-art-tutorial/']
        }
      ]
    },
    /* ------------------------------------------------------------------ 10 */
    {
      id: 'manutenzione', summary: ["L'unghia cresce circa 3–3,5 mm al mese: refill ogni 3–4 settimane per le ricostruzioni (semipermanente 2–3).", "Prima valuta: sollevamenti, crepe, macchie verdi o dolore cambiano il piano.", "Elimina tutte le parti sollevate e assottiglia il vecchio prodotto (circa 30–50%) prima di riempire.", "Riparazioni: la crepa si lima finché sparisce; niente colla né cerotti.", "Soak-off: assottiglia, acetone e stagnola, 10–15 min (acrilico 20–30), senza fare leva.", "Hard gel: si rimuove limando, lasciando un velo sulla lamina. Il danno vero è raschiare o strappare, non l'acetone."], n: 10, level: 'inter', title: 'Refill e rimozione',
      desc: 'Refill e riequilibrio della struttura, riparazioni tra un appuntamento e l\'altro, rimozione senza danni.',
      lessons: [
        {
          id: 'refill', videos: [{"id": "A3-Xnv5PTSs", "title": "Refill: tutorial e tutto quello che c'è da sapere", "channel": "Babina_90_Nails", "lang": "IT"}, {"id": "Be30VBjQ254", "title": "Tutorial completo refill unghie in gel", "channel": "Nailfor Professional", "lang": "IT"}], simple: "Dopo qualche settimana l'unghia è cresciuta e la ricostruzione si è spostata in avanti: il refill toglie il vecchio dove serve, copre la ricrescita e rimette l'apex al suo posto.", title: 'Il refill (riempimento)', min: 15,
          html: `
<p>Il <strong>refill</strong> (o riempimento, in inglese <em>infill</em> o <em>rebalance</em>) non è "aggiungere gel nel buco alla base". È un vero <strong>riequilibrio</strong> della struttura: si accorcia, si assottiglia il vecchio prodotto, si prepara la ricrescita e si ricostruisce l'apex nel punto giusto.</p>
${F('refill.svg', 'Profilo prima, durante e dopo la ricrescita.')}
<h2>Perché serve: l'unghia cresce e l'apex "scappa"</h2>
<p>L'unghia della mano cresce di circa <strong>3–3,5 mm al mese</strong> (in uno studio su giovani adulti sani la media era 3,47 mm): poco meno di <strong>1 mm a settimana</strong>. La ricostruzione cresce insieme all'unghia, quindi l'apex si sposta verso la punta.</p>
<table>
<tr><th>Settimane dopo il servizio</th><th>Ricrescita indicativa</th><th>Cosa succede</th></tr>
<tr><td>1</td><td>circa 0,8 mm</td><td>Quasi invisibile</td></tr>
<tr><td>2</td><td>circa 1,6 mm</td><td>Si vede la ricrescita alla base</td></tr>
<tr><td>3</td><td>circa 2,4 mm</td><td>L'apex non è più sopra il punto di stress: la "leva" è più lunga</td></tr>
<tr><td>4</td><td>circa 3,2 mm</td><td>Più rischio di rotture e sollevamenti</td></tr>
</table>
<p class="muted"><small>Valori medi: la crescita varia con età, stagione, dito (il mignolo cresce più lento) e salute.</small></p>
<h2>Ogni quanto?</h2>
<ul>
<li><strong>Ricostruzioni in gel o acrilico</strong>: in genere ogni <strong>3–4 settimane</strong>; molte fonti consigliano di non superare le 3.</li>
<li><strong>Semipermanente</strong>: di solito si rifà ogni <strong>2–3 settimane</strong>.</li>
<li><strong>Unghie che crescono veloci, onicofagia, clienti nuove</strong>: anche ogni <strong>2 settimane</strong>.</li>
</ul>
<h2>Prima di tutto: la valutazione</h2>
${F('refill-valutazione.svg', 'Prima del refill: controlla ricrescita, sollevamenti, crepe e macchie, poi decidi.')}
<ol class="steps">
<li>Lava e disinfetta le mani (tue e della cliente).</li>
<li>Guarda ogni unghia <strong>dall'alto, di profilo e da sotto</strong> il bordo libero.</li>
<li>Cerca: <strong>sollevamenti</strong> (dove?), <strong>crepe</strong>, <strong>macchie</strong> verdi, gialle o scure sotto il prodotto, <strong>dolore</strong> o arrossamento.</li>
<li>Chiedi alla cliente come sono andate le settimane: botte, unghie usate come attrezzi, lavori in acqua.</li>
<li>Decidi: <strong>refill semplice</strong>, <strong>refill con riparazioni</strong> o <strong>rimozione completa</strong>.</li>
</ol>
${B('danger', 'Quando NON fare il refill', 'Macchia verde sotto il prodotto, pus, gonfiore, dolore o distacco dell\'unghia dal letto: non si copre nulla. Si rimuove il prodotto (se possibile senza traumi) e si consiglia il medico.')}
<h2>Il refill passo passo</h2>
${F('refill-step.svg', 'Il refill visto dall\'alto, passo passo.')}
<ol class="steps">
<li><strong>Togli il colore</strong> se c'è (lima 100/180 o fresa a velocità media), senza arrivare al builder.</li>
<li><strong>Accorcia</strong> la lunghezza e ridai la forma. <em>Perché</em>: meno lunghezza = meno leva sul punto di stress durante il lavoro.</li>
<li><strong>Elimina tutti i sollevamenti</strong> limando fino al punto in cui il prodotto è <strong>ben attaccato</strong>. Mai tagliarli con la tronchesina. <em>Perché</em>: tagliare o strappare porta via strati di lamina e crea nuovi sollevamenti.</li>
<li><strong>Assottiglia il vecchio prodotto</strong> seguendo il profilo dell'unghia: indicativamente del <strong>30–50%</strong>, in base a quanto è cresciuta l'unghia e a dove si è spostato l'apex.</li>
<li><strong>Raccorda il gradino</strong> alla base: il vecchio prodotto deve "sfumare" verso la ricrescita, senza scalino. Non limare l'unghia naturale.</li>
<li><strong>Prepara la ricrescita</strong> come un'unghia naturale: cuticola, opacizzazione leggera, rimozione della polvere, disidratante, primer <strong>solo sulla parte naturale</strong>.</li>
<li><strong>Applica</strong> uno strato sottile di aderenza (se previsto dal sistema) e polimerizza.</li>
<li><strong>Ricostruisci</strong>: zona 3 sottile con un margine di circa 1 mm dalla pelle, <strong>apex in zona 2</strong> sopra il punto di stress, zona 1 sottile. Controlla di profilo prima della lampada.</li>
<li>Polimerizza, rifinisci con lima 180/240, top coat, olio per cuticole.</li>
<li><strong>Annota</strong> sulla scheda cosa hai trovato (sollevamenti, rotture) e fissa il prossimo refill.</li>
</ol>
${F('refill-assottigliare.svg', 'Di profilo: apex spostato dopo 3 settimane, prodotto assottigliato, nuovo apex sopra il punto di stress.')}
${F('refill-gradino.svg', 'Raccordo alla base: il gradino crea una gobba, il raccordo liscio no. Sempre con il margine dalla pelle.')}
${B('danger', 'Mai coprire un sollevamento', 'Sotto un sollevamento possono esserci umidità, sporco e batteri. Coprirlo li chiude dentro: è così che nascono infezioni e macchie verdi. Il sollevamento si elimina tutto.')}
<h2>Errori frequenti</h2>
<table>
<tr><th>Errore</th><th>Conseguenza</th><th>Cosa fare invece</th></tr>
<tr><td>Aggiungere prodotto senza assottigliare</td><td>Unghia sempre più spessa e pesante</td><td>Assottiglia il vecchio prima di ricostruire</td></tr>
<tr><td>Lasciare un gradino alla base</td><td>Si aggancia, solleva, si vede</td><td>Raccorda il vecchio alla ricrescita</td></tr>
<tr><td>Primer sul vecchio prodotto</td><td>Spreco e possibile contatto con la pelle</td><td>Primer solo sulla ricrescita naturale</td></tr>
<tr><td>Apex lasciato dov'era</td><td>Rotture in zona di stress</td><td>Rifai l'apex sopra il punto di stress</td></tr>
<tr><td>Saltare la valutazione</td><td>Si coprono problemi e infezioni</td><td>Guarda sempre dall'alto, di profilo e da sotto</td></tr>
</table>
${B('tip', 'Backfill (french)', 'Nel pink &amp; white, quando la smile line si è spostata in avanti, si fa un "backfill": si toglie il vecchio bianco e si rifà la smile nella posizione giusta. Richiede più tempo di un refill normale.')}
`,
          sources: ['https://www.opi.com/professionals/how-to-rebalance-and-fill-opi-gelevate-overlay-services',
            'https://katiebarnesacademy.com/blogs/nail-structure-application/how-to-deal-with-nail-service-breakdown',
            'https://nailknowledge.org/?p=49737',
            'https://bionumbers.hms.harvard.edu/bionumber.aspx?id=112380',
            'https://dilei.it/bellezza/cose-e-quanto-costa-il-refill-delle-unghie-in-gel/637264/',
            'https://booksolo.co/nailedbyalire/aftercare']
        },
        {
          id: 'riparazione', simple: "Se un'unghia si crepa o si stacca prima del refill, la cliente non deve incollarla né coprirla con un cerotto: va sistemata in salone, togliendo la parte rovinata e ricostruendo.", title: 'Riparare un\'unghia tra un appuntamento e l\'altro', min: 9,
          html: `
<p>Capita: una botta, una porta, un barattolo. La cliente torna con un'unghia crepata, rotta o sollevata. La <strong>riparazione</strong> è un piccolo refill su una sola unghia, ma prima va capito <strong>cosa</strong> si è rotto.</p>
${F('riparazione-decisione.svg', 'Cosa si è rotto? Prodotto, unghia naturale o letto ungueale.')}
<h2>Prima domanda: cosa si è rotto?</h2>
<table>
<tr><th>Situazione</th><th>Cosa fare</th></tr>
<tr><td>Crepa solo nel <strong>prodotto</strong>, l'unghia sotto è sana</td><td>Riparazione in salone</td></tr>
<tr><td><strong>Sollevamento</strong> di una parte del prodotto</td><td>Elimina tutto il sollevamento, poi ricostruisci</td></tr>
<tr><td>Unghia naturale <strong>rotta oltre il bordo libero</strong>, letto intatto</td><td>Rimuovi il prodotto rotto, ricostruisci (eventualmente su cartina) a lunghezza ridotta</td></tr>
<tr><td>Rottura <strong>dentro il letto</strong>, sangue, dolore, unghia staccata dal letto</td><td><strong>Non coprire</strong>: pulisci, proteggi e consiglia il medico</td></tr>
</table>
<h2>Riparare una crepa nel prodotto</h2>
${F('riparazione-crepa.svg', 'Riparazione di una crepa: lima finché sparisce, ricostruisci con l\'apex, rifinisci e annota.')}
<ol class="steps">
<li>Accorcia l'unghia se serve: meno leva sulla zona rotta.</li>
<li>Lima la crepa <strong>fino a farla sparire del tutto</strong> (anche la linea sottile). <em>Perché</em>: una crepa coperta continua ad allargarsi sotto il prodotto nuovo.</li>
<li>Assottiglia e raccorda il prodotto intorno.</li>
<li>Se è esposta unghia naturale, preparala (polvere via, disidratante, primer solo sulla lamina).</li>
<li>Ricostruisci con builder e rifai l'<strong>apex</strong> sopra il punto di stress.</li>
<li>Polimerizza, rifinisci, top, olio.</li>
<li>Chiedi come è successo e <strong>annota</strong> sulla scheda: se si rompe sempre lo stesso dito, controlla struttura e abitudini.</li>
</ol>
${B('danger', 'Colla e cerotti: no', 'Spiega alla cliente di non incollare l\'unghia sollevata e di non coprirla con un cerotto: entrambi chiudono umidità e batteri sotto il prodotto. Meglio limare via la parte che si aggancia e prenotare la riparazione.')}
${B('tip', 'Rotture ripetute', 'Se la stessa cliente rompe spesso le unghie, prima di cambiare prodotto controlla: lunghezza adatta alle sue abitudini, apex nel posto giusto, zona 2 non troppo sottile. Poi rivedi la tua tecnica con le foto di profilo.')}
`,
          sources: ['https://katiebarnesacademy.com/blogs/nail-structure-application/how-to-deal-with-nail-service-breakdown',
            'https://nailknowledge.org/?p=49737']
        },
        {
          id: 'rimozione', videos: [{"id": "60O2H65aZfA", "title": "Rimozione sicura del gel in 7 step", "channel": "Nail Couture Italia", "lang": "IT"}, {"id": "k4gk4ZWEvB0", "title": "Come togliere il semipermanente con acetone", "channel": "Semilac Italia", "lang": "IT"}], simple: "Per togliere gel e acrilico si assottiglia, si ammorbidisce con l'acetone e si spinge via con delicatezza. Non si raschia e non si strappa mai: è questo che rovina l'unghia.", title: 'La rimozione', min: 14,
          html: `
<p>Una rimozione fatta bene lascia l'unghia naturale <strong>intatta</strong>. Una fatta male (strappare, fare leva, raschiare) porta via strati di lamina: l'unghia diventa sottile, dolente e piena di sollevamenti al servizio successivo.</p>
${B('info', 'L\'acetone non è il nemico', 'L\'acetone usato correttamente asciuga solo la superficie della lamina: l\'aspetto biancastro dopo la rimozione è temporaneo e si recupera in alcune ore. Il danno vero viene dal raschiare e dal forzare il prodotto non ancora ammorbidito.')}
<h2>Quale metodo per quale prodotto</h2>
${F('rimozione-decisione.svg', 'Quale prodotto? Soak-off, file-off o scheda tecnica.')}
<table>
<tr><th>Prodotto</th><th>Metodo</th><th>Tempo indicativo in acetone</th></tr>
<tr><td>Semipermanente (gel polish)</td><td>Soak-off</td><td>circa 10–15 min (alcuni remover dedicati dichiarano 5–10 min)</td></tr>
<tr><td>Soft gel / builder "soak-off" (BIAB e simili)</td><td>Assottiglia molto, poi soak-off</td><td>10–15 min, fino a circa 30 per spessori alti</td></tr>
<tr><td>Acrilico</td><td>Assottiglia molto, poi soak-off</td><td>in genere 20–30 min</td></tr>
<tr><td>Polygel</td><td>Dipende dal marchio: spesso file-off o soak-off lento</td><td>Leggi la scheda tecnica</td></tr>
<tr><td>Hard gel</td><td>File-off (non si scioglie in acetone)</td><td>—</td></tr>
</table>
<p class="muted"><small>I tempi variano con prodotto, spessore e temperatura: segui sempre le istruzioni del produttore.</small></p>
<h2>Soak-off passo passo</h2>
${F('rimozione-soakoff-step.svg', 'Soak-off in sei passaggi.')}
<ol class="steps">
<li><strong>Igiene</strong> delle mani; indossa i DPI (guanti in nitrile, mascherina se limi).</li>
<li><strong>Togli il top e assottiglia</strong> il prodotto con lima 100/180 o fresa, senza arrivare alla lamina. <em>Perché</em>: il top sigillante blocca l'acetone; meno spessore = meno tempo di posa.</li>
<li><strong>Proteggi la pelle</strong> intorno con olio o crema barriera. <em>Perché</em>: l'acetone secca e irrita la pelle.</li>
<li>Appoggia un <strong>cotone imbevuto di acetone</strong> e avvolgi con la <strong>stagnola</strong> (o clip/cappucci). Il tempo parte quando tutte le dita della mano sono avvolte.</li>
<li><strong>Controlla un dito</strong> allo scadere del tempo: il prodotto deve essere morbido e "gonfio".</li>
<li><strong>Spingi via</strong> il prodotto con un bastoncino d'arancio o uno spingi-cuticole non tagliente, dalla cuticola verso la punta, <strong>senza premere sulla lamina</strong>.</li>
<li>Se resiste, <strong>riavvolgi</strong> per altri 5–10 minuti. Non forzare.</li>
<li>Togli i residui con un <strong>buffer morbido</strong>, lava le mani, applica <strong>olio</strong> per cuticole.</li>
</ol>
${F('rimozione.svg', 'Rimozione soak-off.')}
${B('warn', 'Acetone: sicurezza', 'L\'acetone è molto infiammabile: usane poco, in un contenitore chiuso, lontano da fiamme e fonti di calore, con la stanza ben ventilata. Non scaldarlo mai. Non usarlo su pelle ferita o irritata.')}
<h2>File-off (hard gel e prodotti che non si sciolgono)</h2>
<ol class="steps">
<li>Togli il colore e il top con lima o fresa (punta per la rimozione, velocità media, sempre in movimento).</li>
<li>Riduci il prodotto <strong>a strati</strong>, controllando spesso con la luce: quando si vede la sfumatura rosa della lamina sotto, rallenta.</li>
<li>Lascia un <strong>velo sottile</strong> di prodotto sulla lamina. <em>Perché</em>: la lamina naturale è spessa pochi decimi di millimetro; arrivarci con la fresa la assottiglia e la scalda.</li>
<li>Da qui puoi rifare il servizio sopra il velo, oppure lasciare che il velo cresca via.</li>
</ol>
${F('rimozione-errori.svg', 'Cosa non fare: leva, raschietto in metallo, strappo. Corretto: ammorbidire e spingere.')}
<h2>Errori frequenti</h2>
<table>
<tr><th>Errore</th><th>Perché è dannoso</th><th>Invece</th></tr>
<tr><td>Fare leva con lo spingi-cuticole</td><td>Strappa strati di lamina</td><td>Riavvolgi e aspetta</td></tr>
<tr><td>Raschiare con il metallo</td><td>Graffi e solchi: la lamina diventa bianca e ruvida</td><td>Bastoncino d'arancio, buffer morbido</td></tr>
<tr><td>Non assottigliare prima</td><td>Tempi lunghissimi, più acetone sulla pelle</td><td>Togli il top e la massa</td></tr>
<tr><td>Fresa sulla lamina</td><td>Assottiglia, scalda, rende sensibile al calore</td><td>Fermati al velo</td></tr>
<tr><td>Lasciar staccare il prodotto alla cliente</td><td>Strappo della lamina</td><td>Spiega che la rimozione va fatta in salone</td></tr>
</table>
<h2>Dopo la rimozione</h2>
<ul>
<li>Guarda la lamina: se è sottile, dolente o con macchie, valuta una <strong>pausa</strong> o un servizio leggero, e annotalo.</li>
<li>Consiglia olio per cuticole ogni giorno per qualche settimana.</li>
<li>Se ci sono segni di infezione o distacco dal letto, consiglia il medico.</li>
</ul>
`,
          sources: ['https://nailknowledge.org/blog/does-acetone-affect-the-natural-nail',
            'https://karanailedit.substack.com/p/how-to-remove-your-gel-safely',
            'https://onglesdor.com/en/shellac-remover-wraps-10-unit.html',
            'https://nailknowledge.org/?p=49737',
            'https://www.marionnaud.it/m-life/tutorial/come-togliere-unghie-gel']
        }
      ]
    },
    /* ------------------------------------------------------------------ 11 */
    {
      id: 'problemi', summary: ["Il punto in cui il prodotto si stacca indica la causa: base = preparazione o pelle; lati = solchi; punta = sigillatura; centro = adesione o trauma.", "Margine dalla pelle: circa 1 mm (le fonti indicano 0,5–1,5 mm), mai prodotto sulla pelle.", "Rotture: apex assente o spostato, zona 2 sottile, lunghezza eccessiva.", "Picco di calore: strati spessi, lamina assottigliata, lampada non abbinata → strati sottili e flash and pull.", "Grinze = strato spesso, superficie dura sopra e liquido sotto; i pigmenti fanno ombra.", "Sotto-polimerizzato = rischio allergia. Diagnosi: dove, quante dita, quando, cosa ho fatto, cosa ha fatto la cliente."], n: 11, level: 'avanz', title: 'Problemi e soluzioni',
      desc: 'Sollevamenti, rotture, picchi di calore, bolle, grinze, ingiallimento e un metodo per risalire alla causa.',
      lessons: [
        {
          id: 'lifting', simple: "Se il prodotto si stacca, guarda DOVE si stacca: ti dice quasi sempre il perché. Nella maggior parte dei casi la causa è la preparazione o il prodotto che ha toccato la pelle.", title: 'Il sollevamento (lifting)', min: 14,
          html: `
<p>Il <strong>sollevamento</strong> (lifting) è la perdita di adesione tra prodotto e unghia naturale: si forma uno spazio dove entrano aria, acqua e sporco. È il problema più frequente e, quasi sempre, è <strong>evitabile</strong>.</p>
${F('lifting.svg', 'Dove nasce il sollevamento e perché.')}
<h2>Leggi il sollevamento: dove si stacca?</h2>
${F('lifting-mappa.svg', 'Mappa del sollevamento: il punto in cui si stacca suggerisce la causa.')}
<table>
<tr><th>Dove</th><th>Cause più probabili</th><th>Cosa cambiare</th></tr>
<tr><td><strong>Alla base</strong> (cuticola)</td><td>Cuticola (pellicina) rimasta sulla lamina; prodotto sulla pelle o troppo spesso alla base; olio o creme non rimossi; pelle molto secca</td><td>Preparazione più accurata; margine dalla pelle; zona 3 sottile; olio quotidiano alla cliente</td></tr>
<tr><td><strong>Sui lati</strong> (solchi laterali)</td><td>Prodotto finito nei solchi; limatura aggressiva sui lati; tip della misura sbagliata</td><td>Margine anche sui lati; lima parallela al solco; tip della misura giusta</td></tr>
<tr><td><strong>In punta</strong> (bordo libero)</td><td>Bordo libero non sigillato; polvere non tolta; sigillatura limata via in rifinitura; lunghezza eccessiva</td><td>Sigilla a ogni strato; togli la polvere; adegua la lunghezza</td></tr>
<tr><td><strong>Al centro</strong> ("a tasca", <em>pocket lifting</em>)</td><td>Adesione scarsa; rapporto liquido/polvere sbagliato; botta o pressione</td><td>Rivedi preparazione e perla; chiedi alla cliente di eventuali traumi</td></tr>
<tr><td><strong>Su tutte le dita</strong></td><td>Tecnica, prodotto o lampada</td><td>Rivedi l'intero protocollo, sistema dello stesso marchio, tempi di polimerizzazione</td></tr>
<tr><td><strong>Su 1–2 dita</strong></td><td>Abitudini (pollice, indice) o struttura di quelle unghie</td><td>Chiedi delle abitudini; rinforza la struttura</td></tr>
</table>
${B('info', 'Cuticola e pterigio non sono la stessa cosa', 'La cuticola è la pellicina morta che si stacca dalla lamina durante la preparazione. Il pterigio è un\'alterazione: la pelle cresce e aderisce sulla lamina. Il pterigio non si rimuove: si indirizza la cliente al medico.')}
<h2>Il margine dalla pelle</h2>
${F('lifting-margine.svg', 'Margine corretto: circa 1 mm di unghia libera tra prodotto e pelle, anche sui lati.')}
<p>Il prodotto deve fermarsi <strong>un filo prima della pelle</strong>: circa <strong>1 mm</strong> dalla cuticola e dai solchi laterali (le fonti di settore indicano da 0,5 a 1,5 mm). <em>Perché</em>: il prodotto che tocca la pelle non aderisce e non polimerizza bene; quando la pelle si muove, crea una "leva" che stacca il bordo. In più aumenta il rischio di allergia.</p>
<h2>Le cause, in cinque gruppi</h2>
<table>
<tr><th>Gruppo</th><th>Esempi</th></tr>
<tr><td><strong>Preparazione</strong></td><td>Cuticola rimasta sulla lamina, oli, polvere, lamina toccata dopo il disidratante</td></tr>
<tr><td><strong>Applicazione</strong></td><td>Prodotto sulla pelle, strati spessi alla base, bordo libero non sigillato, cartina/tip montati male</td></tr>
<tr><td><strong>Prodotto e lampada</strong></td><td>Troppo o troppo poco primer, sistemi di marchi diversi mescolati, lampada non abbinata, polimerizzazione incompleta</td></tr>
<tr><td><strong>Struttura</strong></td><td>Apex nel posto sbagliato, lunghezza eccessiva, refill in ritardo</td></tr>
<tr><td><strong>Cliente</strong></td><td>Mani spesso in acqua, sudorazione, unghie usate come attrezzi, unghie mangiate o "pizzicate"</td></tr>
</table>
<h2>Cosa fare quando la cliente torna con un sollevamento</h2>
<ol class="steps">
<li>Guarda <strong>dove</strong> si stacca e su <strong>quante</strong> dita (tabella sopra).</li>
<li>Controlla che sotto non ci siano <strong>macchie verdi</strong>, umidità, dolore: in quel caso non si copre e si consiglia il medico.</li>
<li><strong>Lima via tutto il sollevamento</strong> fino al prodotto ben attaccato. Mai tagliarlo con la tronchesina.</li>
<li>Prepara di nuovo la zona scoperta come un'unghia naturale.</li>
<li>Ricostruisci, rispettando il margine e sigillando il bordo libero.</li>
<li>Annota sulla scheda <strong>dove</strong> era il sollevamento: se si ripete nello stesso punto, la causa è nel tuo protocollo.</li>
</ol>
${B('danger', 'Mai coprire un sollevamento', 'Sotto il sollevamento restano acqua e batteri: coprirlo può portare a infezioni. Va eliminato tutto.')}
${B('tip', 'Prima di dare la colpa al prodotto', 'Se il problema capita a una o due clienti, chiedi delle abitudini. Se capita a molte, rivedi la tua preparazione e fotografa i lavori di profilo.')}
`,
          sources: ['https://nailknowledge.org/?p=49737',
            'https://katiebarnesacademy.com/blogs/nail-structure-application/how-to-deal-with-nail-service-breakdown',
            'https://www.design4nails.co.uk/?p=285413',
            'https://semilac.co.uk/blogs/news/gel-lifting-and-yellowing-root-causes-and-salon-floor-fixes',
            'https://purespadirect.com/blogs/pure-spa-direct-blog/gel-polish-lifting-troubleshooting-20-causes-prep-lamps-products-and-client-habits-a-nail-tech-39-s-guide-to-perfect-manicures']
        },
        {
          id: 'calore-rotture', simple: "Le unghie si rompono quasi sempre dove manca la struttura. Il gel, indurendo, scalda: strati sottili, lamina non assottigliata e mano fuori dalla lampada qualche secondo evitano il bruciore.", title: 'Rotture e picchi di calore', min: 13,
          html: `
<h2>Rotture e crepe: dove si rompe?</h2>
${F('rotture-mappa.svg', 'Dove si rompe l\'unghia e perché: zona di stress, angoli laterali, punta.')}
<table>
<tr><th>Dove</th><th>Causa più probabile</th><th>Soluzione</th></tr>
<tr><td><strong>Zona di stress</strong> (dove il bordo libero lascia il dito)</td><td>Apex assente, troppo basso o spostato verso la punta; zona 2 troppo sottile</td><td>Apex sopra il punto di stress; spessore corretto in zona 2</td></tr>
<tr><td><strong>Angoli laterali</strong></td><td>Lati troppo sottili; forma molto stretta; lunghezza</td><td>Lati paralleli e non troppo sottili; lunghezza adatta</td></tr>
<tr><td><strong>Punta</strong> (scheggiature)</td><td>Bordo libero non sigillato; trauma; punta troppo sottile per la lunghezza</td><td>Sigilla il bordo; spessore proporzionato</td></tr>
<tr><td><strong>Crepa alla base</strong></td><td>Prodotto troppo spesso o rigido alla cuticola; lamina molto flessibile</td><td>Zona 3 sottile; sistema adatto all'unghia</td></tr>
<tr><td><strong>Sempre lo stesso dito</strong></td><td>Abitudini della cliente</td><td>Accorcia quel dito; chiedi come lo usa</td></tr>
</table>
${F('apex-confronto.svg', 'Apex corretto ed errato a confronto.')}
${B('tip', 'Lunghezza e abitudini', 'Più l\'unghia è lunga, più forza arriva sul punto di stress. Per chi usa molto le mani, una lunghezza corta e una forma squoval o tonda durano di più.')}
<h2>Picco di calore (heat spike)</h2>
<p>La polimerizzazione è una reazione <strong>esotermica</strong>: ogni legame che si forma libera un pochino di calore. Su un'unghia si formano milioni di legami in pochi secondi, e il calore si somma. Il letto ungueale comincia a sentire dolore già intorno ai <strong>46 °C</strong>.</p>
${F('picco-calore-cause.svg', 'Perché scotta: strato spesso, lamina assottigliata, lampada troppo veloce o gel non abbinato.')}
<h2>Le cause</h2>
<ul>
<li><strong>Strati spessi</strong>: più prodotto = più calore. Per questo il pollice, più grande, spesso scotta di più.</li>
<li><strong>Lamina assottigliata</strong> dalla limatura: isola meno. La limatura aggressiva può anche "bruciare" per attrito il letto, che diventa più sensibile.</li>
<li><strong>Lampada non abbinata</strong>: un gel pensato per una lampada più lenta, sotto una lampada LED molto veloce, libera lo stesso calore in molto meno tempo.</li>
<li><strong>Acrilico</strong>: polvere e liquido non abbinati; prodotti a presa rapida in un ambiente caldo.</li>
<li><strong>Formulazioni</strong> poco testate.</li>
</ul>
<h2>Le soluzioni</h2>
<ol class="steps">
<li><strong>Strati sottili</strong>, soprattutto con builder e colori scuri.</li>
<li><strong>Non assottigliare la lamina</strong>: opacizzare non vuol dire limare.</li>
<li>Usa la <strong>lampada consigliata</strong> dal produttore del gel; se c'è, usa la modalità <em>low heat</em>.</li>
<li>Usa la tecnica <strong>flash and pull</strong>: appena la cliente sente caldo, toglie la mano per qualche secondo e poi la rimette, finché il tempo totale è completato.</li>
<li>Avvisa la cliente <strong>prima</strong>: "Se senti caldo, togli pure la mano". Non chiederle di resistere.</li>
</ol>
${F('lampada-posizione.svg', 'Flash and pull: uscire qualche secondo dalla lampada tiene il calore sotto la soglia di bruciore.')}
${B('danger', 'Unghia "bruciata"', 'Picchi di calore ripetuti e limatura eccessiva possono danneggiare il letto ungueale (onicolisi, cioè distacco dell\'unghia dal letto, e infezioni). Se la cliente ha dolore persistente, fermati, rimuovi il prodotto e consiglia il medico.')}
`,
          sources: ['https://nailknowledge.org/?p=44956',
            'https://scratchmagazine.co.uk/feature/heat-spikes-in-gel-nail-services-why-they-happen-how-to-avoid-them',
            'https://www.nsinails.com.au/blogs/news/understand-nail-damages-heat-spikes-lifting-issues',
            'https://nailknowledge.org/blog/uv-curing-why-thin-layers-matter-for-perfect-nails']
        },
        {
          id: 'difetti', simple: "Quasi tutti i difetti di superficie nascono da strati troppo spessi, polimerizzazione incompleta o prodotti e lampade non abbinati. Strati sottili e il sistema giusto risolvono la maggior parte dei problemi.", title: 'Bolle, grinze, ingiallimento', min: 13,
          html: `
${F('problemi.svg', 'Riconosci il difetto.')}
<h2>Perché la luce non arriva in fondo</h2>
<p>La lampada indurisce il gel dall'alto verso il basso. I <strong>pigmenti</strong> (soprattutto colori scuri, bianco e glitter) fanno da <strong>ombrello</strong>: la superficie riceve tanta luce, gli strati sotto poca. Se lo strato è spesso, sopra si forma una "pelle" dura e sotto resta gel liquido. Allungare il tempo in lampada spesso <strong>non basta</strong>: la soluzione è lo strato sottile.</p>
${F('grinze-sezione.svg', 'Grinza in sezione: superficie dura sopra, gel liquido sotto; con strati sottili la luce arriva in fondo.')}
<h2>Tabella dei difetti</h2>
<table>
<tr><th>Difetto</th><th>Come si riconosce</th><th>Cause</th><th>Soluzione</th></tr>
<tr><td><strong>Bolle</strong> (gel)</td><td>Puntini o crateri sulla superficie</td><td>Flacone agitato; gel mescolato con forza; pennello premuto e "sbattuto"; strato troppo spesso</td><td>Ruota il flacone tra le mani, non agitarlo; stendi con calma, in strati sottili</td></tr>
<tr><td><strong>Bolle</strong> (acrilico)</td><td>Bollicine dentro il prodotto</td><td>Perla troppo asciutta o troppo bagnata; perla lavorata troppo; monomero contaminato</td><td>Perla corretta; pochi movimenti; liquido pulito nel dappen</td></tr>
<tr><td><strong>Grinze</strong></td><td>Superficie "a buccia d'arancia" o raggrinzita</td><td>Strato spesso; colore molto pigmentato; lampada non abbinata</td><td>Strati sottili; lampada e tempi del produttore</td></tr>
<tr><td><strong>Ingiallimento</strong></td><td>Tono giallo o bruno</td><td>Lampada non abbinata o vecchia; top non polimerizzato del tutto o non sigillato; pennello o gel contaminati (anche da monomero acrilico); tip economici non stabili alla luce; sole, lettini, nicotina, creme e detersivi sul top</td><td>Sistema dello stesso marchio; top ben polimerizzato e sigillato; attrezzi puliti; guanti alla cliente</td></tr>
<tr><td><strong>Superficie appiccicosa dopo la pulizia</strong></td><td>Resta "colla" anche dopo il cleaner</td><td>Polimerizzazione incompleta</td><td>Controlla lampada, tempi, posizione della mano (pollici a parte)</td></tr>
<tr><td><strong>Sotto/sovra-esposizione</strong></td><td>Morbido e graffiabile / fragile e caldo</td><td>Tempi o lampada non compatibili</td><td>Segui la scheda tecnica; sotto-polimerizzato = rischio allergia</td></tr>
</table>
${F('ingiallimento-cause.svg', 'Le cause più comuni dell\'ingiallimento.')}
${B('tip', 'Ingiallito subito o dopo settimane?', 'Se il giallo compare subito dopo il servizio, cerca la causa nel prodotto o nella lampada. Se compare dopo qualche settimana, chiedi delle abitudini: sole, fumo, creme, prodotti per la casa.')}
<h2>Reazioni allergiche: riconoscerle</h2>
<p>Il contatto ripetuto della pelle con prodotto <strong>non polimerizzato</strong> può causare una <strong>dermatite allergica da contatto</strong>. Segnali tipici: prurito, rossore, gonfiore o vescicole intorno all'unghia o sui polpastrelli; a volte compare anche su viso e palpebre (toccati con le dita).</p>
<ol class="steps">
<li>Interrompi il servizio e non applicare altro prodotto.</li>
<li>Rimuovi il prodotto con delicatezza.</li>
<li>Consiglia alla cliente di rivolgersi al medico (dermatologo) e annotalo sulla scheda.</li>
<li>Rivedi la tua tecnica: prodotto sulla pelle, polimerizzazione incompleta, polvere di limatura non polimerizzata.</li>
</ol>
${B('danger', 'Anche tu sei a rischio', 'L\'operatrice tocca prodotti liquidi ogni giorno: guanti in nitrile, niente contatto con la pelle, salviette e pennelli sporchi chiusi in un contenitore. Un\'allergia agli acrilati è per sempre.')}
`,
          sources: ['https://nailknowledge.org/blog/gel-polish-curing',
            'https://nailknowledge.org/blog/uv-curing-why-thin-layers-matter-for-perfect-nails',
            'https://nailknowledge.org/?p=147555',
            'https://support.pinkgellac.com/hc/en-nl/articles/24253249294098-Why-is-my-gel-polish-wrinkling-or-bubbling-and-how-can-I-prevent-this',
            'https://www.scratchmagazine.co.uk/feature/causes-of-bubbles-in-lp-gel-nail-enhancements',
            'https://katiebarnesacademy.com/blogs/nail-structure-application/how-to-deal-with-nail-service-breakdown']
        },
        {
          id: 'diagnosi', simple: "Quando qualcosa va storto, non cambiare subito prodotto. Fai cinque domande: dove, quante dita, quando, cosa ho fatto, cosa ha fatto la cliente. La risposta è quasi sempre lì.", title: 'Metodo di diagnosi: dal difetto alla causa', min: 8,
          html: `
<p>Un difetto è un <strong>indizio</strong>. Le professioniste esperte non indovinano: seguono sempre lo stesso ragionamento, annotano e correggono una cosa alla volta.</p>
${F('diagnosi-flusso.svg', 'Le cinque domande della diagnosi.')}
<h2>Le cinque domande</h2>
<ol class="steps">
<li><strong>Dove?</strong> Base, lati, punta, centro, superficie. Ogni zona ha cause tipiche (vedi la mappa del sollevamento e quella delle rotture).</li>
<li><strong>Quante dita?</strong> Tutte = tecnica, prodotto o lampada. Una o due = abitudini o struttura di quelle unghie.</li>
<li><strong>Quando?</strong> Subito o nei primi 2–3 giorni = preparazione, applicazione, polimerizzazione. Dopo 2–3 settimane = crescita, struttura, usura, abitudini.</li>
<li><strong>Cosa ho fatto?</strong> Rileggi la scheda: prodotti, lotti, tempi, lampada, eventuali novità nel tuo protocollo.</li>
<li><strong>Cosa ha fatto la cliente?</strong> Lavori, acqua, sport, botte, farmaci nuovi, gravidanza, unghie mangiate o "pizzicate".</li>
</ol>
<h2>Esempi guidati</h2>
<table>
<tr><th>Situazione</th><th>Ragionamento</th><th>Probabile causa</th></tr>
<tr><td>Sollevamento alla base su tutte le dita dopo 3 giorni</td><td>Tutte + subito + base</td><td>Preparazione (cuticola rimasta sulla lamina) o prodotto sulla pelle</td></tr>
<tr><td>Rottura del pollice destro dopo 2 settimane</td><td>Un dito + tardi + zona di stress</td><td>Abitudini o apex del pollice</td></tr>
<tr><td>Ingiallimento su tutte le dita dopo il primo giorno</td><td>Tutte + subito + superficie</td><td>Lampada, top o contaminazione</td></tr>
<tr><td>Scheggiature in punta su 2–3 dita</td><td>Poche + punta</td><td>Bordo libero non sigillato su quelle dita, o tastiera e attrezzi</td></tr>
</table>
${F('diagnosi-scheda.svg', 'Una riga di scheda per ogni difetto: data, dito, dove, quando, causa probabile, correzione.')}
${B('tip', 'Una correzione alla volta', 'Se cambi tre cose insieme non saprai mai quale ha funzionato. Cambia una cosa, annota, guarda il risultato al refill successivo.')}
${B('info', 'Le foto sono il tuo archivio', 'Fotografa ogni lavoro dall\'alto e di profilo, alla fine del servizio e al refill. Confrontando le foto vedi dove si è spostato l\'apex e dove nascono i problemi.')}
`,
          sources: ['https://katiebarnesacademy.com/blogs/nail-structure-application/how-to-deal-with-nail-service-breakdown',
            'https://nailknowledge.org/?p=49737']
        }
      ]
    },
    /* ------------------------------------------------------------------ 12 */
    {
      id: 'professione', summary: ["Consulenza prima di ogni nuovo servizio: salute, allergie, abitudini, aspettative.", "Scheda cliente = dati sulla salute: informativa, consenso esplicito e conservazione sicura.", "Foto per i social solo con un consenso separato e specifico.", "Consigli post-trattamento scritti e data del refill.", "Prezzo = materiali + tempo + spese fisse + margine; i prezzi di mercato sono molto variabili.", "In Italia: qualifica di estetista, partita IVA, INPS artigiani, SCIA al SUAP; RC fortemente consigliata."], n: 12, level: 'avanz', title: 'Professione e business',
      desc: 'Consulenza e privacy, consigli post-trattamento, foto dei lavori, prezzi e agenda, apertura dell\'attività.',
      lessons: [
        {
          id: 'consulenza', simple: "Prima di lavorare si parla con la cliente: salute, allergie, abitudini e cosa desidera. Tutto va scritto in una scheda, che è un documento con dati sulla salute: va custodita con cura.", title: 'Consulenza e scheda cliente', min: 13,
          html: `
<p>Ogni <strong>nuova cliente</strong> e ogni <strong>nuovo servizio</strong> iniziano con una consulenza. Serve a tre cose: capire se si può lavorare in sicurezza, scegliere il sistema giusto e mettersi d'accordo su risultato, tempi e prezzo.</p>
${F('consulenza-flusso.svg', 'La consulenza in cinque fasi.')}
<h2>La consulenza in cinque fasi</h2>
<ol class="steps">
<li><strong>Accoglienza e informativa</strong>: spiega perché raccogli i dati e come li custodisci; consegna l'informativa privacy e fai firmare i consensi.</li>
<li><strong>Domande sulla salute</strong>: allergie (acrilati, lattice, cerotti), farmaci, diabete, problemi di circolazione, chemioterapia, gravidanza, malattie della pelle o delle unghie, reazioni a servizi precedenti.</li>
<li><strong>Osservazione</strong>: mani lavate, guarda unghie e pelle con buona luce. Cerca controindicazioni (micosi, infezioni, ferite, distacco dal letto). Se ci sono, <strong>non lavorare</strong> e consiglia il medico.</li>
<li><strong>Abitudini e desideri</strong>: lavoro, sport, mani in acqua, onicofagia; forma, lunghezza e colore desiderati. Proponi un sistema e una lunghezza <strong>adatti alla vita della cliente</strong>, spiegando il perché.</li>
<li><strong>Accordo</strong>: servizio, durata, prezzo, data del refill, consigli post-trattamento. Annota tutto.</li>
</ol>
${F('scheda-cliente.svg', 'Esempio di scheda cliente.')}
<h2>Cosa scrivere nella scheda</h2>
<table>
<tr><th>Sezione</th><th>Contenuto</th><th>Perché</th></tr>
<tr><td>Dati di contatto</td><td>Nome, telefono, email</td><td>Appuntamenti e richiami</td></tr>
<tr><td>Salute</td><td>Allergie, farmaci, condizioni rilevanti</td><td>Sicurezza; scelta dei prodotti</td></tr>
<tr><td>Valutazione</td><td>Stato della lamina e della pelle, forma del letto</td><td>Confronto nel tempo</td></tr>
<tr><td>Servizio</td><td>Data, sistema, prodotti e <strong>lotti</strong>, colori, lampada, tempi</td><td>Ripetere il risultato; risalire alla causa di un problema o di una reazione</td></tr>
<tr><td>Note</td><td>Sollevamenti, rotture, reazioni, consigli dati, servizi rifiutati e motivo</td><td>Diagnosi e tutela professionale</td></tr>
<tr><td>Consensi</td><td>Firme e date</td><td>Prova di ciò che la cliente ha accettato</td></tr>
</table>
<h2>Privacy: la scheda contiene dati sulla salute</h2>
<p>Allergie, farmaci, gravidanza o patologie sono <strong>dati relativi alla salute</strong>: per il Regolamento europeo (GDPR, art. 9) sono "categorie particolari" e si possono trattare solo in casi precisi, tra cui il <strong>consenso esplicito</strong> della persona.</p>
${F('consensi-separati.svg', 'Informativa e consensi separati: tre fogli, tre firme.')}
<ul>
<li><strong>Informativa</strong> (art. 13 GDPR): chi tratta i dati, perché, per quanto tempo, chi li vede, come esercitare i diritti.</li>
<li><strong>Consenso esplicito</strong> per i dati sulla salute, scritto e firmato.</li>
<li><strong>Consenso separato per le foto</strong> e per la pubblicazione sui social: fotografare non è necessario per fare le unghie, quindi la cliente deve poter dire no senza perdere il servizio.</li>
<li><strong>Conservazione</strong>: schede cartacee in un armadio chiuso; file digitali protetti da password. Conserva i dati solo per il tempo indicato nell'informativa.</li>
<li><strong>Registro dei trattamenti</strong> (art. 30 GDPR): secondo commenti al Regolamento e alle FAQ del Garante, è dovuto anche dalle piccole attività che trattano dati sulla salute dei clienti (per esempio estetiste). Verifica con un consulente.</li>
</ul>
${B('warn', 'Foto e social: casi reali', 'Nel 2024 il Garante privacy ha sanzionato con 8.000 euro un centro di medicina estetica per un video su Instagram che mostrava un paziente senza un consenso specifico. Nel 2026 la Cassazione (ord. n. 25117) ha dato ragione a una cliente fotografata in un centro estetico dopo che aveva negato il consenso. Regola pratica: niente foto senza un consenso separato, e mai volti o tatuaggi riconoscibili senza autorizzazione.')}
<h2>Consenso informato al servizio</h2>
<p>Non abbiamo trovato una norma nazionale che imponga all'onicotecnica un modulo specifico di "consenso informato". È però <strong>buona prassi</strong>: spiega per iscritto rischi e limiti (possibili allergie, sollevamenti, necessità di refill, rimozione in salone) e fai firmare. In ambito estetico i giudici chiedono informazioni <strong>personalizzate</strong>, non frasi generiche.</p>
${B('danger', 'Quando dire di no', 'Infezioni, micosi sospette, ferite aperte, unghia staccata dal letto, reazione allergica in corso: il servizio si rifiuta, si spiega il perché, si consiglia il medico e si annota sulla scheda.')}
`,
          sources: ['https://www.garanteprivacy.it/garante/doc.jsp?ID=9983210',
            'https://www.eutekne.info/Sezioni/Art_1121522_il_consenso_al_trattamento_dei_dati_non_necessari_all_esecuzione.aspx',
            'https://www.quotidianopiu.it/dettaglio/16439364/consenso-alle-foto-in-centro-estetico-la-firma-non-basta',
            'https://www.garanteprivacy.it/it/registro-delle-attivita-di-trattamento',
            'https://www.studiocataldi.it/articoli/40267-registro-attivita-di-trattamento-chi-deve-redigerlo.asp',
            'https://www.studiocataldi.it/articoli/46336-consenso-informato-piu-stringente-per-i-trattamenti-estetici.asp',
            'https://www.noze.it/insights/gdpr-dati-sanitari-art9/']
        },
        {
          id: 'aftercare', simple: "Il lavoro dura di più se la cliente sa come trattarlo: olio ogni giorno, guanti per le pulizie, niente unghie usate come attrezzi, e torna in salone se qualcosa si stacca.", title: 'Consigli post-trattamento', min: 8,
          html: `
<p>Molti problemi (sollevamenti, rotture, ingiallimento) nascono <strong>a casa</strong>. Spiegare i consigli post-trattamento (in inglese <em>aftercare</em>) fa durare il lavoro e protegge l'unghia naturale. Le parole si dimenticano: <strong>dallo per iscritto</strong>.</p>
${F('aftercare-si-no.svg', 'Cosa fare e cosa evitare dopo il servizio.')}
<h2>Cosa consigliare</h2>
<table>
<tr><th>Consiglio</th><th>Perché</th></tr>
<tr><td><strong>Olio per cuticole</strong> ogni giorno, alla base dell'unghia</td><td>Mantiene flessibili pelle e unghia naturale; una pelle secca alla base favorisce i sollevamenti</td></tr>
<tr><td><strong>Guanti</strong> per pulizie, piatti, giardinaggio, prodotti chimici</td><td>Acqua prolungata e detersivi indeboliscono l'adesione e possono macchiare il top</td></tr>
<tr><td><strong>Non usare le unghie come attrezzi</strong> (lattine, etichette, graffette)</td><td>La forza va tutta sul punto di stress</td></tr>
<tr><td><strong>Non mordere, non "pizzicare"</strong>, non staccare il prodotto</td><td>Strappando il prodotto si porta via la lamina</td></tr>
<tr><td><strong>Niente colla né cerotti</strong> su un'unghia sollevata o rotta</td><td>Chiudono umidità e batteri sotto il prodotto</td></tr>
<tr><td><strong>Rispettare la data del refill</strong></td><td>Dopo 3–4 settimane l'apex non è più nel posto giusto</td></tr>
<tr><td><strong>Non usare solventi</strong> o remover con acetone sulle ricostruzioni</td><td>Opacizzano e ammorbidiscono il prodotto</td></tr>
<tr><td><strong>Tornare subito</strong> in caso di sollevamenti, dolore, rossore, prurito o macchie</td><td>Prima si interviene, meno danni</td></tr>
</table>
<h2>Come spiegarli</h2>
<ol class="steps">
<li><strong>Alla fine del servizio</strong>, mentre la cliente guarda le unghie: è il momento in cui ascolta di più.</li>
<li>Scegli <strong>tre consigli</strong> chiave per quella cliente (per esempio chi lavora in cucina: guanti, olio, niente attrezzi).</li>
<li>Consegna un <strong>biglietto</strong> con i consigli e la <strong>data del prossimo appuntamento</strong>.</li>
<li><strong>Annota</strong> sulla scheda che i consigli sono stati dati (a voce e/o per iscritto).</li>
<li>Al refill, chiedi come è andata: è anche un modo per capire le cause dei problemi.</li>
</ol>
${F('aftercare-cartoncino.svg', 'Esempio di biglietto post-trattamento: fronte e retro.')}
${B('tip', 'Vendi l\'olio, non solo il servizio', 'Proporre un olio per cuticole da usare a casa è utile alla cliente (il lavoro dura di più) e a te (meno riparazioni). Mostrale come applicarlo: una goccia alla base, poi massaggia.')}
`,
          sources: ['https://booksolo.co/nailedbyalire/aftercare',
            'https://katiebarnesacademy.com/blogs/nail-structure-application/how-to-deal-with-nail-service-breakdown',
            'https://nailknowledge.org/?p=49737']
        },
        {
          id: 'portfolio-foto', simple: "Le foto dei tuoi lavori sono il tuo biglietto da visita e il tuo archivio per migliorare. Luce buona, sfondo semplice, cuticole pulite, colori veri. E mai pubblicare senza il consenso della cliente.", title: 'Fotografare i lavori e costruire il portfolio', min: 8,
          html: `
<p>Le foto servono a due cose: <strong>mostrare</strong> il tuo lavoro (social, sito, portfolio) e <strong>studiare</strong> i tuoi errori (apex, simmetria, smile line). Una buona foto non nasconde i difetti: li mostra, così puoi correggerli.</p>
${F('foto-set.svg', 'Un set semplice: luce dalla finestra o luce fredda, sfondo neutro, telefono stabile.')}
<h2>Il set</h2>
<table>
<tr><th>Elemento</th><th>Consiglio</th><th>Perché</th></tr>
<tr><td><strong>Luce</strong></td><td>Luce naturale da una finestra; altrimenti luce fredda/diurna o una lampada ad anello</td><td>La luce calda ingiallisce i colori</td></tr>
<tr><td><strong>Sfondo</strong></td><td>Neutro o in tinta con il design, senza oggetti che distraggono</td><td>Le unghie devono essere il soggetto</td></tr>
<tr><td><strong>Pulizia</strong></td><td>Cuticole pulite, poco olio, niente polvere</td><td>L'olio in eccesso sembra sporco o prodotto non pulito</td></tr>
<tr><td><strong>Telefono</strong></td><td>Fotocamera normale (non quella dei social), messa a fuoco sulle unghie</td><td>Più controllo e qualità</td></tr>
<tr><td><strong>Ritocco</strong></td><td>Solo luminosità, contrasto, ritaglio; niente filtri che cambiano il colore</td><td>La cliente deve ricevere ciò che vede in foto</td></tr>
</table>
<h2>Le angolazioni</h2>
${F('foto-angolazioni.svg', 'Dall\'alto, di profilo, a tunnel: tre foto per ogni lavoro.')}
<ol class="steps">
<li><strong>Dall'alto</strong>, dita unite: forma, simmetria, smile line, pulizia della cuticola.</li>
<li><strong>Di profilo</strong>: posizione dell'apex e spessore.</li>
<li><strong>A tunnel</strong> (dalla punta verso la cuticola): curva a C.</li>
<li>Per il portfolio, una foto "di posa": mano rilassata, dita leggermente piegate.</li>
</ol>
${B('tip', 'Archivio per migliorare', 'Salva le foto di ogni cliente con data e nome della scheda. Al refill rifai le stesse foto: vedrai dove si è spostato l\'apex e dove nascono i sollevamenti.')}
${B('warn', 'Consenso prima di pubblicare', 'La foto non serve a eseguire il servizio: per pubblicarla serve un consenso separato e specifico della cliente, che può anche rifiutare. Evita volti, tatuaggi, anelli particolari o altri dettagli che la rendono riconoscibile se non ha autorizzato.')}
`,
          sources: ['https://www.scratchmagazine.co.uk/feature/nailfies-nail-tech-expert-photography-tips/',
            'https://www.scratchmagazine.co.uk/feature/simply-salon-nails-photographing-your-nail-work',
            'https://nailac.com.pl/gb/blog/porady/how-to-take-nail-photos-that-will-get-your-clients-attention-',
            'https://www.garanteprivacy.it/garante/doc.jsp?ID=9983210',
            'https://www.quotidianopiu.it/dettaglio/16439364/consenso-alle-foto-in-centro-estetico-la-firma-non-basta']
        },
        {
          id: 'business', simple: "Il prezzo giusto non si copia: si calcola. Somma materiali, il valore del tuo tempo e le spese fisse, poi aggiungi un margine. Confronta con i prezzi della tua zona.", title: 'Prezzi, agenda e carriera', min: 13,
          html: `
<h2>Prezzi indicativi in Italia</h2>
<table>
<tr><th>Servizio</th><th>Fascia indicativa</th></tr>
<tr><td>Ricostruzione completa (mani)</td><td>circa 40–80 €; 100–140 € in centri di fascia alta</td></tr>
<tr><td>Ricostruzione su unghie rosicchiate</td><td>circa 90–100 €</td></tr>
<tr><td>Refill</td><td>circa 25–35 € (media citata intorno ai 30 €); di più nei centri di fascia alta</td></tr>
<tr><td>Semipermanente</td><td>circa 30–35 €</td></tr>
</table>
<p class="muted"><small>Dati da articoli e testimonianze 2021–2025: non sono listini ufficiali, non esiste una media nazionale aggiornata e i prezzi variano molto per città, zona e centro. Le fonti divergono: usali solo come ordine di grandezza.</small></p>
<h2>Come calcolare il tuo prezzo</h2>
${F('calcolo-prezzo.svg', 'Prezzo = materiali + tempo + spese fisse + margine.')}
<ol class="steps">
<li><strong>Costo dei materiali per servizio</strong>: somma tutto quello che compri in un mese per i servizi (gel, lime, salviette, cleaner, DPI…) e dividi per il numero di clienti del mese. Fallo per più mesi e fai la media.</li>
<li><strong>Valore del tuo tempo</strong>: decidi quanto vuoi guadagnare in un anno e dividilo per le ore che lavori davvero con le clienti (togli ferie, pulizie, ordini, formazione).</li>
<li><strong>Spese fisse all'ora</strong>: affitto, utenze, assicurazione, commercialista, software, ammortamento di lampade e fresa… diviso per le ore lavorate.</li>
<li><strong>Prezzo minimo</strong> = materiali + (tempo del servizio × [valore orario + spese fisse orarie]).</li>
<li>Aggiungi un <strong>margine</strong> per imprevisti e investimenti, poi <strong>confronta</strong> con i prezzi della tua zona.</li>
</ol>
${B('info', 'Esempio di calcolo (numeri di fantasia)', 'Materiali 6 €; servizio di 1,5 ore; valore orario 15 € e spese fisse 8 € all\'ora. Prezzo minimo: 6 + 1,5 × (15 + 8) = 40,50 €. Se nella tua zona il servizio costa meno, devi diventare più veloce o ridurre le spese, non lavorare in perdita.')}
${B('warn', 'Le tasse e i contributi', 'Dal prezzo incassato vanno tolti imposte e contributi INPS (vedi la lezione sull\'apertura dell\'attività). Il "valore orario" che ti resta in tasca è più basso di quello che incassi.')}
<h2>Agenda e tempi</h2>
${F('agenda-tempi.svg', 'Agenda: tempi del servizio più consulenza, consigli e pulizia.')}
<ul>
<li><strong>Misura i tuoi tempi</strong> reali con un cronometro per 10 servizi di ogni tipo. Da principiante sarai più lenta: è normale.</li>
<li>Nell'agenda aggiungi a ogni servizio i minuti per <strong>igiene della postazione e sterilizzazione</strong>.</li>
<li>Prenota il <strong>refill</strong> prima che la cliente esca.</li>
<li>Scrivi e comunica in anticipo le regole su <strong>ritardi e disdette</strong> (per esempio entro quante ore si può spostare l'appuntamento).</li>
<li>Manda un <strong>promemoria</strong> il giorno prima: riduce le assenze.</li>
</ul>
<h2>Percorsi professionali</h2>
<table>
<tr><th>Percorso</th><th>Cosa serve in più</th></tr>
<tr><td>Dipendente in centro estetico o nail bar</td><td>Velocità, pulizia, lavoro in squadra</td></tr>
<tr><td>Titolare / libera professionista</td><td>Qualifica di estetista, partita IVA, SCIA, gestione dei conti</td></tr>
<tr><td>Educator / formatrice per un marchio</td><td>Esperienza, capacità di spiegare, conoscenza tecnica dei prodotti</td></tr>
<tr><td>Nail artist per moda, editoria, foto</td><td>Portfolio curato, creatività, rapidità sul set</td></tr>
<tr><td>Tecnico-commerciale per aziende</td><td>Conoscenza dei prodotti, relazioni con i saloni</td></tr>
<tr><td>Competizioni</td><td>Allenamento mirato (vedi modulo <em>Nail art avanzata e gare</em>)</td></tr>
</table>
${F('gara-scheda.svg', 'In gara si giudicano struttura, simmetria, pulizia e smile line.')}
`,
          sources: ['https://tattoomuse.it/wiki/quanto-costa-il-gel-per-le-unghie-dallestetista',
            'https://dilei.it/bellezza/cose-e-quanto-costa-il-refill-delle-unghie-in-gel/637264/',
            'https://www.arredamento.it/forum/viewtopic.php?p=300359',
            'https://www.youngnails.com/blogs/news/calculating-your-cost-per-nail-service',
            'https://www.scratchmagazine.co.uk/news/nailympia-germany-2025-the-results/']
        },
        {
          id: 'apertura-fisco', simple: "Per lavorare in proprio servono la qualifica di estetista, la partita IVA, l'iscrizione come artigiana con i contributi INPS e la SCIA al Comune. I numeri cambiano ogni anno: verifica sempre con un commercialista.", title: 'Aprire l\'attività: partita IVA, INPS, SCIA, assicurazione', min: 12,
          html: `
${B('warn', 'Prima di tutto', 'Questa lezione dà un\'idea del percorso, non sostituisce un commercialista. Regole, importi e scadenze cambiano ogni anno e da Comune a Comune. I valori qui sotto sono riferiti al 2026.')}
<h2>Il percorso, in ordine</h2>
${F('percorso-apertura.svg', 'Dalla qualifica alla prima cliente: i passaggi principali.')}
<ol class="steps">
<li><strong>Qualifica di estetista</strong> (L. 1/1990 e leggi regionali): in Italia la ricostruzione unghie rientra nell'attività di estetista. Alcuni regolamenti comunali citano esplicitamente l'<em>onicotecnica</em> tra le attività dell'estetista.</li>
<li><strong>Partita IVA</strong> con il codice <strong>ATECO</strong> dell'attività. Con la classificazione ATECO 2025 il codice per manicure e pedicure risulta <strong>96.22.01</strong> (prima 96.02.03): fattelo confermare dal commercialista.</li>
<li><strong>Registro delle imprese e Albo delle imprese artigiane</strong> (Camera di Commercio, pratica unica telematica "ComUnica").</li>
<li><strong>INPS – Gestione artigiani</strong> e, per le artigiane, <strong>INAIL</strong>.</li>
<li><strong>SCIA</strong> (Segnalazione certificata di inizio attività) allo <strong>SUAP</strong> del Comune, con i requisiti igienico-sanitari dei locali e il nome della responsabile tecnica qualificata.</li>
<li><strong>Adempimenti pratici</strong>: incassi documentati (documento commerciale), pagamenti elettronici, informativa privacy, tariffe esposte se il Comune lo richiede, assicurazione.</li>
</ol>
<h2>Esempio di regole comunali</h2>
<p>Ogni Comune ha il suo regolamento. Quello di Piacenza (2025), per esempio:</p>
<ul>
<li>include l'<strong>onicotecnica</strong> nell'attività di estetista;</li>
<li>permette il lavoro <strong>a domicilio del cliente</strong> solo a chi ha già un'attività in sede fissa, per persone malate o con difficoltà di movimento o per eventi (matrimoni, cerimonie), con strumenti monouso;</li>
<li>permette il lavoro a casa dell'esercente solo in locali idonei, <strong>usati solo per l'attività</strong> e separati dall'abitazione;</li>
<li>obbliga a <strong>esporre le tariffe</strong> nel locale e gli orari all'esterno (sanzione da 80 a 480 €).</li>
</ul>
<p class="muted"><small>È un esempio: leggi il regolamento del tuo Comune prima di aprire.</small></p>
<h2>Regime forfettario: come funziona</h2>
<table>
<tr><th>Voce</th><th>Regola 2026</th></tr>
<tr><td>Limite di ricavi</td><td><strong>85.000 €</strong> l'anno. Tra 85.000 e 100.000 € si esce dall'anno dopo; oltre 100.000 € si esce subito</td></tr>
<tr><td>Coefficiente di redditività</td><td><strong>67%</strong> per i servizi alla persona: si paga sul 67% di ciò che incassi, non sui costi reali</td></tr>
<tr><td>Imposta sostitutiva</td><td><strong>5%</strong> per i primi 5 anni se è una vera nuova attività (requisiti precisi); poi <strong>15%</strong></td></tr>
<tr><td>IVA</td><td>Non si applica sulle prestazioni</td></tr>
</table>
${F('forfettario-esempio.svg', 'Esempio: dagli incassi al reddito su cui si pagano contributi e imposta.')}
${B('info', 'Esempio semplificato', 'Incassi 30.000 €. Reddito forfettario = 30.000 × 67% = 20.100 €. Su questo si calcolano i contributi INPS; i contributi versati si deducono, e sul resto si paga l\'imposta del 5% o del 15%. Le spese reali (prodotti, affitto) NON si scaricano: sono già "comprese" nel 33% non tassato.')}
<h2>Contributi INPS artigiani (2026)</h2>
<ul>
<li>Si pagano <strong>contributi fissi</strong> su un reddito minimo (minimale) di <strong>18.808 €</strong>: circa <strong>4.521 € l'anno</strong>, in 4 rate, <strong>anche se guadagni meno</strong>.</li>
<li>Sopra il minimale si paga il <strong>24%</strong> (25% oltre 56.224 €).</li>
<li>Chi è in forfettario può chiedere una <strong>riduzione del 35%</strong> con domanda telematica all'INPS (per il 2026 entro il 28 febbraio; per le attività nuove, subito dopo l'iscrizione). Le fonti non concordano sugli effetti di una domanda tardiva: chiedi al commercialista.</li>
<li>Per chi ha iniziato nel 2025 esiste una riduzione del 50% per 36 mesi (non cumulabile con quella del 35%); dalle fonti consultate non risulta estesa a chi apre nel 2026.</li>
</ul>
${B('danger', 'Il primo anno', 'Molte principianti scoprono i contributi fissi solo alla prima scadenza. Metti da parte ogni mese una quota degli incassi per tasse e contributi.')}
<h2>Assicurazione RC</h2>
<p>Non risulta un <strong>obbligo nazionale</strong> di assicurazione di responsabilità civile per l'estetista (l'obbligo generale riguarda i professionisti iscritti ad albi). Alcune Regioni, Comuni o associazioni di categoria possono richiederla. È comunque <strong>fortemente consigliata</strong>: copre i danni alle clienti (per esempio una reazione allergica o una lesione) e, in salone, i danni a terzi nei locali.</p>
`,
          sources: ['https://www.fiscozen.it/guide/codice-ateco-onicotecinca/',
            'https://www.mysolution.it/fisco/guide/guide-tematiche/come-avviare-unattivita-economica/estetista-e-centri-di-bellezza/',
            'https://www.informazionefiscale.it/contributi-inps-artigiani-commercianti-importi-aliquote-2026',
            'https://www.fisco7.it/2026/02/forfettari-domanda-inps-per-lo-sconto-contributivo-2026-scadenza-perentoria-il-28-febbraio/',
            'https://www.fiscozen.it/guide/quanto-dura-il-regime-forfettario-al-5-2/',
            'https://centrofiscale.com/regime-forfettario-2026-requisiti-aliquote/',
            'https://www.comune.piacenza.it/s3/5141/allegati/documenti-e-dati/atto-normativo/regolamenti/regolamenti-criteri-e-indirizziattivit-economiche-commercio-regolamenti/regolamento-acconciatore-estetista-tatuatore_approvato.pdf',
            'https://www.moneyside.app/it/learn/assicurazioni/assicurazione-rc-estetisti',
            'https://www.money.it/rc-professionale-quando-e-obbligatoria-e-per-quali-lavoratori']
        }
      ]
    },
    /* ------------------------------------------------------------------ 13 */
    {
      id: 'onicofagia', n: 13, level: 'avanz', title: 'Onicofagia e unghie difficili',
      summary: ['Ferite, pus, gonfiore, dolore o distacco della lamina: non si lavora, si consiglia il medico.', 'Su unghie rosicchiate: cartina rifilata (o tip, secondo i casi) aderente al bordo, pelle rialzata spinta in basso.', 'Allungamento corto: al massimo circa 1/3 della lunghezza della lamina; forma tonda, senza bordi da "pizzicare".', 'Il letto artificiale si crea con un cover davvero coprente: controlla controluce.', 'All\'inizio appuntamenti ravvicinati (circa ogni 2 settimane, prassi); il recupero richiede mesi.', 'Cucchiaio, ski-jump, pinza, piatta: osserva da tre lati e adatta la costruzione, non forzare l\'unghia.'],
      desc: 'Unghie rosicchiate (valutazione, costruzione, percorso di recupero) e unghie a cucchiaio, ski-jump, a pinza, piatte, sottili o grasse.',
      lessons: [
        {
          id: 'onicofagia-valutazione', title: 'Unghie rosicchiate: valutazione e limiti', min: 14,
          simple: 'Prima di costruire guardi bene mani e pelle. Se ci sono ferite o infiammazione aspetti che guariscano. Se è tutto integro, si può partire con un\'unghia corta.',
          videos: [{ id: 'pW5BXeGSUSE', title: 'Ricostruzione su onicofagica: 3 metodi step by step', channel: 'Elena Santucci', lang: 'IT' }],
          html: `
<p>L'<strong>onicofagia</strong> è l'abitudine di mangiarsi le unghie. La dermatologia la definisce come il morso ripetuto della lamina, delle pieghe laterali, del letto ungueale e della cuticola. È molto comune: secondo le revisioni scientifiche riguarda fino al 20–30% della popolazione e fino al 45% dei ragazzi tra i 10 anni e la pubertà. Probabilmente i casi reali sono ancora di più, perché molte persone se ne vergognano e non ne parlano.</p>
<p>Per te, onicotecnica, una cliente che si mangia le unghie è una sfida tecnica ma anche una grande soddisfazione. Prima però devi capire <strong>se</strong> si può lavorare e <strong>come</strong>.</p>
${F("onicofagia-segni.svg", "Come si riconosce un'unghia rosicchiata: vista dall'alto e di profilo.")}
<h2>Come si presenta un'unghia rosicchiata</h2>
<ul>
<li><strong>Lamina corta e bordo irregolare</strong>, "seghettato", spesso senza bordo libero.</li>
<li><strong>Letto ungueale accorciato</strong>. Se la lamina viene strappata spesso, il letto scoperto si indurisce e la lamina può restare corta anche per sempre.</li>
<li><strong>Cuscinetto di pelle rialzato</strong> davanti all'unghia. È l'iponichio che, senza la lamina a proteggerlo, si ispessisce e si alza. A volte si "allunga" sotto il bordo (iponichio esteso).</li>
<li><strong>Cuticole e pieghe laterali</strong> strappate, con pellicine e piccole ferite in fasi diverse di guarigione.</li>
<li>Possibili <strong>puntini o righe rosso-scure</strong> (piccole emorragie), solchi trasversali, lamina fragile, lunula che sembra più grande.</li>
<li>Una <strong>banda scura longitudinale</strong> può comparire per il trauma sulla matrice. Una banda scura nuova va sempre fatta vedere al medico: non spetta a te dire da cosa dipende.</li>
</ul>
${B("info", "Perché l'iponichio si alza", "L'iponichio è la pelle che sigilla lo spazio sotto il bordo libero. Quando la lamina manca, viene toccato e morso continuamente. Si ispessisce come una piccola callosità e si solleva sopra il livello della lamina. È pelle viva: non si taglia e non si lima. Si spinge solo delicatamente verso il basso con la cartina.")}
<h2>Rischi per la salute</h2>
<p>Mordere le unghie porta i batteri della bocca sulla pelle intorno all'unghia. Le complicanze descritte in letteratura sono:</p>
<ul>
<li><strong>Paronichia acuta</strong>: infezione della piega intorno all'unghia, rossa, gonfia, calda e dolente, a volte con pus.</li>
<li><strong>Paronichia cronica</strong>: infiammazione che dura settimane, con piega gonfia e cuticola assente.</li>
<li>Infezioni virali: <strong>verruche</strong> intorno e sotto l'unghia, <strong>patereccio erpetico</strong> (vescicole dolorose).</li>
<li>Nei casi gravi l'infezione può arrivare in profondità, fino all'osso (osteomielite, rara).</li>
<li>Danni ai denti e alle gengive. Non riguardano il tuo lavoro, ma spiegano perché il medico e il dentista possono essere coinvolti.</li>
</ul>
${F("onicofagia-semaforo.svg", "Semaforo della valutazione: verde si lavora, giallo si rimanda, rosso si invia al medico.")}
<h2>Il semaforo: lavorare, rimandare o inviare</h2>
<table>
<tr><th>Situazione</th><th>Cosa vedi</th><th>Cosa fai</th></tr>
<tr><td><strong>Verde</strong></td><td>Lamina corta ma integra. Pelle chiusa, non gonfia. Nessun dolore.</td><td>Puoi lavorare con allungamento corto.</td></tr>
<tr><td><strong>Giallo</strong></td><td>Pellicine strappate di recente, piccoli tagli che stanno guarendo, cuticola molto irritata.</td><td>Rimanda di qualche giorno. Nel frattempo: olio, guanti per le pulizie. Lavora solo a pelle chiusa.</td></tr>
<tr><td><strong>Rosso</strong></td><td>Ferite aperte o che sanguinano, gonfiore, calore, pus, dolore che non passa, lamina staccata dal letto (onicolisi), banda scura nuova, verruche.</td><td>Niente servizio. Spiega con calma il perché e consiglia il medico o il dermatologo.</td></tr>
</table>
${B("danger", "Quando NON lavorare", "Ferite aperte, pellicine strappate che sanguinano, gonfiore, pus, dolore persistente o unghia staccata dal letto (onicolisi): rimanda la seduta e consiglia il dermatologo. Coprire un'infiammazione con il gel non la cura: la chiude sotto il prodotto e può peggiorarla.")}
<h2>Cosa valutare, passo per passo</h2>
<ol class="steps">
<li><strong>Parla con la cliente</strong>. Da quanto tempo si mangia le unghie? Lo fa ancora? Morde anche le pellicine? Lo fa di notte, quando è nervosa, quando si annoia? Che cosa si aspetta dal trattamento?</li>
<li><strong>Osserva da tre lati</strong>: dall'alto, di profilo e dalla punta del dito. Usa una buona luce.</li>
<li><strong>Misura quanto letto ungueale resta</strong>. Questo ti dice quanto puoi allungare (vedi la lezione successiva: circa 1/3).</li>
<li><strong>Controlla il cuscinetto di pelle</strong> davanti all'unghia: è più alto della lamina? Si abbassa premendo leggermente, senza dolore?</li>
<li><strong>Controlla cuticole e pieghe laterali</strong>: pelle chiusa o ferite?</li>
<li><strong>Valuta la lamina</strong>: spessore, flessibilità, forma (piatta, a cucchiaio, curva).</li>
<li><strong>Annota tutto nella scheda cliente</strong>, con una foto "prima" se la cliente acconsente. Ti servirà per mostrare i progressi.</li>
</ol>
<h2>L'abitudine: cosa puoi dire e cosa no</h2>
<p>La ricostruzione aiuta molte clienti perché copre le unghie rovinate mentre ricrescono e rende più difficile mordere. Gli studi dermatologici citano la manicure professionale come un aiuto utile per le persone motivate a smettere. Però <strong>non è una cura</strong>.</p>
<ul>
<li>Se l'abitudine è forte o legata all'ansia, puoi suggerire alla cliente di parlarne con il medico. Esistono percorsi efficaci, come la terapia di <strong>inversione dell'abitudine</strong> (habit reversal training).</li>
<li>Esistono smalti dal <strong>sapore amaro</strong> pensati per scoraggiare il morso. Puoi nominarli come possibilità, senza promettere risultati.</li>
<li>Non fare diagnosi e non dare giudizi. Frasi come "devi smettere" mettono a disagio. Meglio: "Lavoriamo insieme: io ti do unghie belle, tu provi a non morderle".</li>
</ul>
${B("tip", "Una frase utile", "«Le tue unghie possono migliorare molto. Iniziamo corte e robuste, poi allunghiamo un po' alla volta mentre la tua unghia ricresce.» Dà fiducia e mette aspettative realistiche.")}
<h2>Errori frequenti</h2>
<ul>
<li>Lavorare su una pellicina appena strappata "perché tanto si copre".</li>
<li>Tagliare o limare il cuscinetto di pelle davanti all'unghia: è tessuto vivo.</li>
<li>Promettere unghie lunghe già alla prima seduta.</li>
<li>Non fotografare il "prima": senza confronto la cliente non vede i progressi e si scoraggia.</li>
</ul>
`,
          sources: ['https://pmc.ncbi.nlm.nih.gov/articles/PMC8953487/',
            'https://www.my-personaltrainer.it/salute-benessere/onicofagia-conseguenze-terapia.html',
            'https://www.my-personaltrainer.it/salute/mangiarsi-le-unghie-perche-non-e-solo-un-vizio-e-quali-sono-i-rischi-per-la-salute.html',
            'https://www.scratchmagazine.co.uk/blog/form-fitting-for-nail-biters']
        },
        {
          id: 'onicofagia-costruzione', title: 'Costruire su unghie rosicchiate', min: 18,
          simple: 'Dove l\'unghia manca la "disegni" con un gel color pelle (cover), così sembra più lunga. Poi aggiungi solo un bordo corto e tondo, difficile da mordere.',
          videos: [{ id: 'eZlxtMxLUZQ', title: 'Ricostruzione onicofagia', channel: 'Nails education', lang: 'IT' }],
          html: `
${F("onicofagia.svg", "Ricostruzione su unghie rosicchiate in quattro passaggi.")}
<p>Su un'unghia rosicchiata il problema non è solo la lunghezza. Mancano il bordo libero e spesso una parte di letto ungueale, e davanti all'unghia c'è un cuscinetto di pelle rialzato. L'obiettivo è costruire un'unghia <strong>corta, robusta e naturale</strong>, che la cliente non riesca a "pizzicare" con i denti.</p>
<h2>Cartina o tip?</h2>
<p>Le fonti professionali non sono d'accordo, e questo ti dice che entrambi i metodi funzionano se eseguiti bene.</p>
<table>
<tr><th></th><th>Cartina (form)</th><th>Tip</th></tr>
<tr><td>Vantaggi</td><td>Si rifila su misura e si adatta a bordi irregolari e al cuscinetto di pelle. Permette di costruire letto e bordo come vuoi.</td><td>Veloce. Dà subito una forma regolare. Alcuni tecnici lo preferiscono proprio sulle mangiatrici di unghie.</td></tr>
<tr><td>Limiti</td><td>Richiede pratica per farla aderire senza spazi.</td><td>Ha bisogno di una zona minima di incollaggio. Su una lamina cortissima e irregolare può staccarsi.</td></tr>
<tr><td>Quando (prassi)</td><td>Lamina molto corta, bordo seghettato, pelle rialzata.</td><td>Lamina corta ma con bordo regolare e un minimo di superficie.</td></tr>
</table>
<p>In questa lezione seguiamo la <strong>cartina</strong>, che è il metodo più adattabile per chi inizia.</p>
${F("onicofagia-cartina-adattata.svg", "Come rifilare la cartina: linguetta, taglio a U per l'iponichio, lati a 45°, cartina aderente che spinge giù la pelle.")}
<h2>Adattare la cartina: il passaggio decisivo</h2>
<p>Con una mangiatrice di unghie la cartina deve stare <strong>a filo del bordo</strong>, anche se il bordo quasi non c'è. Se resta uno spazio tra unghia e cartina, il prodotto cola sotto. Si forma uno scalino che è un punto debole e, in più, è un appiglio da mordere.</p>
<ol class="steps">
<li><strong>Taglia la linguetta</strong> della cartina se ti impedisce di appoggiarla bene. In questo modo la cartina può stare sotto e spingere in basso il cuscinetto di pelle.</li>
<li><strong>Taglia una piccola "U"</strong> nel punto in cui l'iponichio è più alto. Così la cartina non preme sulla pelle e non fa male.</li>
<li><strong>Rifila i lati a circa 45°</strong>, seguendo i solchi laterali. Così la cartina si chiude meglio e la curva a C viene regolare.</li>
<li><strong>Appoggia la cartina</strong> sotto il bordo, in asse con il dito. Chiudila sotto il polpastrello <strong>tirando leggermente verso il basso</strong>: la pelle rialzata scende e lascia spazio all'allungamento.</li>
<li><strong>Controlla da tre lati</strong>: dall'alto (in asse), di profilo (dritta, senza scendere né salire), dalla punta (nessuno spazio).</li>
</ol>
${B("warn", "Non deve fare male", "Tirare la cartina verso il basso serve ad abbassare la pelle, non a schiacciarla. Se la cliente sente dolore, allenta e rifila meglio la U. Il dolore è un segnale di pressione su tessuti vivi.")}
${F("onicofagia-step.svg", "Costruzione in sei passaggi: preparazione, cartina, cover, bordo, apex, limatura.")}
<h2>La costruzione, passo per passo</h2>
<ol class="steps">
<li><strong>Prepara</strong> come sempre: igiene delle mani, cuticola (la pelle morta sulla lamina) arretrata e rimossa delicatamente senza tagli, opacizzazione leggera (non assottigliare una lamina già fragile), polvere via, disidratante, primer se previsto dal sistema.</li>
<li><strong>Base sottile</strong> sulla lamina, a circa 1 mm dalla pelle, e lampada secondo la scheda tecnica.</li>
<li><strong>Letto artificiale con il cover</strong>. Stendi un gel cover <strong>davvero coprente</strong> dalla lamina oltre il letto naturale, fino alla lunghezza di letto che hai deciso. Puoi farlo in due strati sottili. Polimerizza.</li>
<li><strong>Bordo libero</strong>. Costruisci la punta con builder trasparente, rosa naturale o bianco (french). Tienila corta.</li>
<li><strong>Struttura</strong>. Un velo di builder su tutta l'unghia, con l'<strong>apex</strong> nella zona 2, sopra il nuovo punto di stress. Su unghie corte l'apex è basso e morbido: niente "gobba".</li>
<li><strong>Togli la cartina</strong>, poi lima: lati paralleli, forma tonda o squoval corta, bordo sottile e uniforme. Controlla che non ci siano spigoli o bordi taglienti.</li>
<li><strong>Finitura</strong>: top, lampada, eventuale pulizia dello strato di dispersione, olio sulle cuticole.</li>
</ol>
${B("info", "Cuticola e pterigio non sono la stessa cosa", "In preparazione togli solo la cuticola, cioè la pelle morta attaccata alla lamina. Lo pterigio invece è un'alterazione dell'unghia (una specie di cicatrice), non un sinonimo di cuticola: non si rimuove, si indirizza al medico.")}
${F("cover-letto.svg", "Il cover prolunga visivamente il letto ungueale.")}
${F("onicofagia-proporzioni.svg", "Proporzioni: allungamento al massimo circa 1/3 della lamina.")}
<h2>Quanto allungare</h2>
<p>Una formatrice professionale indica una regola semplice: l'allungamento non dovrebbe superare circa <strong>1/3 della lunghezza della lamina</strong>. A volte serve un po' di più solo per arrivare dove sarebbe il bordo naturale. Il motivo: una leva lunga su un'unghia piccola fa forza sulla lamina e sul letto, e la cliente non è abituata ad avere "qualcosa in più" sulla punta delle dita.</p>
${B("tip", "Niente bordi da mordicchiare", "La forma deve essere liscia e arrotondata, senza angoli vivi. Se lasci un bordo o uno scalino, la cliente può iniziare a «pizzicarlo» al posto di mordere: cambia l'abitudine, non il problema.")}
<h2>Il cover deve coprire davvero</h2>
<p>Molti rosa "coprenti" non lo sono abbastanza. Se il cover è troppo trasparente si vede la linea del letto naturale e l'effetto ottico sparisce.</p>
<ul>
<li>Controlla <strong>controluce</strong> dopo ogni strato: non devono esserci "finestre" più chiare.</li>
<li>Fai appoggiare bene gli angoli della smile line sul cover: così non restano zone trasparenti ai lati (le "orecchie").</li>
<li>Scegli la tonalità del cover alla luce naturale (vedi il modulo Cover e colori).</li>
</ul>
<h2>Errori frequenti e come evitarli</h2>
<table>
<tr><th>Errore</th><th>Conseguenza</th><th>Rimedio</th></tr>
<tr><td>Spazio tra unghia e cartina</td><td>Il prodotto cola sotto: scalino, punto debole, appiglio da mordere</td><td>Rifila meglio la cartina; controlla dalla punta prima di stendere</td></tr>
<tr><td>Allungamento troppo lungo</td><td>Leva eccessiva, rotture, sollevamenti</td><td>Al massimo circa 1/3; allunga gradualmente ai refill</td></tr>
<tr><td>Cover trasparente</td><td>Si vede il letto naturale corto</td><td>Cover più coprente, due strati sottili, controllo controluce</td></tr>
<tr><td>Troppo prodotto</td><td>Unghia spessa e innaturale, calore in lampada</td><td>Strati sottili; apex basso</td></tr>
<tr><td>Limatura aggressiva della lamina</td><td>Lamina ancora più sottile e dolente</td><td>Solo opacizzare, con lima 180–240 o buffer</td></tr>
</table>
`,
          sources: ['https://www.scratchmagazine.co.uk/blog/form-fitting-for-nail-biters',
            'https://silcare.com/en/blog/how-to-deal-with-a-clients-bitten-nails-step-by-step-reconstruction-of-bitten-nails-1716549279.html',
            'https://www.salongeek.com/threads/sculpting-bitten-nails.58468/',
            'https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-fit-nail-forms-to-different-nail-shapes']
        },
        {
          id: 'onicofagia-percorso', title: 'Il percorso di recupero: refill, tempi e consigli', min: 12,
          simple: 'Le unghie rosicchiate non guariscono in un giorno. Con appuntamenti regolari e qualche abitudine nuova, in alcuni mesi l\'unghia naturale ricresce sotto la ricostruzione.',
          html: `
<p>La prima ricostruzione è solo l'inizio. Su un'unghia rosicchiata il vero risultato arriva nei mesi successivi, quando la lamina naturale ricresce protetta sotto il prodotto. Il tuo lavoro è accompagnare la cliente in questo percorso.</p>
${F("onicofagia-timeline.svg", "Linea del tempo indicativa del recupero: dalla prima seduta a circa 6 mesi.")}
<h2>Quanto ci vuole</h2>
<p>L'unghia della mano cresce in media <strong>circa 3,5 mm al mese</strong> (3,47 mm in uno studio su giovani adulti). Un'unghia completa, dalla cuticola al bordo, si rinnova in circa <strong>4–6 mesi</strong>. Per questo il recupero di un'unghia rosicchiata si misura in mesi, non in settimane.</p>
${B("info", "Il letto può restare corto", "Se la cliente si è mangiata le unghie per anni, una parte del letto ungueale può restare più corta per sempre. Anche smettendo di mordere, la lamina non sempre «riattacca» fino in fondo. Il cover servirà ancora per l'effetto ottico. Dillo con delicatezza, senza promesse.")}
<h2>Appuntamenti: perché più ravvicinati all'inizio</h2>
<ul>
<li>Le ricostruzioni su unghie molto rosicchiate <strong>durano meno</strong> di quelle su unghie sane. La superficie di appoggio è piccola e la cliente può ancora "provare" a mordere.</li>
<li>Per questo all'inizio conviene vedere la cliente <strong>più spesso</strong>: nella pratica, circa ogni 2 settimane. Poi si passa al refill normale ogni 3–4 settimane.</li>
<li>Continua a vederla anche quando ha smesso di mordere: i controlli regolari aiutano a non ricominciare.</li>
</ul>
${F("refill.svg", "Ricrescita e refill: il profilo prima e dopo il riequilibrio.")}
<h2>Il refill su ex mangiatrice di unghie</h2>
<ol class="steps">
<li>Confronta con la foto della seduta precedente: il letto è cresciuto? Ci sono nuove ferite?</li>
<li>Controlla i segni di morso sul prodotto: bordi masticati o scheggiati vanno limati e lisciati.</li>
<li>Elimina le parti sollevate, come in ogni refill.</li>
<li>Riporta l'apex sopra il nuovo punto di stress.</li>
<li>Se il letto naturale è cresciuto, accorcia il cover di conseguenza: la smile line segue il nuovo letto.</li>
<li>Allunga il bordo libero <strong>poco alla volta</strong>, solo se la cliente si trova bene.</li>
</ol>
${F("onicofagia-aftercare.svg", "Il kit dei consigli a casa: olio, limetta, guanti, refill puntuale.")}
<h2>Consigli a casa (aftercare)</h2>
<table>
<tr><th>Consiglio</th><th>Perché</th></tr>
<tr><td>Olio per cuticole ogni giorno</td><td>Pelle elastica = meno pellicine da strappare.</td></tr>
<tr><td>Una limetta sempre in borsa</td><td>Se un bordo si scheggia, si lima invece di morderlo.</td></tr>
<tr><td>Guanti per pulizie e piatti</td><td>Acqua e detersivi seccano la pelle e indeboliscono il prodotto.</td></tr>
<tr><td>Non usare le unghie come attrezzi</td><td>Leve e urti causano sollevamenti e rotture.</td></tr>
<tr><td>Se si stacca qualcosa: non tirare</td><td>Strappare porta via strati di lamina. Meglio chiamare e fissare un ritocco.</td></tr>
<tr><td>Riconoscere i momenti "a rischio"</td><td>Stress, noia, schermo: tenere le mani occupate aiuta (consiglio generale, non terapia).</td></tr>
</table>
${B("tip", "Fai vedere i progressi", "Una foto ogni refill, sempre con la stessa luce e la stessa angolazione. Vedere il letto che si allunga è la motivazione più forte per non mordere.")}
<h2>Errori frequenti</h2>
<ul>
<li>Allungare troppo e troppo presto perché «ora va meglio».</li>
<li>Lasciare un bordo scheggiato dalla seduta precedente.</li>
<li>Lasciar passare 5–6 settimane tra un appuntamento e l'altro nelle prime fasi.</li>
</ul>
`,
          sources: ['https://bionumbers.hms.harvard.edu/bionumber.aspx?id=112380',
            'https://www.healthline.com/health/how-long-does-it-take-for-a-toenail-to-grow-back',
            'https://www.scratchmagazine.co.uk/blog/form-fitting-for-nail-biters',
            'https://pmc.ncbi.nlm.nih.gov/articles/PMC8953487/']
        },
        {
          id: 'unghie-difficili', title: 'Unghie a cucchiaio, ski-jump, a pinza, piatte', min: 16,
          simple: 'Ogni unghia ha la sua forma: tu non la "raddrizzi", la accompagni con la costruzione giusta. Prima guardala da tre lati, poi decidi.',
          html: `
<p>Un'unghia "difficile" è un'unghia con una forma naturale che rende più complicato costruire. Non è una malattia in sé, ma <strong>alcune forme possono essere un segnale</strong> da far valutare al medico. Il tuo compito è riconoscerle, adattare la tecnica e sapere quando fermarti.</p>
${F("unghie-difficili-viste.svg", "Le tre viste per riconoscere la forma: dall'alto, di profilo, dalla punta.")}
<h2>Prima regola: guarda da tre lati</h2>
<ol class="steps">
<li><strong>Dall'alto</strong>: larghezza, lati paralleli o svasati, forma del bordo.</li>
<li><strong>Di profilo</strong>: la lamina è dritta, curva verso il basso o sale verso l'alto (ski-jump)? È concava (cucchiaio)?</li>
<li><strong>Dalla punta</strong> (vista "a tunnel"): quanto è curva la C? È piatta o si chiude a pinza?</li>
</ol>
${F("unghie-difficili.svg", "Quattro unghie difficili e la strategia di costruzione.")}
<h2>Riconoscere e adattare</h2>
<table>
<tr><th>Unghia</th><th>Come si riconosce</th><th>Perché è difficile</th><th>Strategia (prassi)</th></tr>
<tr><td><strong>A cucchiaio</strong> (coilonichia)</td><td>Lamina concava, sottile: "trattiene una goccia d'acqua".</td><td>Se segui la conca, l'allungamento punta in alto e il prodotto si accumula al centro.</td><td>Livella prima la conca con un velo di builder. Poi cartina in asse con il dito (non con la conca) e apex regolare.</td></tr>
<tr><td><strong>Ski-jump</strong></td><td>Di profilo, il bordo libero sale verso l'alto come un trampolino.</td><td>Tip o cartina seguono la salita e l'unghia sembra "a paletta".</td><td>Accorcia l'unghia naturale fin dove inizia la salita. Cartina leggermente inclinata verso il basso. Più prodotto in zona 2 per "raddrizzare" otticamente il profilo. Riequilibri frequenti.</td></tr>
<tr><td><strong>A pinza / a tegola</strong></td><td>Dalla punta, i lati si chiudono verso il centro e stringono il letto. Più frequente sugli alluci.</td><td>I lati premono già sui tessuti. Una curva forzata aumenta la pressione.</td><td>Curva a C moderata, <strong>niente pinching</strong>, lati non stretti, lunghezza contenuta. Se c'è dolore o infiammazione: medico o podologo.</td></tr>
<tr><td><strong>Piatta e larga</strong></td><td>Dalla punta, quasi nessuna curva.</td><td>Unghie piatte sembrano larghe e si rompono più facilmente sul bordo.</td><td>Crea la curva a C con la cartina ben modellata. Lati paralleli o leggermente convergenti, apex centrato. Evita la quadrata molto larga.</td></tr>
<tr><td><strong>Sottile e morbida</strong></td><td>Si piega e si sfalda.</td><td>Si danneggia facilmente in limatura e rimozione.</td><td>Limatura minima. Base flessibile (rubber o builder). Lunghezza contenuta. Rimozione sempre delicata.</td></tr>
<tr><td><strong>Grassa</strong></td><td>Lamina lucida, sebo abbondante.</td><td>Il gel si ritira e si solleva.</td><td>Disidratante e primer adatti al sistema. Sgrassa di nuovo subito prima della base. Non toccare la lamina dopo.</td></tr>
<tr><td><strong>Molto curva (a tubo)</strong></td><td>Dalla punta la C è quasi un mezzo cerchio.</td><td>La cartina fatica ad aderire ai lati.</td><td>Rifila la cartina ai lati, curva a C che segue quella naturale, niente pinching aggiuntivo.</td></tr>
</table>
${F("cucchiaio-livellamento.svg", "Unghia a cucchiaio vista dalla punta: prima livelli la conca, poi costruisci.")}
<h2>Unghia a cucchiaio: attenzione alla salute</h2>
<p>La coilonichia può avere molte cause. La carenza di ferro (anemia) è tra le più note e più comuni; altre sono malattie della pelle come la psoriasi, problemi della tiroide, micosi, traumi ripetuti o il contatto frequente con solventi. Nei bambini piccoli può essere normale e scomparire con la crescita.</p>
${B("warn", "Comparsa recente? Medico", "Se la forma a cucchiaio è comparsa da poco, o la cliente è stanca e pallida, consiglia un controllo dal medico. Tu non fai diagnosi: segnali solo che vale la pena controllare.")}
${F("ski-jump-correzione.svg", "Ski-jump di profilo: a sinistra l'errore, al centro dove accorciare, a destra la correzione con cartina inclinata e zona 2 più piena.")}
<h2>Ski-jump: perché si accorcia prima</h2>
<p>Se lasci il bordo naturale che sale, il tip o la cartina si appoggiano a quella salita e la seguono. Accorciando fino al punto in cui la lamina è ancora dritta, appoggi l'allungamento su una base in asse con il dito.</p>
<ol class="steps">
<li>Accorcia la lamina fino all'inizio della salita.</li>
<li>Posiziona la cartina in asse con il dito, con una leggera inclinazione verso il basso.</li>
<li>Costruisci con un po' più di prodotto in zona 2: di profilo la linea superiore deve risultare dritta o leggermente arcuata.</li>
<li>Controlla di profilo a ogni refill: l'unghia tende a tornare a salire.</li>
</ol>
<h2>La regola dell'apex</h2>
${B("tip", "Regola sull'apex", "Più l'allungamento è lungo, più l'apex si sposta verso la cuticola, ma senza creare una gobba. Un apex troppo avanti fa piegare il bordo libero verso il basso e lo indebolisce.")}
<h2>Errori frequenti</h2>
<ul>
<li>Seguire la conca del cucchiaio con la cartina.</li>
<li>Fare pinching su un'unghia a pinza "per dare la C".</li>
<li>Costruire su ski-jump senza accorciare.</li>
<li>Guardare solo dall'alto e non di profilo o dalla punta.</li>
<li>Limare a fondo una lamina sottile per "farla aderire meglio".</li>
</ul>
`,
          sources: ['https://dermnetnz.org/cases/what-can-cause-these-flattened-nails', 'https://www.healthline.com/health/spoon-nails-koilonychia',
            'https://en.wikipedia.org/wiki/Pincer_nail',
            'https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-fit-nail-forms-to-different-nail-shapes']
        }
      ]
    },
    /* ------------------------------------------------------------------ 14 */
    {
      id: 'cover-colori', n: 14, level: 'inter', title: 'Cover, camouflage e gel colorati',
      summary: ['Il gel cover (camouflage) è un costruttore color pelle: allunga otticamente il letto e copre piccole imperfezioni.', 'Il cover deve essere coprente: controlla controluce che non ci siano "finestre"; gli angoli della smile line devono appoggiarsi al cover.', 'Colore = tinta + luminosità + saturazione; colori opposti sul cerchio si neutralizzano (viola ↔ giallo).', 'Sottotono freddo → rosa; caldo → pesca/nude caldo; neutro → beige (indicazione pratica): scegli alla luce naturale.', 'Gel pigmentati: strati sottili, perché il pigmento fa "ombrello" alla luce; rossi e neri sono i più difficili.', 'Colore e cover a circa 1 mm dalla pelle; sotto rossi e arancio la base è d\'obbligo.'],
      desc: 'Allungare otticamente il letto, scegliere il nude giusto, lavorare i gel colorati e consigliare la cliente sul colore.',
      lessons: [
        {
          id: 'cover', title: 'Gel cover e allungamento ottico del letto', min: 15,
          simple: 'Il cover è un gel color pelle. Lo stendi un po\' oltre il letto naturale e l\'unghia sembra più lunga, con le dita più slanciate.',
          videos: [{ id: 'ZuU5bu30h5w', title: 'Allungamento del letto ungueale con cover gel UV', channel: 'TheArtisticnail', lang: 'IT' },
            { id: 'yEfVHzpPlwY', title: 'Ricostruzione e refill con cover costruttori', channel: 'Elena Santucci', lang: 'IT' }],
          html: `
${F("cover-letto.svg", "Il cover prolunga visivamente il letto ungueale.")}
<p>Il gel <strong>cover</strong> (detto anche make-up, camouflage o "cover pink") è un gel costruttore con pigmenti color pelle: rosa, nude, pesca, beige. Si usa per due scopi:</p>
<ul>
<li><strong>Allungare otticamente il letto ungueale</strong>: la parte "rosa" dell'unghia sembra più lunga e la mano più elegante.</li>
<li><strong>Uniformare</strong> piccole imperfezioni estetiche della lamina sana, come macchioline bianche o un colore non omogeneo.</li>
</ul>
${B("info", "Attenzione al termine", "In questo corso «allungamento del letto ungueale» indica solo l'effetto estetico ottenuto con il cover sopra un allungamento (tip o cartina). Non si interviene sul letto naturale.")}
<h2>Cover, rosa trasparente, correttore: le differenze</h2>
<table>
<tr><th>Prodotto</th><th>Come appare</th><th>Quando si usa</th></tr>
<tr><td><strong>Cover coprente</strong></td><td>Opaco, color pelle, non lascia vedere sotto</td><td>Letto allungato, unghie rosicchiate, camouflage</td></tr>
<tr><td><strong>Rosa / clear trasparente</strong></td><td>Lascia vedere il letto naturale e la sua linea</td><td>Ricostruzioni "naturali" quando il letto è già lungo</td></tr>
<tr><td><strong>Smalto o gel "effetto correttore"</strong></td><td>Lattiginoso, semitrasparente</td><td>Attenuare piccole discromie, non allunga il letto</td></tr>
</table>
<h2>Perché il cover deve essere coprente</h2>
<p>Se il cover lascia trasparire la lamina, si vede ancora dove finisce il letto naturale e l'effetto sparisce. Molti rosa venduti come "coprenti" non lo sono abbastanza. Nei forum professionali i tecnici lo segnalano spesso: un rosa velato non copre un letto corto, serve un rosa davvero non trasparente.</p>
${F("cover-controluce.svg", "Prova controluce: cover uniforme (giusto), cover con «finestre» e french con «orecchie» trasparenti ai lati (sbagliati).")}
<h2>Procedura passo per passo</h2>
${F("cover-step.svg", "French con letto allungato in cover: sei passaggi.")}
<ol class="steps">
<li><strong>Prepara e allunga</strong> con tip o cartina, come nei moduli precedenti. Su cartina, molti formatori stendono prima un velo sottile di trasparente sulla giunzione tra unghia e cartina: fa da "ponte" stabile.</li>
<li><strong>Scegli la lunghezza del letto</strong>. Guarda la mano intera: il letto allungato deve essere proporzionato al dito. Le dita tra loro devono avere letti simili per lunghezza.</li>
<li><strong>Stendi il cover</strong> dalla zona cuticolare, lasciando un margine di circa 1 mm dalla pelle, fino alla nuova lunghezza di letto. Due strati sottili sono meglio di uno spesso: coprono di più e polimerizzano bene.</li>
<li><strong>Controlla controluce</strong> dopo ogni strato. Se vedi zone più chiare, aggiungi un velo solo lì.</li>
<li><strong>Smile line</strong>. Per un french disegni il bianco <strong>dopo</strong> il cover, appoggiato al bordo del cover. Segna prima il punto centrale, poi i due angoli, poi unisci e arrotonda.</li>
<li><strong>Struttura e finitura</strong>: un velo di builder trasparente su tutta l'unghia con l'apex, poi limatura e top.</li>
</ol>
${F("cover-sezione.svg", "L'unghia in sezione: lamina, base, cover, bianco, builder trasparente con apex, top.")}
<h2>Gli angoli della smile line</h2>
<p>Il bianco deve appoggiarsi al cover lungo tutta la smile line, angoli compresi. Se gli angoli restano troppo "alti", cioè troppo verso la punta, tra il bianco e il cover restano due piccole zone trasparenti ai lati, chiamate a volte <strong>"orecchie"</strong>: controluce si vedono subito. Per evitarle, <strong>abbassa leggermente gli angoli della smile line</strong> fino a toccare il cover, oppure porta il cover fino al bordo laterale.</p>
${B("tip", "Cover denso o fluido?", "I cover più densi (che non si autolivellano) restano dove li appoggi: aiutano a costruire la curva a C e non colano nei solchi laterali. Sono più facili per chi inizia.")}
<h2>Il cover nel refill</h2>
<ul>
<li>Con la ricrescita, tra la cuticola e il vecchio cover si vede una fascia di unghia naturale.</li>
<li>Assottiglia il vecchio prodotto, poi stendi il cover nuovo nella zona di ricrescita, sfumandolo sul vecchio senza scalini.</li>
<li>Se il letto naturale si è allungato (per esempio dopo l'onicofagia), accorcia di conseguenza il cover.</li>
</ul>
<h2>Errori frequenti</h2>
<table>
<tr><th>Errore</th><th>Cosa si vede</th><th>Correzione</th></tr>
<tr><td>Cover troppo trasparente</td><td>Si vede la linea del letto naturale</td><td>Cover più coprente, due strati sottili</td></tr>
<tr><td>Strato unico spesso</td><td>Parte profonda poco polimerizzata, calore in lampada</td><td>Strati sottili, ognuno polimerizzato</td></tr>
<tr><td>Letto troppo lungo</td><td>Unghia sproporzionata, bordo libero cortissimo</td><td>Proporzione con il dito; guarda tutta la mano</td></tr>
<tr><td>Colore sbagliato</td><td>Il cover "stacca" dalla pelle (troppo rosa o troppo giallo)</td><td>Scegli alla luce naturale (lezione successiva)</td></tr>
<tr><td>Cover sulla pelle</td><td>Lifting e rischio di allergia</td><td>Margine di circa 1 mm dalla cuticola e dai solchi</td></tr>
</table>
`,
          sources: ['https://www.scratchmagazine.co.uk/nail_art/classic-french-manicure-using-gel',
            'https://www.scratchmagazine.co.uk/feature/how-to-ace-encapsulation-in-lp-gel-nails',
            'https://www.salongeek.com/threads/camouflage-gel.60825/',
            'https://www.irishbeauty.ie/New-Cover-Gel-launched-by-Crystal-Nails.html',
            'https://www.my-personaltrainer.it/bellezza/unghie-effetto-correttore-il-trend-concealer-nails-del-2026-per-una-manicure-naturale-e-perfetta.html']
        },
        {
          id: 'colori', title: 'Teoria del colore e scelta del nude', min: 14,
          simple: 'Il nude giusto è quello che sull\'unghia "sparisce" e sembra il proseguimento del tuo letto naturale. Per trovarlo guardi il sottotono della pelle, alla luce del giorno.',
          html: `
<p>Per scegliere un cover, un nude o un colore che valorizzi la mano non basta il gusto personale. Servono poche regole di teoria del colore. Le stesse regole le usano truccatori e parrucchieri.</p>
${F("colori-proprieta.svg", "Le tre proprietà del colore: tinta, luminosità, saturazione.")}
<h2>Le tre proprietà di un colore</h2>
<table>
<tr><th>Proprietà</th><th>Cosa vuol dire</th><th>Esempio sulle unghie</th></tr>
<tr><td><strong>Tinta</strong></td><td>Il "nome" del colore: rosso, giallo, blu…</td><td>Un nude rosato e un nude pesca hanno tinte diverse.</td></tr>
<tr><td><strong>Luminosità</strong> (valore)</td><td>Quanto è chiaro o scuro.</td><td>Un beige chiaro su pelle scura "stacca" molto.</td></tr>
<tr><td><strong>Saturazione</strong></td><td>Quanto è intenso o spento (grigio).</td><td>Un rosa acceso è saturo; un rosa antico è poco saturo.</td></tr>
</table>
${F("colori-sottotono.svg", "Cerchio cromatico e scelta del cover.")}
<h2>Il cerchio cromatico</h2>
<ul>
<li><strong>Primari</strong> (nel cerchio tradizionale dei pittori): rosso, giallo, blu.</li>
<li><strong>Secondari</strong>: arancio, verde, viola. Nascono mescolando due primari.</li>
<li><strong>Complementari</strong>: stanno uno di fronte all'altro (rosso/verde, blu/arancio, giallo/viola). Accostati si fanno risaltare a vicenda. Mescolati o sovrapposti in poca quantità <strong>si neutralizzano</strong>.</li>
<li><strong>Analoghi</strong>: colori vicini sul cerchio (per esempio rosa, corallo, pesca). Accostati danno un effetto armonioso, utile per ombré delicati.</li>
</ul>
${B("info", "Perché il viola «toglie» il giallo", "È lo stesso principio dei correttori del trucco: un pigmento leggermente violaceo rende meno evidente un tono giallastro. Per questo alcuni top e smalti «anti-giallo» hanno un velo lilla.")}
<h2>Il sottotono della pelle</h2>
<p>Il <strong>tono</strong> è quanto la pelle è chiara o scura. Il <strong>sottotono</strong> è il riflesso di colore sotto la superficie: freddo (rosato), caldo (dorato) o neutro. Due persone con la stessa pelle chiara possono avere sottotoni diversi.</p>
${F("sottotono-test.svg", "Tre test pratici per capire il sottotono: vene, foglio bianco, gioielli.")}
<ol class="steps">
<li><strong>Test delle vene</strong>: guarda l'interno del polso alla luce del giorno. Vene bluastre o violacee fanno pensare a un sottotono freddo; verdastre a uno caldo; difficili da dire a uno neutro.</li>
<li><strong>Test del foglio bianco</strong>: accosta un foglio bianco alla mano. Se la pelle sembra rosata è più fredda; se sembra gialla o dorata è più calda.</li>
<li><strong>Test dei gioielli</strong>: se all'argento la pelle "si accende" è più fredda; con l'oro è più calda; se vanno bene entrambi è neutra.</li>
</ol>
${B("warn", "Test indicativi", "Questi test sono indicazioni pratiche, non misure. A volte danno risultati diversi tra loro, e il sottotono «olivastro» non rientra bene in nessuna casella. Usali per orientarti, poi decidi provando il colore vero sull'unghia.")}
<h2>Scegliere il cover (indicazione pratica)</h2>
<table>
<tr><th>Sottotono</th><th>Come appare</th><th>Cover di partenza</th></tr>
<tr><td><strong>Freddo</strong></td><td>Riflessi rosati, vene bluastre</td><td>Rosa o rosa-beige</td></tr>
<tr><td><strong>Caldo</strong></td><td>Riflessi dorati o olivastri, vene verdastre</td><td>Pesca o nude caldo</td></tr>
<tr><td><strong>Neutro</strong></td><td>Via di mezzo</td><td>Nude beige</td></tr>
<tr><td><strong>Pelle scura</strong></td><td>Tono profondo, sottotono variabile</td><td>Nude più scuri (caramello, cacao); un rosa chiaro può sembrare "gessoso"</td></tr>
</table>
${F("nude-prova-tip.svg", "La prova del tip: campioni appoggiati all'unghia, alla luce naturale.")}
<h2>La prova pratica: il metodo più sicuro</h2>
<ol class="steps">
<li>Prepara una piccola <strong>cartella di tip</strong> colorati con i tuoi cover, ognuno con nome e numero scritti dietro.</li>
<li>Avvicinati a una finestra: la <strong>luce naturale</strong> mostra i colori com'erano pensati. Le lampade da tavolo spesso sono troppo calde o troppo fredde.</li>
<li>Appoggia 2–3 tip <strong>sopra l'unghia</strong> della cliente, accanto al letto naturale.</li>
<li>Scegli quello che "sparisce": il passaggio tra letto naturale e tip non si deve notare. Confronta con il letto ungueale, non con il dorso della mano.</li>
<li>Annota il colore scelto nella scheda cliente: al refill lo ritrovi subito.</li>
</ol>
<h2>Errori frequenti</h2>
<ul>
<li>Scegliere il colore sotto la lampada da lavoro.</li>
<li>Confrontare con il dorso della mano invece che con il letto ungueale.</li>
<li>Usare un solo cover per tutte le clienti.</li>
<li>Fidarsi solo del colore nel vasetto: steso sottile appare diverso.</li>
</ul>
`,
          sources: ['https://www.masterclass.com/articles/how-to-identify-your-skins-undertone',
            'https://makeup.com/product-and-reviews/foundation/identifying-your-skins-undertone',
            'https://www.my-personaltrainer.it/bellezza/unghie-effetto-correttore-il-trend-concealer-nails-del-2026-per-una-manicure-naturale-e-perfetta.html']
        },
        {
          id: 'gel-colorati', title: 'Gel colorati, pigmenti e polimerizzazione', min: 13,
          simple: 'Più un gel è colorato, più "blocca" la luce della lampada. Per questo va steso a strati sottili, ognuno indurito bene.',
          html: `
<p>Ogni gel colorato contiene <strong>pigmenti</strong>: particelle che danno il colore. I pigmenti sono bellissimi, ma cambiano il modo in cui il gel si indurisce sotto la lampada. Capire questo ti evita colori che si staccano, si raggrinziscono o danno fastidio alla pelle.</p>
<h2>I tipi di prodotto colorato</h2>
<table>
<tr><th>Prodotto</th><th>Consistenza</th><th>Cosa fa</th></tr>
<tr><td><strong>Gel colorato da costruzione</strong></td><td>Denso</td><td>Dà colore e anche struttura (si può costruire l'apex)</td></tr>
<tr><td><strong>Semipermanente</strong> (gel polish)</td><td>Fluido</td><td>Solo colore, in strati sottili sopra la base; nessuna struttura</td></tr>
<tr><td><strong>Gel da pittura / nail art</strong></td><td>Cremoso, molto pigmentato</td><td>Linee e decorazioni; non cola</td></tr>
</table>
${F("colori-finiture.svg", "Le finiture dei colori: coprente, jelly, shimmer, glitter, magnetico.")}
<h2>Le finiture</h2>
<ul>
<li><strong>Coprente</strong> (crema): molto pigmento, copre in 1–2 strati.</li>
<li><strong>Jelly</strong> (traslucido): lascia vedere sotto, effetto "caramella". Più strati = colore più intenso.</li>
<li><strong>Shimmer / perlato</strong>: piccole particelle riflettenti.</li>
<li><strong>Glitter</strong>: particelle grandi, spesso in base trasparente.</li>
<li><strong>Magnetico</strong> (cat-eye): particelle metalliche che si orientano con un magnete (modulo Nail art avanzata).</li>
</ul>
${F("pigmenti-luce.svg", "Effetto ombrello: in uno strato sottile la luce arriva in fondo, in uno spesso e pigmentato no.")}
<h2>Pigmenti e lampada: l'«effetto ombrello»</h2>
<p>Il gel indurisce grazie ai <strong>fotoiniziatori</strong>, che "si accendono" con la luce UV o LED. Anche i pigmenti però assorbono quella luce e fanno ombra agli strati sotto: un divulgatore della chimica delle unghie (Doug Schoon) lo chiama "effetto ombrello".</p>
<ul>
<li>Più pigmento = meno luce arriva in profondità.</li>
<li>I pigmenti <strong>rossi e neri</strong> assorbono la luce più dei colori chiari come il bianco o il blu: sono i più "difficili".</li>
<li>Anche lo <strong>spessore</strong> conta: in uno strato spesso la parte in alto assorbe la luce e quella in fondo resta poco polimerizzata, anche senza pigmenti.</li>
</ul>
${B("warn", "Strati sottili prima di tutto", "Con un gel molto pigmentato le fonti consigliano strati sottili e, se la scheda tecnica lo prevede, un tempo di lampada più lungo. Un tempo più lungo però non «salva» uno strato troppo spesso: la luce comunque non arriva in fondo. Lo strato sotto resta morbido, il colore si raggrinzisce o si stacca, e il gel non polimerizzato può dare allergia se tocca la pelle.")}
${F("colore-strati-step.svg", "Stendere il colore: mescola, base, primo strato sottile, sigilla la punta, secondo strato e top.")}
<h2>Procedura: colore in gel a regola d'arte</h2>
<ol class="steps">
<li><strong>Mescola il colore</strong>. Gira il vasetto o rotola la boccetta tra le mani: il pigmento tende a depositarsi sul fondo. Non agitare forte, si formano bolle.</li>
<li><strong>Base</strong> sottile e lampada come da scheda tecnica.</li>
<li><strong>Primo strato sottile</strong> di colore, lasciando un margine di circa 1 mm dalla cuticola e dai lati. È normale che sia un po' striato.</li>
<li><strong>Sigilla il bordo libero</strong>: passa il pennello anche sullo spessore della punta. Così il colore non si ritira e non si scheggia.</li>
<li><strong>Lampada</strong> per il tempo indicato, con la lampada del sistema.</li>
<li><strong>Secondo strato sottile</strong>: uniforma il colore. Sigilla di nuovo la punta. Lampada.</li>
<li><strong>Top</strong> e lampada; togli lo strato di dispersione se il top lo prevede.</li>
</ol>
${B("tip", "Rossi e arancio: la base è d'obbligo", "I dermatologi americani consigliano uno strato in più di base sotto smalti rossi o arancio: proteggono la lamina dall'ingiallimento. Se la lamina si macchia, di solito torna normale in qualche settimana senza quel colore.")}
<h2>Problemi comuni</h2>
<table>
<tr><th>Problema</th><th>Causa probabile</th><th>Cosa fare</th></tr>
<tr><td>Striature</td><td>Normale al primo strato di molti colori (soprattutto bianco e pastello)</td><td>Il secondo strato sottile uniforma</td></tr>
<tr><td>Ritiro dai bordi</td><td>Olio sulla lamina, primer ancora umido sui lati, lampada non compatibile</td><td>Sgrassa, lascia asciugare, usa la lampada del sistema</td></tr>
<tr><td>Grinze sulla superficie</td><td>Strato troppo spesso: sopra duro, sotto molle</td><td>Strati sottili; rimuovi e rifai</td></tr>
<tr><td>Colore non uniforme</td><td>Spessori irregolari, pigmento non rimescolato</td><td>Mescola il vasetto, strati uniformi</td></tr>
<tr><td>Macchie sulla pelle o sulle cuticole</td><td>Colore steso troppo vicino</td><td>Togli con un bastoncino prima della lampada; margine di circa 1 mm dalla pelle</td></tr>
<tr><td>Calore in lampada</td><td>Strato spesso, molto pigmentato</td><td>Strati sottili; se brucia, mano fuori qualche secondo (flash and pull)</td></tr>
</table>
`,
          sources: ['https://nailknowledge.org/blog/mastering-uv-gel-application-insights-into-pigments',
            'https://nailknowledge.org/blog/unveiling-the-hazards-of-thick-uv-gel-application',
            'https://aad.org/nail-care-secrets/manicure-pedicure-safety',
            'https://pinkgellac.com/blogs/news/how-to-use-cat-eye-gel-polish']
        },
        {
          id: 'consulenza-colore', title: 'Consulenza colore e cartella campioni', min: 10,
          simple: 'Una buona cartella di campioni e due o tre domande alla cliente ti fanno scegliere il colore giusto in pochi minuti.',
          html: `
<p>La scelta del colore è uno dei momenti più importanti dell'appuntamento. Una cliente soddisfatta del colore torna; una cliente indecisa perde tempo e spesso resta delusa. Con una cartella ordinata e poche domande diventa facile.</p>
${F("cartella-colori.svg", "Una cartella colori ordinata: per famiglie, dal chiaro allo scuro, con marca, nome e numero sul retro.")}
<h2>Costruire la cartella campioni</h2>
<ol class="steps">
<li><strong>Un tip per colore</strong>, stesso tipo di tip per tutti, con la stessa forma.</li>
<li><strong>Stendi come in cabina</strong>: base, due strati sottili, top. Così il campione è fedele al risultato vero.</li>
<li><strong>Scrivi dietro</strong> marca, nome e numero del colore.</li>
<li><strong>Ordina per famiglie</strong>: nude e cover, rosa, rossi, viola, blu, verdi, neutri scuri, glitter ed effetti.</li>
<li><strong>Dentro ogni famiglia</strong> ordina dal più chiaro al più scuro.</li>
<li><strong>Aggiorna</strong> quando compri un colore nuovo; togli quelli fuori produzione.</li>
</ol>
<h2>Le domande da fare</h2>
<ul>
<li>"Per quale occasione?" (lavoro, cerimonia, vacanza)</li>
<li>"Preferisci un effetto naturale o un colore che si nota?"</li>
<li>"Che lavoro fai?" (in alcuni lavori servono unghie corte e colori discreti)</li>
<li>"Che colori porti di solito? Ce n'è uno che non ti piace su di te?"</li>
</ul>
${F("armonie-colore.svg", "Abbinamenti facili: monocromatico, analoghi, complementari, neutro più accento.")}
<h2>Abbinamenti facili per nail art</h2>
<table>
<tr><th>Abbinamento</th><th>Come si costruisce</th><th>Effetto</th></tr>
<tr><td><strong>Monocromatico</strong></td><td>Lo stesso colore in più luminosità (chiaro, medio, scuro)</td><td>Elegante, sicuro</td></tr>
<tr><td><strong>Analoghi</strong></td><td>Colori vicini sul cerchio (rosa, corallo, pesca)</td><td>Armonioso, ideale per ombré</td></tr>
<tr><td><strong>Complementari</strong></td><td>Colori opposti (blu e arancio)</td><td>Forte contrasto: meglio un colore dominante e l'altro come dettaglio</td></tr>
<tr><td><strong>Neutro + accento</strong></td><td>Nude su quasi tutte le unghie, un colore acceso o un effetto su una</td><td>Moderno, adatto a chi ha dubbi</td></tr>
</table>
${B("tip", "Mostra, non descrivere", "Invece di chiedere «rosso o bordeaux?», appoggia due tip sull'unghia della cliente alla luce naturale. Decide in pochi secondi.")}
${B("info", "Colore e lavoro", "In ambienti sanitari e alimentari spesso valgono regole interne su unghie artificiali e smalto. Chiedi sempre alla cliente: non è un tuo giudizio, è un'informazione che le serve.")}
<h2>Errori frequenti</h2>
<ul>
<li>Cartella con campioni sbiaditi o graffiati.</li>
<li>Campioni stesi diversamente da come lavori: il risultato non coincide.</li>
<li>Proporre troppi colori insieme: la cliente si confonde. Meglio 3–4 proposte mirate.</li>
</ul>
`,
          sources: ['https://www.masterclass.com/articles/how-to-identify-your-skins-undertone',
            'https://www.youngnails.com/blogs/news/how-to-do-ombre-gel-polish-nails']
        }
      ]
    },
    /* ------------------------------------------------------------------ 15 */
    {
      id: 'piedi', n: 15, level: 'inter', title: 'Pedicure e piedi',
      summary: ['Le unghie dei piedi crescono a meno della metà della velocità di quelle delle mani (≈1,6 contro ≈3,5 mm al mese); un alluce si rinnova in 12–18 mesi.', 'Taglio dritto, non troppo corto, angoli appena smussati con la lima: previene l\'unghia incarnita.', 'Mai coprire un\'unghia con sospetta micosi: medico o podologo.', 'Cliente diabetica con ferite, infezioni o perdita di sensibilità: niente servizio, invio al podologo o al medico.', 'Pediluvio: dopo ogni cliente pulizia + disinfettante attivo anche su funghi per il tempo di contatto (es. 10 minuti nelle norme della California) + registro.', 'Unghie incarnite, ispessite, deformi, calli: competenza del podologo (DM 666/1994).'],
      desc: 'Semipermanente e piccoli ripristini sui piedi, igiene, controindicazioni e limiti.',
      lessons: [
        {
          id: 'piedi-differenze', title: 'Unghie dei piedi: differenze e taglio', min: 12,
          simple: 'Sui piedi l\'unghia cresce piano, è più spessa e viene schiacciata dalle scarpe. Si taglia dritta e non troppo corta, così non entra nella pelle.',
          videos: /* invariato */ [{ id: 'RoFFFE8Nbec', title: 'Tutorial semipermanente piedi', channel: 'Aerrenails', lang: 'IT' },
            { id: '2NuJhMyN4VI', title: 'Semipermanente ai piedi: tutti i passaggi', channel: 'Deby Cannavò', lang: 'IT' }],
          html: `
<p>Le unghie dei piedi sono fatte come quelle delle mani: matrice, lamina, letto, cuticola, iponichio. Però vivono in condizioni molto diverse: dentro la scarpa, al caldo e all'umido, sotto il peso del corpo. Per questo cambiano sia il taglio sia i servizi che puoi offrire.</p>
${F("piede-unghia-anatomia.svg", "L'unghia dell'alluce: più spessa, più curva, con solchi laterali profondi.")}
<h2>Le differenze principali</h2>
<table>
<tr><th></th><th>Mani</th><th>Piedi</th></tr>
<tr><td>Crescita media</td><td>≈ 3,5 mm al mese</td><td>≈ 1,6 mm al mese (meno della metà)</td></tr>
<tr><td>Tempo per rinnovare tutta l'unghia</td><td>≈ 4–6 mesi</td><td>Alluce: fino a 12–18 mesi</td></tr>
<tr><td>Lamina</td><td>Più sottile e flessibile</td><td>Più spessa e spesso più curva, soprattutto sull'alluce</td></tr>
<tr><td>Solchi laterali</td><td>Poco profondi</td><td>Profondi: gli angoli possono "entrare" nella pelle</td></tr>
<tr><td>Ambiente</td><td>Aria, acqua, detersivi</td><td>Scarpa chiusa, caldo, sudore: ideale per i funghi</td></tr>
<tr><td>Forze</td><td>Urti, leve</td><td>Pressione della scarpa e del peso, traumi ripetuti</td></tr>
</table>
<p>I dati di crescita vengono da uno studio su giovani adulti (3,47 mm/mese mani, 1,62 mm/mese piedi). Con l'età, in inverno e con alcune malattie la crescita rallenta. Un effetto pratico: il <strong>semipermanente sui piedi dura di più</strong> che sulle mani, perché la ricrescita si nota più tardi.</p>
${F("piede-taglio.svg", "Taglio corretto e velocità di crescita.")}
<h2>Il taglio corretto</h2>
<p>I dermatologi e i diabetologi danno la stessa indicazione: <strong>taglio dritto</strong>. Gli angoli si smussano appena con la lima, non si arrotondano con le forbici e non si scavano.</p>
${F("piede-taglio-step.svg", "Taglio passo per passo: ammorbidisci, taglia dritto a piccoli colpi, lima gli angoli, controlla la lunghezza.")}
<ol class="steps">
<li><strong>Ammorbidisci</strong>: l'unghia del piede è dura. Si taglia meglio dopo un pediluvio tiepido di pochi minuti o subito dopo la doccia.</li>
<li><strong>Usa lo strumento giusto</strong>: tronchesino da piedi (tagliaunghie a lama dritta), sterilizzato. Per le persone con diabete è consigliato un tronchesino a punte arrotondate.</li>
<li><strong>Taglia dritto a piccoli colpi</strong>, partendo da un lato e procedendo verso l'altro. Un solo colpo largo può spaccare la lamina spessa.</li>
<li><strong>Lunghezza</strong>: a filo della punta del dito. Né oltre (urta nella scarpa) né più corta (il polpastrello spinge la pelle sopra l'angolo).</li>
<li><strong>Lima gli angoli</strong> appena, in una sola direzione, per togliere le punte che pungono.</li>
<li><strong>Controlla</strong>: nessuno spigolo, nessun frammento nei solchi laterali.</li>
</ol>
${B("danger", "Non scavare i lati", "Scavare negli angoli o tagliarli «a V» lascia uno spuntone di unghia dentro il solco. Crescendo, lo spuntone entra nella pelle: è il modo più comune per creare un'unghia incarnita. Un angolo già dolente, arrossato o gonfio non si tocca: è competenza del podologo.")}
${F("scarpa-pressione.svg", "La scarpa conta: punta stretta (pressione sugli angoli) e punta comoda.")}
<h2>Perché le unghie si incarniscono</h2>
<ul>
<li><strong>Taglio sbagliato</strong>: troppo corto, arrotondato o scavato ai lati.</li>
<li><strong>Scarpe strette</strong> in punta, o tacchi che spingono il piede in avanti.</li>
<li><strong>Traumi</strong>: urti, sport, unghia schiacciata.</li>
<li><strong>Forma dell'unghia</strong>: unghie molto curve o a pinza.</li>
</ul>
<p>Puoi dare consigli di prevenzione (taglio, scarpe comode). Il trattamento di un'unghia incarnita spetta al podologo o al medico.</p>
<h2>Cuticole dei piedi</h2>
<p>Come per le mani, la cuticola si arretra <strong>delicatamente</strong>, dopo averla ammorbidita. Si toglie solo la pelle morta sulla lamina. L'Accademia americana di dermatologia sconsiglia di tagliare le cuticole o di spingerle con forza: la cuticola è una barriera contro i germi.</p>
<h2>Errori frequenti</h2>
<ul>
<li>Tagliare l'alluce corto "così dura di più".</li>
<li>Arrotondare gli angoli con le forbici come sulle mani.</li>
<li>Tagliare l'unghia asciutta e dura in un unico colpo.</li>
<li>Usare lo stesso tronchesino per più clienti senza sterilizzarlo.</li>
</ul>
        `,
          sources: ['https://bionumbers.hms.harvard.edu/bionumber.aspx?id=112380',
            'https://www.aad.org/public/everyday-care/nail-care-secrets/basics/how-to-trim-nails',
            'https://aad.org/nail-care-secrets/manicure-pedicure-safety',
            'https://www.healthline.com/health/how-long-does-it-take-for-a-toenail-to-grow-back',
            'https://www.quotidianosanita.it/scienza-e-farmaci/piede-diabetico-ecco-il-decalogo-della-sid-per-prevenirlo/']
        },
        {
          id: 'piedi-igiene', title: 'Igiene, micosi e piede diabetico', min: 16,
          simple: 'Sui piedi i funghi sono comuni: se l\'unghia sembra malata non si copre, si consiglia il medico o il podologo. Il pediluvio va disinfettato dopo ogni cliente. Con una cliente diabetica serve doppia attenzione.',
          html: `
<p>La pedicure è il servizio in cui l'igiene conta di più. I piedi stanno al caldo e all'umido, le micosi sono frequenti, e alcune clienti (per esempio le persone con diabete) rischiano complicazioni serie anche per un piccolo taglio.</p>
<h2>Micosi delle unghie e piede d'atleta</h2>
<ul>
<li>L'<strong>onicomicosi</strong> è l'infezione dell'unghia da funghi. Gli studi danno numeri diversi a seconda di come sono fatti. Nelle indagini sulla popolazione generale la frequenza va da circa il 2% all'8% (media intorno al 5,5%). Alcune stime arrivano al 10–12%. È più frequente con l'età, negli uomini, in chi fa sport, nelle persone con diabete o con difese immunitarie basse.</li>
<li>Colpisce soprattutto le <strong>unghie dei piedi</strong>. I funghi più comuni sono i dermatofiti, in particolare <em>Trichophyton rubrum</em>.</li>
<li>Circa <strong>un terzo</strong> delle persone con onicomicosi ha anche il <strong>piede d'atleta</strong> (tinea pedis): pelle che si squama, prude o si spacca tra le dita. L'unghia infetta fa da "serbatoio" e può reinfettare la pelle.</li>
<li>Tra i fattori di rischio le fonti dermatologiche citano anche le visite nei saloni di unghie, quando l'igiene non è corretta.</li>
</ul>
${F("piede-segnali-stop.svg", "Segnali di STOP: quando non si lavora e si consiglia medico o podologo.")}
<h2>Segnali di STOP</h2>
<table>
<tr><th>Cosa vedi</th><th>Che cosa potrebbe essere</th><th>Cosa fai</th></tr>
<tr><td>Unghia gialla, marrone o bianca, ispessita, friabile, sollevata</td><td>Possibile micosi</td><td>Niente gel o semipermanente. Consiglia medico o podologo.</td></tr>
<tr><td>Pelle squamosa, arrossata o spaccata tra le dita</td><td>Possibile piede d'atleta</td><td>Rimanda; consiglia il medico.</td></tr>
<tr><td>Angolo dell'unghia rosso, gonfio, dolente</td><td>Unghia incarnita, infezione</td><td>Non toccare; podologo o medico.</td></tr>
<tr><td>Ferite, vesciche, ulcere, tagli</td><td>Porta d'ingresso per i germi</td><td>Niente servizio.</td></tr>
<tr><td>Escrescenze ruvide sulla pianta o vicino all'unghia</td><td>Possibile verruca</td><td>Non limare (si diffonde); medico.</td></tr>
<tr><td>Unghia molto spessa e deformata, "a corno"</td><td>Unghia ipertrofica</td><td>Podologo.</td></tr>
</table>
${B("danger", "Regola", "Mai coprire con gel o semipermanente un'unghia con sospetta micosi (gialla o bianca, ispessita, friabile, sollevata). Sospendi il servizio e consiglia medico o podologo. Coprirla non la cura, nasconde il problema e contamina gli strumenti.")}
${B("info", "Cosa dire alla cliente", "«Vedo un cambiamento nel colore e nello spessore dell'unghia. Non posso dirti cosa sia, ma è meglio farlo vedere al medico o al podologo prima di coprirla. Appena ti dà il via libera, ti aspetto.» Chiaro, gentile, senza diagnosi.")}
<h2>Il pediluvio: dove si nascondono i germi</h2>
<p>Nel 2000, in California, oltre 100 clienti di uno stesso salone hanno sviluppato foruncoli alle gambe dopo la pedicure. Erano causati da un micobatterio (<em>Mycobacterium fortuitum</em>) cresciuto nelle tubature delle vasche idromassaggio. In una successiva indagine dei CDC i micobatteri sono stati trovati in 29 vasche su 30 controllate in 18 saloni. Per questo oggi si preferiscono vaschette semplici, senza tubature, o con fodere monouso.</p>
${F("pediluvio-disinfezione.svg", "Pulizia e disinfezione della vaschetta dopo ogni cliente, con il registro.")}
<h2>Pulizia e disinfezione dopo ogni cliente</h2>
<p>La sequenza qui sotto segue le regole del California Board of Barbering and Cosmetology, tra le più dettagliate disponibili. In Italia valgono le regole regionali e comunali e le istruzioni del disinfettante che usi: il principio però è lo stesso.</p>
<ol class="steps">
<li><strong>Svuota</strong> completamente la vaschetta.</li>
<li><strong>Pulisci</strong>: strofina tutte le superfici interne con spazzola pulita, sapone liquido e acqua, fino a togliere ogni residuo. Senza pulizia il disinfettante non funziona bene.</li>
<li><strong>Risciacqua</strong> con acqua pulita.</li>
<li><strong>Disinfetta</strong>: riempi con acqua e la dose giusta di un disinfettante attivo su batteri, funghi e virus (leggi l'etichetta). Lascialo agire per tutto il <strong>tempo di contatto</strong> indicato: in California almeno <strong>10 minuti</strong>.</li>
<li><strong>Svuota, risciacqua e asciuga</strong> con carta pulita monouso.</li>
<li><strong>Registra</strong>: data, ora, iniziali di chi ha fatto la disinfezione.</li>
</ol>
${B("tip", "Fodere monouso", "Le fodere usa e getta per vaschette si buttano dopo ogni cliente: non si lavano e non si riusano. La vaschetta sotto va comunque pulita.")}
<h2>Consigli alla cliente prima della pedicure</h2>
<ul>
<li><strong>Non radersi le gambe nelle 24 ore prima</strong>: i microtagli del rasoio sono porte d'ingresso per i germi. Lo raccomandano sia l'Accademia americana di dermatologia sia gli enti che controllano i saloni negli Stati Uniti. In uno studio, chi si era rasato prima della pedicure aveva più del doppio di probabilità di sviluppare i foruncoli da micobatteri.</li>
<li>Avvisare se ha diabete, problemi di circolazione, micosi in corso o recenti.</li>
</ul>
${F("piede-diabetico-regole.svg", "Cliente con diabete: cosa fare e cosa evitare.")}
<h2>La cliente con diabete</h2>
<p>Il diabete può ridurre la <strong>sensibilità</strong> dei piedi (neuropatia; in Italia ne soffre circa il 30% delle persone con diabete secondo la Società Italiana di Diabetologia) e la <strong>circolazione</strong>. Una persona può scottarsi senza accorgersene, e un piccolo taglio può guarire male e trasformarsi in un'ulcera.</p>
<table>
<tr><th>Fai</th><th>Evita</th></tr>
<tr><td>Chiedi in anamnesi se ha il diabete e se ha mai avuto ferite o ulcere ai piedi</td><td>Lavorare se ci sono ferite, ulcere, infezioni o perdita di sensibilità</td></tr>
<tr><td>Acqua <strong>tiepida</strong>, misurata con termometro o con il tuo gomito; un opuscolo ospedaliero indica circa 32–35 °C</td><td>Acqua calda; chiedere alla cliente se "va bene" (potrebbe non sentirla)</td></tr>
<tr><td>Pediluvio <strong>breve</strong></td><td>Pediluvi lunghi o con sali (la SID li sconsiglia)</td></tr>
<tr><td>Asciuga bene, soprattutto <strong>tra le dita</strong></td><td>Lasciare umido tra le dita</td></tr>
<tr><td>Taglio dritto, non troppo corto, lima sugli angoli</td><td>Tagliare cuticole, pellicine, calli; usare lame</td></tr>
<tr><td>Massaggio leggero, crema idratante (non tra le dita)</td><td>Pressione forte, raspe aggressive</td></tr>
<tr><td>Strumenti sterilizzati o monouso</td><td>Prodotti callifughi</td></tr>
</table>
${B("warn", "Il confine", "Gli esperti citati dalla stampa di settore sono d'accordo: una cliente con diabete può essere trattata in istituto se non ci sono infezioni, ulcere o neuropatia. Se ci sono, o se hai dubbi, il posto giusto è il podologo, che la SID raccomanda di informare sempre del diabete.")}
<h2>Segnali da riferire alla cliente</h2>
<p>Secondo Diabetes UK, una persona con diabete deve rivolgersi al medico se nota: formicolio o intorpidimento, bruciore, pelle lucida e liscia, perdita di peli su gambe e piedi, piedi gonfi, ferite che non guariscono, vesciche o tagli che si vedono ma non si sentono. Tu non diagnostichi: se noti qualcosa, consigli la visita.</p>
        `,
          sources: ['https://jddonline.com/articles/dermatology/S1545961615S0032X',
            'https://pmc.ncbi.nlm.nih.gov/articles/PMC7109406',
            'https://wwwnc.cdc.gov/eid/article/11/4/04-0936_article',
            'https://www.bellusacademy.edu/wp-content/uploads/2022/05/CA-Board-of-Barber-Cosmo-Revised-Article-12-Health-and-Safety-2017.pdf',
            'https://aad.org/nail-care-secrets/manicure-pedicure-safety',
            'https://www.quotidianosanita.it/scienza-e-farmaci/piede-diabetico-ecco-il-decalogo-della-sid-per-prevenirlo/',
            'https://www.scratchmagazine.co.uk/feature/pedicure-tips-nail-techs-clients-diabetes',
            'https://ar.unmhealth.org/services/orthopaedics/_files/take-care-of-your-feet-for-a-lifetime-2-12-20-eng-812-1094.pdf']
        },
        {
          id: 'piedi-competenze', title: 'Pedicure estetica: protocollo e confini con il podologo', min: 13,
          simple: 'L\'estetista si occupa della bellezza del piede sano. Ciò che fa male o sembra malato è compito del podologo o del medico.',
          html: `
<p>In pedicure è facile superare il confine tra estetica e salute senza accorgersene: un callo che fa male, un angolo che si infiamma, un'unghia spessa. Conoscere il confine ti protegge legalmente e protegge la cliente.</p>
${F("estetista-podologo.svg", "Chi fa cosa: estetista e podologo, con le frecce di invio.")}
<h2>Chi fa cosa in Italia</h2>
<table>
<tr><th></th><th>Estetista (L. 1/1990)</th><th>Podologo (DM 666/1994)</th></tr>
<tr><td>Natura</td><td>Prestazioni sulla superficie del corpo per mantenerlo in buone condizioni e migliorarne l'aspetto. Sono escluse le prestazioni "dirette in linea specifica ed esclusiva a finalità di carattere terapeutico" (art. 1, c. 3).</td><td>Operatore sanitario con laurea abilitante e iscrizione all'albo.</td></tr>
<tr><td>Unghie</td><td>Piede sano: taglio, limatura, cuticole, semipermanente, piccoli ripristini estetici</td><td>Tratta "con metodi incruenti, ortesici ed idromassoterapici" callosità, unghie ipertrofiche, deformi e incarnite, piede doloroso</td></tr>
<tr><td>Altro</td><td>Massaggio estetico, idratazione, levigatura della pelle secca</td><td>Su prescrizione medica: medicazione di ulcerazioni e verruche; assiste i pazienti a rischio (es. diabete); segnala al medico i casi sospetti</td></tr>
</table>
<h2>Calli, duroni e lame</h2>
<p>Le <strong>callosità</strong> sono citate espressamente tra le competenze del podologo. Le linee guida sul piede diabetico raccomandano di non rimuoverle con prodotti chimici, cerotti o altre tecniche fai-da-te. La SID raccomanda di non tagliare i calli e di levigare l'ispessimento solo con pietra pomice.</p>
${B("warn", "In estetica: niente lame", "In una pedicure estetica la pelle ispessita si leviga con lime o raspe adatte, senza ferire. Lame e bisturi su calli e duroni non rientrano nel lavoro estetico. Prima di proporre qualsiasi trattamento sui calli, verifica il regolamento del tuo Comune e della tua Regione.")}
<h2>Il protocollo di pedicure estetica</h2>
${F("pedicure-protocollo.svg", "Protocollo di pedicure estetica.")}
<ol class="steps">
<li><strong>Anamnesi</strong>: diabete, problemi di circolazione, farmaci (per esempio anticoagulanti), allergie, micosi recenti, gravidanza. Firma del consenso.</li>
<li><strong>Ispezione</strong> di unghie e pelle, con buona luce, anche tra le dita. Se vedi un segnale di STOP ti fermi.</li>
<li><strong>Igiene</strong>: mani lavate, guanti in nitrile, detersione dei piedi della cliente.</li>
<li><strong>Pediluvio</strong> tiepido e breve, in vaschetta disinfettata o con fodera monouso.</li>
<li><strong>Taglio dritto</strong> e limatura degli angoli.</li>
<li><strong>Cuticole</strong>: ammorbidisci e arretra delicatamente; togli solo la pelle morta sulla lamina.</li>
<li><strong>Levigatura</strong> leggera della pelle secca del tallone, senza lame.</li>
<li><strong>Colore</strong> (se richiesto): opacizza, sgrassa, base, colore in strati sottili, top.</li>
<li><strong>Crema e massaggio</strong> leggero, mai tra le dita.</li>
<li><strong>Riordino</strong>: strumenti a sterilizzare, monouso nei rifiuti, vaschetta disinfettata e registrata.</li>
</ol>
${F("pedicure-postazione.svg", "La postazione di pedicure pronta: pulito da una parte, sporco dall'altra.")}
<h2>Ricostruzione sui piedi</h2>
<p>Solo piccoli <strong>ripristini estetici</strong> su unghia <strong>sana</strong>, per esempio un bordo spezzato da un trauma già guarito. Regole (prassi):</p>
<ul>
<li>Strato sottile e flessibile (rubber base o builder morbido).</li>
<li>Lunghezza a filo del polpastrello, forma dritta.</li>
<li>Mai sopra un'unghia sospetta, ispessita, dolorante o incarnita.</li>
<li>Mai per "ricostruire" un'unghia persa per una micosi o un'unghia che sta ricrescendo dopo un intervento: serve il parere del medico o del podologo.</li>
</ul>
${B("tip", "Una rete di professionisti", "Tieni il contatto di un podologo della tua zona. Quando invii una cliente con un biglietto e un nome di riferimento, lei si fida di più e torna da te per la parte estetica.")}
<h2>Errori frequenti</h2>
<ul>
<li>"Sistemare" un angolo incarnito "solo un pochino".</li>
<li>Rimuovere un callo doloroso con la lama.</li>
<li>Saltare l'anamnesi con una cliente abituale: le condizioni di salute cambiano.</li>
<li>Non registrare la disinfezione della vaschetta.</li>
</ul>
        `,
          sources: ['https://cislfp.it/wp-content/uploads/2018/10/d.-m.-666-1994-podologo.pdf',
            'https://www.normattiva.it/eli/id/1990/01/05/090G0009/CONSOLIDATED/20240920',
            'https://www.mo.camcom.it/sportello-genesi/sportello-genesi/modulistica/estetista-scheda-informativa',
            'https://iwgdfguidelines.org/wp-content/uploads/2019/05/02-IWGDF-prevention-guideline-2019.pdf',
            'https://www.quotidianosanita.it/scienza-e-farmaci/piede-diabetico-ecco-il-decalogo-della-sid-per-prevenirlo/']
        },
        {
          id: 'piedi-semipermanente', title: 'Tutorial: semipermanente sui piedi', min: 12,
          simple: 'Sui piedi il semipermanente si fa come sulle mani, ma con unghie più dure e dita vicine: servono separadita, strati sottili e tanta attenzione ai lati.',
          html: `
<p>Il semipermanente è il servizio più richiesto sui piedi, soprattutto in primavera ed estate. La tecnica è la stessa delle mani; cambiano la postura, la forma delle unghie e gli spazi stretti tra le dita.</p>
${F("tut-semipermanente-piedi.svg", "Il semipermanente sui piedi in otto passaggi.")}
<h2>Prima di iniziare</h2>
<ul>
<li>Anamnesi e ispezione: niente colore su unghie sospette (lezione precedente).</li>
<li>Cliente seduta comoda, piede appoggiato su un supporto stabile all'altezza giusta per te: lavorare piegata fa male alla schiena e peggiora la precisione.</li>
<li>Lampada posizionabile per i piedi (molte lampade hanno il fondo rimovibile).</li>
</ul>
<h2>Procedura</h2>
<ol class="steps">
<li><strong>Igiene e ispezione</strong> di unghie e pelle.</li>
<li><strong>Taglio dritto</strong>, lima sugli angoli; cuticola ammorbidita e arretrata delicatamente.</li>
<li><strong>Asciuga bene</strong>: dopo il pediluvio la lamina è piena d'acqua. Aspetta qualche minuto prima del colore, oppure lavora a secco e fai il pediluvio dopo (prassi: molte tecniche fanno il colore senza ammollo).</li>
<li><strong>Separadita</strong>: allargano le dita e evitano che il colore tocchi il dito vicino.</li>
<li><strong>Opacizza</strong> leggermente la lamina (buffer 180–240), togli la polvere, <strong>sgrassa</strong> con il disidratante.</li>
<li><strong>Base</strong> sottile, senza toccare la pelle; lampada.</li>
<li><strong>Colore</strong> in due strati sottili, sigillando il bordo; lampada dopo ogni strato. Sulle dita piccole usa poco prodotto: il pennello carico "allaga" i lati.</li>
<li><strong>Top</strong>, lampada, eventuale pulizia dello strato di dispersione, olio sulle cuticole.</li>
</ol>
${B("tip", "Le dita piccole", "Sulle unghie del quarto e del quinto dito spesso c'è pochissima lamina. Stendi il colore con la punta del pennello, a piccoli tocchi, partendo dal centro. Meglio un millimetro di margine in più che colore sulla pelle.")}
${F("piedi-errori-colore.svg", "Errori tipici: colore sulla pelle, bordo non sigillato, strato spesso nei solchi.")}
<h2>Durata e rimozione</h2>
<ul>
<li>Sui piedi l'unghia cresce lentamente: il colore resta bello più a lungo che sulle mani. Il momento di rifarlo dipende dalla ricrescita visibile e dallo stato del colore.</li>
<li>Rimozione come sulle mani: opacizza il top, acetone e stagnola, bastoncino senza fare leva. Non strappare: porta via strati di lamina.</li>
</ul>
<h2>Errori frequenti</h2>
<table>
<tr><th>Errore</th><th>Conseguenza</th><th>Rimedio</th></tr>
<tr><td>Colore subito dopo l'ammollo</td><td>Si stacca prima</td><td>Lamina asciutta e sgrassata</td></tr>
<tr><td>Prodotto nei solchi laterali</td><td>Lifting, contatto con la pelle</td><td>Poco prodotto, margine, togli prima della lampada</td></tr>
<tr><td>Bordo non sigillato</td><td>Scheggiature in punta</td><td>Passa il pennello sullo spessore</td></tr>
<tr><td>Senza separadita</td><td>Colore sul dito vicino</td><td>Separadita monouso</td></tr>
</table>
        `,
          sources: ['https://www.aad.org/public/everyday-care/nail-care-secrets/basics/how-to-trim-nails',
            'https://aad.org/nail-care-secrets/manicure-pedicure-safety',
            'https://bionumbers.hms.harvard.edu/bionumber.aspx?id=112380']
        }
      ]
    },
    /* ------------------------------------------------------------------ 16 */
    {
      id: 'arte-gare', n: 16, level: 'avanz', title: 'Nail art avanzata e gare',
      summary: ['Chrome: polvere strofinata sul top no-wipe polimerizzato; togli la polvere libera dal bordo, poi sigilla.', 'Cat-eye: rotola la boccetta, magnete vicino ma senza toccare, prima della lampada; flash breve per fissare.', 'Foil: gel per foil sottile e appiccicoso, foil con il disegno verso l\'alto, sigilla con il top.', 'One-stroke: pennello piatto caricato metà e metà, mai fino alla ghiera.', 'Incapsulato: nelle zone spesse (smile line, apex), mai alla cuticola o ai lati; l\'apex si costruisce sopra.', 'Gare: leggi regolamento e scheda punteggi dell\'edizione; gel non polimerizzato o pulizia dopo lo stop = squalifica.', 'I giudici guardano da più lati: curva C a tunnel, apex, spessore del bordo, smile line, cuticola, lucentezza.'],
      desc: 'Chrome, cat-eye, ombré, one-stroke, 3D e preparazione alle competizioni.',
      lessons: [
        {
          id: 'effetti', title: 'Effetti: chrome, cat-eye, ombré, foil', min: 16,
          simple: 'Molti effetti speciali si fanno sopra un top "no-wipe": prima lo indurisci, poi ci strofini la polvere o appoggi la decorazione. Altri, come il cat-eye, si creano prima della lampada.',
          videos: /* invariato */ [{ id: 'qqr7eqjLYTg', title: 'Chrome Mirror Powder Nail Application', channel: 'Beetles Gel Polish', lang: 'EN' },
            { id: '1x0Oc9gD7GY', title: 'Smalto cat eye: come si applica', channel: 'Estetista Shop', lang: 'IT' }],
          html: `
${F("nail-art-effetti.svg", "Chrome, cat-eye e one-stroke.")}
<p>Gli effetti speciali piacciono molto alle clienti e sono più facili di quanto sembrino. Il segreto è sapere <strong>in quale momento</strong> si applica ogni prodotto: su un gel ancora fluido, su uno strato appiccicoso o su un top già indurito.</p>
<table>
<tr><th>Effetto</th><th>Su cosa si lavora</th><th>Momento chiave</th></tr>
<tr><td>Chrome</td><td>Top no-wipe polimerizzato</td><td>Subito dopo la lampada</td></tr>
<tr><td>Cat-eye</td><td>Gel magnetico fluido</td><td>Prima della lampada</td></tr>
<tr><td>Foil</td><td>Gel per foil appiccicoso</td><td>Dopo la lampada, sullo strato appiccicoso</td></tr>
<tr><td>Ombré</td><td>Due colori fluidi</td><td>Sfumati prima della lampada</td></tr>
</table>
${F("chrome-step.svg", "Chrome in sei passaggi.")}
<h2>Chrome (effetto specchio)</h2>
<p>La polvere chrome è un pigmento finissimo che, strofinato su una superficie liscia e lucida, riflette la luce come uno specchio.</p>
<ol class="steps">
<li><strong>Base e colore</strong> come di consueto. Il colore sotto deve essere liscio: il chrome mette in evidenza ogni imperfezione. Rende di più su colori scuri o neri.</li>
<li><strong>Top no-wipe</strong>, steso sottile, e lampada. Un marchio indica circa 30 secondi; segui la scheda tecnica del tuo top.</li>
<li><strong>Appena fuori dalla lampada</strong>, prendi poca polvere con l'applicatore (spugnetta o pennellino in silicone).</li>
<li><strong>Strofina</strong> con piccoli movimenti fino a coprire tutto. Se resta polvere libera, continua a lucidare invece di aggiungerne.</li>
<li><strong>Pulisci il bordo libero</strong>: passa delicatamente un buffer sulla punta e un pennello per la polvere su tutta l'unghia. La polvere libera impedisce al top di aderire.</li>
<li><strong>Top finale</strong> che avvolge anche il bordo libero, e lampada.</li>
</ol>
${B("info", "Appiccicoso o indurito?", "Le fonti non sono d'accordo: alcune applicano la polvere su un top non ancora completamente indurito o tiepido, altre su un top no-wipe polimerizzato. Per chi inizia il metodo più affidabile è il top no-wipe polimerizzato, come indicato da molti marchi. Prova sempre il tuo prodotto su un tip.")}
${F("cat-eye-magnete.svg", "Cat-eye: dove tieni il magnete decide il disegno.")}
<h2>Cat-eye (gel magnetico)</h2>
<p>Il gel cat-eye contiene particelle metalliche. Un magnete le sposta finché il gel è fluido: dove si concentrano si forma una banda luminosa che sembra muoversi con la luce.</p>
<ol class="steps">
<li><strong>Fondo scuro</strong> (spesso nero) o dello stesso tono: aumenta la profondità. Lampada.</li>
<li><strong>Rotola la boccetta</strong> tra le mani: le particelle tendono a depositarsi.</li>
<li><strong>Stendi lo strato magnetico</strong> sottile. Uno strato spesso rende l'effetto più difficile da controllare. Alcuni tecnici stendono e polimerizzano un primo strato senza magnete, e lavorano il magnete solo sul secondo.</li>
<li><strong>Avvicina il magnete</strong> senza toccare l'unghia e tienilo fermo qualche secondo. Le indicazioni dei marchi variano: distanza da circa 1 a 5 mm, tempo da 3 a 15 secondi. Più vicino e più a lungo = linea più netta.</li>
<li><strong>Flash breve</strong> in lampada (circa 10 secondi secondo un marchio) per "bloccare" le particelle, un dito alla volta. Poi polimerizza tutta la mano.</li>
<li><strong>Top sottile</strong>. Uno spesso fa da "lente" e distorce la linea.</li>
</ol>
<table>
<tr><th>Posizione del magnete</th><th>Effetto</th></tr>
<tr><td>Parallelo all'unghia, al centro</td><td>Linea luminosa centrale</td></tr>
<tr><td>Inclinato a circa 45°</td><td>Banda diagonale, più facile da spostare</td></tr>
<tr><td>Vicino a un lato o alla punta</td><td>Luce concentrata su un lato o in punta</td></tr>
<tr><td>Due magneti ai lati</td><td>Particelle spinte al centro: effetto "galassia"</td></tr>
<tr><td>Magnete mosso su tutta l'unghia</td><td>Effetto diffuso, "velluto" (velvet)</td></tr>
</table>
${B("tip", "Puoi rifare", "Se il disegno non ti piace e il gel è ancora fluido, ripassa il pennello e usa di nuovo il magnete. Tieni i magneti lontani da telefoni e carte.")}
${F("foil-ombre-step.svg", "Foil e ombré passo per passo.")}
<h2>Foil (lamina transfer)</h2>
<ol class="steps">
<li>Colore polimerizzato e liscio: il foil evidenzia ogni difetto.</li>
<li>Stendi un <strong>velo sottile</strong> di gel per foil (o colla per foil) solo dove vuoi la decorazione. Polimerizza: resta appiccicoso.</li>
<li>Appoggia il foil con il <strong>disegno verso l'alto</strong> (lato opaco verso l'unghia), strofina bene e solleva.</li>
<li>Sigilla con un top che copra bene il foil, senza trascinarlo con il pennello. Lampada.</li>
</ol>
<p class="muted"><small>Se il foil non attacca, di solito il gel per foil era troppo spesso o non polimerizzato abbastanza. Olio e acetone fanno sollevare il foil.</small></p>
<h2>Ombré</h2>
<ul>
<li><strong>Con il pennello</strong> (più preciso): primo colore dalla cuticola a metà, secondo dalla punta verso il primo, poi sfuma con pennellate orizzontali leggere nella zona di incontro. Lampada. Ripeti con un secondo strato. Top.</li>
<li><strong>Con la spugnetta</strong> (più facile): picchietta la spugna su un nastro adesivo per togliere i pelucchi, carica un velo di colore, picchietta dalla punta verso il centro. Lampada e ripeti. Top abbondante per lisciare.</li>
</ul>
<h2>Errori frequenti</h2>
<table>
<tr><th>Errore</th><th>Risultato</th><th>Correzione</th></tr>
<tr><td>Chrome su colore irregolare</td><td>Specchio "a buchi"</td><td>Colore liscio, top sottile</td></tr>
<tr><td>Polvere libera sul bordo</td><td>Il top si stacca in punta</td><td>Buffer leggero e pennello prima del top</td></tr>
<tr><td>Magnete appoggiato all'unghia</td><td>Segno sul gel, disegno rovinato</td><td>Distanza di qualche millimetro</td></tr>
<tr><td>Attesa lunga prima della lampada</td><td>Le particelle del cat-eye si spostano</td><td>Flash subito, un dito alla volta</td></tr>
<tr><td>Gel per foil spesso</td><td>Foil che non attacca o si raggrinza</td><td>Velo sottile e ben polimerizzato</td></tr>
</table>
        `,
          sources: ['https://blueskycosmetics.co.uk/blogs/blog/how-to-use-chrome-powder',
            'https://pinkgellac.com/blogs/news/how-to-use-cat-eye-gel-polish',
            'https://www.scratchmagazine.co.uk/nail_art/cat-eye-chrome-nail-art-tutorial/',
            'https://thegelbottle.com/blog/how-to-apply-nail-foils-on-gel-nails-in-5-steps/',
            'https://www.youngnails.com/blogs/news/how-to-do-ombre-gel-polish-nails']
        },
        {
          id: 'one-stroke-3d', title: 'One-stroke, 3D e incapsulato', min: 15,
          simple: 'Nel one-stroke un solo colpo di pennello disegna un petalo già sfumato, perché il pennello porta due colori. Nell\'incapsulato la decorazione finisce "dentro" l\'unghia, tra due strati trasparenti.',
          videos: /* invariato */ [{ id: 'Plp5F1qk40Y', title: 'One stroke flower nail art for beginners', channel: 'Dorota Palicka Nails', lang: 'EN' }],
          html: `
<h2>One-stroke: un colpo, due colori</h2>
<p>Il one-stroke è una tecnica di pittura nata per la decorazione e adattata alle unghie. Un pennello piatto porta due colori, uno per lato: con una sola pennellata ottieni un petalo o una foglia già sfumati, con luce e ombra.</p>
${F("one-stroke-carico.svg", "Caricare il pennello piatto: due colori, metà e metà, sfumati sulla tavolozza.")}
<h3>Materiali</h3>
<ul>
<li>Pennello piatto sintetico (n. 2–3 per le unghie).</li>
<li>Colori acrilici per nail art o gel da pittura, a seconda della tecnica.</li>
<li>Tavolozza. Trucco usato da una formatrice: carta da forno appoggiata su carta assorbente inumidita, così il colore resta cremoso più a lungo.</li>
<li>Top per sigillare.</li>
</ul>
<h3>Caricare il pennello</h3>
<ol class="steps">
<li>Inumidisci il pennello e tamponalo: deve essere umido, non bagnato.</li>
<li>Intingi un <strong>angolo</strong> in un colore e l'angolo opposto nell'altro. Per iniziare carica <strong>circa metà e metà</strong>.</li>
<li>Muovi il pennello avanti e indietro <strong>sempre nello stesso punto</strong> della tavolozza: i due colori si sfumano al centro.</li>
<li>Il colore deve arrivare a circa <strong>3/4 delle setole</strong>, mai dentro la ghiera (la parte metallica): lì si secca e rovina il pennello.</li>
<li>Quando i due colori si mescolano troppo e la linea tra loro sparisce, pulisci il pennello e ricarica.</li>
</ol>
${F("one-stroke-fiore.svg", "Petalo, fiore a cinque petali e foglia, passo per passo.")}
<h3>I tre movimenti base</h3>
<table>
<tr><th>Forma</th><th>Movimento</th></tr>
<tr><td><strong>Petalo</strong></td><td>Appoggia il pennello sul filo, premi per allargare le setole, ruota tenendo fermo un angolo (il "perno") e fai girare l'altro, poi solleva.</td></tr>
<tr><td><strong>Fiore a 5 petali</strong></td><td>Ripeti il petalo cinque volte girando intorno a un centro, con il colore chiaro sempre verso l'esterno. Puntini al centro con il dotting.</td></tr>
<tr><td><strong>Foglia</strong></td><td>Parti sul filo, premi, scivola in avanti alleggerendo la pressione e fai una piccola <strong>torsione finale</strong>: crea la punta.</td></tr>
</table>
${B("tip", "Allenati sulla carta", "Esercitati prima su carta o su tip, decine di volte. Impugna vicino alla ghiera e appoggia il mignolo per stabilizzare la mano. Rinforza il colore ripassando nello stesso punto, nella stessa direzione.")}
<h2>3D</h2>
<p>Il 3D sono decorazioni in rilievo: fiori, fiocchi, perle modellate.</p>
<ul>
<li><strong>Acrilico colorato</strong>: si modella una perla alla volta con il pennello, petalo per petalo, e si lascia indurire all'aria.</li>
<li><strong>Gel da modellare</strong> (o polygel): si modella con calma, poi si polimerizza a piccoli passaggi.</li>
<li>Si fissa alla superficie con un velo di builder o di gel e si sigilla intorno senza coprire il rilievo.</li>
</ul>
${B("warn", "Spessore e vita quotidiana", "Il 3D si rompe facilmente e può impigliarsi. Tienilo basso, su una o due unghie, ed evitalo per clienti con lavori manuali. In gara segui le regole della categoria: in alcune categorie il 3D o certi materiali sono vietati.")}
${F("incapsulato-zone.svg", "Dove incapsulare: nelle zone spesse (smile line, apex, centro della punta), mai alla cuticola, ai lati o sul bordo.")}
<h2>Incapsulato (embedding)</h2>
<p>Incapsulare vuol dire chiudere una decorazione (glitter, fiori secchi, pizzo, foglia) tra due strati di prodotto trasparente. Il risultato è liscio al tatto, come vetro.</p>
<ol class="steps">
<li><strong>Prova sempre su un tip</strong> l'oggetto nuovo: alcuni rivestimenti si sciolgono o si scoloriscono a contatto con il monomero o il gel. Meglio scoprirlo prima che sulla cliente.</li>
<li><strong>Scegli la zona giusta</strong>: le zone più spesse, cioè smile line, zona dell'apex, centro del bordo libero. Evita zona cuticolare, lati e bordo, che sono sottili: dovresti lasciare un rigonfiamento o limare attraverso la decorazione.</li>
<li><strong>Piattaforma sottilissima</strong> di trasparente, non più spessa di un tip.</li>
<li><strong>Fissa la decorazione</strong>:
          <ul>
          <li>in <strong>acrilico</strong>: premila con il retro del pennello finché il prodotto è ancora morbido;</li>
          <li>in <strong>gel</strong>: velo sottilissimo con un flash di 2–3 secondi (dipende da gel e lampada), così non cola ma "trattiene" ciò che premi;</li>
          <li>per oggetti spessi come il pizzo: piattaforma polimerizzata e una goccia di colla.</li>
          </ul></li>
<li><strong>Rifila</strong> ciò che sporge dai lati o dal bordo: altrimenti la "capsula" non si chiude.</li>
<li><strong>Copri e costruisci</strong>: lo strato trasparente sopra fa da struttura. L'<strong>apex si costruisce sopra la decorazione</strong>, così l'unghia resta robusta.</li>
<li>Lima e lucida: superficie liscia, nessun bordo dell'oggetto al tatto.</li>
</ol>
${B("info", "Gel o acrilico?", "Il gel dà il trasparente più limpido e fa sembrare la decorazione più profonda. L'acrilico la fa sembrare più vicina e piatta. Su unghie lunghe incapsulare è più facile perché c'è più superficie.")}
<h2>Errori frequenti</h2>
<ul>
<li>Pennello carico fino alla ghiera: colori impastati e pennello rovinato.</li>
<li>Decorazione incapsulata alla cuticola: rigonfiamento o lifting.</li>
<li>Oggetto che sporge sul bordo: la capsula si apre e si solleva.</li>
<li>Apex dimenticato sopra la decorazione: unghia debole.</li>
</ul>
        `,
          sources: ['https://www.nailpro.com/technique/article/21155084/tips-on-one-stroke-painting',
            'https://www.scratchmagazine.co.uk/nail_art/one-stroke-petals-by-terry-burciaga/',
            'https://www.nailpro.com/technique/article/21156545/nail-art-tutorial-neon-one-stroke-flowers',
            'https://www.scratchmagazine.co.uk/feature/how-to-ace-encapsulation-in-lp-gel-nails']
        },
        {
          id: 'gare', title: 'Prepararsi a una gara', min: 16,
          simple: 'In gara conta la precisione: unghie tutte uguali, pulite e costruite bene, nel tempo stabilito e rispettando ogni regola del regolamento.',
          videos: /* invariato */ [{ id: 'Tx3lwXOS0L0', title: 'Do\'s and Don\'ts of Apex Structure', channel: 'YoungNailsInc', lang: 'EN' }],
          html: `
<p>Una gara di unghie è il modo più rapido per migliorare. Devi lavorare con precisione, in un tempo fisso, sotto lo sguardo di giudici esperti. Anche un piazzamento basso vale molto, se impari a leggere la scheda di valutazione.</p>
${B("warn", "Prima regola", "Le regole cambiano per sede, per anno e per organizzazione: leggi sempre il regolamento dell'edizione a cui ti iscrivi, più volte. Chi gareggia senza leggerlo perde punti evitabili o viene squalificato.")}
<h2>Le principali organizzazioni</h2>
<ul>
<li><strong>Nailympia</strong>: circuito internazionale con tappe in diversi paesi, tra cui l'Italia (Sicilia), Regno Unito, Germania, Stati Uniti, Cina.</li>
<li><strong>NAILPRO Competition</strong>: gare negli Stati Uniti legate alla rivista NAILPRO.</li>
<li>Altre gare nazionali e regionali, a volte con regole molto diverse. Una competitrice racconta di aver scoperto in gara che una competizione francese fissava la lunghezza massima degli stiletto a 5 cm, diversa da quella di Nailympia.</li>
</ul>
<h2>Tempi di esempio</h2>
<table>
<tr><th>Categoria</th><th>Nailympia Sicily</th><th>Nailympia China</th></tr>
<tr><td>Gel Polish Manicure</td><td>45 min</td><td>45 min</td></tr>
<tr><td>Salon Nails</td><td>60 min</td><td>60 min</td></tr>
<tr><td>French Tip &amp; Overlay (1 mano)</td><td>75 min</td><td>—</td></tr>
<tr><td>French Sculpture (1 mano)</td><td>90 min</td><td>—</td></tr>
<tr><td>Competition Style (gel o acrilico)</td><td>—</td><td>90 min</td></tr>
<tr><td>French Twist</td><td>120 min</td><td>75 min</td></tr>
<tr><td>Stiletto</td><td>120 min</td><td>120 min</td></tr>
</table>
<p class="muted"><small>La stessa categoria può avere tempi diversi: il French Twist dura 120 minuti a Sicily e 75 a China, dove è una sfida a 3 unghie con 3 forme diverse. Controlla sempre l'edizione.</small></p>
${F("gara-postazione.svg", "La postazione di gara: prodotti etichettati, scatola tip sigillata, cestino, niente borse sul tavolo.")}
<h2>Regole tipiche (Nailympia)</h2>
<table>
<tr><th>Regola</th><th>Conseguenza</th></tr>
<tr><td>Modelle maggiorenni (18+), presenti finché tutti i giudici le hanno viste</td><td>Modella che se ne va prima: squalifica</td></tr>
<tr><td>Prodotti nell'imballo originale, con etichetta; solo acetone, cleaner e alcol possono stare in flaconi etichettati a mano</td><td>Prodotti senza etichetta rimossi dal tavolo</td></tr>
<tr><td>Tip in scatola ordinata per misura (almeno 10 per misura); cartine e tip non toccati, tagliati o preparati prima del via</td><td>Materiale preparato prima: confiscato</td></tr>
<tr><td>Toccare le unghie della modella dopo l'inizio del briefing</td><td>−5 punti</td></tr>
<tr><td>Preparare le unghie della modella prima del briefing (dove non è permesso)</td><td>−5 punti</td></tr>
<tr><td>Troppa crema o olio sulle mani a fine gara</td><td>Punti in meno</td></tr>
<tr><td>Gel non polimerizzato a fine gara</td><td>Squalifica</td></tr>
<tr><td>Pulire mani o unghie con qualsiasi prodotto dopo lo stop (anche aria compressa)</td><td>Squalifica</td></tr>
<tr><td>Tentativo di imbroglio</td><td>Squalifica</td></tr>
</table>
<p>Ogni categoria ha poi regole sue. Esempi: in alcune categorie sono vietati semipermanente, bianco "a pennarello", strumenti per la smile line, adesivi, top opaco o glitter. Nella categoria Sculptured di NAILPRO si usano solo rosa, trasparente e bianco, senza cover, con la smile line fatta a mano.</p>
${B("info", "Dettagli che costano punti", "Una competitrice racconta di aver perso 5 punti perché non aveva il cestino accanto al tavolo. Fai una lista di controllo del tavolo e rileggila la sera prima.")}
<h2>Come si giudica</h2>
<p>Il giudizio è <strong>anonimo</strong>: i giudici vedono la modella con un numero, non sanno chi ha lavorato. Nelle gare Nailympia possono esserci fino a 10 giudici, in cabine o dietro una tenda, ognuno con i suoi criteri. Le schede si consegnano dopo la premiazione. I giudici non commentano i lavori a fine gara, ma puoi chiedere un parere se le unghie sono ancora disponibili. La lezione successiva spiega una scheda punteggi completa.</p>
${F("gara-scheda.svg", "Criteri di giudizio e vista a tunnel.")}
<h2>Le basi da allenare</h2>
<ul>
<li>Struttura: apex nella stessa posizione su tutte le unghie, curva C regolare.</li>
<li>Bordo libero e "hair line" (spessore visto dalla punta) sottilissimi e uniformi.</li>
<li>Smile line netta e simmetrica, alla stessa profondità sulle dita gemelle.</li>
<li>Zona cuticolare pulita: niente tagli, irritazioni, scalini.</li>
<li>Superficie liscia e lucidissima.</li>
<li>Gestione del tempo: finire è fondamentale. Molti principianti limano fino allo stop e non mettono top o lucidatura: una competitrice esperta stima che così si perdano 15–20 punti.</li>
</ul>
${F("gara-piano-allenamento.svg", "Piano di allenamento indicativo di 12 settimane.")}
<h2>Piano di allenamento (8–12 settimane, prassi)</h2>
<ol class="steps">
<li><strong>Settimana 1</strong>: scegli la categoria, scarica regolamento e scheda punteggi, fai la lista del kit.</li>
<li><strong>Settimane 1–4</strong>: una mano completa a settimana su modella, cronometrata. Foto di profilo, a tunnel, dall'alto e della cuticola.</li>
<li><strong>Settimane 5–8</strong>: allena i punti deboli visti nelle foto (per esempio 20 smile line su tip, 10 apex di profilo).</li>
<li><strong>Ultime settimane</strong>: simulazioni complete con 10 minuti in meno del tempo di gara, kit definitivo, prova del tavolo con la modella.</li>
<li><strong>Ultima settimana</strong>: niente prodotti nuovi. Controlla la modella: unghie sane, nessuna ferita, nessuna preparazione vietata.</li>
</ol>
<h2>Il giorno della gara</h2>
<ul>
<li>Arriva presto: registrazione, controllo del tavolo da parte dei giudici di sala.</li>
<li>Prolunghe e adattatori: spesso sono a carico tuo.</li>
<li>Telefono solo per il cronometro, se il regolamento lo permette.</li>
<li>Allo stop: mani giù, niente più contatto.</li>
</ul>
        `,
          sources: ['https://www.nailympia.com/sicily/rules/', 'https://www.nailympia.com/china/rules/',
            'https://www.scratchmagazine.co.uk/feature/the-importance-of-rules-questions/',
            'https://www.nailpro.com/technique/article/21157846/competition-corner-for-the-win']
        },
        {
          id: 'gara-giudizio', title: 'La scheda punteggi: come ragionano i giudici', min: 12,
          simple: 'La scheda punteggi ti dice esattamente cosa guarderanno i giudici e quanto vale ogni cosa. Leggerla bene è metà dell\'allenamento.',
          html: `
<p>Ogni categoria di gara ha una <strong>scheda punteggi</strong> (score sheet). Elenca i criteri, quanti punti vale ciascuno e quale giudice lo valuta. È il documento più utile per allenarti: ti dice dove si vincono e dove si perdono i punti.</p>
<h2>Un esempio reale: French Twist 3-Shape Challenge (Nailympia 2026)</h2>
<p>La scheda vale per una sfida con 3 unghie su una mano, 3 forme diverse e un decoro "inlay" (inserito nell'allungamento), in 75 minuti. Il totale è <strong>240 punti</strong>, divisi tra 10 giudici.</p>
${F("gara-punteggio.svg", "I punti della scheda French Twist 3-Shape Challenge 2026, giudice per giudice.")}
<table>
<tr><th>Giudice</th><th>Criterio</th><th>Punti</th><th>Cosa guarda</th></tr>
<tr><td>1</td><td>Smile line</td><td>15</td><td>Forma uguale, linea netta, senza ombre. Indice e anulare con smile alla stessa profondità; mignolo più corto, medio più lungo.</td></tr>
<tr><td>2</td><td>Lunghezza</td><td>15</td><td>Proporzionata alla mano. Indicazione: medio e pollice almeno 4 cm (es. letto 16 mm + allungamento 24 mm).</td></tr>
<tr><td>3</td><td>Curva C (vista a tunnel) + apex</td><td>15 + 15</td><td>Curva coerente con la struttura; apex nella stessa posizione su ogni unghia, non esagerato, "elegante".</td></tr>
<tr><td>4</td><td>Hair line e spessore del bordo + convesso/concavo</td><td>15 + 15</td><td>Unghia sottile e uniforme, non più spessa di un biglietto da visita; curva sopra e sotto simmetrica.</td></tr>
<tr><td>5</td><td>Forma</td><td>15</td><td>Uniforme vista dall'alto e dal punto di vista della modella; 3 forme ben riconoscibili.</td></tr>
<tr><td>6</td><td>Arco e linee laterali, sopra e sotto</td><td>15 + 15</td><td>Profilo regolare; lati che escono dritti dalle pieghe laterali, senza scalini.</td></tr>
<tr><td>7</td><td>Decoro inlay, colore, creatività</td><td>15 + 15 + 15</td><td>Decoro evidente e ben fatto, palette armoniosa, effetto "wow".</td></tr>
<tr><td>8</td><td>Zona cuticolare + lucentezza</td><td>9 + 9</td><td>Nessun taglio o irritazione, prodotto uniforme senza scalini; lucido "a vetro", nessun graffio.</td></tr>
<tr><td>9</td><td>Aderenza della cartina/tip + superficie</td><td>9 + 9</td><td>Nessun residuo, polvere o colla sotto il prodotto; superficie liscia, senza avvallamenti.</td></tr>
<tr><td>10</td><td>Applicazione allungamento + letto (rosa/clear/camouflage)</td><td>6 + 18</td><td>Niente ombre, bolle o buchi; stacco netto alla smile line; sfumatura morbida verso la cuticola.</td></tr>
</table>
${B("info", "Cosa insegna questa scheda", "La struttura (curva C, apex, spessore, profilo, linee laterali) vale da sola 90 punti su 240. La pulizia della cuticola e la lucentezza valgono 18 punti: sono «facili» e non vanno mai persi per fretta.")}
${F("gara-viste-giudice.svg", "Le cinque viste del giudice: dall'alto, di profilo, a tunnel, la cuticola, il punto di vista della modella.")}
<h2>Le viste del giudice</h2>
<ol class="steps">
<li><strong>Dall'alto</strong>: forma, simmetria, lunghezze proporzionate tra le dita, linee laterali.</li>
<li><strong>Di profilo</strong>: apex, arco superiore e inferiore, assenza di gobbe o avvallamenti.</li>
<li><strong>A tunnel</strong> (dalla punta): curva C, spessore del bordo ("hair line"), simmetria dei lati.</li>
<li><strong>Zona cuticolare</strong>, spesso con la lente: nessuno scalino, nessun taglio, nessun prodotto sulla pelle.</li>
<li><strong>Dal punto di vista della modella</strong>: la forma deve apparire uniforme anche guardando le proprie mani.</li>
</ol>
<h2>Allenarti con la scheda</h2>
<ol class="steps">
<li>Stampa la scheda della tua categoria.</li>
<li>Dopo ogni prova, fotografa le unghie dalle cinque viste.</li>
<li>Dai un voto onesto a ogni criterio, oppure fallo fare a una collega.</li>
<li>Scegli i <strong>due criteri più deboli</strong> con più punti in gioco e allenali per due settimane.</li>
<li>Ripeti: confronta i punteggi nel tempo.</li>
</ol>
${B("tip", "Decidere dove investire il tempo", "Nessuno prende il punteggio pieno. Sapere quanti punti vale ogni criterio ti aiuta a decidere, in gara, dove spendere gli ultimi minuti: spesso lucidatura e pulizia valgono più di un ritocco alla forma.")}
        `,
          sources: ['https://www.scratchmagazine.co.uk/wp-content/uploads/2026/01/Nailympia-2026-Scoresheet_French-Twist-3-shape-challenge.pdf',
            'https://www.nailympia.com/china/rules/',
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
    { id: 'es-rimozione', module: 'manutenzione', level: 'base', title: 'Rimozione soak-off', time: '30 min', img: 'rimozione.svg', caption: 'Togli il top, acetone, stagnola, bastoncino.', imgs: ['rimozione-soakoff-step.svg', 'dpi.svg'],
      goal: 'Rimuovere il prodotto senza danneggiare la lamina.',
      materials: ['Tip con semipermanente o soft gel', 'Lima 100/180', 'Olio o crema barriera', 'Acetone', 'Cotone', 'Stagnola', 'Bastoncino d\'arancio', 'Buffer morbido', 'Guanti in nitrile'],
      steps: ['Togli il top e assottiglia il prodotto senza arrivare alla lamina.', 'Proteggi la pelle intorno con olio, poi applica cotone con acetone e avvolgi.', 'Attendi 10–15 minuti (dal momento in cui tutte le dita sono avvolte), poi controlla un dito.', 'Spingi via il prodotto ammorbidito dalla cuticola verso la punta; se resiste riavvolgi 5–10 minuti; finisci con buffer morbido e olio.'],
      checks: ['Ho tolto il top senza limare la lamina', 'Ho rispettato i tempi', 'Non ho grattato né fatto leva', 'Ho finito con olio'],
      mistakes: ['Strappare il prodotto non ancora ammorbidito', 'Usare l\'acetone su pelle irritata', 'Usare gli stessi tempi per l\'acrilico (serve di più: 20–30 minuti)'] },
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
    { id: 'es-consulenza', module: 'professione', level: 'inter', title: 'Consulenza simulata', time: '20 min', img: 'scheda-cliente.svg', caption: 'Usa una scheda come questa.', imgs: ['consulenza-flusso.svg', 'consensi-separati.svg'],
      goal: 'Condurre una consulenza completa e compilare la scheda cliente.',
      materials: ['Scheda cliente stampata', 'Informativa privacy e moduli di consenso', 'Una persona che faccia la cliente'],
      steps: ['Consegna l\'informativa e raccogli i consensi separati (dati sulla salute; foto facoltative).', 'Chiedi allergie, farmaci e condizioni di salute; osserva unghie e pelle cercando controindicazioni.', 'Chiedi abitudini e desideri; proponi sistema, forma e lunghezza spiegando il perché.', 'Spiega i consigli post-trattamento, consegna il biglietto e fissa il refill.'],
      checks: ['Ho chiesto di allergie e farmaci', 'Ho raccolto consensi separati per salute e foto', 'Ho valutato le controindicazioni', 'Ho dato i consigli post-trattamento'],
      mistakes: ['Saltare le domande sulla salute', 'Fare foto senza un consenso separato', 'Accettare una lunghezza non adatta alle abitudini della cliente'] },
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
      mistakes: ['Correggere un lato senza ricontrollare l\'altro', 'Guardare solo dall\'alto'] },
    { id: 'es-french-varianti', module: 'decorazioni', level: 'inter', title: 'Varianti del french su 10 tip', time: '45 min', img: 'french-varianti.svg', caption: 'Classico, V, micro, reverse.', imgs: ['reverse-french-step.svg', 'french-punti-guida.svg'],
      goal: 'Ripetere la stessa misura e la stessa simmetria su varianti diverse del french.',
      materials: ['Ruota di tip', 'Gel o semipermanente bianco e un colore', 'Pennello liner', 'Pennello piatto pulito', 'Cleaner', 'Lampada'],
      steps: ['Su 3 tip disegna un V-french con le due linee della stessa inclinazione.', 'Su 3 tip disegna un micro french di spessore uguale.', 'Su 4 tip disegna un reverse french partendo dal centro, lasciando circa 1 mm dal bordo "pelle" del tip.', 'Fotografa i tip dall\'alto e confrontali a coppie.'],
      checks: ['Le V hanno la punta al centro', 'Il micro french ha lo stesso spessore su tutti i tip', 'Gli archi del reverse sono regolari e staccati dal bordo', 'Nessuna sbavatura polimerizzata'],
      mistakes: ['Disegnare l\'arco del reverse da un lato all\'altro (viene storto)', 'Pulire le sbavature dopo la lampada invece che prima'] },
    { id: 'es-riparazione', module: 'manutenzione', level: 'inter', title: 'Riparare una crepa', time: '30 min', img: 'riparazione-crepa.svg', caption: 'Lima finché la crepa sparisce, poi ricostruisci.', imgs: ['riparazione-decisione.svg'],
      goal: 'Riparare una crepa nel prodotto senza lasciare punti deboli.',
      materials: ['Tip o mano da allenamento con ricostruzione', 'Lima 100/180 e 180/240', 'Builder gel', 'Lampada', 'Lente d\'ingrandimento'],
      steps: ['Crea una crepa piegando leggermente un tip ricostruito.', 'Accorcia e lima la zona finché la crepa non si vede più nemmeno con la lente.', 'Raccorda il prodotto intorno e ricostruisci l\'apex.', 'Rifinisci e controlla di profilo e in controluce.'],
      checks: ['La crepa è sparita del tutto', 'Nessun gradino intorno alla riparazione', 'Apex sopra il punto di stress', 'Superficie liscia in controluce'],
      mistakes: ['Coprire la crepa senza limarla', 'Ricostruire senza rifare l\'apex'] },
    { id: 'es-margine', module: 'problemi', level: 'inter', title: 'Allenare il margine dalla pelle', time: '30 min', img: 'lifting-margine.svg', caption: 'Circa 1 mm di margine, uguale su base e lati.', imgs: ['lifting-mappa.svg'],
      goal: 'Applicare il prodotto lasciando un margine regolare di circa 1 mm dalla pelle.',
      materials: ['Mano da allenamento con "pelle" in silicone', 'Base o builder trasparente', 'Pennello', 'Lente d\'ingrandimento', 'Lampada'],
      steps: ['Applica la base su 5 dita fermandoti a circa 1 mm dalla pelle, sulla base e sui lati.', 'Prima della lampada controlla con la lente: correggi dove il prodotto tocca la pelle.', 'Polimerizza e passa un bastoncino lungo il bordo: non deve trovare scalini sulla pelle.', 'Fotografa dall\'alto e confronta il margine sulle 5 dita.'],
      checks: ['Il prodotto non tocca mai la pelle', 'Il margine è uguale su base e lati', 'Nessun prodotto nei solchi', 'Ho corretto prima della lampada'],
      mistakes: ['Margine enorme che lascia scoperta mezza unghia', 'Correggere dopo la polimerizzazione'] },
    { id: 'es-prezzo', module: 'professione', level: 'inter', title: 'Calcola il tuo prezzo', time: '30 min', img: 'calcolo-prezzo.svg', caption: 'Materiali + tempo + spese fisse + margine.', imgs: ['forfettario-esempio.svg'],
      goal: 'Calcolare un prezzo minimo sostenibile per ricostruzione e refill.',
      materials: ['Scontrini o listino dei prodotti', 'Calcolatrice o foglio di calcolo', 'I tempi cronometrati dei tuoi servizi', 'Prezzi di 3 centri della tua zona'],
      steps: ['Somma la spesa mensile in prodotti e dividila per le clienti del mese.', 'Decidi il tuo valore orario e stima le spese fisse all\'ora.', 'Calcola il prezzo minimo di ricostruzione e refill con i tuoi tempi reali.', 'Confronta con i prezzi della zona e scrivi cosa cambieresti (velocità, spese, servizi).'],
      checks: ['Ho usato tempi reali, non stimati', 'Ho incluso le spese fisse', 'Ho ricordato tasse e contributi', 'Il prezzo finale non è sotto il minimo calcolato'],
      mistakes: ['Copiare il prezzo più basso della zona', 'Dimenticare il tempo di pulizia e sterilizzazione'] },
    { id: 'es-onicofagia-cartina', module: 'onicofagia', level: 'avanz', title: 'Rifila la cartina per unghie rosicchiate', time: '30 min', img: 'onicofagia-cartina-adattata.svg', caption: 'Linguetta, taglio a U, lati a 45°, tira verso il basso.', imgs: ['onicofagia-semaforo.svg', 'onicofagia-proporzioni.svg'],
      goal: 'Imparare ad adattare la cartina a un bordo corto e irregolare senza lasciare spazi.',
      materials: ['Mano da allenamento o dita di una compagna (pelle integra)', 'Cartine e forbici piccole', 'Pennarello', 'Lente o smartphone per le foto'],
      steps: ['Con il pennarello disegna su 5 dita un bordo seghettato e un cuscinetto davanti all\'unghia.', 'Per ogni dito: taglia la linguetta, fai una U piccola, rifila i lati a 45°.', 'Applica la cartina a filo e tirala leggermente verso il basso; fotografa dalla punta.', 'Segna sulla cartina dove finirebbe un allungamento di circa 1/3; confronta con la tavola delle proporzioni.'],
      checks: ['Nessuno spazio tra bordo e cartina, visto dalla punta', 'Cartina in asse con il dito', 'Nessuna pressione dolorosa', 'Allungamento segnato non oltre circa 1/3'],
      mistakes: ['U troppo grande: la cartina non sostiene il prodotto', 'Cartina storta verso un lato'] },
    { id: 'es-pigmenti', module: 'cover-colori', level: 'inter', title: 'Test degli strati: sottile contro spesso', time: '35 min', img: 'pigmenti-luce.svg', caption: 'Lo stesso rosso, due spessori.', imgs: ['colore-strati-step.svg'],
      goal: 'Vedere con i tuoi occhi perché i gel pigmentati vanno stesi sottili.',
      materials: ['4 tip trasparenti', 'Base, un gel rosso o nero e un bianco, top', 'Lampada del sistema', 'Bastoncino in legno', 'Guanti in nitrile'],
      steps: ['Tip 1 e 2: rosso. Sul tip 1 due strati sottili, polimerizzati uno alla volta; sul tip 2 un solo strato spesso, stesso tempo totale di lampada.', 'Tip 3 e 4: stesso test con il bianco.', 'Dopo la lampada, con i guanti, premi delicatamente con il bastoncino sul retro del tip in trasparenza e osserva la superficie.', 'Annota: grinze, zone morbide, differenze tra rosso e bianco.'],
      checks: ['Tip sottili lisci e duri', 'Ho notato grinze o morbidezza sullo strato spesso', 'Ho confrontato rosso e bianco', 'Ho smaltito i tip come rifiuto, senza toccare il gel non polimerizzato'],
      mistakes: ['Toccare il gel non polimerizzato a mani nude', 'Allungare a caso i tempi invece di assottigliare'] },
    { id: 'es-pediluvio', module: 'piedi', level: 'base', title: 'Disinfetta e registra la vaschetta', time: '25 min', img: 'pediluvio-disinfezione.svg', caption: 'Svuota, pulisci, disinfetta, asciuga, registra.', imgs: ['pedicure-postazione.svg', 'piede-segnali-stop.svg'],
      goal: 'Eseguire e documentare la disinfezione della vaschetta come se fosse fine servizio.',
      materials: ['Vaschetta da pediluvio', 'Spazzola, sapone liquido', 'Disinfettante attivo su batteri, funghi e virus, con scheda tecnica', 'Timer', 'Carta monouso', 'Registro', 'Guanti in nitrile e occhiali'],
      steps: ['Leggi l\'etichetta del disinfettante: diluizione e tempo di contatto; scrivili sul registro.', 'Svuota, spazzola con sapone tutte le superfici, risciacqua.', 'Riempi con la soluzione disinfettante e avvia il timer per il tempo indicato (almeno 10 minuti se l\'etichetta non dice di più).', 'Svuota, risciacqua, asciuga con carta nuova; compila il registro con data, ora e sigla.'],
      checks: ['Diluizione corretta come da etichetta', 'Tempo di contatto rispettato con il timer', 'Nessun residuo visibile prima della disinfezione', 'Registro compilato in modo leggibile', 'DPI indossati durante la preparazione'],
      mistakes: ['Disinfettare senza aver prima pulito', 'Svuotare prima della fine del tempo di contatto'] },
    { id: 'es-scheda-gara', module: 'arte-gare', level: 'avanz', title: 'Valutati con una scheda vera', time: '45 min', img: 'gara-punteggio.svg', caption: 'Dove si vincono i punti.', imgs: ['gara-viste-giudice.svg', 'gara-scheda.svg'],
      goal: 'Imparare a giudicare il proprio lavoro con i criteri di una scheda punteggi ufficiale.',
      materials: ['3 unghie già costruite (tip su supporto o mano da allenamento)', 'Smartphone', 'Lente', 'Scheda dei criteri (tabella della lezione)'],
      steps: ['Fotografa ogni unghia dalle 5 viste del giudice, sempre con la stessa luce.', 'Assegna un voto a ogni criterio, usando i punti massimi della tabella.', 'Fai valutare le stesse foto a una collega, senza mostrarle i tuoi voti.', 'Confronta i punteggi e scegli i due criteri con più punti persi: scrivi un piano di allenamento di due settimane.'],
      checks: ['Foto da tutte e 5 le viste', 'Voto dato a ogni criterio', 'Confronto con una seconda valutazione', 'Piano scritto con due obiettivi concreti'],
      mistakes: ['Guardare solo dall\'alto', 'Voti generosi senza confronto'] }
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
      { q: 'Su unghie grasse il ritiro del gel è legato soprattutto a:', o: ['Lampada nuova', 'Olio residuo sulla lamina', 'Colori chiari', 'Cartine di carta'], a: 1, e: 'Disidratante, primer adatto e nuovo sgrassaggio prima della base.' },
      { q: 'Secondo una regola usata dai formatori, quanto dovrebbe essere lungo al massimo l\'allungamento su un\'unghia rosicchiata?', o: ['Il doppio del letto', 'Circa 1/3 della lunghezza della lamina', 'Uguale al letto', 'Non conta la lunghezza'], a: 1, e: 'Una leva lunga su un\'unghia piccola causa rotture e sollevamenti; si allunga poco alla volta.' },
      { q: 'Perché si taglia una piccola "U" nella cartina su un\'unghia rosicchiata?', o: ['Per risparmiare carta', 'Per non premere sull\'iponichio rialzato', 'Per fare la smile line', 'Per far colare il gel'], a: 1, e: 'Il cuscinetto di pelle è vivo: la U evita pressione e dolore.' },
      { q: 'Su un\'unghia rosicchiata resta uno spazio tra lamina e cartina. Cosa succede?', o: ['Niente', 'Il prodotto cola sotto e crea uno scalino debole e "mordibile"', 'Il gel polimerizza più in fretta', 'La curva C migliora'], a: 1, e: 'La cartina deve essere a filo del bordo, anche se il bordo quasi non c\'è.' },
      { q: 'Perché nelle prime settimane gli appuntamenti sono più ravvicinati?', o: ['Per vendere di più', 'Le ricostruzioni su unghie molto rosicchiate durano meno e vanno controllate spesso', 'Perché il gel scade', 'Non serve'], a: 1, e: 'Superficie di appoggio piccola e abitudine ancora presente: controlli frequenti, poi refill normali.' },
      { q: 'Un\'unghia mostra una banda scura longitudinale comparsa da poco. Cosa fai?', o: ['La copri con il cover', 'La limi', 'Consigli una visita dal medico', 'La ignori'], a: 2, e: 'Una banda scura nuova va sempre valutata dal medico: non spetta all\'onicotecnica dire da cosa dipende.' },
      { q: 'Con un\'unghia a cucchiaio, la cartina si posiziona:', o: ['Seguendo la conca', 'In asse con il dito, dopo aver livellato la conca', 'Verso l\'alto', 'Non si usa la cartina'], a: 1, e: 'Seguire la conca farebbe puntare l\'allungamento verso l\'alto.' }
    ],
    'cover-colori': [
      { q: 'A cosa serve principalmente il gel cover?', o: ['Lucidare', 'Allungare otticamente il letto ungueale e coprire imperfezioni', 'Sgrassare', 'Ammorbidire le cuticole'], a: 1, e: 'È un costruttore pigmentato color pelle.' },
      { q: 'Perché i gel molto pigmentati vanno stesi sottili?', o: ['Per risparmiare', 'Perché il pigmento assorbe la luce e gli strati profondi polimerizzano male', 'Per un effetto opaco', 'Non serve'], a: 1, e: 'Con strati spessi la parte profonda resta sotto-polimerizzata.' },
      { q: 'Il primo strato di un colore appare striato. È:', o: ['Un difetto del prodotto', 'Normale: il secondo strato uniforma', 'Segno di lampada rotta', 'Da rimuovere sempre'], a: 1, e: 'Molti colori coprono al secondo strato sottile.' },
      { q: 'Quale NON è una causa di ritiro dai bordi?', o: ['Olio sulla lamina', 'Primer ancora umido sui lati', 'Lampada non compatibile', 'Uso di una cartina di carta'], a: 3, e: 'Le prime tre sono cause tipiche di ritiro.' },
      { q: 'Il colore complementare del giallo, che lo neutralizza, è:', o: ['Viola', 'Verde', 'Arancio', 'Rosso'], a: 0, e: 'Sono opposti sul cerchio cromatico.' },
      { q: 'Per un french con camouflage, la sequenza consigliata è:', o: ['Bianco prima, cover dopo', 'Cover prima, poi la smile line', 'Solo top', 'Solo bianco'], a: 1, e: 'Si disegna la smile line sopra il cover.' },
      { q: 'Perché, in un french su letto allungato, si abbassano leggermente gli angoli della smile line?', o: ['Per risparmiare bianco', 'Per non lasciare zone trasparenti ai lati dove non c\'è cover', 'Per allungare il bordo', 'Non si abbassano mai'], a: 1, e: 'Se gli angoli salgono troppo, sotto il bianco restano piccole "orecchie" trasparenti.' },
      { q: 'Quali pigmenti assorbono più luce UV e sono più difficili da polimerizzare?', o: ['Bianco e blu', 'Rossi e neri', 'Solo i glitter', 'Tutti uguali'], a: 1, e: 'Rossi e neri assorbono di più: strati sottili e tempi da scheda tecnica.' },
      { q: 'Uno strato di colore molto spesso si raggrinzisce dopo la lampada. Perché?', o: ['La lampada è troppo nuova', 'La superficie indurisce ma sotto il gel resta morbido', 'Il colore è scaduto', 'Manca il top'], a: 1, e: 'La luce non arriva in fondo; un tempo più lungo non risolve uno strato troppo spesso.' },
      { q: 'Dove si sceglie il colore del cover?', o: ['Sotto la lampada UV', 'Alla luce naturale, appoggiando il tip sull\'unghia', 'Al buio', 'Solo dal catalogo'], a: 1, e: 'La luce naturale mostra il colore com\'è; si confronta con il letto ungueale.' },
      { q: 'Perché si "sigilla" il bordo libero passando il colore sullo spessore della punta?', o: ['Per decorare', 'Per ridurre ritiro e scheggiature in punta', 'Per accelerare la lampada', 'Non serve'], a: 1, e: 'Il colore avvolge il bordo e non si ritira.' },
      { q: 'Sotto uno smalto rosso o arancio, i dermatologi consigliano:', o: ['Nessuna base', 'Uno strato in più di base per evitare l\'ingiallimento', 'Il top prima del colore', 'Acetone'], a: 1, e: 'Indicazione dell\'American Academy of Dermatology.' }
    ],
    piedi: [
      { q: 'Rispetto alle mani, le unghie dei piedi crescono:', o: ['Più velocemente', 'Alla stessa velocità', 'A meno della metà della velocità', 'Non crescono'], a: 2, e: 'Circa 1,6 contro 3,5 mm al mese in uno studio su giovani adulti.' },
      { q: 'Per prevenire l\'unghia incarnita si taglia:', o: ['A punta', 'Molto corta e tonda', 'Dritta, angoli appena smussati', 'Scavando i lati'], a: 2, e: 'Indicazione dei dermatologi (AAD).' },
      { q: 'Un\'unghia gialla, ispessita e friabile:', o: ['Si copre con gel colorato', 'Si lima fino ad assottigliarla', 'Non si tratta: si consiglia medico o podologo', 'Si ricostruisce in acrilico'], a: 2, e: 'Possibile micosi: controindicazione.' },
      { q: 'Chi tratta le unghie incarnite in Italia?', o: ['L\'estetista', 'L\'onicotecnica', 'Il podologo (o il medico)', 'Chiunque abbia una lima'], a: 2, e: 'Il podologo è una professione sanitaria (DM 666/1994).' },
      { q: 'Cliente diabetica con una ferita al piede che non guarisce:', o: ['Pedicure con lama', 'Pediluvio caldo', 'Niente servizio, invio a medico o podologo', 'Semipermanente rinforzato'], a: 2, e: 'Rischio di lesioni non percepite e infezioni.' },
      { q: 'La L. 1/1990 esclude dall\'attività di estetista:', o: ['La manicure estetica', 'Le prestazioni con finalità terapeutica', 'Il trucco', 'Il massaggio estetico'], a: 1, e: 'L\'estetista lavora a scopo estetico.' },
      { q: 'Dopo ogni cliente, la vaschetta del pediluvio va:', o: ['Solo risciacquata', 'Svuotata, pulita con sapone, disinfettata per il tempo di contatto indicato, asciugata e registrata', 'Riempita con acqua calda', 'Spruzzata con profumo'], a: 1, e: 'Senza pulizia il disinfettante funziona male; il tempo di contatto (es. 10 minuti in California) va rispettato.' },
      { q: 'Che consiglio si dà alla cliente prima di una pedicure?', o: ['Radersi le gambe la mattina stessa', 'Non radersi le gambe nelle 24 ore prima', 'Mettere crema grassa sulle unghie', 'Venire con lo smalto vecchio'], a: 1, e: 'I microtagli del rasoio sono porte d\'ingresso per i germi.' },
      { q: 'Quanto tempo può servire perché un\'unghia dell\'alluce si rinnovi del tutto?', o: ['2 settimane', '1 mese', 'Fino a 12–18 mesi', '10 anni'], a: 2, e: 'Le unghie dei piedi crescono circa 1,6 mm al mese.' },
      { q: 'Con una cliente diabetica, la temperatura dell\'acqua si controlla:', o: ['Chiedendo alla cliente', 'Con il termometro o con il proprio gomito', 'Con la punta del piede della cliente', 'Non serve controllarla'], a: 1, e: 'Con la neuropatia la cliente può non sentire il calore e scottarsi.' },
      { q: 'Secondo il DM 666/1994, le callosità sono trattate da:', o: ['Estetista con lama', 'Podologo', 'Onicotecnica', 'Nessuno'], a: 1, e: 'Il podologo tratta con metodi incruenti callosità, unghie ipertrofiche, deformi e incarnite.' },
      { q: 'Perché i pediluvi con tubature di ricircolo sono considerati più a rischio?', o: ['Consumano più acqua', 'Nelle tubature possono crescere micobatteri difficili da eliminare', 'Sono più rumorosi', 'Non sono più a rischio'], a: 1, e: 'Indagine CDC in California: micobatteri in 29 vasche su 30.' }
    ],
    'arte-gare': [
      { q: 'Su cosa si applica la polvere chrome?', o: ['Gel colorato non polimerizzato', 'Top no-wipe polimerizzato', 'Base appiccicosa', 'Lamina nuda'], a: 1, e: 'Poi si sigillano i bordi e si mette il top.' },
      { q: 'Nel cat-eye il magnete si usa:', o: ['Dopo il top', 'Prima di polimerizzare lo strato magnetico', 'Dopo la polimerizzazione', 'Non serve'], a: 1, e: 'Le particelle si orientano finché il gel è fluido.' },
      { q: 'Nel one-stroke, per iniziare, il pennello piatto si carica:', o: ['Con un solo colore', 'Circa metà e metà con due colori', 'Fino alla ghiera', 'Asciutto'], a: 1, e: 'Il colore non deve entrare nella ghiera.' },
      { q: 'In gara, il gel non polimerizzato a fine prova comporta:', o: ['−5 punti', 'Nessuna penalità', 'Squalifica', 'Un bonus'], a: 2, e: 'È una regola tipica dei regolamenti Nailympia.' },
      { q: 'La "vista a tunnel" valuta soprattutto:', o: ['La smile line', 'La curva C', 'Il colore', 'La lucentezza'], a: 1, e: 'Si guarda l\'unghia dalla punta.' },
      { q: 'In un\'unghia con decorazione incapsulata, l\'apex:', o: ['Non serve', 'Si costruisce sopra la decorazione', 'Va alla cuticola', 'Si sostituisce con glitter'], a: 1, e: 'La struttura deve restare corretta.' },
      { q: 'Prima del top finale sul chrome, perché si passa un buffer leggero sul bordo libero?', o: ['Per accorciare l\'unghia', 'Per togliere la polvere libera che impedirebbe al top di aderire', 'Per opacizzare il chrome', 'Non si fa mai'], a: 1, e: 'La polvere libera sulla punta fa staccare il top.' },
      { q: 'Il gel per foil "non tiene" il foil. Causa probabile?', o: ['Strato troppo spesso o non polimerizzato abbastanza', 'Lampada troppo nuova', 'Foil troppo lucido', 'Colore sotto troppo chiaro'], a: 0, e: 'Serve un velo sottile, polimerizzato fino a restare appiccicoso.' },
      { q: 'Dove conviene incapsulare una decorazione?', o: ['Alla cuticola', 'Sui lati', 'Nelle zone spesse: smile line, apex, centro della punta', 'Sul bordo libero'], a: 2, e: 'Le zone sottili costringono a lasciare un rigonfiamento o a limare la decorazione.' },
      { q: 'In una gara Nailympia, cosa succede se pulisci le unghie della modella dopo lo stop?', o: ['Nulla', '−5 punti', 'Squalifica', 'Bonus di pulizia'], a: 2, e: 'Pulire mani o unghie con qualsiasi prodotto dopo la chiusura porta alla squalifica.' },
      { q: 'Nella scheda Nailympia 2026 French Twist 3 forme, quanto vale l\'apex?', o: ['30 punti da solo', '15 punti, valutato con la curva C dallo stesso giudice', '5 punti', 'Non è valutato'], a: 1, e: 'Il giudice 3 assegna 15 punti alla curva C e 15 all\'apex: 30 in tutto.' },
      { q: 'Il gel cat-eye va "flashato" pochi secondi subito dopo il magnete perché:', o: ['Si secca il pennello', 'Le particelle continuano a muoversi e il disegno si perde', 'Il magnete si scarica', 'Il top non serve'], a: 1, e: 'Un flash breve, un dito alla volta, fissa le particelle.' }
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
      { q: 'Una buona smile line è…', o: ['Asimmetrica', 'Simmetrica, netta e con la stessa profondità sui lati', 'Piatta', 'Sfumata'], a: 1, e: 'Simmetria e nettezza sono i criteri principali, e la smile deve essere uguale su tutte le dita.' },
      { q: 'Una smile line troppo piatta…', o: ['Allunga visivamente il letto', 'Fa sembrare l\'unghia più larga e corta', 'Non cambia nulla', 'Rende il bianco più coprente'], a: 1, e: 'La profondità della curva cambia la percezione: piatta allarga, troppo profonda sembra innaturale.' },
      { q: 'Quale curva di smile line è in genere più armoniosa?', o: ['Una linea dritta', 'Una curva che ripete quella della cuticola', 'Una curva diversa per ogni dito', 'Una curva che segue sempre il bordo libero naturale'], a: 1, e: 'La smile che "fa eco" alla cuticola è proporzionata; inoltre può stare più in alto del bordo naturale per allungare il letto.' },
      { q: 'Perché il gel bianco si stende in strati sottili?', o: ['Per risparmiare prodotto', 'Perché i pigmenti schermano la luce e uno strato spesso resta morbido sotto', 'Perché il bianco non si polimerizza mai', 'Per renderlo trasparente'], a: 1, e: 'È l\'effetto ombrello dei pigmenti: meglio due strati sottili ben polimerizzati.' },
      { q: 'Nel reverse french l\'arco di colore si disegna…', o: ['Sul bordo libero', 'Alla base, dal centro verso i lati, lasciando circa 1 mm dalla pelle', 'Toccando la cuticola per coprirla', 'Solo con lo stamping'], a: 1, e: 'Partire dal centro aiuta la regolarità; il margine evita sollevamenti e contatto con la pelle.' },
      { q: 'Il baby boomer è…', o: ['Un french con linea netta', 'Una sfumatura dal nude al bianco', 'Un tipo di gel', 'Una forma'], a: 1, e: 'È un french sfumato, senza linea netta.' },
      { q: 'Nel baby boomer la sfumatura si ottiene soprattutto…', o: ['Limando forte la zona di passaggio', 'Con il pennello, a colpi brevi e strati sottili', 'Con un solo strato spesso di bianco', 'Con il top coat'], a: 1, e: 'La lima assottiglia la zona sfumata e crea macchie; la sfumatura si costruisce con il pennello.' },
      { q: 'L\'incapsulato consiste nel…', o: ['Chiudere decorazioni tra due strati trasparenti', 'Mettere glitter sul top', 'Usare solo colori', 'Dipingere con il dotter'], a: 0, e: 'Le decorazioni restano protette dentro il prodotto, con l\'apex costruito sopra.' },
      { q: 'Lo stamping usa…', o: ['Una piastra incisa e un tampone', 'Una fresa', 'Un attivatore', 'Solo pennelli'], a: 0, e: 'Il disegno viene trasferito dalla piastra all\'unghia con il tampone.' },
      { q: 'Nello stamping il raschietto si passa…', o: ['In verticale premendo forte', 'A circa 45° per lasciare lo smalto solo nelle incisioni', 'Dopo il tampone', 'Solo se lo smalto è già secco'], a: 1, e: 'Poi si rotola subito il tampone sul disegno e sull\'unghia.' }
    ],
    manutenzione: [
      { q: 'Ogni quanto si consiglia il refill di una ricostruzione?', o: ['Ogni settimana', 'Ogni 3–4 settimane', 'Ogni 3 mesi', 'Mai'], a: 1, e: 'Dopo 3–4 settimane l\'apex si è spostato in avanti; il semipermanente si rifà in genere ogni 2–3 settimane.' },
      { q: 'Di quanto cresce in media un\'unghia della mano in un mese?', o: ['Circa 0,5 mm', 'Circa 3–3,5 mm', 'Circa 1 cm', 'Circa 2 cm'], a: 1, e: 'In uno studio su giovani adulti la media era 3,47 mm al mese: poco meno di 1 mm a settimana.' },
      { q: 'Durante il refill le parti sollevate…', o: ['Si coprono con prodotto nuovo', 'Si eliminano completamente', 'Si incollano', 'Si lasciano'], a: 1, e: 'Sotto un sollevamento possono esserci umidità e batteri.' },
      { q: 'Come si elimina un sollevamento durante il refill?', o: ['Si taglia con la tronchesina', 'Si lima fino al punto in cui il prodotto è ben attaccato', 'Si incolla', 'Si copre con prodotto nuovo'], a: 1, e: 'Tagliare o strappare porta via strati di lamina e crea nuovi sollevamenti.' },
      { q: 'Durante il rebalance il vecchio prodotto si assottiglia indicativamente…', o: ['Per niente', 'Del 30–50%, in base alla ricrescita', 'Fino all\'unghia naturale', 'Solo sul bordo libero'], a: 1, e: 'Così si può ricostruire l\'apex nel punto giusto senza rendere l\'unghia sempre più spessa.' },
      { q: 'Una cliente ha una crepa nel prodotto: cosa le consigli fino all\'appuntamento?', o: ['Incollarla con colla per tip', 'Coprirla con un cerotto', 'Non incollare né coprire, limare via la parte che si aggancia e prenotare la riparazione', 'Strappare il prodotto'], a: 2, e: 'Colla e cerotto chiudono umidità e batteri sotto il prodotto.' },
      { q: 'Quanto tempo serve in genere per il soak-off del semipermanente?', o: ['1 minuto', '10–15 minuti', '2 ore', '24 ore'], a: 1, e: 'Per soft gel spessi si arriva a circa 30 minuti; l\'acrilico richiede in genere 20–30 minuti.' },
      { q: 'Quale tempo in acetone è più realistico per un acrilico già assottigliato?', o: ['1–2 minuti', '20–30 minuti', '2 ore', 'Non si scioglie'], a: 1, e: 'Il semipermanente richiede meno tempo (circa 10–15 min); l\'hard gel invece non si scioglie e si lima.' },
      { q: 'L\'hard gel si rimuove…', o: ['Con acetone', 'Limando, lasciando un velo sulla lamina', 'Strappandolo', 'Con acqua calda'], a: 1, e: 'Non si scioglie in acetone.' },
      { q: 'La lamina biancastra subito dopo un soak-off è di solito…', o: ['Un danno permanente', 'Disidratazione superficiale temporanea', 'Una micosi', 'Prodotto rimasto'], a: 1, e: 'Si recupera in alcune ore; i danni veri vengono dal raschiare o dal fare leva.' },
      { q: 'Dopo la rimozione…', o: ['Si gratta la lamina', 'Si applica olio per cuticole', 'Si mette subito un nuovo gel senza preparare', 'Si lima con grana 80'], a: 1, e: 'Nutrire la zona aiuta la pelle e la lamina.' }
    ],
    problemi: [
      { q: 'Quale NON è una causa di sollevamento?', o: ['Cuticola non rimossa dalla lamina', 'Prodotto a contatto con la pelle', 'Bordo libero sigillato', 'Refill in ritardo'], a: 2, e: 'Sigillare il bordo libero previene il sollevamento.' },
      { q: 'Un sollevamento al centro dell\'unghia ("a tasca") fa pensare soprattutto a…', o: ['Bordo libero non sigillato', 'Adesione scarsa, perla sbagliata o una botta', 'Prodotto sui solchi laterali', 'Lampada troppo lenta'], a: 1, e: 'Il centro non è vicino alla pelle: le cause tipiche sono adesione, rapporto liquido/polvere e traumi.' },
      { q: 'Quanto margine si lascia indicativamente tra prodotto e pelle?', o: ['Nessuno', 'Circa 1 mm', 'Circa 3 mm', 'Metà unghia'], a: 1, e: 'Le fonti indicano 0,5–1,5 mm: il prodotto sulla pelle non aderisce, fa leva e aumenta il rischio di allergia.' },
      { q: 'Il sollevamento compare su tutte le dita di una cliente dopo pochi giorni. Prima cosa da controllare?', o: ['Le abitudini della cliente', 'La tua preparazione e applicazione', 'Il colore scelto', 'La forma'], a: 1, e: 'Tutte le dita + subito = protocollo, prodotto o lampada.' },
      { q: 'Una rottura in zona 2 dipende spesso da…', o: ['Apex assente o mal posizionato', 'Troppo olio', 'Colore scuro', 'Top lucido'], a: 0, e: 'La struttura deve reggere il punto di stress.' },
      { q: 'Il picco di calore è favorito da…', o: ['Strati sottili', 'Strati spessi e lamina assottigliata', 'Gel a basso calore', 'Lampada in low-heat'], a: 1, e: 'La polimerizzazione è esotermica: strati spessi = più calore.' },
      { q: 'Perché un gel non abbinato alla lampada può scottare di più?', o: ['Perché la lampada è spenta', 'Perché libera lo stesso calore in molto meno tempo', 'Perché il gel diventa più spesso', 'Non scotta mai'], a: 1, e: 'Una lampada molto veloce concentra la reazione: il calore arriva tutto insieme.' },
      { q: 'La tecnica "flash and pull" serve a…', o: ['Accelerare la polimerizzazione', 'Ridurre il calore percepito', 'Rimuovere il gel', 'Lucidare'], a: 1, e: 'Si toglie la mano dalla lampada qualche secondo e la si rimette.' },
      { q: 'Le grinze sul gel indicano di solito…', o: ['Strato troppo spesso polimerizzato solo in superficie', 'Troppo primer', 'Lima sbagliata', 'Smile line storta'], a: 0, e: 'Strati sottili e tempi corretti risolvono il problema.' },
      { q: 'Un colore scuro steso spesso fa le grinze perché…', o: ['È scaduto', 'I pigmenti fanno ombra e la luce non arriva negli strati sotto', 'Il top è opaco', 'L\'unghia è troppo corta'], a: 1, e: 'Si forma una pelle dura sopra il gel liquido: la soluzione sono strati sottili.' },
      { q: 'Un gel sotto-polimerizzato aumenta il rischio di…', o: ['Ingiallimento soltanto', 'Allergia', 'Unghie più dure', 'Nessun problema'], a: 1, e: 'Il monomero non reagito sensibilizza la pelle.' },
      { q: 'Una cliente ha prurito e rossore intorno alle unghie dopo il servizio. Cosa fai?', o: ['Aggiungi un altro strato', 'Interrompi, rimuovi con delicatezza e consigli il medico', 'Le dai una crema e continui', 'Aspetti il refill'], a: 1, e: 'Può essere una dermatite allergica da contatto: annotala sulla scheda e rivedi la tecnica.' }
    ],
    professione: [
      { q: 'Cosa NON serve nella scheda cliente?', o: ['Allergie', 'Farmaci e patologie', 'Il colore preferito dell\'auto', 'Consenso privacy'], a: 2, e: 'La scheda raccoglie dati utili alla sicurezza del servizio.' },
      { q: 'Allergie, farmaci e gravidanza scritti nella scheda cliente sono…', o: ['Dati qualunque', 'Dati relativi alla salute, protetti in modo particolare dal GDPR', 'Dati pubblici', 'Dati fiscali'], a: 1, e: 'Sono "categorie particolari" (art. 9 GDPR): servono informativa, consenso esplicito e custodia sicura.' },
      { q: 'Per pubblicare sui social la foto delle mani di una cliente serve…', o: ['Niente, se le unghie le ho fatte io', 'Un consenso separato e specifico, che la cliente può rifiutare', 'Solo la firma sulla scheda del servizio', 'Il permesso del Comune'], a: 1, e: 'La foto non è necessaria al servizio: serve un consenso a parte. Garante e Cassazione si sono espressi su casi simili.' },
      { q: 'Quale consiglio dai dopo il trattamento?', o: ['Usare le unghie per aprire le lattine', 'Olio per cuticole ogni giorno e guanti per i lavori domestici', 'Staccare da sola il prodotto', 'Saltare il refill'], a: 1, e: 'Cura quotidiana e protezione allungano la durata.' },
      { q: 'Quale foto mostra meglio la posizione dell\'apex?', o: ['Dall\'alto', 'Di profilo', 'Da lontano con la cliente in posa', 'Con un filtro colorato'], a: 1, e: 'Dall\'alto si vedono forma e smile line; a tunnel la curva a C; di profilo apex e spessore.' },
      { q: 'Prezzo indicativo di un refill in Italia?', o: ['5 €', '25–35 €', '150 €', '300 €'], a: 1, e: 'Ordine di grandezza da articoli e testimonianze 2021–2025; i prezzi variano molto per zona e centro.' },
      { q: 'Come si calcola il costo dei materiali per servizio?', o: ['Prezzo del gel diviso per 10', 'Spesa mensile per i prodotti divisa per il numero di clienti del mese', 'Si copia il prezzo della concorrenza', 'Non serve calcolarlo'], a: 1, e: 'Meglio fare la media su più mesi per tener conto dei periodi più o meno pieni.' },
      { q: 'Nel regime forfettario, su cosa si calcolano imposta e contributi di un\'estetista?', o: ['Su tutti gli incassi', 'Sul 67% degli incassi (coefficiente di redditività)', 'Solo sugli incassi in contanti', 'Sul guadagno dopo aver tolto le spese reali'], a: 1, e: 'Le spese reali non si scaricano: sono comprese forfettariamente nel 33% non tassato.' },
      { q: 'I contributi INPS fissi degli artigiani…', o: ['Si pagano solo se si guadagna più di 85.000 €', 'Si pagano sul minimale anche se si guadagna meno', 'Non esistono in forfettario', 'Si pagano una volta sola all\'apertura'], a: 1, e: 'Nel 2026 il minimale è 18.808 € e i contributi fissi circa 4.521 € l\'anno; i forfettari possono chiedere la riduzione del 35%.' },
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
    { t: 'Incapsulato', d: 'Decorazione piatta chiusa tra due strati di prodotto trasparente, con l\'apex costruito sopra.' },
    { t: 'Lamina ungueale', d: 'La placca dura di cheratina che chiamiamo comunemente unghia.' },
    { t: 'Letto ungueale', d: 'Tessuto vascolarizzato su cui poggia la lamina.' },
    { t: 'Lifting (sollevamento)', d: 'Distacco del prodotto dalla lamina: il punto in cui si stacca (base, lati, punta, centro) suggerisce la causa.' },
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
    { t: 'Refill', d: 'Riempimento della ricrescita (per le ricostruzioni in genere ogni 3–4 settimane), con riequilibrio della struttura e nuovo apex.' },
    { t: 'SCIA', d: 'Segnalazione certificata di inizio attività da presentare al Comune/SUAP.' },
    { t: 'Semipermanente', d: 'Smalto in gel che polimerizza in lampada e dura 2–3 settimane.' },
    { t: 'Slip solution', d: 'Liquido per lavorare il polygel con il pennello senza che si attacchi.' },
    { t: 'Smile line', d: 'Linea che separa la parte bianca del french dal resto dell\'unghia.' },
    { t: 'Soak-off', d: 'Rimozione con acetone (cotone e stagnola o clip) dopo aver tolto il top e assottigliato il prodotto; non funziona sull\'hard gel.' },
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
    { t: 'Buffer', d: 'Blocchetto o lima morbida a grana fine per levigare la superficie.' },
    { t: 'Punti laterali (smile line)', d: 'I due punti in cui la smile line tocca i lati dell\'unghia: devono essere alla stessa altezza.' },
    { t: 'Pink & white', d: 'French scolpito in gel o acrilico: bianco per la punta e rosa/cover per il letto, entrambi parte della struttura.' },
    { t: 'Reverse french', d: 'Variante del french con un arco di colore alla base dell\'unghia, a circa 1 mm dalla cuticola.' },
    { t: 'V-french', d: 'French con la punta a forma di V (chevron) invece della curva.' },
    { t: 'Micro french', d: 'French con una linea sottilissima solo sul bordo libero.' },
    { t: 'Smalto da stamping', d: 'Smalto più denso e coprente, adatto a riempire le incisioni della piastra; asciuga in pochi secondi.' },
    { t: 'Raschietto (scraper)', d: 'Lamina a bordo dritto che toglie lo smalto in eccesso dalla piastra da stamping.' },
    { t: 'Tampone (stamper)', d: 'Testina morbida che raccoglie il disegno dalla piastra e lo trasferisce sull\'unghia rotolando.' },
    { t: 'Rebalance (riequilibrio)', d: 'Refill in cui si assottiglia il vecchio prodotto e si ricostruisce l\'apex nella posizione corretta.' },
    { t: 'Backfill', d: 'Refill del french scolpito in cui si toglie il vecchio bianco e si rifà la smile line nella posizione giusta.' },
    { t: 'Ricrescita', d: 'La parte di unghia naturale cresciuta tra la cuticola e il prodotto dopo l\'ultimo servizio.' },
    { t: 'File-off', d: 'Rimozione solo meccanica, con lima o fresa, per i prodotti che non si sciolgono in acetone (per esempio l\'hard gel).' },
    { t: 'Gradino', d: 'Scalino tra il vecchio prodotto e la ricrescita: va raccordato perché si aggancia e favorisce il sollevamento.' },
    { t: 'Nipping', d: 'Tagliare con la tronchesina il prodotto sollevato: da evitare, perché strappa strati di lamina.' },
    { t: 'Pocket lifting (sollevamento a tasca)', d: 'Distacco al centro dell\'unghia, lontano dai bordi; spesso legato ad adesione, rapporto liquido/polvere o traumi.' },
    { t: 'Margine libero', d: 'Il filo di unghia naturale (circa 1 mm; le fonti indicano 0,5–1,5 mm) lasciato senza prodotto vicino alla cuticola e ai solchi.' },
    { t: 'Effetto ombrello', d: 'I pigmenti e i glitter fanno ombra alla luce della lampada, che arriva meno negli strati profondi.' },
    { t: 'Reazione esotermica', d: 'Reazione chimica che libera calore, come la polimerizzazione di gel e acrilico.' },
    { t: 'Dermatite allergica da contatto', d: 'Reazione della pelle (prurito, rossore, vescicole) a una sostanza a cui ci si è sensibilizzati, per esempio gli acrilati non polimerizzati.' },
    { t: 'Grinze (wrinkling)', d: 'Superficie raggrinzita del gel: la parte sopra si indurisce mentre quella sotto resta liquida.' },
    { t: 'Dati relativi alla salute', d: 'Informazioni sulla salute di una persona (allergie, farmaci, gravidanza…): per il GDPR sono categorie particolari e richiedono tutele maggiori.' },
    { t: 'Informativa privacy', d: 'Documento che spiega alla cliente chi tratta i suoi dati, perché, per quanto tempo e quali diritti ha (art. 13 GDPR).' },
    { t: 'Consenso esplicito', d: 'Consenso chiaro e specifico, di solito scritto e firmato, necessario per esempio per trattare dati sulla salute o pubblicare foto.' },
    { t: 'Registro dei trattamenti', d: 'Elenco scritto dei trattamenti di dati personali svolti dall\'attività (art. 30 GDPR).' },
    { t: 'Codice ATECO', d: 'Codice che classifica l\'attività economica all\'apertura della partita IVA; per manicure e pedicure, nella classificazione 2025, risulta 96.22.01.' },
    { t: 'Regime forfettario', d: 'Regime fiscale semplificato per ricavi fino a 85.000 €: imposta del 5% o 15% su una parte forfettaria degli incassi.' },
    { t: 'Coefficiente di redditività', d: 'Percentuale degli incassi considerata reddito nel regime forfettario: 67% per i servizi alla persona.' },
    { t: 'Minimale INPS', d: 'Reddito minimo su cui gli artigiani pagano comunque i contributi fissi (18.808 € nel 2026).' },
    { t: 'SUAP', d: 'Sportello unico per le attività produttive del Comune, a cui si presenta la SCIA.' },
    { t: 'Aftercare', d: 'Consigli post-trattamento dati alla cliente per far durare il lavoro e proteggere l\'unghia naturale.' },
    { t: 'Iponichio esteso', d: 'Iponichio che, su unghie rosicchiate, si ispessisce, si alza e "avanza" sotto il bordo. È pelle viva: non si taglia, si abbassa con la cartina.' },
    { t: 'Habit reversal training', d: 'Terapia di inversione dell\'abitudine: tecnica comportamentale usata da medici e psicologi contro onicofagia e simili. L\'onicotecnica può solo suggerire di parlarne con il medico.' },
    { t: 'Smalto amaro', d: 'Smalto dal sapore amaro pensato per scoraggiare il morso delle unghie. Aiuto possibile, non una cura.' },
    { t: 'Patereccio erpetico', d: 'Infezione da virus herpes intorno all\'unghia, con vescicole dolorose. Controindicazione: si invia al medico.' },
    { t: 'Paronichia cronica', d: 'Infiammazione della piega intorno all\'unghia che dura settimane: piega gonfia, cuticola assente. Frequente in chi morde le pellicine o tiene spesso le mani in acqua. Si invia al medico.' },
    { t: 'Tinta, luminosità, saturazione', d: 'Le tre proprietà del colore: il "nome" del colore, quanto è chiaro o scuro, quanto è intenso o spento.' },
    { t: 'Colori analoghi', d: 'Colori vicini sul cerchio cromatico (es. rosa, corallo, pesca). Insieme danno un effetto armonioso.' },
    { t: 'Gel jelly', d: 'Gel o semipermanente colorato traslucido, che lascia vedere sotto. Più strati = colore più intenso.' },
    { t: 'Fotoiniziatore', d: 'Ingrediente del gel che, colpito dalla luce UV/LED della lunghezza d\'onda giusta, avvia l\'indurimento.' },
    { t: 'Cartella colori', d: 'Raccolta di tip campione, uno per colore, stesi come in cabina e numerati, per scegliere il colore con la cliente.' },
    { t: 'Dermatofiti', d: 'Gruppo di funghi che si nutrono di cheratina (pelle, unghie, capelli). Causano la maggior parte delle micosi delle unghie dei piedi; il più comune è Trichophyton rubrum.' },
    { t: 'Tempo di contatto', d: 'Tempo minimo per cui una superficie deve restare bagnata dal disinfettante perché questo agisca. È scritto in etichetta.' },
    { t: 'Neuropatia periferica', d: 'Danno ai nervi delle estremità, frequente nel diabete: riduce la sensibilità al dolore e al calore. Chi ne soffre può ferirsi senza accorgersene.' },
    { t: 'Unghia ipertrofica', d: 'Unghia molto ispessita, a volte ricurva "a corno". Competenza del podologo.' },
    { t: 'Separadita', d: 'Divisori morbidi, di solito monouso, che allargano le dita dei piedi durante il colore.' },
    { t: 'Registro di disinfezione', d: 'Quaderno o modulo in cui si annotano data, ora e sigla di chi ha disinfettato vaschette e strumenti.' },
    { t: 'Hair line', d: 'Nelle gare: lo spessore del bordo libero visto dalla punta. Deve essere sottile come un capello e uniforme su tutte le unghie.' },
    { t: 'Scheda punteggi (score sheet)', d: 'Documento ufficiale di una categoria di gara con criteri, punti e giudice responsabile di ciascuno.' },
    { t: 'Giudice di sala (floor judge)', d: 'Giudice che controlla tavoli, prodotti e rispetto delle regole durante la gara; può togliere punti o squalificare.' },
    { t: 'Inlay', d: 'Decorazione inserita dentro l\'allungamento (per esempio una smile line creativa o un fiore incapsulato), tipica di alcune categorie di gara.' },
    { t: 'Transfer foil', d: 'Sottile lamina decorativa che si trasferisce sull\'unghia premendola su un gel o una colla appiccicosa.' },
    { t: 'Ombré', d: 'Sfumatura graduale tra due o più colori, fatta con il pennello o con la spugnetta.' },
    { t: 'Velvet (cat-eye)', d: 'Effetto "velluto" del gel magnetico: luce diffusa su tutta l\'unghia, ottenuta muovendo il magnete.' }
  ];

  // esercizi ordinati secondo l'ordine dei moduli
  var order = {};
  modules.forEach(function (m, i) { order[m.id] = i; });
  exercises.sort(function (a, b) { return order[a.module] - order[b.module]; });

  window.NAILX = { modules: modules, exercises: exercises, quiz: quiz, glossary: glossary };
})();
