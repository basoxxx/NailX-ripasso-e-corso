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
      id: 'preparazione', summary: ["Igiene → cuticola → pterigio → opacizza → polvere → disidratante → primer.", "Opacizzare non significa assottigliare.", "Primer: poco prodotto, solo sulla lamina, mai sulla pelle.", "Dopo il disidratante non toccare più la lamina."], n: 5, level: 'base', title: 'Preparazione dell\'unghia',
      desc: 'Il passaggio che decide se la ricostruzione tiene o si solleva.',
      lessons: [
        {
          id: 'passaggi', videos: [{"id": "tyZfOTu6T70", "title": "Nail prep: passaggi di preparazione unghie", "channel": "Proglow Italia", "lang": "IT"}], simple: "Prima di costruire, l'unghia va pulita, asciutta e leggermente ruvida: così il prodotto \"si aggrappa\".", title: 'I passaggi della preparazione', min: 7,
          html: `
<p>La preparazione è la <strong>prima causa</strong> di tenuta o di sollevamento. Va fatta con calma, ogni volta.</p>
${F('preparazione.svg', 'Preparazione in sei passaggi.')}
<ol class="steps">
<li><strong>Igienizza</strong> le tue mani e quelle della cliente; consulenza e analisi dell'unghia.</li>
<li><strong>Arretra la cuticola</strong> con lo spingicuticole, delicatamente.</li>
<li><strong>Rimuovi il pterigio</strong>, la pellicina morta aderente alla lamina.</li>
<li><strong>Opacizza</strong> leggermente con grana 180–240: togli solo la lucidità, non assottigliare.</li>
<li><strong>Elimina la polvere</strong> con un pennello pulito.</li>
<li><strong>Disidratante</strong> e poi <strong>primer</strong> (vedi lezione successiva).</li>
</ol>
${F('cuticola.svg', 'Nella zona cuticolare si arretra e si rimuove solo la pelle morta.')}
${B('warn', 'Da non fare', 'Non toccare la lamina con le dita dopo il disidratante: il sebo della pelle riduce l\'adesione.')}
`,
          sources: ['https://www.katiebarnesacademy.com/blogs/preparation/what-is-the-difference-between-acid-free-and-acid-based-nail-primer']
        },
        {
          id: 'primer', videos: [{"id": "TFk5uRlLXdA", "title": "Liquidi di preparazione: nomi e differenze", "channel": "Accademia Nails", "lang": "IT"}], simple: "Il disidratante asciuga l'unghia, il primer fa da colla. Ne basta pochissimo.", title: 'Disidratante e primer', min: 5,
          html: `
<ul>
<li><strong>Disidratante (nail prep)</strong>: toglie umidità e sebo. Si applica <em>prima</em> del primer, non al suo posto.</li>
<li><strong>Primer acido</strong>: "incide" la lamina. Indicato per acrilico e unghie difficili. Pochissimo prodotto, solo sulla lamina, mai ripetuto (la assottiglia).</li>
<li><strong>Primer senza acido</strong>: funziona come un "biadesivo" tra lamina e prodotto. Indicato per gel e semipermanente. Anche qui poco prodotto: l'eccesso riduce l'adesione.</li>
</ul>
${B('danger', 'Pelle', 'Il primer non deve mai toccare la pelle. Lascia asciugare secondo le istruzioni prima di procedere.')}
`,
          sources: ['https://dilei.it/bellezza/primer-unghie-cos-e-e-a-cosa-serve/568373/']
        }
      ]
    },
    /* ------------------------------------------------------------------ 6 */
    {
      id: 'tip', summary: ["Il tip copre da solco a solco: se in dubbio, misura più grande.", "Si appoggia a ~45° e si abbassa per far uscire l'aria.", "Si fonde solo la linea di contatto, mai l'unghia naturale.", "Sul tip si costruisce comunque l'apex in zona 2."], n: 6, level: 'inter', title: 'Ricostruzione su tip',
      desc: 'Scegliere, applicare, tagliare e fondere il tip; copertura in gel.',
      lessons: [
        {
          id: 'applicazione', videos: [{"id": "mCY3EVijhjw", "title": "Come applicare una tip dopo aver preparato l'unghia", "channel": "Naio Nails IT", "lang": "IT"}, {"id": "hJCElOAO23k", "title": "Ricostruzione unghie con tip in gel", "channel": "Mondo NAILS", "lang": "IT"}], title: 'Applicazione del tip', min: 7,
          html: `
${F('tip-applicazione.svg', 'Applicazione del tip in quattro passaggi.')}
<h2>Tipi di tip</h2>
<ul>
<li><strong>Con incavo (well)</strong>: hanno una zona di appoggio da incollare sul bordo libero; poi va fusa.</li>
<li><strong>A contatto (contact)</strong>: senza incavo, non serve fondere.</li>
</ul>
${F('tip-tipi.svg', 'Tipi di tip e misure: lo 0 è il più largo.')}
<h2>Procedimento</h2>
<ol class="steps">
<li><strong>Misura</strong>: il tip deve coprire l'unghia da solco laterale a solco laterale. Se sei tra due misure, scegli la più grande e lima i lati.</li>
<li><strong>Incolla</strong> con poca colla nell'incavo, appoggia sul bordo libero a circa 45° e abbassa lentamente per far uscire l'aria. Tieni premuto qualche secondo.</li>
<li><strong>Taglia</strong> con il tagliatip alla lunghezza desiderata.</li>
<li><strong>Fondi</strong> la linea di contatto con la lima finché non si vede più il gradino, <strong>senza limare l'unghia naturale</strong>.</li>
</ol>
${B('tip', 'Controllo', 'Guarda il tip di profilo e dal davanti: deve essere in asse con il dito e senza bolle sotto.')}
`,
          sources: []
        },
        {
          id: 'copertura', title: 'Costruzione in gel sul tip', min: 6,
          html: `
<ol class="steps">
<li>Disidratante e primer sulla sola unghia naturale.</li>
<li>Base sottile su unghia e tip, polimerizza.</li>
<li>Costruttore: una prima passata sottile, poi la "perla" di gel al centro per costruire l'<strong>apex</strong> in zona 2.</li>
<li>Lascia livellare qualche secondo; capovolgi la mano un istante per far scorrere il gel verso l'apex, poi polimerizza.</li>
<li>Sigilla il bordo libero a ogni strato.</li>
<li>Limatura, forma, cleaner e top.</li>
</ol>
${F('zone-costruzione.svg', 'Le tre zone: sottile alla cuticola, struttura in zona 2, sottile in punta.')}
`,
          sources: []
        }
      ]
    },
    /* ------------------------------------------------------------------ 7 */
    {
      id: 'cartina', summary: ["Cartina a filo del bordo libero e in asse.", "Zona 3 sottile (≈1,5 mm dalla pelle), zona 2 apex, zona 1 sottile in punta.", "Apex sopra il punto di stress: controlla sempre di profilo.", "Curva a C: pinching senza dolore, seguendo la curva naturale."], n: 7, level: 'inter', title: 'Ricostruzione su cartina e apex',
      desc: 'Posizionare la cartina, costruire le 3 zone, l\'apex e la curva a C.',
      lessons: [
        {
          id: 'posizionamento', title: 'Posizionare la cartina', min: 5,
          html: `
${F('cartina.svg', 'Cartina corretta ed errori comuni.')}
<ul>
<li>La cartina va <strong>a filo</strong> del bordo libero, senza spazi.</li>
<li>Deve essere <strong>in asse</strong> con il dito: guarda la mano dall'alto e di lato.</li>
<li>Chiudi bene le alette sotto il polpastrello per mantenere la curva.</li>
</ul>
${B('warn', 'Errore classico', 'Uno spazio tra cartina e bordo libero fa colare il prodotto sotto l\'unghia: crea sollevamenti e un "gradino" difficile da correggere.')}
`,
          sources: []
        },
        {
          id: 'zone-apex', videos: [{"id": "Tx3lwXOS0L0", "title": "Do's and Don'ts of Apex Structure", "channel": "YoungNailsInc", "lang": "EN"}, {"id": "PD1qHAO3cvk", "title": "How to Build the Perfect Apex", "channel": "Liz Means Business", "lang": "EN"}], simple: "Immagina un ponte: dove l'unghia lascia il dito (punto di stress) serve il pilastro più alto, cioè l'apex.", title: 'Le tre zone e l\'apex', min: 8,
          html: `
${F('zone-costruzione.svg', 'Le tre zone di costruzione.')}
<ul>
<li><strong>Zona 1 – bordo libero</strong>: spessore moderato che si assottiglia verso la punta.</li>
<li><strong>Zona 2 – apex</strong>: la parte più spessa, il "ponte" che regge la lunghezza. L'apex va costruito <strong>sopra il punto di stress</strong>.</li>
<li><strong>Zona 3 – cuticola</strong>: sottilissima, con circa <strong>1,5 mm</strong> di margine dalla pelle.</li>
</ul>
${F('apex-confronto.svg', 'Apex corretto e due errori tipici.')}
${B('tip', 'Come controllarlo', 'Guarda l\'unghia di profilo: la linea deve salire dolcemente dalla cuticola, raggiungere il punto più alto sopra il punto di stress e scendere verso la punta. Guarda anche dal davanti: lo spessore deve essere uniforme da lato a lato.')}
`,
          sources: ['https://open-exam-prep.com/study-guides/oh-nail-technician/artificial-nail-services/sculptured-acrylic-nails']
        },
        {
          id: 'curva-c', simple: "Guardando l'unghia dalla punta deve sembrare un piccolo arco, come una \"C\" sdraiata.", title: 'La curva a C (pinching)', min: 5,
          html: `
${F('curva-c.svg', 'La curva a C vista dal bordo libero.')}
<p>La curva a C è la curvatura trasversale della ricostruzione vista dalla punta. Dà resistenza e un aspetto naturale.</p>
<ul>
<li><strong>Acrilico</strong>: si "pizzica" mentre il prodotto non è ancora del tutto indurito.</li>
<li><strong>Gel</strong>: si pizzica dopo una polimerizzazione breve (flash cure) di pochi secondi.</li>
</ul>
${B('danger', 'Mai dolore', 'Il pinching non deve far male né staccare la lamina dal letto. Non esiste una percentuale di curva valida per tutti: si segue la curva naturale della cliente.')}
`,
          sources: []
        },
        {
          id: 'tutorial-gel', videos: [{"id": "ilkQqQbeCQQ", "title": "Ricostruzione unghie con cartine e gel: ogni passaggio spiegato", "channel": "Valeriya Nails", "lang": "IT"}, {"id": "jOJjB8vjEg0", "title": "Sculpting Gel Nails – Step by Step", "channel": "Nail Career Education", "lang": "EN"}], title: 'Tutorial completo: gel su cartina', min: 10,
          html: `
<p>Questo tutorial mette insieme tutto ciò che hai studiato: preparazione, cartina, tre zone, apex e rifinitura. Esercitati prima su una mano da allenamento.</p>
${F('tut-gel-cartina.svg', 'Ricostruzione in gel su cartina in otto passaggi.')}
<ol class="steps">
<li><strong>Prepara</strong>: igiene, cuticola e pterigio, opacizzazione 180–240, polvere via, disidratante e primer.</li>
<li><strong>Cartina</strong>: a filo del bordo libero, in asse, alette chiuse.</li>
<li><strong>Base</strong>: uno strato sottile su tutta la lamina, senza toccare la pelle. Polimerizza.</li>
<li><strong>Zona 1</strong>: con il costruttore disegna l'allungamento sulla cartina, sottile e alla lunghezza voluta; polimerizza brevemente.</li>
<li><strong>Zona 2</strong>: appoggia una perla di gel al centro e accompagnala verso i lati e verso la cuticola, lasciando circa 1,5 mm di margine.</li>
<li><strong>Capovolgi</strong> la mano per 5–10 secondi: il gel scorre verso l'apex. Controlla di profilo, poi polimerizza.</li>
<li><strong>Togli la cartina</strong>, eventuale pinching dopo una flash cure, poi limatura: lunghezza, lati, punta, superficie.</li>
<li><strong>Cleaner e top</strong>: sigilla anche il bordo libero; polimerizza e finisci con olio.</li>
</ol>
${F('zone-costruzione.svg', 'Controllo finale del profilo: sottile – spesso – sottile.')}
${B('tip', 'Checklist finale', 'Profilo con apex sopra il punto di stress · curva a C regolare · zona cuticolare pulita · bordo libero sottile e sigillato · nessuna sbavatura sulla pelle.')}
`,
          sources: []
        },
        {
          id: 'tutorial-acrilico', videos: [{"id": "yVuhQ9Nh43M", "title": "Tutorial applicazione acrilico", "channel": "Nail Couture Italia", "lang": "IT"}, {"id": "-xLyP7jYlMA", "title": "Come realizzare un allungamento in acrilico", "channel": "Nailover International", "lang": "IT"}], title: 'Tutorial completo: acrilico su cartina', min: 10,
          html: `
<p>Con l'acrilico il prodotto indurisce all'aria: lavora con ordine e con la perla giusta. Indossa guanti in nitrile e accendi l'aspiratore.</p>
${F('perla-acrilico.svg', 'Prima di iniziare: controlla la consistenza della perla.')}
${F('tut-acrilico.svg', 'Ricostruzione in acrilico su cartina in sei passaggi.')}
<ol class="steps">
<li><strong>Zona 1</strong>: appoggia una perla (bianca per il french o trasparente/rosa) sulla cartina, all'altezza del bordo libero.</li>
<li><strong>Picchietta e modella</strong> con il ventre del pennello per dare forma e lunghezza; per il french disegna la smile line.</li>
<li><strong>Zona 2</strong>: perla al centro, sopra il punto di stress, e fondila verso la zona 1.</li>
<li><strong>Zona 3</strong>: perla piccola e più umida, stesa sottilissima, a circa 1,5 mm dalla pelle.</li>
<li><strong>Pinching</strong> quando il prodotto è ancora leggermente morbido.</li>
<li><strong>Lima e rifinisci</strong>: controlla l'apex di profilo, leviga e sigilla.</li>
</ol>
${B('warn', 'Pulizia del pennello', 'Pulisci il pennello nel monomero e asciugalo su carta tra una perla e l\'altra; non toccare mai il monomero con la pelle.')}
`,
          sources: ['https://open-exam-prep.com/study-guides/oh-nail-technician/artificial-nail-services/sculptured-acrylic-nails']
        }
      ]
    },
    /* ------------------------------------------------------------------ 8 */
    {
      id: 'limatura', summary: ["Squoval: tra le forme più resistenti; mandorla: slancia il dito.", "Lati paralleli al solco, punta dai lati verso il centro.", "Movimento in una sola direzione, niente \"sega\".", "Controlla da 4 punti di vista: alto, profilo, fronte, sotto."], n: 8, level: 'inter', title: 'Limatura e forme',
      desc: 'Le forme dell\'unghia e la tecnica di limatura per un risultato pulito.',
      lessons: [
        {
          id: 'forme', videos: [{"id": "a4NPD2HqrRc", "title": "Limatura: forma quadrata, mandorla e squoval", "channel": "Aerrenails", "lang": "IT"}, {"id": "z3OaoVY-jAM", "title": "Limatura ovale delle unghie", "channel": "Accademia Nails", "lang": "IT"}], title: 'Le forme dell\'unghia', min: 6,
          html: `
${F('forme.svg', 'Le forme principali.')}
<table>
<tr><th>Forma</th><th>Caratteristiche</th><th>Consigliata per</th></tr>
<tr><td>Quadrata</td><td>Lati paralleli, angoli netti. Visivamente accorcia il dito.</td><td>Dita lunghe e sottili</td></tr>
<tr><td>Squoval</td><td>Quadrata con angoli smussati. Tra le più resistenti.</td><td>Quasi tutte; chi usa molto le mani</td></tr>
<tr><td>Tonda</td><td>Segue la curva del polpastrello.</td><td>Unghie corte, uomini, sport</td></tr>
<tr><td>Ovale</td><td>Arrotondata e allungata.</td><td>Effetto elegante, dita corte</td></tr>
<tr><td>Mandorla</td><td>Lati convergenti, punta arrotondata. Slancia molto il dito.</td><td>Dita corte o larghe</td></tr>
<tr><td>Stiletto</td><td>A punta.</td><td>Look deciso; richiede lunghezza e struttura</td></tr>
<tr><td>Ballerina / coffin</td><td>Rastremata con punta piatta.</td><td>Lunghezze medio-lunghe</td></tr>
<tr><td>Lipstick</td><td>Taglio obliquo come un rossetto.</td><td>Look moda</td></tr>
</table>
<h2>Esempio: ottenere una mandorla</h2>
${F('forme-limatura-step.svg', 'Dalla quadrata alla mandorla in quattro passaggi.')}
${B('tip', 'Scegli con la cliente', 'Considera lavoro, abitudini e forma del letto ungueale: una stiletto lunga non è adatta a chi lavora molto con le mani.')}
`,
          sources: ['https://www.my-personaltrainer.it/bellezza/qual-e-la-forma-di-unghie-che-slancia-le-dita-e-resiste-davvero-agli-urti-senza-spezzarsi.html']
        },
        {
          id: 'tecnica', videos: [{"id": "UGpcsTGXAUI", "title": "Sculpting Gel Nails – Advanced Filing", "channel": "Nail Career Education", "lang": "EN"}], title: 'Tecnica di limatura', min: 6,
          html: `
${F('limatura-direzioni.svg', 'Direzioni di limatura.')}
<ol class="steps">
<li><strong>Lunghezza</strong>: accorcia con grana 100/180 tenendo la lima perpendicolare alla punta.</li>
<li><strong>Lati</strong>: lima parallela al solco laterale, senza entrare nel solco.</li>
<li><strong>Punta</strong>: dai lati verso il centro, sempre nella stessa direzione.</li>
<li><strong>Superficie</strong>: movimenti lunghi dalla cuticola verso la punta, seguendo la curva; controlla l'apex di profilo.</li>
<li><strong>Sotto il bordo libero</strong>: pulisci con la lima inclinata.</li>
<li><strong>Rifinitura</strong>: buffer, polvere via, cleaner e top.</li>
</ol>
${B('warn', 'Controlla da 4 punti di vista', 'Dall\'alto (simmetria), di profilo (apex), dal davanti (curva a C) e dal basso (pulizia del bordo).')}
`,
          sources: []
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
    { id: 'es-prep', imgs: ['cuticola.svg'], module: 'preparazione', level: 'base', title: 'Preparazione completa su 10 dita', time: '40 min', img: 'preparazione.svg', caption: 'I sei passaggi della preparazione.',
      goal: 'Eseguire la preparazione in modo ordinato e ripetibile.',
      materials: ['Mano da allenamento o modella', 'Spingicuticole', 'Lima 180/240', 'Pennello per polveri', 'Disidratante e primer'],
      steps: ['Segui i 6 passaggi su ogni dito, nello stesso ordine.', 'Cronometra il tempo totale.', 'Controlla con una luce radente che non resti pellicina sulla lamina.', 'Ripeti cercando di ridurre il tempo senza saltare passaggi.'],
      checks: ['Nessun residuo di pterigio', 'Lamina opaca in modo uniforme ma non assottigliata', 'Primer solo sulla lamina, mai sulla pelle', 'Tempo sotto i 30 minuti'],
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
    { id: 'es-apex', imgs: ['tut-gel-cartina.svg'], module: 'cartina', level: 'inter', title: 'Costruisci l\'apex in gel', time: '60 min', img: 'zone-costruzione.svg', caption: 'Zona 3 sottile, zona 2 struttura, zona 1 sottile.',
      goal: 'Costruire una struttura con apex sopra il punto di stress.',
      materials: ['Tip o cartina su mano da allenamento', 'Gel costruttore', 'Pennello per gel', 'Lampada'],
      steps: ['Stendi una base sottile e polimerizza.', 'Metti una perla di gel in zona 2 e accompagnala verso le zone 1 e 3.', 'Capovolgi la mano qualche secondo per far scendere il gel verso l\'apex, poi polimerizza.', 'Lima e controlla di profilo.'],
      checks: ['Apex sopra il punto di stress', 'Zona cuticolare sottile e a 1,5 mm dalla pelle', 'Punta sottile e uniforme', 'Spessore uguale da lato a lato'],
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
      mistakes: ['Saltare le domande sulla salute', 'Accettare una lunghezza non adatta alle abitudini della cliente'] }
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
      { q: 'Qual è la prima causa di sollevamento?', o: ['La lampada', 'Una preparazione non accurata', 'Il colore', 'La forma'], a: 1, e: 'Pterigio, sebo e umidità sono i nemici dell\'adesione.' },
      { q: 'L\'opacizzazione dell\'unghia naturale serve a…', o: ['Assottigliarla', 'Togliere la lucidità', 'Accorciarla', 'Sbiancarla'], a: 1, e: 'Si toglie solo la lucidità, mai spessore.' },
      { q: 'L\'ordine corretto è…', o: ['Primer → disidratante', 'Disidratante → primer', 'Solo primer', 'Top → primer'], a: 1, e: 'Prima si disidrata, poi si applica il primer.' },
      { q: 'Il primer acido è indicato soprattutto per…', o: ['Semipermanente', 'Acrilico e unghie difficili', 'Top coat', 'Rimozione'], a: 1, e: 'Va usato in quantità minima e solo sulla lamina.' },
      { q: 'Dopo il disidratante…', o: ['Tocco la lamina per controllare', 'Non tocco più la lamina con le dita', 'Lavo le mani della cliente', 'Applico olio'], a: 1, e: 'Il sebo delle dita riduce l\'adesione.' }
    ],
    tip: [
      { q: 'Come scegli la misura del tip?', o: ['Il più piccolo possibile', 'Deve coprire da solco a solco', 'Sempre la misura 5', 'In base al colore'], a: 1, e: 'Se sei tra due misure scegli la più grande e lima i lati.' },
      { q: 'Con quale angolo si appoggia il tip?', o: ['90°', 'Circa 45°, poi si abbassa', '0°, piatto subito', '180°'], a: 1, e: 'Abbassandolo lentamente l\'aria esce e non si formano bolle.' },
      { q: 'Durante il blending del tip…', o: ['Limo anche l\'unghia naturale', 'Fondo solo la linea di contatto del tip', 'Uso la grana 80 sulla lamina', 'Uso acetone'], a: 1, e: 'Non si lima l\'unghia naturale.' },
      { q: 'I tip "a contatto"…', o: ['Hanno un incavo da fondere', 'Non hanno incavo e non vanno fusi', 'Si applicano senza colla', 'Sono solo per i piedi'], a: 1, e: 'Non c\'è zona d\'incavo da fondere.' }
    ],
    cartina: [
      { q: 'Dove va costruito l\'apex?', o: ['Alla cuticola', 'Sopra il punto di stress', 'Sulla punta', 'Ovunque'], a: 1, e: 'In zona 2, sopra il punto di stress.' },
      { q: 'Quanto margine lasci dalla pelle in zona cuticolare?', o: ['Nessuno', 'Circa 1,5 mm', '5 mm', '1 cm'], a: 1, e: 'Circa 1,5 mm evita contatto con la pelle e sollevamenti.' },
      { q: 'Cosa succede se la cartina lascia uno spazio sotto il bordo libero?', o: ['Niente', 'Il prodotto cola sotto e crea sollevamenti', 'L\'unghia è più robusta', 'Si polimerizza prima'], a: 1, e: 'La cartina va a filo del bordo libero.' },
      { q: 'Una ricostruzione piatta, senza apex…', o: ['È più naturale e resistente', 'Si rompe facilmente', 'Non si solleva mai', 'Dura di più'], a: 1, e: 'Senza struttura non regge la lunghezza.' },
      { q: 'Quando si pizzica il gel per la curva a C?', o: ['Prima di stenderlo', 'Dopo una breve polimerizzazione (flash cure)', 'Dopo il top', 'Mai'], a: 1, e: 'Per l\'acrilico invece mentre non è del tutto indurito.' },
      { q: 'La zona 3 deve essere…', o: ['La più spessa', 'Sottilissima', 'Bianca', 'Lucida'], a: 1, e: 'Sottile in zona cuticolare, struttura in zona 2.' }
    ],
    limatura: [
      { q: 'Quale forma è considerata tra le più resistenti?', o: ['Stiletto', 'Squoval', 'Lipstick', 'Ballerina'], a: 1, e: 'Gli angoli smussati riducono il rischio di rotture.' },
      { q: 'Quale forma slancia di più il dito?', o: ['Quadrata', 'Mandorla', 'Tonda', 'Squoval'], a: 1, e: 'I lati convergenti allungano visivamente il dito.' },
      { q: 'Come si limano i lati?', o: ['Con la lima parallela al solco laterale', 'Entrando nel solco', 'Con la grana 80', 'In diagonale'], a: 0, e: 'Senza entrare nel solco.' },
      { q: 'Il movimento corretto della lima è…', o: ['Avanti e indietro veloce', 'In una sola direzione', 'Circolare con forza', 'Casuale'], a: 1, e: 'Il movimento a "sega" scalda e sfibra.' },
      { q: 'Da quanti punti di vista controlli la ricostruzione?', o: ['Solo dall\'alto', 'Alto, profilo, fronte e sotto', 'Solo di profilo', 'Non serve controllare'], a: 1, e: 'Simmetria, apex, curva a C e pulizia del bordo.' }
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
    { t: 'Cuticola', d: 'Pellicina morta che aderisce alla lamina; va rimossa.' },
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
    { t: 'Pterigio', d: 'Pellicina che aderisce alla lamina e va rimossa per evitare sollevamenti.' },
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
    { t: 'Zone 1-2-3', d: 'Bordo libero (1), apex/struttura (2) e zona cuticolare (3) della ricostruzione.' }
  ];

  // esercizi ordinati secondo l'ordine dei moduli
  var order = {};
  modules.forEach(function (m, i) { order[m.id] = i; });
  exercises.sort(function (a, b) { return order[a.module] - order[b.module]; });

  window.NAILX = { modules: modules, exercises: exercises, quiz: quiz, glossary: glossary };
})();
