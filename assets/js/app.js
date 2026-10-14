/* NailX – motore del corso: rendering pagine, progressi, quiz, esercizi */
(function () {
  'use strict';
  var D = window.NAILX;
  var LEVELS = { base: 'Base', inter: 'Intermedio', avanz: 'Avanzato' };

  /* ---------- storage (sempre protetto: può non essere disponibile) ---------- */
  var KEY = 'nailx-progress-v1';
  function load() {
    try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; }
  }
  var state = load();
  state.lessons = state.lessons || {};
  state.checks = state.checks || {};
  state.quiz = state.quiz || {};
  state.quizAt = state.quizAt || {};
  state.exAt = state.exAt || {};
  function save() {
    state.updatedAt = Date.now();
    try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) { /* ignore */ }
    if (window.NAILX_CLOUD) window.NAILX_CLOUD.queuePush();
    refreshNavProgress();
  }
  // area online (Supabase) attiva solo se configurata in assets/js/config.js
  function cloudEnabled() {
    var c = window.NAILX_CONFIG;
    return !!(c && c.supabaseUrl && c.supabaseAnonKey);
  }

  /* ---------- helpers ---------- */
  function $(sel, root) { return (root || document).querySelector(sel); }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function qs(name) { return new URLSearchParams(location.search).get(name); }
  function reducedMotion() { return !!(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches); }
  function scrollToEl(el, block) { if (el) el.scrollIntoView({ behavior: reducedMotion() ? 'auto' : 'smooth', block: block || 'start' }); }
  function allLessons() {
    var out = [];
    D.modules.forEach(function (m) {
      m.lessons.forEach(function (l) { out.push({ m: m, l: l }); });
    });
    return out;
  }
  function lessonKey(m, l) { return m.id + '/' + l.id; }
  function lessonUrl(m, l) { return 'corso.html?m=' + m.id + '&l=' + l.id; }
  function moduleDone(m) {
    return m.lessons.filter(function (l) { return state.lessons[lessonKey(m, l)]; }).length;
  }
  function pct(a, b) { return b ? Math.round((a / b) * 100) : 0; }
  function badge(level) { return '<span class="badge ' + level + '">' + LEVELS[level] + '</span>'; }
  function progressBar(p, label) {
    return '<div class="progress"><i style="width:' + p + '%"></i></div>' +
      (label ? '<div class="progress-label">' + label + '</div>' : '');
  }

  /* ---------- header / footer / tema ---------- */
  var THEME_KEY = 'nailx-theme';
  function applyTheme(t) {
    if (t) document.documentElement.setAttribute('data-theme', t);
    else document.documentElement.removeAttribute('data-theme');
  }
  try { applyTheme(localStorage.getItem(THEME_KEY)); } catch (e) { /* ignore */ }

  function header(active) {
    var links = [
      ['index.html', 'home', 'Home'],
      ['programma.html', 'programma', 'Programma'],
      ['corso.html', 'corso', 'Lezioni'],
      ['esercizi.html', 'esercizi', 'Esercizi'],
      ['ripasso.html', 'ripasso', 'Ripasso'],
      ['quiz.html', 'quiz', 'Quiz'],
      ['glossario.html', 'glossario', 'Glossario'],
      ['attestato.html', 'attestato', 'Attestato']
    ];
    if (cloudEnabled()) links.push(['accedi.html', 'accedi', 'Accedi']);
    var h = document.createElement('header');
    h.className = 'site-header';
    h.innerHTML = '<nav class="nav" aria-label="Menu principale"><a class="brand" href="index.html" aria-label="NailX, pagina iniziale">' +
      '<img src="assets/img/logo.svg" alt="" width="30" height="30"><span>Nail<b>X</b></span></a>' +
      '<div class="nav-links">' + links.map(function (x) {
        return '<a href="' + x[0] + '"' + (x[1] === active ? ' class="active" aria-current="page"' : '') + (x[1] === 'accedi' ? ' id="nav-account"' : '') + '>' + x[2] + '</a>';
      }).join('') + '</div>' +
      '<a class="nav-progress" href="index.html#progresso" title="Avanzamento del corso"><i aria-hidden="true"></i><span>0%</span></a>' +
      '<button class="theme-btn" type="button"></button></nav>';
    document.body.insertBefore(h, document.body.firstChild);
    // salto al contenuto principale (primo elemento raggiungibile con Tab)
    var main = document.querySelector('main');
    if (main) {
      if (!main.id) main.id = 'contenuto';
      main.setAttribute('tabindex', '-1');
      var skip = document.createElement('a');
      skip.className = 'skip-link';
      skip.href = '#' + main.id;
      skip.textContent = 'Vai al contenuto';
      skip.addEventListener('click', function (e) { e.preventDefault(); main.focus(); main.scrollIntoView(); });
      document.body.insertBefore(skip, document.body.firstChild);
    }
    refreshNavProgress();
    var themeBtn = $('.theme-btn', h);
    function isDark() {
      var cur = document.documentElement.getAttribute('data-theme');
      return cur ? cur === 'dark' : !!(window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches);
    }
    function themeLabel() {
      var dark = isDark();
      themeBtn.textContent = dark ? '☀' : '☾';
      themeBtn.title = dark ? 'Passa al tema chiaro' : 'Passa al tema scuro';
      themeBtn.setAttribute('aria-label', themeBtn.title);
    }
    themeLabel();
    themeBtn.addEventListener('click', function () {
      var next = isDark() ? 'light' : 'dark';
      applyTheme(next);
      try { localStorage.setItem(THEME_KEY, next); } catch (e) { /* ignore */ }
      themeLabel();
    });
    if (window.matchMedia) {
      var mq = matchMedia('(prefers-color-scheme: dark)');
      if (mq.addEventListener) mq.addEventListener('change', themeLabel);
    }
    // menu a scorrimento su schermi stretti: sfumatura sul lato dove ci sono altre voci
    var nl = $('.nav-links', h);
    function navFade() {
      var max = nl.scrollWidth - nl.clientWidth;
      nl.classList.toggle('fade-l', max > 2 && nl.scrollLeft > 2);
      nl.classList.toggle('fade-r', max > 2 && nl.scrollLeft < max - 2);
    }
    var act = $('.active', nl);
    if (act && nl.scrollWidth > nl.clientWidth) nl.scrollLeft = Math.max(0, act.offsetLeft - nl.clientWidth / 2 + act.offsetWidth / 2);
    nl.addEventListener('scroll', navFade, { passive: true });
    nl.addEventListener('focusin', function (e) { if (e.target.scrollIntoView) e.target.scrollIntoView({ block: 'nearest', inline: 'nearest' }); });
    addEventListener('resize', navFade);
    navFade();
    var f = document.createElement('footer');
    f.innerHTML = 'NailX · Corso di ricostruzione unghie · Corso professionalizzante non abilitante: non sostituisce ' +
      'la qualifica di estetista prevista dalla legge né il parere medico.<br>' +
      '<a href="valore-attestato.html">Valore dell\'attestato</a> · <a href="privacy.html">Privacy e cookie</a> · <a href="verifica.html">Verifica un attestato</a>';
    document.body.appendChild(f);
  }

  /* ---------- stato del corso (calcolato in automatico) ---------- */
  function lessonsDone() { return allLessons().filter(function (x) { return state.lessons[lessonKey(x.m, x.l)]; }).length; }
  function coursePct() {
    // lezioni 80%, esame finale 20%
    var l = allLessons().length;
    return Math.round(80 * lessonsDone() / l + ((state.quiz.final || 0) >= 80 ? 20 : 0));
  }
  function refreshNavProgress() {
    var el = document.querySelector('.nav-progress');
    if (!el) return;
    var p = coursePct();
    el.querySelector('span').textContent = p + '%';
    el.querySelector('i').style.setProperty('--p', p);
    el.setAttribute('aria-label', 'Avanzamento del corso: ' + p + '%');
  }
  function moduleStatus(m) {
    var d = moduleDone(m), q = state.quiz[m.id];
    if (d === m.lessons.length && (!D.quiz[m.id] || q >= 80)) return ['done', 'Completato ✓'];
    if (d === m.lessons.length) return ['quiz', 'Manca il quiz'];
    if (d > 0) return ['progress', 'In corso'];
    return ['todo', 'Da iniziare'];
  }
  function nextStep() {
    var last = state.last && allLessons().filter(function (x) { return lessonKey(x.m, x.l) === state.last; })[0];
    if (last && !state.lessons[state.last]) return { t: 'Riprendi la lezione', d: last.l.title, href: lessonUrl(last.m, last.l), b: 'Riprendi', short: 'Riprendi: ' + last.l.title };
    for (var i = 0; i < D.modules.length; i++) {
      var m = D.modules[i];
      var todo = m.lessons.filter(function (l) { return !state.lessons[lessonKey(m, l)]; })[0];
      if (todo) {
        return { t: lessonsDone() ? 'Prossima lezione' : 'Inizia il corso', d: 'Modulo ' + m.n + ' · ' + todo.title, href: lessonUrl(m, todo), b: lessonsDone() ? 'Continua' : 'Inizia', short: 'Continua: ' + todo.title };
      }
      if (D.quiz[m.id] && (state.quiz[m.id] || 0) < 80) {
        return { t: 'Verifica il modulo ' + m.n, d: 'Quiz: ' + m.title + (state.quiz[m.id] != null ? ' (ultimo ' + state.quiz[m.id] + '%, obiettivo 80%)' : ''), href: 'quiz.html?m=' + m.id, b: 'Fai il quiz', short: 'Quiz del modulo ' + m.n };
      }
    }
    if ((state.quiz.final || 0) < 80) return { t: 'Tutte le lezioni completate!', d: 'Ora l\'esame finale: 40 domande, soglia 80%.', href: 'quiz.html?m=final', b: 'Esame finale', short: 'Vai all\'esame finale' };
    return { t: 'Corso completato 🎉', d: 'Scarica o aggiorna il tuo attestato di fine corso.', href: 'attestato.html', b: 'Attestato', short: 'Il tuo attestato' };
  }

  /* ---------- avvisi (toast) ---------- */
  var toastRegion = null;
  function toast(html, ms) {
    if (!toastRegion) {
      toastRegion = document.createElement('div');
      toastRegion.className = 'toast-region';
      toastRegion.setAttribute('role', 'status');
      toastRegion.setAttribute('aria-live', 'polite');
      document.body.appendChild(toastRegion);
    }
    var t = document.createElement('div');
    t.className = 'toast';
    t.innerHTML = html;
    toastRegion.appendChild(t);
    requestAnimationFrame(function () { t.classList.add('show'); });
    var close = function () { t.classList.remove('show'); setTimeout(function () { t.remove(); }, 300); };
    setTimeout(close, ms || 6000);
    return { el: t, close: close };
  }

  /* ---------- HOME ---------- */
  function renderHome() {
    var lessons = allLessons();
    var done = lessons.filter(function (x) { return state.lessons[lessonKey(x.m, x.l)]; }).length;
    var exDone = D.exercises.filter(function (e) { return exScore(e) === 100; }).length;
    var quizDone = Object.keys(state.quiz).length;
    $('#stats').innerHTML =
      stat(D.modules.length, 'moduli') + stat(lessons.length, 'lezioni') + stat('≈' + hours(totalMinutes().lessons + totalMinutes().exercises), 'ore di formazione') +
      stat(D.exercises.length, 'esercizi pratici') + stat(countQuiz(), 'domande quiz');
    $('#global-progress').innerHTML = progressBar(pct(done, lessons.length),
      done + ' di ' + lessons.length + ' lezioni completate · ' + exDone + ' esercizi superati · ' + quizDone + ' quiz svolti');
    var ns = nextStep();
    $('#continue').href = ns.href;
    $('#continue').textContent = done ? ns.short : 'Inizia il corso';
    if ($('#nextstep')) {
      $('#nextstep').innerHTML = '<div class="next-card"><div class="ring" style="--p:' + coursePct() + '"><span>' + coursePct() + '%</span></div>' +
        '<div class="next-txt"><small>Prossimo passo</small><strong>' + esc(ns.t) + '</strong><span>' + esc(ns.d) + '</span></div>' +
        '<a class="btn" href="' + ns.href + '">' + esc(ns.b) + ' →</a></div>';
    }

    $('#modules').innerHTML = D.modules.map(function (m) {
      var d = moduleDone(m), st = moduleStatus(m);
      return '<article class="card mod-' + st[0] + '"><div style="display:flex;justify-content:space-between;align-items:center;gap:.4rem">' +
        '<span class="mod-num">' + String(m.n).padStart(2, '0') + '</span><span class="status s-' + st[0] + '">' + st[1] + '</span>' + badge(m.level) + '</div>' +
        '<h3><a class="stretch" href="' + lessonUrl(m, m.lessons[0]) + '">' + esc(m.title) + '</a></h3>' +
        '<p>' + esc(m.desc) + '</p>' + progressBar(pct(d, m.lessons.length), d + '/' + m.lessons.length + ' lezioni') +
        '</article>';
    }).join('');
  }
  function stat(n, label) { return '<div class="stat"><b>' + n + '</b><span>' + label + '</span></div>'; }
  function countQuiz() {
    return Object.keys(D.quiz).reduce(function (a, k) { return a + D.quiz[k].length; }, 0);
  }

  /* ---------- CORSO ---------- */
  function renderCourse() {
    var m = D.modules.filter(function (x) { return x.id === qs('m'); })[0] || D.modules[0];
    var l = m.lessons.filter(function (x) { return x.id === qs('l'); })[0] || m.lessons[0];
    var list = allLessons();
    var idx = list.findIndex(function (x) { return x.m === m && x.l === l; });
    var prev = list[idx - 1], next = list[idx + 1];
    document.title = l.title + ' · NailX';

    function side() {
      $('#sidebar').innerHTML = D.modules.map(function (mm) {
        return '<details' + (mm === m ? ' open' : '') + '><summary><span class="n">' + mm.n + '</span>' +
          esc(mm.title) + '</summary><ul>' + mm.lessons.map(function (ll) {
            var cls = [];
            if (mm === m && ll === l) cls.push('current');
            if (state.lessons[lessonKey(mm, ll)]) cls.push('done');
            return '<li><a class="' + cls.join(' ') + '" href="' + lessonUrl(mm, ll) + '"' + (mm === m && ll === l ? ' aria-current="page"' : '') + '>' + esc(ll.title) +
              (state.lessons[lessonKey(mm, ll)] ? '<span class="sr-only"> (completata)</span>' : '') + '</a></li>';
          }).join('') + '</ul></details>';
      }).join('');
    }
    side();

    var key = lessonKey(m, l);
    var relatedEx = D.exercises.filter(function (e) { return e.module === m.id; });
    var html = '<div class="crumbs">Modulo ' + m.n + ' · ' + esc(m.title) + '</div>' +
      '<h1>' + esc(l.title) + '</h1>' +
      '<div class="meta">' + badge(m.level) + '<span>⏱ ' + (l.min || 10) + ' min di lettura</span>' +
      '<span>Lezione ' + (m.lessons.indexOf(l) + 1) + ' di ' + m.lessons.length + '</span></div>' +
      (l.simple ? '<div class="box simple"><strong class="t">In parole semplici</strong>' + esc(l.simple) + '</div>' : '') +
      '<nav class="toc" id="toc" hidden aria-label="In questa lezione"></nav>' +
      '<div class="lesson-body">' + l.html + '</div>' + videosHtml(l.videos);
    var isLast = m.lessons.indexOf(l) === m.lessons.length - 1;
    if (isLast && m.summary && m.summary.length) {
      html += '<div class="keypoints"><strong class="t">Punti chiave del modulo ' + m.n + '</strong><ol>' +
        m.summary.map(function (s) { return '<li>' + esc(s) + '</li>'; }).join('') + '</ol></div>';
    }
    html += quickCheckHtml(m, l) +
      '<details class="notes"><summary>📝 I miei appunti su questa lezione</summary>' +
      '<textarea id="note" rows="5" placeholder="Scrivi qui cosa vuoi ricordare: restano salvati solo in questo browser."></textarea>' +
      '<small class="muted" id="note-st"></small></details>';
    if (relatedEx.length && isLast) {
      html += '<div class="box info"><strong class="t">Mettiti alla prova</strong>Esercizi pratici di questo modulo: ' +
        relatedEx.map(function (e) { return '<a href="esercizi.html#' + e.id + '">' + esc(e.title) + '</a>'; }).join(' · ') +
        (D.quiz[m.id] ? ' — oppure fai il <a href="quiz.html?m=' + m.id + '">quiz del modulo</a>.' : '') + '</div>';
    }
    if (l.sources && l.sources.length) {
      html += '<hr><div class="sources"><strong>Fonti e approfondimenti</strong><ul>' + l.sources.map(function (s) {
        return '<li><a href="' + esc(s) + '" target="_blank" rel="noopener">' + esc(s) + '</a></li>';
      }).join('') + '</ul></div>';
    }
    html += '<div class="lesson-nav">' +
      (prev ? '<a class="btn ghost small" href="' + lessonUrl(prev.m, prev.l) + '">← ' + esc(prev.l.title) + '</a>' : '<span></span>') +
      '<button class="btn small" id="mark" type="button"></button>' +
      (next ? '<a class="btn small" href="' + lessonUrl(next.m, next.l) + '">' + esc(next.l.title) + ' →</a>' : '<a class="btn small" href="quiz.html?m=final">Esame finale →</a>') +
      '</div>';
    $('#lesson').innerHTML = html;
    linkGlossary($('#lesson'));
    lessonExtras(key);

    var mark = $('#mark');
    function upd() { mark.textContent = state.lessons[key] ? '✓ Completata' : 'Segna come completata'; mark.classList.toggle('ghost', !!state.lessons[key]); }
    upd();
    state.last = key;
    save();
    var userUndid = false;
    function complete(auto) {
      var before = lessonsDone(), modBefore = moduleDone(m);
      state.lessons[key] = Date.now();
      save(); upd(); side();
      if (auto) {
        var t = toast('✓ Lezione completata in automatico. <button type="button" class="linklike">Annulla</button>');
        t.el.querySelector('button').addEventListener('click', function () {
          delete state.lessons[key]; userUndid = true; save(); upd(); side(); t.close();
        });
      }
      // traguardi
      if (modBefore < m.lessons.length && moduleDone(m) === m.lessons.length) {
        toast('🎉 Hai completato il modulo <strong>' + esc(m.title) + '</strong>' +
          (D.quiz[m.id] ? ' · <a href="quiz.html?m=' + m.id + '">fai il quiz</a>' : ''), 8000);
      }
      if (before < list.length && lessonsDone() === list.length) {
        toast('🏁 Tutte le lezioni completate! <a href="quiz.html?m=final">Vai all\'esame finale</a>', 9000);
      }
    }
    mark.addEventListener('click', function () {
      if (state.lessons[key]) { delete state.lessons[key]; userUndid = true; save(); upd(); side(); }
      else complete(false);
    });
    // completamento automatico: fine della lezione raggiunta dopo un tempo minimo di lettura
    var minMs = Math.min(30, (l.min || 10) * 6) * 1000, t0 = Date.now(), seenEnd = false, timer = null;
    function tryAuto() {
      if (state.lessons[key] || userUndid || !seenEnd) return;
      var wait = minMs - (Date.now() - t0);
      if (wait > 0) { clearTimeout(timer); timer = setTimeout(tryAuto, wait); return; }
      complete(true);
    }
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        if (entries.some(function (e) { return e.isIntersecting; })) { seenEnd = true; tryAuto(); }
      }, { threshold: 0.5 }).observe($('.lesson-nav'));
    }
    var mt = $('.menu-toggle');
    mt.setAttribute('aria-controls', 'sidebar');
    mt.setAttribute('aria-expanded', 'false');
    mt.addEventListener('click', function () {
      var open = $('#sidebar').classList.toggle('open');
      mt.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  /* ---------- extra della lezione: indice, barra di lettura, verifica rapida, appunti ---------- */
  function hashStr(s) { var h = 0; for (var i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) | 0; return Math.abs(h); }
  function quickCheckHtml(m, l) {
    var pool = D.quiz[m.id] || [];
    if (pool.length < 2) return '';
    var n = m.lessons.indexOf(l), h = hashStr(m.id + l.id);
    var picks = [pool[(n * 2 + h) % pool.length], pool[(n * 2 + 1 + h) % pool.length]];
    if (picks[0] === picks[1]) picks.pop();
    return '<section class="quick-check"><h2>Verifica rapida</h2><p class="muted">Due domande per fissare i concetti del modulo. Non incidono sul punteggio.</p>' +
      picks.map(function (q, i) {
        var opts = shuffle(q.o.map(function (o, j) { return { t: o, ok: j === q.a }; }));
        var hid = 'qc-' + (i + 1);
        return '<div class="quiz-q" role="group" aria-labelledby="' + hid + '"><h3 id="' + hid + '">' + (i + 1) + '. ' + esc(q.q) + '</h3>' + opts.map(function (o) {
          return '<button type="button" class="opt" data-ok="' + (o.ok ? 1 : 0) + '">' + esc(o.t) + '</button>';
        }).join('') + FB + '<div class="explain" hidden>' + esc(q.e || '') + '</div></div>';
      }).join('') + '</section>';
  }
  // riga di esito letta dai lettori di schermo (aria-live) e visibile: l'esito non è affidato solo al colore
  var FB = '<p class="fb" aria-live="polite"></p>';
  function feedback(box, chosen, timeout) {
    var fb = box && box.querySelector('.fb'); if (!fb) return;
    var right = box.querySelector('.opt.right');
    var ok = !!chosen && chosen.dataset.ok === '1';
    fb.className = 'fb ' + (ok ? 'ok' : 'no');
    fb.textContent = ok ? '✓ Risposta corretta.' : (timeout ? '⏱ Tempo scaduto. ' : '✗ Risposta sbagliata. ') +
      (right ? 'Quella corretta è: «' + right.textContent + '».' : '');
  }
  var NOTES_KEY = 'nailx-notes-v1';
  function loadNotes() { try { return JSON.parse(localStorage.getItem(NOTES_KEY)) || {}; } catch (e) { return {}; } }
  function lessonExtras(key) {
    var body = $('.lesson-body');
    // indice della lezione
    var hs = body ? body.querySelectorAll('h2') : [];
    if (hs.length >= 3) {
      $('#toc').innerHTML = '<strong>In questa lezione</strong><ol>' + Array.prototype.map.call(hs, function (h, i) {
        h.id = 'sez-' + (i + 1);
        return '<li><a href="#sez-' + (i + 1) + '">' + esc(h.textContent) + '</a></li>';
      }).join('') + '</ol>';
      $('#toc').hidden = false;
    }
    // barra di lettura
    var bar = document.createElement('div');
    bar.className = 'read-bar'; bar.innerHTML = '<i></i>';
    document.body.appendChild(bar);
    function onScroll() {
      var el = $('#lesson'), r = el.getBoundingClientRect();
      var total = el.offsetHeight - innerHeight, done = Math.min(Math.max(-r.top, 0), Math.max(total, 1));
      bar.firstChild.style.width = (total > 0 ? done / total * 100 : 100) + '%';
    }
    addEventListener('scroll', onScroll, { passive: true }); onScroll();
    // verifica rapida
    var qc = $('.quick-check');
    if (qc) qc.addEventListener('click', function (ev) {
      var b = ev.target.closest('.opt'); if (!b || b.disabled) return;
      var box = b.parentNode;
      box.querySelectorAll('.opt').forEach(function (o) { o.disabled = true; if (o.dataset.ok === '1') o.classList.add('right'); });
      if (b.dataset.ok !== '1') b.classList.add('wrong');
      box.querySelector('.explain').hidden = false;
      feedback(box, b);
    });
    // appunti (solo in questo browser)
    var ta = $('#note'), st = $('#note-st'), notes = loadNotes(), tmr;
    if (notes[key]) { ta.value = notes[key]; ta.closest('details').open = true; }
    ta.addEventListener('input', function () {
      clearTimeout(tmr);
      tmr = setTimeout(function () {
        var n = loadNotes();
        if (ta.value.trim()) n[key] = ta.value; else delete n[key];
        try { localStorage.setItem(NOTES_KEY, JSON.stringify(n)); st.textContent = 'Salvato'; } catch (e) { st.textContent = 'Impossibile salvare in questo browser'; }
      }, 400);
    });
  }

  /* ---------- PROGRAMMA ---------- */
  function totalMinutes() {
    var lm = allLessons().reduce(function (a, x) { return a + (x.l.min || 10); }, 0);
    var em = D.exercises.reduce(function (a, e) { return a + exMinutes(e); }, 0);
    return { lessons: lm, exercises: em };
  }
  function hours(min) { return Math.round(min / 60); }
  function plain(html) { var d = document.createElement('div'); d.innerHTML = html.replace(/<figure[\s\S]*?<\/figure>/g, ' '); return d.textContent.replace(/\s+/g, ' '); }
  function renderProgram() {
    var t = totalMinutes(), lessons = allLessons();
    $('#pstats').innerHTML = stat(D.modules.length, 'moduli') + stat(lessons.length, 'lezioni') +
      stat('≈' + hours(t.lessons), 'ore di teoria') + stat('≈' + hours(t.exercises), 'ore di pratica guidata') +
      stat(countQuiz(), 'domande d\'esame') + stat(D.glossary.length, 'termini nel glossario');
    $('#syllabus').innerHTML = D.modules.map(function (m) {
      var min = m.lessons.reduce(function (a, l) { return a + (l.min || 10); }, 0);
      var ex = D.exercises.filter(function (e) { return e.module === m.id; });
      return '<details class="syl"><summary><span class="mod-num">' + String(m.n).padStart(2, '0') + '</span>' +
        '<span class="syl-t"><strong>' + esc(m.title) + '</strong><small>' + m.lessons.length + ' lezioni · ' + min + ' min · ' +
        ex.length + (ex.length === 1 ? ' esercizio' : ' esercizi') + (D.quiz[m.id] ? ' · quiz da ' + D.quiz[m.id].length + ' domande' : '') + '</small></span>' + badge(m.level) + '</summary>' +
        '<p>' + esc(m.desc) + '</p>' +
        (m.summary ? '<p><strong>Al termine saprai:</strong></p><ul>' + m.summary.map(function (s) { return '<li>' + esc(s) + '</li>'; }).join('') + '</ul>' : '') +
        '<p><strong>Lezioni</strong></p><ol>' + m.lessons.map(function (l) {
          return '<li><a href="' + lessonUrl(m, l) + '">' + esc(l.title) + '</a> <small class="muted">· ' + (l.min || 10) + ' min' +
            (state.lessons[lessonKey(m, l)] ? ' · ✓ completata' : '') + '</small></li>';
        }).join('') + '</ol>' +
        (ex.length ? '<p><strong>Esercizi pratici</strong></p><ul>' + ex.map(function (e) {
          return '<li><a href="esercizi.html#' + e.id + '">' + esc(e.title) + '</a> <small class="muted">· ' + esc(e.time) + '</small></li>';
        }).join('') + '</ul>' : '') +
        '<p class="btn-row"><a class="btn small" href="' + lessonUrl(m, m.lessons[0]) + '">Apri il modulo</a>' +
        '<a class="btn ghost small" href="dispensa.html?m=' + m.id + '">Dispensa del modulo</a></p></details>';
    }).join('');
    // ricerca nelle lezioni
    var idx = lessons.map(function (x) { var raw = x.l.title + ' ' + (x.l.simple || '') + ' ' + plain(x.l.html); return { m: x.m, l: x.l, raw: raw, txt: raw.toLowerCase() }; });
    var inp = $('#search'), out = $('#results');
    inp.addEventListener('input', function () {
      var q = inp.value.trim().toLowerCase();
      if (q.length < 3) { out.innerHTML = ''; return; }
      var words = q.split(/\s+/);
      var hits = idx.filter(function (x) { return words.every(function (w) { return x.txt.indexOf(w) >= 0; }); }).slice(0, 25);
      out.innerHTML = hits.length ? '<ul class="results">' + hits.map(function (x) {
        var i = x.txt.indexOf(words[0]), s = Math.max(0, i - 70);
        var snip = x.raw.slice(s, i + 110);
        return '<li><a href="' + lessonUrl(x.m, x.l) + '"><strong>' + esc(x.l.title) + '</strong></a> <small class="muted">· Modulo ' + x.m.n + '</small><br><small>…' + esc(snip) + '…</small></li>';
      }).join('') + '</ul>' : '<p class="muted">Nessuna lezione contiene queste parole.</p>';
    });
  }

  /* ---------- DISPENSA (stampabile / PDF) ---------- */
  function renderHandbook() {
    var only = qs('m');
    var mods = D.modules.filter(function (m) { return !only || m.id === only; });
    if (!mods.length) mods = D.modules;
    var t = totalMinutes();
    var title = mods.length === 1 ? 'Modulo ' + mods[0].n + ' · ' + mods[0].title : 'Manuale completo del corso';
    document.title = title + ' · Dispensa NailX';
    var html = '<div class="hb-tools no-print"><p class="muted">Usa <strong>Salva in PDF</strong> per avere la dispensa sul telefono o stamparla. ' +
      'Suggerimento: nella finestra di stampa scegli "Salva come PDF".</p><div class="btn-row">' +
      '<button class="btn" type="button" id="print">🖨 Salva in PDF / Stampa</button>' +
      (only ? '<a class="btn ghost" href="dispensa.html">Manuale completo</a>' : '') +
      '<a class="btn ghost" href="programma.html">← Programma</a></div></div>' +
      '<section class="hb-cover"><img src="assets/img/logo.svg" alt="" width="72" height="72"><h1>' + esc(title) + '</h1>' +
      '<p>Corso di ricostruzione unghie NailX · Dispensa didattica</p>' +
      (mods.length > 1 ? '<p class="muted">' + D.modules.length + ' moduli · ' + allLessons().length + ' lezioni · circa ' + hours(t.lessons) + ' ore di teoria</p>' : '') +
      '</section>';
    if (mods.length > 1) {
      html += '<section class="hb-index"><h2>Indice</h2><ol>' + mods.map(function (m) {
        return '<li><a href="#mod-' + m.id + '">' + esc(m.title) + '</a><ol>' + m.lessons.map(function (l) {
          return '<li><a href="#les-' + m.id + '-' + l.id + '">' + esc(l.title) + '</a></li>';
        }).join('') + '</ol></li>';
      }).join('') + '</ol></section>';
    }
    html += mods.map(function (m) {
      return '<section class="hb-mod" id="mod-' + m.id + '"><p class="crumbs">Modulo ' + m.n + '</p><h1>' + esc(m.title) + '</h1><p class="lead">' + esc(m.desc) + '</p>' +
        (m.summary ? '<div class="keypoints"><strong class="t">Punti chiave</strong><ol>' + m.summary.map(function (s) { return '<li>' + esc(s) + '</li>'; }).join('') + '</ol></div>' : '') +
        m.lessons.map(function (l) {
          return '<article class="hb-lesson" id="les-' + m.id + '-' + l.id + '"><h2>' + m.n + '.' + (m.lessons.indexOf(l) + 1) + ' · ' + esc(l.title) + '</h2>' +
            (l.simple ? '<div class="box simple"><strong class="t">In parole semplici</strong>' + esc(l.simple) + '</div>' : '') +
            l.html.replace(/<h2>/g, '<h3>').replace(/<\/h2>/g, '</h3>') +
            (l.sources && l.sources.length ? '<p class="hb-src"><small>Fonti: ' + l.sources.map(esc).join(' · ') + '</small></p>' : '') + '</article>';
        }).join('') + '</section>';
    }).join('');
    var ps = document.createElement('style');
    ps.textContent = '@page { size: A4 portrait; margin: 14mm 12mm; }';
    document.head.appendChild(ps);
    $('#handbook').innerHTML = html;
    $('#print').addEventListener('click', function () { window.print(); });
  }

  /* ---------- ESERCIZI ---------- */
  function exScore(e) {
    var c = state.checks[e.id] || [];
    var n = c.filter(Boolean).length;
    return pct(n, e.checks.length);
  }
  function renderExercises() {
    var filter = 'all';
    var bar = $('#filters');
    var levels = [['all', 'Tutti']].concat(Object.keys(LEVELS).map(function (k) { return [k, LEVELS[k]]; }));
    bar.innerHTML = levels.map(function (x) {
      return '<button class="chip' + (x[0] === 'all' ? ' active' : '') + '" data-f="' + x[0] + '" type="button" aria-pressed="' + (x[0] === 'all') + '">' + x[1] + '</button>';
    }).join('');
    bar.addEventListener('click', function (ev) {
      var b = ev.target.closest('.chip'); if (!b) return;
      filter = b.dataset.f;
      bar.querySelectorAll('.chip').forEach(function (c) { c.classList.toggle('active', c === b); c.setAttribute('aria-pressed', c === b ? 'true' : 'false'); });
      draw();
    });

    function modTitle(id) { var m = D.modules.filter(function (x) { return x.id === id; })[0]; return m ? m.title : ''; }

    function draw() {
      var hash = location.hash.slice(1);
      $('#exercises').innerHTML = D.exercises.filter(function (e) { return filter === 'all' || e.level === filter; })
        .map(function (e, i) {
          var c = state.checks[e.id] || [];
          return '<details class="ex" id="' + e.id + '"' + (hash === e.id ? ' open' : '') + '><summary>' +
            '<span class="mod-num" style="font-size:1.3rem">' + (D.exercises.indexOf(e) + 1) + '</span>' +
            '<h3>' + esc(e.title) + '</h3>' + badge(e.level) + '<span class="muted">⏱ ' + esc(e.time) + '</span>' +
            '<span class="score" data-score="' + e.id + '">' + exScore(e) + '%</span></summary>' +
            '<div class="ex-body"><div>' +
            '<p><strong>Obiettivo:</strong> ' + esc(e.goal) + '</p>' +
            '<p class="muted"><small>Modulo: ' + esc(modTitle(e.module)) + '</small></p>' +
            '<h4>Materiali</h4><ul>' + e.materials.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul>' +
            '<h4>Procedimento</h4><ol class="steps">' + e.steps.map(function (x) { return '<li>' + x + '</li>'; }).join('') + '</ol>' +
            '</div><div>' +
            (e.img ? '<figure><img src="assets/img/' + e.img + '" alt="' + esc(e.title) + '" loading="lazy"><figcaption>' + esc(e.caption || '') + '</figcaption></figure>' : '') +
            (e.imgs || []).map(function (src) {
              return '<figure><img src="assets/img/' + src + '" alt="Tavola di riferimento: ' + esc(e.title) + '" loading="lazy"></figure>';
            }).join('') +
            (e.img ? '<div class="photo-eval" data-ref="assets/img/' + e.img + '"><h4>Confronta con il tuo lavoro</h4>' +
              '<label class="btn small ghost photo-btn">📷 Scatta o scegli una foto<input type="file" accept="image/*" data-photo="' + e.id + '"></label>' +
              '<p class="muted"><small>La foto resta sul tuo dispositivo e non viene caricata online. Fotografa dall\'alto e di profilo, con luce uniforme.</small></p>' +
              '<div class="compare" hidden><div class="chips cmp-modes"><button type="button" class="chip active" data-mode="side">Affianca</button>' +
              '<button type="button" class="chip" data-mode="over">Sovrapponi</button></div>' +
              '<div class="cmp-stage side"><img class="ref" alt="Tavola di riferimento"><img class="mine" alt="La tua foto"></div>' +
              '<label class="cmp-range" hidden>Trasparenza della tua foto <input type="range" min="0" max="100" value="55"></label>' +
              '<p class="muted"><small>Ora rispondi alla checklist guardando la foto accanto alla tavola.</small></p></div></div>' : '') +
            '<h4>Auto-valutazione</h4><ul class="checklist">' + e.checks.map(function (x, j) {
              return '<li><label><input type="checkbox" data-ex="' + e.id + '" data-i="' + j + '"' + (c[j] ? ' checked' : '') + '> <span>' + esc(x) + '</span></label></li>';
            }).join('') + '</ul>' +
            '<div class="box warn"><strong class="t">Errori frequenti</strong><ul>' + e.mistakes.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul></div>' +
            '</div></div></details>';
        }).join('');
      if (hash) { var t = document.getElementById(hash); if (t) t.scrollIntoView(); }
    }
    draw();
    var photoUrls = {};
    $('#exercises').addEventListener('change', function (ev) {
      var inp = ev.target;
      if (inp.dataset.photo && inp.files && inp.files[0]) {
        var box = inp.closest('.photo-eval'), cmp = box.querySelector('.compare');
        if (photoUrls[inp.dataset.photo]) URL.revokeObjectURL(photoUrls[inp.dataset.photo]);
        photoUrls[inp.dataset.photo] = URL.createObjectURL(inp.files[0]);
        cmp.querySelector('.mine').src = photoUrls[inp.dataset.photo];
        cmp.querySelector('.ref').src = box.dataset.ref;
        cmp.hidden = false;
        return;
      }
    });
    $('#exercises').addEventListener('click', function (ev) {
      var b = ev.target.closest('.cmp-modes .chip'); if (!b) return;
      var cmp = b.closest('.compare'), over = b.dataset.mode === 'over';
      cmp.querySelectorAll('.cmp-modes .chip').forEach(function (c) { c.classList.toggle('active', c === b); });
      cmp.querySelector('.cmp-stage').className = 'cmp-stage ' + (over ? 'over' : 'side');
      cmp.querySelector('.cmp-range').hidden = !over;
      cmp.querySelector('.mine').style.opacity = over ? cmp.querySelector('.cmp-range input').value / 100 : '';
    });
    $('#exercises').addEventListener('input', function (ev) {
      if (ev.target.type !== 'range') return;
      ev.target.closest('.compare').querySelector('.mine').style.opacity = ev.target.value / 100;
    });
    $('#exercises').addEventListener('change', function (ev) {
      var cb = ev.target; if (!cb.dataset.ex) return;
      var arr = state.checks[cb.dataset.ex] = state.checks[cb.dataset.ex] || [];
      arr[+cb.dataset.i] = cb.checked;
      var e = D.exercises.filter(function (x) { return x.id === cb.dataset.ex; })[0];
      if (exScore(e) === 100) state.exAt[e.id] = state.exAt[e.id] || Date.now(); else delete state.exAt[e.id];
      save();
      $('[data-score="' + e.id + '"]').textContent = exScore(e) + '%';
    });
  }

  /* ---------- QUIZ ---------- */
  function shuffle(a) {
    a = a.slice();
    for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; }
    return a;
  }
  function renderQuiz() {
    var id = qs('m');
    if (id === 'final' && cloudEnabled() && window.NAILX_CLOUD) { window.NAILX_CLOUD.renderExam($('#quiz')); return; }
    var root = $('#quiz');
    if (!id) {
      root.innerHTML = '<div class="grid">' + D.modules.filter(function (m) { return D.quiz[m.id]; }).map(function (m) {
        var best = state.quiz[m.id];
        return '<article class="card"><span class="mod-num">' + String(m.n).padStart(2, '0') + '</span><h3>' + esc(m.title) + '</h3>' +
          '<p>' + D.quiz[m.id].length + ' domande' + (best != null ? ' · miglior risultato: <strong>' + best + '%</strong>' : '') + '</p>' +
          '<a class="btn small" href="quiz.html?m=' + m.id + '">' + (best != null ? 'Ripeti' : 'Inizia') + '</a></article>';
      }).join('') +
        '<article class="card" style="border:2px solid var(--accent)"><span class="mod-num">★</span><h3>Esame finale</h3>' +
        '<p>40 domande estratte a caso da tutti i moduli. Soglia di superamento: 80%.' +
        (state.quiz.final != null ? ' Miglior risultato: <strong>' + state.quiz.final + '%</strong>' : '') + '</p>' +
        '<a class="btn small" href="quiz.html?m=final">Inizia l\'esame</a></article></div>';
      return;
    }
    var qs_, title;
    if (id === 'final') {
      var all = [];
      Object.keys(D.quiz).forEach(function (k) { all = all.concat(D.quiz[k]); });
      qs_ = shuffle(all).slice(0, 40);
      title = 'Esame finale';
    } else {
      var m = D.modules.filter(function (x) { return x.id === id; })[0];
      qs_ = D.quiz[id] || [];
      title = 'Quiz · ' + (m ? m.title : id);
    }
    var answered = 0, correct = 0;
    root.innerHTML = '<p><a href="quiz.html">← Tutti i quiz</a></p><h1>' + esc(title) + '</h1>' +
      '<div id="qprog"></div><div id="qlist">' + qs_.map(function (q, i) {
        // mescola le opzioni mantenendo traccia di quella corretta
        var opts = shuffle(q.o.map(function (o, j) { return { t: o, ok: j === q.a }; }));
        return '<div class="quiz-q" role="group" aria-labelledby="qh-' + i + '"><h3 id="qh-' + i + '">' + (i + 1) + '. ' + esc(q.q) + '</h3>' + opts.map(function (o) {
          return '<button type="button" class="opt" data-q="' + i + '" data-ok="' + (o.ok ? 1 : 0) + '">' + esc(o.t) + '</button>';
        }).join('') + FB + '<div class="explain" hidden>' + esc(q.e || '') + '</div></div>';
      }).join('') + '</div><div id="qres" aria-live="polite"></div>';
    function prog() { $('#qprog').innerHTML = progressBar(pct(answered, qs_.length), answered + '/' + qs_.length + ' risposte · ' + correct + ' corrette'); }
    prog();
    $('#qlist').addEventListener('click', function (ev) {
      var b = ev.target.closest('.opt'); if (!b || b.disabled) return;
      var box = b.parentNode;
      box.querySelectorAll('.opt').forEach(function (o) {
        o.disabled = true;
        if (o.dataset.ok === '1') o.classList.add('right');
      });
      if (b.dataset.ok === '1') correct++; else b.classList.add('wrong');
      answered++;
      box.querySelector('.explain').hidden = false;
      feedback(box, b);
      prog();
      if (answered === qs_.length) {
        var score = pct(correct, qs_.length);
        var prevBest = state.quiz[id];
        state.quiz[id] = Math.max(score, prevBest || 0);
        if (score >= (prevBest || 0)) state.quizAt[id] = Date.now();
        save();
        var pass = score >= 80;
        $('#qres').innerHTML = '<div class="card result"><b>' + score + '%</b>' +
          '<p>' + correct + ' risposte corrette su ' + qs_.length + '. ' +
          (pass ? 'Ottimo lavoro: obiettivo raggiunto! 🎉' : 'Rivedi le lezioni del modulo e riprova: l\'obiettivo è l\'80%.') + '</p>' +
          (pass && id === 'final' ? '<p><a class="btn" href="attestato.html">Vai al tuo attestato →</a></p>' : '') +
          '<div class="btn-row" style="justify-content:center"><a class="btn" href="quiz.html?m=' + id + '">Ripeti</a>' +
          '<a class="btn ghost" href="quiz.html">Altri quiz</a></div></div>';
        scrollToEl($('#qres'));
      }
    });
  }

  /* ---------- video (caricati solo al clic, per privacy e velocità) ---------- */
  function videosHtml(list) {
    if (!list || !list.length) return '';
    return '<h2>Video consigliati</h2><div class="videos">' + list.map(function (v) {
      return '<div class="yt" data-id="' + esc(v.id) + '"><button type="button" class="yt-play" aria-label="Riproduci il video: ' + esc(v.title) + '">' +
        '<span class="yt-icon">▶</span><span class="yt-title">' + esc(v.title) + '</span><span class="yt-ch">' + esc(v.channel || '') +
        (v.lang ? ' · ' + esc(v.lang) : '') + '</span></button></div>';
    }).join('') + '</div><p class="muted"><small>Video di terze parti su YouTube, scelti come approfondimento: verifica sempre che le tecniche ' +
      'mostrate rispettino le regole di igiene e sicurezza del corso. Premendo ▶ il video viene caricato da YouTube (modalità privacy avanzata).</small></p>';
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest('.yt-play'); if (!b) return;
    var box = b.parentNode, id = box.dataset.id;
    if (!/^[\w-]{11}$/.test(id)) return;
    box.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="Video YouTube" ' +
      'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>';
  });

  /* ---------- termini del glossario cliccabili nelle lezioni ---------- */
  var glossIndex = null;
  function buildGlossIndex() {
    var list = [];
    D.glossary.forEach(function (g) {
      g.t.split(/\s*[\/(]\s*/).forEach(function (part) {
        part = part.replace(/\)$/, '').trim();
        if (part.length >= 4 && !/^zone/i.test(part)) list.push({ term: part, def: g.d, label: g.t });
      });
    });
    list.sort(function (a, b) { return b.term.length - a.term.length; });
    return list;
  }
  function linkGlossary(root) {
    glossIndex = glossIndex || buildGlossIndex();
    var used = {};
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        return n.parentNode.closest('h1,h2,h3,a,th,figcaption,.box.simple,.gl,.meta,.crumbs,.lesson-nav,.sources,.videos,button,code')
          ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT;
      }
    });
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function (node) {
      for (var i = 0; i < glossIndex.length; i++) {
        var g = glossIndex[i];
        if (used[g.label]) continue;
        var re = new RegExp('(^|[^\\p{L}])(' + g.term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')(?![\\p{L}])', 'iu');
        var m = re.exec(node.nodeValue);
        if (!m) continue;
        used[g.label] = true;
        var start = m.index + m[1].length;
        var after = node.splitText(start);
        after.nodeValue = after.nodeValue.slice(m[2].length);
        var span = document.createElement('span');
        span.className = 'gl';
        span.tabIndex = 0;
        span.textContent = m[2];
        span.setAttribute('data-def', g.def);
        span.setAttribute('role', 'note');
        span.setAttribute('aria-label', m[2] + ': ' + g.def);
        node.parentNode.insertBefore(span, after);
        node = after;
        i = -1;
      }
    });
  }

  /* ---------- GLOSSARIO ---------- */
  function renderGlossary() {
    var items = D.glossary.slice().sort(function (a, b) { return a.t.localeCompare(b.t, 'it'); });
    function draw(q) {
      q = (q || '').toLowerCase().trim();
      var f = items.filter(function (g) { return !q || (g.t + ' ' + g.d).toLowerCase().indexOf(q) >= 0; });
      $('#gloss').innerHTML = f.length ? f.map(function (g) {
        return '<div><dt>' + esc(g.t) + '</dt><dd>' + esc(g.d) + '</dd></div>';
      }).join('') : '<p class="muted">Nessun termine trovato.</p>';
      $('#gcount').textContent = f.length + ' termini';
    }
    draw();
    $('#gsearch').addEventListener('input', function (e) { draw(e.target.value); });
  }


  /* ---------- RIPASSO: flashcard, schede, quiz a tempo ---------- */
  function renderReview() {
    state.cards = state.cards || {};
    var root = $('#review');
    var tabs = [['flash', 'Flashcard'], ['schede', 'Schede riassuntive'], ['tempo', 'Quiz a tempo']];
    function current() { var h = location.hash.slice(1); return tabs.some(function (t) { return t[0] === h; }) ? h : 'flash'; }
    function nav() {
      $('#rtabs').innerHTML = tabs.map(function (t) {
        return '<a class="chip' + (t[0] === current() ? ' active' : '') + '" href="#' + t[0] + '"' + (t[0] === current() ? ' aria-current="page"' : '') + '>' + t[1] + '</a>';
      }).join('');
    }
    window.addEventListener('hashchange', function () { nav(); show(); });
    nav(); show();

    function show() {
      clearInterval(timerId);
      ({ flash: flash, schede: sheets, tempo: timed })[current()]();
    }

    /* flashcard */
    function deckFor(sel) {
      var cards = [];
      if (sel === 'glossario') {
        D.glossary.forEach(function (g) { cards.push({ k: 'g:' + g.t, f: g.t, b: g.d }); });
        return cards;
      }
      D.modules.forEach(function (m) {
        if (sel !== 'tutti' && sel !== m.id) return;
        (D.quiz[m.id] || []).forEach(function (q, i) {
          cards.push({ k: m.id + ':' + i, f: q.q, b: q.o[q.a] + (q.e ? ' — ' + q.e : ''), m: m.title });
        });
      });
      return cards;
    }
    function flash() {
      var opts = '<option value="tutti">Tutti i moduli</option>' + D.modules.filter(function (m) { return D.quiz[m.id]; }).map(function (m) {
        return '<option value="' + m.id + '">' + m.n + '. ' + esc(m.title) + '</option>';
      }).join('') + '<option value="glossario">Glossario (termini)</option>';
      root.innerHTML = '<div class="fc-bar"><select id="fcsel" class="search" aria-label="Scegli il mazzo">' + opts + '</select>' +
        '<button class="btn small ghost" id="fcreset" type="button">Ricomincia il mazzo</button></div><div id="fc"></div>';
      var sel = 'tutti', deck = [], idx = 0;
      function build() {
        var all = deckFor(sel);
        // prima le carte da ripassare o mai viste, poi quelle già sapute
        deck = shuffle(all.filter(function (c) { return state.cards[c.k] !== 'ok'; }));
        idx = 0;
        draw(all.length);
      }
      function draw(total) {
        total = total || deckFor(sel).length;
        var known = deckFor(sel).filter(function (c) { return state.cards[c.k] === 'ok'; }).length;
        if (idx >= deck.length) {
          $('#fc').innerHTML = '<div class="card result"><b>' + known + '/' + total + '</b><p>carte sapute in questo mazzo.</p>' +
            '<button class="btn" id="fcagain" type="button">Ripassa di nuovo le carte da rivedere</button></div>';
          $('#fcagain').addEventListener('click', build);
          return;
        }
        var c = deck[idx];
        $('#fc').innerHTML = progressBar(pct(known, total), known + ' sapute su ' + total + ' · carta ' + (idx + 1) + ' di ' + deck.length + ' da ripassare') +
          '<button type="button" class="flashcard" id="card" aria-live="polite"><span class="fc-side">Domanda</span>' +
          (c.m ? '<small class="muted">' + esc(c.m) + '</small>' : '') + '<strong>' + esc(c.f) + '</strong><span class="muted">Tocca per vedere la risposta</span></button>' +
          '<div class="btn-row fc-actions" hidden><button class="btn ghost" id="fcno" type="button">↺ Da ripassare</button>' +
          '<button class="btn" id="fcyes" type="button">✓ La so</button></div>';
        $('#card').addEventListener('click', function () {
          this.classList.add('flipped');
          this.innerHTML = '<span class="fc-side">Risposta</span><strong>' + esc(c.b) + '</strong>';
          $('.fc-actions').hidden = false;
        });
        $('#fcyes').addEventListener('click', function () { state.cards[c.k] = 'ok'; save(); idx++; draw(); });
        $('#fcno').addEventListener('click', function () { state.cards[c.k] = 'again'; save(); deck.push(c); idx++; draw(); });
      }
      $('#fcsel').addEventListener('change', function () { sel = this.value; build(); });
      $('#fcreset').addEventListener('click', function () {
        deckFor(sel).forEach(function (c) { delete state.cards[c.k]; });
        save(); build();
      });
      build();
    }

    /* schede riassuntive */
    function sheets() {
      root.innerHTML = '<div class="btn-row"><button class="btn small" id="printall" type="button">Stampa tutte le schede</button></div>' +
        '<div class="sheets">' + D.modules.map(function (m) {
          return '<article class="card sheet" data-m="' + m.id + '"><div class="sheet-head"><span class="mod-num">' + String(m.n).padStart(2, '0') + '</span>' +
            badge(m.level) + '</div><h3>' + esc(m.title) + '</h3><ul>' + (m.summary || []).map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul>' +
            '<p class="muted sheet-lessons"><small>Lezioni: ' + m.lessons.map(function (l) { return esc(l.title); }).join(' · ') + '</small></p>' +
            '<button class="btn small ghost sheet-print" type="button">Stampa questa scheda</button></article>';
        }).join('') + '</div>';
      function printOnly(id) {
        document.querySelectorAll('.sheet').forEach(function (el) { el.classList.toggle('no-print', !!id && el.dataset.m !== id); });
        window.print();
      }
      $('#printall').addEventListener('click', function () { printOnly(null); });
      root.addEventListener('click', function (e) {
        var b = e.target.closest('.sheet-print'); if (b) printOnly(b.closest('.sheet').dataset.m);
      });
    }

    /* quiz a tempo */
    var timerId = null;
    function timed() {
      state.timed = state.timed || {};
      root.innerHTML = '<div class="card"><h3 style="margin-top:.2rem">Quiz a tempo</h3><p>Domande casuali da tutti i moduli, <strong>15 secondi</strong> per risposta. ' +
        'Allena la rapidità: le risposte devono diventare automatiche.</p><div class="btn-row">' +
        [10, 20, 30].map(function (n) { return '<button class="btn small" data-n="' + n + '" type="button">' + n + ' domande' +
          (state.timed[n] != null ? ' · record ' + state.timed[n] + '%' : '') + '</button>'; }).join('') + '</div></div><div id="tq"></div>';
      root.querySelectorAll('[data-n]').forEach(function (b) { b.addEventListener('click', function () { start(+b.dataset.n); }); });
    }
    function start(n) {
      var all = [];
      Object.keys(D.quiz).forEach(function (k) { all = all.concat(D.quiz[k]); });
      var qs = shuffle(all).slice(0, n), i = 0, ok = 0, log = [];
      var SEC = 15;
      function ask() {
        clearInterval(timerId);
        if (i >= qs.length) return finish();
        var q = qs[i], left = SEC * 10;
        var opts = shuffle(q.o.map(function (o, j) { return { t: o, ok: j === q.a }; }));
        $('#tq').innerHTML = '<div class="quiz-q timed" role="group" aria-labelledby="tqh"><div class="tbar" aria-hidden="true"><i style="width:100%"></i></div>' +
          '<p class="muted"><small>Domanda ' + (i + 1) + ' di ' + qs.length + ' · ' + ok + ' corrette</small></p><h3 id="tqh">' + esc(q.q) + '</h3>' +
          opts.map(function (o) { return '<button type="button" class="opt" data-ok="' + (o.ok ? 1 : 0) + '">' + esc(o.t) + '</button>'; }).join('') + FB + '</div>';
        $('#tq').scrollIntoView({ block: 'nearest' });
        var bar = $('#tq .tbar i');
        timerId = setInterval(function () {
          left--;
          bar.style.width = (left / (SEC * 10) * 100) + '%';
          if (left <= SEC * 3) bar.classList.add('late');
          if (left <= 0) answer(null);
        }, 100);
        $('#tq').querySelectorAll('.opt').forEach(function (b) { b.addEventListener('click', function () { answer(b); }); });
        function answer(b) {
          clearInterval(timerId);
          var right = !!b && b.dataset.ok === '1';
          if (right) ok++;
          log.push({ q: q, right: right, timeout: !b });
          $('#tq').querySelectorAll('.opt').forEach(function (o) { o.disabled = true; if (o.dataset.ok === '1') o.classList.add('right'); });
          if (b && !right) b.classList.add('wrong');
          feedback($('#tq .quiz-q'), b, !b);
          i++;
          setTimeout(ask, right ? 600 : 1500);
        }
      }
      function finish() {
        var score = pct(ok, qs.length);
        state.timed[n] = Math.max(state.timed[n] || 0, score);
        save();
        $('#tq').innerHTML = '<div class="card result"><b>' + score + '%</b><p>' + ok + ' su ' + qs.length + ' in tempo.</p>' +
          '<button class="btn" type="button" id="tagain">Riprova</button></div>' +
          (log.some(function (x) { return !x.right; }) ? '<h3>Da ripassare</h3><ul class="review-list">' + log.filter(function (x) { return !x.right; }).map(function (x) {
            return '<li><strong>' + esc(x.q.q) + '</strong><br>' + (x.timeout ? '<span class="muted">Tempo scaduto.</span> ' : '') +
              'Risposta: ' + esc(x.q.o[x.q.a]) + (x.q.e ? ' <span class="muted">— ' + esc(x.q.e) + '</span>' : '') + '</li>';
          }).join('') + '</ul>' : '');
        $('#tagain').addEventListener('click', function () { start(n); });
      }
      ask();
    }
  }

  /* ---------- zoom immagini ---------- */
  function lightbox() {
    var box = document.createElement('div');
    box.className = 'lightbox';
    box.hidden = true;
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-modal', 'true');
    box.setAttribute('aria-label', 'Immagine ingrandita');
    box.innerHTML = '<button type="button" class="lb-close" aria-label="Chiudi l\'immagine ingrandita">✕</button>' +
      '<p class="lb-hint" aria-hidden="true">Tocca l\'immagine per ingrandirla · Esc o ✕ per chiudere</p><img alt="">';
    document.body.appendChild(box);
    var big = box.querySelector('img'), btn = box.querySelector('.lb-close'), opener = null;
    function close() {
      if (box.hidden) return;
      box.hidden = true; box.classList.remove('zoomed'); document.body.style.overflow = '';
      if (opener && document.contains(opener)) opener.focus();
      opener = null;
    }
    function open(img) {
      opener = img;
      big.src = img.currentSrc || img.src;
      big.alt = img.alt;
      box.classList.remove('zoomed');
      box.hidden = false;
      box.scrollTop = 0; box.scrollLeft = 0;
      document.body.style.overflow = 'hidden';
      btn.focus();
    }
    // clic sull'immagine: ingrandisce/riduce (testi piccoli leggibili); clic sullo sfondo o ✕: chiude
    box.addEventListener('click', function (e) {
      if (e.target === big) {
        var zoom = !box.classList.contains('zoomed');
        var rx = e.offsetX / big.clientWidth, ry = e.offsetY / big.clientHeight;
        box.classList.toggle('zoomed', zoom);
        if (zoom) { box.scrollLeft = rx * box.scrollWidth - box.clientWidth / 2; box.scrollTop = ry * box.scrollHeight - box.clientHeight / 2; }
        return;
      }
      close();
    });
    document.addEventListener('keydown', function (e) {
      if (box.hidden) {
        // immagini delle lezioni apribili da tastiera
        var t = e.target;
        if ((e.key === 'Enter' || e.key === ' ') && t.matches && t.matches('figure img')) { e.preventDefault(); open(t); }
        return;
      }
      if (e.key === 'Escape') { e.preventDefault(); close(); }
      else if (e.key === 'Tab') { e.preventDefault(); btn.focus(); } // unico controllo: il focus resta nel dialogo
    });
    document.addEventListener('click', function (e) {
      var img = e.target.closest('figure img');
      if (!img || box.contains(img)) return;
      e.preventDefault();
      open(img);
    });
  }

  /* ---------- miglioramenti automatici dei contenuti: immagini ingrandibili da tastiera, tabelle a scorrimento ---------- */
  function enhance(root) {
    if (!root || !root.querySelectorAll) return;
    root.querySelectorAll('figure img:not([tabindex])').forEach(function (img) {
      if (img.closest('.cmp-stage')) return;
      img.tabIndex = 0;
      img.setAttribute('role', 'button');
      img.setAttribute('aria-label', 'Ingrandisci immagine' + (img.alt ? ': ' + img.alt : ''));
    });
    root.querySelectorAll('table').forEach(function (t) {
      if (t.parentNode.classList && t.parentNode.classList.contains('table-wrap')) return;
      if (t.closest('svg')) return;
      var w = document.createElement('div');
      w.className = 'table-wrap';
      var cols = t.rows[0] ? t.rows[0].cells.length : 0;
      if (cols >= 4) w.classList.add('wide');
      // area scorrevole raggiungibile da tastiera, con un nome per i lettori di schermo
      w.tabIndex = 0;
      w.setAttribute('role', 'region');
      var cap = t.querySelector('caption'), head = t.querySelector('th');
      w.setAttribute('aria-label', 'Tabella' + (cap ? ': ' + cap.textContent.trim() : head ? ': ' + head.textContent.trim() : '') + ' (scorrevole)');
      t.parentNode.insertBefore(w, t);
      w.appendChild(t);
    });
  }
  function watchContent() {
    var main = document.querySelector('main');
    if (!main) return;
    enhance(main);
    if (!('MutationObserver' in window)) return;
    var pending = false;
    new MutationObserver(function () {
      if (pending) return;
      pending = true;
      requestAnimationFrame(function () { pending = false; enhance(main); });
    }).observe(main, { childList: true, subtree: true });
  }

  /* ---------- ATTESTATO ---------- */
  var PASS = 80;
  var LOGO = '<defs><linearGradient id="lgc" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d2668a"/><stop offset="1" stop-color="#8e3b5a"/></linearGradient></defs>' +
    '<rect width="64" height="64" rx="16" fill="url(#lgc)"/><rect x="25" y="7" width="14" height="19" rx="3.5" fill="#fff"/>' +
    '<rect x="22" y="24" width="20" height="6" rx="2" fill="#fff"/><rect x="14" y="29" width="36" height="28" rx="9" fill="#fff"/>' +
    '<rect x="18" y="35" width="28" height="18" rx="6" fill="#f3a9c0"/><rect x="21" y="37" width="4" height="12" rx="2" fill="#fff" opacity=".75"/>' +
    '<path d="M50 8 C50.8 12.2 51.8 13.2 56 14 C51.8 14.8 50.8 15.8 50 20 C49.2 15.8 48.2 14.8 44 14 C48.2 13.2 49.2 12.2 50 8 Z" fill="#fff"/>';
  function fmtDate(t) {
    return new Date(t).toLocaleDateString('it-IT', { day: 'numeric', month: 'long', year: 'numeric' });
  }
  function exMinutes(e) { var m = /(\d+)/.exec(e.time); return m ? +m[1] : 0; }
  function certCode(name, date, score) {
    var str = name + '|' + date + '|' + score, h = 2166136261;
    for (var i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 16777619); }
    return 'NX-' + new Date(date).getFullYear() + '-' + (h >>> 0).toString(36).toUpperCase().padStart(7, '0').slice(0, 7);
  }
  function summary() {
    var lessons = allLessons();
    var done = lessons.filter(function (x) { return state.lessons[lessonKey(x.m, x.l)]; });
    var exDone = D.exercises.filter(function (e) { return exScore(e) === 100; });
    var minutes = done.reduce(function (a, x) { return a + (x.l.min || 10); }, 0) +
      exDone.reduce(function (a, e) { return a + exMinutes(e); }, 0);
    var modQuiz = D.modules.filter(function (m) { return D.quiz[m.id] && state.quiz[m.id] != null; });
    return {
      lessons: lessons, done: done, exDone: exDone, hours: Math.max(1, Math.round(minutes / 60)),
      final: state.quiz.final, modQuiz: modQuiz,
      allLessons: done.length === lessons.length, finalOk: (state.quiz.final || 0) >= PASS
    };
  }

  function certSvg(name, s, cert, qrSvg, opts) {
    opts = opts || {};
    var W = 1123, H = 794, GOLD = '#b8892f';
    var shown = name || 'Il tuo nome';
    var fs = Math.min(60, Math.floor(1600 / Math.max(shown.length, 10)));
    var t = function (x, y, str, size, weight, fill, extra) {
      return '<text x="' + x + '" y="' + y + '" text-anchor="middle" font-size="' + size + '" font-weight="' + (weight || 400) +
        '" fill="' + (fill || '#3b2a30') + '"' + (extra || '') + '>' + esc(str) + '</text>';
    };
    var sans = ' font-family="system-ui, -apple-system, Segoe UI, Roboto, sans-serif"';
    var o = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + W + ' ' + H + '" width="' + W + '" height="' + H + '" ' +
      'font-family="Georgia, \'Times New Roman\', serif" role="img" aria-label="Attestato di fine corso">' +
      '<defs>' +
      '<linearGradient id="cg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d2668a"/><stop offset="1" stop-color="#7d2f4e"/></linearGradient>' +
      '<linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f1d58e"/><stop offset=".5" stop-color="#c99a3e"/><stop offset="1" stop-color="#e9c977"/></linearGradient>' +
      '<radialGradient id="bgr" cx=".5" cy=".42" r=".75"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#fbeff2"/></radialGradient>' +
      '<pattern id="pt" width="18" height="18" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="18" stroke="#c2577a" stroke-width="1" opacity=".05"/></pattern>' +
      '</defs>' +
      '<rect width="' + W + '" height="' + H + '" fill="url(#bgr)"/>' +
      '<rect x="56" y="56" width="' + (W - 112) + '" height="' + (H - 112) + '" fill="url(#pt)"/>' +
      '<rect x="20" y="20" width="' + (W - 40) + '" height="' + (H - 40) + '" fill="none" stroke="url(#cg)" stroke-width="12"/>' +
      '<rect x="38" y="38" width="' + (W - 76) + '" height="' + (H - 76) + '" fill="none" stroke="url(#gold)" stroke-width="2.5"/>' +
      '<rect x="46" y="46" width="' + (W - 92) + '" height="' + (H - 92) + '" fill="none" stroke="#e7c3cf" stroke-width="1"/>';
    // ornamenti agli angoli
    [[46, 46, 1, 1], [W - 46, 46, -1, 1], [46, H - 46, 1, -1], [W - 46, H - 46, -1, -1]].forEach(function (c) {
      var x = c[0], y = c[1], sx = c[2], sy = c[3];
      o += '<path d="M' + x + ',' + (y + sy * 70) + ' L' + x + ',' + y + ' L' + (x + sx * 70) + ',' + y + '" fill="none" stroke="url(#gold)" stroke-width="5"/>' +
        '<path d="M' + (x + sx * 14) + ',' + (y + sy * 48) + ' Q' + (x + sx * 14) + ',' + (y + sy * 14) + ' ' + (x + sx * 48) + ',' + (y + sy * 14) + '" fill="none" stroke="url(#gold)" stroke-width="2"/>' +
        '<rect x="' + (x + sx * 22 - 6) + '" y="' + (y + sy * 22 - 6) + '" width="12" height="12" fill="#c2577a" transform="rotate(45 ' + (x + sx * 22) + ' ' + (y + sy * 22) + ')"/>';
    });
    o += '<g transform="translate(' + (W / 2 - 26) + ',72) scale(.82)">' + LOGO + '</g>';
    o += t(W / 2, 158, 'NAILX · CORSO DI RICOSTRUZIONE UNGHIE', 15, 700, '#8e3b5a', ' letter-spacing="5"' + sans);
    o += t(W / 2, 228, 'Attestato di fine corso', 56, 700, '#2b1f22', ' letter-spacing="1"');
    o += '<path d="M' + (W / 2 - 150) + ',250 L' + (W / 2 - 14) + ',250 M' + (W / 2 + 14) + ',250 L' + (W / 2 + 150) + ',250" stroke="' + GOLD + '" stroke-width="2"/>' +
      '<rect x="' + (W / 2 - 6) + '" y="244" width="12" height="12" fill="url(#gold)" transform="rotate(45 ' + W / 2 + ' 250)"/>';
    o += t(W / 2, 292, 'Si attesta che', 20, 400, '#6e5a5f', ' font-style="italic"');
    o += t(W / 2, 362, shown, fs, 700, name ? '#b0466c' : '#d8b4c2', ' font-style="italic"');
    o += '<line x1="' + (W / 2 - 280) + '" y1="384" x2="' + (W / 2 + 280) + '" y2="384" stroke="#e7c3cf" stroke-width="1.5"/>';
    o += t(W / 2, 422, 'ha completato con successo il corso online «Ricostruzione unghie: dalla teoria al banco di lavoro»', 18.5, 400);
    o += t(W / 2, 452, 'livello base → avanzato · ' + D.modules.length + ' moduli · ' + s.lessons.length + ' lezioni · circa ' + s.hours + (s.hours === 1 ? ' ora' : ' ore') + ' di formazione', 16.5, 400, '#6e5a5f');
    var nEx = s.exDone.length;
    o += t(W / 2, 482, s.final != null ? 'Esame finale superato con il ' + s.final + '% · ' + nEx + (nEx === 1 ? ' esercizio pratico completato' : ' esercizi pratici completati')
      : 'Esame finale: da sostenere', 17, 700, s.final != null ? '#2f8a5b' : '#b7791f');
    var lines = [], cur = 'Programma:';
    D.modules.forEach(function (m) {
      var add = (cur === 'Programma:' ? ' ' : ' · ') + m.title;
      if ((cur + add).length > 140) { lines.push(cur); cur = m.title; } else cur += add;
    });
    lines.push(cur);
    lines.slice(0, 4).forEach(function (ln, i) { o += t(W / 2, 512 + i * 17, ln, 11, 400, '#7a6369', sans); });
    // data e codice
    var cx1 = qrSvg ? 250 : 270, cx2 = qrSvg ? W - 360 : W - 270;
    o += '<line x1="' + (cx1 - 120) + '" y1="652" x2="' + (cx1 + 120) + '" y2="652" stroke="#3b2a30" stroke-width="1"/>' +
      t(cx1, 642, cert.date ? fmtDate(cert.date) : '—', 19, 700) + t(cx1, 672, 'Data di rilascio', 13.5, 400, '#6e5a5f', sans);
    o += '<line x1="' + (cx2 - 130) + '" y1="652" x2="' + (cx2 + 130) + '" y2="652" stroke="#3b2a30" stroke-width="1"/>' +
      t(cx2, 642, cert.code || 'NX-····-········', 19, 700, '#2b1f22', ' font-family="ui-monospace, Menlo, Consolas, monospace"') +
      t(cx2, 672, qrSvg ? 'Codice · verificabile online' : 'Codice attestato', 13.5, 400, '#6e5a5f', sans);
    if (qrSvg) o += '<g transform="translate(' + (W - 190) + ',575)">' + qrSvg + '</g>';
    // sigillo a coccarda con nastri
    var sx0 = W / 2, sy0 = 628, pts = [];
    for (var k = 0; k < 48; k++) {
      var a = Math.PI * 2 * k / 48, r = k % 2 ? 45 : 50;
      pts.push((sx0 + r * Math.cos(a)).toFixed(1) + ',' + (sy0 + r * Math.sin(a)).toFixed(1));
    }
    o += '<path d="M' + (sx0 - 26) + ',' + (sy0 + 26) + ' l-16,40 l14,-6 l9,12 l12,-40 Z" fill="#9c3b60"/>' +
      '<path d="M' + (sx0 + 26) + ',' + (sy0 + 26) + ' l16,40 l-14,-6 l-9,12 l-12,-40 Z" fill="#b0466c"/>' +
      '<polygon points="' + pts.join(' ') + '" fill="url(#gold)"/>' +
      '<circle cx="' + sx0 + '" cy="' + sy0 + '" r="38" fill="url(#cg)"/>' +
      '<circle cx="' + sx0 + '" cy="' + sy0 + '" r="32" fill="none" stroke="#f1d58e" stroke-width="1.2" stroke-dasharray="2 3"/>' +
      t(sx0, sy0 - 8, 'CORSO', 11, 700, '#fff', ' letter-spacing="2"' + sans) +
      t(sx0, sy0 + 7, 'COMPLETATO', 7.5, 700, '#fff', sans) +
      t(sx0, sy0 + 23, cert.date ? String(new Date(cert.date).getFullYear()) : '★', 11, 700, '#f1d58e', sans);
    o += t(W / 2, 726, qrSvg ? 'Attestato di corso professionalizzante rilasciato dalla piattaforma didattica NailX: requisiti ed esame finale verificati online.'
      : 'Attestato di corso professionalizzante rilasciato in autovalutazione dalla piattaforma didattica NailX.', 11.5, 400, '#8a777d', sans);
    o += t(W / 2, 743, 'Corso professionalizzante non abilitante: in Italia l\'esercizio della professione richiede la qualifica di estetista (L. 1/1990).', 11.5, 400, '#8a777d', sans);
    if (opts.preview) {
      o += '<text x="' + W / 2 + '" y="' + H / 2 + '" text-anchor="middle" font-size="120" font-weight="800" fill="#c2577a" opacity=".1" ' +
        'transform="rotate(-24 ' + W / 2 + ' ' + H / 2 + ')"' + sans + ' letter-spacing="12">ANTEPRIMA</text>';
    }
    return o + '</svg>';
  }

  function certDetail(name, s, cert) {
    var h = '<div class="cert-detail"><h2>Dettaglio del percorso svolto</h2>' +
      '<p><strong>' + esc(name) + '</strong> · codice <code>' + esc(cert.code) + '</code> · rilasciato il ' + fmtDate(cert.date) + '</p>' +
      '<table><tr><th>#</th><th>Modulo</th><th>Livello</th><th>Lezioni</th><th>Quiz</th><th>Completato il</th></tr>';
    D.modules.forEach(function (m) {
      var times = m.lessons.map(function (l) { return state.lessons[lessonKey(m, l)]; }).filter(Boolean);
      var q = state.quiz[m.id];
      h += '<tr><td>' + m.n + '</td><td>' + esc(m.title) + '<br><small class="muted">' + m.lessons.map(function (l) { return esc(l.title); }).join(' · ') + '</small></td>' +
        '<td>' + LEVELS[m.level] + '</td><td>' + times.length + '/' + m.lessons.length + '</td>' +
        '<td>' + (q != null ? q + '%' : '—') + '</td><td>' + (times.length ? fmtDate(Math.max.apply(null, times)) : '—') + '</td></tr>';
    });
    h += '</table><h3>Esercizi pratici completati (' + s.exDone.length + ' di ' + D.exercises.length + ')</h3>';
    if (s.exDone.length) {
      h += '<table><tr><th>Esercizio</th><th>Livello</th><th>Durata</th><th>Auto-valutazione</th><th>Data</th></tr>' + s.exDone.map(function (e) {
        return '<tr><td>' + esc(e.title) + '</td><td>' + LEVELS[e.level] + '</td><td>' + esc(e.time) + '</td><td>100%</td><td>' + (state.exAt[e.id] ? fmtDate(state.exAt[e.id]) : '—') + '</td></tr>';
      }).join('') + '</table>';
    } else {
      h += '<p class="muted">Nessun esercizio completato al 100%.</p>';
    }
    var partial = D.exercises.filter(function (e) { var sc = exScore(e); return sc > 0 && sc < 100; });
    if (partial.length) {
      h += '<p class="muted"><small>In corso: ' + partial.map(function (e) { return esc(e.title) + ' (' + exScore(e) + '%)'; }).join(' · ') + '</small></p>';
    }
    h += '<h3>Verifiche</h3><ul><li>Esame finale: <strong>' + s.final + '%</strong> (soglia ' + PASS + '%)' +
      (state.quizAt.final ? ', svolto il ' + fmtDate(state.quizAt.final) : '') + '</li>' +
      '<li>Quiz di modulo svolti: ' + s.modQuiz.length + ' di ' + Object.keys(D.quiz).length + '</li>' +
      '<li>Ore di formazione stimate (lezioni + esercizi completati): circa ' + s.hours + '</li></ul></div>';
    return h;
  }

  /* Interfaccia della pagina attestato (usata in locale e online).
   * ctx: { lessonsDone, lessonsTotal, best, cert:{name,code,date,final,hours,exercises}|null, verifiable,
   *        generate(name) → Promise<cert>, qr(cert) → Promise<svg|null>, verifyUrl(cert) → url|null } */
  function certUI(root, ctx) {
    var lessonsOk = ctx.lessonsDone >= ctx.lessonsTotal;
    var examOk = (ctx.best || 0) >= PASS;
    var cert = ctx.cert;
    var eligible = lessonsOk && examOk;
    var ns = nextStep();
    function step(n, st, title, sub, cta) {
      var icon = st === 'done' ? '✓' : (st === 'locked' ? '🔒' : n);
      return '<li class="st-' + st + '"><span class="st-ic">' + icon + '</span><div class="st-txt"><strong>' + title + '</strong><small>' + sub + '</small></div>' +
        (cta && st !== 'done' && st !== 'locked' ? '<a class="btn small" href="' + cta[1] + '">' + cta[0] + '</a>' : '') + '</li>';
    }
    var pctNow = Math.round(80 * ctx.lessonsDone / ctx.lessonsTotal + (examOk ? 20 : 0));
    var status = cert ? 'Attestato rilasciato il ' + fmtDate(cert.date) + (ctx.verifiable ? ' · verificabile online' : '')
      : eligible ? 'Requisiti completati: inserisci il nome e genera l\'attestato.'
        : 'Completa i passaggi qui sotto per sbloccare l\'attestato.';
    var h = '<section class="card cert-hero no-print">' +
      '<div class="cert-hero-top"><div class="ring big" style="--p:' + pctNow + '"><span>' + pctNow + '%</span></div>' +
      '<div><h2>Il tuo percorso</h2><p class="muted">' + status + '</p></div></div><ol class="cert-steps">' +
      step(1, lessonsOk ? 'done' : 'current', 'Lezioni', ctx.lessonsDone + ' di ' + ctx.lessonsTotal + ' completate', ['Continua', lessonsOk ? 'corso.html' : ns.href]) +
      step(2, examOk ? 'done' : (lessonsOk ? 'current' : 'todo'), 'Esame finale', ctx.best != null ? 'miglior risultato ' + ctx.best + '% (soglia ' + PASS + '%)' : 'soglia ' + PASS + '% · non ancora svolto', ['Fai l\'esame', 'quiz.html?m=final']) +
      step(3, cert ? 'done' : (eligible ? 'current' : 'locked'), 'Attestato', cert ? 'codice ' + esc(cert.code) : (eligible ? 'pronto da generare' : 'si sblocca dopo i passi 1 e 2'), null) +
      '</ol></section>' +
      '<div class="cert-layout"><aside class="card cert-panel no-print">' +
      '<label for="cname"><strong>Nome e cognome sull\'attestato</strong></label>' +
      '<input id="cname" class="search" maxlength="60" autocomplete="name" placeholder="Es. Maria Rossi" value="' + esc((cert && cert.name) || state.certDraft || '') + '">' +
      '<button class="btn" id="cgen" type="button"' + (eligible ? '' : ' disabled') + '>' + (cert ? 'Aggiorna il nome' : 'Genera l\'attestato') + '</button>' +
      (eligible ? '' : '<p class="muted"><small>🔒 Il pulsante si attiva quando lezioni ed esame sono completati. Intanto puoi vedere l\'anteprima con il tuo nome.</small></p>') +
      '<div id="cerr" aria-live="polite"></div>' +
      '<div class="cert-ex"><strong>Esercizi pratici</strong><span>' + summary().exDone.length + ' di ' + D.exercises.length + ' completati</span>' +
      '<small class="muted">Facoltativi ma consigliati: compaiono sull\'attestato.</small><a href="esercizi.html">Vai agli esercizi →</a></div>' +
      '<div id="cactions"></div></aside>' +
      '<div class="cert-print"><div class="cert-page cert-wrap" id="cpreview"></div><div class="cert-page" id="cdetail"></div></div></div>';
    root.innerHTML = h;

    var input = $('#cname', root);
    function svgFor(c, qrSvg) {
      var s = summary();
      if (c) { s.final = c.final != null ? c.final : s.final; if (c.hours) s.hours = c.hours; if (c.exercises) s.exDone = c.exercises; }
      else s.final = ctx.best != null && ctx.best >= PASS ? ctx.best : null;
      var nm = input.value.trim().replace(/\s+/g, ' ');
      return certSvg(nm || (c && c.name) || '', s, c || {}, qrSvg, { preview: !c });
    }
    function drawPreview() { $('#cpreview', root).innerHTML = svgFor(null); }
    function drawCert(c) {
      Promise.resolve(ctx.qr ? ctx.qr(c) : null).then(function (qrSvg) {
        input.value = c.name;
        $('#cpreview', root).innerHTML = svgFor(c, qrSvg);
        $('#cdetail', root).innerHTML = certDetail(c.name, summary(), c);
        var url = ctx.verifyUrl ? ctx.verifyUrl(c) : null;
        $('#cactions', root).innerHTML = '<div class="cert-actions"><button class="btn" id="cprint" type="button">🖨 Stampa / salva PDF</button>' +
          '<button class="btn ghost" id="cpng" type="button">⬇ Scarica immagine</button>' +
          (navigator.share ? '<button class="btn ghost" id="cshare" type="button">↗ Condividi</button>' : '') +
          (url ? '<button class="btn ghost" id="ccopy" type="button">🔗 Copia link di verifica</button><a class="small-link" href="' + esc(url) + '" target="_blank" rel="noopener">Apri la pagina di verifica</a>' : '') + '</div>';
        $('#cprint', root).addEventListener('click', function () { window.print(); });
        $('#cpng', root).addEventListener('click', function () { downloadPng($('#cpreview svg', root), 'attestato-nailx.png'); });
        if ($('#cshare', root)) $('#cshare', root).addEventListener('click', function () {
          navigator.share({ title: 'Il mio attestato NailX', text: 'Ho completato il corso di ricostruzione unghie NailX! Codice ' + c.code, url: url || location.href }).catch(function () {});
        });
        if ($('#ccopy', root)) $('#ccopy', root).addEventListener('click', function () {
          var b = this;
          (navigator.clipboard ? navigator.clipboard.writeText(url) : Promise.reject()).then(function () { b.textContent = '✓ Link copiato'; },
            function () { prompt('Copia il link di verifica:', url); });
        });
      });
    }
    input.addEventListener('input', function () {
      state.certDraft = input.value;
      try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) { /* ignore */ }
      if (!cert) drawPreview();
      else $('#cgen', root).disabled = input.value.trim().replace(/\s+/g, ' ') === cert.name;
    });
    $('#cgen', root).addEventListener('click', function () {
      var btn = this, name = input.value.trim().replace(/\s+/g, ' ');
      if (name.length < 3) { input.classList.add('invalid'); input.focus(); $('#cerr', root).innerHTML = '<p class="err">Scrivi nome e cognome (almeno 3 caratteri).</p>'; return; }
      input.classList.remove('invalid');
      $('#cerr', root).innerHTML = '';
      btn.disabled = true;
      Promise.resolve(ctx.generate(name)).then(function (c) {
        // ridisegna tutta la pagina: passi, pannello e attestato aggiornati
        certUI(root, Object.assign({}, ctx, { cert: c }));
        toast('🎓 Attestato ' + (ctx.verifiable ? 'registrato' : 'generato') + ': codice <strong>' + esc(c.code) + '</strong>', 7000);
        scrollToEl($('#cpreview', root));
      }).catch(function (e) {
        btn.disabled = false;
        $('#cerr', root).innerHTML = '<div class="box danger">' + esc((e && e.message) || 'Errore imprevisto, riprova.') + '</div>';
      });
    });
    if (cert) { drawCert(cert); $('#cgen', root).disabled = true; } else drawPreview();
  }

  function renderCertificate() {
    if (cloudEnabled() && window.NAILX_CLOUD) { window.NAILX_CLOUD.renderCertificate($('#cert')); return; }
    var s = summary();
    var c = state.cert && state.cert.name ? { name: state.cert.name, code: state.cert.code, date: state.cert.date, final: s.final } : null;
    certUI($('#cert'), {
      lessonsDone: s.done.length, lessonsTotal: s.lessons.length, best: state.quiz.final != null ? state.quiz.final : null,
      cert: c, verifiable: false,
      generate: function (name) {
        var date = (state.cert && state.cert.date) || Date.now();
        state.cert = { name: name, date: date, code: certCode(name, date, s.final) };
        save();
        return { name: name, code: state.cert.code, date: date, final: s.final };
      }
    });
  }

  function downloadPng(svgEl, filename) {
    var data = new XMLSerializer().serializeToString(svgEl);
    var url = URL.createObjectURL(new Blob([data], { type: 'image/svg+xml;charset=utf-8' }));
    var img = new Image();
    img.onload = function () {
      var scale = 2, c = document.createElement('canvas');
      c.width = svgEl.viewBox.baseVal.width * scale;
      c.height = svgEl.viewBox.baseVal.height * scale;
      var ctx = c.getContext('2d');
      ctx.scale(scale, scale);
      ctx.drawImage(img, 0, 0);
      URL.revokeObjectURL(url);
      c.toBlob(function (blob) {
        var a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 1000);
      });
    };
    img.src = url;
  }

  /* ---------- VERIFICA ATTESTATO (pubblica) ---------- */
  function renderVerify() {
    var root = $('#verify');
    if (!cloudEnabled()) {
      root.innerHTML = '<div class="box warn"><strong class="t">Verifica non disponibile</strong>Questo sito non ha ancora attivato l\'archivio online degli attestati.</div>';
      return;
    }
    root.innerHTML = '<form class="card cert-form" id="vform"><label for="vcode"><strong>Codice dell\'attestato</strong></label>' +
      '<div class="row"><input id="vcode" class="search" placeholder="NX-2026-XXXXXXXX" autocomplete="off" maxlength="20" value="' + esc(qs('c') || '') + '">' +
      '<button class="btn" type="submit">Verifica</button></div></form><div id="vres" aria-live="polite"></div>';
    $('#vform').addEventListener('submit', function (e) { e.preventDefault(); check($('#vcode').value); });
    if (qs('c')) check(qs('c'));
    function check(code) {
      code = String(code || '').trim().toUpperCase();
      if (!/^NX-\d{4}-[0-9A-F]{8}$/.test(code)) { $('#vres').innerHTML = '<div class="box warn">Formato del codice non valido (esempio: NX-2026-1A2B3C4D).</div>'; return; }
      $('#vres').innerHTML = '<p class="muted">Verifica in corso…</p>';
      var c = window.NAILX_CONFIG;
      fetch(c.supabaseUrl.replace(/\/$/, '') + '/rest/v1/rpc/verify_certificate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', apikey: c.supabaseAnonKey, Authorization: 'Bearer ' + c.supabaseAnonKey },
        body: JSON.stringify({ p_code: code })
      }).then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); }).then(function (v) {
        if (!v || !v.code) {
          $('#vres').innerHTML = '<div class="box danger"><strong class="t">Attestato non trovato</strong>Nessun attestato corrisponde al codice ' + esc(code) + '.</div>';
        } else if (!v.valid) {
          $('#vres').innerHTML = '<div class="box danger"><strong class="t">Attestato revocato</strong>Il codice ' + esc(v.code) + ' esiste ma l\'attestato non è più valido.</div>';
        } else {
          $('#vres').innerHTML = '<div class="box tip"><strong class="t">✓ Attestato autentico</strong>' +
            '<p><strong>' + esc(v.full_name) + '</strong> ha completato il corso NailX.</p><ul>' +
            '<li>Codice: <code>' + esc(v.code) + '</code></li>' +
            '<li>Rilasciato il ' + fmtDate(v.issued_at) + '</li>' +
            '<li>Lezioni completate: ' + v.lessons_done + ' di ' + v.lessons_total + '</li>' +
            '<li>Esame finale: ' + v.final_score + '% (soglia ' + PASS + '%)</li>' +
            '<li>Ore di formazione stimate: circa ' + v.hours + '</li>' +
            '<li>Esercizi pratici completati: ' + (v.exercises && v.exercises.length ? v.exercises.map(esc).join(', ') : 'nessuno') + '</li></ul>' +
            '<p class="muted"><small>Attestato di un corso professionalizzante online: documenta le competenze acquisite ma non è un titolo abilitante.</small></p></div>';
        }
      }).catch(function () {
        $('#vres').innerHTML = '<div class="box warn">Servizio di verifica non raggiungibile. Riprova più tardi.</div>';
      });
    }
  }

  // funzioni condivise con assets/js/cloud.js
  window.NAILX_APP = {
    state: state, save: save, esc: esc, $: $, qs: qs, pct: pct, progressBar: progressBar, fmtDate: fmtDate,
    summary: summary, certSvg: certSvg, certDetail: certDetail, certUI: certUI, downloadPng: downloadPng, shuffle: shuffle, toast: toast,
    PASS: PASS, D: D, cloudEnabled: cloudEnabled
  };

  /* ---------- avvio ---------- */
  var page = document.body.dataset.page;
  header(page);
  lightbox();
  watchContent();
  ({ home: renderHome, corso: renderCourse, esercizi: renderExercises, quiz: renderQuiz, glossario: renderGlossary,
    attestato: renderCertificate, ripasso: renderReview, verifica: renderVerify, programma: renderProgram, dispensa: renderHandbook,
    accedi: function () { if (window.NAILX_CLOUD) window.NAILX_CLOUD.renderAccount($('#account')); } }[page] || function () {})();
})();
