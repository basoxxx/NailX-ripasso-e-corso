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
      id: 'anatomia', n: 1, level: 'base', title: 'Anatomia e patologie dell\'unghia',
      summary: [
  "La matrice produce la lamina e ne decide spessore e curva: un danno può essere permanente.",
  "Quattro \"sigilli\" proteggono l'unghia: cuticola con piega prossimale, due pieghe laterali, iponichio. Non si tagliano.",
  "Si rimuove solo la cuticola morta; eponichio, iponichio e pterigio vero sono tessuti vivi.",
  "Il punto di stress è dove il bordo libero si stacca dal letto: lì sopra va l'apex.",
  "L'unghia della mano cresce circa 3–3,5 mm al mese (~0,8 mm a settimana): refill ogni 3–4 settimane.",
  "Micosi, paronichia, verruche, unghia verde, banda scura nuova o che si allarga: non lavorare e indirizzare al medico."
],
desc: 'Com\'è fatta l\'unghia, come cresce, come osservarla e quando non si deve lavorare.',
      lessons: [
        {
          id: 'struttura',
          title: 'Struttura dell\'unghia',
          min: 14,
          simple: "L'unghia è una \"piastrella\" di cheratina fatta a strati, prodotta da una radice nascosta (la matrice) e tenuta al riparo da quattro \"guarnizioni\" di pelle. Tu lavori solo sulla superficie: radice e guarnizioni si proteggono sempre.",
          html: `
<p>Conoscere l'anatomia serve a capire <strong>dove</strong> appoggiare il prodotto, <strong>dove</strong> costruire la struttura e quali zone non vanno <strong>mai</strong> toccate. Ogni regola della preparazione nasce da qui.</p>
<p>I dermatologi parlano di <strong>apparato ungueale</strong> (o unità ungueale): non solo la lamina dura che vedi, ma anche la pelle e i tessuti che la producono, la sostengono e la proteggono.</p>
${F('anatomia-alto.svg', 'L\'unghia vista dall\'alto: eponichio, cuticola, lunula, lamina, pieghe laterali, smile line e bordo libero.')}
${F('anatomia-sezione.svg', 'Sezione laterale del dito: matrice, letto ungueale, lamina, iponichio e falange.')}
<h2>Le parti principali</h2>
<table>
<tr><th>Parte</th><th>Cos'è</th><th>Cosa significa per l'onicotecnica</th></tr>
<tr><td><strong>Matrice</strong></td><td>Tessuto vivo nascosto sotto la piega prossimale. Produce di continuo nuove cellule che spingono in avanti la lamina. Poggia quasi sull'osso del dito (falange).</td><td>È la parte più delicata. Pressione, fresa o spingicuticole forzati sulla zona alla base possono lasciare macchie, solchi o deformità, a volte <strong>per sempre</strong>.</td></tr>
<tr><td><strong>Lunula</strong></td><td>La "mezzaluna" chiara alla base: è la parte finale della matrice che si vede attraverso la lamina. Si nota soprattutto sui pollici; su alcune dita non si vede.</td><td>Sotto la lunula la lamina è ancora giovane e morbida: lì si lavora con il massimo della delicatezza.</td></tr>
<tr><td><strong>Lamina ungueale</strong></td><td>Strati di cellule morte piene di cheratina, senza nervi né vasi. È traslucida: il rosa che vedi è il letto sotto. Spessa in media circa 0,4–0,6 mm sulle mani (vedi box).</td><td>Si <em>opacizza</em> soltanto. Se la assottigli si indebolisce, assorbe più sostanze e isola meno dal calore della lampada.</td></tr>
<tr><td><strong>Letto ungueale</strong></td><td>Pelle ricca di vasi sanguigni e terminazioni nervose sotto la lamina. Le dà nutrimento, umidità e oli.</td><td>Mai forzare il distacco della lamina (curva a C troppo stretta, leve in rimozione, limature troppo profonde).</td></tr>
<tr><td><strong>Epitelio del letto</strong></td><td>Sottile strato che "aggancia" la lamina al letto con creste e solchi, come una cerniera lampo, e la lascia scivolare in avanti mentre cresce.</td><td>Se la cerniera si apre in un punto (trauma, leve), si apre facilmente anche oltre: nasce l'onicolisi.</td></tr>
<tr><td><strong>Banda onicodermica</strong></td><td>Sottile linea grigio-rosata dove il letto finisce, sotto il bordo libero. È la "smile line naturale".</td><td>Ti indica dove finisce il letto: è un riferimento per la smile line e per il punto di stress.</td></tr>
<tr><td><strong>Iponichio</strong></td><td>Pelle sotto il bordo libero, all'estremità del dito. Sigilla il letto contro germi e sporco ed è molto sensibile.</td><td>Non va mai spinto, raschiato o "pulito" con strumenti appuntiti. La cartina si appoggia senza premerci contro.</td></tr>
<tr><td><strong>Piega prossimale</strong></td><td>La piega di pelle alla base, che copre e protegge la matrice.</td><td>Non si taglia e non si lima: tagliarla di continuo la fa ispessire e la espone a infezioni.</td></tr>
<tr><td><strong>Eponichio</strong></td><td>Pelle <em>viva</em> sul lato interno della piega prossimale: è lei che produce la cuticola.</td><td>Non si taglia: si arretra con delicatezza, senza spingere sotto la piega.</td></tr>
<tr><td><strong>Cuticola</strong></td><td>Pellicina <em>morta</em>, sottile e appiccicosa, che nasce dall'eponichio e aderisce alla lamina. Chiude lo spazio tra piega e lamina.</td><td>La parte attaccata alla lamina va tolta prima di applicare prodotto: se resta sotto è una delle prime cause di sollevamento.</td></tr>
<tr><td><strong>Pieghe e solchi laterali</strong></td><td>La pelle ai lati della lamina e il "canale" in cui scorre.</td><td>Il prodotto non deve mai toccarle: lascia un margine sottile e pulito.</td></tr>
<tr><td><strong>Bordo libero</strong></td><td>La parte di lamina che sporge oltre il dito.</td><td>Va sempre <em>sigillato</em> (capping) con il prodotto.</td></tr>
<tr><td><strong>Punto di stress</strong></td><td>Zona in cui il bordo libero si stacca dal letto, soprattutto ai lati, lungo la linea della banda onicodermica.</td><td>È lì sopra che va costruito l'<strong>apex</strong>.</td></tr>
</table>
${B('info', 'Quanto è spessa la lamina?', 'Uno studio con ecografia ad alta frequenza su 58 adulti ha misurato in media <strong>0,36–0,45 mm</strong> (dall\'indice al mignolo; un po\' più spessa negli uomini). Altri testi didattici riportano <strong>0,5–0,6 mm</strong>. Ricorda l\'ordine di grandezza: <strong>meno di mezzo millimetro</strong>. Basta poco per assottigliarla troppo.')}
<h2>La lamina è fatta a strati</h2>
${F('anatomia-strati-lamina.svg', 'I tre strati della lamina e da quale parte della matrice nascono.')}
<p>La lamina non è un blocco unico: è come una <strong>pila di fogli</strong> incollati tra loro.</p>
<ul>
<li><strong>Strato superiore</strong>: il più duro e compatto, resiste meglio ad acqua e sostanze chimiche. È quello che opacizzi. Nasce dalla parte più arretrata della matrice.</li>
<li><strong>Strato centrale</strong>: il più spesso (circa due terzi dello spessore o più, secondo le fonti). Dà flessibilità e resistenza. Le sue fibre corrono da lato a lato: per questo l'unghia di solito si rompe di traverso e non per il lungo.</li>
<li><strong>Strato inferiore</strong>: sottile, aderisce al letto. Nasce dalla parte più avanzata della matrice (la lunula).</li>
</ul>
<p><strong>Perché ci interessa:</strong> se con la lima porti via lo strato superiore, sotto trovi strati meno compatti. L'unghia diventa più debole e più "assorbente": entrano più facilmente solventi, monomeri e germi. Per questo si opacizza con grana fine e senza pressione.</p>
${B('tip', 'Sfogliamento', 'Lo sfogliamento a strati del bordo libero (onicoschisi) è proprio la "pila di fogli" che si apre: acqua, detergenti e acetone tolgono gli oli che tengono uniti gli strati. Consiglia olio per cuticole ogni giorno e guanti per i lavori domestici.')}
<div class="box deep"><strong class="t">Approfondimento: perché la lamina è dura ma "beve" acqua</strong> <p>La cheratina della lamina è fatta di fibre proteiche tenute insieme da <strong>ponti disolfuro</strong> (legami tra atomi di zolfo della cistina): sono loro, più dell'acqua e molto più del calcio, a darle durezza. Ma la lamina non è impermeabile: contiene normalmente acqua (una fonte divulgativa indica circa il 18%; i testi didattici danno intervalli diversi, 10–25%) e ne assorbe in fretta.</p> <ul><li>Quando l'unghia sta in acqua si <strong>gonfia</strong>; asciugandosi si ritira. Ogni ciclo stressa i legami tra gli strati: per questo chi ha le mani spesso bagnate ha unghie che si sfogliano.</li> <li>Se applichi il prodotto su una lamina gonfia, quando l'acqua se ne va la lamina "si restringe" sotto un prodotto rigido: è una via diretta al sollevamento.</li></ul> <p>Regola pratica: niente pediluvio o maniluvio prima della ricostruzione; se la cliente arriva con le mani appena lavate a lungo o dalla piscina, lascia asciugare bene la lamina prima del disidratante.</p></div>
<h2>La matrice decide spessore e forma</h2>
${F('matrice-forma.svg', 'Matrice lunga = lamina spessa; matrice corta = lamina sottile; matrice curva = curva a C profonda.')}
<ul>
<li>Una matrice <strong>più lunga</strong> produce più strati: la lamina è <strong>più spessa</strong>. Una matrice corta dà una lamina sottile.</li>
<li>Una matrice <strong>più curva</strong> produce un'unghia con curva a C profonda; una matrice piatta, un'unghia piatta.</li>
<li>Per questo <strong>non puoi cambiare</strong> lo spessore o la forma naturale dell'unghia: puoi solo compensarli con la costruzione.</li>
<li>Un'unghia della mano impiega circa <strong>5 mesi</strong> (4–6 secondo le fonti) per crescere dalla matrice al bordo libero. Un danno alla matrice si vede solo dopo settimane, e ci mette mesi a "uscire".</li>
</ul>
<div class="box deep"><strong class="t">Approfondimento: dove "nasce" il danno</strong> <p>Secondo i testi di dermatologia circa l'<strong>80% della lamina</strong> viene dalla parte prossimale (più arretrata) della matrice, quella nascosta sotto la piega. È anche l'unica zona dell'apparato ungueale con <strong>melanociti</strong>, le cellule del pigmento: per questo le bande scure partono sempre dalla base.</p> <p>Conseguenze pratiche:</p> <ul><li>Uno spingicuticole premuto con forza alla base schiaccia proprio la zona che produce la superficie della lamina: settimane dopo compaiono solchi o ondulazioni <strong>in superficie</strong>.</li> <li>Un'alterazione che "esce" dalla piega non è colpa del servizio di oggi: è nata almeno 1–2 mesi prima. Annotala e fotografala subito, così puoi dimostrarlo.</li></ul></div>
<h2>I quattro sigilli: le guarnizioni dell'unghia</h2>
${F('anatomia-sigilli.svg', 'I quattro sigilli: cuticola con piega prossimale, due pieghe laterali, iponichio.')}
<p>L'unghia è protetta da quattro "guarnizioni" che impediscono a batteri, funghi e sostanze chimiche di entrare sotto la lamina o verso la matrice:</p>
<ol class="steps">
<li><strong>Cuticola + piega prossimale</strong> (alla base).</li>
<li><strong>Piega laterale sinistra</strong>.</li>
<li><strong>Piega laterale destra</strong>.</li>
<li><strong>Iponichio</strong> (sotto il bordo libero).</li>
</ol>
<p>Se rompi un sigillo (tagli troppo, spingi sotto la piega, raschi sotto il bordo libero) apri una porta alle infezioni. È il motivo per cui si toglie solo la cuticola <em>attaccata alla lamina</em> e non la pelle viva.</p>
<div class="box case"><strong class="t">Caso pratico</strong> <p>Una cliente torna dopo cinque settimane: un'unghia ha un sollevamento sulla punta e, sotto, una macchia verde. Che cosa è successo? Il distacco della lamina dal letto (onicolisi) ha <strong>rotto il sigillo dell'iponichio</strong>. Nello spazio entrano acqua e sporco e trova casa il batterio <em>Pseudomonas</em>, che ama l'umidità e produce pigmenti verdi. Di solito è colpita una sola unghia, spesso in chi ha le mani molto in acqua.</p> <p>Cosa fai: non limare dentro la macchia, non ricoprire, consiglia il medico, annota. Cosa impari: i sollevamenti vanno sistemati subito e il refill non va rimandato. Un sollevamento "piccolo" è già un sigillo aperto.</p></div>
<h2>Eponichio, cuticola e pterigio: non confonderli</h2>
<table>
<tr><th></th><th>Eponichio</th><th>Cuticola</th><th>Pterigio (in senso medico)</th></tr>
<tr><td>Vivo o morto?</td><td>Vivo</td><td>Morto</td><td>Vivo (tessuto cicatriziale)</td></tr>
<tr><td>Dove</td><td>Sotto la piega prossimale</td><td>Pellicina trasparente attaccata alla lamina</td><td>La piega cresce "fusa" sopra la lamina e la divide</td></tr>
<tr><td>Cosa fai</td><td>Lo arretri con delicatezza</td><td>La rimuovi dalla lamina</td><td>Non lo tocchi: è un caso per il medico</td></tr>
</table>
${B('warn', 'Attenzione alle parole', 'Nel gergo dei saloni italiani si chiama spesso "pterigio" la cuticola che resta incollata alla lamina. Nei testi professionali e in medicina, invece, il <strong>pterigio</strong> è un\'alterazione di tessuto vivo e cicatriziale che non si spinge e non si taglia. Quando rimuovi la pellicina morta, chiamala <strong>cuticola aderente</strong>.')}
<h2>Applicalo: leggere un dito in 5 passi</h2>
<ol class="steps">
<li><strong>Dall'alto</strong>: individua piega prossimale, lunula (se visibile), pieghe laterali, banda onicodermica e bordo libero.</li>
<li><strong>Di profilo</strong>: guarda dove il bordo libero si stacca dal dito: è il punto di stress.</li>
<li><strong>Dalla punta</strong>: osserva la curva a C naturale (piatta, media, profonda).</li>
<li><strong>Al tatto</strong> (con guanti): senti se la lamina è sottile e flessibile o spessa e rigida.</li>
<li><strong>Annota</strong> tutto sulla scheda cliente: ti servirà per scegliere sistema, cartina e posizione dell'apex.</li>
</ol>
<h2>Errori frequenti</h2>
<ul>
<li>Chiamare "cuticola" l'eponichio e tagliarlo: si ottengono pellicine, ispessimenti e rischio di infezione.</li>
<li>Spingere lo spingicuticole sotto la piega prossimale "per pulire meglio": si preme sulla matrice.</li>
<li>Raschiare sotto il bordo libero: si rompe il sigillo dell'iponichio.</li>
<li>Opacizzare con grana grossa o con la fresa a velocità alta: si porta via lo strato superiore.</li>
</ul>
${B('tip', 'Da ricordare', 'Si rimuove solo ciò che è morto e attaccato alla lamina (cuticola). Tutto ciò che è vivo (eponichio, piega prossimale, pieghe laterali, iponichio) si protegge.')}
        `,
          sources: [
            'https://www.my-personaltrainer.it/fisiologia/unghie.html',
            'https://nailknowledge.org/wp-content/uploads/2026/03/v13-anatomy-and-physiology-the-nail-unit-en.pdf',
            'https://pmc.ncbi.nlm.nih.gov/articles/PMC8236586',
            'https://www.radiopaedia.org/articles/nail-unit-anatomy',
            'https://www.oregon.gov/oha/PH/HLO/Documents/Practice_Clarification_Nail_Pterygium.pdf'
          , 'https://nailknowledge.org/blog/wet-nails', 'https://open-exam-prep.com/study-guides/mn-nail-technician/nail-anatomy-physiology-growth/nail-growth-physiology', 'https://www.statpearls.com/point-of-care/25507', 'https://mdedge.com/content/green-thumbnail', 'https://casereports.bmj.com/content/2009/bcr.07.2009.2074']
        },
        {
          id: 'crescita',
          title: 'Crescita e tempi di ricrescita',
          min: 9,
          simple: "L'unghia della mano cresce di circa 3 mm al mese, cioè quasi 1 mm a settimana. Dopo 3–4 settimane la ricostruzione si è spostata in avanti e va riequilibrata con il refill.",
          html: `
<p>La matrice produce la lamina di continuo, giorno e notte. La lamina scivola in avanti sul letto come un nastro trasportatore. Sapere <strong>quanto</strong> e <strong>come</strong> cresce ti permette di spiegare alla cliente perché serve il refill e di programmare gli appuntamenti.</p>
<h2>Quanto cresce</h2>
<table>
<tr><th></th><th>Mani</th><th>Piedi</th></tr>
<tr><td>Velocità media</td><td>circa <strong>3–3,5 mm al mese</strong> (circa 0,1 mm al giorno; 0,8 mm a settimana)</td><td>circa <strong>1,6 mm al mese</strong> (meno della metà delle mani)</td></tr>
<tr><td>Intervallo normale</td><td>circa 1,8–4,5 mm al mese: varia molto da persona a persona</td><td>più lento e più variabile</td></tr>
<tr><td>In un anno</td><td>circa 3,6–4,2 cm</td><td>circa 2 cm</td></tr>
<tr><td>Ricambio completo</td><td>circa <strong>4–6 mesi</strong></td><td>circa <strong>12–18 mesi</strong> (l'alluce è il più lento)</td></tr>
</table>
${B('info', 'Da dove vengono i numeri', 'Uno studio su giovani adulti sani (Yaemsiri e coll., 2010) ha misurato in media <strong>3,47 mm/mese</strong> per le unghie delle mani e <strong>1,62 mm/mese</strong> per quelle dei piedi. Uno studio su studenti cinesi ha trovato circa 3,1 mm/mese per il pollice. Per questo nel corso usiamo "circa 3 mm al mese": è un valore medio, non una regola fissa.')}
${F('crescita-timeline.svg', 'Una linea segnata alla base si sposta in avanti di circa 0,8 mm a settimana.')}
<h2>Cosa fa variare la velocità</h2>
<ul>
<li><strong>Persona</strong>: a parità di età, ci sono persone "veloci" e persone "lente". Osserva la ricrescita della tua cliente al primo refill e annotala.</li>
<li><strong>Età</strong>: con gli anni la crescita rallenta.</li>
<li><strong>Salute</strong>: febbre alta, malattie, interventi chirurgici, chemioterapia, problemi di circolazione possono rallentarla o fermarla per un periodo. Quando riparte resta un solco trasversale (<em>linee di Beau</em>).</li>
<li><strong>Traumi</strong>: un colpo forte alla base (es. dito nella porta) può interrompere la produzione; a volte la vecchia unghia si stacca e ne cresce una nuova sotto.</li>
<li><strong>Mani e piedi</strong>: le unghie dei piedi crescono molto più lentamente.</li>
</ul>
<div class="box deep"><strong class="t">Approfondimento: non tutte le dita crescono uguali</strong> <ul><li><strong>Mano dominante</strong>: le unghie della mano che usi di più tendono a crescere un po' più in fretta. La differenza è piccola (frazioni di millimetro a settimana) e in alcune persone non c'è.</li> <li><strong>Dito</strong>: medio e pollice spesso crescono più del mignolo, ma le fonti non sono d'accordo su quale sia il più lento.</li> <li><strong>Stagione</strong>: con il caldo le unghie crescono un po' più in fretta (circolazione migliore).</li></ul> <p>Per questo, quando misuri la ricrescita, usa sempre <strong>lo stesso dito della stessa mano</strong> (per esempio il medio della mano dominante) e annota la stagione: confronti dati omogenei e la previsione del refill diventa affidabile.</p></div>
<h2>Perché ci interessa: la ricostruzione "scivola"</h2>
${F('refill.svg', 'La ricrescita sposta in avanti l\'apex: per questo serve il refill.')}
<ul>
<li>Il prodotto è attaccato alla lamina, quindi si sposta in avanti insieme a lei.</li>
<li>Dopo <strong>3–4 settimane</strong> compare alla base una fascia di unghia naturale scoperta (ricrescita) di circa 2,5–3,5 mm.</li>
<li>L'<strong>apex</strong> non è più sopra il punto di stress ma più avanti: la leva sul bordo libero aumenta e con lei il rischio di rotture e sollevamenti.</li>
<li>Il <strong>refill</strong> rimette l'apex al suo posto (modulo 10).</li>
</ul>
<h2>Calcola la ricrescita</h2>
${F('crescita-refill-calcolo.svg', 'Settimane e millimetri di ricrescita: dopo 3–4 settimane si programma il refill.')}
<table>
<tr><th>Settimane dall'applicazione</th><th>Ricrescita media (mani)</th><th>Cosa succede</th></tr>
<tr><td>1</td><td>~0,8 mm</td><td>Quasi invisibile.</td></tr>
<tr><td>2</td><td>~1,6 mm</td><td>Si vede una linea sottile alla base.</td></tr>
<tr><td>3</td><td>~2,4 mm</td><td>Fascia visibile; l'apex comincia a spostarsi. Momento ideale per il refill.</td></tr>
<tr><td>4</td><td>~3,2 mm</td><td>Limite consigliato per il refill.</td></tr>
<tr><td>5–6</td><td>~4–5 mm</td><td>Struttura sbilanciata: più rotture e sollevamenti; spesso conviene rifare.</td></tr>
</table>
<h2>Programma il refill in 4 passi</h2>
<ol class="steps">
<li>Al primo appuntamento fissa il refill a <strong>3 settimane</strong>.</li>
<li>Al refill misura con un righello la fascia di ricrescita sul dito medio.</li>
<li>Dividi i millimetri per le settimane: ottieni la velocità della tua cliente.</li>
<li>Adatta l'intervallo: 3 settimane per chi cresce veloce o ha unghie lunghe, fino a 4 per chi cresce lento e porta unghie corte.</li>
</ol>
<div class="box case"><strong class="t">Caso pratico</strong> <p>Una cliente salta il refill e torna a 6 settimane con due unghie spezzate proprio sopra il punto di stress. Perché proprio lì? Con circa 4–5 mm di ricrescita l'apex si è spostato in avanti: alla base c'è unghia naturale senza rinforzo, mentre il punto più spesso sta "a sbalzo" oltre il letto. La lunghezza fa da leva e il punto debole diventa quello in cui l'unghia si stacca dal letto.</p> <p>Come ragioni: accorcia prima di tutto (meno leva), poi rimetti l'apex al suo posto. Se ci sono sollevamenti estesi conviene rifare. Spiega alla cliente con una foto di profilo prima/dopo: capirà da sola perché il refill a 3–4 settimane non è un capriccio.</p></div>
<h2>Errori frequenti</h2>
<ul>
<li>Allungare l'intervallo a 5–6 settimane "per risparmiare": aumentano rotture, sollevamenti e rischio di infezioni sotto il prodotto.</li>
<li>Promettere che l'unghia "crescerà più veloce" con la ricostruzione: non è vero.</li>
<li>Dimenticare che un danno alla matrice si vede dopo settimane: annota sulla scheda ogni macchia o solco già presente.</li>
</ul>
${B('info', 'Curiosità', 'Alcuni siti italiani riportano "365 mm all\'anno": è un errore. Il valore corretto è circa 36–42 mm all\'anno.')}
        `,
          sources: [
            'https://bionumbers.hms.harvard.edu/bionumber.aspx?id=112380',
            'https://www.clinicalcorrelations.org/2014/11/14/why-do-toenails-grow-more-slowly-than-fingernails/',
            'https://open-exam-prep.com/study-guides/mn-nail-technician/nail-anatomy-physiology-growth/nail-growth-physiology',
            'https://nailknowledge.org/wp-content/uploads/2026/03/v13-anatomy-and-physiology-the-nail-unit-en.pdf',
            'https://qualcherisposta.it/quanto-tempo-per-ricrescita-unghie'
          , 'https://nailknowledge.org/blog/dominant-hand-nail-growth']
        },
        {
          id: 'controindicazioni',
          title: 'Patologie e controindicazioni',
          min: 14,
          simple: "Se l'unghia o la pelle intorno sembrano malate, infiammate, infette o cambiano colore senza un motivo chiaro, non si lavora: si consiglia il medico. Tu osservi e riconosci, non fai diagnosi.",
          html: `
<p>L'onicotecnica <strong>non fa diagnosi</strong> e <strong>non cura</strong>. Deve però riconoscere i segnali che impongono di <strong>non lavorare</strong> e di consigliare il medico (medico di base, dermatologo o podologo). Le linee guida regionali per l'estetica sono chiare: con clienti affetti da patologie o con lesioni sospette ci si astiene dalla prestazione e si consiglia il medico, nel rispetto della privacy. Poi si puliscono e si disinfettano superfici, strumenti e mani.</p>
<h2>Il semaforo</h2>
${F('semaforo-unghie.svg', 'Rosso: non lavorare. Giallo: chiedi, adatta o aspetta il parere del medico. Verde: puoi lavorare.')}
<table>
<tr><th>Colore</th><th>Quando</th><th>Cosa fai</th></tr>
<tr><td><strong>Rosso</strong></td><td>Infezioni (funghi, batteri, virus), infiammazione con dolore o pus, ferite aperte, pelle con eczema in fase attiva, allergia nota agli acrilati, banda scura nuova o che cambia.</td><td>Non lavori sulla zona (spesso su tutta la mano). Spieghi con calma, consigli il medico, disinfetti, annoti.</td></tr>
<tr><td><strong>Giallo</strong></td><td>Onicolisi di causa sconosciuta, psoriasi, ematoma recente, unghia incarnita senza infiammazione, diabete o problemi di circolazione, farmaci che rendono la pelle fragile.</td><td>Chiedi, osserva, adatta il servizio o aspetta il parere del medico. Se hai dubbi, è rosso.</td></tr>
<tr><td><strong>Verde</strong></td><td>Disturbi non contagiosi e non infiammati: linee di Beau, macchioline bianche, striature, unghie fragili o sfogliate.</td><td>Lavori con delicatezza (lezione successiva).</td></tr>
</table>
<h2>Le condizioni da riconoscere</h2>
${F('patologie-tavola.svg', 'Tavola di riconoscimento: onicomicosi, tinea, paronichia, unghia verde, verruche, granuloma, onicolisi, psoriasi e banda scura.')}
<table>
<tr><th>Condizione</th><th>Come si riconosce</th><th>Cosa fare</th></tr>
<tr><td><strong>Onicomicosi</strong> (micosi dell'unghia)</td><td>Unghia ispessita, opaca, gialla, bianca o grigia, friabile; detriti sotto il bordo libero; a volte odore.</td><td>Rosso: è contagiosa. Non limare, non coprire. Disinfetta tutto ciò che hai toccato e consiglia il medico.</td></tr>
<tr><td><strong>Tinea</strong> (micosi della pelle)</td><td>Pelle che si squama, prude, si arrossa (tra le dita, sul palmo, sui piedi).</td><td>Rosso. Al piede è il "piede d'atleta": niente pedicure né pediluvio.</td></tr>
<tr><td><strong>Paronichia</strong></td><td>Infezione della pelle intorno all'unghia: rossore, gonfiore, calore, dolore, a volte pus.</td><td>Rosso. Mai spremere né immergere il dito. Consiglia subito il medico.</td></tr>
<tr><td><strong>Onichia</strong></td><td>Infiammazione profonda della matrice, con pus; la lamina può staccarsi.</td><td>Rosso. Medico.</td></tr>
<tr><td><strong>Granuloma piogenico</strong></td><td>Piccola massa rossa o violacea di "carne" che cresce in fretta e sanguina facilmente.</td><td>Rosso. Non toccarla, non limarla.</td></tr>
<tr><td><strong>Verruche periungueali</strong></td><td>Escrescenze ruvide e dure intorno o sotto l'unghia (virus).</td><td>Rosso: sono contagiose. Non lavorare sulla zona; consiglia il medico.</td></tr>
<tr><td><strong>Unghia verde</strong> (sindrome dell'unghia verde)</td><td>Macchia verde, verde-nera o marrone, spesso sotto un sollevamento della ricostruzione.</td><td>Rosso. È un'infezione batterica (<em>Pseudomonas</em>), non "muffa". Rimuovi il prodotto senza limare dentro la macchia, non riapplicare, consiglia il medico.</td></tr>
<tr><td><strong>Onicolisi</strong></td><td>La lamina si stacca dal letto, di solito dalla punta: zona biancastra o giallastra.</td><td>Giallo/rosso. Se la causa non è nota, niente prodotto: nello spazio si accumulano umidità e germi. Puoi solo accorciare il bordo libero staccato, se è pulito e asciutto.</td></tr>
<tr><td><strong>Banda scura</strong> (melanonichia longitudinale)</td><td>Striscia marrone o nera dalla base alla punta.</td><td>Vedi sotto: in molti casi è innocua, ma alcuni segni vanno visti dal dermatologo con urgenza.</td></tr>
<tr><td><strong>Psoriasi ungueale</strong></td><td>Puntini a "ditale", macchie color salmone ("goccia d'olio"), onicolisi, ispessimento.</td><td>Giallo. Non è contagiosa, ma la lamina è fragile e spesso staccata: serve il parere del dermatologo prima di applicare prodotto.</td></tr>
<tr><td><strong>Altre</strong></td><td>Ferite aperte o tagli, eczema/dermatite in corso, ustioni, unghia incarnita arrossata, allergia nota agli acrilati.</td><td>Non lavorare sulla zona. Con allergia agli acrilati: niente gel, acrilico, polygel, semipermanente.</td></tr>
</table>
<div class="box deep"><strong class="t">Approfondimento: perché una lima può trasmettere la micosi</strong> <p>I funghi delle unghie producono elementi resistenti che restano vivi nella polvere e nei detriti. Una lima in carta o un buffer sono <strong>porosi</strong>: la polvere entra tra i granelli e nessun disinfettante la raggiunge davvero. Per questo le autorità che regolano i saloni chiedono di buttarli dopo ogni cliente.</p> <p>Il disinfettante funziona solo su superfici <strong>lisce, non porose e già pulite</strong>, rispettando il tempo di contatto. È il motivo per cui con una micosi non basta "lavorare solo sulle altre dita": strumenti, piano e poggiamano sono già stati toccati. Elimina tutto il monouso usato e pulisci e disinfetta ciò che è riutilizzabile.</p></div>
<h2>La banda scura: quando preoccuparsi</h2>
${F('melanonichia-segnali.svg', 'Bande scure: quando sono spesso innocue e quando servono controlli urgenti.')}
<p>Una striscia scura lungo l'unghia è frequente, soprattutto nelle pelli scure, e spesso è innocua (traumi, farmaci, un neo della matrice). Alcuni segnali però vanno valutati <strong>subito</strong> dal dermatologo, perché raramente può trattarsi di un melanoma:</p>
<ul>
<li>una sola banda, su un solo dito, in un adulto;</li>
<li>banda <strong>larga</strong> (circa 3 mm o più) o con colore irregolare, dal marrone al nero;</li>
<li>banda <strong>nuova</strong> o che si <strong>allarga</strong> o si scurisce nel tempo;</li>
<li>pigmento che "esce" sulla pelle intorno (piega prossimale o laterale): <strong>segno di Hutchinson</strong>.</li>
</ul>
${B('danger', 'Non coprire mai una banda scura sospetta', 'Il colore o il gel coprono il segnale e ritardano la visita. Fai una foto con il permesso della cliente, annotala sulla scheda e consiglia il dermatologo.')}
<div class="box pro"><strong class="t">Consiglio da professionista</strong> <p>I dermatologi usano un promemoria chiamato <strong>ABCDEF</strong> per le bande scure: <strong>A</strong>ge (adulto), <strong>B</strong>and (banda marrone-nera, larga circa 3 mm o più, bordi sfumati), <strong>C</strong>hange (cambia nel tempo), <strong>D</strong>igit (pollice, alluce e indice sono i più colpiti), <strong>E</strong>xtension (il colore passa sulla pelle), <strong>F</strong>amily (familiari con melanoma). Non serve a fare diagnosi: serve a te per capire quando insistere con gentilezza perché la cliente vada dal dermatologo.</p> <p>Per documentare bene: foto sempre con la stessa luce, dito appoggiato, un righello accanto. A ogni appuntamento rifai la foto: un cambiamento di larghezza si vede solo confrontando immagini fatte nello stesso modo.</p></div>
<h2>Se trovi un problema durante il servizio</h2>
<ol class="steps">
<li><strong>Fermati</strong> in sicurezza: non continuare "solo per finire".</li>
<li><strong>Spiega</strong> con calma e in privato cosa hai visto, senza dare un nome alla malattia ("vedo un'alterazione che è meglio far controllare").</li>
<li><strong>Consiglia</strong> il medico di base, il dermatologo o il podologo.</li>
<li><strong>Elimina</strong> lime e materiali monouso usati su quella cliente.</li>
<li><strong>Pulisci e disinfetta</strong> strumenti, piano di lavoro, lampada; poi sterilizza ciò che va sterilizzato.</li>
<li><strong>Annota</strong> sulla scheda data, cosa hai osservato, servizio rifiutato o interrotto e consiglio dato.</li>
</ol>
<div class="box case"><strong class="t">Caso pratico</strong> <p>"Ho un matrimonio sabato, fallo lo stesso: mi prendo io la responsabilità." Che cosa rispondi? Una firma della cliente non elimina il rischio di contagio per le clienti successive, né il fatto che coprire un'infezione la peggiora (calore e umidità sotto il prodotto). Le linee guida per l'estetica dicono di <strong>astenersi</strong> dalla prestazione.</p> <p>Cosa puoi offrire: una manicure senza prodotto sulle dita sane solo se la condizione non è contagiosa e il medico lo conferma; un appuntamento "di riserva" appena ha il parere medico; consigli su come presentarsi all'evento (unghie corte, curate, olio). Così perdi un servizio oggi ma guadagni una cliente che si fida.</p></div>
<h2>Errori frequenti</h2>
<ul>
<li>"Copro con un gel coprente così non si vede": nascondi il problema e lo peggiori (calore e umidità sotto il prodotto).</li>
<li>Lavorare "solo sulle altre dita" in caso di micosi: il rischio di contagio resta su strumenti e superfici.</li>
<li>Dire alla cliente "è un fungo" o "è niente": non sei tu a fare diagnosi.</li>
<li>Limare via la parte colorata di un'unghia verde: sollevi polvere contaminata.</li>
</ul>
${B('warn', 'Documenta sempre', 'Sulla scheda cliente annota data, cosa hai osservato, il servizio rifiutato e il consiglio di rivolgersi al medico. Per riprendere il servizio, se hai dubbi, chiedi che il medico confermi che la condizione non è contagiosa.')}
        `,
          sources: [
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-skin-science/nail-diseases-contraindications',
            'https://open-exam-prep.com/study-guides/mn-nail-technician/nail-disorders-diseases-assessment/nail-diseases-infections-referrals',
            'https://suap.regione.fvg.it/portale/export/sites/SUAP/allegati/archivio_file/LINEE-GUIDA-ESTETICA.pdf',
            'https://mdedge.com/content/five-rules-evaluating-melanonychia',
            'https://blogs.the-hospitalist.org/content/dark-lines-nails'
          , 'https://www.barbercosmo.ca.gov/forms_pubs/publications/disinfect_nailfiles.pdf']
        },
        {
          id: 'disturbi',
          title: 'Disturbi comuni: quando si può lavorare con attenzione',
          min: 10,
          simple: "Non tutte le unghie \"strane\" sono malate. Solchi, macchioline bianche, striature e sfogliamento di solito non sono contagiosi: si può lavorare, con delicatezza e qualche adattamento.",
          html: `
<p>Nei testi professionali si distingue tra <strong>malattie</strong> (infezioni, spesso contagiose: non si lavora) e <strong>disturbi</strong> (alterazioni non contagiose, spesso dovute a traumi, secchezza o fattori temporanei). Sui disturbi, se la pelle è sana e non c'è dolore, di solito si può lavorare adattando il servizio.</p>
${F('disturbi-tavola.svg', 'I disturbi più comuni (linee di Beau, macchioline, striature, sfogliamento, pellicine, ematoma…) e come adattare il lavoro.')}
<h2>I disturbi più comuni</h2>
<table>
<tr><th>Disturbo</th><th>Come si riconosce</th><th>Perché succede</th><th>Come adatti il lavoro</th></tr>
<tr><td><strong>Linee di Beau</strong></td><td>Solchi trasversali, da un lato all'altro.</td><td>La matrice ha rallentato per un periodo (febbre, malattia, trauma).</td><td>Opacizza con grana fine senza "livellare" il solco; il prodotto riempie il dislivello.</td></tr>
<tr><td><strong>Leuconichia puntata</strong></td><td>Macchioline bianche.</td><td>Piccoli traumi alla matrice. Non è "mancanza di calcio".</td><td>Nessuna limitazione: avanzano con la crescita e spariscono.</td></tr>
<tr><td><strong>Onicoressi</strong></td><td>Striature longitudinali, unghia fragile che si spacca per il lungo.</td><td>Secchezza, detergenti, età.</td><td>Grana 240 o più fine, poca pressione; consiglia olio ogni giorno.</td></tr>
<tr><td><strong>Onicoschisi</strong> (sfogliamento)</td><td>Il bordo libero si apre a strati.</td><td>Acqua e solventi indeboliscono i legami tra gli strati.</td><td>Accorcia fin sotto la zona sfogliata; sigilla bene il bordo libero.</td></tr>
<tr><td><strong>Unghia sottile e morbida</strong></td><td>Lamina flessibile, si piega.</td><td>Matrice corta, costituzione, a volte assottigliamento da limature passate.</td><td>Non opacizzare troppo; strati sottili e flash cure per evitare il calore; base flessibile.</td></tr>
<tr><td><strong>Pellicine</strong> (hangnail)</td><td>Piccoli lembi di pelle secca sui lati.</td><td>Secchezza.</td><td>Taglia solo il lembo secco con tronchesine sterili, senza tirare né tagliare pelle viva.</td></tr>
<tr><td><strong>Ematoma</strong></td><td>Macchia rosso-viola o nera sotto la lamina dopo un colpo.</td><td>Sangue sotto la lamina.</td><td>Recente o dolente: non lavorare. Vecchio, che "cresce" in avanti con l'unghia e non fa male: si può lavorare con delicatezza. Se non ricorda un trauma: medico.</td></tr>
<tr><td><strong>Coilonichia</strong> (a cucchiaio)</td><td>Unghia concava.</td><td>Spesso carenza di ferro o costituzione.</td><td>Struttura adattata (modulo 13); consiglia un controllo dal medico se è nuova.</td></tr>
<tr><td><strong>Unghia a pinza</strong></td><td>Curva molto stretta che "stringe" il letto.</td><td>Costituzione, calzature (piedi).</td><td>Niente pinching; se fa male: podologo o medico.</td></tr>
</table>
${B('tip', 'La regola del dubbio', 'Se il disturbo è <strong>nuovo</strong>, compare su <strong>tutte</strong> le unghie insieme, fa <strong>male</strong> o la pelle intorno è <strong>arrossata</strong>, trattalo come "giallo" e consiglia il medico prima di lavorare.')}
<div class="box deep"><strong class="t">Approfondimento: macchie bianche e "mancanza di calcio"</strong> <p>La durezza della lamina dipende dai <strong>legami tra le fibre di cheratina</strong> (ponti disolfuro) e dal giusto contenuto d'acqua, non dal calcio. Le macchioline bianche nascono quando un piccolo trauma alla matrice disturba la formazione delle cellule: quel punto di lamina riflette la luce in modo diverso.</p> <p>Per l'onicotecnica il dato utile è un altro: se compaiono spesso dopo i servizi, chiediti se stai <strong>premendo troppo alla base</strong> con lo spingicuticole o con la fresa. La macchia comparirà settimane dopo: annota sempre quelle già presenti alla prima visita.</p></div>
<h2>Ematoma vecchio o nuovo?</h2>
${F('ematoma-confronto.svg', 'Ematoma: recente e dolente (non lavorare) o vecchio che si sposta con la crescita (lavora con delicatezza).')}
<ul>
<li>Un ematoma da trauma <strong>si sposta in avanti</strong> con la crescita: in 2–3 settimane la macchia non parte più dalla base.</li>
<li>Una macchia che resta <strong>attaccata alla base</strong> o si allarga non è un ematoma "normale": consiglia il dermatologo.</li>
</ul>
<div class="box pro"><strong class="t">Consiglio da professionista</strong> <p>Usa il calendario della crescita come prova: le unghie delle mani avanzano di circa 0,8 mm a settimana. Al primo appuntamento misura con un righello la distanza tra la piega prossimale e il bordo della macchia e fai una foto. Dopo 2–3 settimane ripeti la misura.</p> <ul><li>Distanza aumentata di circa 1,5–2,5 mm: la macchia si sposta con l'unghia, compatibile con un vecchio ematoma.</li> <li>Distanza uguale, macchia che parte ancora dalla base o si allarga: non è un ematoma "normale". Consiglia il dermatologo senza allarmare.</li></ul> <p>Due misure con righello valgono più di qualsiasi impressione a occhio.</p></div>
<h2>Come lavori su un'unghia con disturbi</h2>
<ol class="steps">
<li>Osserva e annota il disturbo sulla scheda (con foto, se la cliente acconsente).</li>
<li>Chiedi se c'è dolore, da quanto tempo c'è e se è cambiato.</li>
<li>Prepara con grana fine (180–240) e pressione leggera; non cercare di "cancellare" solchi o striature con la lima.</li>
<li>Scegli strati sottili e un prodotto flessibile; usa il flash cure se la lamina è sottile.</li>
<li>Dai i consigli a casa: olio per cuticole ogni giorno, guanti per acqua e detergenti.</li>
</ol>
<div class="box case"><strong class="t">Caso pratico</strong> <p>Una cliente ha su tutte le dita un solco trasversale a metà lamina: due mesi fa ha avuto febbre alta (linee di Beau). Non è una controindicazione se la pelle è sana e non c'è dolore. Ragiona però sul futuro: il solco è un punto più sottile e avanza verso il bordo libero. Quando arriverà al punto di stress, l'unghia tenderà a <strong>spezzarsi lungo il solco</strong>.</p> <p>Scelte sensate: non limare il solco per "pareggiarlo"; riempilo con il prodotto; tieni la lunghezza corta finché il solco non è uscito; avvisa la cliente che un'eventuale rottura in quel punto sarà legata al solco e non al lavoro. Se il solco compare senza una causa nota, consiglia il medico.</p></div>
<h2>Errori frequenti</h2>
<ul>
<li>Limare fino a eliminare le striature: si assottiglia la lamina.</li>
<li>Strappare le pellicine: si apre una porta alle infezioni (paronichia).</li>
<li>Confondere un ematoma vecchio con una banda scura sospetta: guarda se si sposta con la crescita.</li>
</ul>
        `,
          sources: [
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-skin-science/nail-diseases-contraindications',
            'https://nailknowledge.org/wp-content/uploads/2026/03/v13-anatomy-and-physiology-the-nail-unit-en.pdf',
            'https://www.my-personaltrainer.it/fisiologia/unghie.html'
          , 'https://www.statpearls.com/point-of-care/25507', 'https://nailknowledge.org/blog/wet-nails', 'https://blogs.the-hospitalist.org/content/dark-lines-nails', 'https://bionumbers.hms.harvard.edu/bionumber.aspx?id=112380']
        },
        {
          id: 'osservazione',
          title: 'Osservare mani e unghie prima del servizio',
          min: 8,
          simple: "Prima di toccare il prodotto guarda la mano da tre lati, fai qualche domanda e scrivi tutto. In due minuti capisci se puoi lavorare e quale costruzione serve.",
          html: `
<p>Ogni servizio inizia con un <strong>check-up</strong> veloce. Serve a tre cose: escludere controindicazioni, scegliere il sistema giusto, avere un "prima" documentato in caso di problemi.</p>
${F('checkup-6-punti.svg', 'Il check-up in 6 punti: pelle, pieghe, lamina, letto, forma, abitudini.')}
<h2>Il check-up in 6 punti</h2>
<ol class="steps">
<li><strong>Pelle della mano</strong>: tagli, eczema, arrossamenti, verruche, screpolature profonde.</li>
<li><strong>Pieghe e cuticole</strong>: rossore, gonfiore, dolore, pellicine; pieghe ispessite da tagli ripetuti.</li>
<li><strong>Lamina</strong>: colore, spessore, macchie, bande scure, sfogliamento, striature, segni di vecchie limature.</li>
<li><strong>Letto e bordo libero</strong>: lunghezza del letto, onicolisi (zone bianche), detriti sotto il bordo.</li>
<li><strong>Forma</strong>: di profilo e dalla punta (piatta, normale, a pinza, a cucchiaio, ski-jump).</li>
<li><strong>Abitudini e salute</strong>: lavoro (acqua, tastiera, guanti), sport, allergie, farmaci, diabete, servizi precedenti e reazioni.</li>
</ol>
${F('viste-dito.svg', 'Tre viste dello stesso dito: dall\'alto, di profilo, dalla punta.')}
<div class="box pro"><strong class="t">Consiglio da professionista: leggi i segni dei servizi precedenti</strong> <ul><li><strong>Anelli o solchi curvi</strong> sulla lamina ("anelli di fuoco"): fresa usata inclinata o con troppa pressione. La lamina lì è più sottile: niente fresa in quel punto, strati sottili, polimerizzazione prudente.</li> <li><strong>Zone più rosa o trasparenti</strong>: lamina assottigliata. Rischio di bruciore in lampada.</li> <li><strong>Macchie biancastre ruvide</strong> dopo una rimozione: strati superficiali strappati o seccati. Idrata, opacizza appena.</li> <li><strong>Onicolisi su più dita</strong> dopo gel o acrilico: possibile reazione ai prodotti; chiedi di prurito o arrossamenti.</li></ul> <p>Chiedi alla cliente chi ha fatto l'ultimo servizio e come è stato rimosso: ti spiega metà di ciò che vedi.</p></div>
<h2>Domande da fare sempre</h2>
<ul>
<li>"Ha mai avuto prurito, rossore o gonfiore dopo gel, acrilico o semipermanente?" (allergia agli acrilati)</li>
<li>"Ha avuto febbre, malattie o interventi negli ultimi mesi?" (linee di Beau, unghie fragili)</li>
<li>"Questa macchia c'è da molto? È cambiata?"</li>
<li>"Prende farmaci o ha problemi di circolazione o diabete?"</li>
<li>"Che lavoro fa con le mani?" (per scegliere lunghezza e forma)</li>
</ul>
${F('scheda-cliente.svg', 'Esempio di scheda cliente: dati, consensi, allergie, farmaci, stato della lamina, servizio e prodotti usati.')}
<div class="box deep"><strong class="t">Approfondimento: farmaci e luce</strong> <p>Alcuni farmaci rendono la pelle e il letto ungueale più sensibili alla luce. L'esempio più documentato è la <strong>doxiciclina</strong> (un antibiotico): con l'esposizione al sole può causare foto-onicolisi, cioè il distacco della lamina dalla punta, a volte con una macchia a mezzaluna. Gli studi riguardano la luce solare, non le lampade per unghie: non ci sono prove dirette di un rischio con la lampada.</p> <p>Per prudenza, se la cliente sta prendendo antibiotici o farmaci "che fanno male al sole" e nota distacchi o dolore alle unghie, rimanda o adatta il servizio e consiglia di chiedere al medico. Annota il farmaco sulla scheda: ti aiuta a interpretare un'onicolisi improvvisa.</p></div>
<h2>Dall'osservazione alla scelta</h2>
<table>
<tr><th>Cosa vedi</th><th>Cosa scegli</th></tr>
<tr><td>Lamina sottile e flessibile</td><td>Opacizzazione minima, strati sottili, flash cure, lunghezza moderata.</td></tr>
<tr><td>Letto corto, unghie rosicchiate</td><td>Valutazione dedicata (modulo 13), lunghezza corta, eventuale cover.</td></tr>
<tr><td>Curva a C profonda o a pinza</td><td>Niente pinching; cartina adattata.</td></tr>
<tr><td>Mani sempre in acqua</td><td>Preparazione accurata, bordo libero sigillato, unghie corte-medie.</td></tr>
<tr><td>Reazione passata ai prodotti</td><td>Niente acrilati; consiglia il dermatologo (test allergologico).</td></tr>
</table>
<div class="box case"><strong class="t">Caso pratico</strong> <p>Un'infermiera chiede una ricostruzione lunga. Prima di parlare di forme, chiedi del lavoro: le linee guida dell'OMS sull'igiene delle mani indicano che chi ha contatto diretto con i pazienti <strong>non dovrebbe portare unghie artificiali</strong> e dovrebbe tenere le unghie naturali corte, perché sotto e intorno alle unghie lunghe o artificiali restano più germi e i guanti si rompono più facilmente.</p> <p>Come ragioni: spiega la regola senza giudicare, chiedi se la struttura in cui lavora ha un regolamento e proponi alternative per le ferie o per i periodi lontano dal reparto. Annota la scelta sulla scheda.</p></div>
<h2>Errori frequenti</h2>
<ul>
<li>Saltare il check-up perché "è una cliente abituale": le condizioni cambiano.</li>
<li>Non annotare macchie già presenti: se la cliente torna con un problema, non puoi dimostrare che c'era già.</li>
<li>Fotografare senza chiedere il consenso.</li>
</ul>
${B('tip', 'Due minuti ben spesi', 'Un check-up ordinato ti evita la maggior parte delle sorprese: lavora sempre nello stesso ordine, così non dimentichi nulla.')}
        `,
          sources: [
            'https://suap.regione.fvg.it/portale/export/sites/SUAP/allegati/archivio_file/LINEE-GUIDA-ESTETICA.pdf',
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-skin-science/nail-diseases-contraindications',
            'https://www.eczema.org.uk/support/nail-allergy-and-eczema'
          , 'https://nailknowledge.org/blog/how-to-prevent-rings-of-fire-on-the-nail-plate', 'https://community.the-hospitalist.org/content/bilateral-symmetric-onycholysis-distal-fingernails', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3921241', 'https://www.who.int/publications/i/item/9789241597906']
        }
      ]
    },
    /* ------------------------------------------------------------------ 2 */
    {
      id: 'igiene', n: 2, level: 'base', title: 'Igiene, sicurezza e normativa',
      summary: [
  "Detersione → disinfezione → sterilizzazione: ogni strumento al livello giusto. Autoclave classe B (UNI EN 13060) con registro dei cicli.",
  "Lime in carta, buffer, bastoncini d'arancio e bande abrasive sono monouso.",
  "Prima l'aspirazione alla fonte, poi i DPI: nitrile (da cambiare spesso), occhiali, FFP2 in limatura; ventilare.",
  "HEMA e di-HEMA TMHDC solo per uso professionale (Reg. UE 2020/1682); TPO e DMTA vietati dal 1/9/2025 (Reg. UE 2025/877), anche per le scorte.",
  "Il prodotto non polimerizzato non deve mai toccare la pelle: l'allergia agli acrilati è permanente.",
  "In Italia la ricostruzione unghie è in genere ricondotta all'attività di estetista (L. 1/1990: qualifica, responsabile tecnico, SCIA al SUAP); alcuni regolamenti comunali escludono la sola applicazione di unghie artificiali: verifica con Comune e Camera di Commercio."
],
desc: 'Sanificare, disinfettare, sterilizzare; mani, DPI, aria, allergie, regole UE e italiane.',
      lessons: [
        {
          id: 'livelli',
          title: 'Sanificazione, disinfezione, sterilizzazione',
          min: 14,
          simple: "Prima si lava via lo sporco, poi si uccidono i germi con un disinfettante, infine gli strumenti di metallo vanno in autoclave, che elimina tutto, anche le spore. Ciò che non si può pulire bene si usa una volta sola e si butta.",
          html: `
<p>Le mani, la pelle e gli strumenti possono trasmettere <strong>batteri</strong> (es. infezioni della pelle), <strong>funghi</strong> (micosi), <strong>virus</strong> (verruche e, attraverso il sangue, epatite B, epatite C e HIV). Basta un piccolo taglio con uno strumento non sterile. L'igiene non è un dettaglio: è la prima cosa che controllano i NAS e le ASL.</p>
${F('igiene.svg', 'I tre livelli di trattamento igienico: detersione, disinfezione e sterilizzazione.')}
<h2>Le parole giuste</h2>
<table>
<tr><th>Livello</th><th>Cosa fa</th><th>Con cosa</th><th>Su cosa</th></tr>
<tr><td><strong>Detersione / pulizia</strong></td><td>Toglie lo sporco visibile, polvere, residui di prodotto, grasso.</td><td>Acqua, detergente, spazzolino; vasca a ultrasuoni (pulisce ma <em>non</em> disinfetta).</td><td>Tutto, sempre per primo.</td></tr>
<tr><td><strong>Sanificazione</strong></td><td>Pulizia + riduzione dei germi a un livello sicuro.</td><td>Detergenti-disinfettanti.</td><td>Ambienti, arredi, biancheria.</td></tr>
<tr><td><strong>Disinfezione</strong></td><td>Uccide gran parte dei germi, ma non sempre le spore.</td><td>Disinfettanti chimici, rispettando concentrazione e tempo di contatto.</td><td>Superfici, lampada, strumenti che toccano solo pelle integra.</td></tr>
<tr><td><strong>Sterilizzazione</strong></td><td>Elimina ogni forma di vita, spore comprese.</td><td>Autoclave a vapore.</td><td>Strumenti riutilizzabili che possono toccare sangue o pelle lesa (tronchesine, spingicuticole, curette, punte per fresa in metallo).</td></tr>
</table>
<h2>I tre livelli di disinfezione</h2>
${F('livelli-disinfezione.svg', 'Disinfezione bassa, intermedia e alta; in cima la sterilizzazione.')}
<ul>
<li><strong>Bassa</strong>: uccide la maggior parte dei batteri e alcuni virus e funghi (es. sali di ammonio quaternario).</li>
<li><strong>Intermedia</strong>: uccide tutti i batteri e la maggior parte di virus e funghi, non le spore (es. alcol etilico o isopropilico al 70–90%).</li>
<li><strong>Alta</strong>: uccide tutti i microrganismi tranne alcune spore (es. acido peracetico 0,2%, perossido di idrogeno 6%, ipocloriti).</li>
</ul>
<p>Le linee guida regionali chiedono per piani di lavoro e attrezzature un prodotto ad azione <strong>battericida, fungicida e virucida</strong>, usato come indicato in etichetta e nella scheda tecnica.</p>
${B('info', 'Leggi sempre l\'etichetta del disinfettante', 'Controlla: spettro d\'azione (batteri, funghi, virus), diluizione, <strong>tempo di contatto</strong> (quanti minuti la superficie deve restare bagnata), DPI da usare e scheda di sicurezza. Scrivi sul flacone la <strong>data di apertura</strong>: una linea guida regionale indica come validità dopo l\'apertura circa 60 giorni per i disinfettanti a base alcolica e 30 per quelli a base acquosa, salvo diversa indicazione del produttore.')}
<div class="box deep"><strong class="t">Approfondimento: perché l'alcol al 70% funziona meglio di quello puro</strong> <p>L'alcol uccide i germi <strong>denaturando le loro proteine</strong>, cioè facendo perdere loro la forma. Questa reazione è molto più rapida in presenza di acqua: per questo le linee guida indicano come concentrazioni più efficaci quelle tra il 60% e il 90% in acqua, mentre l'alcol assoluto è meno battericida. Sotto il 50% l'efficacia crolla.</p> <p>Due conseguenze pratiche: l'alcol evapora in fretta, quindi su una superficie va steso in quantità sufficiente a restare bagnata per il tempo indicato; e non penetra lo sporco organico (sangue, polvere di limatura), quindi va usato <strong>dopo la pulizia</strong>, mai al posto di essa.</p></div>
<h2>Dove va ogni strumento</h2>
${F('classificazione-strumenti.svg', 'Monouso, disinfettabile o sterilizzabile: ogni oggetto ha la sua strada.')}
<table>
<tr><th>Tipo</th><th>Esempi</th><th>Cosa fai dopo la cliente</th></tr>
<tr><td><strong>Monouso</strong> (porosi, non si possono disinfettare davvero)</td><td>Lime in carta/spugna, buffer, bastoncini d'arancio, bande abrasive per fresa, cotone, salviette, guanti, cartine, tip, carta per il piano.</td><td>Si buttano (o le lime si regalano alla cliente).</td></tr>
<tr><td><strong>Disinfettabili</strong> (non porosi, toccano pelle integra)</td><td>Lima in vetro o metallo, ciotola per manicure, poggiamano lavabile, occhiali, lampada.</td><td>Pulizia + disinfezione.</td></tr>
<tr><td><strong>Da sterilizzare</strong> (metallo, possono toccare sangue)</td><td>Tronchesine, forbicine, spingicuticole, curette, punte per fresa in metallo, pinzette.</td><td>Pulizia → disinfezione → busta → autoclave.</td></tr>
</table>
<h2>Il percorso degli strumenti in 9 passi</h2>
${F('ciclo-sterilizzazione.svg', 'Il ciclo degli strumenti dopo ogni cliente: detersione, disinfezione, risciacquo, busta, autoclave e registro.')}
<ol class="steps">
<li><strong>Con i guanti</strong>, metti subito gli strumenti usati in una vaschetta dedicata (se non puoi lavarli subito, immergili in soluzione disinfettante).</li>
<li><strong>Sciacqua</strong> in acqua corrente tiepida: l'acqua calda "cuoce" i residui di sangue e proteine, quella fredda indurisce i grassi.</li>
<li><strong>Smonta</strong> ciò che si smonta e apri le tronchesine.</li>
<li><strong>Detergi</strong>: spazzolino e detergente sotto il pelo dell'acqua (senza schizzi) o vasca a ultrasuoni con coperchio chiuso. Per le punte da fresa usa lo spazzolino in ottone.</li>
<li><strong>Risciacqua e asciuga</strong> bene con salvietta che non lascia pelucchi.</li>
<li><strong>Controlla</strong> che siano pulite e integre (niente ruggine, lame sbeccate, punte storte).</li>
<li><strong>Imbusta</strong> su un piano diverso da quello di lavaggio: busta con indicatore di processo, data e numero del ciclo scritti sul bordo (non bucare la busta).</li>
<li><strong>Sterilizza</strong> in autoclave con il ciclo indicato dal manuale, senza sovraccaricare la camera.</li>
<li><strong>Registra</strong> il ciclo e conserva le buste in un cassetto chiuso e pulito, fino alla scadenza.</li>
</ol>
${F('autoclave-busta.svg', 'Una busta pronta: indicatore virato, data, numero di ciclo, nessun foro.')}
<h2>L'autoclave: cosa devi sapere</h2>
<ul>
<li>Per strumenti <strong>cavi e porosi</strong> le linee guida chiedono un'autoclave a vapore di <strong>tipo B</strong> (vuoto frazionato), conforme alla norma <strong>UNI EN 13060</strong> per le piccole sterilizzatrici. Le classi N e S sono adatte solo a carichi più semplici.</li>
<li>Prima dei carichi si fanno i <strong>test</strong> previsti dal manuale (tenuta del vuoto, penetrazione del vapore: Bowie-Dick o Helix).</li>
<li>A fine ciclo le buste devono essere <strong>asciutte</strong>: una busta umida significa sterilizzazione non riuscita.</li>
<li>Il <strong>registro di sterilizzazione</strong> (pagine numerate) riporta per ogni ciclo: numero, data, temperatura, pressione e durata, test eseguiti, firma.</li>
<li>Scadenza delle buste: una linea guida regionale indica di norma <strong>non oltre 30 giorni</strong>; altri regolamenti locali arrivano a 60. Segui le regole della tua ASL.</li>
</ul>
${B('warn', 'Sfere di quarzo, UV e calore secco', 'Le sterilizzatrici a sfere di quarzo, i box UV e il calore secco <strong>non</strong> sono considerati adatti: agiscono solo su una parte dello strumento. Un box UV acceso può solo aiutare a conservare strumenti già sterili.')}
<div class="box deep"><strong class="t">Approfondimento: perché vapore e vuoto</strong> <p>Il vapore sterilizza perché, quando tocca lo strumento più freddo, si <strong>condensa</strong> e gli cede moltissimo calore in un attimo. Ma funziona solo dove arriva: una bolla d'aria rimasta dentro una busta o in uno strumento cavo fa da "cuscino" e lì il vapore non entra. Le autoclavi di classe B tolgono l'aria con più cicli di vuoto prima di far entrare il vapore: per questo sono richieste per carichi imbustati e cavi.</p> <p>Come riferimento: le temperature più usate sono circa 121 °C e 132–134 °C; le fonti indicano tempi minimi di mantenimento di pochi minuti a 134 °C e di 15–30 minuti a 121 °C, secondo il tipo di autoclave e di carico. Il ciclo intero dura di più (vuoto, riscaldamento, asciugatura): usa sempre i programmi validati del tuo apparecchio.</p></div>
<h2>Protocollo per ogni cliente</h2>
<ol class="steps">
<li>Piano di lavoro pulito e disinfettato, con carta monouso.</li>
<li>Igiene delle mani tua e della cliente (lezione "Mani, piccoli incidenti e rifiuti").</li>
<li>Strumenti in busta sterile, aperta <strong>davanti alla cliente</strong>; lime e buffer nuovi.</li>
<li>Prodotti prelevati con spatola monouso o dispenser; flaconi chiusi subito dopo l'uso.</li>
<li>Fine servizio: monouso nei rifiuti, strumenti nel percorso di sterilizzazione, piano, lampada, poggiamano e aspiratore puliti e disinfettati.</li>
</ol>
<h2>Errori frequenti</h2>
<ul>
<li>Spruzzare disinfettante su uno strumento sporco: lo sporco protegge i germi.</li>
<li>Asciugare subito la superficie disinfettata: non rispetti il tempo di contatto.</li>
<li>Aprire le buste sterili in anticipo "per fare prima".</li>
<li>Riutilizzare la stessa lima "solo per un'altra cliente".</li>
<li>Non scrivere la data di apertura su disinfettanti e prodotti.</li>
</ul>
${B('danger', 'Controlli reali', 'I NAS controllano i centri: in un caso a Trento un centro è stato sospeso e multato di 3.000 € per mancanza di procedure di sterilizzazione. Tieni sempre a disposizione protocollo scritto, registro di sterilizzazione e schede dei disinfettanti.')}
        
<div class="box pro"><strong class="t">Consiglio da professionista: la busta racconta il ciclo</strong> <ul><li>Indicatore <strong>non virato</strong> o virato a metà: la busta non ha visto le condizioni giuste. Si rifà tutto il percorso.</li> <li>Busta <strong>umida, macchiata o strappata</strong>: non è più sterile. Si riapre, si asciuga lo strumento, si reimbusta e si risterilizza.</li> <li>Strumenti con <strong>ruggine o puntini</strong>: le microcavità trattengono sporco e germi. Si cambia lo strumento, non si "sterilizza di più".</li></ul> <p>Un'abitudine che rassicura le clienti: tieni sul piano una busta chiusa con l'indicatore ben visibile e aprila davanti a loro, mostrando data e numero del ciclo.</p></div>
`,
          sources: [
            'https://suap.regione.fvg.it/portale/export/sites/SUAP/allegati/archivio_file/LINEE-GUIDA-ESTETICA.pdf',
            'https://archiviositi.comune.prato.it/governo2019/moduli/allegato-d-requisiti-igienico-sanitari-attivita-piercing-tatuaggi1f8a.pdf',
            'https://tuttnauer.com/knowledge-center/sterile-processing/autoclave/process-challenge-devices-bowie-dick-helix-tests',
            'https://www.barbercosmo.ca.gov/forms_pubs/publications/disinfect_nailfiles.pdf',
            'https://www.puntosicuro.it/vigilanza-controllo-C-66/vigilanza-nei-centri-estetici-la-sicurezza-dei-clienti-AR-16787/',
            'https://www.ladige.it/territori/trento/controlli-del-nas-a-trento-chiuso-un-centro-estetico-multa-da-3000-euro-wedq1kmt'
          , 'https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/chemical-disinfectants.html', 'https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/steam-sterilization.html']
        },
        {
          id: 'dpi',
          title: 'DPI, polveri e vapori',
          min: 12,
          simple: "La polvere della lima e i vapori dei prodotti vanno catturati vicino alle mani, con un aspiratore, e portati via con aria pulita. Poi ti proteggi con guanti in nitrile, occhiali e mascherina quando limi.",
          html: `
<p>Chi fa unghie respira e tocca ogni giorno piccole quantità di sostanze. Una sola esposizione non fa danni visibili, ma anni di polvere e vapori possono dare <strong>irritazioni</strong>, <strong>asma</strong>, <strong>dermatiti</strong> e <strong>allergie</strong>. La protezione segue un ordine preciso: prima si toglie il rischio alla fonte, poi si usano i DPI.</p>
${F('dpi.svg', 'I DPI da usare a ogni servizio (guanti in nitrile, occhiali, FFP2 in limatura) insieme all\'aspiratore da tavolo.')}
<h2>I rischi in breve</h2>
<table>
<tr><th>Rischio</th><th>Da dove viene</th><th>Effetti possibili</th></tr>
<tr><td><strong>Polveri</strong></td><td>Limatura a mano e con fresa di gel, acrilico, unghia naturale.</td><td>Irritazione di occhi e naso, tosse, respiro sibilante, asma; polvere di prodotto non polimerizzato sulla pelle.</td></tr>
<tr><td><strong>Vapori</strong></td><td>Monomero dell'acrilico, acetone, cleaner, solventi.</td><td>Mal di testa, capogiri, nausea, irritazione.</td></tr>
<tr><td><strong>Contatto con la pelle</strong></td><td>Gel, monomero, primer non polimerizzati; acetone.</td><td>Dermatite irritativa, allergia agli acrilati (permanente).</td></tr>
<tr><td><strong>Occhi</strong></td><td>Schizzi di primer acido, monomero, acetone; frammenti di prodotto.</td><td>Irritazioni, lesioni (il primer acido è corrosivo).</td></tr>
<tr><td><strong>Incendio</strong></td><td>Acetone e monomero sono infiammabili.</td><td>Fiamme vicino a fonti di calore o sigarette.</td></tr>
</table>
<div class="box deep"><strong class="t">Approfondimento: vapori pesanti e punto di infiammabilità</strong> <p>Il <strong>punto di infiammabilità</strong> è la temperatura minima alla quale un liquido libera abbastanza vapore da prendere fuoco con una scintilla. Per l'acetone è sotto zero (circa −18 °C secondo il database NOAA); per l'etil metacrilato (EMA) circa 16–21 °C. Vuol dire che <strong>a temperatura ambiente</strong> entrambi producono vapori infiammabili.</p> <p>I vapori di EMA sono circa quattro volte più pesanti dell'aria: scendono e si accumulano in basso, sul tavolo e vicino al cestino. Per questo l'aspirazione funziona meglio quando la bocchetta è <strong>vicina e in basso</strong>, sotto le mani, e il cestino ha il coperchio. Mai fiamme, candele o stufette elettriche vicino alla postazione.</p></div>
<h2>L'ordine giusto della protezione</h2>
${F('protezione-piramide.svg', 'Prima eliminare e catturare alla fonte, poi ventilare, organizzare il lavoro e infine usare i DPI.')}
<ol class="steps">
<li><strong>Scegli prodotti conformi</strong> (etichetta in italiano, canali ufficiali) e compra solo le quantità necessarie.</li>
<li><strong>Cattura alla fonte</strong>: aspiratore da tavolo o cappa mobile, con le mani della cliente sopra la griglia o il più vicino possibile alla bocchetta.</li>
<li><strong>Ventila</strong> l'ambiente: finestre o ventilazione meccanica che porti aria pulita; l'aria aspirata va scaricata fuori o filtrata.</li>
<li><strong>Lavora pulito</strong>: flaconi chiusi subito, poco monomero nel dappen, cestino con coperchio e sacchetto, piano pulito ogni giorno.</li>
<li><strong>Usa i DPI</strong>: guanti, occhiali, mascherina, camice.</li>
</ol>
${F('aspirazione-tavolo.svg', 'Mani sopra la griglia dell\'aspiratore: la polvere va verso il basso, non verso il tuo viso.')}
<h2>I DPI uno per uno</h2>
<table>
<tr><th>DPI</th><th>Quale</th><th>Perché</th></tr>
<tr><td><strong>Guanti</strong></td><td>Monouso in <strong>nitrile</strong> (norma EN ISO 374 per i prodotti chimici).</td><td>Il lattice resiste meno alle sostanze chimiche e può dare allergia; vinile e polietilene sono poco resistenti. Anche il nitrile protegge per <strong>pochi minuti</strong> dai metacrilati: cambia i guanti appena si sporcano di prodotto e a ogni cliente.</td></tr>
<tr><td><strong>Occhiali</strong></td><td>Occhiali protettivi o visiera (norma EN 166).</td><td>Schizzi di primer, monomero, acetone; frammenti durante il taglio e la limatura.</td></tr>
<tr><td><strong>Mascherina</strong></td><td>Durante la limatura: chirurgica o meglio <strong>FFP2</strong> (EN 149), secondo la valutazione dei rischi.</td><td>Riduce la polvere inalata. <strong>Non</strong> protegge dai vapori: per quelli serve aspirazione, ventilazione o, se necessario, una maschera con filtri a carboni attivi.</td></tr>
<tr><td><strong>Camice</strong></td><td>Chiaro, a maniche lunghe, lavato separatamente.</td><td>Protegge la pelle delle braccia dalla polvere; le macchie si vedono subito.</td></tr>
</table>
${F('mascherine-confronto.svg', 'Mascherina chirurgica, FFP2 e maschera a carboni attivi: cosa fermano.')}
${B('warn', 'Le mascherine non bastano', 'Le linee guida britanniche sui nail bar ricordano che le mascherine "per le goccioline" non proteggono da polveri e odori e non sostituiscono l\'aspirazione. La FFP2 è un aiuto in limatura, non la soluzione principale.')}
<div class="box deep"><strong class="t">Approfondimento: quanto resiste davvero un guanto</strong> <p>Uno studio sui metacrilati usati in odontoiatria (gli stessi "mattoni" di gel e basi) ha misurato quanto tempo impiegano a passare attraverso i guanti:</p> <ul><li>HEMA e TEGDMA concentrati: in media circa <strong>16 minuti</strong> per i guanti in nitrile e circa 5 per il lattice, con grandi differenze tra marche.</li> <li>Con <strong>acetone</strong> nella miscela, il nitrile ha resistito in media meno di <strong>3 minuti</strong>.</li> <li>Altri studi mostrano che il monomero più piccolo (MMA) attraversa tutti i materiali in pochi minuti.</li></ul> <p>In pratica: il guanto ti protegge dagli schizzi, non da un contatto prolungato. Se si sporca di gel o di monomero, toglilo e cambialo subito; non pulire il pennello con cleaner o acetone tenendolo tra le dita guantate.</p></div>
<h2>Togliere i guanti senza sporcarsi</h2>
${F('guanti-togliere.svg', 'Come sfilare i guanti senza toccare l\'esterno con la pelle.')}
<ol class="steps">
<li>Con la mano guantata afferra il primo guanto all'esterno, sul polso.</li>
<li>Sfilalo rovesciandolo e tienilo nel pugno dell'altra mano.</li>
<li>Infila due dita nude <strong>dentro</strong> il secondo guanto, sul polso.</li>
<li>Sfilalo rovesciandolo sopra il primo: ottieni un "sacchetto" chiuso.</li>
<li>Buttalo nel cestino con coperchio e lavati o frizionati le mani.</li>
</ol>
<h2>Il monomero: EMA sì, MMA no</h2>
<ul>
<li>Il monomero standard dell'acrilico per unghie è l'<strong>EMA</strong> (etil metacrilato).</li>
<li>L'<strong>MMA</strong> liquido (metil metacrilato) aderisce in modo troppo rigido, si toglie a fatica (quasi insolubile in acetone), può strappare la lamina e dare forti reazioni. Negli USA la FDA lo ha considerato non adatto e negli anni '70 ha fatto ritirare i prodotti (senza un regolamento di divieto specifico); diversi Stati lo vietano. In Germania il BfR (2011) lo ha giudicato dannoso nei prodotti per modellare le unghie. Si trova ancora in liquidi economici: <strong>evitalo</strong>.</li>
<li>Segnali sospetti di MMA: prezzo molto basso, odore molto forte e "fruttato-acre", prodotto durissimo che non si scioglie in acetone, etichetta senza INCI o non in italiano.</li>
</ul>
<div class="box pro"><strong class="t">Consiglio da professionista: verifica il liquido prima di usarlo</strong> <ul><li>Leggi la <strong>SDS, sezione 3</strong> (composizione): deve comparire Ethyl Methacrylate (CAS 97-63-2). Se trovi Methyl Methacrylate (CAS 80-62-6) come componente principale, non usarlo.</li> <li>Guarda la <strong>sezione 2</strong>: i liquidi per acrilico sono di norma classificati come liquidi facilmente infiammabili (H225) e sensibilizzanti per la pelle (H317). Se l'etichetta non riporta nulla, è un cattivo segnale.</li> <li>Diffida di un liquido senza SDS o con SDS in un'altra lingua: per i controlli devi averla in italiano.</li></ul> <p>Due minuti di lettura prima di aprire un flacone nuovo valgono più di qualsiasi "prova dell'odore".</p></div>
<h2>Cosa dicono gli studi sull'aria dei saloni</h2>
<p>Uno studio su saloni di Boston ha rilevato più CO₂, composti organici volatili e polveri sottili dove entrava meno aria esterna. Le linee guida dell'HSE britannico per i nail bar indicano come misura principale l'<strong>aspirazione localizzata</strong> (tavolo aspirante o cappa mobile), una buona ventilazione generale, flaconi chiusi, rifiuti in cestini con coperchio e manutenzione periodica dell'aspiratore.</p>
${B('tip', 'Manutenzione dell\'aspiratore', 'Pulisci la griglia ogni giorno e cambia i filtri come indica il manuale: un filtro intasato aspira poco. Se possibile, scarica l\'aria all\'esterno.')}
<h2>Errori frequenti</h2>
<ul>
<li>Soffiare via la polvere: la mandi nell'aria (e negli occhi). Usa un pennello pulito sopra l'aspiratore.</li>
<li>Tenere la mascherina sotto il naso o riusarla per giorni.</li>
<li>Lasciare aperti flaconi di monomero e acetone.</li>
<li>Toccare viso, occhi o telefono con i guanti sporchi di prodotto.</li>
<li>Gettare salviette imbevute di monomero o acetone nel cestino aperto.</li>
</ul>
        `,
          sources: [
            'https://www.hse.gov.uk/pubns/guidance/sr13.pdf',
            'https://certifico.com/component/attachments/download/26525',
            'https://cdc.gov/niosh/docs/99-112',
            'https://pmc.ncbi.nlm.nih.gov/articles/PMC6325001',
            'https://dudley.gov.uk/business/environmental-health/health-and-safety/nail-bar-safety',
            'https://www.dguv.de/ifa/forschung/projektverzeichnis/ifa3159-2.jsp',
            'https://mgaleg.maryland.gov/2000rs/fnotes/bil_0005/hb0135.PDF'
          , 'https://cameochemicals.noaa.gov/chemical/8', 'https://cameochemicals.noaa.gov/chemical/3434', 'https://medicaljournalssweden.se/actaodontologica/article/view/39113', 'https://www.niom.no/permeability-of-medical-gloves-to-mono-and-dimethacrylate-monomers-in-dental-restorative-materials.6641978-606139.html', 'https://www.parchem.com/siteimages/Attachment/GHS%20Ethyl%20Methacrylate%20MSDS.pdf']
        },
        {
          id: 'allergie-ue',
          title: 'Allergie agli acrilati e regole UE (HEMA, TPO, DMTA)',
          min: 13,
          simple: "Gel, acrilico, polygel e semipermanente contengono sostanze che possono dare allergia se toccano la pelle quando sono ancora liquide. L'allergia, una volta presa, resta per sempre. Le regole UE limitano o vietano alcune di queste sostanze.",
          html: `
<p>I (met)acrilati sono i "mattoni" di gel, acrilici, polygel, semipermanenti, colle e resine. Sono tra le cause più comuni di <strong>dermatite allergica da contatto</strong> legata alle unghie. Il rischio è basso finché il prodotto sta sulla lamina ed è ben polimerizzato; diventa concreto quando il prodotto <strong>non polimerizzato</strong> (liquido, appiccicoso, in polvere fresca di limatura) <strong>tocca la pelle</strong>.</p>
${B('danger', 'Due regole d\'oro', '1) Il prodotto non deve mai toccare la pelle della cliente. 2) Non toccare mai gel, monomero o primer non polimerizzati a mani nude.')}
<h2>Come nasce un'allergia</h2>
<ol class="steps">
<li><strong>Sensibilizzazione</strong>: le molecole piccole passano nella pelle. All'inizio non succede nulla di visibile.</li>
<li><strong>Esposizioni ripetute</strong>: il sistema immunitario "impara" a riconoscerle.</li>
<li><strong>Reazione</strong>: a un contatto successivo compaiono prurito, rossore, vescicole. Da quel momento l'allergia è <strong>permanente</strong>.</li>
</ol>
${F('allergia-zone.svg', 'Dove compare l\'allergia: intorno alle unghie, polpastrelli, palpebre, viso e collo.')}
<div class="box deep"><strong class="t">Approfondimento: che cosa dicono i dati europei</strong> <p>Uno studio del gruppo europeo di ricerca sulla dermatite da contatto (11 centri, 2013–2015) ha trovato 136 casi di allergia ai (met)acrilati delle unghie: erano i due terzi di tutte le allergie agli acrilati viste. Circa il <strong>57% erano professioniste</strong> delle unghie, il resto clienti. L'<strong>HEMA</strong> era positivo nel 92,5% dei casi; il cianoacrilato della colla solo in circa il 10%.</p> <p>Perché l'HEMA? È una molecola piccola: passa attraverso pelle e guanti più facilmente delle molecole grandi. Un dettaglio utile da riferire al dermatologo: alcune reazioni al patch test compaiono tardi, e i dermatologi consigliano una lettura anche al 7° giorno.</p></div>
<h2>Come si riconosce</h2>
<ul>
<li>Prurito, rossore, gonfiore o vescicole intorno all'unghia; bruciore sotto la lamina.</li>
<li>Pelle dei polpastrelli secca, spaccata, ispessita.</li>
<li>Onicolisi (l'unghia si stacca), lamina deformata.</li>
<li>Eczema anche lontano: <strong>palpebre</strong>, viso, collo, dove le dita toccano.</li>
</ul>
<p><strong>Cosa fai</strong>: interrompi l'uso di acrilati su quella cliente, rimuovi il prodotto senza aggredire la pelle e consiglia il dermatologo per il <strong>patch test</strong>. Annota tutto sulla scheda. Lo stesso vale per te: se compaiono sintomi sulle tue mani, vai dal medico.</p>
${B('info', 'Perché è importante', 'Chi è allergico agli acrilati può avere problemi in futuro con alcune cure dentali, interventi o dispositivi medici che li contengono. Proteggere la pelle non è solo estetica.')}
<h2>Le cause più comuni (e come evitarle)</h2>
${F('contatto-pelle.svg', 'Prodotto che tocca cuticola e pieghe (✗) e margine pulito di circa 1 mm (✓).')}
<table>
<tr><th>Causa</th><th>Come evitarla</th></tr>
<tr><td>Prodotto sulle pieghe o sulla cuticola</td><td>Lascia un margine sottile e pulito; togli le sbavature <strong>prima</strong> di polimerizzare.</td></tr>
<tr><td>Polimerizzazione incompleta</td><td>Strati sottili, tempi della scheda tecnica, lampada consigliata dal produttore, pollice a parte.</td></tr>
<tr><td>Perla di acrilico troppo bagnata</td><td>Rapporto liquido/polvere corretto (perla media).</td></tr>
<tr><td>Strato di dispersione o polvere fresca sulla pelle</td><td>Cleaner con salvietta pulita per ogni dito; aspirazione durante la limatura; lavare le mani della cliente a fine servizio.</td></tr>
<tr><td>Kit "fai da te" usati senza formazione</td><td>Spiega alla cliente i rischi; i prodotti con HEMA sono per uso professionale.</td></tr>
</table>
<div class="box case"><strong class="t">Caso pratico</strong> <p>Una cliente con le unghie in gel da un anno racconta che le si arrossano e prudono le <strong>palpebre</strong>, ma le dita sono a posto. Può c'entrare il gel? Sì: le dita toccano spesso gli occhi e la pelle delle palpebre è sottilissima, quindi reagisce prima di quella delle mani. Pellicine di prodotto, polvere fresca di limatura o un top poco polimerizzato bastano.</p> <p>Come ragioni: non dire "è il gel", ma non escluderlo. Consiglia il dermatologo per il patch test, annota prodotti e lotti usati, controlla la tua tecnica (margine dalla pelle, salvietta pulita per ogni dito, lampada giusta, tempi pieni). Finché non c'è risposta, niente acrilati.</p></div>
<h2>Le regole UE in vigore</h2>
<p>I cosmetici nell'UE seguono il <strong>Regolamento (CE) 1223/2009</strong>. L'<strong>Allegato II</strong> elenca le sostanze <strong>vietate</strong>; l'<strong>Allegato III</strong> quelle ammesse solo con limiti e avvertenze.</p>
<h3>HEMA e di-HEMA TMHDC – Reg. (UE) 2020/1682</h3>
<ul>
<li>Inseriti nell'Allegato III (voci 313 e 314): ammessi solo nei <strong>prodotti per unghie</strong> e solo per <strong>uso professionale</strong>.</li>
<li>In etichetta: «Solo per uso professionale» e «Può provocare una reazione allergica».</li>
<li>Dal <strong>3 giugno 2021</strong> i prodotti non conformi non possono essere immessi sul mercato; dal <strong>3 settembre 2021</strong> non possono più essere messi a disposizione (venduti).</li>
<li>Il comitato scientifico UE (SCCS) li considera sensibilizzanti da deboli a moderati, sicuri solo se usati sulla lamina <strong>senza contatto con la pelle</strong>.</li>
</ul>
<h3>Divieto di TPO e DMTA – Reg. (UE) 2025/877 ("Omnibus VII")</h3>
<ul>
<li>Pubblicato il 13 maggio 2025, si applica dal <strong>1° settembre 2025</strong>. Aggiunge all'Allegato II sostanze classificate CMR (cancerogene, mutagene o tossiche per la riproduzione).</li>
<li><strong>TPO</strong> (difenil(2,4,6-trimetilbenzoil)fosfina ossido, CAS 75980-60-8): fotoiniziatore di gel e semipermanenti, classificato tossico per la riproduzione (cat. 1B). È stato tolto dall'Allegato III e messo tra i vietati.</li>
<li><strong>DMTA</strong> (N,N-dimetil-p-toluidina, CAS 99-97-8, detta anche DMPT): <strong>accelerante</strong> usato nei liquidi per acrilico e negli attivatori dei sistemi "dip". Il divieto riguarda quindi anche alcuni monomeri liquidi e attivatori, non solo i gel.</li>
<li>Nessun periodo di smaltimento: dal 1° settembre 2025 i prodotti con TPO o DMTA non si vendono e non si usano, <strong>anche in salone e anche se già acquistati o aperti</strong>. Secondo la stampa, una circolare del Ministero della Salute (agosto 2025) ha indicato il ritiro da parte dei fornitori e lo smaltimento tramite canali autorizzati.</li>
<li>Esistono fotoiniziatori alternativi (per esempio TPO-L, cioè etil fenil(2,4,6-trimetilbenzoil)fosfinato, o BAPO): sono sostanze diverse, ma <strong>controlla sempre l'INCI</strong> e chiedi conferma scritta al fornitore.</li>
</ul>
${F('etichetta-inci.svg', 'Cosa cercare in etichetta: avvertenze HEMA, assenza di TPO e DMTA, lotto e PAO.')}
<div class="box deep"><strong class="t">Approfondimento: perché togliere il TPO cambia la polimerizzazione</strong> <p>Il TPO era così diffuso perché assorbe bene la luce fino a circa 400–410 nm, proprio dove emettono le lampade LED. I fotoiniziatori sostitutivi hanno "finestre" di assorbimento diverse: per esempio il TPO-L ha il massimo intorno ai 370 nm e assorbe meno verso i 405 nm.</p> <p>Cosa significa per te: un gel riformulato <strong>senza TPO</strong> può richiedere una lampada diversa o tempi più lunghi. Quando cambi prodotto:</p> <ul><li>leggi i nuovi tempi e la lampada indicati nella scheda tecnica;</li> <li>fai una prova su tip: dopo il cleaner la superficie non deve restare appiccicosa, e lo strato non deve graffiarsi con l'unghia;</li> <li>se la cliente sente più calore o il top resta molle, ricontrolla l'abbinamento con la lampada.</li></ul></div>
<h2>Inventario in 5 passi</h2>
<ol class="steps">
<li>Raccogli tutti i prodotti: gel, semipermanenti, top, base, liquidi per acrilico, attivatori, colle.</li>
<li>Leggi l'INCI di ognuno: cerca "Trimethylbenzoyl Diphenylphosphine Oxide" (TPO) e "Dimethyltolylamine" / "N,N-dimethyl-p-toluidine" (DMTA).</li>
<li>Separa i prodotti non conformi con il cartello "NON UTILIZZABILI" e contatta il fornitore per ritiro o smaltimento.</li>
<li>Verifica che i prodotti con HEMA riportino le avvertenze obbligatorie in italiano.</li>
<li>Archivia schede tecniche e schede di sicurezza (SDS) dei prodotti in uso.</li>
</ol>
<h2>Errori frequenti</h2>
<ul>
<li>"Questo gel è ipoallergenico, quindi posso lavorare più largo": nessun gel è privo di rischio se tocca la pelle.</li>
<li>Usare una lampada "universale" non indicata dal produttore del gel: il gel può restare sottopolimerizzato.</li>
<li>Pensare che il divieto TPO riguardi solo il semipermanente: controlla anche top, base, builder e liquidi per acrilico (DMTA).</li>
<li>Vendere alla cliente kit con HEMA per uso domestico.</li>
</ul>
        `,
          sources: [
            'https://www.legislation.gov.uk/eur/2020/1682/data.xht',
            'https://eur-lex.europa.eu/eli/reg/2020/1682/oj/eng',
            'https://coslaw.eu/omnibus-act-vii-new-substances-officially-banned-in-the-eu-from-september-2025/',
            'https://news.ceway.eu/omnibus-act-vii-eu-bans-new-cmr-substances-in-cosmetics-what-you-must-know-about-regulation-eu-2025-877/',
            'https://certifico.com/chemicals/legislazione-chemicals/312-legislazione-cosmetici/23967-regolamento-ue-2025-877',
            'https://www.money.it/divieto-tpo-e-dmta-negli-smalti-le-regole-per-professionisti-e-centri-estetici',
            'https://www.lapresse.it/economia/2025/08/31/smalto-da-domani-stop-a-quelli-con-tpo-le-aziende-il-mercato-ha-gestito-la-transizione/',
            'https://www.eczema.org.uk/support/nail-allergy-and-eczema',
            'https://pubmed.ncbi.nlm.nih.gov/38093676/'
          , 'https://doi.org/10.1111/cod.12942', 'https://community.the-hospitalist.org/content/bilateral-symmetric-onycholysis-distal-fingernails', 'https://americas.sartomer.arkema.com/en/product-finders/product/f/sartomer_Lambson/p/speedcure-tpo-l', 'https://radtech.org/proceedings/2012/papers/end-user-presentations/LED/DSM_Rundlett_LED.pdf', 'https://eur-lex.europa.eu/eli/reg/2025/877/oj']
        },
        {
          id: 'normativa-italia',
          title: 'Chi può lavorare in Italia',
          min: 10,
          simple: "In Italia chi fa unghie a pagamento lavora, di regola, come estetista: serve la qualifica, un responsabile tecnico qualificato e una SCIA al Comune. Un attestato di un corso privato da solo non basta per aprire un'attività.",
          html: `
<p>In Italia la ricostruzione unghie rientra di norma nell'attività di <strong>estetista</strong>, regolata dalla <strong>Legge 4 gennaio 1990 n. 1</strong> e dalle leggi e regolamenti di Regioni e Comuni. Le schede delle Camere di Commercio elencano l'<strong>onicotecnica</strong> tra le attività di estetica. L'onicotecnico non ha (ancora) una figura professionale nazionale autonoma.</p>
${B('info', 'Un tema ancora aperto', 'Ci sono state interpretazioni diverse: per esempio, una sentenza del TAR Veneto del 2001 la considerava attività artigianale. Alcune Regioni hanno creato registri o percorsi formativi (le Marche hanno un registro regionale degli onicotecnici, a iscrizione facoltativa). In Emilia-Romagna una proposta di legge sull\'onicotecnico è stata pubblicata a novembre 2025 per la consultazione. In Parlamento sono stati presentati più disegni di legge. Finché non cambiano le regole, la strada sicura è la qualifica di estetista: <strong>chiedi sempre al SUAP del tuo Comune</strong>.')}
<h2>Come si ottiene la qualifica di estetista</h2>
${F('percorsi-estetista.svg', 'I percorsi principali per diventare estetista abilitata.')}
<p>I dettagli (ore, enti, esami) li decide ogni Regione. A titolo di esempio, in Emilia-Romagna i percorsi sono:</p>
<table>
<tr><th>Percorso</th><th>Come funziona</th></tr>
<tr><td><strong>1. Corso di qualifica</strong></td><td>Corso biennale di almeno 1.800 ore (circa 900 l'anno) → attestato di qualifica (per lavorare come dipendente o socia) → corso di specializzazione di 600 ore <em>oppure</em> un anno di lavoro → esame → abilitazione.</td></tr>
<tr><td><strong>2. Apprendistato</strong></td><td>Apprendistato (durata del contratto collettivo) + almeno un anno di lavoro qualificato → corso teorico di 300 ore → esame.</td></tr>
<tr><td><strong>3. Esperienza</strong></td><td>Tre anni di lavoro qualificato → corso teorico di 300 ore → esame.</td></tr>
</table>
${B('warn', 'Attenzione agli attestati', 'Un corso privato o un "attestato di onicotecnica" da solo <strong>non abilita</strong> ad aprire un\'attività in proprio. È utile per imparare la tecnica, ma la qualifica la rilascia un percorso riconosciuto dalla Regione.')}
<h2>Aprire l'attività</h2>
${F('apertura-attivita.svg', 'SCIA al SUAP, responsabile tecnico, ComUnica: i passaggi per aprire.')}
<ol class="steps">
<li><strong>Verifica i requisiti</strong> del locale con il regolamento comunale e l'ASL (igiene, servizi, impianti).</li>
<li><strong>Presenta la SCIA</strong> (Segnalazione Certificata di Inizio Attività) al <strong>SUAP</strong> del Comune: dichiari i requisiti professionali e quelli dei locali.</li>
<li><strong>Indica il responsabile tecnico</strong>: una persona qualificata (titolare, socia, familiare o dipendente) presente durante l'attività, per ogni sede.</li>
<li><strong>Iscrivi l'impresa</strong> al Registro delle Imprese (ed eventualmente all'Albo artigiani) con la <strong>ComUnica</strong>, che informa anche Agenzia delle Entrate, INPS e INAIL.</li>
<li><strong>Prepara i documenti</strong> da mostrare ai controlli: protocollo igienico scritto, registro di sterilizzazione, schede tecniche e di sicurezza dei prodotti, schede clienti.</li>
</ol>
<div class="box pro"><strong class="t">Consiglio da professionista: le domande da portare al SUAP</strong> <ul><li>Nel mio Comune la ricostruzione unghie rientra nell'attività di estetista? Serve un responsabile tecnico qualificato per ogni sede?</li> <li>Quali requisiti minimi chiede il regolamento comunale per il locale (superficie, lavabo, servizio igienico, aerazione)?</li> <li>Posso lavorare in affitto di cabina? Che documenti servono?</li> <li>L'ASL chiede un protocollo di sterilizzazione scritto o un modello particolare di registro?</li></ul> <p>Fatti dare le risposte per iscritto o annota nome, data e riferimento normativo. Le regole cambiano da Regione a Regione e da Comune a Comune: una risposta scritta è la tua tutela più semplice.</p></div>
<h2>Dove si può lavorare</h2>
<ul>
<li>In un <strong>locale</strong> adatto, conforme ai regolamenti edilizi e igienico-sanitari.</li>
<li>A <strong>domicilio dell'esercente</strong> solo se i locali sono separati dall'abitazione, destinati solo all'attività e con servizio igienico per i clienti (così prevede l'esempio emiliano: verifica le regole della tua Regione).</li>
<li>Presso la sede scelta dal cliente o in strutture convenzionate, dove la Regione lo prevede.</li>
<li>Non in forma <strong>ambulante</strong> o di posteggio (es. bancarelle).</li>
<li>Con l'<strong>affitto di cabina</strong> presso un altro centro, se si hanno i titoli abilitanti.</li>
</ul>
<h2>Altre regole che ti riguardano</h2>
<ul>
<li><strong>Sicurezza sul lavoro</strong> (D.Lgs. 81/2008): l'obbligo di usare DPI adeguati vale anche per artigiani e lavoratori autonomi.</li>
<li><strong>Apparecchi elettromeccanici per uso estetico</strong>: devono essere conformi al Decreto 15 ottobre 2015 n. 206; chiedi al fornitore la dichiarazione di conformità e conserva il manuale in italiano.</li>
<li><strong>Cosmetici</strong>: solo da canali ufficiali, con etichetta in italiano (Reg. CE 1223/2009).</li>
<li><strong>Privacy</strong>: la scheda cliente con dati di salute va trattata secondo il GDPR (consenso, conservazione sicura).</li>
</ul>
<div class="box deep"><strong class="t">Approfondimento: sicurezza sul lavoro se hai dipendenti</strong> <p>Il D.Lgs. 81/2008 chiede a chi lavora da solo, in sostanza, di usare attrezzature e DPI conformi. Quando assumi qualcuno, diventi <strong>datore di lavoro</strong> e gli obblighi crescono: valutazione dei rischi scritta (DVR, che per un salone di unghie deve considerare almeno sostanze chimiche, polveri, postura e rischio biologico), formazione dei lavoratori, fornitura dei DPI, nomina delle figure previste.</p> <p>Le schede di sicurezza (SDS) dei prodotti sono la base della valutazione del rischio chimico: tienile aggiornate. Per i dettagli rivolgiti a un consulente per la sicurezza o alla tua associazione di categoria: questa è un'indicazione generale, non una consulenza.</p></div>
<h2>Errori frequenti</h2>
<ul>
<li>Lavorare in casa "in nero" con un attestato privato: rischi sanzioni e, in caso di danni alla cliente, non sei coperta.</li>
<li>Pensare che la partita IVA basti: senza qualifica e SCIA l'attività non è regolare.</li>
<li>Copiare le regole di un'altra Regione: ore, percorsi e requisiti dei locali cambiano.</li>
</ul>
        `,
          sources: [
            'https://www.mo.camcom.it/promozione/sportello-genesi/schede-informative/estetista-scheda-informativa',
            'https://www.regione.veneto.it/web/attivita-produttive/professione-estetista',
            'https://documenti.camera.it/leg18/dossier/pdf/AP0107.pdf',
            'https://www.consiglio.marche.it/banche_dati_e_documentazione/atti_di_indirizzo_e_controllo/mozioni/pdf/moz479_10.pdf',
            'https://bur.regione.emilia-romagna.it/area-bollettini/supplemento-speciale-n-27-del-25-11.2025/@@download/pdf_firmato',
            'https://suap.regione.fvg.it/portale/export/sites/SUAP/allegati/archivio_file/LINEE-GUIDA-ESTETICA.pdf'
          , 'https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2008-04-09;81', 'https://certifico.com/component/attachments/download/26525']
        },
        {
          id: 'mani-incidenti',
          title: 'Mani, piccoli incidenti e rifiuti',
          min: 9,
          simple: "Mani pulite prima e dopo ogni cliente, unghie corte e niente anelli. Se c'è un taglio: guanti, garza, pressione, disinfezione e strumenti sporchi da parte. I rifiuti taglienti vanno nel contenitore rigido.",
          html: `
<p>Le mani dell'operatrice sono lo strumento che tocca tutto. Lavarle bene, gestire con calma un piccolo sanguinamento e smaltire correttamente i rifiuti sono competenze di base, richieste dalle linee guida regionali per l'estetica.</p>
<h2>Igiene delle mani</h2>
${F('lavaggio-mani.svg', 'Frizione alcolica (20–30 secondi) e lavaggio con acqua e sapone (40–60 secondi): tutti i punti da coprire.')}
<ul>
<li><strong>Quando</strong>: prima e dopo ogni cliente, prima di mettere e dopo aver tolto i guanti, dopo aver toccato rifiuti o strumenti sporchi, dopo la toilette.</li>
<li><strong>Come</strong>: frizione con gel alcolico per <strong>20–30 secondi</strong> se le mani non sono visibilmente sporche; lavaggio con acqua e sapone per <strong>40–60 secondi</strong> se sono sporche. Insisti su pollici, punte delle dita e spazi tra le dita.</li>
<li><strong>Le tue unghie</strong>: corte, pulite, preferibilmente senza smalto durante il lavoro; niente anelli, bracciali e orologio.</li>
<li><strong>Le mani della cliente</strong>: falle lavare o igienizzare all'inizio.</li>
<li>Copri eventuali tagli o abrasioni sulle tue mani con un cerotto impermeabile e i guanti.</li>
</ul>
${B('tip', 'Proteggi la tua pelle', 'Lavaggi frequenti seccano la pelle e la rendono più permeabile ai prodotti. Usa una crema idratante a fine giornata: la pelle sana è la tua prima barriera contro le allergie.')}
<div class="box deep"><strong class="t">Approfondimento: perché il gel non basta sulle mani sporche</strong> <p>L'OMS indica la frizione alcolica come metodo preferito solo quando le mani <strong>non sono visibilmente sporche</strong>. L'alcol uccide i germi ma non attraversa lo sporco organico: polvere di limatura, residui di prodotto o sangue fanno da scudo. Acqua e sapone, invece, staccano e portano via lo sporco grazie allo sfregamento e al risciacquo.</p> <p>Nel lavoro sulle unghie questo è frequente: dopo la limatura le mani sono coperte di polvere fine. In quel momento lava, non frizionare. Ricorda anche che un gel alcolico funziona solo se le mani restano bagnate per tutto il tempo indicato: se si asciugano in 5 secondi, ne hai messo troppo poco.</p></div>
<h2>Piccolo taglio durante il servizio</h2>
${F('incidente-taglio.svg', 'Cosa fare se una cliente sanguina: pressione con garza sterile, disinfezione, strumenti da parte.')}
<ol class="steps">
<li>Mantieni la calma e assicurati di indossare i guanti.</li>
<li>Premi sulla ferita con una <strong>garza sterile</strong> finché il sanguinamento si ferma. Se non si ferma, continua a premere e cerca assistenza medica.</li>
<li>Disinfetta con un disinfettante per cute lesa e copri con un cerotto.</li>
<li>Metti da parte lo strumento usato: va pulito, disinfettato e sterilizzato prima di riusarlo. Le lime che hanno toccato sangue si buttano.</li>
<li>Pulisci le superfici sporche di sangue con carta monouso e disinfettante ad ampio spettro, poi risciacqua.</li>
<li>Butta garze e salviette nel contenitore per rifiuti a rischio infettivo e lavati le mani.</li>
<li>Annota l'episodio sulla scheda cliente.</li>
</ol>
<div class="box deep"><strong class="t">Approfondimento: perché una goccia di sangue secca è ancora un rischio</strong> <p>Secondo i documenti dei CDC statunitensi il virus dell'epatite B può restare infettivo fuori dal corpo, anche nel sangue secco, per <strong>almeno 7 giorni</strong>. Una macchietta invisibile su una tronchesina o sul piano può quindi bastare. È il motivo per cui:</p> <ul><li>lo strumento che ha toccato sangue va sempre pulito e sterilizzato, anche se "sembra pulito";</li> <li>le superfici sporche di sangue si puliscono prima con carta monouso e poi si disinfettano con un prodotto adatto (le linee guida citano anche l'ipoclorito diluito);</li> <li>la vaccinazione contro l'epatite B è la protezione più efficace per chi lavora.</li></ul></div>
<h2>Se ti ferisci tu con uno strumento usato</h2>
<ol class="steps">
<li>Favorisci il sanguinamento premendo per qualche istante.</li>
<li>Lava la ferita per <strong>10 minuti</strong> con acqua corrente e detergente antisettico.</li>
<li>Disinfetta con un disinfettante per cute lesa.</li>
<li>Se lo schizzo è in occhi, naso o bocca: lava abbondantemente con acqua o soluzione fisiologica per 10 minuti.</li>
<li>Rivolgiti subito a un medico o al pronto soccorso per la valutazione del rischio.</li>
</ol>
${B('info', 'Vaccinazioni', 'Le linee guida regionali per l\'estetica consigliano a chi lavora di essere vaccinato contro <strong>tetano</strong> ed <strong>epatite B</strong>. Parlane con il tuo medico.')}
<h2>Rifiuti</h2>
${F('rifiuti-contenitori.svg', 'Tre contenitori: taglienti, rifiuti a rischio infettivo, rifiuti chimici e scaduti.')}
<table>
<tr><th>Rifiuto</th><th>Dove va</th></tr>
<tr><td>Lame, aghi, taglienti</td><td>Contenitore rigido con scritta "rifiuti sanitari pericolosi a rischio infettivo", smaltito da ditta autorizzata.</td></tr>
<tr><td>Garze, cotone, guanti sporchi di sangue</td><td>Contenitore per rifiuti a rischio infettivo.</td></tr>
<tr><td>Salviette con acetone, monomero, cleaner</td><td>Cestino metallico con coperchio e sacchetto, svuotato ogni giorno.</td></tr>
<tr><td>Residui di monomero e gel</td><td>Mai nel lavandino: lascia polimerizzare piccole quantità (il gel in lampada, il monomero mescolato con polvere) e smaltisci come indicato in SDS.</td></tr>
<tr><td>Prodotti scaduti o vietati</td><td>Separati con cartello "PRODOTTI SCADUTI E NON UTILIZZABILI", smaltiti come rifiuti (pericolosi o no secondo la SDS) o ritirati dal fornitore.</td></tr>
</table>
<div class="box pro"><strong class="t">Consiglio da professionista: avanzi di gel e monomero</strong> <p>La polimerizzazione produce calore. Un pezzetto di gel in lampada scalda poco, ma una grande quantità di monomero o di gel che reagisce tutta insieme può scaldarsi molto: il database NOAA avverte che l'etil metacrilato, se contaminato o scaldato, può polimerizzare in modo violento e, in un contenitore chiuso, persino romperlo.</p> <ul><li>Fai polimerizzare solo <strong>piccole quantità</strong> alla volta, su carta, lontano da salviette imbevute di solventi.</li> <li>Non versare mai monomero avanzato nel flacone originale: lo contamini.</li> <li>Per quantità grandi o prodotti scaduti segui la sezione 13 della SDS o affidati al fornitore.</li></ul></div>
<h2>Biancheria e postazione</h2>
<ul>
<li>Preferisci teli e asciugamani monouso; quelli riutilizzabili si cambiano a ogni cliente e si lavano ad almeno <strong>70 °C</strong>.</li>
<li>Camice chiaro, sempre pulito, lavato separatamente dagli abiti personali.</li>
<li>Scadenze: controlla i prodotti, usa prima quelli che scadono prima, scrivi la data di apertura e rispetta il <strong>PAO</strong> (il simbolo del vasetto aperto con "12M", "24M"...).</li>
</ul>
<h2>Errori frequenti</h2>
<ul>
<li>Usare solo il gel alcolico su mani visibilmente sporche di polvere.</li>
<li>Continuare il servizio con un taglio aperto "tanto è piccolo".</li>
<li>Buttare salviette con acetone in un cestino aperto vicino alla lampada o a fonti di calore.</li>
<li>Versare monomero o acetone nello scarico.</li>
</ul>
        `,
          sources: [
            'https://suap.regione.fvg.it/portale/export/sites/SUAP/allegati/archivio_file/LINEE-GUIDA-ESTETICA.pdf',
            'https://www.who.int/publications/i/item/9789241597906',
            'https://www.hse.gov.uk/pubns/guidance/sr13.pdf'
          , 'https://www.afro.who.int/sites/default/files/2017-06/Hand_Hygiene_Why_How_and_When_Brochure.pdf', 'https://stacks.cdc.gov/view/cdc/117930/cdc_117930_DS1.pdf', 'https://cameochemicals.noaa.gov/chemical/3434']
        }
      ]
    },
    /* ------------------------------------------------------------------ 3 */
    {
      id: 'sistemi', n: 3, level: 'base', title: 'Materiali e sistemi',
      summary: [
  "Tutti i sistemi sono a base di (met)acrilati: cambia come induriscono (luce, aria, attivatore) e come si tolgono (acetone o lima).",
  "Gel: oligomeri + fotoiniziatori che induriscono in lampada; hard gel si lima, soft gel si scioglie in acetone.",
  "Acrilico: liquido EMA + polvere PMMA con perossido di benzoile; perla media ≈1,5:1; mai MMA, mai mescolare marche.",
  "Polygel: pasta + slip solution, in lampada. Dip e fibra: resina cianoacrilica + attivatore.",
  "Semipermanente: colore 2–3 settimane, non dà struttura.",
  "Lampada abbinata ai fotoiniziatori del gel: UV ~320–400 nm, LED ~365–405 nm. I watt non indicano la potenza di polimerizzazione."
],
desc: 'Gel UV/LED, acrilico, polygel, semipermanente, dip, soft gel tips, fibra, press-on, lampade ed etichette.',
      lessons: [
        {
          id: 'panoramica',
          title: 'Panoramica dei sistemi',
          min: 10,
          simple: "Gel, acrilico, polygel e gli altri sistemi sono \"parenti\": sono tutti plastiche che si formano sull'unghia. Cambia come diventano duri e come si tolgono. Scegli in base all'unghia della cliente e a cosa vuole.",
          html: `
${F('sistemi.svg', 'Gel, acrilico, polygel e fibra a confronto: come induriscono, punti forti e limiti.')}
<p>Quasi tutti i prodotti per unghie artificiali sono a base di <strong>(met)acrilati</strong>: piccole molecole (monomeri) o catenelle già formate (oligomeri) che, con una reazione chiamata <strong>polimerizzazione</strong>, si uniscono in una rete solida, una plastica. Ciò che cambia tra un sistema e l'altro è:</p>
<ul>
<li><strong>cosa fa partire la reazione</strong>: la luce della lampada (gel, polygel, semipermanente), una reazione chimica tra liquido e polvere, senza lampada (acrilico: iniziatore nella polvere, accelerante nel liquido) oppure un attivatore (fibra, dip);</li>
<li><strong>quanto è fitta la rete</strong>: rete fitta = duro, si toglie limando; rete più "aperta" = l'acetone ci entra e lo scioglie.</li>
</ul>
<h2>Tabella di confronto</h2>
<table>
<tr><th>Sistema</th><th>Indurisce con</th><th>Rimozione</th><th>Punti forti</th><th>Limiti</th><th>Ideale per</th></tr>
<tr><td>Gel costruttore (hard gel)</td><td>Lampada UV/LED</td><td>Limatura</td><td>Nessun odore, lucido, autolivellante</td><td>Picchi di calore con strati spessi; rimozione lunga</td><td>Ricostruzioni, lunghezze medie</td></tr>
<tr><td>Soft gel / builder in bottiglia (BIAB)</td><td>Lampada</td><td>Acetone (10–15 min o secondo produttore)</td><td>Flessibile, rimozione delicata</td><td>Meno adatto a lunghezze importanti</td><td>Rinforzo e coperture su unghia naturale, allungamenti corti</td></tr>
<tr><td>Acrilico</td><td>Reazione liquido + polvere (senza lampada)</td><td>Acetone (15–20 min) o limatura</td><td>Molto resistente, scultura, 3D</td><td>Odore e vapori, tempi di lavoro da gestire</td><td>Lunghezze estreme, sculpting, unghie molto sollecitate</td></tr>
<tr><td>Polygel</td><td>Lampada</td><td>Limatura / acetone (dipende dal prodotto)</td><td>Tempo di lavoro libero, niente monomero liquido</td><td>Curva di apprendimento</td><td>Chi vuole modellare con calma</td></tr>
<tr><td>Semipermanente</td><td>Lampada</td><td>Acetone</td><td>Veloce, colore lucido 2–3 settimane</td><td>Non dà struttura né lunghezza</td><td>Colore su unghia naturale sana</td></tr>
<tr><td>Soft gel tips</td><td>Lampada</td><td>Acetone</td><td>Allungamento veloce e uniforme</td><td>Misure da scegliere bene</td><td>Allungamento rapido</td></tr>
<tr><td>Dip (polvere a immersione)</td><td>Attivatore chimico</td><td>Acetone</td><td>Niente lampada, colore resistente</td><td>Igiene della polvere da gestire</td><td>Coperture colorate</td></tr>
<tr><td>Fibra di vetro / seta</td><td>Resina + attivatore</td><td>Acetone</td><td>Sottile, ottima per riparare</td><td>Tecnica minuziosa</td><td>Riparazioni, rinforzi sottili</td></tr>
<tr><td>Press-on (unghie preformate)</td><td>Colla o adesivo</td><td>Acetone / olio, secondo il tipo</td><td>Rapidissime</td><td>Durata limitata</td><td>Eventi, uso temporaneo</td></tr>
</table>
${F('sistemi-rimozione.svg', 'Si scioglie in acetone o si toglie limando: la differenza sta nella rete di polimero.')}
<div class="box deep"><strong class="t">Approfondimento: l'acrilico non indurisce "con l'aria"</strong> <p>Si dice spesso, per semplicità, che l'acrilico indurisce "all'aria". Il meccanismo reale è chimico: nella polvere c'è un <strong>iniziatore</strong> (perossido di benzoile, BPO), nel liquido un <strong>accelerante</strong>. Quando il monomero bagna le perline di polvere, l'accelerante raggiunge il BPO e lo spezza in radicali liberi, che avviano la polimerizzazione a temperatura ambiente, senza lampada e senza calore esterno.</p> <p>Anzi, l'ossigeno dell'aria tende a rallentare le reazioni radicaliche in superficie. Quello che conta davvero è il rapporto liquido/polvere, la temperatura dell'ambiente e usare liquido e polvere della stessa linea, perché iniziatore e accelerante sono dosati l'uno sull'altro.</p></div>
<h2>Come scegliere: 4 domande</h2>
${F('sistemi-scelta.svg', 'Albero decisionale: unghia, lunghezza, stile di vita, allergie.')}
<ol class="steps">
<li><strong>Ci sono controindicazioni o allergie agli acrilati?</strong> Se sì, nessun sistema a base di acrilati: consiglia il dermatologo.</li>
<li><strong>Vuole lunghezza o solo colore/rinforzo?</strong> Solo colore: semipermanente. Rinforzo corto: soft gel/BIAB. Lunghezza: hard gel, acrilico, polygel o soft gel tips.</li>
<li><strong>Com'è l'unghia?</strong> Sottile e flessibile: sistemi flessibili, strati sottili. Rosicchiata o a forma difficile: costruzione su cartina (moduli 7 e 13).</li>
<li><strong>Che vita fa?</strong> Mani in acqua, lavoro manuale, sport: lunghezze corte-medie e sistema resistente.</li>
</ol>
<div class="box case"><strong class="t">Caso pratico</strong> <p>Una cliente vuole "le unghie più resistenti possibile": fa la parrucchiera, ha le mani in acqua e shampoo tutto il giorno e porta unghie naturali sottili. Quale sistema? Prima di scegliere il prodotto, ragiona sulle cause dei problemi: acqua e detergenti fanno gonfiare e sgonfiare la lamina, e le lunghezze fanno leva.</p> <p>Una scelta ragionevole: lunghezza corta-media, forma con angoli morbidi, preparazione molto accurata, bordo libero ben sigillato, un sistema che la tua mano gestisce bene (gel costruttore o acrilico) e il consiglio di usare i guanti per i trattamenti chimici. La resistenza viene più da struttura e preparazione che dal nome del sistema.</p></div>
<h2>Regole che valgono per tutti</h2>
<ul>
<li>Usa <strong>prodotti dello stesso sistema</strong> (stesso produttore) dalla base al top: sono studiati per legarsi tra loro.</li>
<li>Leggi la <strong>scheda tecnica</strong>: tempi, lampada, spessori, rimozione.</li>
<li>Il prodotto liquido o non polimerizzato <strong>non tocca la pelle</strong>.</li>
</ul>
<div class="box deep"><strong class="t">Approfondimento: perché marche diverse non vanno d'accordo</strong> <ul><li><strong>Fotoiniziatori diversi</strong>: base, gel e top possono essere calibrati su lunghezze d'onda diverse. Uno strato può polimerizzare bene e l'altro restare crudo con la stessa lampada.</li> <li><strong>Ritiro diverso</strong>: tutti i prodotti si ritirano un poco mentre polimerizzano. Se due strati si ritirano in modo diverso, nasce una tensione tra loro che favorisce distacchi.</li> <li><strong>Liquido e polvere</strong>: la quantità di iniziatore nella polvere è calcolata sull'accelerante del liquido della stessa linea.</li></ul> <p>Un sistema "chiuso" non è una scelta di marketing: è il modo in cui il produttore ha testato l'aggancio tra gli strati.</p></div>
<h2>Errori frequenti</h2>
<ul>
<li>Promettere a tutte "il sistema più resistente": la resistenza dipende soprattutto da preparazione e struttura.</li>
<li>Usare il semipermanente per allungare: non ha struttura, si spezza.</li>
<li>Mescolare base di una marca, gel di un'altra e top di una terza: aumentano sollevamenti e sottopolimerizzazione.</li>
</ul>
        `,
          sources: [
            'https://www.beyondpolish.com/blogs/news/gel-x-vs-builder-gel-vs-poly-gel',
            'https://c8nailsupply.com/blogs/news/builder-gel-vs-hard-gel-vs-polygel',
            'https://akzentz.com/blogs/education-professional-nail-education/professional-gel-systems-guide',
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/light-cured-gels-dip-systems',
            'https://open-exam-prep.com/study-guides/ca-nail-technician/chemical-nail-services-enhancements/liquid-powder-acrylic-systems'
          , 'https://open-exam-prep.com/study-guides/mn-nail-technician/nail-enhancements-chemistry-application/acrylic-monomer-polymer-chemistry', 'https://nailknowledge.org/blog/the-inhibition-layer', 'https://nailknowledge.org/blog/wet-nails', 'https://pronails.com/naily-news/tech-talk-n28-what-determines-lamp-and-product-compatibility', 'https://nailknowledge.org/blog/uv-gel-polish-shrinkage', 'https://nailknowledge.org/nail-knowledge-base/is-there-such-a-thing-as-a-universal-acrylic-nail-powder-that-works-with-any-monomer-liquid']
        },
        {
          id: 'gel',
          title: 'Il gel UV/LED',
          min: 13,
          simple: "Il gel è un \"miele\" che resta morbido finché non lo metti sotto la lampada: la luce accende i fotoiniziatori e il gel diventa duro. Strati sottili, tempi giusti e lampada giusta: così indurisce tutto e non scalda.",
          html: `
<h2>Di cosa è fatto</h2>
${F('gel-chimica.svg', 'Oligomeri e fotoiniziatori: la luce fa partire la reazione e le catene si uniscono in una rete.')}
<ul>
<li><strong>Oligomeri</strong>: catenelle già "pre-unite" di (met)acrilati, spesso uretano-acrilati. Danno corpo e flessibilità e rendono il gel denso.</li>
<li><strong>Monomeri</strong>: molecole piccole che regolano viscosità e adesione (per esempio HEMA nelle basi).</li>
<li><strong>Fotoiniziatori</strong>: sostanze che assorbono la luce di una certa lunghezza d'onda e fanno partire la reazione.</li>
<li><strong>Additivi</strong>: pigmenti, cover, glitter, stabilizzanti.</li>
</ul>
<p>Sotto la lampada i fotoiniziatori producono "radicali liberi" che agganciano le catene tra loro: si forma una rete solida. La reazione <strong>produce calore</strong> (è esotermica): più gel c'è, più calore.</p>
<h2>I tipi di gel</h2>
<ul>
<li><strong>Base / bonder</strong>: crea l'aggancio alla lamina.</li>
<li><strong>Costruttore (builder)</strong>: dà struttura e lunghezza. Può essere autolivellante (fluido, si stende da solo) o ad alta viscosità (resta dove lo metti). Esistono versioni trasparenti, rosa, lattiginose e "cover" (camouflage).</li>
<li><strong>Sigillante (top)</strong>: protegge e lucida; con o senza strato di dispersione.</li>
<li><strong>Gel colorati</strong> e <strong>semipermanenti</strong> (modulo 14).</li>
</ul>
<h2>Hard gel e soft gel</h2>
<table>
<tr><th></th><th>Hard gel</th><th>Soft gel (soak-off)</th></tr>
<tr><td>Rete di polimero</td><td>Fitta</td><td>Più aperta, porosa</td></tr>
<tr><td>Acetone</td><td>Non lo scioglie</td><td>Lo scioglie (circa 10–15 minuti, secondo produttore)</td></tr>
<tr><td>Rimozione</td><td>Limatura, lasciando un velo</td><td>Soak-off dopo aver opacizzato il top</td></tr>
<tr><td>Uso tipico</td><td>Ricostruzioni, lunghezze medie</td><td>Rinforzi, coperture, semipermanente, allungamenti corti</td></tr>
</table>
<h2>Monofasico, bifasico, trifasico</h2>
${F('gel-fasi.svg', 'Trifasico, bifasico e monofasico: base, costruttore e sigillante separati o riuniti in un solo prodotto.')}
<ul>
<li><strong>Monofasico</strong>: un solo gel fa da base, costruttore e sigillante. Veloce, meno controllo.</li>
<li><strong>Bifasico</strong>: base+costruttore in un prodotto, più un sigillante.</li>
<li><strong>Trifasico</strong>: tre prodotti separati, più controllo su ogni fase. Consigliato per imparare.</li>
</ul>
<h2>Lo strato di dispersione</h2>
${F('strato-dispersione.svg', 'L\'ossigeno blocca la reazione in superficie: resta una patina appiccicosa.')}
<p>Dopo la lampada molti gel restano <strong>appiccicosi in superficie</strong>. Non è un difetto: l'ossigeno dell'aria impedisce alla reazione di completarsi nello strato più esterno. Questa patina (strato di dispersione o di inibizione) aiuta lo strato successivo ad aggrapparsi.</p>
<ul>
<li>Tra uno strato e l'altro <strong>non si toglie</strong> (salvo indicazione del produttore).</li>
<li>Alla fine si toglie con il <strong>cleaner</strong> o alcol isopropilico, con una <strong>salvietta pulita per ogni dito</strong>: è gel non polimerizzato e non deve finire sulla pelle.</li>
<li>I top <strong>no-wipe</strong> sono formulati per non lasciarla.</li>
</ul>
<div class="box deep"><strong class="t">Approfondimento: che cosa fa l'ossigeno</strong> <p>Nella polimerizzazione del gel i radicali liberi allungano le catene. L'ossigeno dell'aria reagisce con le estremità delle catene in crescita e le "blocca": in superficie le catene restano corte e lo strato rimane molle e appiccicoso. Sotto, dove l'ossigeno non arriva, la reazione va avanti. Per questo il nome più corretto è <strong>strato di inibizione</strong> (da ossigeno), più che "di dispersione".</p> <ul><li>Lo strato è gel polimerizzato per meno della metà: è <strong>allergizzante</strong> e non va toccato.</li> <li>Se è insolitamente spesso, la causa è spesso la lampada: luce debole, lunghezza d'onda sbagliata, LED sporchi o mano posizionata male.</li> <li>Non è vero che il gel indurisce "dall'alto" o "dal basso": la luce raggiunge tutti gli strati insieme, ma si indebolisce in profondità.</li></ul></div>
<h2>Applicare il gel: i passi base</h2>
<ol class="steps">
<li>Preparazione completa (modulo 5) e disidratante; primer o bonder se il sistema lo prevede.</li>
<li>Base in strato sottile, senza toccare pelle e pieghe; polimerizza.</li>
<li>Costruttore in strati sottili: prima uno strato di aggancio, poi la struttura con l'apex in zona 2.</li>
<li>Prima di ogni lampada controlla di profilo e togli le sbavature dalle pieghe.</li>
<li>Polimerizza con i tempi della scheda tecnica; pollice a parte.</li>
<li>Rimuovi lo strato di dispersione, lima e rifinisci; top, lampada, cleaner se necessario.</li>
</ol>
<h2>Il picco di calore</h2>
<p>Quando la cliente sente <strong>bruciore</strong> in lampada, la reazione sta producendo troppo calore tutto insieme. Succede con strati spessi, lamine sottili o troppo limate, lampade molto potenti.</p>
<ul>
<li>Strati sottili; lamina non assottigliata.</li>
<li><strong>Flash cure</strong>: pochi secondi in lampada, poi pausa, poi polimerizzazione completa (alcune lampade hanno la modalità "low heat").</li>
<li>Se brucia, togli la mano per qualche secondo e poi completa la polimerizzazione (modulo 11).</li>
</ul>
<div class="box deep"><strong class="t">Approfondimento: da dove viene il bruciore</strong> <p>Ogni legame che si forma tra le molecole libera un po' di calore. Su un'unghia si formano milioni di legami: se si formano <strong>tutti in pochi secondi</strong>, il calore non fa in tempo a disperdersi. I recettori del letto ungueale danno la sensazione di bruciore quando la temperatura arriva a circa 46 °C.</p> <ul><li>Un gel pensato per le vecchie lampade UV a tubi, messo sotto una LED potente, polimerizza più in fretta e scalda di più.</li> <li>La stessa quantità di calore distribuita in un minuto invece che in dieci secondi è molto più sopportabile: è il principio del flash cure.</li> <li>Una lamina assottigliata o un letto già irritato dalla limatura sentono il calore molto prima.</li></ul> <p>Il bruciore ripetuto può favorire il distacco della lamina dal letto (onicolisi): non è un fastidio da ignorare.</p></div>
<h2>Pro e contro</h2>
<p><strong>+</strong> nessun odore, autolivellante, finitura lucida, tempo di lavoro libero finché non va in lampada. <strong>−</strong> picchi di calore con strati spessi; rischio allergia se il gel non polimerizza del tutto o tocca la pelle; serve la lampada giusta.</p>
<h2>Conservazione</h2>
<ul>
<li>Vasetti e flaconi <strong>chiusi</strong> e lontani da luce solare e lampade: la luce li fa indurire.</li>
<li>Preleva con spatola pulita; non rimettere nel vasetto gel già usato.</li>
<li>Non lasciare il pennello carico di gel vicino alla lampada.</li>
</ul>
<h2>Errori frequenti</h2>
<ul>
<li>Strato troppo spesso: polimerizza in superficie ma resta crudo sotto (grinze, allergie, sollevamenti).</li>
<li>Pulire lo strato di dispersione con la stessa salvietta su tutte le dita: porti gel crudo sulla pelle.</li>
<li>Accorciare i tempi in lampada "perché tanto è duro": il gel sembra duro anche se non è completamente polimerizzato.</li>
</ul>
${B('tip', 'Consiglio', 'Stendi strati sottili e rispetta i tempi della scheda tecnica: uno strato troppo spesso polimerizza solo in superficie e fa grinze.')}
        
<div class="box deep"><strong class="t">Approfondimento: il gel si ritira mentre indurisce</strong> <p>Tutti i prodotti per unghie si <strong>ritirano</strong> un poco durante la polimerizzazione: le molecole, unendosi, si avvicinano. Il ritiro avviene durante la lampada, non prima. Il risultato visibile è che i bordi tendono a "tirarsi indietro" verso il centro.</p> <ul><li>Strati sottili e ben sigillati sul bordo libero limitano il problema.</li> <li>Una polimerizzazione eccessiva (lampada troppo potente per quel gel) può aumentare il ritiro e il distacco dai bordi.</li> <li>Lavorare più velocemente o più lentamente prima della lampada non cambia il ritiro.</li></ul> <p>Se un prodotto "si ritira" sempre dai lati, controlla l'abbinamento con la lampada prima di accusare la preparazione.</p></div>
`,
          sources: [
            'https://areasosta.com/faq/che-differenza-ce-tra-gel-monofasico-e-trifasico',
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/light-cured-gels-dip-systems',
            'https://open-exam-prep.com/study-guides/nc-nail-technician/nail-enhancement-systems/gels-soft-hard-hybrid',
            'https://akzentz.com/blogs/education-professional-nail-education/professional-gel-systems-guide',
            'https://nailknowledge.org/glossary/soak-off-gels',
            'https://scratchmagazine.co.uk/feature/heat-spikes-in-gel-nail-services-why-they-happen-how-to-avoid-them'
          , 'https://nailknowledge.org/blog/the-inhibition-layer', 'https://nailknowledge.org/nail-knowledge-base/inhibition-layer-and-no-cleanse-gels', 'https://nailknowledge.org/blog/heat-spikes', 'https://nailknowledge.org/blog/uv-gel-polish-shrinkage']
        },
        {
          id: 'acrilico',
          videos: [{"id": "2vezvcjA-cc", "title": "Consigli utili sul sistema acrilico per le unghie", "channel": "Accademia Nails", "lang": "IT"}],
          title: 'L\'acrilico (liquido e polvere)',
          min: 12,
          simple: "Con l'acrilico mescoli sul pennello un liquido (monomero) e una polvere (polimero): si forma una pallina che indurisce da sola in pochi minuti, senza lampada. La quantità giusta di liquido è il segreto.",
          html: `
<p>L'acrilico unisce un <strong>monomero liquido</strong> e un <strong>polimero in polvere</strong>. Quando si incontrano sul pennello parte la reazione: in pochi minuti la "perla" diventa dura, senza lampada.</p>
${F('acrilico-chimica.svg', 'Cosa c\'è nel liquido e nella polvere, e cosa succede quando si incontrano.')}
<h2>Cosa c'è dentro</h2>
<table>
<tr><th>Liquido (monomero)</th><th>Polvere (polimero)</th></tr>
<tr><td><strong>EMA</strong> (etil metacrilato): il monomero principale.</td><td>Perline di <strong>PMMA</strong> (polimetil metacrilato) già polimerizzato.</td></tr>
<tr><td><strong>Catalizzatore/accelerante</strong>: regola la velocità della reazione.</td><td><strong>Perossido di benzoile</strong> (BPO, circa 1–2%): l'iniziatore che fa partire la reazione.</td></tr>
<tr><td><strong>Inibitore</strong> (es. MEHQ, in tracce): impedisce che il liquido indurisca nel flacone.</td><td>Pigmenti (rosa, bianco, cover, colori).</td></tr>
<tr><td><strong>Reticolante</strong>: rende il risultato più resistente.</td><td></td></tr>
</table>
${B('warn', 'Liquido e polvere della stessa linea', 'La quantità di iniziatore nella polvere è calibrata sul liquido dello stesso produttore. Mescolare marche diverse può dare un acrilico sottopolimerizzato (più monomero libero, più rischio di allergia) o fragile.')}
${B('danger', 'DMTA e regole UE', 'Un accelerante classico dei liquidi, la DMTA (N,N-dimetil-p-toluidina), è vietato nei cosmetici UE dal 1° settembre 2025 (Reg. UE 2025/877). Controlla l\'INCI dei liquidi che usi e chiedi al fornitore la versione conforme.')}
<div class="box deep"><strong class="t">Approfondimento: che cosa succede sul pennello</strong> <p>Il monomero liquido bagna le perline di polimero e ne ammorbidisce la superficie. L'accelerante sciolto nel liquido entra nelle perline e incontra il <strong>perossido di benzoile</strong> (circa 1–2% del peso della polvere): il suo legame ossigeno-ossigeno si spezza e nascono i radicali liberi, che uniscono il monomero in catene intorno alle perline.</p> <p>Ecco perché la perla bagnata è un problema: c'è <strong>troppo monomero per l'iniziatore disponibile</strong>. Una parte del liquido non reagisce, resta libera nel prodotto, lo indebolisce e può arrivare alla pelle. La perla troppo asciutta, al contrario, non ha abbastanza liquido per bagnare tutte le perline: restano granuli e porosità.</p></div>
<h2>La perla</h2>
${F('perla-acrilico.svg', 'La consistenza della perla dipende dal rapporto liquido/polvere.')}
<table>
<tr><th>Perla</th><th>Rapporto liquido:polvere</th><th>Come appare</th><th>Problemi</th></tr>
<tr><td><strong>Bagnata</strong></td><td>circa 2:1</td><td>Cola, perde forma subito.</td><td>Scivola nei solchi, ritira, indurisce lentamente, lascia monomero non reagito (rischio allergia).</td></tr>
<tr><td><strong>Media</strong> ✓</td><td>circa 1,5:1</td><td>Lucida, bombata, resta in forma qualche secondo e poi si distende.</td><td>È quella giusta.</td></tr>
<tr><td><strong>Asciutta</strong></td><td>circa 1:1</td><td>Granulosa, opaca, polverosa.</td><td>Poca adesione, bolle e porosità, fragile.</td></tr>
</table>
<div class="box case"><strong class="t">Caso pratico</strong> <p>Le tue perle sembrano giuste, ma dopo qualche giorno compaiono bolline e la superficie limata è porosa. Ragiona per ordine:</p> <ol><li><strong>Perla troppo asciutta</strong>? Se è opaca e gessosa appena posata, scarica meno il pennello.</li> <li><strong>Picchietti troppo forte</strong> o lavori la perla quando ha già iniziato a indurire? Intrappoli aria. Appoggia, poi accarezza.</li> <li><strong>Pennello sporco</strong> o pieno di polvere secca? Pulisci tra una perla e l'altra.</li> <li><strong>Liquido e polvere</strong> di linee diverse? Torna a una coppia dello stesso produttore.</li></ol> <p>Cambia una sola variabile alla volta, altrimenti non scopri mai quale era la causa.</p></div>
<h2>Come si forma una perla: i passi</h2>
${F('acrilico-dappen.svg', 'Dappen dish, pennello e polvere: immergi, scarica, raccogli.')}
<ol class="steps">
<li>Versa nel <strong>dappen dish</strong> (bicchierino con coperchio) solo il monomero che ti serve; chiudi subito il flacone.</li>
<li>Immergi il pennello (misura 8–12) fino alla ghiera e lascia che si impregni.</li>
<li>Scarica l'eccesso premendo un lato del pennello sul bordo del dappen: la quantità di liquido rimasta decide la perla.</li>
<li>Appoggia la punta nella polvere e trascinala piano per 1–2 secondi: si forma una pallina.</li>
<li>Guarda la perla: lucida e bombata = giusta. Se è granulosa, la prossima volta scarica meno; se cola, scarica di più.</li>
<li>Appoggia la perla sull'unghia e lavorala picchiettando e accarezzando, prima che indurisca.</li>
<li>Pulisci il pennello nel monomero e asciugalo su carta senza pelucchi tra una perla e l'altra.</li>
</ol>
<h2>Cosa cambia i tempi di lavorazione</h2>
<ul>
<li><strong>Temperatura</strong>: con il caldo la reazione accelera, con il freddo rallenta. Lavora in un ambiente temperato e segui la scheda tecnica.</li>
<li><strong>Quantità di liquido</strong>: perle più bagnate restano lavorabili più a lungo ma induriscono male.</li>
<li><strong>Tipo di polvere</strong>: esistono polveri a presa rapida e a presa lenta; per imparare scegli quella lenta.</li>
</ul>
<div class="box pro"><strong class="t">Consiglio da professionista: la temperatura del salone</strong> <ul><li>In una stanza calda un acrilico a presa rapida indurisce in fretta e libera tutto il calore in poco tempo: la cliente sente <strong>bruciore</strong>. D'estate preferisci una polvere a presa più lenta.</li> <li>In una stanza fredda la reazione rallenta: la perla resta morbida, scivola e indurisce male. Non scaldare mai il monomero (è infiammabile): porta prodotti e ambiente a temperatura normale.</li> <li>Una polvere di un'altra linea può cambiare i tempi in modo imprevedibile e far scaldare il prodotto.</li></ul> <p>Se cambia la stagione e cambiano i tuoi risultati, prima di cambiare tecnica guarda il termometro.</p></div>
<h2>Pro e contro</h2>
<p><strong>+</strong> il sistema più resistente sulle lunghezze lunghe, ottimo per sculpting e 3D, si toglie in acetone (circa 15–20 minuti). <strong>−</strong> odore e vapori (serve aspirazione), tempi di lavorazione da gestire, perla da imparare.</p>
<h2>Sicurezza</h2>
<ul>
<li>Solo monomero <strong>EMA</strong>, mai MMA (vedi modulo 2).</li>
<li>Dappen con coperchio; non lasciare monomero all'aria.</li>
<li>Il monomero avanzato non va nello scarico: assorbilo con carta e lascialo evaporare sotto aspirazione o fallo reagire con un po' di polvere, poi butta nel cestino con coperchio (o segui la SDS).</li>
<li>Il monomero è infiammabile: lontano da fiamme e fonti di calore.</li>
</ul>
<h2>Errori frequenti</h2>
<ul>
<li>Perla bagnata vicino alla cuticola: scivola sulla pelle.</li>
<li>Pennello lavato in acetone: le setole si seccano. Si pulisce nel monomero (o con il cleaner indicato dal produttore).</li>
<li>Toccare la perla con le dita per "sistemarla".</li>
</ul>
        `,
          sources: [
            'https://open-exam-prep.com/study-guides/ca-nail-technician/chemical-nail-services-enhancements/liquid-powder-acrylic-systems',
            'https://open-exam-prep.com/study-guides/mn-nail-technician/nail-enhancements-chemistry-application/acrylic-monomer-polymer-chemistry',
            'https://nailknowledge.org/nail-knowledge-base/is-there-such-a-thing-as-a-universal-acrylic-nail-powder-that-works-with-any-monomer-liquid',
            'https://publications.iarc.fr/_publications/media/download/5405/6e7ede0da351f42c09efa74e0950a97cf889dfc3.pdf',
            'https://nsinails.com.au/pages/instruction-how-to-clean-your-brush'
          , 'https://nailknowledge.org/blog/heat-spikes', 'https://cameochemicals.noaa.gov/chemical/3434']
        },
        {
          id: 'polygel-altri',
          videos: [{"id": "7Y2eF_L9cgs", "title": "Tutorial semipermanente in 9 step per principianti", "channel": "Nail Couture Italia", "lang": "IT"}, {"id": "z-NbcApd4Y8", "title": "Come applicare le soft gel tips", "channel": "Proglow Italia", "lang": "IT"}],
          title: 'Polygel, semipermanente, soft gel tips e fibra',
          min: 14,
          simple: "Il polygel è una pasta che modelli con calma e poi indurisci in lampada. Il semipermanente dà solo colore. Le soft gel tips sono unghie già pronte da incollare con gel. La fibra è un tessuto sottile che rinforza e ripara.",
          html: `
<h2>Polygel (acrygel)</h2>
${F('polygel-step.svg', 'Polygel: preleva, taglia, appoggia, modella con slip solution, polimerizza.')}
<p>È una pasta ibrida che unisce caratteristiche di acrilico e gel: densa come una plastilina morbida, si modella con il pennello inumidito di <strong>slip solution</strong> (il liquido indicato dal produttore) e <strong>indurisce solo in lampada</strong>.</p>
<ol class="steps">
<li>Preparazione e base del sistema, polimerizzata.</li>
<li>Preleva dal tubetto una piccola quantità con una spatola pulita e tagliala alla misura che serve.</li>
<li>Appoggiala al centro dell'unghia o sulla cartina/dual form.</li>
<li>Inumidisci appena il pennello di slip solution e distribuisci la pasta: zona 3 sottile, apex in zona 2, zona 1 sottile.</li>
<li>Controlla di profilo e dalla punta; polimerizza con i tempi della scheda tecnica.</li>
<li>Lima, rifinisci e applica il top.</li>
</ol>
<p><strong>+</strong> tempo di lavoro libero, niente monomero liquido, leggero. <strong>−</strong> curva di apprendimento; troppa slip solution rende la pasta scivolosa e la indebolisce; sollevamenti se la preparazione è scarsa.</p>
<div class="box deep"><strong class="t">Approfondimento: il polygel è un gel, con le regole del gel</strong> <p>Anche se si lavora come una pasta, il polygel indurisce con la luce: valgono le stesse regole del gel. Ha uno strato di inibizione da togliere a fine lavoro, produce calore se lo strato è spesso, si ritira un poco in lampada e ha bisogno della lampada indicata dal produttore.</p> <p>La slip solution serve solo a non far attaccare la pasta al pennello. Ciò che resta sulla superficie non fa parte della rete di polimero: se ne usi tanto, la pasta diventa scivolosa e la superficie più debole. Tieni il pennello appena umido e asciugalo spesso su carta. Su pezzi spessi (allungamenti lunghi) usa il flash cure per evitare il picco di calore.</p></div>
<h2>Semipermanente (gel polish)</h2>
<p>Base → colore → top, ognuno in lampada; dura circa <strong>2–3 settimane</strong> e si toglie con acetone. <strong>Non allunga</strong> e non dà struttura: protegge e colora l'unghia naturale.</p>
${F('tut-semipermanente.svg', 'Semipermanente passo passo: due strati sottili di colore e bordo libero sigillato.')}
<ol class="steps">
<li>Preparazione delicata: cuticola, opacizzazione leggera (240 o più fine), polvere via, disidratante.</li>
<li>Base sottile, bordo libero sigillato; lampada.</li>
<li>Primo strato di colore molto sottile; lampada.</li>
<li>Secondo strato di colore; lampada.</li>
<li>Top, bordo libero sigillato; lampada; cleaner se il top lo richiede.</li>
<li>Olio per cuticole a fine servizio.</li>
</ol>
<div class="box deep"><strong class="t">Approfondimento: perché i colori scuri vogliono strati più sottili</strong> <p>I pigmenti e i glitter si comportano come tanti piccoli <strong>ombrelli</strong>: assorbono o riflettono la luce prima che arrivi in profondità. In un nero, un rosso scuro o un glitter lo strato in basso riceve molta meno luce di quello in alto e può restare molle, anche se la superficie sembra perfetta.</p> <ul><li>Stendi colori scuri e glitter in strati <strong>molto sottili</strong>, polimerizzando ciascuno per il tempo pieno.</li> <li>Allungare il tempo di lampada non salva uno strato troppo spesso: quando i fotoiniziatori si esauriscono, la reazione si ferma.</li></ul> <p>Segnali di sottopolimerizzazione: grinze, colore che si sposta sotto il top, semipermanente che si stacca in pellicola.</p></div>
<h2>Soft gel tips</h2>
${F('tut-soft-gel-tips.svg', 'Soft gel tips passo passo: misura, gel adesivo, applicazione con flash cure, lampada e rifinitura.')}
<p>Sono tip "full cover" in gel soak-off, che coprono tutta l'unghia. Si incollano con un gel adesivo che indurisce in lampada.</p>
<ol class="steps">
<li>Preparazione, opacizzazione con grana 180–240, disidratante e primer/bonder.</li>
<li>Scelta della misura <strong>da solco a solco</strong>, per tutte e dieci le dita prima di iniziare.</li>
<li>Opacizza leggermente l'interno del tip se il produttore lo indica.</li>
<li>Gel adesivo dentro il tip; appoggia partendo dalla zona cuticolare (senza toccarla) e abbassa per far uscire l'aria.</li>
<li>Pre-polimerizzazione breve (flash) tenendo fermo il tip, poi polimerizzazione completa.</li>
<li>Rifinitura e top. Rimozione con acetone.</li>
</ol>
<h2>Fibra di vetro e seta</h2>
${F('tut-fibra.svg', 'Rinforzo in fibra passo passo: taglio, resina, attivatore a pennello, limatura e sigillatura.')}
<p>Un tessuto sottilissimo viene impregnato di <strong>resina cianoacrilica</strong> (la stessa famiglia della colla per tip) e indurito con un <strong>attivatore</strong>. La fibra di vetro è più resistente, la seta più invisibile.</p>
<ol class="steps">
<li>Taglia la fibra un po' più piccola dell'unghia, senza toccarla con le dita (si sporca di grasso).</li>
<li>Strato sottile di resina sull'unghia; appoggia la fibra a circa 1 mm da cuticola e lati.</li>
<li>Resina sopra la fibra finché diventa trasparente.</li>
<li>Attivatore <strong>a pennello o a goccia</strong>; se usi lo spray, poco e da lontano: l'eccesso produce calore.</li>
<li>Lima, ripeti se serve un secondo strato, rifinisci.</li>
</ol>
${F('fibra-riparazione.svg', 'Riparare una crepa con la fibra: la toppa supera la crepa di qualche millimetro per lato.')}
<div class="box deep"><strong class="t">Approfondimento: come indurisce la resina</strong> <p>La resina della fibra (e la colla per tip) è un <strong>cianoacrilato</strong>: indurisce quando incontra tracce di umidità, che fanno partire una reazione molto veloce. L'attivatore fornisce direttamente ciò che serve alla reazione, così indurisce tutto lo spessore in pochi secondi.</p> <ul><li>La reazione produce calore: <strong>più è veloce, più scalda</strong>. Troppo attivatore, spruzzato da vicino, dà bruciore.</li> <li>Gli acceleranti rendono il risultato più rapido ma anche più fragile e a volte opaco o biancastro.</li> <li>Con aria molto secca la resina indurisce lentamente; con aria umida più in fretta.</li></ul> <p>Per questo si usa poco attivatore, da lontano, oppure a pennello.</p></div>
<h2>Tabella riassuntiva</h2>
<table>
<tr><th></th><th>Polygel</th><th>Semipermanente</th><th>Soft gel tips</th><th>Fibra</th></tr>
<tr><td>Allunga</td><td>Sì</td><td>No</td><td>Sì</td><td>Poco (riparazioni)</td></tr>
<tr><td>Indurisce con</td><td>Lampada</td><td>Lampada</td><td>Lampada</td><td>Attivatore</td></tr>
<tr><td>Rimozione</td><td>Lima o acetone</td><td>Acetone</td><td>Acetone</td><td>Acetone</td></tr>
<tr><td>Difficoltà</td><td>Media</td><td>Bassa</td><td>Media</td><td>Alta</td></tr>
</table>
<h2>Errori frequenti</h2>
<ul>
<li>Polygel "annegato" nella slip solution: scivola e si indebolisce.</li>
<li>Semipermanente in strati spessi per coprire prima: grinze e sottopolimerizzazione.</li>
<li>Soft gel tip troppo stretto: preme sulle pieghe, si solleva ai lati.</li>
<li>Attivatore spray abbondante e vicino: bruciore e resina opaca.</li>
</ul>
        `,
          sources: [
            'https://sophiecress.com/blog/gel-x-nails-a-step',
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/light-cured-gels-dip-systems',
            'https://www.beyondpolish.com/blogs/news/gel-x-vs-builder-gel-vs-poly-gel',
            'https://c8nailsupply.com/blogs/news/builder-gel-vs-hard-gel-vs-polygel'
          , 'https://nailknowledge.org/blog/heat-spikes', 'https://nailknowledge.org/blog/the-inhibition-layer', 'https://nailknowledge.org/blog/uv-curing-why-thin-layers-matter-for-perfect-nails', 'https://dm.henkel-dam.com/is/content/henkel/Medical-Best-Practices-Flyer', 'https://mdpi-res.com/d_attachment/molecules/molecules-23-00465/article_deploy/molecules-23-00465.pdf']
        },
        {
          id: 'lampade',
          title: 'Lampade UV e LED',
          min: 11,
          simple: "Ogni gel \"si accende\" con una certa luce: usa la lampada consigliata per quel gel. Contano le lunghezze d'onda e l'intensità che arriva sull'unghia, non i watt scritti sulla scatola.",
          html: `
${F('lampade.svg', 'Bande di emissione tipiche delle lampade UV, LED e dual, in nanometri.')}
<h2>Che luce fanno le lampade</h2>
<p>La luce si misura in <strong>nanometri (nm)</strong>: è la sua "lunghezza d'onda". Gli ultravioletti A (UVA) vanno circa da 315 a 400 nm; oltre 400 nm inizia la luce visibile viola. I fotoiniziatori dei gel reagiscono solo a certe lunghezze d'onda.</p>
<table>
<tr><th>Tipo</th><th>Emissione indicativa</th><th>Tempi tipici</th><th>Durata della sorgente</th></tr>
<tr><td><strong>UV classica</strong> (tubi fluorescenti)</td><td>banda larga, circa 320–400 nm (picco spesso intorno a 365 nm)</td><td>circa 2 minuti per strato</td><td>I tubi perdono potenza nel tempo: alcuni manuali indicano il cambio ogni 4–6 mesi di uso professionale; segui il produttore.</td></tr>
<tr><td><strong>LED</strong></td><td>bande strette, intorno a <strong>365 e/o 405 nm</strong> (alcune fonti danno 385–405)</td><td>30–60 s per strati sottili; più a lungo per costruttori e colori scuri, secondo scheda tecnica</td><td>Diodi di lunga durata (decine di migliaia di ore), ma si sporcano e possono guastarsi.</td></tr>
<tr><td><strong>Dual UV/LED</strong></td><td>due picchi, es. 365 + 405 nm</td><td>secondo prodotto</td><td>Le più diffuse.</td></tr>
</table>
${B('info', 'Le fonti non usano gli stessi numeri', 'Per i LED alcuni manuali indicano 395–405 nm, altri 365–405 nm; per le UV 300–410 o 320–400 nm. Non serve ricordarli a memoria: serve leggere sulla scheda del tuo gel a quale lunghezza d\'onda polimerizza e controllare che la tua lampada la emetta.')}
<h2>Watt, intensità e abbinamento</h2>
${F('lampada-watt-vs-nm.svg', 'Due lampade: i watt dicono quanta corrente consumano, non quanta luce utile arriva sull\'unghia.')}
<ul>
<li>I <strong>watt</strong> indicano quanta corrente consuma la lampada, non quanta luce utile arriva sull'unghia. Una LED da pochi watt può polimerizzare meglio di una UV da 36 W.</li>
<li>Conta l'<strong>irradianza</strong> (luce che arriva sulla superficie) alle <strong>lunghezze d'onda giuste</strong>.</li>
<li>Lampada "sbagliata" o debole → gel <strong>sottopolimerizzato</strong>: sembra duro, ma sotto resta crudo (sollevamenti, grinze, allergie).</li>
<li>Lampada troppo potente per quel gel → <strong>picco di calore</strong> e prodotto fragile.</li>
</ul>
${B('warn', 'Le lampade "senza UV"', 'Una lampada che non emette nulla tra 365 e 405 nm non può polimerizzare la maggior parte dei gel. Le scritte "UV-free" spesso indicano solo che la luce è intorno ai 405 nm, cioè al confine tra UV e visibile. Fidati della scheda tecnica, non dello slogan.')}
<div class="box deep"><strong class="t">Approfondimento: fotoiniziatori che si consumano</strong> <p>Ogni molecola di fotoiniziatore, assorbendo la luce, si trasforma e avvia la reazione una volta sola. Quando sono finiti, la polimerizzazione si ferma. Due conseguenze:</p> <ul><li>Lasciare la mano più a lungo in lampada <strong>non recupera</strong> uno strato troppo spesso o una lampada sbagliata: il fondo resta crudo.</li> <li>Più luce in meno tempo vuol dire più calore concentrato: una lampada "più forte" non è sempre migliore per il tuo gel.</li></ul> <p>La luce inoltre si indebolisce entrando nel gel, tanto più se è pigmentato. Per questo la scheda tecnica indica insieme tre cose che vanno rispettate tutte: lampada, tempo e spessore.</p></div>
<h2>Usare bene la lampada</h2>
${F('lampada-posizione.svg', 'Mano piatta e dita tutte dentro la lampada; il pollice si polimerizza a parte.')}
<ol class="steps">
<li>Usa la lampada <strong>indicata dal produttore</strong> del gel; se cambi lampada, fai una prova.</li>
<li>Mano <strong>piatta</strong>, dita dentro e centrate; il <strong>pollice a parte</strong>, perché di lato non riceve abbastanza luce.</li>
<li>Rispetta i <strong>tempi</strong> della scheda per ogni prodotto (base, colore, costruttore, top).</li>
<li>Se la cliente sente calore, usa il flash cure o la modalità a bassa intensità, poi completa i tempi.</li>
<li>Pulisci e disinfetta l'interno e la base a fine servizio; i residui di gel sui LED riducono la luce.</li>
<li>Annota la data di acquisto; per le UV cambia i tubi come indica il produttore.</li>
</ol>
<div class="box pro"><strong class="t">Consiglio da professionista: un controllo veloce della lampada</strong> <ul><li><strong>Fondo e LED</strong>: una goccia di gel polimerizzato sopra un LED fa ombra. Controlla con la lampada spenta e pulisci come indica il produttore.</li> <li><strong>Posizione</strong>: le dita ai bordi e il pollice di lato ricevono meno luce. Se i sollevamenti o le grinze compaiono sempre sulle stesse dita (spesso pollici e mignoli), il problema può essere la posizione in lampada.</li> <li><strong>Prova su tip</strong>: stendi il tuo gel sul tip, polimerizza con i tempi della scheda, pulisci con il cleaner. Se resta appiccicoso o si graffia con l'unghia, la lampada non basta per quel prodotto.</li></ul> <p>Annota la data della prova: ripetila quando cambi gel, lampada o se i risultati peggiorano.</p></div>
<h2>La pelle della cliente e la luce</h2>
${F('lampada-protezione.svg', 'Protezione facoltativa: crema solare ad ampio spettro sul dorso o guanti senza dita.')}
<p>Uno studio di laboratorio del 2023 ha mostrato danni a cellule esposte a lungo alla luce di lampade per unghie, ma gli stessi autori dicono che non dimostra un aumento del rischio di tumore nelle persone; i dermatologi considerano il rischio <strong>basso</strong>. A chi lo desidera (o fa servizi molto frequenti) si può proporre una <strong>crema solare</strong> sul dorso delle mani o <strong>guanti senza dita</strong> anti-UV.</p>
<div class="box case"><strong class="t">Caso pratico</strong> <p>"Ho letto che la lampada fa venire il cancro." Come rispondi senza minimizzare né allarmare? Spiega che uno studio di laboratorio del 2023 ha visto danni su cellule esposte a lungo, ma che non ha dimostrato un aumento di tumori nelle persone e che i dermatologi considerano il rischio basso. Poi offri qualcosa di concreto: crema solare ad ampio spettro sul dorso 15–20 minuti prima, oppure guanti senza dita anti-UV, e tempi di lampada giusti (né più lunghi né più brevi).</p> <p>Una cliente informata e rispettata si fida di più. Se prende farmaci che rendono sensibili alla luce, suggeriscile di parlarne con il medico.</p></div>
<h2>Errori frequenti</h2>
<ul>
<li>Scegliere la lampada per i watt o il prezzo.</li>
<li>Polimerizzare il pollice insieme alle altre dita, di lato.</li>
<li>Accorciare i tempi perché "il gel è già duro".</li>
<li>Non pulire mai l'interno della lampada.</li>
</ul>
        `,
          sources: [
            'https://pronails.com/naily-news/tech-talk-n28-what-determines-lamp-and-product-compatibility',
            'https://nailknowledge.org/blog/uv-free-nail-lamps',
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/light-cured-gels-dip-systems',
            'https://scratchmagazine.co.uk/feature/heat-spikes-in-gel-nail-services-why-they-happen-how-to-avoid-them',
            'https://www.mdanderson.org/cancerwise/2025/09/is-your-gel-manicure-safe.html',
            'https://mdedge.com/content/study-highlights-potential-skin-cancer-risk-uv-nail-polish-dryers'
          , 'https://nailknowledge.org/blog/uv-curing-why-thin-layers-matter-for-perfect-nails', 'https://nailknowledge.org/blog/the-inhibition-layer']
        },
        {
          id: 'etichette',
          title: 'Leggere etichetta, scheda tecnica e SDS',
          min: 8,
          simple: "Ogni prodotto ha tre \"carte d'identità\": l'etichetta (cosa contiene e avvertenze), la scheda tecnica (come si usa) e la scheda di sicurezza (rischi e protezioni). Leggerle ti evita errori, allergie e prodotti vietati.",
          html: `
<p>Saper leggere i documenti dei prodotti è una competenza professionale: ti serve per lavorare bene, per la sicurezza tua e della cliente e per i controlli.</p>
${F('tre-documenti.svg', 'Etichetta, scheda tecnica e scheda di sicurezza: a cosa serve ciascuna.')}
<h2>I tre documenti</h2>
<table>
<tr><th>Documento</th><th>Cosa trovi</th><th>Quando lo usi</th></tr>
<tr><td><strong>Etichetta</strong> (obbligatoria, in italiano)</td><td>Nome, responsabile UE, quantità, lotto, scadenza o PAO, avvertenze (es. "Solo per uso professionale"), elenco ingredienti <strong>INCI</strong>.</td><td>Prima di comprare e prima di usare.</td></tr>
<tr><td><strong>Scheda tecnica</strong> (del produttore)</td><td>Sistema di appartenenza, lampada e tempi di polimerizzazione, spessori, ordine dei prodotti, rimozione.</td><td>Quando impari un prodotto o cambi lampada.</td></tr>
<tr><td><strong>Scheda di sicurezza (SDS)</strong></td><td>16 sezioni: pericoli, primo soccorso, incendio, manipolazione e stoccaggio, DPI, smaltimento.</td><td>Per DPI, conservazione, incidenti e smaltimento; da tenere a disposizione dei controlli.</td></tr>
</table>
<h2>L'INCI in pratica</h2>
<ul>
<li>Gli ingredienti sono elencati con nomi internazionali (INCI), in ordine decrescente di quantità (sotto l'1% in ordine libero).</li>
<li>Nomi da riconoscere: <strong>HEMA</strong>, <strong>Di-HEMA Trimethylhexyl Dicarbamate</strong> (ammessi solo per uso professionale), <strong>Trimethylbenzoyl Diphenylphosphine Oxide</strong> (TPO, vietato), <strong>Dimethyltolylamine</strong> (DMTA, vietata), <strong>Ethyl Methacrylate</strong> (EMA, monomero dell'acrilico).</li>
</ul>
${F('sds-sezioni.svg', 'Le cinque sezioni della SDS più utili in salone: 2, 4, 7, 8 e 13.')}
<div class="box case"><strong class="t">Caso pratico</strong> <p>Su un builder gel leggi: <em>Di-HEMA Trimethylhexyl Dicarbamate, Hydroxypropyl Methacrylate, HEMA, Ethyl Trimethylbenzoyl Phenylphosphinate, Silica...</em>. Come lo interpreti?</p> <ul><li>I primi ingredienti sono i "mattoni" (oligomeri e monomeri): c'è HEMA, quindi in etichetta devono esserci «Solo per uso professionale» e «Può provocare una reazione allergica».</li> <li><em>Ethyl Trimethylbenzoyl Phenylphosphinate</em> è il TPO-L, un fotoiniziatore ammesso e diverso dal TPO vietato. Non confonderli: il nome del TPO vietato è <em>Trimethylbenzoyl Diphenylphosphine Oxide</em>.</li> <li>Non c'è <em>Dimethyltolylamine</em> (DMTA).</li></ul> <p>Conclusione: prodotto utilizzabile, se le avvertenze sono presenti in italiano. Conserva la scheda tecnica per i tempi di lampada, che con il TPO-L possono essere diversi.</p></div>
<h2>Le sezioni SDS che userai di più</h2>
<ol class="steps">
<li><strong>Sezione 2</strong> – Pericoli: pittogrammi e frasi (es. "Può provocare una reazione allergica cutanea", "Liquido e vapori facilmente infiammabili").</li>
<li><strong>Sezione 4</strong> – Primo soccorso: cosa fare per contatto con occhi o pelle.</li>
<li><strong>Sezione 7</strong> – Manipolazione e immagazzinamento: dove e come conservare.</li>
<li><strong>Sezione 8</strong> – Protezione individuale: quali guanti, occhiali, mascherina.</li>
<li><strong>Sezione 13</strong> – Smaltimento.</li>
</ol>
<div class="box pro"><strong class="t">Consiglio da professionista: le frasi H da riconoscere al volo</strong> <table><tr><th>Codice</th><th>Significato</th><th>Cosa fai</th></tr> <tr><td>H225</td><td>Liquido e vapori facilmente infiammabili</td><td>Lontano da fonti di calore, flacone chiuso.</td></tr> <tr><td>H317</td><td>Può provocare una reazione allergica cutanea</td><td>Mai sulla pelle, guanti, salvietta pulita per dito.</td></tr> <tr><td>H319</td><td>Provoca grave irritazione oculare</td><td>Occhiali.</td></tr> <tr><td>H335</td><td>Può irritare le vie respiratorie</td><td>Aspirazione e ventilazione.</td></tr> <tr><td>H314</td><td>Provoca gravi ustioni cutanee e lesioni oculari</td><td>Tipico di alcuni primer acidi: massima attenzione.</td></tr></table> <p>Nella sezione 9 trovi anche il punto di infiammabilità: più è basso, più il prodotto è pericoloso vicino al calore.</p></div>
<h2>Compatibilità: controlla prima di comprare</h2>
<ul>
<li>La base, il costruttore e il top sono dello <strong>stesso sistema</strong>?</li>
<li>La lampada emette le lunghezze d'onda indicate nella scheda tecnica?</li>
<li>L'etichetta è in italiano e riporta un responsabile nell'UE?</li>
<li>Il fornitore ti dà scheda tecnica e SDS?</li>
</ul>
<h2>Errori frequenti</h2>
<ul>
<li>Comprare prodotti online senza INCI né responsabile UE.</li>
<li>Tenere le SDS "da qualche parte": vanno raccolte e consultabili.</li>
<li>Ignorare il PAO e usare un gel aperto da anni.</li>
</ul>
${B('tip', 'Un raccoglitore per tutto', 'Tieni una cartella (anche digitale) con scheda tecnica e SDS di ogni prodotto in uso, aggiornata quando cambi fornitore.')}
        `,
          sources: [
            'https://certifico.com/component/attachments/download/26525',
            'https://suap.regione.fvg.it/portale/export/sites/SUAP/allegati/archivio_file/LINEE-GUIDA-ESTETICA.pdf',
            'https://www.legislation.gov.uk/eur/2020/1682/data.xht',
            'https://coslaw.eu/omnibus-act-vii-new-substances-officially-banned-in-the-eu-from-september-2025/',
            'https://cosingchecker.com/ingredients/55929-dimethyltolylamine/'
          , 'https://www.parchem.com/siteimages/Attachment/GHS%20Ethyl%20Methacrylate%20MSDS.pdf', 'https://eur-lex.europa.eu/eli/reg/2025/877/oj', 'https://eur-lex.europa.eu/eli/reg/2020/1682/oj/eng']
        },
        {
          id: 'dip-press',
          title: 'Dip powder e press-on',
          min: 7,
          simple: "Il dip è una polvere colorata che si fissa con una resina e un attivatore, senza lampada. Le press-on sono unghie già pronte da incollare. Sono veloci, ma hanno regole d'igiene e di sicurezza precise.",
          html: `
<h2>Dip powder (polvere a immersione)</h2>
<p>È un sistema senza lampada, composto da tre o quattro prodotti:</p>
<ul>
<li><strong>Base</strong>: resina cianoacrilica a presa rapida.</li>
<li><strong>Polvere</strong>: perline fini di PMMA con pigmenti e iniziatore.</li>
<li><strong>Attivatore</strong>: liquido che fa indurire gli strati.</li>
<li><strong>Top</strong>: resina che reagisce con l'attivatore e dà lucentezza.</li>
</ul>
${F('dip-versare.svg', 'Igiene del dip: polvere versata con un cucchiaino sopra un contenitore monouso (✓), mai il dito nel barattolo comune (✗).')}
${B('danger', 'Mai il dito nel barattolo', 'Immergere le dita di clienti diverse nello stesso barattolo porta pelle, germi e spore nella polvere, che non si può disinfettare. Versa la polvere con un cucchiaino pulito sopra un contenitore monouso, oppure preleva una dose per cliente in una ciotolina usa e getta, e butta ciò che avanza.')}
<h3>I passi</h3>
<ol class="steps">
<li>Preparazione, opacizzazione leggera, disidratante.</li>
<li>Base sui tre quarti dell'unghia, lontano dalla cuticola; versa la polvere, togli l'eccesso.</li>
<li>Secondo strato di base più vicino alla cuticola (margine sottile) e polvere; terzo strato se serve.</li>
<li>Attivatore; attendi il tempo indicato dal produttore (un manuale indica 2–3 minuti).</li>
<li>Lima e leviga; seconda passata di attivatore se il sistema la prevede; asciuga.</li>
<li>Top in due strati sottili.</li>
</ol>
${B('warn', 'Controlla l\'attivatore', 'Molti attivatori dip contenevano DMTA (N,N-dimetil-p-toluidina), vietata nell\'UE dal 1° settembre 2025. Verifica l\'INCI dei prodotti che hai.')}
<div class="box deep"><strong class="t">Approfondimento: perché il dip indurisce senza lampada</strong> <p>La base del dip è un <strong>cianoacrilato</strong>, la stessa famiglia della colla per tip. Da solo indurisce con le tracce di umidità, ma lentamente e in modo non uniforme sotto la polvere. L'attivatore fa partire la reazione in tutto lo spessore, legando base e polvere in un unico strato duro.</p> <ul><li>La reazione scalda: troppo attivatore o strati molto spessi possono dare calore e rendere il risultato fragile.</li> <li>Se lo strato è rimasto morbido o gommoso dopo il tempo indicato, l'attivatore non è arrivato ovunque: non coprire con il top, ripassa l'attivatore.</li> <li>Ogni goccia di base su cuticola o pieghe diventa un bordo rialzato e un punto di irritazione.</li></ul></div>
<h2>Press-on (unghie preformate)</h2>
${F('press-on-step.svg', 'Press-on: misura, prepara, incolla, premi, rifinisci.')}
<ol class="steps">
<li>Scegli le misure da solco a solco per tutte le dita.</li>
<li>Prepara l'unghia: cuticola, opacizzazione leggera, sgrassatura.</li>
<li>Applica colla o linguetta adesiva; appoggia partendo dalla cuticola (senza toccarla) e premi bene per il tempo indicato dal produttore.</li>
<li>Rifinisci la lunghezza e la forma; spiega alla cliente come toglierle (acqua tiepida e olio o acetone, secondo il tipo), senza strappare.</li>
</ol>
<div class="box pro"><strong class="t">Consiglio da professionista: colla o linguette?</strong> <ul><li><strong>Linguette adesive</strong>: durano pochi giorni, si tolgono facilmente. Adatte a eventi e a chi vuole provare.</li> <li><strong>Colla</strong> (cianoacrilato): dura di più, ma va tolta con pazienza. I cianoacrilati resistono poco al caldo-umido: acqua tiepida, olio e pazienza ammorbidiscono il legame. Se la colla è molta, si usa acetone come per un tip.</li></ul> <p>Spiega alla cliente che strappare la press-on porta via strati di lamina e lascia macchie bianche ruvide. Consegnale una piccola istruzione scritta per la rimozione: è il modo migliore per evitare che torni con le unghie rovinate.</p></div>
<h2>Errori frequenti</h2>
<ul>
<li>Riutilizzare la polvere dip avanzata di un'altra cliente.</li>
<li>Base dip sulla pelle: la resina cianoacrilica incolla e irrita.</li>
<li>Strappare le press-on: si portano via strati di lamina.</li>
</ul>
        `,
          sources: [
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/light-cured-gels-dip-systems',
            'https://coslaw.eu/omnibus-act-vii-new-substances-officially-banned-in-the-eu-from-september-2025/',
            'https://publications.iarc.fr/_publications/media/download/5405/6e7ede0da351f42c09efa74e0950a97cf889dfc3.pdf'
          , 'https://dm.henkel-dam.com/is/content/henkel/Medical-Best-Practices-Flyer', 'https://patents.google.com/patent/US6602970']
        }
      ]
    },
    /* ------------------------------------------------------------------ 4 */
    {
      id: 'attrezzatura', n: 4, level: 'base', title: 'Attrezzatura',
      summary: [
  "Grana bassa = più abrasiva. Sulla lamina naturale 180–240 o più fine (le fonti divergono: nel dubbio 240). Lime in carta e buffer sono monouso.",
  "Carburo e ceramica solo sul prodotto; diamantate su unghia naturale e zona cuticolare (pelle morta).",
  "Fresa: velocità bassa vicino alla pelle (indicativamente 2.000–10.000 RPM), punta parallela e sempre in movimento, mai la velocità massima.",
  "Pennelli: piatto/ovale sintetico per gel, tondo 8–12 per acrilico (si pulisce nel monomero), liner e dotter per i dettagli.",
  "Postazione: aspiratore, buona luce, sedia regolabile e avambracci appoggiati."
],
desc: 'Lime e grane, fresa e punte, pennelli e strumenti manuali, kit e postazione.',
      lessons: [
        {
          id: 'lime',
          title: 'Lime e grane',
          min: 9,
          simple: "Il numero sulla lima dice quanto \"gratta\": numero basso = grana grossa che toglie tanto, numero alto = grana fine che leviga. Sull'unghia naturale si usano solo grane fini.",
          html: `
${F('lime-grane.svg', 'Più il numero è basso, più la lima è abrasiva.')}
<h2>Cosa vuol dire "grana"</h2>
<p>Il numero di grana viene dal modo in cui si selezionano i granelli abrasivi con setacci sempre più fitti: <strong>numero più alto = granelli più piccoli</strong> = lima più fine. Molte lime hanno due numeri (es. <strong>100/180</strong>): una grana per lato.</p>
<div class="box deep"><strong class="t">Approfondimento: lo stesso numero non è sempre la stessa grana</strong> <p>Per la carta abrasiva esistono due scale principali: quella americana (CAMI, numero senza lettera) e quella europea (FEPA, con la <strong>P</strong> davanti, es. P180). Fino a circa 220 i numeri quasi coincidono; per le grane fini divergono molto (una 600 americana corrisponde circa a una P1000–P1200 europea). La FEPA ha anche tolleranze più strette: i granelli sono più uniformi.</p> <p>Le lime per unghie spesso non dicono quale scala usano, e ogni produttore ha la sua. Conseguenza pratica: una "180" di una marca può graffiare come la "150" di un'altra. Quando cambi marca, prova la lima su un tip prima di usarla su una cliente.</p></div>
<h2>Quale grana per cosa</h2>
<table>
<tr><th>Grana</th><th>Abrasività</th><th>Uso</th><th>Mai su</th></tr>
<tr><td>80–100</td><td>Molto grossa</td><td>Accorciare e togliere molto prodotto artificiale (rimozione, refill).</td><td>Unghia naturale, pelle.</td></tr>
<tr><td>100/150</td><td>Grossa-media</td><td>Riequilibrare e accorciare ricostruzioni spesse.</td><td>Unghia naturale.</td></tr>
<tr><td>180</td><td>Media</td><td>Dare forma al prodotto, fondere il tip, togliere i sollevamenti. Alcune fonti la indicano anche per opacizzare l'unghia naturale.</td><td>Pelle.</td></tr>
<tr><td>240</td><td>Fine</td><td>Opacizzare e dare forma all'unghia naturale; rifinire.</td><td>—</td></tr>
<tr><td>Buffer (circa 180–900, varia tra marchi)</td><td>Fine (morbido)</td><td>Levigare superfici e togliere i segni della lima.</td><td>—</td></tr>
<tr><td>Lucidante (circa 900 e oltre, fino a diverse migliaia)</td><td>Finissima</td><td>Lucidare l'unghia naturale o il prodotto senza top.</td><td>Prima di applicare prodotto (la superficie lucida non aderisce).</td></tr>
</table>
${B('info', 'Le fonti non sono d\'accordo su 180 o 240', 'Per opacizzare l\'unghia naturale alcuni manuali indicano 180–240, altri "mai più grossa di 240". Per chi inizia la scelta più sicura è <strong>240</strong>, con pressione leggera: l\'obiettivo è solo togliere la lucentezza.')}
<h2>Forme e anime delle lime</h2>
${F('lime-forme-anime.svg', 'Dritta, banana, mezzaluna, ovale, buffer: forma e anima della lima.')}
<ul>
<li><strong>Dritta</strong>: per lati e bordo libero; aiuta a fare lati paralleli.</li>
<li><strong>Banana / mezzaluna</strong>: curve, seguono la zona cuticolare e affaticano meno il polso.</li>
<li><strong>Ovale</strong>: larga, copre più superficie.</li>
<li><strong>Anima rigida</strong> (legno, plastica): trasmette più forza; indicata per le grane basse e per dare forma.</li>
<li><strong>Anima morbida</strong> (spugna): segue la curva dell'unghia; ideale per buffer e rifinitura.</li>
</ul>
<h2>Igiene: monouso o disinfettabile?</h2>
${F('lime-igiene.svg', 'Lima porosa = monouso; vetro e metallo = si puliscono e si disinfettano.')}
<table>
<tr><th>Tipo</th><th>Cosa fai</th><th>Perché</th></tr>
<tr><td>Lima in carta, buffer in spugna, blocchetto</td><td><strong>Monouso</strong>: si butta o si regala alla cliente.</td><td>Sono porose: non si possono disinfettare davvero, anche se c'è scritto "lavabile".</td></tr>
<tr><td>Lima in vetro o metallo</td><td>Pulizia (spazzolino, acqua e detergente) + disinfezione.</td><td>Non porose; ma se toccano sangue vanno trattate come strumenti da sterilizzare (metallo) o eliminate.</td></tr>
<tr><td>Lima con supporto e ricambi adesivi</td><td>Ricambio monouso, supporto metallico pulito e disinfettato.</td><td>Unisce risparmio e igiene.</td></tr>
</table>
<div class="box case"><strong class="t">Caso pratico</strong> <p>Una cliente porta la sua lima "personale" e chiede di usarla. Puoi? Se è una lima porosa usata a casa, non sai che cosa ha toccato e non puoi disinfettarla: non è adatta al servizio professionale. Proponi una soluzione: usi una lima nuova e alla fine gliela regali. Così ha la sua lima personale e tu rispetti le regole.</p> <p>Se è una lima in vetro o metallo, puoi pulirla e disinfettarla prima dell'uso come uno strumento del salone. Spiega con gentilezza il perché: la cliente capirà che l'igiene è anche a sua tutela.</p></div>
<h2>Usare la lima: le basi</h2>
<ol class="steps">
<li>Scegli la grana in base al <strong>materiale</strong>: grossa sul prodotto, fine sull'unghia naturale.</li>
<li>Tieni la lima con leggerezza, senza stringere: la lima lavora, tu guidi.</li>
<li>Sull'unghia naturale lima <strong>in una sola direzione</strong>, dai lati verso il centro; niente movimento a "sega" (scalda e sfibra gli strati).</li>
<li>Controlla spesso da più punti di vista (dettagli nel modulo 8).</li>
<li>Togli la polvere con un pennello pulito sopra l'aspiratore, non soffiando.</li>
<li>Cambia lima quando devi premere per farla lavorare: una lima consumata scalda e rovina.</li>
</ol>
<div class="box deep"><strong class="t">Approfondimento: perché il movimento a "sega" fa male</strong> <p>Ogni passata produce calore per attrito. Con passate corte, veloci e premute nello stesso punto il calore si accumula: il letto ungueale sente bruciore e, a lungo andare, si irrita e diventa più sensibile anche al calore della lampada. Le formatrici parlano di "bruciatura da attrito".</p> <ul><li>Passate lunghe, in una direzione, spostando la lima.</li> <li>Se la cliente ritira il dito, fermati: hai già scaldato troppo.</li> <li>Una lima nuova lavora con meno pressione, quindi scalda meno di una consumata.</li></ul></div>
<h2>Errori frequenti</h2>
<ul>
<li>Opacizzare con la 100/180 "per fare prima": si assottiglia la lamina.</li>
<li>Usare la stessa lima su più clienti.</li>
<li>Limare il prodotto appena applicato con grane troppo basse: si scheggia o si scalda.</li>
<li>Lucidare la lamina prima del gel: il prodotto non aderisce.</li>
</ul>
${B('danger', 'Mai grane grosse sulla lamina naturale', 'L\'unghia naturale va solo opacizzata, non assottigliata: la lamina è spessa meno di mezzo millimetro.')}
        `,
          sources: [
            'https://www.my-personaltrainer.it/bellezza/limare-le-unghie-c-e-un-modo-giusto-per-farlo.html',
            'https://blog.insightcosmetics.com/en/the-ultimate-nail-file-guide',
            'https://purespadirect.com/blogs/pure-spa-direct-blog/what-are-the-different-grits-of-nail-files-for',
            'https://www.barbercosmo.ca.gov/forms_pubs/publications/disinfect_nailfiles.pdf',
            'https://www.seriousgrit.com/blogs/sandpaper-post/what-do-the-numbers-mean-in-sandpaper-how-is-grain-size-measured'
          , 'https://www.finewoodworking.com/2005/03/01/true-grit', 'https://www.metallographic.com/tools/grit-size-converter', 'https://nailknowledge.org/blog/heat-spikes']
        },
        {
          id: 'fresa',
          title: 'Fresa elettrica e punte',
          min: 14,
          simple: "La fresa è un trapanino per unghie: velocità bassa vicino alla pelle, punta sempre parallela all'unghia e sempre in movimento, pressione leggerissima. Si impara prima su tip e mano finta.",
          html: `
<p>La fresa (o "e-file") fa risparmiare tempo e fatica, ma è lo strumento che, usato male, fa più danni: solchi sulla lamina, bruciature da attrito, tagli alla pelle. Si impara per gradi.</p>
${F('fresa-anatomia.svg', 'Le parti della fresa: centralina, manipolo, mandrino, punta con gambo da 2,35 mm.')}
<h2>Com'è fatta</h2>
<ul>
<li><strong>Centralina</strong>: regola la velocità (RPM, giri al minuto) e il senso di rotazione (avanti/indietro).</li>
<li><strong>Manipolo</strong>: il "manico" con il motore e il mandrino che stringe la punta.</li>
<li><strong>Coppia (torque)</strong>: la "forza" del motore. Una buona fresa mantiene la velocità quando appoggi la punta; una fresa da hobby rallenta e ti spinge a premere o ad alzare troppo i giri.</li>
<li><strong>Gambo standard</strong>: le punte professionali hanno gambo da <strong>3/32 di pollice (2,35 mm)</strong>. Gli attrezzi per bricolage (gambo 1/8") non vanno usati sulle clienti.</li>
<li><strong>Concentricità</strong>: la punta deve girare "dritta". Una punta caduta o storta vibra, scava e va buttata.</li>
</ul>
<h2>I materiali delle punte</h2>
${F('punte-fresa.svg', 'Forme delle punte, codici colore e velocità indicative.')}
<table>
<tr><th>Materiale</th><th>Come lavora</th><th>Dove si usa</th><th>Dove NO</th></tr>
<tr><td><strong>Carburo</strong> (metallo con scanalature)</td><td>"Taglia" il prodotto, scalda meno; tagli dritti, incrociati (meno vibrazioni e polvere) o a spirale.</td><td>Solo prodotto artificiale: accorciare, riequilibrare, rimuovere.</td><td>Unghia naturale, pelle.</td></tr>
<tr><td><strong>Ceramica</strong></td><td>Scanalature, meno calore da attrito.</td><td>Prodotto: superfici e refill.</td><td>Unghia naturale, pelle.</td></tr>
<tr><td><strong>Diamantata</strong></td><td>Polvere di diamante: "leviga".</td><td>Zona cuticolare (pelle morta), pieghe, unghia naturale con grana fine.</td><td>Rimozione di molto prodotto (lenta, scalda).</td></tr>
<tr><td><strong>Bande abrasive</strong> (carta su mandrino in gomma)</td><td>Come una lima.</td><td>Superfici, opacizzazione a bassa velocità.</td><td>Mai riusate: sono <strong>monouso</strong>.</td></tr>
</table>
<h2>Codici colore (indicativi)</h2>
<p>Variano tra i marchi: controlla sempre la tabella del produttore. Lo schema più comune: <strong>giallo</strong> extra-fine, <strong>rosso</strong> fine, <strong>blu</strong> media, <strong>verde</strong> grossa, <strong>nero</strong> extra-grossa. Per il carburo la grana si capisce anche dalle scanalature: larghe e profonde = grossa, strette e basse = fine.</p>
<h2>Le forme e a cosa servono</h2>
${F('punte-forme.svg', 'Cilindro, cilindro di sicurezza, cono, fiamma, pallina, ago: dove si usa ciascuna.')}
<table>
<tr><th>Forma</th><th>Uso</th></tr>
<tr><td><strong>Cilindro (barrel)</strong></td><td>Superficie del prodotto, accorciare. Lontano dalla zona cuticolare.</td></tr>
<tr><td><strong>Cilindro di sicurezza</strong> (punta arrotondata o liscia)</td><td>Superficie vicino alle pieghe senza tagliare la pelle.</td></tr>
<tr><td><strong>Cono</strong></td><td>Sotto il bordo libero, smile line, angoli.</td></tr>
<tr><td><strong>Fiamma</strong></td><td>Sollevare la cuticola morta, pieghe laterali.</td></tr>
<tr><td><strong>Pallina</strong></td><td>Pulire la pelle morta della zona cuticolare (solo pelle secca e morta).</td></tr>
<tr><td><strong>Ago / cono rovesciato</strong></td><td>Dettagli, sotto il bordo libero.</td></tr>
</table>
<h2>Velocità indicative</h2>
${F('fresa-rpm-scala.svg', 'Scala delle velocità: più vicino alla pelle, più lento.')}
<table>
<tr><th>Lavoro</th><th>Velocità indicativa</th></tr>
<tr><td>Zona cuticolare e unghia naturale (diamantate, bande)</td><td>circa <strong>2.000–10.000 RPM</strong></td></tr>
<tr><td>Levigare la superficie del prodotto</td><td>circa 8.000–15.000 RPM</td></tr>
<tr><td>Dare forma, riequilibrare (refill)</td><td>circa 10.000–20.000 RPM</td></tr>
<tr><td>Accorciare e togliere molto prodotto (operatrice esperta)</td><td>circa 15.000–25.000 RPM</td></tr>
<tr><td>Velocità massima (25.000–35.000)</td><td><strong>Mai durante il servizio</strong></td></tr>
</table>
${B('info', 'Perché tanti numeri diversi', 'Le fonti divergono molto: per la zona cuticolare si va da 2.000–5.000 RPM (manuali d\'esame USA) a 5.000–12.000 (alcune accademie); per la rimozione da 12.000–15.000 fino a 20.000–30.000. Dipende da punta, fresa ed esperienza. <strong>Per chi inizia</strong>: parti dal valore più basso e alza a piccoli passi solo se la punta "salta" o non scorre.')}
<div class="box pro"><strong class="t">Consiglio da professionista: impara con il manipolo, non con i giri</strong> <ul><li>Allenati su tip incollati a una ruota di tip: lavora a 5.000–8.000 RPM finché il movimento è fluido e la punta resta parallela. Solo dopo aumenta.</li> <li>Ascolta il motore: se cala di giri quando appoggi la punta, stai premendo troppo o la fresa non ha coppia sufficiente.</li> <li>Impara il <strong>senso di rotazione</strong>: in avanti la punta "tira" verso un lato, all'indietro verso l'altro. Chi è mancina spesso lavora al contrario: segui il verso di taglio indicato sulla punta.</li> <li>Prima di usare la fresa sulla zona cuticolare di una cliente, fai pratica su pelle sintetica o con una formatrice.</li></ul></div>
<h2>Tecnica sicura in 8 passi</h2>
${F('fresa-angolo.svg', 'Punta parallela alla lamina (✓); punta inclinata che scava "anelli di fuoco" (✗).')}
<ol class="steps">
<li>Indossa occhiali e mascherina, accendi l'aspiratore.</li>
<li>Controlla che la punta sia pulita, integra e ben inserita fino in fondo.</li>
<li>Imposta il senso di rotazione: in avanti per lavorare in un verso, all'indietro per l'altro lato (le punte in carburo hanno un verso di taglio: segui le istruzioni).</li>
<li>Appoggia il mignolo sulla mano della cliente (<strong>punto d'appoggio</strong>) per stabilità.</li>
<li>Avvia la fresa <strong>prima</strong> di toccare l'unghia; parti da velocità bassa.</li>
<li>Tieni la punta <strong>parallela</strong> alla superficie: se inclini il bordo o la punta scavi solchi circolari ("anelli di fuoco").</li>
<li>Pressione leggerissima e <strong>movimento continuo</strong>: fermarsi in un punto scalda e scava. Se la cliente sente calore, solleva subito.</li>
<li>Controlla spesso al tatto e alla vista; finisci con lima o buffer dove serve.</li>
</ol>
<div class="box deep"><strong class="t">Approfondimento: gli "anelli di fuoco"</strong> <p>Sono solchi curvi sulla lamina naturale, lasciati dal bordo della punta inclinata. La causa principale è l'eccesso di limatura: troppa pressione, punta inclinata, troppi passaggi sullo stesso punto. Anche le punte scadenti costringono a premere di più. La velocità conta in tutti e due i sensi: troppo lenta la punta "trascina" e spinge a premere; troppo veloce si perde il controllo.</p> <p>Che cosa fare se li trovi:</p> <ul><li><strong>Solco leggero</strong>: si può applicare il prodotto, tenendo all'inizio la mano un po' fuori dalla lampada per evitare il picco di calore, poi completare.</li> <li><strong>Solco profondo</strong>: niente prodotto su quell'unghia; si lascia ricrescere.</li></ul></div>
<h2>Pulizia delle punte</h2>
<ol class="steps">
<li>Togli polvere e residui con lo spazzolino in ottone (le scanalature intasate scaldano).</li>
<li>Lava con acqua e detergente (anche in vasca a ultrasuoni).</li>
<li>Disinfetta; poi le punte metalliche che possono toccare pelle lesa o sangue vanno in busta e in autoclave.</li>
<li>Conserva in un contenitore chiuso e pulito. Le bande abrasive si buttano.</li>
</ol>
${B('warn', 'Sicurezza', 'Pressione leggera e punta sempre in movimento: fermarsi in un punto crea calore da attrito e solchi. La manicure a secco ("russa") con fresa è una tecnica avanzata che richiede formazione specifica. Non usare la fresa su pelle viva: si lavora solo sulla pelle morta.')}
<h2>Errori frequenti</h2>
<ul>
<li>Alzare la velocità per compensare una punta consumata o una fresa debole.</li>
<li>Usare il carburo sulla lamina naturale.</li>
<li>Premere la punta contro la piega prossimale.</li>
<li>Continuare a usare una punta che vibra.</li>
<li>Usare un trapanino da bricolage.</li>
</ul>
        `,
          sources: [
            'https://www.katiebarnesacademy.com/blogs/e-filing/e-file-bit-grit-guide',
            'https://www.katiebarnesacademy.com/blogs/e-filing/a-guide-to-choosing-the-right-speed-for-every-nail-technique',
            'https://purespadirect.com/blogs/pure-spa-direct-blog/e-file-bit-guide-for-nail-techs-shapes-grits-and-safe-use-for-speed-cuticle-care-your-cuticles-will-thank-you',
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/electric-filing-safety',
            'https://open-exam-prep.com/study-guides/or-nail-technician/advanced-artificial-nail-systems/electric-filing-safety-techniques',
            'https://suap.regione.fvg.it/portale/export/sites/SUAP/allegati/archivio_file/LINEE-GUIDA-ESTETICA.pdf'
          , 'https://nailknowledge.org/blog/how-to-prevent-rings-of-fire-on-the-nail-plate']
        },
        {
          id: 'kit',
          title: 'Kit di partenza',
          min: 9,
          simple: "Per iniziare servono poche cose ma buone: un sistema completo di una sola marca con la sua lampada, lime giuste, strumenti sterilizzabili, aspiratore e DPI. Il resto si compra man mano.",
          html: `
<p>Il mercato offre migliaia di prodotti. Un kit ben scelto ti fa imparare più in fretta e lavorare in sicurezza. Regola d'oro: <strong>un solo sistema completo</strong> (base, gel, top e lampada dello stesso produttore) all'inizio.</p>
${F('kit-priorita.svg', 'Cosa comprare subito, dopo qualche mese e più avanti.')}
<h2>Le priorità</h2>
<table>
<tr><th>Subito (indispensabile)</th><th>Dopo qualche mese</th><th>Più avanti</th></tr>
<tr><td>Lampada consigliata dal produttore; aspiratore da tavolo; DPI; sistema gel trifasico (base, builder trasparente e rosa, top); disidratante e primer; cleaner e acetone; lime 100/180 e 240, buffer; spingicuticole, curetta, tronchesine; bastoncini d'arancio; tip e colla; cartine; pennelli per gel; mano da allenamento e ruota di tip</td><td>Fresa professionale con poche punte (diamantata fine a pallina o fiamma, cilindro di sicurezza, carburo medio); gel cover; semipermanenti in pochi colori; pennelli per nail art e dotter</td><td>Sistema acrilico (liquido, polveri, pennello 8–12, dappen); polygel; effetti (chrome, cat-eye); stampini</td></tr>
</table>
<div class="box case"><strong class="t">Caso pratico</strong> <p>Trovi un kit "completo" con lampada "universale", 30 colori e gel a un prezzo molto basso. Conviene per iniziare? Ragiona così: la lampada non indica per quali prodotti è testata, i gel non hanno scheda tecnica, i colori non ti servono finché non sai costruire.</p> <p>Il rischio concreto è la <strong>sottopolimerizzazione</strong>: il gel sembra duro, ma resta crudo sotto, si solleva e può sensibilizzare te e le clienti. Meglio un sistema trifasico con la sua lampada e pochi colori, più aspiratore e DPI. Spendi meno in colori e più in ciò che ti fa lavorare sicura.</p></div>
<h2>Attrezzature</h2>
<ul>
<li><strong>Lampada</strong> UV/LED o dual, adatta al tuo sistema.</li>
<li><strong>Aspiratore</strong> da tavolo con filtri di ricambio.</li>
<li><strong>Fresa</strong> professionale (gambo 2,35 mm, buona coppia), con punte diamantate e in carburo.</li>
<li><strong>Autoclave di classe B</strong> o servizio esterno di sterilizzazione documentato; vasca per detersione/disinfezione; buste; registro.</li>
<li><strong>Lampada da tavolo</strong> a luce bianca diffusa e <strong>sedia regolabile</strong> (lezione "Postazione ed ergonomia").</li>
</ul>
<h2>Prodotti e consumabili</h2>
<ul>
<li>Disidratante, primer acido e senza acido, base, costruttore (trasparente, rosa, cover), sigillante, cleaner, acetone.</li>
<li>Tip di varie misure, tagliatip, colla, cartine.</li>
<li>Pennelli per gel e per acrilico (misura 8–12), pennellini per nail art, dotter.</li>
<li>Lime 100/180 e 240, buffer, bastoncini d'arancio, spazzolino per la polvere.</li>
<li>Olio per cuticole, salviette che non lasciano pelucchi, carta per il piano.</li>
<li>DPI: guanti in nitrile in più taglie, mascherine FFP2, occhiali.</li>
<li>Disinfettanti per superfici e strumenti con scheda tecnica e SDS.</li>
</ul>
${F('pennelli.svg', 'I pennelli principali e il loro uso: piatto e ovale per il gel, tondo per l\'acrilico, liner, ventaglio e dotter.')}
${F('tip-tipi.svg', 'Tip con incavo, a contatto e scala delle misure.')}
<h2>Come scegliere i prodotti</h2>
<ol class="steps">
<li>Compra da canali ufficiali: etichetta in italiano, INCI, responsabile UE.</li>
<li>Chiedi scheda tecnica e SDS prima dell'acquisto.</li>
<li>Controlla l'INCI: niente TPO, niente DMTA; HEMA con le avvertenze obbligatorie.</li>
<li>Verifica che la lampada emetta le lunghezze d'onda indicate dal gel.</li>
<li>Diffida dei kit completi "tutto a pochi euro" senza documenti.</li>
</ol>
${F('kit-postazione.svg', 'Una postazione ordinata: zona pulita, zona di lavoro, zona sporco.')}
<div class="box pro"><strong class="t">Consiglio da professionista: checklist per gli acquisti online</strong> <ul><li>Il venditore indica una <strong>persona responsabile nell'UE</strong> (nome e indirizzo)? Per i cosmetici è obbligatoria.</li> <li>Etichetta e avvertenze sono in <strong>italiano</strong>? C'è il numero di lotto?</li> <li>Puoi scaricare <strong>SDS e scheda tecnica</strong> prima di comprare?</li> <li>La scheda tecnica indica lampada e tempi, non solo "UV/LED"?</li> <li>Il prezzo è credibile? Un sistema completo a pochi euro spesso non ha documenti.</li></ul> <p>Se manca anche uno solo di questi punti, aspetta: un prodotto non conforme non lo puoi usare, e in caso di reazione allergica di una cliente non hai nulla da mostrare.</p></div>
<h2>Errori frequenti</h2>
<ul>
<li>Comprare molti colori prima di saper fare una buona struttura.</li>
<li>Mescolare gel e top di marche diverse "perché costano meno".</li>
<li>Risparmiare su aspiratore e DPI.</li>
<li>Comprare una fresa da bricolage o da pochi euro.</li>
</ul>
${B('tip', 'Consiglio d\'acquisto', 'Scegli un sistema completo di un solo produttore per iniziare: base, gel e lampada sono studiati per funzionare insieme. Molti produttori offrono corsi sul proprio sistema.')}
        `,
          sources: [
            'https://pronails.com/naily-news/tech-talk-n28-what-determines-lamp-and-product-compatibility',
            'https://www.hse.gov.uk/pubns/guidance/sr13.pdf',
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/electric-filing-safety',
            'https://suap.regione.fvg.it/portale/export/sites/SUAP/allegati/archivio_file/LINEE-GUIDA-ESTETICA.pdf'
          , 'https://eur-lex.europa.eu/eli/reg/2009/1223/oj', 'https://nailknowledge.org/blog/uv-free-nail-lamps']
        },
        {
          id: 'pennelli-strumenti',
          title: 'Pennelli e strumenti manuali',
          min: 9,
          simple: "Ogni pennello ha il suo lavoro: piatto o ovale per il gel, tondo per l'acrilico, sottile per i dettagli. Gli strumenti di metallo (spingicuticole, curetta, tronchesine) vanno usati con delicatezza e sterilizzati.",
          html: `
<h2>I pennelli</h2>
${F('pennelli.svg', 'I pennelli principali e il loro uso: piatto e ovale per il gel, tondo per l\'acrilico, liner, ventaglio e dotter.')}
<table>
<tr><th>Pennello</th><th>Forma e setole</th><th>Uso</th><th>Pulizia</th></tr>
<tr><td><strong>Gel piatto / ovale</strong></td><td>Setole sintetiche, punta piatta, quadrata o ovale.</td><td>Stendere base, builder, cover; la punta ovale aiuta lungo la cuticola.</td><td>Togli il gel con una salvietta; usa il cleaner solo se indicato dal produttore. Chiudi con il cappuccio e tienilo lontano dalla luce.</td></tr>
<tr><td><strong>Acrilico tondo</strong></td><td>Setole naturali (spesso kolinsky), pancia piena, punta sottile; misure comuni 8–12.</td><td>Raccogliere e modellare la perla.</td><td>Nel <strong>monomero</strong>; asciuga su carta e rimodella la punta. Evita acetone e acqua: seccano le setole.</td></tr>
<tr><td><strong>Liner / striper</strong></td><td>Setole lunghe e sottili.</td><td>Linee, smile line, dettagli.</td><td>Come il pennello del prodotto usato.</td></tr>
<tr><td><strong>Ventaglio</strong></td><td>Setole aperte a ventaglio.</td><td>Glitter, sfumature, polvere.</td><td>Asciutto, pulito con un panno.</td></tr>
<tr><td><strong>Dotter</strong></td><td>Bastoncino con sfera.</td><td>Puntini, decorazioni.</td><td>Pulizia e disinfezione.</td></tr>
<tr><td><strong>Pennello per polvere</strong></td><td>Morbido, largo.</td><td>Togliere la polvere di limatura sopra l'aspiratore.</td><td>Lavato e disinfettato regolarmente.</td></tr>
</table>
${F('pennelli-cura.svg', 'Cura dei pennelli: pulire, asciugare, rimodellare, chiudere.')}
${B('tip', 'Un pennello per prodotto', 'Usa pennelli diversi per gel trasparente, colori e acrilico: i residui di un prodotto possono macchiare o contaminare l\'altro.')}
<div class="box deep"><strong class="t">Approfondimento: perché ogni pennello ha il suo solvente</strong> <ul><li><strong>Kolinsky (setole naturali)</strong>: le setole sono peli con una superficie a scaglie e un po' di grasso naturale. L'acetone toglie questo grasso: le setole si aprono, si spezzano e non tengono più la punta. Il monomero, invece, scioglie l'acrilico senza seccarle.</li> <li><strong>Pennello da gel (sintetico)</strong>: il gel resta liquido finché non vede la luce. Anche la luce ambiente o quella della lampada vicina lo fanno indurire lentamente tra le setole: per questo cappuccio e distanza dalla lampada.</li> <li><strong>Residui di acrilico</strong> lasciati seccare alla base delle setole (vicino alla ghiera) aprono il pennello "a forbice". Pulisci sempre fino alla base.</li></ul></div>
<h2>Gli strumenti manuali</h2>
${F('strumenti-manuali.svg', 'Spingicuticole, curetta, tronchesine, tagliatip, pinzette, bastoncino d\'arancio.')}
<table>
<tr><th>Strumento</th><th>A cosa serve</th><th>Come usarlo</th><th>Igiene</th></tr>
<tr><td><strong>Spingicuticole</strong> (metallo, doppio)</td><td>Arretrare l'eponichio e staccare la cuticola dalla lamina.</td><td>Inclinato basso, sulla lamina, senza premere sotto la piega.</td><td>Sterilizzare.</td></tr>
<tr><td><strong>Curetta</strong></td><td>Rimuovere la cuticola aderente; pulire i solchi.</td><td>Movimenti piccoli e leggeri, sempre sulla lamina.</td><td>Sterilizzare.</td></tr>
<tr><td><strong>Tronchesine</strong></td><td>Tagliare pellicine e lembi di pelle <em>morta</em> sollevata.</td><td>Solo la punta, senza tirare; mai sull'eponichio vivo.</td><td>Sterilizzare; affilatura periodica.</td></tr>
<tr><td><strong>Tagliatip</strong></td><td>Accorciare i tip prima di limarli.</td><td>Taglio netto, dal lato verso il centro.</td><td>Pulire e disinfettare.</td></tr>
<tr><td><strong>Pinzette</strong></td><td>Strass, decorazioni, fibra.</td><td>—</td><td>Pulire e disinfettare (sterilizzare se toccano pelle lesa).</td></tr>
<tr><td><strong>Bastoncino d'arancio</strong></td><td>Spingere delicatamente la cuticola, pulire i bordi.</td><td>—</td><td><strong>Monouso</strong>.</td></tr>
<tr><td><strong>Spazzolino per unghie</strong></td><td>Pulire unghie e strumenti.</td><td>—</td><td>Lavare e disinfettare dopo ogni cliente.</td></tr>
</table>
<div class="box pro"><strong class="t">Consiglio da professionista: controlla gli strumenti come una formatrice</strong> <ul><li><strong>Tronchesine</strong>: chiudile controluce. Le lame devono toccarsi lungo tutta la punta, senza spazi. Una lama che "mastica" strappa invece di tagliare e lascia lembi che diventano nuove pellicine.</li> <li><strong>Spingicuticole</strong>: passa il polpastrello sul bordo. Deve essere liscio e senza sbavature; un bordo graffiante solca la lamina.</li> <li><strong>Ruggine o puntini scuri</strong>: lo strumento va sostituito. Le microcavità trattengono sporco che la sterilizzazione non raggiunge bene.</li></ul> <p>Fai questo controllo ogni volta che reimbusti, prima della sterilizzazione.</p></div>
<h2>Prima e dopo l'uso</h2>
<ol class="steps">
<li>Apri la busta sterile davanti alla cliente.</li>
<li>Usa ogni strumento solo per il suo scopo (la curetta non è una leva, le tronchesine non tagliano i tip).</li>
<li>Appoggia gli strumenti usati in una vaschetta "sporco", separata dal "pulito".</li>
<li>A fine servizio: percorso di pulizia, disinfezione e sterilizzazione (modulo 2).</li>
<li>Controlla periodicamente lame e punte: uno strumento rovinato graffia o strappa.</li>
</ol>
<h2>Errori frequenti</h2>
<ul>
<li>Lavare il pennello da acrilico in acetone.</li>
<li>Lasciare il pennello da gel aperto vicino alla lampada.</li>
<li>Tagliare l'eponichio con le tronchesine.</li>
<li>Usare lo spingicuticole come leva sotto la piega.</li>
</ul>
        `,
          sources: [
            'https://nsinails.com.au/pages/instruction-how-to-clean-your-brush',
            'https://tnbl.co.uk/blogs/blog/how-to-clean-acrylic-nail-brushes-a-professional-guide-for-beginners',
            'https://open-exam-prep.com/study-guides/ca-nail-technician/natural-nail-care-manicures-pedicures/implements-equipment-maintenance',
            'https://suap.regione.fvg.it/portale/export/sites/SUAP/allegati/archivio_file/LINEE-GUIDA-ESTETICA.pdf'
          ]
        },
        {
          id: 'postazione',
          title: 'Postazione ed ergonomia',
          min: 6,
          simple: "Una postazione ordinata, ben illuminata e con l'aspiratore vicino alle mani ti fa lavorare meglio e ti protegge la schiena, il collo e i polsi.",
          html: `
<p>Una ricostruzione dura anche un'ora e mezza. Ripetuta più volte al giorno, una postura sbagliata dà dolori a collo, spalle, schiena e polsi. Una postazione ben pensata migliora anche igiene e qualità del lavoro.</p>
${F('postura-tavolo.svg', 'Postura corretta (schiena dritta, avambracci appoggiati, piedi a terra) e scorretta (collo piegato, gomiti sospesi, mano lontana).')}
<h2>Postura</h2>
<ul>
<li><strong>Sedia regolabile</strong> con schienale: piedi appoggiati a terra, ginocchia circa ad angolo retto.</li>
<li><strong>Avambracci appoggiati</strong> al tavolo; spalle rilassate, non sollevate.</li>
<li>Avvicina la mano della cliente a te (cuscinetto poggiamano) invece di piegarti in avanti.</li>
<li>Schiena dritta: piega appena la testa, non tutto il busto.</li>
<li>Fai brevi pause tra una cliente e l'altra e muovi collo, spalle e polsi.</li>
</ul>
<div class="box deep"><strong class="t">Approfondimento: che cosa dicono gli studi</strong> <p>Le ricerche sulle onicotecniche concordano: il disturbo più frequente è il <strong>dolore al collo</strong>. In uno studio iraniano su 80 operatrici lo riferiva il 63,8%, seguito da dolore alla parte alta della schiena (51%) e alle spalle (41%). In un sondaggio canadese su 155 operatrici, chi lavorava più di 30 ore a settimana aveva più spesso dolore al collo. Il NIOSH statunitense ha osservato nei saloni collo e spalle piegati in avanti per molto tempo.</p> <p>Il messaggio: il problema non è un movimento sbagliato, ma la <strong>posizione mantenuta</strong> per ore. Alza la mano della cliente con un poggiamano più alto, alterna i compiti e programma micro-pause.</p></div>
<h2>Luce</h2>
<ul>
<li>Luce generale buona più una <strong>lampada da tavolo</strong> a luce bianca e diffusa, orientata per non fare ombre sulla mano.</li>
<li>Per i colori e il nude usa una luce il più possibile simile alla luce del giorno.</li>
<li>Non usare la lampada UV/LED come luce di lavoro: fa indurire i prodotti e affatica la vista.</li>
</ul>
<div class="box pro"><strong class="t">Consiglio da professionista: come scegliere la lampada da tavolo</strong> <p>La norma europea sull'illuminazione dei luoghi di lavoro (EN 12464-1), nelle tabelle riportate dai software di progettazione, indica per i trattamenti estetici circa <strong>750 lux</strong> e una resa cromatica di almeno <strong>Ra 90</strong>. La resa cromatica (indicata anche come CRI) dice quanto fedelmente la luce mostra i colori.</p> <ul><li>Cerca sulla confezione "CRI ≥ 90" o "Ra ≥ 90": con una luce a bassa resa i nude e i rosa sembrano diversi da come li vedrà la cliente fuori.</li> <li>Preferisci una luce diffusa e regolabile, posizionata dal lato opposto alla mano che lavora, per non avere ombre.</li></ul></div>
<h2>Ordine: tre zone</h2>
${F('kit-postazione.svg', 'Una postazione ordinata: zona pulita, zona di lavoro, zona sporco.')}
<ol class="steps">
<li><strong>Zona pulita</strong>: strumenti in busta sterile, lime nuove, prodotti chiusi.</li>
<li><strong>Zona di lavoro</strong>: poggiamano sopra l'aspiratore, lampada a portata di mano.</li>
<li><strong>Zona sporco</strong>: vaschetta strumenti usati, cestino con coperchio, salviette usate.</li>
</ol>
<h2>Errori frequenti</h2>
<ul>
<li>Lavorare piegata in avanti con la mano della cliente lontana.</li>
<li>Tenere flaconi aperti sparsi sul tavolo.</li>
<li>Mettere l'aspiratore di lato, lontano dalle mani.</li>
</ul>
${B('tip', 'Allenati anche alla postura', 'Quando ti alleni sulla mano finta, sistemala alla stessa altezza e distanza della mano di una cliente: così prendi subito le abitudini giuste.')}
        `,
          sources: [
            'https://www.hse.gov.uk/pubns/guidance/sr13.pdf',
            'https://suap.regione.fvg.it/portale/export/sites/SUAP/allegati/archivio_file/LINEE-GUIDA-ESTETICA.pdf',
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/electric-filing-safety'
          , 'https://doaj.org/article/0ecc380f064f466da3066f5febfd55c3', 'https://stacks.cdc.gov/view/cdc/77120/cdc_77120_DS1.pdf', 'https://dialux4.support-en.dial.de/support/solutions/articles/9000078423-task-lighting']
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
<div class="box deep"><strong class="t">Approfondimento: come si "attacca" davvero il prodotto</strong> <ul><li><strong>Aggancio meccanico</strong>: il prodotto liquido entra nei microgaffi dell'opacizzazione e, indurendo, ci resta "incastrato".</li> <li><strong>Aggancio chimico</strong>: basi e primer hanno molecole con un'estremità che si lega debolmente alla cheratina (legami a idrogeno) e un'altra che si unisce al prodotto mentre polimerizza.</li></ul> <p>Entrambi funzionano solo se il prodotto può <strong>bagnare</strong> la lamina, cioè stendersi e toccarla ovunque. Olio, sebo, crema o una pellicina fanno da pellicola che separa il prodotto dall'unghia: lì non c'è né incastro né legame. Per questo la pulizia è importante quanto l'opacizzazione.</p></div>
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
<div class="box case"><strong class="t">Caso pratico</strong> <p>Una cliente ha sempre sollevamenti sugli stessi due pollici, mai sulle altre dita. Come cerchi la causa?</p> <ol><li><strong>Preparazione</strong>: i pollici hanno solchi laterali larghi e curvi; è facile lasciare cuticola o polvere ai lati.</li> <li><strong>Lampada</strong>: il pollice polimerizzato insieme alle altre dita resta di lato e riceve meno luce.</li> <li><strong>Uso</strong>: chiedi che cosa fa con i pollici (aprire lattine, scrivere sul telefono, staccare etichette).</li> <li><strong>Struttura</strong>: il pollice è più largo e piatto; ha bisogno di un apex ben costruito.</li></ol> <p>Correggi un punto alla volta e annota sulla scheda: al refill successivo saprai quale era la causa.</p></div>
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
            'https://www.homeofnailart.com/blogs/knowledge-hub/mastering-the-art-of-nail-filing-a-comprehensive-guide-for-professional-nail-technicians', 'https://nailknowledge.org/blog/unraveling-the-mystery-of-acids-in-nail-products/', 'https://patents.google.com/patent/WO2004080231A2/en', 'https://nailknowledge.org/blog/the-inhibition-layer']
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
<div class="box case"><strong class="t">Caso pratico</strong> <p>Sotto il bordo libero di una cliente con ricostruzioni da anni la pelle sembra "attaccata" alla lamina e, se provi a pulire, fa male o sanguina. Probabilmente è un <strong>pterigio inverso</strong>: l'iponichio è cresciuto aderente alla parte inferiore della lamina. È descritto anche come reazione ai prodotti per ricostruzione.</p> <p>Che cosa fai: non spingere, non raschiare e non limare sotto il bordo libero. Tieni la lunghezza che la cliente sopporta senza dolore e consiglia il dermatologo. Le autorità che regolano la professione negli USA ricordano che pterigio e cuticola non sono la stessa cosa e che spingere il pterigio non è di competenza dell'onicotecnica: lo stesso vale per il pterigio inverso.</p></div>
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
<div class="box deep"><strong class="t">Approfondimento: perché la cuticola fa sollevare il prodotto</strong> <p>La cuticola è pelle morta che continua a <strong>sfaldarsi</strong>. Se il prodotto si appoggia su di lei, si attacca a uno strato che a sua volta è attaccato male: nei giorni successivi le scaglie si staccano e portano via il bordo del prodotto. In più la cuticola assorbe acqua e oli, che indeboliscono l'adesione intorno.</p> <p>Un trucco per vederla: dopo averla sollevata, passa un bastoncino asciutto in piano sulla lamina verso la base. Se senti un leggero "attrito" o vedi formarsi una piccola pellicina bianca, c'è ancora cuticola da togliere. Sulla lamina pulita il bastoncino scorre liscio.</p></div>
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
            'https://www.nsinails.com.au/blogs/news/nail-preparation', 'https://www.statpearls.com/point-of-care/25507']
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
<div class="box deep"><strong class="t">Approfondimento: la lamina è un isolante</strong> <p>Il letto ungueale è pieno di terminazioni nervose: la sensazione di bruciore parte quando arriva a circa <strong>46 °C</strong>. Tra il prodotto che polimerizza (e scalda) e il letto c'è solo la lamina, spessa in media meno di mezzo millimetro. Ogni centesimo di millimetro tolto riduce l'isolamento.</p> <p>Anche l'attrito conta: una limatura aggressiva irrita il letto e lo rende più sensibile al calore. La combinazione tipica è: lamina limata troppo + strato spesso + lampada potente = la cliente toglie di scatto la mano. Ripetuto nel tempo, il calore eccessivo può favorire l'onicolisi.</p></div>
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
<div class="box pro"><strong class="t">Consiglio da professionista: un metodo da contare</strong> <ul><li>Dividi l'unghia in <strong>zone</strong> (base, lato sinistro, centro, lato destro, bordo libero) e dai a ogni zona lo stesso numero di passate leggere, per esempio 3–4.</li> <li>Dopo ogni giro togli la polvere e guarda con luce radente: ripassa <strong>solo</strong> le zone ancora lucide.</li> <li>Il segnale per fermarsi è la scomparsa della lucentezza, non la quantità di polvere.</li> <li>Sui pollici e sulle unghie molto curve tieni la lima più corta (o usa un buffer stretto) per seguire la curva senza spianare il centro.</li></ul> <p>Contare le passate all'inizio sembra lento, ma ti abitua a una pressione e a un ritmo costanti.</p></div>
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
            'https://www.youngnails.com/blogs/news/how-to-use-nail-forms', 'https://nailknowledge.org/blog/heat-spikes']
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
<tr><td><strong>Come funziona</strong></td><td>Contiene acido metacrilico: si lega alla lamina e al prodotto (l'idea che "scavi" microfori è discussa: secondo Doug Schoon la lamina resta integra)</td><td>Fa da "nastro biadesivo" chimico tra lamina e prodotto, senza acido forte</td></tr>
<tr><td><strong>Aspetto da asciutto</strong></td><td>Bianco gessoso, opaco</td><td>Resta leggermente appiccicoso (dipende dal marchio)</td></tr>
<tr><td><strong>Quando si usa</strong></td><td>Acrilico tradizionale, unghie molto grasse o con sollevamenti ripetuti</td><td>Gel e uso quotidiano; spesso anche con l'acrilico moderno</td></tr>
<tr><td><strong>Rischi</strong></td><td>Corrosivo: ustioni chimiche su pelle e occhi; ripetuto assottiglia la lamina</td><td>Meno aggressivo, ma resta un prodotto con acrilati: mai sulla pelle</td></tr>
<tr><td><strong>Tempi</strong></td><td>Applica il prodotto solo quando è asciutto (bianco gessoso)</td><td>Asciuga in circa 40–60 secondi; l'effetto cala dopo circa 20 minuti</td></tr>
</table>
<div class="box deep"><strong class="t">Approfondimento: il primer acido "scava" davvero?</strong> <p>Molti testi dicono che l'acido metacrilico "incide" o "fa dei fori" nella lamina. Il chimico Doug Schoon, tra i maggiori esperti del settore, lo considera un <strong>falso mito</strong>: l'acido metacrilico è un acido organico debole e la cheratina è molto resistente. Nei suoi test, ritagli di unghia lasciati per mesi nel primer non si sono rovinati.</p> <p>Il primer funziona come un <strong>biadesivo</strong>: un'estremità della molecola si lega alla lamina (legami a idrogeno), l'altra si unisce al prodotto. Attenzione però: la lamina resiste, la pelle e gli occhi no. Per la pelle e gli occhi l'acido metacrilico è aggressivo (pH 1–2): lì causa ustioni chimiche.</p></div>
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
<div class="box deep"><strong class="t">Approfondimento: perché troppo primer riduce l'aggancio</strong> <p>Il biadesivo funziona quando è un velo sottilissimo: una faccia tocca l'unghia e l'altra il prodotto. Se ne metti troppo, si forma uno strato in mezzo che non è legato né all'una né all'altro e fa da "cuscinetto" debole. In più il liquido in eccesso scivola nei solchi laterali e sotto le pieghe, dove può causare dolore e ustioni.</p> <p>Regola di Schoon: <strong>meno è meglio</strong>. Uno strato sottile su una lamina pulita e asciutta. Se la cliente sente pizzicare ai lati subito dopo il primer, sciacqua la zona con acqua e sapone e annota l'episodio.</p></div>
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
<div class="box case"><strong class="t">Caso pratico</strong> <p>Una cliente con unghie molto lisce e "grasse" ha sollevamenti dopo una settimana, anche con una preparazione accurata e il primer senza acido. Che cosa provi?</p> <ul><li>Lava le mani della cliente con sapone non grasso all'inizio e lavora <strong>una mano alla volta</strong>: il sebo torna in fretta.</li> <li>Ripassa il disidratante subito prima del primer, non 10 minuti prima.</li> <li>Se il tuo sistema lo prevede, valuta un primer acido solo sulla lamina, in piccolissima quantità, oppure il bonder specifico del produttore.</li> <li>Controlla tempi e lampada: un sollevamento può essere anche una sotto-polimerizzazione.</li></ul> <p>Cambia una cosa per volta e annota il risultato al refill.</p></div>
`,
          sources: ['https://www.katiebarnesacademy.com/blogs/preparation/what-is-the-difference-between-acid-free-and-acid-based-nail-primer',
            'https://www.nsinails.com.au/blogs/news/nail-preparation',
            'https://open-exam-prep.com/study-guides/oh-nail-technician/artificial-nail-services/sculptured-acrylic-nails',
            'https://purespadirect.com/blogs/pure-spa-direct-blog/how-to-use-nail-primer-dehydrator-ndash-the-secret-weapons-for-flawless-long-lasting-nail-art', 'https://nailknowledge.org/blog/unraveling-the-mystery-of-acids-in-nail-products/', 'https://patents.google.com/patent/WO2004080231A2/en']
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
<div class="box pro"><strong class="t">Consiglio da professionista: la "formula" della cliente</strong> <p>Alla prima applicazione annota sulla scheda le misure di ogni dito, dal pollice al mignolo, per entrambe le mani, e la marca dei tip. Per esempio: <em>Dx 2-6-5-7-9, Sx 3-6-5-7-9 (marca X, mezzo incavo)</em>. Al servizio successivo prepari i tip in pochi secondi.</p> <p>Se cambi marca, ricomincia da capo: la stessa cifra corrisponde a larghezze diverse. Un righello flessibile o una striscia di carta appoggiata da solco a solco ti aiuta a confrontare le misure in millimetri.</p></div>
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
<div class="box case"><strong class="t">Caso pratico</strong> <p>Una cliente ha unghie con curva a C molto profonda: i tip della misura giusta in larghezza restano "sollevati" ai lati, quelli più stretti premono. Che cosa fai?</p> <ul><li>Scegli la misura che copre da solco a solco e prova una linea di tip con <strong>curva più accentuata</strong> o a mezzo incavo: meno plastica rigida da far combaciare.</li> <li>Assottiglia l'incavo ai lati, perché segua meglio la lamina.</li> <li>Se la curva è troppo diversa, lascia perdere il tip e lavora su cartina: costruisci la curva con il prodotto.</li></ul> <p>Un tip che non appoggia bene diventa un sollevamento ai lati nel giro di pochi giorni.</p></div>
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
<div class="box deep"><strong class="t">Approfondimento: come indurisce la colla</strong> <p>La colla per tip è un <strong>cianoacrilato</strong>: non asciuga evaporando, ma polimerizza quando incontra tracce di umidità sulle superfici. Bastano quelle presenti su una lamina disidratata. Per questo:</p> <ul><li>uno <strong>strato sottile</strong> indurisce in pochi secondi; una goccia spessa indurisce lentamente, resta molle al centro e intrappola aria;</li> <li>la reazione produce calore: più è rapida, più scalda;</li> <li>con aria molto secca la presa è più lenta; con aria umida più veloce;</li> <li>un attivatore accelera la presa, ma rende la colla più fragile.</li></ul> <p>Circa il 10% delle persone allergiche ai prodotti per unghie reagisce anche al cianoacrilato: anche la colla non deve toccare la pelle.</p></div>
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
<div class="box pro"><strong class="t">Consiglio da professionista: togliere un tip appena messo male</strong> <ul><li>Se te ne accorgi subito (bolla, tip storto), agisci prima di tagliare e fondere: c'è meno plastica da ammorbidire.</li> <li>Metti un batuffolo con acetone solo sul tip e lascia agire qualche minuto, proteggendo la pelle intorno con olio o crema.</li> <li>Quando la colla è ammorbidita, il tip scorre via con una spinta leggera di bastoncino. Se resiste, aspetta ancora: niente leve.</li> <li>Prima di riapplicare, rifai opacizzazione leggera e disidratante: l'acetone e l'olio hanno lasciato residui.</li></ul></div>
`,
          sources: ['https://open-exam-prep.com/study-guides/oh-nail-technician/artificial-nail-services/nail-tips-application',
            'https://open-exam-prep.com/study-guides/wa-nail-technician/tips-wraps-sculpting/nail-tips',
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/nail-tips', 'https://mdpi-res.com/d_attachment/molecules/molecules-23-00465/article_deploy/molecules-23-00465.pdf', 'https://dm.henkel-dam.com/is/content/henkel/Medical-Best-Practices-Flyer', 'https://doi.org/10.1111/cod.12942']
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
<div class="box pro"><strong class="t">Consiglio da professionista: tagliare senza crepe</strong> <ul><li>Su tip curvi taglia in <strong>due tempi</strong>: prima un lato, poi l'altro, incontrandoti al centro. Un unico taglio dal centro schiaccia la curva e può lasciare crepe sottili che si vedono solo dopo la copertura.</li> <li>Tieni il dito della cliente e il tip fermi con l'altra mano, così la forza va sulla plastica e non sulla colla appena indurita.</li> <li>Prima di coprire, guarda il bordo tagliato in controluce: una crepa sottile si allarga con il tempo. Meglio limare via quel tratto o cambiare tip subito.</li></ul></div>
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
<div class="box deep"><strong class="t">Approfondimento: che cosa fa il tip blender</strong> <p>I tip sono spesso in ABS, una plastica che contiene stirene. I tip blender sono solventi (per esempio miscele con acetone o stirene) che <strong>ammorbidiscono</strong> la superficie della plastica: il gradino si scioglie e si leviga più in fretta.</p> <p>Il rovescio: il solvente continua ad agire finché non evapora del tutto. Se resta intrappolato sotto la copertura, la plastica resta morbida e l'adesione si indebolisce: diverse formatrici collegano l'uso abbondante di blender ai sollevamenti. Se lo usi: pochissimo, solo sulla linea dell'incavo, mai sull'unghia naturale; poi lascia asciugare bene, opacizza e togli la polvere prima della copertura.</p></div>
`,
          sources: ['https://open-exam-prep.com/study-guides/oh-nail-technician/artificial-nail-services/nail-tips-application',
            'https://open-exam-prep.com/study-guides/wa-nail-technician/tips-wraps-sculpting/nail-tips',
            'https://www.salongeek.com/threads/blending-with-file-or-tip-blender-liquid.61963/', 'https://patents.justia.com/patent/5587108']
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
<div class="box pro"><strong class="t">Consiglio da professionista: far lavorare la gravità</strong> <ul><li>Il gel autolivellante continua a muoversi finché non va in lampada. Capovolgendo la mano, la gravità lo porta verso il centro dell'unghia e forma l'apex; rimettendola dritta, prima della lampada, il gel torna a distendersi. Per questo devi guardare il profilo <strong>subito prima</strong> di polimerizzare.</li> <li>Con un gel ad alta viscosità il capovolgimento serve meno: modelli tu la forma con il pennello.</li> <li>Se lavori su più dita prima di polimerizzare, il gel delle prime si sposta. All'inizio fai una o due dita alla volta, poi aumenta.</li></ul></div>
<h2>Spessori indicativi</h2>
<table>
<tr><th>Zona</th><th>Spessore</th><th>Perché</th></tr>
<tr><td>Zona 3 (cuticola)</td><td>Sottilissimo, "a filo"</td><td>Si fonde con l'unghia e non si vede il gradino quando ricresce</td></tr>
<tr><td>Zona 2 (apex)</td><td>Il punto più spesso</td><td>Regge la leva della lunghezza</td></tr>
<tr><td>Zona 1 (bordo)</td><td>Circa 0,8–1 mm, come una carta di credito o poco più</td><td>Più spesso si nota e si impiglia; più sottile si scheggia</td></tr>
</table>
${B('tip', 'Perla piccola, poi aggiungi', 'Meglio due perle piccole che una grande: una perla grande, capovolgendo la mano, può colare verso i lati o la pelle.')}
<div class="box deep"><strong class="t">Approfondimento: perché pochi decimi di millimetro contano tanto</strong> <p>In fisica, la rigidità di una lastra che si piega cresce con il <strong>cubo dello spessore</strong>: se raddoppi lo spessore, la lastra diventa circa 8 volte più rigida. È il motivo per cui l'apex funziona: pochi decimi di millimetro in più proprio sopra il punto di stress rendono la struttura molto più resistente, senza appesantire tutta l'unghia.</p> <p>Vale anche al contrario: una zona assottigliata per sbaglio durante la limatura perde molta resistenza. Un riferimento utile: una carta di credito è spessa circa <strong>0,76 mm</strong>. Usala per allenare l'occhio al bordo libero, guardando il profilo in controluce.</p></div>
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
            'https://www.katiebarnesacademy.com/blogs/preparation/what-is-the-difference-between-acid-free-and-acid-based-nail-primer', 'https://en.wikipedia.org/wiki/Flexural_rigidity']
        }
      ]
    },
    /* ------------------------------------------------------------------ 7 */
    {
      id: 'cartina', summary: ['Cartina a filo del bordo libero, in asse e in livello (né in su né in giù).', 'Zona 3 sottile (≈1 mm dalla pelle, mai sulla pelle), zona 2 apex, zona 1 ≈0,8–1 mm in punta.', 'Apex sopra il punto di stress: più lunga l\'unghia, più conta. Controlla sempre di profilo.', 'Bordo libero al massimo circa metà del letto ungueale.', 'Curva a C: segue l\'unghia naturale; pinching mai doloroso.'], n: 7, level: 'inter', title: 'Ricostruzione su cartina e apex',
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
<div class="box deep"><strong class="t">Approfondimento: perché la cartina decide la forza, non solo l'estetica</strong><p>I lati dell'allungamento devono uscire <strong>dritti dal solco laterale naturale</strong> e proseguire paralleli a esso. Se la cartina è storta o fuori livello, il prodotto nasce già nel posto sbagliato e l'unica correzione possibile è la lima.</p><ul><li>Dove manca prodotto, limando assottigli: nasce un punto debole.</li><li>Dove c'è troppo prodotto, resta spessore inutile: più peso e più leva sul letto ungueale.</li></ul><p>In entrambi i casi aumentano rotture e sollevamenti. Per questo le educatrici dicono che <em>la forma si costruisce sulla cartina e la lima rifinisce soltanto</em>. Tre minuti spesi in più per la cartina ti fanno risparmiare dieci minuti di limatura e una riparazione.</p></div>
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
<div class="box pro"><strong class="t">Consiglio da professionista</strong>Per vedere se la cartina (e poi l'unghia) è davvero centrata, metti dietro il dito qualcosa di <strong>nero</strong> (un cartoncino, la manica, il cuscinetto scuro), <strong>chiudi un occhio</strong> e guarda lungo l'unghia dalla cuticola verso la punta. Con un occhio solo la vista non "compensa" e lo sfondo scuro fa risaltare i contorni: ogni rotazione o ala più alta salta subito all'occhio. Fai questo controllo <em>prima</em> di appoggiare il prodotto, quando correggere costa solo un movimento delle alette.</div>
<h2>Errori frequenti</h2>
<ul>
<li><strong>Cartina ruotata verso il pollice</strong>: è l'errore più comune su anulare e mignolo. Guarda la mano dall'alto con le dita dritte.</li>
<li><strong>Alette chiuse in modo diverso</strong>: curva asimmetrica.</li>
<li><strong>Cartina spinta contro la pelle</strong>: dolore e prodotto steso male.</li>
<li><strong>Bordo libero non preparato</strong>: polvere e sebo anche sotto il bordo impediscono la saldatura.</li>
</ul>
<div class="box case"><strong class="t">Caso pratico</strong><p><strong>La cartina dell'anulare continua a girare verso il mignolo, anche se la rifai.</strong></p><p>Ragiona così: (1) la cliente tiene la mano rilassata con le dita piegate? Allora l'asse che vedi non è quello vero: fai appoggiare la mano piatta sul cuscinetto, dita distese e in linea con l'avambraccio. (2) Chiudi le alette prima sotto il polpastrello, tirando con la stessa forza dai due lati; solo dopo fai aderire i fianchi. (3) Usa come riferimento le linee di crescita della lamina, non il bordo libero, che spesso su anulare e mignolo è asimmetrico. Se l'unghia naturale stessa cresce inclinata, allinea l'allungamento al dito e compensa l'asimmetria con la lima sul bordo, non spostando la cartina.</p></div>
`,
          sources: ['https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/nail-sculpting-forms',
            'https://www.youngnails.com/blogs/news/how-to-use-nail-forms',
            'https://www.nailpro.com/how-to-customize-nail-forms/', 'https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-fit-nail-forms-to-different-nail-shapes', 'https://www.katiebarnesacademy.com/blogs/nail-structure-application/understanding-apex-placement-for-different-nail-shapes']
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
<div class="box deep"><strong class="t">Approfondimento: iponichio lungo o pterigio inverso?</strong><p>Non tutta la pelle che vedi sotto il bordo libero è un "iponichio lungo". Esiste una condizione chiamata <strong>pterigio inverso</strong> (pterygium inversum unguis o pterigio ventrale): la parte finale del letto ungueale resta <em>attaccata alla faccia inferiore della lamina</em> e il solco sotto la punta scompare. Spesso non dà fastidio, ma tagliare o spingere in quella zona provoca dolore o sanguinamento.</p><ul><li>Le fonti dermatologiche la collegano a malattie del tessuto connettivo, ma anche a fattori esterni come i prodotti acrilici e gel.</li><li>Non va "staccata", né raschiata, né spinta indietro con la cartina.</li><li>Lavora con lunghezze corte, cartina con incavo ampio e nessuna pressione.</li></ul><p>Se la pelle aderente aumenta da un appuntamento all'altro o fa male, annotalo e consiglia una visita dermatologica. Ricorda: come lo pterigio dorsale non è la cuticola, anche questo non è "pelle in più" da togliere.</p></div>
<div class="box case"><strong class="t">Caso pratico</strong><p><strong>Cliente con unghie a "trampolino" (ski-jump) marcato che vuole un allungamento medio.</strong></p><ol><li>Accorcia il bordo libero naturale il più possibile: la parte che sale è proprio quella che ti porterebbe fuori linea.</li><li>Posiziona la cartina seguendo la linea della lamina vicino alla cuticola (le linee di crescita), quindi leggermente <em>più in basso</em> del bordo.</li><li>Riempi l'eventuale spazio tra bordo e cartina con strati sottili di prodotto, non con una perla grande.</li><li>Porta l'apex un po' più in alto del solito: di profilo la linea deve sembrare dritta, e lo spessore in più "nasconde" la salita della lamina.</li><li>Proponi una lunghezza prudente al primo servizio: la lamina a ski-jump è spesso sottile e flessibile.</li></ol></div>
<div class="box pro"><strong class="t">Consiglio da professionista</strong>Tieni una <strong>scheda delle cartine</strong> per le clienti abituali: annota "anulare destro: incavo profondo", "pollici: due cartine", "mignolo: aletta sinistra più stretta". Al refill o alla ricostruzione successiva ritagli le cartine <em>prima</em> che la cliente si sieda, e risparmi tempo e prove a secco. Un'altra abitudine utile: ritaglia sempre poco per volta e riprova. Un incavo troppo largo lascia uno spazio sotto il bordo, ed è proprio lo spazio che fa colare il prodotto.</div>
`,
          sources: ['https://www.youngnails.com/blogs/news/how-to-use-nail-forms',
            'https://www.salongeek.com/threads/fitting-forms-with-high-hyponychium-advice-please.329807/',
            'https://www.nailpro.com/how-to-customize-nail-forms/',
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/nail-sculpting-forms', 'https://en.wikipedia.org/wiki/Pterygium_inversum_unguis', 'https://cdn.enzyklopaedie-dermatologie.de/en/dermatology/pterygium-unguis-ventralis-132424', 'https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-fit-nail-forms-to-different-nail-shapes']
        },
        {
          id: 'zone-apex', videos: [{"id": "Tx3lwXOS0L0", "title": "Do's and Don'ts of Apex Structure", "channel": "YoungNailsInc", "lang": "EN"}, {"id": "PD1qHAO3cvk", "title": "How to Build the Perfect Apex", "channel": "Liz Means Business", "lang": "EN"}], simple: 'Immagina un ponte: dove l\'unghia lascia il dito (punto di stress) serve il pilastro più alto, cioè l\'apex. Alla base e in punta il prodotto è sottile.', title: 'Le tre zone e l\'apex', min: 11,
          html: `
<p>Un'unghia allungata funziona come una <strong>leva</strong>: ogni volta che la punta urta qualcosa, la forza si scarica nel punto in cui l'unghia si stacca dal dito, il <strong>punto di stress</strong>. Per questo la ricostruzione non ha lo stesso spessore ovunque: è divisa in tre zone.</p>
${F('zone-costruzione.svg', 'Le tre zone di costruzione.')}
<h2>Le tre zone</h2>
<table>
<tr><th>Zona</th><th>Dove</th><th>Spessore</th><th>Perché</th></tr>
<tr><td><strong>Zona 1</strong> – bordo libero</td><td>Dall'allungamento fino alla linea del sorriso</td><td>Sottile e uniforme: circa lo spessore di una carta di credito (0,76 mm) o poco più, fino a circa 1 mm</td><td>Più spesso si impiglia e sembra finto; più sottile si scheggia</td></tr>
<tr><td><strong>Zona 2</strong> – apex</td><td>Centro dell'unghia, sopra il punto di stress</td><td>La parte più spessa</td><td>Regge la leva della lunghezza</td></tr>
<tr><td><strong>Zona 3</strong> – zona cuticolare</td><td>Vicino a cuticola e solchi laterali</td><td>Sottilissima, sfumata "a zero"</td><td>Il prodotto deve fondersi con la lamina e non toccare mai la pelle</td></tr>
</table>
${F('zone-spessori-sezione.svg', 'Sezione longitudinale e trasversale: dove il prodotto è spesso e dove è sottile.')}
<div class="box deep"><strong class="t">Approfondimento: "sottile il più possibile, spesso solo dove serve"</strong><p>Le educatrici ripetono una regola: la ricostruzione deve essere <strong>sottile quanto basta per durare</strong>, e non di più. Lo spessore in eccesso non rende l'unghia più forte: la rende più pesante e rigida, e questo carica di stress la lamina naturale sotto. Il risultato tipico sono i sollevamenti, soprattutto alla base.</p><p>Pensa a una trave: serve materiale solo dove la trave si piega, cioè sopra il punto di stress. Per questo l'apex è <strong>un punto</strong>, non una fascia: dal centro si scende dolcemente verso i lati, che restano dritti ma non massicci, così la mano non sembra "a paletta".</p></div>
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
<h3>L'apex cambia con la forma</h3><table><tr><th>Forma</th><th>Dove sta l'apex</th><th>Linea dall'apex alla punta</th></tr><tr><td>Quadrata, squoval</td><td>Al centro del letto ungueale "allungato"</td><td>Dritta, quasi orizzontale</td></tr><tr><td>Mandorla, stiletto</td><td>Circa a un terzo della lunghezza dell'unghia</td><td>Scende dritta verso la punta</td></tr><tr><td>Ballerina (coffin)</td><td>Circa a un terzo</td><td>Dritta fino alla punta</td></tr></table><p>Regola comune: <strong>più l'unghia è lunga, più l'apex sale e si sposta verso la cuticola</strong>, ma non così indietro da creare una gobba che non sostiene niente. Nelle forme a punta (mandorla, stiletto) l'apex viene chiamato anche "punto di equilibrio".</p>
<h2>Come controllarlo</h2>
${F('apex-controllo-viste.svg', 'Controllo dell\'apex da tre punti di vista.')}
<ol class="steps">
<li><strong>Di profilo</strong>: la linea sale dolcemente dalla cuticola, raggiunge il punto più alto sopra il punto di stress e scende in modo regolare verso la punta.</li>
<li><strong>Dal davanti</strong> (guardando la punta verso di te): lo spessore è uguale a destra e a sinistra, la curva è regolare.</li>
<li><strong>Dall'alto, con luce</strong>: il riflesso della lampada scorre senza "salti" e mostra il punto più alto al centro.</li>
<li><strong>Dal basso</strong>: il bordo libero è sottile e uniforme.</li>
</ol>
${B('tip', 'Il trucco del riflesso', 'Ruota lentamente il dito sotto la lampada: una striscia di luce continua e regolare indica una superficie ben costruita; una luce che si spezza indica avvallamenti o gobbe.')}
<div class="box pro"><strong class="t">Consiglio da professionista</strong>Oltre al punto più alto, guarda la <strong>linea che va dall'apex alla punta</strong> (l'arco superiore). Deve essere dritta. Se l'apex è troppo avanti, questa linea si incurva verso il basso e "tira" il bordo libero sopra il polpastrello: l'unghia sembra un artiglio e diventa debole proprio dove la leva è maggiore. Controllo veloce: appoggia una lima dritta sull'unghia di profilo, dall'apex verso la punta. Se sotto la lima vedi una "pancia" o una luce irregolare, la curva non è giusta.</div>
<div class="box case"><strong class="t">Caso pratico</strong><p><strong>Una cliente rompe tre volte di fila il medio, sempre con una crepa trasversale vicino alla linea del sorriso.</strong></p><p>Domande da farsi: la crepa è <em>sopra il punto di stress</em>? Allora la zona 2 era troppo sottile o l'apex era spostato in avanti. Guarda le tue foto di profilo: l'apex era sopra il punto in cui l'unghia si stacca dal dito? Il refill è stato fatto dopo 4 settimane o più? In quel caso l'apex era "migrato" verso la punta. Correzione: accorcia, ricostruisci la zona 2 con più spessore sopra il punto di stress e anticipa il refill di una settimana.</p></div>
`,
          sources: ['https://open-exam-prep.com/study-guides/oh-nail-technician/artificial-nail-services/sculptured-acrylic-nails',
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/nail-sculpting-forms',
            'https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-file-different-nail-shapes',
            'https://www.scratchmagazine.co.uk/blog/simply-salon-nails-perfecting-proper-nail-structure/', 'https://www.katiebarnesacademy.com/blogs/nail-structure-application/understanding-apex-placement-for-different-nail-shapes', 'https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-fit-nail-forms-to-different-nail-shapes', 'https://scratchmagazine.co.uk/feature/why-the-arch-is-integral-to-a-well-balanced-nail-enhancement', 'https://katiebarnesacademy.com/blogs/nail-structure-application/how-to-deal-with-nail-service-breakdown', 'https://open-exam-prep.com/study-guides/ga-nail-technician/nail-enhancement-chemistry-acrylics/acrylic-maintenance-removal']
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
<div class="box deep"><strong class="t">Approfondimento: la fisica della leva</strong><p>Quando la punta urta il bordo di un tavolo, la forza agisce come su una chiave inglese: <strong>più lungo è il braccio, maggiore è lo sforzo</strong> nel punto in cui l'unghia si stacca dal dito. In modo semplificato, se raddoppi la lunghezza che sporge, a parità di urto raddoppia lo sforzo sul punto di stress.</p><p>Per questo la regola della metà non è solo estetica. Oltre quella misura servono più spessore in zona 2 e una curva a C più marcata per reggere lo stesso urto; se la struttura non cresce insieme alla lunghezza, il prodotto si crepa o, peggio, fa leva sulla lamina e la stacca dal letto.</p></div>
<h2>Più lunghezza = più struttura</h2>
${F('apex-lunghezza.svg', 'Unghia corta e unghia lunga: l\'apex cresce e resta sopra il punto di stress.')}
<table>
<tr><th>Lunghezza</th><th>Struttura</th><th>Adatta a</th></tr>
<tr><td>Corta (bordo ≤ 1/3 del letto)</td><td>Apex leggero, quasi naturale</td><td>Chi lavora molto con le mani, prime clienti</td></tr>
<tr><td>Media (circa 1/2 del letto)</td><td>Apex ben visibile di profilo</td><td>Uso quotidiano in salone</td></tr>
<tr><td>Lunga (oltre 1/2)</td><td>Apex alto, curva a C più marcata</td><td>Clienti abituate, eventi, gare</td></tr>
</table>
<div class="box pro"><strong class="t">Consiglio da professionista</strong>Quando "allunghi il letto" con il cover, la smile line si sposta in avanti, ma <strong>la leva non cambia</strong>: si misura sempre dal punto in cui l'unghia lascia il dito fino alla punta. Un'unghia con un letto allungato bello e un bordo bianco corto può <em>sembrare</em> corta e invece essere molto lunga dal punto di vista della struttura. Calcola l'apex sulla lunghezza reale dell'allungamento, non sulla lunghezza del bianco.</div>
<h2>Come decidere con la cliente</h2>
<ol class="steps">
<li><strong>Chiedi</strong> che lavoro fa, se usa tastiera o attrezzi, se fa sport.</li>
<li><strong>Guarda il letto ungueale</strong>: corto, lungo, morsicato?</li>
<li><strong>Proponi</strong> una lunghezza di partenza prudente: si può allungare al refill successivo.</li>
<li><strong>Segna</strong> la lunghezza sulla griglia della cartina, uguale per tutte le dita (il pollice può essere leggermente più lungo e il mignolo leggermente più corto, a parità di aspetto).</li>
</ol>
${B('warn', 'Prima volta', 'Alla prima ricostruzione la cliente non è abituata: una lunghezza eccessiva aumenta il rischio di urti, rotture e traumi al letto ungueale.')}
<div class="box case"><strong class="t">Caso pratico</strong><p><strong>Cliente con letto ungueale cortissimo (ex onicofagia) che chiede unghie lunghe "come in foto".</strong></p><ul><li><strong>Spiega con un gesto:</strong> mostra con la cartina quanto sporgerebbe l'unghia rispetto alla base che la sostiene.</li><li><strong>Proponi una strada a tappe:</strong> primo servizio corto, con il cover per allungare otticamente il letto e un bordo libero sottile; al refill si aggiungono 1–2 mm se l'unghia ha tenuto.</li><li><strong>Scegli una forma che perdona:</strong> squoval o ovale corta, non stiletto.</li><li><strong>Annota sulla scheda</strong> la lunghezza in quadretti della griglia: così puoi aumentarla in modo controllato.</li></ul><p>Spesso la cliente si fida di più quando vede un piano chiaro che quando le dici solo di no.</p></div>
`,
          sources: ['https://www.salongeek.com/threads/choosing-the-correct-length-for-balance-and-beauty.11417/',
            'https://www.scratchmagazine.co.uk/blog/simply-salon-nails-perfecting-proper-nail-structure/',
            'https://open-exam-prep.com/study-guides/oh-nail-technician/artificial-nail-services/sculptured-acrylic-nails', 'https://www.katiebarnesacademy.com/blogs/nail-structure-application/understanding-apex-placement-for-different-nail-shapes', 'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/nail-sculpting-forms', 'https://www.salongeek.com/threads/camouflage-gel.60825/']
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
<div class="box deep"><strong class="t">Approfondimento: perché un arco regge più di una lastra</strong><p>La curva a C funziona come l'arco di un ponte: una forza che arriva al centro non piega la lastra, ma viene <strong>deviata verso i lati</strong>, dove i solchi e i bordi laterali la scaricano. Una superficie piatta, invece, prende tutta la forza al centro e si flette.</p><p>Per questo una curva più alta permette lunghezze maggiori con meno spessore. Ma l'arco funziona solo se i <strong>lati sono pieni e dritti</strong>: se in limatura assottigli i fianchi, l'arco perde le sue "spalle" e la crepa nasce proprio lì. Le guide commerciali parlano di curve tra circa il 25 e il 50% per il salone: la percentuale giusta è quella che la lamina della cliente sopporta senza dolore.</p></div>
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
<div class="box pro"><strong class="t">Consiglio da professionista</strong><ul><li><strong>Gel:</strong> molte educatrici fanno un flash di circa 10 secondi (dipende da gel e lampada), poi applicano la pinzetta, la lasciano in posizione e completano la polimerizzazione con la pinzetta montata. Dopo averla tolta, fai un'ultima passata in lampada: le parti coperte dalla pinzetta potrebbero aver ricevuto meno luce.</li><li><strong>Pinzetta che scivola sul gel:</strong> metti un pezzetto di nastro o di cerotto in tessuto all'interno delle ganasce.</li><li><strong>Troppo presto</strong> lasci un'impronta: un'ammaccatura sul fianco è un punto debole. <strong>Troppo tardi</strong> non cambi la curva e fai solo male.</li><li>Un bastoncino per curva a C troppo piccolo forza una curva troppo stretta e indebolisce l'unghia.</li></ul></div>
<h2>Errori frequenti</h2>
<ul>
<li><strong>Pinching troppo tardi</strong> (acrilico già duro): crepe sui lati.</li>
<li><strong>Pressione diversa sui due lati</strong>: curva storta, unghia che "gira".</li>
<li><strong>Pinching sul letto ungueale</strong>: dolore e rischio di distacco.</li>
<li><strong>Curve diverse tra le dita</strong>: la mano sembra disordinata.</li>
</ul>
${B('tip', 'Strumenti', 'Esistono pinzette e "bastoncini per curva a C". Le pinze trasparenti sono preferibili con il gel perché lasciano passare la luce. In alcune gare le pinze sono vietate: controlla sempre il regolamento.')}
<div class="box case"><strong class="t">Caso pratico</strong><p><strong>Cliente con unghie naturali piatte che vede le foto da gara e vuole "quella curva".</strong></p><p>Una lamina piatta non si può forzare: il pinching sul letto provoca dolore e può staccare la lamina (onicolisi). La soluzione è costruire la curva <em>solo sull'allungamento</em>:</p><ol><li>Pre-curva la cartina in modo più marcato, partendo dal bordo libero.</li><li>Accetta che sulla parte naturale la curva resti quella della cliente: il passaggio deve essere graduale.</li><li>Fai il pinching solo sull'allungamento, dal punto di stress in avanti.</li><li>Spiega alla cliente che la curva aumenterà un po' a ogni servizio, man mano che l'allungamento è sostenuto meglio.</li></ol></div>
`,
          sources: ['https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/nail-sculpting-forms',
            'https://open-exam-prep.com/study-guides/oh-nail-technician/artificial-nail-services/sculptured-acrylic-nails',
            'https://www.nailpro.com/technique/article/21156099/competition-technique-how-to-pre-shape-a-c-curve',
            'https://purespadirect.com/blogs/pure-spa-direct-blog/how-to-achieve-the-perfect-c-curve-using-professional-pinching-tools-a-nail-techs-guide-to-strength-style', 'https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-fit-nail-forms-to-different-nail-shapes', 'https://www.nailpro.com/how-to-customize-nail-forms/']
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
<div class="box deep"><strong class="t">Approfondimento: temperatura e autolivellamento</strong><p>La consistenza (viscosità) di un gel cambia con la temperatura. Con il freddo il gel diventa <strong>più denso</strong>: si autolivella poco e restano segni del pennello. Con il caldo diventa <strong>più fluido</strong>: si livella in fretta, ti lascia meno tempo per costruire e tende a colare verso i solchi e la cuticola.</p><ul><li>Molti produttori indicano una temperatura di lavoro di circa <strong>20–25 °C</strong>: controlla la scheda del tuo gel.</li><li>Non tenere i vasetti sul davanzale, vicino al termosifone o sotto la lampada accesa.</li><li>D'inverno lascia il vasetto a temperatura ambiente prima di usarlo; d'estate lavora un dito alla volta e fai un flash appena la perla è al posto giusto.</li></ul></div>
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
<div class="box deep"><strong class="t">Approfondimento: lo strato appiccicoso (strato di dispersione)</strong><p>Dopo la lampada la superficie del gel resta appiccicosa perché <strong>l'ossigeno dell'aria blocca la crescita delle catene</strong> di polimero: quello strato è polimerizzato meno della metà. Non è un difetto: è la "colla" che fa aderire lo strato successivo.</p><ul><li>Non pulirlo tra uno strato e l'altro, se il produttore non lo chiede.</li><li>È gel non polimerizzato: <strong>non deve toccare la pelle</strong>. Toglilo con un tampone senza pelucchi e il cleaner, senza strofinare sulle cuticole.</li><li>Uno strato appiccicoso più spesso del solito può indicare una lampada debole o non adatta al gel.</li><li>I prodotti "no-wipe" sono formulati in modo diverso; secondo Doug Schoon, i gel senza strato di inibizione tendono a scaldare di più.</li></ul></div>
<h2>Problemi durante il lavoro</h2>
<table>
<tr><th>Problema</th><th>Causa probabile</th><th>Rimedio</th></tr>
<tr><td>Il gel cola nei solchi</td><td>Perla troppo grande o gel troppo fluido; mano capovolta troppo a lungo</td><td>Perle più piccole; pulisci con un pennello prima della lampada</td></tr>
<tr><td>Bruciore in lampada</td><td>Strato spesso, lamina sottile</td><td>Togli la mano qualche secondo e rientra ("flash and pull"); strati più sottili</td></tr>
<tr><td>Allungamento storto dopo aver tolto la cartina</td><td>Cartina fuori asse</td><td>Correggi in limatura; la prossima volta controlla dall'alto</td></tr>
<tr><td>Bolle</td><td>Pennello agitato o gel mescolato con forza</td><td>Movimenti lenti, gel a temperatura ambiente</td></tr>
</table>
${B('tip', 'Checklist finale', 'Profilo con apex sopra il punto di stress · curva a C regolare · zona cuticolare pulita e sottile · bordo libero sottile (≈0,8–1 mm) e sigillato · lati dritti · nessuna sbavatura sulla pelle.')}
<div class="box deep"><strong class="t">Approfondimento: da dove viene il bruciore</strong><p>Il calore <strong>non viene dalla lampada</strong> ma dalla reazione: ogni legame che si forma libera un po' di calore. Più prodotto polimerizza nello stesso momento, più calore arriva sul letto ungueale.</p><ul><li><strong>Spessore:</strong> più spesso = più calore. Per questo il pollice, che ha più superficie, si scalda di più.</li><li><strong>Velocità:</strong> un gel pensato per una lampada più lenta, sotto un LED potente, libera tutto il calore in poco tempo. Nell'esempio di Schoon, da 2 minuti a 30 secondi: lo stesso calore in un quarto del tempo.</li><li><strong>Lamina sottile:</strong> la lamina fa da isolante. Se è stata limata troppo, il calore arriva al letto. I recettori del dolore si attivano intorno a <strong>46 °C</strong>.</li></ul><p>Il calore eccessivo può contribuire al distacco della lamina (onicolisi). Usa la lampada indicata dal produttore e lavora a strati sottili.</p></div>
<div class="box case"><strong class="t">Caso pratico</strong><p><strong>Il gel scivola sempre verso il solco del lato del mignolo, solo su alcune dita.</strong></p><p>Cause probabili: dito inclinato mentre lavori (la gravità porta il gel verso il lato più basso), perla troppo grande, salone caldo. Soluzioni: tieni il dito della cliente perfettamente orizzontale e ruotalo tu per guardare; lavora <strong>un'unghia alla volta</strong> e fai un flash appena la perla è in posizione, invece di preparare quattro dita e poi la lampada; usa un pennello pulito per "riprendere" il gel dal solco prima del flash. Se succede su tutte le dita, il gel è probabilmente troppo caldo o è la viscosità sbagliata per quel lavoro.</p></div>
`,
          sources: ['https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/nail-sculpting-forms',
            'https://www.ellisons.co.uk/blog/how-to-build-the-perfect-apex-with-the-gelbottle-inc',
            'https://www.nsinails.com.au/blogs/news/nail-preparation', 'https://www.homeofnailart.com/blogs/knowledge-hub/a-nail-tech-s-guide-to-heat-runny-builder-gel-and-heat-spikes', 'https://www.homeofnailart.com/blogs/knowledge-hub/easy-guide-to-temperature-control-for-perfect-hema-free-biab-and-gel-polish', 'https://nailknowledge.org/nail-knowledge-base/inhibition-layer-and-no-cleanse-gels', 'https://nailknowledge.org/blog/heat-spikes']
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
<div class="box deep"><strong class="t">Approfondimento: che cosa succede dentro la perla</strong><ul><li><strong>Nella polvere</strong> c'è un iniziatore, il perossido di benzoile: con il calore dell'ambiente e del dito si spezza e avvia la reazione.</li><li><strong>Nel liquido</strong> c'è un catalizzatore che accelera la rottura dell'iniziatore, e ci sono inibitori che impediscono al monomero di indurirsi nel flacone. La sfumatura viola indica assorbitori UV contro l'ingiallimento.</li><li>Il monomero deve <strong>avvolgere ogni granello</strong> di polvere: se manca liquido, i granelli non si legano bene (perla asciutta, fragile); se ce n'è troppo, il monomero in eccesso si ritira mentre indurisce e "tira" via il prodotto dalla lamina.</li></ul><p>Le polveri colorate hanno più pigmento e a volte vogliono una perla appena più umida: controlla le istruzioni del produttore.</p></div>
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
<div class="box pro"><strong class="t">Consiglio da professionista</strong><p><strong>La temperatura cambia i tempi.</strong> Con il freddo l'acrilico indurisce più lentamente e la perla tende a colare: scarica bene il pennello. Con il caldo indurisce in fretta. Valori indicativi di un marchio: prodotto normale circa 1 min 30 s prima che non si possa più muovere e circa 4 min 30 s prima di limarlo; prodotto rapido circa 1 min e 4 min.</p><p><strong>La grandezza della perla dipende dal liquido nel pennello.</strong> Più monomero nel corpo del pennello dà una perla più grande. Scarica l'eccesso sul bordo del dappen e appoggia la punta sulla polvere senza affondare. La perla giusta sembra una perla bagnata, senza polvere asciutta ai bordi: appena posata comincia a distendersi ma non scorre verso la pelle.</p></div>
<h2>Errori frequenti</h2>
<table>
<tr><th>Errore</th><th>Conseguenza</th><th>Correzione</th></tr>
<tr><td>Perla bagnata in zona 3</td><td>Cola sulla cuticola: sollevamento e rischio di allergia</td><td>Perla più asciutta, scarica il pennello</td></tr>
<tr><td>Perla asciutta in zona 1</td><td>Bolle, opacità, punta fragile</td><td>Più monomero nel pennello</td></tr>
<tr><td>Prodotto sulla pelle o sulla cuticola</td><td>Sollevamento in pochi giorni</td><td>Rimuovi subito con il pennello pulito, prima che indurisca</td></tr>
<tr><td>Apex piatto o troppo avanti</td><td>Crepa al centro o leva sul letto</td><td>Perla di zona 2 centrata sopra il punto di stress</td></tr>
<tr><td>Troppo prodotto in una volta su unghia sottile</td><td>Calore durante l'indurimento</td><td>Perle più piccole, lavoro per strati</td></tr>
</table>
<div class="box warn"><strong class="t">Prodotti rapidi e calore</strong>Un acrilico "fast set" libera <strong>lo stesso calore</strong> di uno normale, ma in meno tempo: il calore diventa percepibile quando si libera in un minuto o meno. Per questo i prodotti rapidi scaldano di più nelle giornate calde. Anche usare una <strong>polvere di un altro sistema</strong> con il tuo liquido può provocare surriscaldamento: liquido e polvere sono studiati in coppia. Non rendere la perla più bagnata per "rallentare" un prodotto rapido: cambi il rapporto e indebolisci la struttura. Meglio scegliere il prodotto adatto alla stagione.</div>
`,
          sources: ['https://open-exam-prep.com/study-guides/oh-nail-technician/artificial-nail-services/sculptured-acrylic-nails',
            'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/nail-sculpting-forms',
            'https://nsinails.com.au/blogs/news/mix-ratio-l-p',
            'https://www.katiebarnesacademy.com/blogs/nail-structure-application/understanding-acrylic-chemistry-mix-ratio', 'https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/liquid-powder-acrylics', 'https://nailknowledge.org/blog/heat-spikes']
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
<div class="box deep"><strong class="t">Approfondimento: ogni forma ha la sua cartina</strong><table><tr><th>Forma</th><th>Di profilo</th><th>Dall'alto</th></tr><tr><td>Quadrata, squoval</td><td>Dritta, in linea con il centro del dito</td><td>Lati paralleli, "aperti"</td></tr><tr><td>Mandorla, stiletto</td><td>Leggermente verso il basso: linea dritta dall'apex alla punta</td><td>Lati che si chiudono</td></tr><tr><td>Ballerina</td><td>Dritta come una quadrata</td><td>Chiusa come una mandorla</td></tr></table><p>Se costruisci con la cartina di una quadrata e poi limi una mandorla, apex e linea di profilo finiscono nel posto sbagliato: l'unghia è sbilanciata e più debole. Decidi la forma <strong>prima</strong> di posare la cartina.</p></div>
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
<div class="box case"><strong class="t">Caso pratico</strong><p><strong>Parrucchiera con dita corte che vuole la stiletto vista sui social.</strong></p><p>Pesa tre cose: lavora tutto il giorno con mani in acqua, prodotti e spazzole; ha dita corte (la stiletto la slancerebbe davvero); è alla prima ricostruzione. Proposta: una <strong>mandorla morbida di lunghezza media</strong>. Slancia quasi quanto la stiletto, ha la punta più larga e quindi più resistente, e non si impiglia nei capelli. Se dopo due refill l'unghia ha tenuto, si può stringere gradualmente verso la stiletto. Così la cliente ottiene l'effetto che vuole e tu non perdi tempo in riparazioni.</p></div>
<h2>Esempio: ottenere una mandorla</h2>
${F('forme-limatura-step.svg', 'Dalla quadrata alla mandorla in quattro passaggi.')}
${B('tip', 'Scegli con la cliente', 'Considera lavoro, abitudini e forma del letto ungueale: una stiletto lunga non è adatta a chi lavora molto con le mani.')}
${B('warn', 'Le forme si costruiscono, non solo si limano', 'Una forma riesce bene se la prepari già con la cartina e con il prodotto (lati dritti, apex al posto giusto). La lima rifinisce: se il prodotto è stato messo male, limando assottigli i punti sbagliati.')}
<div class="box pro"><strong class="t">Consiglio da professionista</strong>Ballerina e coffin vengono spesso confuse: la <strong>coffin</strong> ha la punta piatta e gli angoli netti; la <strong>ballerina</strong> ha la punta squadrata ma con angoli leggermente ammorbiditi. In entrambe il restringimento riguarda <strong>solo l'allungamento</strong>: se limi i lati in diagonale già dove l'unghia poggia sul dito, togli prodotto proprio dai fianchi che reggono la struttura. I lati devono partire dritti e paralleli dai solchi, e cominciare a chiudersi solo dopo il bordo del dito.</div>
`,
          sources: ['https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-file-different-nail-shapes',
            'https://www.makeup.com/your-nail-shape-guide',
            'https://www.livethatglow.com/nail-shape-guide/',
            'https://www.my-personaltrainer.it/bellezza/qual-e-la-forma-di-unghie-che-slancia-le-dita-e-resiste-davvero-agli-urti-senza-spezzarsi.html', 'https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-fit-nail-forms-to-different-nail-shapes', 'https://www.katiebarnesacademy.com/blogs/nail-structure-application/understanding-apex-placement-for-different-nail-shapes', 'https://scratchmagazine.co.uk/blog/simply-salon-nails-how-to-create-various-nail-shapes']
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
<div class="box pro"><strong class="t">Consiglio da professionista</strong>Per una quadrata "morbida" senza trasformarla in squoval, tieni la lima a circa <strong>45°</strong> sullo spigolo superiore della punta e fai una o due passate leggere lungo tutto il bordo. Dall'alto la forma resta quadrata, ma il bordo non è più tagliente: si impiglia meno nelle calze e nei maglioni e si scheggia meno. Fai lo stesso numero di passate su tutte le dita, altrimenti la punta appare più sottile su alcune unghie.</div>
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
<div class="box deep"><strong class="t">Approfondimento: i due archi delle forme a punta</strong><p>Nelle forme a triangolo (stiletto e simili) l'<strong>arco superiore</strong> deve scendere dritto dall'apex alla punta, con un'inclinazione di circa 45°. L'<strong>arco inferiore</strong>, quello che vedi di lato sotto l'allungamento, deve restare parallelo all'asse del dito: se lo inclini in su o in giù aumenti la pressione sull'unghia e la indebolisci.</p><p>I lati della stiletto devono restare dritti, non arrotondati, fino alla punta. Una punta "a pancia" sembra più morbida ma ha meno materiale proprio dove la forma è più fragile.</p></div>
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
<div class="box pro"><strong class="t">Consiglio da professionista: l'arco inferiore si lima per ultimo</strong><ol><li>Costruisci l'arco inferiore circa <strong>1 mm più basso</strong> del necessario: ti resta materiale per correggere. Togliere dove manca prodotto crea solo un punto debole.</li><li>Gira la mano della cliente di lato e lavora da quella vista.</li><li>Se serve, segna con matita e righello la linea da seguire.</li><li>Infila la lima nell'angolo, dal punto in cui finisce l'unghia naturale all'angolo della punta, e sostienila da dietro con uno o due dita perché non si fletta.</li><li>Una o due passate, togli la polvere, controlla. Ripeti solo se serve.</li></ol><p>Tieni la lima lontana dal solco laterale naturale: è un'abitudine comune e toglie dritto e forza all'arco.</p></div>
`,
          sources: ['https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-file-different-nail-shapes',
            'https://www.homeofnailart.com/blogs/knowledge-hub/mastering-the-art-of-nail-filing-a-comprehensive-guide-for-professional-nail-technicians',
            'https://www.scratchmagazine.co.uk/blog/simply-salon-nails-filing-different-nail-shapes/', 'https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-fit-nail-forms-to-different-nail-shapes', 'https://scratchmagazine.co.uk/feature/why-the-arch-is-integral-to-a-well-balanced-nail-enhancement', 'https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-file-the-lower-arch-and-side-walls-without-removing-too-much']
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
<div class="box deep"><strong class="t">Approfondimento: che cosa vuol dire il numero della grana</strong><p>Il numero indica quante particelle abrasive ci sono su una certa superficie (per pollice quadrato): <strong>numero basso = particelle grandi = lima aggressiva</strong>; numero alto = particelle piccole = lima fine. Per questo 100 accorcia in fretta e 240 leviga.</p><ul><li>Sull'unghia naturale molte fonti considerano <strong>240</strong> la grana più grossa consigliata; 80–100 assottigliano la lamina.</li><li>Una lima consumata "non morde": istintivamente premi di più, e la pressione produce calore e solchi. Quando senti che devi spingere, cambiala.</li><li>Attenzione: alcune etichette commerciali usano formule confuse. Fidati del numero, non della parola "grit alto/basso".</li></ul></div>
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
<div class="box deep"><strong class="t">Approfondimento: limatura e sensibilità al calore</strong>La lamina naturale fa da <strong>isolante</strong> per il letto ungueale. Ogni passata aggressiva in preparazione la assottiglia, e una lamina sottile lascia passare il calore della polimerizzazione. Una limatura troppo energica può anche causare una piccola <strong>ustione da attrito</strong> sul letto: da quel momento la cliente sente bruciore in lampada anche con un prodotto che prima tollerava bene. Per questo in preparazione basta togliere la lucidità; la forza della lima si usa sul prodotto, non sulla lamina.</div>
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
<div class="box case"><strong class="t">Caso pratico</strong><p><strong>Al refill la cliente sente bruciare in lampada solo su indice e medio, mai successo prima.</strong></p><p>Ragiona sulle differenze rispetto al servizio precedente: (1) Su quelle dita hai limato di più per togliere un sollevamento e sei arrivata alla lamina? (2) Hai usato più prodotto per ricostruire l'apex? (3) È cambiata la lampada? Rimedi immediati: tira fuori la mano per qualche secondo e rientra, strati più sottili. Per i prossimi servizi: annota sulla scheda le dita sensibili, prepara con buffer fine e lascia sempre un velo di prodotto quando elimini i sollevamenti. In genere la sensibilità diminuisce quando la lamina sottile è cresciuta via.</p></div>
`,
          sources: ['https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-file-different-nail-shapes',
            'https://www.homeofnailart.com/blogs/knowledge-hub/mastering-the-art-of-nail-filing-a-comprehensive-guide-for-professional-nail-technicians',
            'https://open-exam-prep.com/study-guides/pa-nail-technician/manicure-pedicure-foundations/manicure-pedicure-procedures',
            'https://www.katiebarnesacademy.com/blogs/allergies-and-nail-tech-protection/why-how-to-take-care-of-yourself-at-the-nail-desk', 'https://purespadirect.com/blogs/pure-spa-direct-blog/is-higher-grit-number-smoother-or-rougher', 'https://purespadirect.com/blogs/pure-spa-direct-blog/what-nail-file-grit-to-use-for-natural-nails', 'https://nailknowledge.org/blog/heat-spikes', 'https://katiebarnesacademy.com/blogs/nail-structure-application/how-to-deal-with-nail-service-breakdown']
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
<div class="box pro"><strong class="t">Consiglio da professionista</strong>Per la vista dall'alto e dal davanti usa uno <strong>sfondo nero</strong> e guarda con <strong>un occhio chiuso</strong>, lungo l'unghia dalla cuticola verso la punta. Così vedi subito se l'apex è al centro e se i fianchi sono uguali. Per l'arco inferiore, invece, appoggia di lato una lima dritta sotto l'allungamento: se tocca in un punto solo, la linea non è dritta. Ricorda che lo stesso difetto si vede meglio a 30–40 cm di distanza che da vicino.</div>
<h2>La simmetria con l'asse</h2>
${F('simmetria-asse.svg', 'L\'asse del dito: punta centrata e lati uguali.')}
<ol class="steps">
<li><strong>Immagina una linea</strong> che parte dal centro della cuticola e prosegue lungo il dito.</li>
<li><strong>La punta</strong> (o il centro della punta) deve cadere su quella linea.</li>
<li><strong>I due lati</strong> devono essere a uguale distanza dalla linea, come immagini allo specchio.</li>
<li><strong>Se un lato è più largo</strong>, lima solo quel lato, poche passate alla volta, e ricontrolla.</li>
</ol>
<div class="box pro"><strong class="t">Consiglio da professionista</strong>Quando non sei sicura della simmetria, <strong>disegna l'asse</strong>: con una matita morbida traccia una linea sottile dal centro della cuticola alla punta, sopra il prodotto limato. Il segno si toglie con il buffer. Un altro trucco utile: fotografa la mano dall'alto con il telefono e guarda la foto <strong>capovolta</strong>. L'occhio, che si era "abituato" all'unghia, vede subito il lato più largo e la punta fuori centro.</div>
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
<div class="box case"><strong class="t">Caso pratico</strong><p><strong>L'unghia è perfetta da tutte le viste, ma passando il polpastrello verso la cuticola senti un leggero gradino.</strong></p><p>Non è un dettaglio estetico. Un bordo di prodotto spesso alla cuticola forma una piccola cresta: l'unghia naturale flette, la cresta no, e il prodotto comincia a staccarsi proprio da lì. È una delle cause più comuni di sollevamento alla base. Sfuma con un buffer fine finché il polpastrello passa dalla lamina al prodotto senza accorgersene, e controlla che non ci sia prodotto a contatto con la pelle. Se il gradino è spesso, chiediti perché: perla troppo grande in zona 3 o prodotto troppo vicino alla cuticola.</p></div>
`,
          sources: ['https://open-exam-prep.com/study-guides/ks-nail-technician/nail-enhancements/nail-sculpting-forms',
            'https://www.scratchmagazine.co.uk/blog/simply-salon-nails-perfecting-proper-nail-structure/',
            'https://www.scratchmagazine.co.uk/wp-content/uploads/2026/01/Nailympia-2026-Scoresheet_French-Twist-3-shape-challenge.pdf', 'https://www.katiebarnesacademy.com/blogs/nail-structure-application/understanding-apex-placement-for-different-nail-shapes', 'https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-file-the-lower-arch-and-side-walls-without-removing-too-much', 'https://katiebarnesacademy.com/blogs/nail-structure-application/how-to-deal-with-nail-service-breakdown']
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
<div class="box deep"><strong class="t">Approfondimento: perché il bianco è il colore più difficile</strong><p>Il pigmento bianco principale è il <strong>biossido di titanio</strong>. Riflette moltissima luce, e per questo:</p><ul><li><strong>Mostra ogni difetto:</strong> una piccola differenza di spessore cambia il riflesso e diventa una riga visibile. Sui colori scuri lo stesso difetto quasi non si vede.</li><li><strong>Si deposita:</strong> nel vasetto il pigmento scende verso il fondo; un bianco non mescolato dà strisce e grumi.</li><li><strong>Blocca la luce:</strong> uno strato spesso sembra duro in superficie ma sotto resta morbido, e poi si raggrinzisce.</li></ul><p>Non tutti i bianchi sono uguali: i bianchi da french sono spesso un po' traslucidi e vanno usati in modo diverso da un bianco coprente da nail art.</p></div>
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
<div class="box pro"><strong class="t">Consiglio da professionista</strong><ul><li><strong>Mescola il bianco</strong> con una spatolina prima di iniziare, soprattutto se il vasetto è fermo da giorni.</li><li>Usa la <strong>mano leggera</strong>: premere sul pennello crea micro-righe che rendono il bianco opaco e "gessoso".</li><li>Lascia che il gel si autolivelli: non ripassare tre volte nello stesso punto.</li><li>Polimerizza completamente ogni strato sottile prima del successivo.</li><li>Se cambi marca di bianco, rifai prove su tip: pigmento, densità e fotoiniziatori cambiano, e con loro il comportamento sotto la tua lampada.</li></ul></div>
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
<div class="box pro"><strong class="t">Consiglio da professionista: french in acrilico</strong><ul><li>Il bianco deve avere una consistenza "<strong>da argilla</strong>": una perla bagnata scivola giù dalla cartina curva.</li><li>Dopo aver preso la perla aspetta qualche secondo, poi tampona il dorso del pennello su carta per togliere il liquido in eccesso.</li><li>Appoggia la perla vicino alla smile, distribuiscila dall'alto e usa il <strong>fianco</strong> del pennello per "rimboccare" il bianco fino alla linea, senza superarla.</li><li>Per il rosa di sopra, una perla di circa metà del letto: con il dito della cliente rivolto verso il basso, accompagnala lungo il bordo perché la smile prenda una forma a goccia.</li><li>Controlla di lato che i fianchi siano dritti e non ad artiglio. Piccole irregolarità si correggono poi con la lima.</li></ul></div>
<div class="box case"><strong class="t">Caso pratico</strong><p><strong>Cliente con il bordo libero naturale storto: su un lato la linea bianca naturale arriva molto più in basso.</strong></p><p>Se segui la linea naturale, la smile sarà storta. La smile si disegna rispetto all'<strong>asse del dito</strong> e all'altezza decisa per tutta la mano, non rispetto al bordo naturale. Sul lato dove il letto è più corto, prolunga il letto con il cover fino all'altezza dei punti laterali; sul lato più lungo la smile coprirà semplicemente un po' di letto. Controlla controluce che il cover sotto sia uniforme: se resta una zona trasparente si vedrà la vecchia linea "fantasma" sotto il bianco.</p></div>
`,
          sources: ['https://www.scratchmagazine.co.uk/feature/how-to-create-a-crisp-smile-line-with-the-gel-system',
            'https://www.scratchmagazine.co.uk/nail_art/classic-french-manicure-using-gel',
            'https://www.scratchmagazine.co.uk/nail_art/how-to-perfect-a-french-tip',
            'https://www.opi.com/professionals/gelcolor-french-manicure-application',
            'https://www.salongeek.com/threads/how-do-you-do-your-smile-line-using-gel.86701/',
            'https://nailknowledge.org/blog/uv-curing-why-thin-layers-matter-for-perfect-nails', 'https://nailknowledge.org/blog/why-white-gel-polish-looks-patchy', 'https://www.youngnails.com/blogs/news/how-to-do-french-tips', 'https://www.salongeek.com/threads/camouflage-gel.60825/']
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
<div class="box deep"><strong class="t">Approfondimento: perché il reverse si solleva più facilmente</strong><p>Il reverse french porta il colore nella zona dove il prodotto è più sottile e dove nasce la maggior parte dei sollevamenti, cioè vicino alla cuticola. I sollevamenti alla base compaiono spesso entro <strong>5–7 giorni</strong> e hanno tre cause tipiche:</p><ul><li>residui di pterigio (la pellicina attaccata alla lamina) non tolti in preparazione;</li><li>base o colore che "allagano" la cuticola;</li><li>crema o olio sul bordo della piega prossimale.</li></ul><p>Per questo, nel reverse, la preparazione della zona cuticolare va fatta con ancora più cura, si sgrassa anche la piega prima del primer e si rispetta il margine dalla pelle (circa 1 mm).</p></div>
<h2>V-french in tre mosse</h2>
<ol class="steps">
<li>Segna il <strong>punto centrale</strong> della V.</li>
<li>Traccia una linea dritta da un lato al punto centrale, poi dall'altro lato con la <strong>stessa inclinazione</strong>.</li>
<li>Riempi verso la punta, sigilla il bordo libero, top.</li>
</ol>
${B('tip', 'Allenati su tip', 'Disegna 10 V-french e 10 reverse su una ruota di tip prima di proporli: confronta le unghie a coppie e cerca la stessa misura.')}
<div class="box pro"><strong class="t">Consiglio da professionista: il nastro guida</strong><p>Per le prime V-french puoi usare lo <strong>striping tape</strong> (nastro adesivo sottilissimo) come guida:</p><ol><li>Il colore di fondo deve essere completamente polimerizzato (e senza strato appiccicoso), altrimenti il nastro lo strappa.</li><li>Applica due pezzi di nastro a V e premili bene ai bordi, perché il colore non passi sotto.</li><li>Stendi il colore della V e togli il nastro <strong>subito</strong>, prima della lampada: se polimerizzi con il nastro sopra, il gel indurito si strappa insieme al nastro.</li><li>Sistema il bordo con un pennello pulito, polimerizza e sigilla con il top.</li></ol><p>Con l'esperienza passerai al pennello liner, più veloce e più preciso.</p></div>
<div class="box case"><strong class="t">Caso pratico</strong><p><strong>Quale variante proporre?</strong></p><ul><li><strong>Cliente con unghie corte e letto corto:</strong> micro french. La linea sottilissima sta solo sul bordo e lascia "rosa" quasi tutta l'unghia, che sembra più lunga.</li><li><strong>Cliente con dita corte e forma mandorla:</strong> V-french. Le due linee oblique seguono la chiusura dei lati e allungano visivamente il dito.</li><li><strong>Cliente con unghie larghe e quadrate:</strong> evita una smile piatta molto larga, che allarga ancora di più. Una smile più profonda, o una V poco accentuata, restringe visivamente.</li><li><strong>Cliente con cuticole irregolari o pterigio evidente:</strong> sconsiglia il reverse finché la zona cuticolare non è in ordine: il colore lì metterebbe in evidenza ogni difetto.</li></ul></div>
`,
          sources: ['https://www.opi.com/nail-art/glow-with-the-flow',
            'https://www.opi.com/professionals/gelcolor-french-manicure-application',
            'https://www.scratchmagazine.co.uk/feature/how-to-reverse-french-using-halos-polibuild',
            'https://www.design4nails.co.uk/?p=285413', 'https://semilac.co.uk/blogs/news/gel-lifting-and-yellowing-root-causes-and-salon-floor-fixes', 'https://katiebarnesacademy.com/blogs/nail-structure-application/how-to-deal-with-nail-service-breakdown', 'https://www.lulus.com/blog/guest-blogger/manicure-monday-chevron-nail-tutorial/', 'https://www.opi.com/blog/tutorialtuesday-light-blue-chevron', 'https://www.scratchmagazine.co.uk/feature/how-to-create-a-crisp-smile-line-with-the-gel-system']
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
<div class="box pro"><strong class="t">Consiglio da professionista: baby boomer in acrilico "a zone"</strong><ol><li>Posa una perla di cover nella zona cuticolare e sfumala verso il centro.</li><li>Posa una perla di bianco sulla punta e sfumala verso il centro dell'unghia.</li><li>Aggiungi al centro una <strong>perla piccola, appena più umida</strong>: ammorbidisce il punto d'incontro tra i due colori.</li><li>Modella quasi tutta la forma con il pennello. Ogni passata di lima in più "taglia" la sfumatura.</li></ol><p>Il segreto è che le due perle si incontrino quando sono ancora lavorabili: lavora un'unghia alla volta.</p></div>
<h2>Passo passo in gel builder</h2>
${F('baby-boomer-step.svg', 'Baby boomer in gel: bianco sulla punta, sfuma verso il centro, cover sopra con apex, top.')}
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
<div class="box deep"><strong class="t">Approfondimento: perché il bianco lattiginoso sfuma meglio</strong><p>Un bianco coprente ha molto biossido di titanio: riflette tanta luce, quindi ogni variazione di spessore diventa un "gradino" visibile. Un bianco <strong>lattiginoso</strong> ha meno pigmento e lascia passare parte della luce: nel passaggio verso il cover lo spessore cambia gradualmente e l'occhio vede una sfumatura invece di una linea.</p><p>C'è anche un vantaggio tecnico: meno pigmento significa che la luce della lampada arriva meglio in profondità. Anche così, tieni gli strati sottili e polimerizza completamente ognuno prima di coprirlo con il cover.</p></div>
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
<div class="box case"><strong class="t">Caso pratico</strong><p><strong>Al refill la cliente con baby boomer ha una fascia di ricrescita e la sfumatura è salita di 3 mm verso la punta.</strong></p><p>Assottiglia il vecchio prodotto seguendo il profilo e decidi: se la sfumatura è ancora nella metà alta dell'unghia, basta stendere il cover sulla ricrescita, sfumandolo sul vecchio, e rifare l'apex sopra il punto di stress. Se la parte bianca si è spostata troppo e l'unghia sembra un french sbavato, va rifatta la sfumatura (come un backfill): togli parte del vecchio bianco, riposa il bianco lattiginoso e ricostruisci. Calcola più tempo e annotalo, così al prossimo appuntamento lo prenoti già come servizio lungo.</p></div>
`,
          sources: ['https://pinkgellac.com/blogs/news/baby-boomer-nails',
            'https://salongeek.com/threads/baby-boomer-nails.323883',
            'https://onglesdor.com/en/blog/make-your-babyboomer-with-oh-blush-gel-and-powder.html', 'https://nailknowledge.org/blog/why-white-gel-polish-looks-patchy', 'https://nailknowledge.org/blog/mastering-uv-gel-application-insights-into-pigments', 'https://www.opi.com/professionals/how-to-rebalance-and-fill-opi-gelevate-overlay-services']
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
<div class="box deep"><strong class="t">Approfondimento: decorazioni che fanno ombra</strong><p>Foglia metallica, glitter grossi, strass e carta <strong>non lasciano passare la luce</strong> della lampada. Il gel che sta sotto una decorazione opaca può restare poco polimerizzato: è lo stesso "effetto ombrello" dei pigmenti, solo più forte.</p><ul><li>Polimerizza completamente lo strato su cui appoggi la decorazione <em>prima</em> di posarla.</li><li>Fissala con un velo sottilissimo di prodotto, così la luce lo raggiunge dai bordi.</li><li>Copri con builder trasparente e polimerizza per il tempo pieno.</li></ul><p>Gel non polimerizzato intrappolato sotto una decorazione è una causa nascosta di distacchi e, se arriva alla pelle durante la rimozione, di irritazioni.</p></div>
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
<div class="box pro"><strong class="t">Consiglio da professionista</strong>Metti le decorazioni da incapsulare nella <strong>zona 2 o tra zona 1 e 2</strong>, mai a ridosso della cuticola. In zona 3 il prodotto deve essere sottilissimo: una decorazione lì crea spessore proprio dove nasce il sollevamento, e per coprirla dovresti alzare la base fino a formare una cresta. Se la cliente vuole un dettaglio vicino alla cuticola, usa una decorazione piatta (gel da pittura, stamping) invece di un oggetto in rilievo.</div>
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
<div class="box pro"><strong class="t">Consiglio da professionista: lo stamping che non riesce</strong><ul><li>Su una piastra nuova togli la <strong>pellicola protettiva</strong> blu.</li><li>Pulisci la piastra dopo ogni uso con acetone puro: i solventi con oli lasciano residui, e lo smalto secco nelle incisioni rovina i disegni successivi.</li><li>Usa dischetti piatti o salviette senza pelucchi, non batuffoli di cotone.</li><li><strong>Non pulire il tampone in silicone con l'acetone</strong>: diventa opaco. Usa nastro adesivo o un rullo levapelucchi.</li><li>Movimento leggero e rapido, rotolando: tenere il tampone premuto deforma il disegno.</li><li>Il gel semipermanente comune non è adatto allo stamping: sul tampone forma goccioline e non si trasferisce.</li></ul></div>
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
            'https://www.scratchmagazine.co.uk/nail_art/cat-eye-chrome-nail-art-tutorial/', 'https://nailknowledge.org/blog/mastering-uv-gel-application-insights-into-pigments', 'https://katiebarnesacademy.com/blogs/nail-structure-application/how-to-deal-with-nail-service-breakdown', 'https://www.katiebarnesacademy.com/blogs/nail-structure-application/understanding-apex-placement-for-different-nail-shapes', 'https://maniology.com/blogs/maniology-blog/nail-stamping-not-working-common-mistakes']
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
<div class="box deep"><strong class="t">Approfondimento: misura la ricrescita, non solo i giorni</strong><p>Nello studio di Yaemsiri e colleghi (2010) le unghie delle mani crescevano in media <strong>3,47 mm al mese</strong>; il mignolo più lentamente delle altre dita, e <strong>senza differenze significative tra mano destra e sinistra</strong>. Le medie però nascondono grandi differenze tra persone.</p><p>Abitudine da professionista: al refill misura con il righello o con la griglia di una cartina la fascia di ricrescita del medio e annotala. Se una cliente arriva sempre con 3 mm o più dopo tre settimane, l'apex sarà già fuori posto: proponi un intervallo più breve. Se ne ha 1,5 mm dopo quattro settimane, puoi allungarlo senza rischi.</p></div>
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
<div class="box pro"><strong class="t">Consiglio da professionista: leggere i sollevamenti come una mappa</strong><table><tr><th>Dove</th><th>Quando</th><th>Cause più probabili</th></tr><tr><td>Alla cuticola</td><td>Entro 5–7 giorni, spesso 1–2 dita</td><td>Pterigio non tolto, prodotto sulla pelle, crema o olio sulla piega</td></tr><tr><td>Al bordo libero</td><td>Entro 3–5 giorni, clienti che usano molto le mani</td><td>Bordo non sigillato a ogni strato, sotto della punta non sgrassato, prodotto troppo rigido su lamina flessibile</td></tr><tr><td>Tutta l'unghia in un pezzo</td><td>Variabile</td><td>Primer saltato o ancora umido, opacizzazione saltata</td></tr></table><p>Un trucco veloce: se si solleva soprattutto l'indice della mano dominante, pensa all'uso; se succede su tutte e dieci le dita, il problema è nella procedura.</p></div>
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
<div class="box deep"><strong class="t">Approfondimento: prodotto nuovo su prodotto vecchio</strong>Nel refill il nuovo prodotto si attacca bene al vecchio perché, come dice Doug Schoon, "la plastica aderisce alla plastica". Il problema nasce quando sul vecchio prodotto c'è <strong>un sistema diverso</strong>: marchi diversi possono avere flessibilità diverse, e due materiali che si piegano in modo diverso tendono a separarsi. Se la cliente arriva da un altro salone e non sai che cosa porta, la scelta più sicura è la rimozione completa, oppure assottigliare fino a un velo sottile e ricostruire con il tuo sistema. Annota sempre marca e prodotto sulla scheda: al refill successivo lo sai già.</div>
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
<div class="box case"><strong class="t">Caso pratico</strong><p><strong>Cliente con unghie che crescono in fretta, arriva dopo 4 settimane: l'apex è a metà dell'allungamento e due unghie hanno piccole crepe ai lati.</strong></p><ol><li>Accorcia prima di tutto: meno leva mentre lavori.</li><li>Lima le crepe finché spariscono del tutto.</li><li>Assottiglia il <strong>vecchio apex</strong>: se lasci quello spessore a metà unghia e ne costruisci uno nuovo più indietro, l'unghia diventa pesante in avanti e si rompe di nuovo.</li><li>Ricostruisci l'apex sopra il punto di stress attuale.</li><li>Fissa il prossimo refill a 2–3 settimane e spiega il perché alla cliente: non è per vendere di più, è perché le sue unghie crescono più veloci della media.</li></ol></div>
`,
          sources: ['https://www.opi.com/professionals/how-to-rebalance-and-fill-opi-gelevate-overlay-services',
            'https://katiebarnesacademy.com/blogs/nail-structure-application/how-to-deal-with-nail-service-breakdown',
            'https://nailknowledge.org/?p=49737',
            'https://bionumbers.hms.harvard.edu/bionumber.aspx?id=112380',
            'https://dilei.it/bellezza/cose-e-quanto-costa-il-refill-delle-unghie-in-gel/637264/',
            'https://booksolo.co/nailedbyalire/aftercare', 'https://hero.epa.gov/hero/index.cfm/reference/details/reference_id/7330295', 'https://semilac.co.uk/blogs/news/gel-lifting-and-yellowing-root-causes-and-salon-floor-fixes', 'https://nailknowledge.org/?p=44851', 'https://open-exam-prep.com/study-guides/ga-nail-technician/nail-enhancement-chemistry-acrylics/acrylic-maintenance-removal']
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
<div class="box deep"><strong class="t">Approfondimento: dove si rompe dice perché si rompe</strong><table><tr><th>Che cosa vedi</th><th>Causa da verificare</th></tr><tr><td>Crepa trasversale sopra il punto di stress</td><td>Zona 2 troppo sottile, apex troppo avanti o "migrato" per il refill in ritardo</td></tr><tr><td>Crepa su un fianco</td><td>Fianchi assottigliati in limatura; forma ristretta già sul dito (ballerina, mandorla)</td></tr><tr><td>Scheggiature sul bordo libero</td><td>Bordo non sigillato, zona 1 troppo sottile, forma con angoli netti su chi usa molto le mani</td></tr><tr><td>Sacca d'aria al centro (pocket lifting)</td><td>Preparazione, primer, polimerizzazione insufficiente</td></tr></table><p>Annota il tipo di rottura sulla scheda: tre crepe uguali sullo stesso dito non sono "sfortuna", sono un messaggio sulla struttura.</p></div>
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
<div class="box pro"><strong class="t">Consiglio da professionista</strong><ul><li>Ripara con <strong>lo stesso sistema</strong> con cui hai costruito: due prodotti con flessibilità diverse si separano proprio sulla linea della riparazione.</li><li>Molte educatrici <strong>polimerizzano i pollici a parte</strong>, ben dritti sotto la lampada: nella posizione con le quattro dita il pollice spesso resta inclinato e riceve meno luce.</li><li>Se la riparazione riguarda il fianco, ricostruisci il fianco intero fino al solco, non solo la parte crepata: un "rattoppo" piccolo crea un nuovo punto di debolezza sul suo bordo.</li></ul></div>
<div class="box case"><strong class="t">Caso pratico</strong><p><strong>Cliente impiegata, destrimane, rompe sempre l'indice destro, di solito sull'angolo esterno.</strong></p><p>Un problema concentrato sull'indice della mano dominante fa pensare all'<strong>uso</strong> più che alla tecnica (se fosse la tecnica, i problemi sarebbero su più dita). Chiedi: apre lattine, scatole o tasti dell'auto con quell'unghia? Batte sulla tastiera con le punte? Soluzioni: su quel dito angoli più arrotondati (squoval invece di quadrata), 1 mm in meno di lunghezza, fianco esterno costruito pieno. E un consiglio pratico: usare il polpastrello, non l'unghia, per aprire e premere. Annota se la soluzione funziona al refill successivo.</p></div>
`,
          sources: ['https://katiebarnesacademy.com/blogs/nail-structure-application/how-to-deal-with-nail-service-breakdown',
            'https://nailknowledge.org/?p=49737', 'https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-fit-nail-forms-to-different-nail-shapes', 'https://semilac.co.uk/blogs/news/gel-lifting-and-yellowing-root-causes-and-salon-floor-fixes', 'https://nailknowledge.org/?p=44851']
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
<div class="box deep"><strong class="t">Approfondimento: perché alcuni prodotti si sciolgono e altri no</strong><p>Quando un gel polimerizza, le molecole si collegano tra loro formando una rete. Nei gel <strong>soak-off</strong> (soft gel) questa rete è più "aperta": le piccole molecole di acetone riescono a entrare, la rete si gonfia e si ammorbidisce. Negli <strong>hard gel</strong> la rete è molto più fitta e il solvente non entra: per questo sono più resistenti ma vanno limati.</p><ul><li>Molti semipermanenti hanno un <strong>top più duro</strong>: se non lo opacizzi, l'acetone fatica a passare.</li><li>Nei sistemi a immersione (dip) la polvere riempie gli spazi della rete e la rimozione è più lenta.</li></ul></div>
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
${B('warn', 'Acetone: sicurezza', 'L\'acetone è molto infiammabile: usane poco, in un contenitore chiuso, lontano da fiamme e fonti di calore, con la stanza ben ventilata. Non metterlo mai su fonti di calore dirette (piastre, scaldini, microonde). Non usarlo su pelle ferita o irritata.')}
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
<div class="box case"><strong class="t">Caso pratico</strong><p><strong>Nuova cliente da un altro salone, non sa che prodotto ha.</strong></p><p>Usa il tempo di ammorbidimento come indizio:</p><ul><li>Gel soak-off: si ammorbidisce in genere in <strong>10–20 minuti</strong>.</li><li>Acrilico (EMA): in genere intorno ai <strong>30 minuti</strong>.</li><li>Nessun cambiamento dopo il tempo previsto: probabilmente <strong>hard gel</strong>, da limare.</li><li>Prodotto durissimo, che dopo molto tempo in acetone resta quasi invariato, spesso con odore forte: può essere un acrilico a base di <strong>MMA</strong>. Si rimuove con la lima, con molta cautela, perché aderisce in modo aggressivo alla lamina.</li></ul><p>Rimuovere il lavoro di un'altra persona richiede tempo: prevedilo nel prezzo e chiedi già al telefono che cosa porta la cliente.</p></div>
<h2>Dopo la rimozione</h2>
<ul>
<li>Guarda la lamina: se è sottile, dolente o con macchie, valuta una <strong>pausa</strong> o un servizio leggero, e annotalo.</li>
<li>Consiglia olio per cuticole ogni giorno per qualche settimana.</li>
<li>Se ci sono segni di infezione o distacco dal letto, consiglia il medico.</li>
</ul>
<div class="box pro"><strong class="t">Consiglio da professionista: il test della goccia d'acqua</strong>Dopo la rimozione la lamina può apparire bianca e opaca. Per capire se è solo disidratazione o un danno, metti una <strong>goccia d'acqua</strong> sulla zona bianca. Se il bianco sparisce, è disidratazione superficiale: la superficie resta più asciutta per circa 30–40 minuti e si reidrata del tutto in qualche ora. Se il bianco resta, la causa è un danno meccanico (graffi, strati di lamina sollevati) o residui di prodotto. Mostra il test alla cliente: capisce subito la differenza tra "l'acetone mi ha rovinato le unghie" e una rimozione fatta male.</div>
`,
          sources: ['https://nailknowledge.org/blog/does-acetone-affect-the-natural-nail',
            'https://karanailedit.substack.com/p/how-to-remove-your-gel-safely',
            'https://onglesdor.com/en/shellac-remover-wraps-10-unit.html',
            'https://nailknowledge.org/?p=49737',
            'https://www.marionnaud.it/m-life/tutorial/come-togliere-unghie-gel', 'https://nailknowledge.org/glossary/soak-off-gels', 'https://nailknowledge.org/?p=52939']
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
<div class="box deep"><strong class="t">Approfondimento: perché l'acqua stacca il prodotto</strong> <p>La lamina non è un materiale fermo: contiene normalmente circa il 15–18% di acqua. In ammollo ne assorbe molta già in circa un minuto e può arrivare al 25–30%. L'acqua si infila tra gli strati di cheratina, li allontana e la lamina si gonfia e cambia forma.</p> <p>Se applichi il prodotto su una lamina gonfia, quando l'unghia si asciuga e torna alla sua forma il rivestimento resta "tirato" su una superficie che si è ristretta: compaiono crepe, scheggiature e sollevamenti. Le lamine sottili e flessibili sono le più colpite; quelle spesse e sane quasi non ne risentono. Un normale lavaggio delle mani (circa 20 secondi) invece non crea problemi.</p> <ul><li>Prima di una ricostruzione lavora <strong>a secco</strong>: niente ammollo.</li> <li>Se la cliente arriva dalla piscina o ha appena lavato i piatti, aspetta qualche minuto prima di applicare.</li> <li>Mani spesso in acqua + lamina sottile = scegli un prodotto più flessibile e strati sottili.</li></ul></div>
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
<div class="box case"><strong class="t">Caso pratico</strong> <p>Martina torna dopo 10 giorni: su tre dita il gel si è staccato <strong>al centro</strong>, a "bolla", ma i bordi alla cuticola e ai lati sono ancora sigillati.</p> <p><strong>Ragionamento.</strong> Centro staccato e bordi integri: il margine dalla pelle non è il problema. Le ipotesi principali sono due: un urto o una pressione (anche senza sollevamenti visibili ai bordi, un colpo può separare il prodotto dalla lamina) oppure una lamina molto flessibile che si piega mentre il prodotto rigido non la segue. Con l'acrilico va aggiunta una perla troppo bagnata: asciugando, il prodotto si ritira e "tira" verso l'alto.</p> <p><strong>Domande da fare:</strong> lavori alla tastiera? Apri lattine o scatole con le unghie? Hai preso un colpo?</p> <p><strong>Soluzione.</strong> Lima via tutto il prodotto staccato e controlla sotto: umidità, macchie verdi o bianche vanno fatte vedere al medico. Se la lamina è sana, ricostruisci con un prodotto più flessibile e una lunghezza minore, e annota il caso sulla scheda.</p></div>
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
<div class="box pro"><strong class="t">Consiglio da professionista</strong> <p>Tre errori di preparazione che non si vedono a occhio nudo:</p> <ul><li><strong>Ricontaminazione.</strong> Una lamina perfetta si sporca di nuovo se lavori lentamente, se la cliente si tocca viso o capelli, se una cartina scivola. Prepara e applica <strong>una mano alla volta</strong>.</li> <li><strong>Troppa opacizzazione.</strong> La lamina è spessa in media circa 0,38 mm. Togliere troppo materiale la rende instabile e più sensibile al calore. Serve solo togliere la lucentezza.</li> <li><strong>Troppo primer.</strong> Un primer "abbondante" allaga la lamina, non aumenta l'adesione e aumenta il rischio di irritazioni e allergie. Usa la quantità indicata dal produttore e usa primer e base dello stesso sistema.</li></ul> <p>Infine: un sollevamento tagliato con la tronchesina crea un nuovo punto di distacco. Si lima, sempre.</p></div>
`,
          sources: ['https://nailknowledge.org/?p=49737',
            'https://katiebarnesacademy.com/blogs/nail-structure-application/how-to-deal-with-nail-service-breakdown',
            'https://www.design4nails.co.uk/?p=285413',
            'https://semilac.co.uk/blogs/news/gel-lifting-and-yellowing-root-causes-and-salon-floor-fixes',
            'https://purespadirect.com/blogs/pure-spa-direct-blog/gel-polish-lifting-troubleshooting-20-causes-prep-lamps-products-and-client-habits-a-nail-tech-39-s-guide-to-perfect-manicures', 'https://nailknowledge.org/blog/water-vs-waterless-manicures']
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
<div class="box deep"><strong class="t">Approfondimento: perché l'apex protegge</strong> <p>Il bordo libero funziona come una <strong>leva</strong>: una forza sulla punta (un urto, una pressione) fa piegare l'unghia soprattutto nel punto in cui il bordo lascia il dito. Più l'unghia è lunga, più la leva è forte.</p> <p>L'apex mette lo spessore proprio sopra quella zona. Un arco costruito bene sale in modo graduale dalla cuticola all'apex e poi scende o va dritto verso la punta: così bordo libero e lati possono restare sottili come una carta di credito senza rompersi. Una struttura troppo piatta, invece, si crepa nella zona di stress e lungo i lati.</p> <ul><li>Un tip troppo piccolo indebolisce i lati: meglio un tip più largo, poi stretto con la lima.</li> <li>Riparare una crepa con un "grumo" di prodotto non basta: la flessione si concentra lì e l'unghia si rompe di nuovo. Lima fino a eliminare la crepa e ricostruisci l'apex.</li> <li>L'apex si sposta con la crescita: per questo il refill puntuale è parte della riparazione.</li></ul></div>
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
<div class="box deep"><strong class="t">Approfondimento: perché "entrare piano" in lampada riduce il calore</strong> <p>Il calore dipende da <strong>quanto velocemente</strong> avvengono le reazioni. Se la mano entra lentamente in lampada, o resta per qualche secondo appena fuori dall'apertura, al prodotto arriva meno luce UV: la reazione parte più piano e il calore si distribuisce nel tempo. È come il flash di una macchina fotografica: più sei lontana, meno luce ti arriva. Le lampade con modalità <em>low heat</em> fanno la stessa cosa in automatico, con un avvio a bassa potenza.</p> <p><strong>Attenzione:</strong> dopo una partenza "morbida" la mano va rimessa in posizione normale per tutto il tempo di polimerizzazione indicato. Un gel non polimerizzato del tutto si rovina prima e aumenta il rischio di allergia.</p> <p>Anche i gel <em>no-wipe</em> (senza strato appiccicoso) tendono a scaldare di più: con questi prodotti gli strati sottili sono ancora più importanti.</p></div>
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
<div class="box case"><strong class="t">Caso pratico</strong> <p>Giulia dice che "brucia solo il pollice, e solo al refill". Alla prima applicazione non sentiva niente.</p> <p><strong>Ragionamento.</strong> Il pollice ha la superficie più grande e riceve più prodotto. Al refill, per riportare l'apex al suo posto si tende a stendere il builder in un unico strato spesso. In più la zona di ricrescita è lamina naturale, forse assottigliata dalla preparazione o da una rimozione precedente. D'estate il problema peggiora: con il caldo il gel è più fluido e i picchi di calore sono più frequenti.</p> <p><strong>Soluzione.</strong></p> <ul><li>Costruisci l'apex in <strong>due passate sottili</strong>, polimerizzando tra una e l'altra.</li> <li>Polimerizza il pollice da solo, partendo con la modalità low heat o con la mano appena fuori dalla lampada.</li> <li>Sulla ricrescita: solo opacizzazione leggera, niente lime grosse.</li> <li>Annota sulla scheda "pollice sensibile al calore": al prossimo refill parti già così.</li></ul></div>
`,
          sources: ['https://nailknowledge.org/?p=44956',
            'https://scratchmagazine.co.uk/feature/heat-spikes-in-gel-nail-services-why-they-happen-how-to-avoid-them',
            'https://www.nsinails.com.au/blogs/news/understand-nail-damages-heat-spikes-lifting-issues',
            'https://nailknowledge.org/blog/uv-curing-why-thin-layers-matter-for-perfect-nails', 'https://www.scratchmagazine.co.uk/blog/simply-salon-nails-perfecting-proper-nail-structure/', 'https://purenails.co.uk/blogs/news/why-cracks-can-appear-in-gel-polish', 'https://www.nailpro.com/technique/article/21156901/how-to-create-durable-nails-with-perfect-structure', 'https://www.scratchmagazine.co.uk/feature/heat-spikes-in-gel-nail-services-why-they-happen-how-to-avoid-them', 'https://nailknowledge.org/nail-knowledge-base/inhibition-layer-and-no-cleanse-gels', 'https://twentypro.co.uk/blogs/news/how-to-work-with-gel-products-in-extreme-temperatures']
        },
        {
          id: 'difetti', simple: "Quasi tutti i difetti di superficie nascono da strati troppo spessi, polimerizzazione incompleta o prodotti e lampade non abbinati. Strati sottili e il sistema giusto risolvono la maggior parte dei problemi.", title: 'Bolle, grinze, ingiallimento', min: 13,
          html: `
${F('problemi.svg', 'Riconosci il difetto.')}
<h2>Perché la luce non arriva in fondo</h2>
<p>La lampada indurisce il gel dall'alto verso il basso. I <strong>pigmenti</strong> (soprattutto colori scuri, bianco e glitter) fanno da <strong>ombrello</strong>: la superficie riceve tanta luce, gli strati sotto poca. Se lo strato è spesso, sopra si forma una "pelle" dura e sotto resta gel liquido. Allungare il tempo in lampada spesso <strong>non basta</strong>: la soluzione è lo strato sottile.</p>
${F('grinze-sezione.svg', 'Grinza in sezione: superficie dura sopra, gel liquido sotto; con strati sottili la luce arriva in fondo.')}
<div class="box deep"><strong class="t">Approfondimento: lo strato appiccicoso</strong> <p>Dopo la lampada molti gel lasciano una pellicola appiccicosa: è lo <strong>strato di inibizione</strong>. Si forma perché l'ossigeno dell'aria blocca le estremità delle catene che stanno crescendo in superficie. Lì le catene restano corte e lo strato è polimerizzato meno della metà; sotto, dove l'ossigeno non arriva, il gel indurisce normalmente.</p> <ul><li>Un gel che polimerizza in fretta lascia uno strato più sottile; una lampada debole o con lampadine da cambiare lo rende più spesso.</li> <li>I gel <em>no-wipe</em> sono formulati per non lasciare questo strato. In cambio possono scaldare di più, diventare più rigidi con il tempo e contenere ingredienti che irritano la pelle più facilmente.</li> <li>Lo strato appiccicoso è gel non indurito: non va toccato con la pelle. Toglilo con un dischetto con il retro in plastica o con i guanti, non con un batuffolo imbevuto tenuto tra le dita.</li></ul></div>
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
<div class="box deep"><strong class="t">Approfondimento: viscosità, temperatura e bolle</strong> <p>La <strong>viscosità</strong> è la resistenza di un liquido a scorrere. Un gel normale ha circa 25.000–100.000 centipoise (cP); molti builder circa 350.000 cP, alcuni fino a 1.000.000. Più il gel è denso, più trattiene l'aria che ci entra mescolando o premendo il pennello.</p> <p>Il gel è <strong>tissotropico</strong>: mentre lo lavori diventa più fluido, quando ti fermi torna denso. La temperatura cambia tutto:</p> <table><tr><th>Ambiente</th><th>Cosa succede</th><th>Cosa fare</th></tr> <tr><td>Freddo</td><td>Gel rigido, non si autolivella, trattiene bolle</td><td>Scalda il flacone tra le mani o in un panno caldo e umido</td></tr> <tr><td>Caldo</td><td>Gel troppo fluido, invade cuticola e lati; più picchi di calore</td><td>Strati più sottili; stanza fresca; tende contro il sole</td></tr></table> <p>Mai microonde, termosifone o acqua bollente: i gel sono infiammabili. Non metterli nemmeno in frigo: il raffreddamento brusco può alterare la formula. Conservali al fresco e al buio.</p></div>
<h2>Reazioni allergiche: riconoscerle</h2>
<p>Il contatto ripetuto della pelle con prodotto <strong>non polimerizzato</strong> può causare una <strong>dermatite allergica da contatto</strong>. Segnali tipici: prurito, rossore, gonfiore o vescicole intorno all'unghia o sui polpastrelli; a volte compare anche su viso e palpebre (toccati con le dita).</p>
<ol class="steps">
<li>Interrompi il servizio e non applicare altro prodotto.</li>
<li>Rimuovi il prodotto con delicatezza.</li>
<li>Consiglia alla cliente di rivolgersi al medico (dermatologo) e annotalo sulla scheda.</li>
<li>Rivedi la tua tecnica: prodotto sulla pelle, polimerizzazione incompleta, polvere di limatura non polimerizzata.</li>
</ol>
${B('danger', 'Anche tu sei a rischio', 'L\'operatrice tocca prodotti liquidi ogni giorno: guanti in nitrile, niente contatto con la pelle, salviette e pennelli sporchi chiusi in un contenitore. Un\'allergia agli acrilati è per sempre.')}
<div class="box deep"><strong class="t">Approfondimento: HEMA e la regola europea</strong> <p>Il sensibilizzante più frequente nei prodotti per unghie è l'<strong>HEMA</strong> (2-idrossietil metacrilato). In uno studio portoghese su 230 persone con allergia agli acrilati (onicotecniche e clienti) il test era positivo all'HEMA nel 90% dei casi, e spesso anche ad altri acrilati simili. In Europa, tra le persone sottoposte a patch test nel 2019–2020, circa il 2,3% è risultato positivo all'HEMA.</p> <p>Per questo il Regolamento UE 2020/1682 ha stabilito che i prodotti per unghie con HEMA o di-HEMA TMHDC devono riportare <strong>"solo per uso professionale"</strong> e <strong>"può provocare una reazione allergica"</strong>, con applicazione dal 2021.</p> <ul><li>In consulenza chiedi sempre se la cliente usa kit di gel o semipermanente a casa: è una fonte frequente di sensibilizzazione.</li> <li>"HEMA free" non vuol dire "senza acrilati": chi è già allergica può reagire anche ad altri.</li></ul></div>
`,
          sources: ['https://nailknowledge.org/blog/gel-polish-curing',
            'https://nailknowledge.org/blog/uv-curing-why-thin-layers-matter-for-perfect-nails',
            'https://nailknowledge.org/?p=147555',
            'https://support.pinkgellac.com/hc/en-nl/articles/24253249294098-Why-is-my-gel-polish-wrinkling-or-bubbling-and-how-can-I-prevent-this',
            'https://www.scratchmagazine.co.uk/feature/causes-of-bubbles-in-lp-gel-nail-enhancements',
            'https://katiebarnesacademy.com/blogs/nail-structure-application/how-to-deal-with-nail-service-breakdown', 'https://nailknowledge.org/nail-knowledge-base/inhibition-layer-and-no-cleanse-gels', 'https://www.scratchmagazine.co.uk/feature/gel-nails-why-you-need-to-know-about-viscosity/', 'https://twentypro.co.uk/blogs/news/how-to-work-with-gel-products-in-extreme-temperatures', 'https://eur-lex.europa.eu/eli/reg/2020/1682/oj/eng', 'https://repositorio.hospitaldebraga.pt/entities/publication/cc5b7169-4a9d-434b-b973-a05002cb696e', 'https://www.mdedge.com/content/tackling-acrylate-allergy-sticky-truth']
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
<div class="box pro"><strong class="t">Consiglio da professionista</strong> <p>Quando i problemi compaiono "all'improvviso" su molte clienti, cerca cosa è cambiato nel tuo lavoro. Tre controlli che isolano la causa:</p> <ol><li><strong>Prova su cartina.</strong> Stendi il prodotto sospetto su una cartina con lo spessore di sempre, polimerizza e controlla che sia duro anche sotto. Se resta morbido, il problema è la coppia gel–lampada (o le lampadine).</li> <li><strong>Lotto contro lotto.</strong> Se hai aperto un flacone nuovo, prova vecchio e nuovo sulla stessa cliente, uno per mano. La scheda con i lotti serve proprio a questo.</li> <li><strong>Una sola variabile.</strong> Se il problema è su una o due clienti, chiedi cosa fanno con le mani durante la giornata, anche le cose che sembrano irrilevanti. Se è su molte, rivedi la tua procedura passo per passo e cerca il passaggio saltato o cambiato.</li></ol> <p>Distingui sempre l'incidente singolo (un colpo durante le pulizie) dal problema che si ripete.</p></div>
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
<div class="box case"><strong class="t">Caso pratico</strong> <p>Una cliente torna dopo 4 settimane con una <strong>macchia verde</strong> sotto il gel dell'anulare. Ammette di aver incollato a casa un angolo che si era alzato.</p> <p><strong>Che cos'è.</strong> Non è muffa, come si sente dire spesso. Il colore verde è tipico della <em>sindrome dell'unghia verde</em>, un'infezione da batteri (<em>Pseudomonas aeruginosa</em>) che producono pigmenti verdi. Questi batteri crescono nell'umido: lo spazio sotto un prodotto sollevato è l'ambiente ideale. Spesso c'era già un piccolo distacco, un trauma o un problema dell'unghia.</p> <p><strong>Cosa fai.</strong></p> <ul><li>Rimuovi il prodotto senza coprire nulla e senza limare la lamina sotto la macchia.</li> <li>Consiglia il medico; riprendi il servizio solo con l'unghia guarita.</li> <li>Strumenti a sterilizzare, lima e buffer usati nel cestino.</li> <li>Annota sulla scheda: data, dito, sollevamento incollato a casa. Al biglietto dei consigli aggiungi: "mai colla su un'unghia sollevata".</li></ul></div>
<div class="box warn"><strong class="t">Quando il difetto non dipende da te</strong> <p>Alcuni segni sembrano "difetti di lavorazione" ma possono indicare un problema di salute. Non è compito tuo fare la diagnosi, ma devi saperli notare:</p> <ul><li><strong>Puntini a ditale</strong> (pitting) sulla lamina, <strong>macchie giallo-rosate</strong> sotto l'unghia ("a goccia d'olio") e distacco dal letto: possono essere segni di psoriasi ungueale. Nelle casistiche il pitting è il segno più frequente sulle mani.</li> <li>La psoriasi viene spesso scambiata per una micosi, e le due possono esserci insieme (in circa il 18–30% dei casi secondo una revisione).</li> <li>Nella psoriasi un trauma può far comparire nuove lesioni (fenomeno di Koebner): una preparazione aggressiva può peggiorare la situazione.</li></ul> <p>Se vedi questi segni su più unghie, non coprire per "nascondere": consiglia il dermatologo e annota sulla scheda.</p></div>
<h3>Bianco gessoso dopo la rimozione: due possibilità</h3> <table><tr><th></th><th>Granulazioni di cheratina</th><th>Micosi bianca superficiale</th></tr> <tr><td>Quando compare</td><td>Subito dopo aver tolto smalto o gel</td><td>Anche su unghie mai smaltate</td></tr> <tr><td>Dove</td><td>Solo sulle unghie che avevano il prodotto</td><td>Può passare ad altre unghie, spesso con piede d'atleta</td></tr> <tr><td>Aspetto</td><td>Macchie bianche ruvide, in superficie</td><td>Tende ad allargarsi, a ispessire, a sbriciolarsi</td></tr> <tr><td>Evoluzione</td><td>Migliora in settimane, con pausa e olio</td><td>Progredisce</td></tr></table> <p>Le granulazioni nascono quando il prodotto, aderendo agli strati più superficiali della lamina, li porta via durante una rimozione energica. Solo un esame (raschiato o coltura) distingue con certezza le due cose: nel dubbio, niente copertura e consiglio del medico o del podologo.</p>
`,
          sources: ['https://katiebarnesacademy.com/blogs/nail-structure-application/how-to-deal-with-nail-service-breakdown',
            'https://nailknowledge.org/?p=49737', 'https://mdedge.com/content/green-thumbnail', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11047019', 'https://emjreviews.com/wp-content/uploads/2025/01/Nail-Psoriasis-A-Narrative-Review-of-Manifestations-Diagnosis-and-Management.pdf', 'https://doaj.org/article/bf2d5743b618496cbde01a29ede64169', 'https://www.michiganfootdoctors.com/white-toenails-from-nail-polish/']
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
<div class="box pro"><strong class="t">Consiglio da professionista</strong> <p>Le domande chiuse ("Hai allergie?") ricevono risposte veloci e incomplete. Le domande <strong>aperte</strong> fanno emergere le informazioni utili:</p> <ul><li>"Raccontami una tua giornata tipo: cosa fai con le mani?"</li> <li>"Hai mai avuto prurito, rossore o gonfiore dopo un servizio alle unghie, anche anni fa?"</li> <li>"Fai gel o semipermanente a casa con un kit?" (molte persone si sensibilizzano proprio così; per legge i prodotti con HEMA sono "solo per uso professionale").</li> <li>"Come sono andate le tue ultime ricostruzioni? Dove si staccavano?"</li></ul> <p>Chiedi anche le cose che alla cliente sembrano irrilevanti: lavori di casa, sport, hobby, strumenti musicali. Spesso la causa di un problema futuro è lì.</p></div>
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
<div class="box case"><strong class="t">Caso pratico</strong> <p>Laura, cliente da due anni, dice che inizierà la chemioterapia e vuole "tenere le unghie in ordine".</p> <p><strong>Cosa sapere.</strong> Alcuni farmaci antitumorali, in particolare i taxani, causano spesso alterazioni delle unghie (secondo una meta-analisi, circa il 35–44% dei pazienti): distacco dal letto, fragilità, infezioni intorno all'unghia. Le revisioni mediche raccomandano di evitare traumi ripetuti da manicure e unghie artificiali; una fonte dermatologica consiglia di rimuovere gel e ricostruzioni durante la terapia.</p> <p><strong>Cosa fai.</strong></p> <ul><li>Proponi di rimuovere la ricostruzione con delicatezza e di passare a unghie corte, tagliate dritte.</li> <li>Niente taglio delle cuticole, niente remover con acetone; olio e crema ogni giorno.</li> <li>Qualsiasi altro servizio solo dopo aver chiesto al team oncologico.</li> <li>Annota sulla scheda la terapia, la data e i consigli dati.</li></ul> <p>Rinunciare alla ricostruzione non vuol dire perdere la cliente: una manicure delicata e la tua attenzione in un momento difficile creano un legame forte.</p></div>
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
${B('warn', 'Foto e social: casi reali', 'Nel 2024 il Garante privacy ha sanzionato con 8.000 euro un centro di medicina estetica per un video su Instagram che mostrava un paziente senza un consenso specifico. Nel 2026 la Cassazione (ord. n. 25117, caso di foto scattate a una cliente in un centro estetico) ha chiarito che il consenso non si ricava dalla firma di un contratto o di un piano dei trattamenti: deve essere specifico, libero e ben distinguibile, e tocca al centro dimostrarlo. Regola pratica: niente foto senza un consenso separato, e mai volti o tatuaggi riconoscibili senza autorizzazione.')}
<h2>Consenso informato al servizio</h2>
<p>Non abbiamo trovato una norma nazionale che imponga all'onicotecnica un modulo specifico di "consenso informato". È però <strong>buona prassi</strong>: spiega per iscritto rischi e limiti (possibili allergie, sollevamenti, necessità di refill, rimozione in salone) e fai firmare. In ambito estetico i giudici chiedono informazioni <strong>personalizzate</strong>, non frasi generiche.</p>
${B('danger', 'Quando dire di no', 'Infezioni, micosi sospette, ferite aperte, unghia staccata dal letto, reazione allergica in corso: il servizio si rifiuta, si spiega il perché, si consiglia il medico e si annota sulla scheda.')}
<div class="box warn"><strong class="t">Cliente già allergica agli acrilati</strong> <p>Se la cliente racconta una reazione passata (vescicole, prurito, gonfiore intorno all'unghia o sulle palpebre) o ha un patch test positivo, <strong>non proporre</strong> gel, semipermanente, acrilico o polygel, nemmeno "HEMA free".</p> <ul><li>L'allergia agli acrilati non passa: ogni nuova esposizione può dare reazioni più forti.</li> <li>Nello studio portoghese su 230 casi, oltre all'HEMA molte persone reagivano anche ad altri acrilati (per esempio l'HPMA, positivo nel 64%): cambiare marchio non basta.</li> <li>Un'alternativa è lo smalto tradizionale, ma solo dopo il parere del dermatologo.</li></ul> <p>Scrivi sulla scheda l'allergia, la fonte dell'informazione (racconto o referto) e i servizi che hai sconsigliato. Ricorda alla cliente di segnalarla anche ad altri professionisti: gli acrilati si trovano anche in materiali dentali e medici.</p></div>
`,
          sources: ['https://www.garanteprivacy.it/garante/doc.jsp?ID=9983210',
            'https://www.eutekne.info/Sezioni/Art_1121522_il_consenso_al_trattamento_dei_dati_non_necessari_all_esecuzione.aspx',
            'https://www.quotidianopiu.it/dettaglio/16439364/consenso-alle-foto-in-centro-estetico-la-firma-non-basta',
            'https://www.garanteprivacy.it/it/registro-delle-attivita-di-trattamento',
            'https://www.studiocataldi.it/articoli/40267-registro-attivita-di-trattamento-chi-deve-redigerlo.asp',
            'https://www.studiocataldi.it/articoli/46336-consenso-informato-piu-stringente-per-i-trattamenti-estetici.asp',
            'https://www.noze.it/insights/gdpr-dati-sanitari-art9/', 'https://katiebarnesacademy.com/blogs/nail-structure-application/how-to-deal-with-nail-service-breakdown', 'https://eur-lex.europa.eu/eli/reg/2020/1682/oj/eng', 'https://altmeyers.org/en/dermatology/chemotherapy-and-nails-156029', 'https://www.em-consulte.com/article/1742394/figures/nail-toxicity-associated-with-anticancer-agents', 'https://pmc.ncbi.nlm.nih.gov/articles/9262963', 'https://repositorio.hospitaldebraga.pt/entities/publication/cc5b7169-4a9d-434b-b973-a05002cb696e', 'https://www.mdedge.com/content/tackling-acrylate-allergy-sticky-truth']
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
<div class="box deep"><strong class="t">Approfondimento: perché l'olio funziona</strong> <p>Gli oli per cuticole, come jojoba o avocado, non arrivano in profondità nella lamina, ma con applicazioni ripetute entrano negli <strong>strati superficiali</strong>. Negli studi di Doug Schoon la vitamina E sciolta in questi oli è penetrata lentamente nella lamina, concentrandosi vicino alla superficie: l'olio fa da "veicolo".</p> <p>La lamina invece assorbe acqua molto in fretta e si gonfia; quando si asciuga si restringe. Questo "su e giù" continuo stressa l'adesione del prodotto, soprattutto alla cuticola.</p> <p><strong>In pratica:</strong> conta la <strong>regolarità</strong>, non la quantità. Una goccia al giorno, tutti i giorni, funziona meglio di tanto olio una volta alla settimana. Il momento più facile da ricordare: la sera, dopo l'ultima volta che ci si lava le mani.</p></div>
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
<div class="box case"><strong class="t">Caso pratico</strong> <p>Sara fa la parrucchiera. Le sue ricostruzioni si sollevano sempre alla cuticola dopo circa 10 giorni.</p> <p><strong>Ragionamento.</strong> Mani in acqua per ore, shampoo, prodotti chimici e il calore del phon: la lamina si gonfia e si asciuga molte volte al giorno, e la pelle intorno si secca. Il sollevamento parte dalla zona più sottile e più vicina alla pelle.</p> <p><strong>Il piano, scritto sul biglietto:</strong></p> <ul><li>Guanti in nitrile per colori, decolorazioni e lavaggi.</li> <li>Olio ogni sera, crema mani dopo il lavoro.</li> <li>Lunghezza corta e refill ogni 3 settimane invece di 4.</li></ul> <p><strong>Dalla tua parte:</strong> zona della cuticola sottilissima, margine di circa 1 mm, base o builder più flessibile. Al refill successivo confronta le foto: se il sollevamento è diminuito, sai che la strada è giusta.</p></div>
<div class="box info"><strong class="t">"Le unghie devono respirare?" No</strong> <p>È una delle domande più frequenti. La lamina non respira: è fatta di cellule morte e non ha bisogno di aria. La matrice, cioè la parte viva che produce l'unghia, riceve l'ossigeno dal sangue. Anche sotto smalto e gel piccole molecole come acqua e ossigeno passano lentamente: l'unghia non "soffoca". Le scritte "traspirante" sugli smalti, secondo il chimico Doug Schoon, non sono dimostrate.</p> <p>Perché allora alcune clienti dicono di stare meglio dopo una pausa? Di solito perché in quel periodo usano l'olio e non subiscono rimozioni. Una pausa ha senso quando l'unghia cambia colore o spessore o appare danneggiata: allora si valuta, e si consiglia il medico se serve.</p> <p>Il vero danno quasi sempre viene da <strong>rimozioni fatte male</strong> (strappare, raschiare, limare la lamina), non dal prodotto in sé.</p></div>
`,
          sources: ['https://booksolo.co/nailedbyalire/aftercare',
            'https://katiebarnesacademy.com/blogs/nail-structure-application/how-to-deal-with-nail-service-breakdown',
            'https://nailknowledge.org/?p=49737', 'https://nailknowledge.org/blog/2024/02/22', 'https://nailknowledge.org/blog/water-vs-waterless-manicures', 'https://nailknowledge.org/nail-knowledge-base/so-do-nails-breathe', 'https://nailknowledge.org/blog/do-nails-need-to-breathe', 'https://www.michiganfootdoctors.com/white-toenails-from-nail-polish/']
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
<div class="box pro"><strong class="t">Consiglio da professionista</strong> <ul><li><strong>Temperatura colore.</strong> La luce del giorno è tra circa 5.000 e 6.200 K (kelvin). Sotto i 5.000 K i colori tirano al giallo-rosso, sopra diventano più freddi e azzurri. Quando compri una lampada, controlla i kelvin sulla confezione.</li> <li><strong>Più di una fonte di luce.</strong> Un anello luminoso da solo non basta: affiancalo a una finestra o a una lampada. La luce da più direzioni elimina le ombre che scuriscono i colori e spengono i glitter.</li> <li><strong>Il riflesso.</strong> L'anello luminoso disegna un cerchio sull'unghia che la fa sembrare più spessa. Inclinalo finché il riflesso diventa una linea sottile o un ovale allungato.</li> <li><strong>Il telefono.</strong> Pulisci l'obiettivo, non zoomare oltre 2x (meglio ritagliare dopo), tocca lo schermo per mettere a fuoco, niente flash.</li> <li><strong>Sole diretto e neon:</strong> evitali. Meglio lavorare all'ombra, con luce diffusa.</li></ul></div>
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
<div class="box pro"><strong class="t">Consiglio da professionista</strong> <p>Per un portfolio riconoscibile, scegli <strong>una o due pose</strong> e ripetile in tutte le foto: l'insieme sembra più professionale, costruisci uno stile e la sessione dura meno.</p> <ul><li>Le clienti non sono modelle: guidale nella posizione. Se le dita non sono dritte, chiedi di tenere la mano intorno a un oggetto (per esempio il flacone del colore).</li> <li>Le luci a barra creano linee di luce sulle unghie: belle sui colori pieni, ma coprono i dettagli della nail art. Per la nail art è meglio una luce tonda e diffusa.</li> <li>Sul telefono puoi bloccare messa a fuoco ed esposizione tenendo premuto lo schermo (blocco AE/AF) e attivare la griglia per allineare le dita.</li> <li>Olio sì, ma poco e massaggiato: polvere o prodotto nelle cuticole rovinano anche il design più bello.</li></ul></div>
<div class="box case"><strong class="t">Caso pratico</strong> <p>Chiara riceve molte richieste di "unghie come in foto" che poi non riesce a replicare in un'ora di servizio.</p> <p><strong>Il problema.</strong> Il suo profilo mostra quasi solo lavori da gara e nail art complessa. Le clienti scelgono quello che vedono.</p> <p><strong>La soluzione.</strong></p> <ul><li>Pubblica soprattutto i lavori che vuoi vendere davvero: lunghezze portabili, colori di stagione, refill ben fatti.</li> <li>Nella didascalia scrivi il nome del servizio come compare nel tuo listino, così la richiesta arriva già "tradotta".</li> <li>Se hai il consenso, mostra percorsi "prima e dopo" (per esempio unghie rosicchiate): sono le foto che convincono di più chi ha un problema simile.</li> <li>Tieni le foto da gara in una sezione a parte: mostrano la tua tecnica, non il servizio standard.</li></ul></div>
`,
          sources: ['https://www.scratchmagazine.co.uk/feature/nailfies-nail-tech-expert-photography-tips/',
            'https://www.scratchmagazine.co.uk/feature/simply-salon-nails-photographing-your-nail-work',
            'https://nailac.com.pl/gb/blog/porady/how-to-take-nail-photos-that-will-get-your-clients-attention-',
            'https://www.garanteprivacy.it/garante/doc.jsp?ID=9983210',
            'https://www.quotidianopiu.it/dettaglio/16439364/consenso-alle-foto-in-centro-estetico-la-firma-non-basta', 'https://www.scratchmagazine.co.uk/feature/5-steps-to-improve-your-nail-photos/', 'https://www.katiebarnesacademy.com/en-ie/blogs/katiebarnesblogs/how-to-improve-your-nail-photos']
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
<div class="box pro"><strong class="t">Consiglio da professionista: come aumentare i prezzi</strong> <p>Rivedere il listino fa parte del lavoro: i costi salgono e la tua velocità e qualità migliorano. Le formatrici di settore suggeriscono:</p> <ul><li><strong>Preavviso di 3–4 settimane.</strong> Per esempio: annuncio all'inizio del mese, nuovi prezzi dal mese successivo. Puoi lasciare il vecchio prezzo agli appuntamenti già prenotati.</li> <li><strong>Messaggio breve e professionale:</strong> data di inizio, una frase sul motivo (costi e formazione), un grazie. Senza scusarti e senza lunghe giustificazioni.</li> <li><strong>Aumenti piccoli e regolari</strong> (alcune fonti indicano intorno al 10% o meno all'anno) pesano meno di un salto improvviso dopo anni.</li> <li>Un prezzo calcolato sui costi reali, come nel metodo sopra, ti dà sicurezza quando lo comunichi.</li></ul> <p>Le clienti scelgono anche per la qualità, la pulizia, la puntualità e il rapporto di fiducia, non solo per il prezzo.</p></div>
<h2>Agenda e tempi</h2>
${F('agenda-tempi.svg', 'Agenda: tempi del servizio più consulenza, consigli e pulizia.')}
<ul>
<li><strong>Misura i tuoi tempi</strong> reali con un cronometro per 10 servizi di ogni tipo. Da principiante sarai più lenta: è normale.</li>
<li>Nell'agenda aggiungi a ogni servizio i minuti per <strong>igiene della postazione e sterilizzazione</strong>.</li>
<li>Prenota il <strong>refill</strong> prima che la cliente esca.</li>
<li>Scrivi e comunica in anticipo le regole su <strong>ritardi e disdette</strong> (per esempio entro quante ore si può spostare l'appuntamento).</li>
<li>Manda un <strong>promemoria</strong> il giorno prima: riduce le assenze.</li>
</ul>
<div class="box deep"><strong class="t">Approfondimento: disdette, caparra e acconto</strong> <p>Molti saloni chiedono un anticipo al momento della prenotazione per ridurre le assenze. I dati dei software gestionali (non studi indipendenti) parlano di forti riduzioni delle assenze con anticipo e promemoria. In Italia è importante chiamare le cose con il nome giusto:</p> <ul><li><strong>Caparra confirmatoria</strong> (art. 1385 del Codice civile): se la cliente non si presenta senza giustificato motivo, puoi trattenerla; se sei tu a non rispettare l'appuntamento, devi restituire il doppio.</li> <li><strong>Acconto</strong>: è un anticipo sul prezzo e va restituito se il servizio non viene eseguito.</li></ul> <p>Scrivi le regole in modo chiaro prima della prenotazione: importo, entro quante ore si può disdire senza perderlo, se diventa un buono per un'altra data. Le condizioni comunicate prima sono quelle che contano. Per un caso concreto, chiedi a un consulente o a un'associazione di categoria.</p></div>
<div class="box case"><strong class="t">Caso pratico</strong> <p>Elisa ha 60 clienti attive ma l'agenda è piena a ondate: una settimana esaurita, la successiva mezza vuota.</p> <p><strong>Diagnosi.</strong> Prenota il refill solo quando la cliente scrive. Così le clienti tornano in ritardo (con più sollevamenti e servizi più lunghi) e alcune spariscono.</p> <p><strong>Cosa cambia.</strong></p> <ul><li>Fissa il prossimo appuntamento <strong>prima che la cliente si alzi</strong>, proponendo due date.</li> <li>Misura per un mese quante clienti escono con il refill già prenotato. Alcuni software di settore indicano una media intorno al 40% e oltre il 60% nei saloni migliori: sono dati commerciali, usali solo come riferimento.</li> <li>Promemoria automatico il giorno prima.</li> <li>Lascia ogni settimana uno o due spazi liberi per riparazioni e clienti nuove.</li></ul> <p>Il refill puntuale aiuta la cliente (unghie più sane e stabili) e il tuo incasso, che diventa più prevedibile.</p></div>
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
            'https://www.scratchmagazine.co.uk/news/nailympia-germany-2025-the-results/', 'https://academy.thegelbottle.com/blog/how-to-update-your-prices-confidently-nail-business-pricing-guide-tgb-academy', 'https://ericasata.com/blogs/news/how-to-confidently-increase-your-prices-as-a-nail-artist', 'https://www.filodiritto.com/codici/codice-civile/capo-v-degli-effetti-del-contratto/art-1385', 'https://quifinanza.it/fisco-tasse/leggi/caparra-digitale-ristorante-restituzione/918141/', 'https://www.zenoti.com/en-uk/thecheckin/no-show-revenue-calculator', 'https://www.reservio.com/blog/tips/nail-salon-guide', 'https://schedulingkit.com/statistics/nail-salon-industry-statistics']
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
<div class="box info"><strong class="t">POS e registratore telematico: la novità 2026</strong> <p>Dal 2026, per effetto della Legge di Bilancio 2025, gli strumenti di pagamento elettronico (POS) devono essere <strong>collegati al registratore telematico</strong>. Non è un cavo né un programma: è un'associazione che si fa online, nell'area riservata del portale dell'Agenzia delle Entrate. Per i POS attivati o cambiati dopo l'avvio ci sono scadenze periodiche (per esempio, per quelli di settembre 2026 il termine indicato è il 30 novembre 2026).</p> <p>Sulle sanzioni le fonti non sono d'accordo. Quando apri l'attività, o cambi POS o banca, chiedi al commercialista di fare subito l'associazione.</p></div>
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
<div class="box tip"><strong class="t">Il bollo da 2 euro</strong> <p>Chi è in regime forfettario non applica l'IVA. Per questo sulle <strong>fatture senza IVA di importo superiore a 77,47 €</strong> va applicata l'imposta di bollo di 2 € (DPR 642/1972). Con la fattura elettronica il bollo è "virtuale": si indica nel file e si paga con F24 o con addebito dal portale dell'Agenzia, con scadenze trimestrali.</p> <ul><li>Esempio: una ricostruzione da 90 € fatturata a una cliente supera la soglia, quindi serve il bollo.</li> <li>Se lo addebiti alla cliente, quei 2 € diventano un ricavo su cui si pagano imposta e contributi (interpello dell'Agenzia delle Entrate n. 428/2022).</li></ul> <p>Chiedi al commercialista come gestirlo con il tuo documento di incasso e con il tuo programma di fatturazione.</p></div>
<h2>Contributi INPS artigiani (2026)</h2>
<ul>
<li>Si pagano <strong>contributi fissi</strong> su un reddito minimo (minimale) di <strong>18.808 €</strong>: circa <strong>4.521 € l'anno</strong>, in 4 rate, <strong>anche se guadagni meno</strong>.</li>
<li>Sopra il minimale si paga il <strong>24%</strong> (25% oltre 56.224 €).</li>
<li>Chi è in forfettario può chiedere una <strong>riduzione del 35%</strong> con domanda telematica all'INPS (per il 2026 entro il 28 febbraio; per le attività nuove, subito dopo l'iscrizione). Le fonti non concordano sugli effetti di una domanda tardiva: chiedi al commercialista.</li>
<li>Per chi ha iniziato nel 2025 esiste una riduzione del 50% per 36 mesi (non cumulabile con quella del 35%); dalle fonti consultate non risulta estesa a chi apre nel 2026.</li>
</ul>
${B('danger', 'Il primo anno', 'Molte principianti scoprono i contributi fissi solo alla prima scadenza. Metti da parte ogni mese una quota degli incassi per tasse e contributi.')}
<div class="box case"><strong class="t">Caso pratico: quanto mettere da parte</strong> <p>Riprendiamo l'esempio con 30.000 € di incassi in regime forfettario (calcolo semplificato, senza riduzioni contributive).</p> <table><tr><th>Voce</th><th>Calcolo</th><th>Importo</th></tr> <tr><td>Reddito forfettario</td><td>30.000 × 67%</td><td>20.100 €</td></tr> <tr><td>Contributi INPS</td><td>4.521 fissi + 24% × (20.100 − 18.808)</td><td>circa 4.830 €</td></tr> <tr><td>Imposta al 5%</td><td>(20.100 − 4.830) × 5%</td><td>circa 760 €</td></tr> <tr><td>Imposta al 15%</td><td>(20.100 − 4.830) × 15%</td><td>circa 2.290 €</td></tr></table> <p>Totale: circa <strong>5.600 €</strong> (19% degli incassi) con l'imposta al 5%, circa <strong>7.100 €</strong> (24%) con il 15%. Una regola prudente è mettere da parte <strong>un quinto–un quarto di ogni incasso</strong> su un conto separato. Ricorda che i contributi fissi si pagano anche se incassi poco: nei primi mesi la percentuale reale è più alta. Fai verificare i numeri al commercialista.</p></div>
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
            'https://www.money.it/rc-professionale-quando-e-obbligatoria-e-per-quali-lavoratori', 'https://quifinanza.it/fisco-tasse/pos-collegato-registratore-cassa-obbligo-sanzioni/960520/', 'https://www.agendadigitale.eu/documenti/collegamento-registratori-telematici-e-pos-ecco-le-nuove-regole/', 'https://www.money.it/pos-e-registratore-telematico-obbligo-mensile', 'https://www.fiscozen.it/guide/chi-paga-bollo-fatture-regime-forfettario/', 'https://www.fattureincloud.it/glossario/regime-forfettario/imposta-bollo/', 'https://copia.ordinepsicologi.piemonte.it/wp-content/uploads/2022/10/Focus-Forfettari-il-bollo-riaddebitato-al-cliente-costituisce-ricavo-tassato.pdf']
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
<div class="box deep"><strong class="t">Approfondimento: morsa o "pizzicata"?</strong> <p>Non tutte le unghie rovinate sono morse. L'<strong>onicotillomania</strong> è l'abitudine di strappare o "pizzicare" l'unghia e la pelle intorno, con le dita o con strumenti (forbicine, lime). I segni sono diversi:</p> <table><tr><th>Onicofagia (morso)</th><th>Onicotillomania (pizzicare)</th></tr> <tr><td>Bordo corto e seghettato, cuticole assenti o strappate</td><td>Solchi trasversali paralleli al centro della lamina, spesso sui pollici ("deformità da tic")</td></tr> <tr><td>Colpisce soprattutto le mani</td><td>Lamina assottigliata, lunula più grande, pieghe arrossate o con crosticine</td></tr></table> <p>Perché ti interessa: chi pizzica lo fa spesso con l'altra mano, quindi il gel non basta. Lascia superfici lisce e senza bordi, e lavora sulla zona della cuticola con più cautela. Un'altra nota: mordere anche le unghie dei piedi è meno comune e può accompagnarsi ad altri disturbi; in questi casi il suggerimento del medico è ancora più importante.</p></div>
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
<div class="box case"><strong class="t">Caso pratico</strong> <p>Federica, 28 anni, porta la foto di unghie a mandorla lunghe 2 cm per il suo matrimonio, tra 6 settimane. Le sue unghie sono rosicchiate fino al letto, le pellicine sono strappate ma la pelle è chiusa.</p> <p><strong>Ragionamento.</strong> Semaforo verde per lavorare, ma il letto è corto: la regola dell'allungamento di circa 1/3 della lamina dice che 2 cm sono fuori portata. Una leva così lunga su una base piccola si stacca, e Federica non è abituata ad avere "qualcosa" sulla punta delle dita.</p> <p><strong>La proposta.</strong></p> <ul><li>Oggi: unghie corte e robuste, cover per allungare otticamente il letto.</li> <li>Controllo dopo 2 settimane, e un altro una settimana prima del matrimonio.</li> <li>Per il giorno delle nozze: forma a mandorla corta, colore chiaro coprente, eventualmente decori leggeri.</li></ul> <p>Mostrale foto di risultati simili. Una promessa realistica mantenuta vale più di un "sì" che si rompe prima della cerimonia.</p></div>
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
<div class="box deep"><strong class="t">Approfondimento: cosa funziona davvero per smettere</strong> <ul><li><strong>Inversione dell'abitudine</strong> (habit reversal training): è il trattamento con più prove. In uno studio gli episodi di morso sono scesi da circa 10 a 0,3 al giorno, e il 40% delle persone ha smesso del tutto. Una revisione del 2025 su 21 studi la conferma come l'intervento più efficace.</li> <li><strong>Smalti amari</strong>: sono il rimedio più diffuso, ma le prove sono deboli. In uno studio i promemoria che non si possono togliere hanno avuto meno abbandoni (12%) dello smalto amaro (26%).</li> <li><strong>Farmaci</strong>: le prove sono scarse e spettano solo al medico.</li></ul> <p>Le revisioni dermatologiche dicono che la manicure professionale può aiutare le persone motivate e nasconde l'unghia rovinata mentre ricresce. Limare i bordi rotti riduce gli "appigli" che fanno partire il morso. Tu sei un aiuto concreto, ma la decisione di smettere resta della cliente.</p></div>
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
            'https://www.scratchmagazine.co.uk/blog/form-fitting-for-nail-biters', 'https://repositori.uvic-ucc.cat/handle/10854/180495']
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
<div class="box pro"><strong class="t">Consiglio da professionista: se scegli il tip</strong> <p>Sulle unghie rosicchiate il polpastrello è spesso gonfio e rialzato: un tip normale non si appoggia bene e la pelle lo spinge verso l'alto, così il tip si stacca in punta. Le tecniche usate dalle professioniste:</p> <ul><li>Usa tip <strong>con l'incavo</strong> (la zona di contatto) e rifilalo su misura, sia nell'incavo sia ai lati, finché il tip si "siede" sull'unghia senza fessure.</li> <li>Scegli forme <strong>tonde e di lunghezza moderata</strong>: punte e angoli sono più facili da afferrare con i denti.</li> <li>Se resta uno spazio sotto il tip, o se la pelle davanti all'unghia è gonfia o ferita, passa alla cartina o rimanda.</li></ul> <p>Il letto corto si nasconde con un cover rosa o "camouflage" steso in modo da portare la smile line dove la vuoi.</p></div>
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
<div class="box case"><strong class="t">Caso pratico</strong> <p>Su una cliente la cartina non entra: il cuscinetto di pelle davanti all'unghia è più alto della lamina e la lamina è quasi piatta, un po' concava.</p> <p><strong>Come procede una formatrice esperta.</strong></p> <ol><li>Taglia la parte superiore della linguetta della cartina.</li> <li>Rifila la cartina perché tocchi il bordo dell'unghia, e taglia una piccola "U" dove l'iponichio è più alto: toglie pressione dalla pelle.</li> <li>Fai scivolare la cartina sotto: spinge in basso il cuscinetto e diventa una base su cui costruire.</li> <li>Taglia i lati della cartina a circa 45° partendo dal solco laterale: si chiude meglio e la curva a C viene più regolare.</li></ol> <p>Se la lamina è concava, livellala prima con un velo sottile di builder: se la cartina è curva e l'unghia piatta resta uno spazio dove il prodotto cola sotto.</p> <p><strong>Limite:</strong> si lavora solo se la pelle intorno non è gonfia ed è integra.</p></div>
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
<div class="box warn"><strong class="t">Lamina sottile, rischio calore più alto</strong> <p>Le unghie rosicchiate hanno spesso una lamina sottile e irregolare e un letto sensibile. Una lamina sana fa da "cuscinetto" tra il prodotto che scalda in lampada e il letto ungueale; se è sottile, il calore arriva quasi tutto. In più il cover e il builder coprono una superficie piccola, e si tende a stenderli spessi.</p> <ul><li>Cover e builder in strati sottili, polimerizzando tra uno e l'altro.</li> <li>Avvio morbido in lampada (modalità low heat, o mano appena fuori per qualche secondo), poi polimerizzazione completa.</li> <li>Avvisa prima la cliente: "Se senti caldo, togli la mano".</li></ul> <p>Una cliente che si brucia alla prima seduta difficilmente torna, e il percorso di recupero si ferma prima di iniziare.</p></div>
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
            'https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-fit-nail-forms-to-different-nail-shapes', 'https://www.salongeek.com/threads/help-my-first-nail-biter.67797/', 'https://www.bustle.com/life/best-fake-nails-for-nail-biters', 'https://nailknowledge.org/?p=49737', 'https://nailknowledge.org/?p=44956', 'https://www.scratchmagazine.co.uk/feature/heat-spikes-in-gel-nail-services-why-they-happen-how-to-avoid-them']
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
<div class="box pro"><strong class="t">Consiglio da professionista: misura i progressi in millimetri</strong> <p>Con una crescita di circa 3,5 mm al mese, in 2 settimane la lamina avanza di circa 1,5–2 mm. È poco a occhio, ma si vede bene se lo misuri.</p> <ul><li>A ogni controllo misura con un righello o un calibro la distanza tra cuticola e <strong>linea onicodermica</strong> (dove la lamina si stacca dal letto) di due dita di riferimento, per esempio indice e anulare.</li> <li>Scrivi i numeri sulla scheda accanto alla foto.</li> <li>Mostra il grafico alla cliente: "Due mesi fa il tuo letto misurava 9 mm, oggi 11".</li></ul> <p>Tieni presenti i tempi lunghi: una fonte tecnica riporta un recupero che ha richiesto 11 mesi. Se a ogni seduta c'è un numero che sale, la cliente ha un motivo concreto per non mordere.</p></div>
<h2>Appuntamenti: perché più ravvicinati all'inizio</h2>
<ul>
<li>Le ricostruzioni su unghie molto rosicchiate <strong>durano meno</strong> di quelle su unghie sane. La superficie di appoggio è piccola e la cliente può ancora "provare" a mordere.</li>
<li>Per questo all'inizio conviene vedere la cliente <strong>più spesso</strong>: nella pratica, circa ogni 2 settimane. Poi si passa al refill normale ogni 3–4 settimane.</li>
<li>Continua a vederla anche quando ha smesso di mordere: i controlli regolari aiutano a non ricominciare.</li>
</ul>
${F("refill.svg", "Ricrescita e refill: il profilo prima e dopo il riequilibrio.")}
<div class="box pro"><strong class="t">Consiglio da professionista: proponi un percorso, non un servizio</strong> <p>Chi si mangia le unghie ha bisogno di appuntamenti più frequenti all'inizio e di continuare i controlli anche dopo aver smesso. Presentarlo come un <strong>percorso</strong> rende tutto più chiaro:</p> <ul><li>Prima seduta: consulenza, foto "prima", ricostruzione corta.</li> <li>Primi 2–3 mesi: controlli ravvicinati (circa ogni 2 settimane), più brevi di un refill completo.</li> <li>Poi refill normali ogni 3–4 settimane.</li></ul> <p>Scrivi sulla scheda e sul biglietto le date già fissate. Prezza i controlli brevi per il tempo reale che richiedono: la cliente sa in anticipo quanto spenderà e tu non lavori in perdita. Quando la cliente smette di mordere, festeggialo con una foto confronto: è anche la pubblicità più efficace (con il suo consenso).</p></div>
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
<div class="box case"><strong class="t">Caso pratico</strong> <p>Dopo due mesi senza problemi, Anna torna con tre unghie morse e una staccata: "È stato un periodo stressante, scusa".</p> <p><strong>Come rispondi.</strong> Niente rimproveri: le ricadute sono normali nelle abitudini ripetitive. Un tono giudicante la spingerebbe a non tornare più.</p> <p><strong>Cosa fai.</strong></p> <ul><li>Controlla la pelle: se ci sono ferite aperte, sistemi solo le unghie integre e rimandi le altre.</li> <li>Lima e leviga ogni bordo morso o scheggiato: niente appigli.</li> <li>Accorcia di nuovo dove serve; la lunghezza si riconquista.</li> <li>Rivedi con lei i momenti "a rischio" e fissa un controllo ravvicinato.</li></ul> <p>Se le ricadute sono frequenti o l'abitudine è legata all'ansia, ricordale con delicatezza che esistono percorsi efficaci, come l'inversione dell'abitudine, e che può parlarne con il medico.</p></div>
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
            'https://pmc.ncbi.nlm.nih.gov/articles/PMC8953487/', 'https://nailknowledge.org/?p=49737']
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
<div class="box deep"><strong class="t">Approfondimento: perché sulle lamine flessibili il prodotto rigido si stacca</strong> <p>Una lamina sottile e morbida si piega a ogni movimento delle dita. Un prodotto rigido non la segue: a ogni flessione l'adesione viene "strattonata", soprattutto ai bordi, finché si apre un varco. Le lamine sottili sono anche le più sensibili all'acqua: si gonfiano e si asciugano più delle lamine spesse, e questo aggiunge altro stress.</p> <ul><li>Scegli prodotti <strong>flessibili</strong> (rubber base, builder morbidi) e stendili sottili.</li> <li>Lunghezza contenuta: meno leva, meno flessione.</li> <li>Per le occasioni speciali, su lamine molto deboli, si può usare un gel trasparente rinforzato con fibre, sempre sottile.</li></ul> <p>Più spessore non risolve: aumenta la rigidità e quindi lo "strappo" alla base.</p></div>
<h2>Unghia a cucchiaio: attenzione alla salute</h2>
<p>La coilonichia può avere molte cause. La carenza di ferro (anemia) è tra le più note e più comuni; altre sono malattie della pelle come la psoriasi, problemi della tiroide, micosi, traumi ripetuti o il contatto frequente con solventi. Nei bambini piccoli può essere normale e scomparire con la crescita.</p>
${B("warn", "Comparsa recente? Medico", "Se la forma a cucchiaio è comparsa da poco, o la cliente è stanca e pallida, consiglia un controllo dal medico. Tu non fai diagnosi: segnali solo che vale la pena controllare.")}
${F("ski-jump-correzione.svg", "Ski-jump di profilo: a sinistra l'errore, al centro dove accorciare, a destra la correzione con cartina inclinata e zona 2 più piena.")}
<div class="box info"><strong class="t">Unghia a pinza: quando è un segnale</strong> <p>L'unghia a pinza colpisce soprattutto gli alluci, molto più raramente le mani; secondo alcune stime riguarda circa lo 0,9% delle persone. Può essere ereditaria (di solito uguale sui due lati) oppure acquisita (spesso asimmetrica). Le forme acquisite sono state associate anche a malattie generali.</p> <p>Per te significa:</p> <ul><li>Una curva "a pinza" <strong>comparsa da poco</strong>, soprattutto su un solo dito o sulle mani, è un buon motivo per consigliare il medico.</li> <li>I bordi che premono nei solchi possono dare dolore, infiammazione e infezioni ripetute: in questo caso la cura è del podologo o del medico.</li> <li>I trattamenti conservativi spesso danno solo un miglioramento temporaneo: non promettere di "raddrizzare" l'unghia con la ricostruzione.</li></ul></div>
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
<div class="box pro"><strong class="t">Consiglio da professionista: la cartina segue la forma finale</strong> <table><tr><th>Forma</th><th>Cartina di profilo</th><th>Cartina dall'alto</th><th>Apex</th></tr> <tr><td>Quadrata, squoval</td><td>Dritta, in asse con il centro del dito</td><td>Aperta, lati paralleli</td><td>Al centro del letto allungato, poi dritto verso la punta</td></tr> <tr><td>Mandorla, ovale, stiletto</td><td>Leggermente verso il basso</td><td>Chiusa</td><td>A circa 1/3 del letto, poi in discesa verso la punta</td></tr> <tr><td>Ballerina, coffin</td><td>Dritta</td><td>Chiusa</td><td>A circa 1/3 del letto, poi dritto verso la punta</td></tr></table> <p>Nella ballerina si restringe solo l'allungamento: se limi i lati in diagonale anche sopra il letto, indebolisci la struttura. Evita anche di riempire troppo i lati: il peso in più aumenta lo stress e le rotture.</p></div>
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
            'https://www.katiebarnesacademy.com/blogs/nail-structure-application/how-to-fit-nail-forms-to-different-nail-shapes', 'https://nailknowledge.org/?p=49737', 'https://nailknowledge.org/blog/water-vs-waterless-manicures']
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
<div class="box deep"><strong class="t">Approfondimento: coprenza e polimerizzazione</strong><p>Un cover è coprente perché contiene molto pigmento. Ma più pigmento significa anche <strong>meno luce che arriva in profondità</strong> (l'effetto ombrello). Ecco perché con i cover vale più che mai la regola degli strati sottili:</p><ul><li>Due strati sottili coprono come uno spesso, ma polimerizzano fino in fondo.</li><li>Il pollice ha una superficie più grande e si scalda di più: è il dito dove il calore si sente per primo.</li><li>Uno strato di cover rimasto morbido sotto si nota dopo qualche giorno: grinze, distacchi, o un'unghia che si "ammacca" premendo.</li></ul></div>
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
<div class="box pro"><strong class="t">Consiglio da professionista</strong>Decidi la lunghezza del nuovo letto usando la <strong>proporzione</strong>, non la stessa misura in millimetri su tutte le dita: il mignolo ha un letto più corto del medio, e con la stessa misura sembrerebbe "tutto rosa". Un metodo pratico: allinea le dita e guarda la mano a 40 cm di distanza; le smile line devono formare una linea armoniosa, come i denti in un sorriso. Ricorda che il letto allungato sta <strong>sopra l'allungamento</strong>: non spingere mai il cover sopra l'iponichio per guadagnare millimetri.</div>
<h2>Il cover nel refill</h2>
<ul>
<li>Con la ricrescita, tra la cuticola e il vecchio cover si vede una fascia di unghia naturale.</li>
<li>Assottiglia il vecchio prodotto, poi stendi il cover nuovo nella zona di ricrescita, sfumandolo sul vecchio senza scalini.</li>
<li>Se il letto naturale si è allungato (per esempio dopo l'onicofagia), accorcia di conseguenza il cover.</li>
</ul>
<div class="box case"><strong class="t">Caso pratico</strong><p><strong>Ex onicofagica, dopo tre mesi il letto naturale si è allungato di circa 2 mm.</strong></p><p>Il letto naturale ora arriva sotto la parte di cover che prima "fingeva" il letto. Va bene così: è il risultato che volevi. Al refill:</p><ol><li>Fotografa la mano prima di iniziare e confronta con le foto dei servizi precedenti.</li><li>Assottiglia il vecchio prodotto e valuta dove finisce ora il letto vero.</li><li>Se il cover allungato ora sembra eccessivo, accorcialo: la smile line si riposiziona più vicina al bordo naturale.</li><li>Se la cliente lo desidera, prova un cover un po' più trasparente: il suo letto non ha più bisogno di essere nascosto.</li></ol></div>
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
            'https://www.my-personaltrainer.it/bellezza/unghie-effetto-correttore-il-trend-concealer-nails-del-2026-per-una-manicure-naturale-e-perfetta.html', 'https://nailknowledge.org/blog/mastering-uv-gel-application-insights-into-pigments', 'https://nailknowledge.org/blog/heat-spikes', 'https://www.scratchmagazine.co.uk/feature/how-to-create-a-crisp-smile-line-with-the-gel-system', 'https://www.opi.com/professionals/how-to-rebalance-and-fill-opi-gelevate-overlay-services']
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
<div class="box deep"><strong class="t">Approfondimento: il camouflage con i complementari</strong><p>Come nel trucco correttivo: il verde neutralizza il rosso, pesca e arancio neutralizzano i toni blu-violacei, il lilla attenua il giallo. Applicato alle unghie:</p><table><tr><th>Che cosa vedi</th><th>Scelta di cover</th></tr><tr><td>Letto molto rosso o arrossato</td><td>Nude beige più neutro, non un rosa acceso che lo esalta</td></tr><tr><td>Letto bluastro o violaceo (mani fredde)</td><td>Cover con base pesca</td></tr><tr><td>Lamina un po' ingiallita (es. dopo smalti rossi senza base)</td><td>Nude rosato; top con riflesso lilla</td></tr></table><p><strong>Attenzione:</strong> il camouflage è per lamine sane con piccole discromie. Macchie verdi, nere, una striscia scura o un colore che cambia vanno mostrati al medico, non coperti.</p></div>
<h2>Il sottotono della pelle</h2>
<p>Il <strong>tono</strong> è quanto la pelle è chiara o scura. Il <strong>sottotono</strong> è il riflesso di colore sotto la superficie: freddo (rosato), caldo (dorato) o neutro. Due persone con la stessa pelle chiara possono avere sottotoni diversi.</p>
${F("sottotono-test.svg", "Tre test pratici per capire il sottotono: vene, foglio bianco, gioielli.")}
<ol class="steps">
<li><strong>Test delle vene</strong>: guarda l'interno del polso alla luce del giorno. Vene bluastre o violacee fanno pensare a un sottotono freddo; verdastre a uno caldo; difficili da dire a uno neutro.</li>
<li><strong>Test del foglio bianco</strong>: accosta un foglio bianco alla mano. Se la pelle sembra rosata è più fredda; se sembra gialla o dorata è più calda.</li>
<li><strong>Test dei gioielli</strong>: se all'argento la pelle "si accende" è più fredda; con l'oro è più calda; se vanno bene entrambi è neutra.</li>
</ol>
${B("warn", "Test indicativi", "Questi test sono indicazioni pratiche, non misure. A volte danno risultati diversi tra loro, e il sottotono «olivastro» non rientra bene in nessuna casella. Usali per orientarti, poi decidi provando il colore vero sull'unghia.")}
<div class="box pro"><strong class="t">Consiglio da professionista</strong>Il colore del letto ungueale non dipende solo dal sottotono: risente anche della <strong>temperatura delle mani</strong>. Una cliente che arriva dal freddo può avere letti pallidi o violacei, e un cover scelto in quel momento risulterà troppo caldo dopo mezz'ora. Fai la prova colore <strong>dopo</strong> la preparazione, quando le mani si sono scaldate (anche con un breve lavaggio in acqua tiepida). E valuta sempre il letto ungueale e la pelle intorno insieme: il cover deve legare con entrambi.</div>
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
<div class="box deep"><strong class="t">Approfondimento: il metamerismo</strong><p>Due colori possono sembrare identici sotto una luce e diversi sotto un'altra. Si chiama <strong>metamerismo</strong>: il colore che vediamo dipende sia dalla superficie sia dalla luce che la illumina. Le luci fluorescenti e molti LED economici hanno uno spettro "a picchi" e rendono il fenomeno più evidente.</p><p>Per le unghie vuol dire che un cover che "sparisce" sotto la lampada da tavolo può staccare alla luce del giorno, o viceversa. Per i colori più delicati (nude, cover, rosa) fai la prova in <strong>due luci</strong>: vicino alla finestra e sotto la luce del tuo posto di lavoro. Una lampada con un indice di resa cromatica alto aiuta, ma non garantisce che il colore resti uguale ovunque.</p></div>
<h2>Errori frequenti</h2>
<ul>
<li>Scegliere il colore sotto la lampada da lavoro.</li>
<li>Confrontare con il dorso della mano invece che con il letto ungueale.</li>
<li>Usare un solo cover per tutte le clienti.</li>
<li>Fidarsi solo del colore nel vasetto: steso sottile appare diverso.</li>
</ul>
<div class="box deep"><strong class="t">Approfondimento: il contrasto simultaneo</strong>Josef Albers ha mostrato che lo stesso colore cambia aspetto a seconda di ciò che lo circonda: un grigio sembra più chiaro su sfondo scuro e più scuro su sfondo chiaro. Per questo un tip nude sulla ruota bianca della cartella non è lo stesso nude sull'unghia della cliente: lì è circondato dalla pelle, che lo fa sembrare più chiaro, più scuro, più rosa o più giallo. È un motivo in più per <strong>appoggiare sempre il campione sul dito</strong> e confrontare colori a coppie, sullo stesso sfondo.</div>
`,
          sources: ['https://www.masterclass.com/articles/how-to-identify-your-skins-undertone',
            'https://makeup.com/product-and-reviews/foundation/identifying-your-skins-undertone',
            'https://www.my-personaltrainer.it/bellezza/unghie-effetto-correttore-il-trend-concealer-nails-del-2026-per-una-manicure-naturale-e-perfetta.html', 'https://www.cbc.ca/life/style/colour-correcting-101-the-why-and-how-of-this-technical-makeup-step-1.7055449', 'https://aad.org/nail-care-secrets/manicure-pedicure-safety', 'https://rmit.pressbooks.pub/colourtheory1/chapter/metamerism-when-colours-seem-to-change-in-different-light-sources/', 'https://www.printed-editions.com/blog/josefs-albers-colour-theory/']
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
<li>I pigmenti <strong>rossi e neri</strong> assorbono molta luce UV: sono tra i più "difficili". Anche il <strong>bianco coprente</strong> (biossido di titanio) è delicato: non assorbe, ma riflette e blocca la luce negli strati spessi. Per entrambi: strati sottili.</li>
<li>Anche lo <strong>spessore</strong> conta: in uno strato spesso la parte in alto assorbe la luce e quella in fondo resta poco polimerizzata, anche senza pigmenti.</li>
</ul>
${B("warn", "Strati sottili prima di tutto", "Con un gel molto pigmentato le fonti consigliano strati sottili e, se la scheda tecnica lo prevede, un tempo di lampada più lungo. Un tempo più lungo però non «salva» uno strato troppo spesso: la luce comunque non arriva in fondo. Lo strato sotto resta morbido, il colore si raggrinzisce o si stacca, e il gel non polimerizzato può dare allergia se tocca la pelle.")}
${F("colore-strati-step.svg", "Stendere il colore: mescola, base, primo strato sottile, sigilla la punta, secondo strato e top.")}
<div class="box deep"><strong class="t">Approfondimento: e il bianco?</strong><p>Secondo NailKnowledge, i pigmenti <strong>rossi e neri</strong> sono quelli che assorbono più luce UV. Il <strong>bianco</strong> funziona in modo diverso: il biossido di titanio non "assorbe" come il nero, ma riflette e diffonde moltissimo la luce, e in uno strato spesso la blocca prima che arrivi in fondo. Il risultato è lo stesso: sopra duro, sotto molle, poi grinze.</p><p>Quindi la regola pratica non cambia: <strong>rossi, neri, bianchi coprenti e cover molto pigmentati</strong> sono i colori in cui gli strati sottili contano di più.</p></div>
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
<div class="box pro"><strong class="t">Consiglio da professionista</strong>Non basta "dare più tempo di lampada": conta <strong>quale</strong> lampada. Ogni gel contiene fotoiniziatori che rispondono a certe lunghezze d'onda. Un gel con fotoiniziatori non adatti alla tua lampada polimerizza lentamente e lascia uno strato appiccicoso più spesso; uno pensato per lampade lente, sotto un LED potente, polimerizza troppo in fretta e scalda. Se cambi marca di colore senza cambiare lampada, prova prima su tip: superficie, grinze e calore ti dicono se la combinazione funziona.</div>
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
<div class="box case"><strong class="t">Caso pratico</strong><p><strong>Una cliente con un gel nude chiaro si lamenta che il colore è ingiallito.</strong></p><p>Fai una domanda chiave: <em>era già giallo quando è uscita dal salone, o lo è diventato durante la settimana?</em></p><ul><li><strong>Giallo subito:</strong> calore in lampada, spesso per strati spessi con lampada molto potente. Strati più sottili.</li><li><strong>Giallo dopo giorni o una vacanza:</strong> esposizione al sole; alcuni top ingialliscono con gli UV. Valuta un top stabilizzato.</li><li><strong>Lamina gialla dopo la rimozione:</strong> pigmento a contatto diretto con la lamina, senza base.</li><li><strong>Giallo che si ripete a ogni servizio:</strong> fumo, prodotti per la pulizia, tinte per capelli. Consiglia i guanti.</li></ul></div>
`,
          sources: ['https://nailknowledge.org/blog/mastering-uv-gel-application-insights-into-pigments',
            'https://nailknowledge.org/blog/unveiling-the-hazards-of-thick-uv-gel-application',
            'https://aad.org/nail-care-secrets/manicure-pedicure-safety',
            'https://pinkgellac.com/blogs/news/how-to-use-cat-eye-gel-polish', 'https://nailknowledge.org/blog/why-white-gel-polish-looks-patchy', 'https://nailknowledge.org/blog/heat-spikes', 'https://nailknowledge.org/nail-knowledge-base/inhibition-layer-and-no-cleanse-gels', 'https://semilac.co.uk/blogs/news/gel-lifting-and-yellowing-root-causes-and-salon-floor-fixes']
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
<div class="box pro"><strong class="t">Consiglio da professionista</strong>Per i colori <strong>jelly</strong> e per i cover semitrasparenti prepara due campioni: uno con uno strato e uno con tre. Il colore cambia molto con lo spessore, e la cliente deve vedere quello che otterrà davvero. Conserva la cartella al riparo dal sole: alcuni top ingialliscono con gli UV, e un campione ingiallito non è più fedele. Ogni tanto confronta il campione con un tip appena fatto con lo stesso colore: se non coincidono più, rifallo.</div>
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
<div class="box deep"><strong class="t">Approfondimento: prima la luminosità, poi la tinta</strong>Un disegno si legge da lontano soprattutto grazie al <strong>contrasto di luminosità</strong> (chiaro contro scuro), più che alla differenza di tinta. Due colori diversi ma ugualmente chiari, per esempio un rosa e un azzurro pastello, da lontano si confondono. Prova semplice: fotografa i tip della proposta e guarda la foto in <strong>bianco e nero</strong>. Se il disegno sparisce, aumenta la differenza di luminosità: scurisci uno dei due colori o aggiungi un contorno sottile.</div>
<h2>Errori frequenti</h2>
<ul>
<li>Cartella con campioni sbiaditi o graffiati.</li>
<li>Campioni stesi diversamente da come lavori: il risultato non coincide.</li>
<li>Proporre troppi colori insieme: la cliente si confonde. Meglio 3–4 proposte mirate.</li>
</ul>
<div class="box case"><strong class="t">Caso pratico</strong><p><strong>La cliente non riesce a decidere tra tre nude quasi uguali.</strong></p><ol><li><strong>Elimina per sottotono:</strong> se ha riflessi dorati, il nude più rosato è il primo a uscire.</li><li><strong>Confronta a coppie:</strong> due tip sul dito, alla luce della finestra; quello che "sparisce" meglio vince e sfida il terzo.</li><li><strong>Cambia luce:</strong> ricontrolla il vincitore sotto la luce del tuo tavolo, perché i nude sono i colori più sensibili al cambio di luce.</li><li><strong>Annota</strong> il colore scelto sulla scheda, con la nota "scelto alla luce naturale".</li></ol><p>In pochi minuti la scelta diventa ragionata, e la cliente si sente seguita.</p></div>
`,
          sources: ['https://www.masterclass.com/articles/how-to-identify-your-skins-undertone',
            'https://www.youngnails.com/blogs/news/how-to-do-ombre-gel-polish-nails', 'https://nailknowledge.org/blog/mastering-uv-gel-application-insights-into-pigments', 'https://semilac.co.uk/blogs/news/gel-lifting-and-yellowing-root-causes-and-salon-floor-fixes', 'https://www.printed-editions.com/blog/josefs-albers-colour-theory/', 'https://rmit.pressbooks.pub/colourtheory1/chapter/metamerism-when-colours-seem-to-change-in-different-light-sources/']
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
<div class="box pro"><strong class="t">Consiglio da professionista: fai il conto della ricrescita</strong> <p>Con circa 1,6 mm al mese puoi stimare quando un segno sparirà, e dirlo alla cliente prima che si preoccupi.</p> <ul><li>Un segno (una macchia, un'ammaccatura, un'impronta di rimozione) a 10 mm dalla punta dell'alluce uscirà in circa <strong>6 mesi</strong> (10 ÷ 1,6).</li> <li>Un segno alla base di un alluce lungo 20 mm ci metterà più di <strong>un anno</strong>.</li> <li>Sulle mani, con circa 3,5 mm al mese, lo stesso segno a 10 mm sparisce in meno di 3 mesi.</li></ul> <p>Annota la data e la distanza dalla cuticola sulla scheda, con una foto. Se il segno <strong>non avanza</strong> con la crescita, o si allarga, non è un normale segno da trauma: consiglia il medico.</p></div>
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
<div class="box case"><strong class="t">Caso pratico</strong> <p>La signora Rina, 79 anni, chiede di "sistemare" gli alluci: le unghie sono molto spesse, giallastre e difficili da tagliare.</p> <p><strong>Ragionamento.</strong> Non è "solo l'età". Un'unghia gialla, ispessita e friabile può essere una micosi; un'unghia spessissima e deformata è un'unghia ipertrofica, che per legge è competenza del podologo. In più a quest'età possono esserci diabete, problemi di circolazione o farmaci anticoagulanti.</p> <p><strong>Cosa fai.</strong></p> <ul><li>Anamnesi completa, anche se è una cliente abituale.</li> <li>Non assottigliare né tagliare con forza gli alluci spessi: consiglia il podologo, con un biglietto e un nome di riferimento.</li> <li>Sulle altre unghie sane puoi lavorare normalmente: ammorbidire, tagliare dritto a piccoli colpi, limare gli angoli.</li> <li>Niente colore sulle unghie sospette.</li></ul> <p>Così la cliente resta tua per la parte estetica, e riceve la cura giusta per il resto.</p></div>
<h2>Perché le unghie si incarniscono</h2>
<ul>
<li><strong>Taglio sbagliato</strong>: troppo corto, arrotondato o scavato ai lati.</li>
<li><strong>Scarpe strette</strong> in punta, o tacchi che spingono il piede in avanti.</li>
<li><strong>Traumi</strong>: urti, sport, unghia schiacciata.</li>
<li><strong>Forma dell'unghia</strong>: unghie molto curve o a pinza.</li>
</ul>
<p>Puoi dare consigli di prevenzione (taglio, scarpe comode). Il trattamento di un'unghia incarnita spetta al podologo o al medico.</p>
<div class="box warn"><strong class="t">Unghia nera all'alluce: ematoma o altro?</strong> <p>Una macchia scura sotto l'unghia del piede è spesso un <strong>ematoma</strong>, cioè sangue dovuto a scarpe strette, corsa o urti. Di solito colpisce l'alluce (a volte entrambi), ha un bordo curvo e netto verso la base e <strong>si sposta in avanti</strong> mentre l'unghia cresce.</p> <p>Segnali che invece vanno fatti vedere subito al dermatologo:</p> <ul><li>una banda scura in lunghezza larga più di circa 3 mm, o che si allarga;</li> <li>colori diversi o bordi irregolari;</li> <li>pigmento che passa sulla pelle intorno all'unghia (segno di Hutchinson);</li> <li>un solo dito colpito, soprattutto pollice o alluce, senza un trauma ricordato;</li> <li>unghia che si rovina o sanguina.</li></ul> <p>Non coprirla con il colore: fotografala con la data e consiglia la visita. Solo il medico può fare la diagnosi.</p></div>
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
            'https://www.quotidianosanita.it/scienza-e-farmaci/piede-diabetico-ecco-il-decalogo-della-sid-per-prevenirlo/', 'https://cdn.enzyklopaedie-dermatologie.de/en/dermatology/subungual-melanoma-120192', 'https://actasdermo.org/en-is-hutchinson-s-sign-pathognomic-subungual-articulo-S1578219018301719', 'https://www.pulsetoday.co.uk/?p=15395', 'https://cislfp.it/wp-content/uploads/2018/10/d.-m.-666-1994-podologo.pdf', 'https://www.michiganfootdoctors.com/white-toenails-from-nail-polish/', 'https://iwgdfguidelines.org/wp-content/uploads/2019/05/02-IWGDF-prevention-guideline-2019.pdf']
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
<div class="box case"><strong class="t">Caso pratico</strong> <p>Valentina vuole il semipermanente rosso per le vacanze. Il suo alluce destro è giallastro, un po' spesso e friabile sul bordo. "Tanto con il colore non si vede".</p> <p><strong>Perché no.</strong> Gel e semipermanente sigillano la lamina: i podologi li considerano controindicati finché un'infezione da funghi non è guarita. Il colore non cura la micosi, la nasconde, e intanto il problema può peggiorare. Una ricerca del 2025 ha collegato l'uso frequente di cosmetici per unghie e i traumi ripetuti alle infezioni fungine, senza però dire che il gel ne sia la causa.</p> <p><strong>Cosa puoi proporre.</strong></p> <ul><li>Spiegazione gentile, senza diagnosi, e consiglio di andare dal podologo o dal medico.</li> <li>Una pedicure estetica di base su unghie e pelle sane, con strumenti monouso o sterilizzati e lima buttata subito.</li> <li>Un nuovo appuntamento quando avrà il via libera.</li></ul></div>
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
<div class="box pro"><strong class="t">Consiglio da professionista: cosa non si può disinfettare</strong> <p>Lime in carta o spugna, buffer, pietra pomice, raspe abrasive non metalliche, spazzolini: sono materiali <strong>porosi</strong>. Lo sporco e i microrganismi entrano nei pori e nessun disinfettante li raggiunge davvero.</p> <ul><li>Il comitato di controllo della California considera questi oggetti monouso per ogni cliente, <strong>anche se sulla confezione c'è scritto "disinfettabile"</strong>, finché non ci saranno prove valide del contrario.</li> <li>Regole simili valgono in altri stati americani; dove sono più permissive, l'oggetto va comunque buttato se ha toccato sangue o pelle o unghie non sane.</li></ul> <p>In pratica: lima e buffer nuovi per ogni cliente (puoi regalarli a lei a fine servizio), strumenti in metallo puliti e sterilizzati. In Italia segui le regole della tua Regione e del tuo Comune, ma il principio è lo stesso.</p></div>
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
<div class="box danger"><strong class="t">Un piccolo taglio non è mai piccolo</strong> <p>Nel 2019 a Treviso una donna di 82 anni è morta in ospedale per un'infezione partita, secondo la stampa locale, da un piccolo taglio all'alluce durante una normale pedicure. L'associazione dei podologi ha ricordato che questi casi non sono isolati, soprattutto nelle strutture per anziani.</p> <p>Le linee guida internazionali sul piede diabetico (IWGDF) indicano che vesciche, fessure (ragadi) ed emorragie sotto la pelle sono <strong>segni pre-ulcerativi</strong>: possono annunciare un'ulcera e vanno trattati subito da un professionista sanitario formato. Lo stesso vale per calli abbondanti, unghie incarnite o ispessite e micosi.</p> <ul><li>Su anziane e persone con diabete: niente lame, niente tagli delle pellicine, niente prodotti per calli.</li> <li>Se vedi uno di questi segni: ti fermi, lo annoti e consigli il podologo.</li></ul></div>
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
            'https://ar.unmhealth.org/services/orthopaedics/_files/take-care-of-your-feet-for-a-lifetime-2-12-20-eng-812-1094.pdf', 'https://www.barbercosmo.ca.gov/forms_pubs/publications/disinfect_nailfiles.pdf', 'https://www.law.cornell.edu/regulations/wyoming/033-10-Wyo-Code-R-SS-10-3', 'https://regulations.justia.com/states/maine/02/041/barbering-and-cosmetology-licensing-program/chapter-26/section-041-26-26-250', 'https://www.michiganfootdoctors.com/nail-polish-feet/', 'https://www.ynetnews.com/health_science/article/r1jz4spzgl', 'https://www.tanglewoodfootspecialists.com/faqs/can-i-polish-my-toenails-during-treatment-for-fungal-toenails.cfm', 'https://www.quotidianosanita.it/lettere-al-direttore/taglio-fatale-all-alluce-anziana-muore-dopo-la-pedicure-appello-dei-podologi-a-grillo/', 'https://iwgdfguidelines.org/wp-content/uploads/2019/05/02-IWGDF-prevention-guideline-2019.pdf']
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
<div class="box deep"><strong class="t">Approfondimento: il criterio dei giudici è lo scopo</strong> <p>Non esiste una sentenza della Cassazione dedicata proprio alla pedicure, ma per i massaggi la Corte usa un criterio chiaro, utile anche per te. L'esercizio abusivo di una professione (art. 348 del Codice penale) c'è quando una prestazione ha uno <strong>scopo di cura</strong> di un problema di salute ed è svolta da chi non ha il titolo.</p> <ul><li>Cass. n. 50063/2015: condanna per massaggi a pagamento rivolti a disturbi reali (ernie, sciatica, distorsioni).</li> <li>Cass. n. 12539/2020: nessun reato per massaggi in spiaggia con solo scopo di benessere e relax.</li></ul> <p>Applicato alla pedicure: levigare la pelle secca del tallone per migliorarne l'aspetto è estetica; "togliere il callo che fa male" o "curare" un'unghia incarnita è cura. Fai attenzione anche alle parole del listino e dei social: scritte come "pedicure curativa" o "trattamento delle unghie incarnite" descrivono uno scopo di cura.</p></div>
<h2>Calli, duroni e lame</h2>
<p>Le <strong>callosità</strong> sono citate espressamente tra le competenze del podologo. Le linee guida sul piede diabetico raccomandano di non rimuoverle con prodotti chimici, cerotti o altre tecniche fai-da-te. La SID raccomanda di non tagliare i calli e di levigare l'ispessimento solo con pietra pomice.</p>
${B("warn", "In estetica: niente lame", "In una pedicure estetica la pelle ispessita si leviga con lime o raspe adatte, senza ferire. Lame e bisturi su calli e duroni non rientrano nel lavoro estetico. Prima di proporre qualsiasi trattamento sui calli, verifica il regolamento del tuo Comune e della tua Regione.")}
<div class="box case"><strong class="t">Caso pratico</strong> <p>Un cliente di 60 anni, diabetico, chiede di "togliere quel callo sotto l'avampiede". Al centro del callo vedi un puntino scuro.</p> <p><strong>Ragionamento.</strong> Un puntino scuro dentro un callo può essere sangue sotto la pelle: per le linee guida sul piede diabetico è un segno che può precedere un'ulcera, e va trattato subito da un professionista sanitario. Le stesse linee guida dicono di non usare mai prodotti chimici o cerotti per togliere i calli.</p> <p><strong>Cosa fai.</strong></p> <ul><li>Non levighi quella zona e non usi alcun prodotto.</li> <li>Spieghi con calma: "Vedo un segno che è meglio far controllare dal podologo prima di trattare questa zona".</li> <li>Scrivi su un biglietto cosa hai visto e dove, con la data, e il contatto di un podologo.</li> <li>Puoi completare la parte estetica sul resto del piede, se la pelle è integra.</li></ul></div>
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
<div class="box pro"><strong class="t">Consiglio da professionista: chiedi del rischio, non solo della diagnosi</strong> <p>Molte persone con diabete non sanno di avere già una ridotta sensibilità ai piedi. Le linee guida IWGDF dividono le persone con diabete in classi di rischio (da 0 a 3) e raccomandano controlli dal medico o podologo da una volta l'anno (rischio molto basso) fino a ogni 1–3 mesi (rischio alto).</p> <p>In anamnesi aggiungi tre domande semplici:</p> <ul><li>"Il medico o il podologo le ha mai detto che ha i piedi a rischio?"</li> <li>"Ha mai avuto ferite o ulcere ai piedi, o interventi?"</li> <li>"Ogni quanto va dal podologo?"</li></ul> <p>Se la risposta è sì alle prime due, o se non è mai stata controllata, la pedicure estetica si limita al minimo e si consiglia una visita. Ricordale anche i consigli delle linee guida: mai a piedi nudi, nemmeno in casa, e controllo dei piedi ogni giorno.</p></div>
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
            'https://www.quotidianosanita.it/scienza-e-farmaci/piede-diabetico-ecco-il-decalogo-della-sid-per-prevenirlo/', 'https://www.studiocataldi.it/articoli/38203-cassazione-il-massaggio-in-spiaggia-non-e-reato-abusivo-della-professione.asp', 'https://www.studiocataldi.it/articoli/20455-improvvisarsi-massaggiatore-a-scopo-terapeutico-e-reato.asp']
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
<div class="box tip"><strong class="t">Lampada e piedi</strong> <p>Sui piedi è più difficile posizionare bene la lampada e le dita piccole spesso restano in ombra. Controlla che <strong>tutte</strong> le unghie siano dentro il fascio di luce, compreso il mignolo, ed eventualmente polimerizzale in due tempi. Un gel che resta morbido su un dito piccolo dura meno e aumenta il rischio di allergia.</p> <p>Ricorda anche lo strato appiccicoso: sulle dita vicine è facile toccarlo con la pelle. Usa separadita monouso e toglilo con un dischetto senza strofinare sulla pelle.</p></div>
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
<div class="box deep"><strong class="t">Approfondimento: le macchie bianche dopo l'estate</strong> <p>Togliendo il colore a fine estate si trovano spesso chiazze bianche, ruvide, "gessose". Spesso sono <strong>granulazioni di cheratina</strong>: il prodotto aderisce agli strati più superficiali della lamina e, con una rimozione energica (strappare, raschiare, acetone ripetuto), li porta via. La superficie diventa porosa e diffonde la luce: per questo appare bianca.</p> <ul><li>Non sono un'infezione e di solito spariscono con qualche settimana di pausa e olio quotidiano (da 2–3 settimane nei casi lievi a 2–3 mesi in quelli estesi).</li> <li>Prevenzione: base sotto il colore, rimozione con ammollo completo, mai strappare.</li> <li>Attenzione: una micosi bianca superficiale può sembrare simile. Se le macchie si allargano, l'unghia si ispessisce o compaiono su unghie mai smaltate, consiglia il podologo.</li></ul></div>
<div class="box pro"><strong class="t">Consiglio da professionista: quando rifarlo</strong> <p>L'unghia del piede cresce circa 1,6 mm al mese: dopo 4 settimane la ricrescita è di circa 1,5 mm, dopo 8 settimane supera i 3 mm. Il colore regge a lungo, ma tenerlo troppo non conviene:</p> <ul><li>più a lungo resta, più il bordo libero si consuma e si scheggia;</li> <li>sotto un colore coprente non vedi cambiamenti come macchie, ispessimenti o distacchi.</li></ul> <p>Una prassi ragionevole è proporre il rifacimento ogni <strong>4–6 settimane</strong>, controllando ogni volta la lamina scoperta. Se la cliente vuole tenerlo di più, almeno a ogni rimozione osserva bene l'unghia con buona luce prima di rifare il colore.</p></div>
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
            'https://bionumbers.hms.harvard.edu/bionumber.aspx?id=112380', 'https://www.michiganfootdoctors.com/white-toenails-from-nail-polish/', 'https://www.michiganfootdoctors.com/nail-polish-feet/', 'https://nailknowledge.org/nail-knowledge-base/inhibition-layer-and-no-cleanse-gels', 'https://nailknowledge.org/?p=49737']
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
<div class="box deep"><strong class="t">Approfondimento: perché il chrome diventa uno specchio</strong> <p>Le polveri chrome sono di solito particelle metalliche finissime (spesso alluminio), a volte su base di vetro, colorate in vari toni. Uno specchio è una superficie in cui tutte le particelle riflettenti sono <strong>piatte e allineate</strong>: strofinando, le pieghi e le stendi sulla superficie liscia del top.</p> <ul><li>Se il top sotto ha avvallamenti o bolle, le particelle seguono quei difetti e lo specchio "si rompe".</li> <li>Un fondo scuro assorbe la luce che passa tra le particelle: il riflesso sembra più intenso. Su fondi chiari l'effetto è più debole.</li> <li>Le polveri con molti riempitivi (filler) riflettono meno: a parità di tecnica, una polvere più pura è più brillante.</li> <li>Le particelle restano in superficie e si consumano: senza top finale il chrome si toglie strofinando.</li></ul></div>
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
<div class="box deep"><strong class="t">Approfondimento: come funziona il magnete</strong> <p>Il gel cat-eye contiene minuscole particelle di <strong>ossido di ferro</strong>, metalliche e allungate. Senza magnete sono orientate a caso e la luce si disperde. Il campo del magnete le fa ruotare tutte nella stessa direzione: insieme diventano una piccola superficie riflettente dentro il gel. La lampada le "congela" in quella posizione.</p> <ul><li>Le particelle sono leggermente inclinate nel gel: per questo la linea sembra muoversi quando giri la mano, anche se in realtà è ferma.</li> <li>Particelle più fini danno un luccichio morbido; più grandi, una linea più netta e "drammatica".</li> <li>Magneti dritti danno una linea pulita; magneti curvi o a più poli creano onde, linee doppie o effetti a stella.</li> <li>Il gel deve restare fluido abbastanza a lungo: se è freddo e denso, le particelle si muovono male.</li></ul></div>
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
<div class="box pro"><strong class="t">Consiglio da professionista: densità giusta per ogni effetto</strong> <p>La densità del gel decide quanto il disegno resta dove lo metti. Un gel molto fluido si autolivella: è perfetto per una sfumatura morbida, ma allarga le linee e rischia di toccare la pelle. Per linee nette (foil a strisce, smile line, decori) serve un gel <strong>più denso</strong>, ma non così denso da sembrare in rilievo.</p> <ul><li>Ombré morbido: colori fluidi, pennellate leggere, poco prodotto.</li> <li>Linee precise e bordi puliti alla cuticola: gel più denso o gel da pittura.</li> <li>Se il gel "scappa", non è sempre colpa della mano: cambia viscosità o fai un flash più breve tra un passaggio e l'altro.</li></ul> <p>Con il caldo i gel diventano più fluidi, con il freddo più densi: tienine conto prima di un servizio con molti dettagli.</p></div>
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
            'https://www.youngnails.com/blogs/news/how-to-do-ombre-gel-polish-nails', 'https://fairyglamor.com/blogs/dip-acrylic-nail-powder-help/what-are-chrome-nails', 'https://mitty.com.au/products/shattered-plum', 'https://nailknowledge.org/?p=169165', 'https://www.scratchmagazine.co.uk/feature/gel-nails-why-you-need-to-know-about-viscosity/', 'https://twentypro.co.uk/blogs/news/how-to-work-with-gel-products-in-extreme-temperatures']
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
<div class="box pro"><strong class="t">Consiglio da professionista: i pennelli per gel</strong> <p>Se dipingi one-stroke con il gel, il nemico è la <strong>luce</strong>. La luce del giorno contiene raggi UV: un pennello lasciato vicino a una finestra o alla lampada può polimerizzare il gel tra le setole.</p> <ul><li>Rimetti sempre il cappuccio e conserva i pennelli lontano da finestre e lampade, senza schiacciare le setole.</li> <li>Carica solo la parte che serve e tieni il gel lontano dalla ghiera.</li> <li>Se il gel nel pennello si è solo addensato, a volte si recupera lavorando un po' di gel fresco tra le setole. Se è indurito del tutto, toglierlo rovina i peli e la forma.</li></ul> <p>Con i colori acrilici per nail art (a base d'acqua) lascia asciugare bene la pittura prima di sigillare: il top va steso sottile, su colore asciutto al tatto.</p></div>
<h2>3D</h2>
<p>Il 3D sono decorazioni in rilievo: fiori, fiocchi, perle modellate.</p>
<ul>
<li><strong>Acrilico colorato</strong>: si modella una perla alla volta con il pennello, petalo per petalo, e si lascia indurire all'aria.</li>
<li><strong>Gel da modellare</strong> (o polygel): si modella con calma, poi si polimerizza a piccoli passaggi.</li>
<li>Si fissa alla superficie con un velo di builder o di gel e si sigilla intorno senza coprire il rilievo.</li>
</ul>
${B("warn", "Spessore e vita quotidiana", "Il 3D si rompe facilmente e può impigliarsi. Tienilo basso, su una o due unghie, ed evitalo per clienti con lavori manuali. In gara segui le regole della categoria: in alcune categorie il 3D o certi materiali sono vietati.")}
${F("incapsulato-zone.svg", "Dove incapsulare: nelle zone spesse (smile line, apex, centro della punta), mai alla cuticola, ai lati o sul bordo.")}
<div class="box deep"><strong class="t">Approfondimento: la perla per il 3D in acrilico</strong> <p>Nel 3D la perla deve essere "giusta": né troppo bagnata, né troppo asciutta, e va lavorata in fretta, prima che l'acrilico indurisca. Molte tecniche partono da una perla <strong>un po' più asciutta</strong> del solito, perché tiene meglio la forma del petalo. Ma se il prodotto indurisce troppo presto, di solito è il pennello a essere troppo asciutto: tienilo leggermente umido di liquido.</p> <ul><li>Petali: una piccola perla tirata a goccia, poi la punta del pennello preme verso il basso e verso l'esterno al centro della goccia. Usa le ore di un orologio per distanziare i petali.</li> <li>Rose: una striscia di prodotto che si arrotola su se stessa quando ha iniziato a fare presa ma è ancora flessibile.</li> <li>Petali complessi: si possono modellare a parte e posizionare con il pennello inumidito di liquido.</li></ul> <p>Lavora con una buona ventilazione: con il 3D si sta a lungo vicino al monomero.</p></div>
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
<div class="box case"><strong class="t">Caso pratico</strong> <p>Una sposa vuole fiori in rilievo su tutte e dieci le unghie, lunghezza media, e indosserà guanti di pizzo e un anello importante.</p> <p><strong>Ragionamento.</strong> Il 3D si impiglia nei tessuti, si rompe con gli urti e su dieci dita rende difficili anche gesti semplici. Il pizzo dei guanti e l'anello sono due punti di attrito sicuri.</p> <p><strong>La proposta.</strong></p> <ul><li>3D basso solo su uno o due accenti, per esempio l'anulare della mano senza fede o i pollici.</li> <li>Sulle altre unghie fiori secchi o pizzo <strong>incapsulati</strong>: stesso tema, superficie liscia.</li> <li>Prova i fiori o il pizzo su un tip qualche giorno prima: alcuni materiali perdono colore a contatto con gel o liquido.</li></ul> <p>Come riferimento per "basso": nelle gare Nailympia di Sicilia la categoria Stiletto ammette decori 3D solo sotto i 5 mm di altezza. Per la vita quotidiana, meglio ancora meno.</p></div>
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
            'https://www.scratchmagazine.co.uk/feature/how-to-ace-encapsulation-in-lp-gel-nails', 'https://www.katiebarnesacademy.com/blogs/brushes/why-does-gel-cure-inside-my-nail-art-brush', 'https://www.katiebarnesacademy.com/blogs/brushes/how-should-you-clean-gel-nail-brushes', 'https://www.salongeek.com/threads/sealing-nail-art.85539/', 'https://www.nailpro.com/3d-flower/', 'https://www.cosmeticsandtoiletries.com/home/article/22933935/mastering-acrylic-flowers-elevating-your-nail-art-with-realistic-details', 'https://www.scratchmagazine.co.uk/nail_art/how-to-create-a-3d-flower-nail-design', 'https://www.nailympia.com/sicily/rules/']
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
<h3>Dettagli di regolamento che sorprendono (Nailympia Sicily 2026)</h3> <table><tr><th>Categoria</th><th>Regola</th></tr> <tr><td>Gel Polish (45 min)</td><td>La modella arriva con la manicure già fatta e le unghie naturali, senza prodotto; nessun allungamento. Una mano rosso vivo pieno (niente metallizzato, glitter, opaco o perlato), l'altra french rosso e bianco. Smile line solo con un pennellino sottile: niente strumenti o fresa.</td></tr> <tr><td>Fantasy</td><td>10 punti in meno se sulle unghie della modella c'è smalto o base.</td></tr> <tr><td>Salon Nails (60 min)</td><td>Un solo sistema, niente miscele; solo french rosa e bianco scolpito; esattamente 10 cartine, non preparate; niente colla sul tavolo se usi le cartine.</td></tr> <tr><td>Tutte</td><td>Scatola di tip nuova con almeno 10 tip per misura; i tip restano nella scatola fino al via. Acqua, sapone e aria compressa solo durante la gara: dopo lo stop si viene squalificati.</td></tr></table> <p>Leggi le regole della <strong>tua</strong> categoria e della <strong>tua</strong> edizione: queste valgono per Sicily 2026.</p>
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
<div class="box case"><strong class="t">Caso pratico: scegliere la modella</strong> <p>Silvia ha due possibili modelle: la sorella, disponibile sempre ma con dita storte e unghie corte e piatte, e un'amica con letti lunghi e dita dritte, libera però solo nei weekend.</p> <p><strong>Ragionamento.</strong> Il regolamento Nailympia, per la categoria Tip &amp; Overlay French, consiglia proprio una modella con dita e unghie dritte. Dita storte fanno sembrare storte anche unghie perfette viste dall'alto e dal punto di vista della modella, e una lamina piatta rende più difficile una curva a C regolare.</p> <p><strong>La scelta.</strong> L'amica, con un calendario fisso di allenamenti nei weekend. La sorella resta per gli esercizi tecnici su singole unghie durante la settimana.</p> <p><strong>Prima della gara:</strong> cuticole sane e senza tagli (i danni alla pelle costano punti), nessuna preparazione vietata e mani idratate nei giorni precedenti, non il giorno stesso.</p></div>
<h2>Piano di allenamento (8–12 settimane, prassi)</h2>
<ol class="steps">
<li><strong>Settimana 1</strong>: scegli la categoria, scarica regolamento e scheda punteggi, fai la lista del kit.</li>
<li><strong>Settimane 1–4</strong>: una mano completa a settimana su modella, cronometrata. Foto di profilo, a tunnel, dall'alto e della cuticola.</li>
<li><strong>Settimane 5–8</strong>: allena i punti deboli visti nelle foto (per esempio 20 smile line su tip, 10 apex di profilo).</li>
<li><strong>Ultime settimane</strong>: simulazioni complete con 10 minuti in meno del tempo di gara, kit definitivo, prova del tavolo con la modella.</li>
<li><strong>Ultima settimana</strong>: niente prodotti nuovi. Controlla la modella: unghie sane, nessuna ferita, nessuna preparazione vietata.</li>
</ol>
<div class="box pro"><strong class="t">Consiglio da professionista: i consigli di una giudice Nailympia</strong> <p>Gabriella Kovács, giudice Nailympia, suggerisce cinque abitudini:</p> <ol><li><strong>Tavolo sempre uguale.</strong> Ogni prodotto e attrezzo nella stessa posizione in allenamento e in gara: sotto pressione troverai tutto anche senza guardare.</li> <li><strong>Non guardare le altre.</strong> Ognuna ha la sua velocità: il tuo obiettivo è finire il tuo set con il tuo ritmo.</li> <li><strong>Niente cambi di marchio nell'ultimo mese.</strong> Le mani si abituano alla consistenza e ai tempi di un prodotto.</li> <li><strong>Allenati per pezzi.</strong> Prima la forma della base, poi i lati, poi la smile line, poi la superficie e la lunghezza: una cosa per sessione.</li> <li><strong>Fai domande a chi ha già vinto.</strong> Molte campionesse tengono masterclass di gara.</li></ol></div>
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
            'https://www.nailpro.com/technique/article/21157846/competition-corner-for-the-win', 'https://www.scratchmagazine.co.uk/feature/gabriella-kovacs-nail-competition-tips']
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
<div class="box deep"><strong class="t">Approfondimento: dove si nascondono i punti "facili"</strong> <p>Raggruppiamo i criteri della scheda per tipo di abilità:</p> <table><tr><th>Gruppo</th><th>Criteri</th><th>Punti</th></tr> <tr><td>Struttura</td><td>Curva C, apex, hair line, convesso/concavo, arco e linee laterali</td><td>90</td></tr> <tr><td>Arte e colore</td><td>Decoro inlay, colore, creatività</td><td>45</td></tr> <tr><td>Rosa e bianco</td><td>Smile line, applicazione allungamento, letto</td><td>39</td></tr> <tr><td>Pulizia e finitura</td><td>Zona cuticolare, lucentezza, aderenza cartina, superficie</td><td>36</td></tr> <tr><td>Proporzioni</td><td>Lunghezza, forma</td><td>30</td></tr></table> <p>La struttura richiede mesi di allenamento. La pulizia e la finitura (36 punti, il 15% del totale) dipendono soprattutto da <strong>tempo e attenzione</strong>: polvere sotto il prodotto, cuticola graffiata o lucentezza incompleta sono punti persi per fretta. Per questo il piano di gara deve riservare gli ultimi minuti alla pulizia e alla lucidatura.</p></div>
<h2>Le viste del giudice</h2>
<ol class="steps">
<li><strong>Dall'alto</strong>: forma, simmetria, lunghezze proporzionate tra le dita, linee laterali.</li>
<li><strong>Di profilo</strong>: apex, arco superiore e inferiore, assenza di gobbe o avvallamenti.</li>
<li><strong>A tunnel</strong> (dalla punta): curva C, spessore del bordo ("hair line"), simmetria dei lati.</li>
<li><strong>Zona cuticolare</strong>, spesso con la lente: nessuno scalino, nessun taglio, nessun prodotto sulla pelle.</li>
<li><strong>Dal punto di vista della modella</strong>: la forma deve apparire uniforme anche guardando le proprie mani.</li>
</ol>
<div class="box tip"><strong class="t">Controlla anche quello che i giudici non dicono</strong> <ul><li><strong>Sotto l'unghia.</strong> Polvere, colla o residui di cartina sotto il bordo libero si vedono nella vista a tunnel e nella valutazione dell'aderenza.</li> <li><strong>Crema e olio.</strong> Nelle gare Nailympia troppa crema o olio a fine gara costa punti: serve una mano idratata, non lucida di olio.</li> <li><strong>Prodotto non polimerizzato.</strong> Un gel non polimerizzato del tutto non viene giudicato: polimerizza sempre per il tempo pieno, anche negli ultimi minuti.</li> <li><strong>Dopo lo stop.</strong> Qualsiasi pulizia di mani o unghie, anche solo con aria compressa, porta alla squalifica: tutta la pulizia va fatta prima.</li></ul> <p>Prova la sequenza finale (pulizia, lucidatura, olio) con il cronometro: deve diventare automatica.</p></div>
<h2>Allenarti con la scheda</h2>
<ol class="steps">
<li>Stampa la scheda della tua categoria.</li>
<li>Dopo ogni prova, fotografa le unghie dalle cinque viste.</li>
<li>Dai un voto onesto a ogni criterio, oppure fallo fare a una collega.</li>
<li>Scegli i <strong>due criteri più deboli</strong> con più punti in gioco e allenali per due settimane.</li>
<li>Ripeti: confronta i punteggi nel tempo.</li>
</ol>
${B("tip", "Decidere dove investire il tempo", "Nessuno prende il punteggio pieno. Sapere quanti punti vale ogni criterio ti aiuta a decidere, in gara, dove spendere gli ultimi minuti: spesso lucidatura e pulizia valgono più di un ritocco alla forma.")}
        
<div class="box case"><strong class="t">Caso pratico</strong> <p>Nella simulazione Paola ottiene 150 punti su 240. I suoi voti più bassi: arco e linee laterali 16 su 30, decoro e creatività 24 su 45, zona cuticolare e lucentezza 8 su 18.</p> <p><strong>Ragionamento.</strong> Per scegliere cosa allenare guarda due cose: <strong>quanti punti mancano</strong> e <strong>quanto tempo serve</strong> per recuperarli.</p> <ul><li>Cuticola e lucentezza: mancano 10 punti. Si recuperano in poche settimane con una routine fissa di pulizia e 5 minuti di lucidatura riservati.</li> <li>Arco e linee laterali: mancano 14 punti. Serve un lavoro tecnico lungo: 10 profili al giorno su tip, controllati in foto.</li> <li>Decoro: mancano 21 punti, ma dipende anche dal gusto dei giudici. Prova due o tre idee e falle vedere a una collega esperta.</li></ul> <p><strong>Piano.</strong> Subito la routine di pulizia (punti "sicuri"), in parallelo l'allenamento su arco e lati. Alla simulazione successiva confronta i punteggi criterio per criterio.</p></div>
`,
          sources: ['https://www.scratchmagazine.co.uk/wp-content/uploads/2026/01/Nailympia-2026-Scoresheet_French-Twist-3-shape-challenge.pdf',
            'https://www.nailympia.com/china/rules/',
            'https://www.scratchmagazine.co.uk/feature/the-importance-of-rules-questions/', 'https://www.nailympia.com/sicily/rules/']
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
      mistakes: ['Guardare solo dall\'alto', 'Voti generosi senza confronto'] },
    { id: 'es-semaforo', module: 'anatomia', level: 'base', title: 'Il semaforo delle unghie', time: '25 min', img: 'semaforo-unghie.svg', caption: 'Rosso, giallo, verde: decidi se lavorare.', imgs: ['patologie-tavola.svg', 'disturbi-tavola.svg'],
      goal: 'Allenarsi a riconoscere i casi in cui non si lavora, quelli da approfondire e quelli in cui si lavora con delicatezza.',
      materials: ['Le tavole patologie-tavola e disturbi-tavola', '10 foto di unghie da manuali o atlanti (non di clienti senza consenso)', 'Scheda cliente vuota', 'Penne rossa, gialla, verde'],
      steps: ['Per ogni foto descrivi in una riga cosa vedi (colore, forma, pelle intorno), senza dare un nome alla malattia.', 'Assegna un colore del semaforo e scrivi il perché.', 'Per i casi rossi scrivi la frase che diresti alla cliente e cosa annoti sulla scheda.', 'Per i casi verdi scrivi l\'adattamento (grana, strati, consigli a casa).', 'Confronta con le tavole e correggi.'],
      checks: ['Ho classificato come rosso micosi, paronichia, verruche, unghia verde e bande scure sospette', 'Ho usato frasi che non fanno diagnosi', 'Ho indicato la disinfezione dopo un caso rosso', 'Per ogni caso verde ho previsto un adattamento'],
      mistakes: ['Coprire con il colore una macchia o una banda scura', 'Classificare l\'onicolisi come verde senza conoscerne la causa', 'Dire alla cliente "è un fungo"'] },
    { id: 'es-inventario', module: 'igiene', level: 'base', title: 'Inventario prodotti e documenti', time: '40 min', img: 'etichetta-inci.svg', caption: 'Cosa cercare in etichetta.', imgs: ['autoclave-busta.svg', 'rifiuti-contenitori.svg'],
      goal: 'Verificare che tutti i prodotti siano conformi alle regole UE e che i documenti richiesti dai controlli siano in ordine.',
      materials: ['Tutti i prodotti della postazione', 'Lente o smartphone per ingrandire l\'INCI', 'Etichette adesive e pennarello', 'Cartellina per schede tecniche e SDS', 'Registro di sterilizzazione'],
      steps: ['Elenca ogni prodotto con nome, lotto, data di apertura e PAO.', 'Cerca nell\'INCI TPO (Trimethylbenzoyl Diphenylphosphine Oxide) e DMTA (Dimethyltolylamine): separa i prodotti che li contengono con il cartello "NON UTILIZZABILI".', 'Controlla che i prodotti con HEMA riportino "Solo per uso professionale" e "Può provocare una reazione allergica".', 'Scrivi la data di apertura su disinfettanti e prodotti che ne sono privi.', 'Raccogli schede tecniche e SDS; verifica che il registro di sterilizzazione sia compilato (n. ciclo, data, parametri, test, firma).'],
      checks: ['Nessun prodotto con TPO o DMTA in uso', 'Ogni flacone aperto ha la data di apertura', 'Ho le SDS dei disinfettanti e dei prodotti principali', 'Il registro ha pagine numerate e cicli firmati'],
      mistakes: ['Controllare solo i semipermanenti e dimenticare liquidi per acrilico e attivatori', 'Buttare i prodotti vietati nell\'indifferenziata o nello scarico'] },
    { id: 'es-lampada', module: 'sistemi', level: 'base', title: 'Lampada e strato giusto', time: '35 min', img: 'lampada-watt-vs-nm.svg', caption: 'Conta la luce giusta, non i watt.', imgs: ['strato-dispersione.svg', 'lampada-posizione.svg'],
      goal: 'Capire l\'effetto di spessore, posizione e tempi di polimerizzazione su tip di prova.',
      materials: ['6 tip trasparenti su stecchini', 'Base e builder dello stesso sistema', 'La lampada indicata dal produttore', 'Cleaner e salviette', 'Scheda tecnica del gel', 'Guanti in nitrile'],
      steps: ['Leggi sulla scheda tecnica lunghezza d\'onda e tempi del builder; verifica sul manuale della lampada che li emetta.', 'Su 2 tip stendi uno strato sottile, su 2 uno strato molto spesso; polimerizza con i tempi corretti.', 'Su 2 tip sottili polimerizza mettendo il tip di lato, come un pollice dentro la lampada con le altre dita.', 'Togli lo strato di dispersione con una salvietta diversa per ogni tip e premi con un bastoncino: nota zone morbide, grinze o calore.', 'Scrivi una regola per ogni risultato.'],
      checks: ['Ho controllato la compatibilità lampada-gel sui documenti', 'Ho notato grinze o morbidezza negli strati spessi', 'Ho notato la differenza del tip "di lato"', 'Ho usato una salvietta pulita per ogni tip'],
      mistakes: ['Toccare il gel non polimerizzato senza guanti', 'Giudicare la polimerizzazione solo dalla superficie'] },
    { id: 'es-kit', module: 'attrezzatura', level: 'base', title: 'Riconosci strumenti e destinazione igienica', time: '25 min', img: 'strumenti-manuali.svg', caption: 'Ogni strumento ha il suo uso e la sua igiene.', imgs: ['lime-igiene.svg', 'kit-postazione.svg'],
      goal: 'Saper nominare ogni attrezzo del kit, il suo uso corretto e se va buttato, disinfettato o sterilizzato.',
      materials: ['Il tuo kit di partenza', 'Tre scatole o fogli con scritto MONOUSO, DISINFETTARE, STERILIZZARE', 'Quaderno'],
      steps: ['Disponi sul tavolo tutti gli strumenti, lime, pennelli e punte del kit.', 'Per ciascuno scrivi nome e uso principale in una riga.', 'Mettilo nella scatola giusta: monouso, disinfettare o sterilizzare.', 'Organizza la postazione in tre zone (pulita, lavoro, sporco) e fotografala.', 'Confronta con le tavole e correggi.'],
      checks: ['Lime in carta, buffer, bastoncini e bande abrasive nella scatola monouso', 'Spingicuticole, curetta, tronchesine e punte metalliche da sterilizzare', 'Lima in vetro, tagliatip e pinzette da disinfettare', 'Postazione con zona pulita e zona sporco separate'],
      mistakes: ['Considerare "lavabile" una lima porosa', 'Dimenticare le punte della fresa tra gli strumenti da sterilizzare'] }
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
      { q: 'Perché non si deve assottigliare la lamina naturale?', o: ['Perché diventa lucida', 'Perché isola meno dal calore e si indebolisce', 'Perché cresce più veloce', 'Non c\'è nessun motivo'], a: 1, e: 'Una lamina sottile espone a picchi di calore e danni.' },
      { q: 'Quale parte dell\'unghia produce la cuticola?', o: ['La matrice', 'L\'eponichio', 'L\'iponichio', 'Il letto ungueale'], a: 1, e: 'L\'eponichio è pelle viva sotto la piega prossimale: produce la cuticola, che invece è morta.' },
      { q: 'Quali sono i quattro "sigilli" che proteggono l\'unghia?', o: ['Lunula, matrice, letto, lamina', 'Cuticola con piega prossimale, due pieghe laterali, iponichio', 'Bordo libero, apex, punto di stress, lunula', 'Solo la cuticola'], a: 1, e: 'Sono le barriere contro germi e sostanze: non si tagliano e non si forzano.' },
      { q: 'Una matrice più lunga produce una lamina…', o: ['Più sottile', 'Più spessa', 'Più corta', 'Più colorata'], a: 1, e: 'Più lunga è la matrice, più strati produce: la lamina è più spessa. Lo spessore naturale non si può cambiare.' },
      { q: 'Dopo 3 settimane, quanta ricrescita ti aspetti in media sulle mani?', o: ['Circa 0,2 mm', 'Circa 2–2,5 mm', 'Circa 1 cm', 'Circa 5 mm'], a: 1, e: 'Circa 0,8 mm a settimana: in 3 settimane circa 2,4 mm.' },
      { q: 'Quale di questi segni di una banda scura sull\'unghia richiede il dermatologo con urgenza?', o: ['Bande sottili e uguali su più dita da anni', 'Pigmento che si estende sulla pelle intorno all\'unghia', 'Una macchia viola che si sposta in avanti dopo un colpo', 'Macchioline bianche'], a: 1, e: 'Il pigmento sulla piega (segno di Hutchinson) è un segnale d\'allarme: non coprire e consiglia subito il dermatologo.' },
      { q: 'Le linee di Beau (solchi trasversali) sono…', o: ['Un\'infezione contagiosa', 'Un disturbo dovuto a un rallentamento temporaneo della matrice: si può lavorare con delicatezza', 'Il segno di un\'allergia agli acrilati', 'Una forma di micosi'], a: 1, e: 'Si formano dopo febbre, malattie o traumi; non sono contagiose. Non si "livellano" con la lima.' }
    ],
    igiene: [
      { q: 'Quale trattamento elimina anche le spore?', o: ['Sanificazione', 'Disinfezione', 'Sterilizzazione', 'Detersione'], a: 2, e: 'Solo la sterilizzazione (autoclave) elimina ogni forma di vita.' },
      { q: 'Quale autoclave è adatta a strumenti imbustati, cavi e porosi?', o: ['Classe N', 'Classe B', 'Qualsiasi forno', 'Sterilizzatrice a sfere'], a: 1, e: 'L\'autoclave di classe B (EN 13060) gestisce carichi imbustati, cavi e porosi.' },
      { q: 'Quali guanti proteggono dai monomeri?', o: ['Lattice', 'Vinile', 'Nitrile', 'Cotone'], a: 2, e: 'Il lattice non protegge dai monomeri: usa il nitrile.' },
      { q: 'Dal 1° settembre 2025 nell\'UE è vietato nei cosmetici…', o: ['L\'HEMA', 'Il TPO', 'L\'acetone', 'L\'EMA'], a: 1, e: 'Il Reg. UE 2025/877 vieta TPO e DMTA, anche per uso professionale e per le scorte.' },
      { q: 'L\'HEMA nei prodotti per unghie è…', o: ['Vietato del tutto', 'Libero per tutti', 'Ammesso solo per uso professionale con avvertenze', 'Ammesso solo nei top'], a: 2, e: 'Reg. UE 2020/1682: uso professionale, con avvertenza sulle reazioni allergiche.' },
      { q: 'Quando è concreto il rischio di allergia agli acrilati?', o: ['Quando il prodotto polimerizzato è sulla lamina', 'Quando il prodotto non polimerizzato tocca la pelle', 'Solo con la lampada LED', 'Mai'], a: 1, e: 'Il contatto della pelle con prodotto non polimerizzato sensibilizza.' },
      { q: 'In Italia la ricostruzione unghie in proprio richiede…', o: ['Solo un attestato privato', 'La qualifica di estetista e la SCIA', 'Nessun requisito', 'La partita IVA e basta'], a: 1, e: 'Rientra nell\'attività di estetista (L. 1/1990); l\'apertura avviene con SCIA.' },
      { q: 'Che cosa significa "tempo di contatto" di un disinfettante?', o: ['Quanto dura il flacone aperto', 'Per quanti minuti la superficie deve restare bagnata perché il prodotto agisca', 'Il tempo per far asciugare le mani', 'La durata del ciclo in autoclave'], a: 1, e: 'Se asciughi prima, il disinfettante non fa effetto: rispetta il tempo indicato in etichetta.' },
      { q: 'Una lima in carta usata su una cliente…', o: ['Si disinfetta con alcol e si riusa', 'Si mette in autoclave', 'Si butta o si regala alla cliente', 'Si lascia al sole'], a: 2, e: 'È porosa: non si può disinfettare davvero, quindi è monouso.' },
      { q: 'A fine ciclo trovi una busta di sterilizzazione umida. Cosa fai?', o: ['La usi lo stesso', 'La asciughi con una salvietta', 'Consideri la sterilizzazione non riuscita e ripeti il ciclo con busta nuova', 'La metti nel box UV'], a: 2, e: 'Una busta umida indica un processo incompleto: la busta va rifatta e il ciclo ripetuto.' },
      { q: 'Qual è la protezione più efficace contro la polvere di limatura?', o: ['La mascherina chirurgica', 'L\'aspirazione vicino alle mani (tavolo aspirante o cappa)', 'Aprire la porta una volta al giorno', 'Soffiare via la polvere'], a: 1, e: 'Prima si cattura alla fonte; i DPI sono l\'ultima barriera.' },
      { q: 'La DMTA, vietata dal 1° settembre 2025, si trova soprattutto…', o: ['Negli smalti tradizionali', 'Nei liquidi per acrilico e negli attivatori dip, come accelerante', 'Nell\'acetone', 'Nell\'olio per cuticole'], a: 1, e: 'La N,N-dimetil-p-toluidina accelera l\'indurimento dei sistemi senza lampada: controlla l\'INCI di monomeri e attivatori.' },
      { q: 'Ti pungi con una tronchesina appena usata su una cliente. Cosa fai per prima cosa?', o: ['Ti metti un cerotto e continui', 'Favorisci il sanguinamento, lavi 10 minuti con acqua e antisettico, disinfetti e consulti un medico', 'Metti il dito in acetone', 'Aspetti la fine della giornata'], a: 1, e: 'È la procedura delle linee guida per l\'esposizione a sangue: poi serve una valutazione medica.' }
    ],
    sistemi: [
      { q: 'Il gel monofasico…', o: ['Non ha bisogno di lampada', 'Fa da base, costruttore e sigillante', 'Si usa solo per il french', 'È un tipo di acrilico'], a: 1, e: 'Un solo prodotto per tutte e tre le fasi.' },
      { q: 'Come indurisce l\'acrilico?', o: ['In lampada UV', 'Per reazione chimica tra liquido e polvere, senza lampada', 'Con l\'acetone', 'Con l\'attivatore spray'], a: 1, e: 'Il perossido di benzoile nella polvere e l\'accelerante nel liquido avviano la reazione a temperatura ambiente.' },
      { q: 'Una perla di acrilico troppo bagnata…', o: ['È la più resistente', 'Cola nei solchi e lascia monomero sulla pelle', 'È granulosa', 'Non aderisce'], a: 1, e: 'Troppo liquido = colature, ritiro e rischio allergia.' },
      { q: 'Il polygel si lavora con…', o: ['Monomero liquido', 'Slip solution e pennello, poi lampada', 'Acqua', 'Colla per tip'], a: 1, e: 'Si modella con slip solution e indurisce in lampada.' },
      { q: 'Il semipermanente…', o: ['Allunga l\'unghia', 'Dà colore per 2–3 settimane ma non struttura', 'Si toglie solo con la fresa', 'Non va in lampada'], a: 1, e: 'Colore su unghia naturale, nessuna struttura.' },
      { q: 'Per scegliere la lampada conta soprattutto…', o: ['Il numero di watt', 'Il colore della lampada', 'L\'abbinamento tra lunghezze d\'onda e fotoiniziatori del gel', 'La marca'], a: 2, e: 'Usa la lampada adatta al tuo sistema.' },
      { q: 'Picco di emissione tipico di una lampada LED per unghie?', o: ['250 nm', '500 nm', 'Circa 365–405 nm', '700 nm'], a: 2, e: 'Le lampade LED per unghie emettono in genere picchi a 365 e/o 405 nm (le fonti indicano 365–405 nm).' },
      { q: 'Perché un soft gel si toglie con l\'acetone e un hard gel no?', o: ['Perché il soft gel non va in lampada', 'Perché la rete di polimero del soft gel è meno fitta e l\'acetone ci penetra', 'Perché l\'hard gel contiene acetone', 'Perché il soft gel è un acrilico'], a: 1, e: 'Rete più aperta = l\'acetone entra e la scioglie; l\'hard gel, molto reticolato, si toglie limando.' },
      { q: 'Lo strato appiccicoso che resta sul gel dopo la lampada…', o: ['Indica che la lampada è guasta', 'È dovuto all\'ossigeno dell\'aria e si toglie alla fine con cleaner, una salvietta per dito', 'Va lasciato per sempre', 'Si toglie con acqua'], a: 1, e: 'È lo strato di dispersione: serve all\'aggancio tra gli strati, a fine lavoro si rimuove senza portarlo sulla pelle.' },
      { q: 'Nella polvere dell\'acrilico, cosa fa partire la reazione?', o: ['L\'acetone', 'Il perossido di benzoile (iniziatore)', 'Il pigmento', 'La luce della lampada'], a: 1, e: 'Il BPO nella polvere, attivato dal liquido, avvia la polimerizzazione all\'aria.' },
      { q: 'Perché non conviene usare il liquido di una marca con la polvere di un\'altra?', o: ['Perché cambia il colore', 'Perché iniziatore e acceleranti sono calibrati tra loro: si rischia un acrilico sotto-polimerizzato o fragile', 'Perché è vietato dalla legge', 'Non ci sono problemi'], a: 1, e: 'Più monomero non reagito significa anche più rischio di allergia.' },
      { q: 'Una lampada da 36 W polimerizza sicuramente meglio di una da 9 W?', o: ['Sì, sempre', 'No: conta che emetta le lunghezze d\'onda giuste con intensità sufficiente sull\'unghia', 'Sì, se è UV', 'Dipende solo dal colore'], a: 1, e: 'I watt misurano il consumo elettrico, non la luce utile ai fotoiniziatori.' },
      { q: 'Nel sistema dip, il modo igienico di applicare la polvere è…', o: ['Immergere il dito nel barattolo comune', 'Versare la polvere con un cucchiaino pulito sopra un contenitore monouso e buttare l\'avanzo', 'Soffiare la polvere sull\'unghia', 'Riutilizzare la polvere caduta'], a: 1, e: 'La polvere non si può disinfettare: niente dita nel barattolo comune.' }
    ],
    attrezzatura: [
      { q: 'Quale grana è la più abrasiva?', o: ['80', '180', '240', 'Buffer'], a: 0, e: 'Numero più basso = grana più grossa.' },
      { q: 'Quale grana usi sull\'unghia naturale?', o: ['80–100', '100/180', '180–240', 'Carburo'], a: 2, e: '180–240 per opacizzare senza assottigliare.' },
      { q: 'Le punte in carburo si usano…', o: ['Sulla cuticola', 'Solo sul prodotto artificiale', 'Sull\'unghia naturale', 'Per lucidare'], a: 1, e: 'Sulla lamina naturale e sulla cuticola si usano punte diamantate.' },
      { q: 'Velocità indicativa per lavorare in zona cuticolare?', o: ['5.000–10.000 RPM', '20.000–25.000 RPM', '30.000 RPM', 'Massima'], a: 0, e: 'Velocità basse e pressione leggera vicino alla pelle.' },
      { q: 'Perché la punta della fresa deve restare in movimento?', o: ['Per lucidare meglio', 'Per evitare calore da attrito e solchi', 'Per consumare meno', 'Non è necessario'], a: 1, e: 'Fermarsi in un punto scalda e scava.' },
      { q: 'Una lima in vetro usata su pelle integra, dopo la cliente…', o: ['Si butta sempre', 'Si pulisce e si disinfetta', 'Si mette in tasca per la prossima cliente', 'Si lucida con il buffer'], a: 1, e: 'Il vetro non è poroso: pulizia e disinfezione. Le lime in carta invece sono monouso.' },
      { q: 'Che cosa sono gli "anelli di fuoco"?', o: ['Un effetto di nail art', 'Solchi circolari sulla lamina causati da una punta della fresa inclinata', 'Un tipo di lampada', 'Il segno del primer'], a: 1, e: 'Si evitano tenendo la punta parallela alla superficie e sempre in movimento.' },
      { q: 'Qual è il diametro standard del gambo delle punte professionali per fresa?', o: ['1/8 di pollice (3,17 mm)', '3/32 di pollice (2,35 mm)', '5 mm', 'Non esiste uno standard'], a: 1, e: 'Le punte professionali hanno gambo da 2,35 mm; gli utensili da bricolage non vanno usati sulle clienti.' },
      { q: 'Come si pulisce un pennello da acrilico in setole naturali?', o: ['In acetone puro ogni sera', 'Nel monomero, poi asciugato su carta e rimodellato', 'Con acqua e sapone', 'Non si pulisce mai'], a: 1, e: 'Acetone e acqua seccano le setole; il monomero le mantiene morbide.' },
      { q: 'Le bande abrasive per fresa (carta su mandrino)…', o: ['Si sterilizzano in autoclave', 'Sono monouso', 'Si lavano in lavatrice', 'Si usano sulla pelle viva'], a: 1, e: 'Sono porose come le lime in carta: si buttano dopo la cliente.' }
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
      { q: 'Quanto è spesso, indicativamente, il bordo libero finito?', o: ['Come un foglio di carta', 'Sottile: circa come una carta di credito (0,8–1 mm)', '5 mm', 'Non conta'], a: 1, e: 'Più spesso si impiglia, più sottile si scheggia.' },
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
    { t: 'Giudizio alla cieca', d: 'Giudizio anonimo di gara: i giudici valutano il lavoro senza sapere chi l\'ha eseguito (modelle con un numero, giudici dietro tenda o in cabina).' },
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
    { t: 'MMA', d: 'Metil metacrilato: monomero da evitare nelle unghie (troppo rigido, difficile da togliere, irritante). Negli USA la FDA lo ha fatto ritirare negli anni \'70 e molti Stati lo vietano.' },
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
    { t: 'Velvet (cat-eye)', d: 'Effetto "velluto" del gel magnetico: luce diffusa su tutta l\'unghia, ottenuta muovendo il magnete.' },
    { t: 'Apparato ungueale', d: 'L\'insieme di lamina, matrice, letto, pieghe, cuticola e iponichio: l\'unghia come "sistema".' },
    { t: 'Banda onicodermica', d: 'Linea grigio-rosata sotto il bordo libero dove finisce il letto: la "smile line naturale".' },
    { t: 'Epitelio del letto', d: 'Strato sottile che aggancia la lamina al letto con creste e solchi e la lascia scorrere in avanti.' },
    { t: 'Piega prossimale', d: 'Piega di pelle alla base dell\'unghia che copre e protegge la matrice; non si taglia.' },
    { t: 'Sigilli dell\'unghia', d: 'Cuticola con piega prossimale, due pieghe laterali e iponichio: barriere contro germi e sostanze.' },
    { t: 'Linee di Beau', d: 'Solchi trasversali sulla lamina dovuti a un rallentamento temporaneo della matrice (febbre, malattia, trauma).' },
    { t: 'Leuconichia', d: 'Macchioline o strisce bianche sulla lamina, di solito da piccoli traumi alla matrice.' },
    { t: 'Onicoressi', d: 'Striature longitudinali e fragilità della lamina che si spacca per il lungo.' },
    { t: 'Onicoschisi', d: 'Sfogliamento a strati del bordo libero.' },
    { t: 'Melanonichia', d: 'Banda o colorazione bruno-nera della lamina. Se è singola, larga, nuova o si estende sulla pelle va vista dal dermatologo.' },
    { t: 'Segno di Hutchinson', d: 'Pigmento scuro che dalla lamina si estende alla pelle intorno: segnale d\'allarme da far valutare subito.' },
    { t: 'Granuloma piogenico', d: 'Piccola massa rossa di tessuto che cresce in fretta e sanguina facilmente: non si tocca, si invia al medico.' },
    { t: 'Sindrome dell\'unghia verde', d: 'Colorazione verde-nera da batteri (Pseudomonas), spesso sotto un sollevamento; non è muffa.' },
    { t: 'Ematoma subungueale', d: 'Raccolta di sangue sotto la lamina dopo un trauma; si sposta in avanti con la crescita.' },
    { t: 'Detersione', d: 'Rimozione dello sporco con acqua e detergente: viene sempre prima della disinfezione.' },
    { t: 'Sanificazione', d: 'Pulizia che riduce i germi a un livello sicuro su ambienti, arredi e biancheria.' },
    { t: 'Disinfezione', d: 'Eliminazione della maggior parte dei germi con prodotti chimici; può essere di livello basso, intermedio o alto.' },
    { t: 'Sterilizzazione', d: 'Eliminazione di ogni forma di vita, spore comprese; nel centro estetico si fa in autoclave a vapore.' },
    { t: 'Indicatore di processo', d: 'Striscia sulla busta che cambia colore quando è passata in autoclave (non prova da sola la sterilità).' },
    { t: 'Registro di sterilizzazione', d: 'Documento a pagine numerate con numero, data, parametri, test e firma di ogni ciclo di autoclave.' },
    { t: 'UNI EN 13060', d: 'Norma tecnica sulle piccole sterilizzatrici a vapore (classi B, N, S).' },
    { t: 'Aspirazione localizzata', d: 'Aspiratore da tavolo o cappa che cattura polvere e vapori vicino alla fonte.' },
    { t: 'FFP2', d: 'Facciale filtrante contro le polveri (norma EN 149); non protegge dai vapori.' },
    { t: 'Patch test', d: 'Test allergologico fatto dal dermatologo applicando le sostanze sulla pelle della schiena.' },
    { t: 'Sensibilizzazione', d: 'Fase in cui l\'organismo "impara" a riconoscere una sostanza: dopo, ogni contatto può dare allergia.' },
    { t: 'DMTA (DMPT)', d: 'N,N-dimetil-p-toluidina: accelerante di liquidi acrilici e attivatori dip, vietato nei cosmetici UE dal 1/9/2025.' },
    { t: 'Allegato II e III', d: 'Elenchi del Reg. CE 1223/2009: sostanze vietate (II) e sostanze ammesse con limiti (III).' },
    { t: 'CMR', d: 'Sostanza cancerogena, mutagena o tossica per la riproduzione; nei cosmetici UE è di norma vietata.' },
    { t: 'SDS', d: 'Scheda di dati di sicurezza: dice pericoli, DPI, conservazione, smaltimento e primo soccorso di un prodotto.' },
    { t: 'PAO', d: 'Period After Opening: mesi in cui un cosmetico si può usare dopo l\'apertura (simbolo del vasetto aperto).' },
    { t: 'Responsabile tecnico', d: 'Persona qualificata estetista, presente in sede, indicata nella SCIA per ogni locale.' },
    { t: 'ComUnica', d: 'Pratica telematica unica per iscrivere l\'impresa al Registro delle Imprese e informare Fisco, INPS e INAIL.' },
    { t: 'Polimerizzazione', d: 'Reazione in cui piccole molecole si uniscono in una rete solida: è il modo in cui gel e acrilico induriscono.' },
    { t: 'Oligomero', d: 'Catenella di poche unità già unite; dà corpo e flessibilità ai gel.' },
    { t: 'Hard gel', d: 'Gel molto reticolato, non si scioglie in acetone: si rimuove limando.' },
    { t: 'Builder autolivellante', d: 'Costruttore fluido che si distende da solo creando una superficie liscia.' },
    { t: 'PMMA', d: 'Polimetil metacrilato: le perline della polvere per acrilico e dip.' },
    { t: 'Perossido di benzoile (BPO)', d: 'Iniziatore contenuto nella polvere acrilica che, a contatto con il liquido, avvia la reazione.' },
    { t: 'Inibitore', d: 'Sostanza aggiunta in tracce al monomero per evitare che indurisca nel flacone.' },
    { t: 'Dappen dish', d: 'Bicchierino (meglio con coperchio) per il monomero durante il lavoro con l\'acrilico.' },
    { t: 'Resina cianoacrilica', d: 'Resina a presa rapida (famiglia della colla per tip) usata in fibra, dip e colle.' },
    { t: 'Attivatore', d: 'Liquido che fa indurire la resina di fibra e dip senza lampada.' },
    { t: 'Dip powder', d: 'Sistema con base in resina, polvere colorata, attivatore e top; non usa la lampada.' },
    { t: 'Press-on', d: 'Unghie preformate e decorate da incollare con colla o linguette adesive.' },
    { t: 'Nanometro (nm)', d: 'Unità con cui si misura la lunghezza d\'onda della luce delle lampade (es. 365 nm, 405 nm).' },
    { t: 'Irradianza', d: 'Quantità di luce che arriva su una superficie: conta più dei watt della lampada.' },
    { t: 'INCI', d: 'Nomenclatura internazionale degli ingredienti cosmetici, obbligatoria in etichetta.' },
    { t: 'Scheda tecnica', d: 'Documento del produttore con modo d\'uso, lampada, tempi e rimozione di un prodotto.' },
    { t: 'Grana', d: 'Numero che indica quanto è abrasiva una lima: più è basso, più la lima è grossa e toglie materiale.' },
    { t: 'Lima in vetro', d: 'Lima non porosa che si può pulire e disinfettare; adatta all\'unghia naturale.' },
    { t: 'RPM', d: 'Giri al minuto della punta della fresa.' },
    { t: 'Coppia (torque)', d: 'Forza del motore della fresa: con una buona coppia la velocità resta costante quando appoggi la punta.' },
    { t: 'Gambo 3/32"', d: 'Diametro standard (2,35 mm) delle punte professionali per fresa.' },
    { t: 'Punta diamantata', d: 'Punta rivestita di polvere di diamante, per zona cuticolare (pelle morta) e unghia naturale.' },
    { t: 'Punta in ceramica', d: 'Punta scanalata in ceramica per il prodotto artificiale; scalda poco.' },
    { t: 'Punta di sicurezza', d: 'Punta con estremità arrotondata o liscia per lavorare vicino alle pieghe senza tagliare.' },
    { t: 'Anelli di fuoco', d: 'Solchi circolari sulla lamina causati da una punta della fresa inclinata.' },
    { t: 'Banda abrasiva', d: 'Cilindretto di carta abrasiva su mandrino in gomma per fresa; monouso.' },
    { t: 'Curetta', d: 'Piccolo strumento a cucchiaio per togliere la cuticola aderente; si sterilizza.' },
    { t: 'Kolinsky', d: 'Setole naturali usate nei pennelli per acrilico di qualità.' },
    { t: 'Dotter', d: 'Bastoncino con una sferetta in punta per fare puntini e decorazioni.' },
    { t: 'Punto d\'appoggio', d: 'Dito (di solito il mignolo) appoggiato sulla mano della cliente per dare stabilità a fresa o pennello.' }
  ];

  // esercizi ordinati secondo l'ordine dei moduli
  var order = {};
  modules.forEach(function (m, i) { order[m.id] = i; });
  exercises.sort(function (a, b) { return order[a.module] - order[b.module]; });

  window.NAILX = { modules: modules, exercises: exercises, quiz: quiz, glossary: glossary };
})();
