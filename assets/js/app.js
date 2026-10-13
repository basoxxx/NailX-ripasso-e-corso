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
  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) { /* ignore */ }
  }

  /* ---------- helpers ---------- */
  function $(sel, root) { return (root || document).querySelector(sel); }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function qs(name) { return new URLSearchParams(location.search).get(name); }
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
      ['corso.html', 'corso', 'Lezioni'],
      ['esercizi.html', 'esercizi', 'Esercizi'],
      ['quiz.html', 'quiz', 'Quiz'],
      ['glossario.html', 'glossario', 'Glossario']
    ];
    var h = document.createElement('header');
    h.className = 'site-header';
    h.innerHTML = '<nav class="nav"><a class="brand" href="index.html">' +
      '<img src="assets/img/logo.svg" alt="" width="30" height="30"><span>Nail<b>X</b></span></a>' +
      '<div class="nav-links">' + links.map(function (x) {
        return '<a href="' + x[0] + '"' + (x[1] === active ? ' class="active"' : '') + '>' + x[2] + '</a>';
      }).join('') + '</div>' +
      '<button class="theme-btn" type="button" title="Cambia tema" aria-label="Cambia tema">☾</button></nav>';
    document.body.insertBefore(h, document.body.firstChild);
    $('.theme-btn', h).addEventListener('click', function () {
      var cur = document.documentElement.getAttribute('data-theme');
      var dark = cur ? cur === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
      var next = dark ? 'light' : 'dark';
      applyTheme(next);
      try { localStorage.setItem(THEME_KEY, next); } catch (e) { /* ignore */ }
    });
    var f = document.createElement('footer');
    f.innerHTML = 'NailX · Corso di ricostruzione unghie · Materiale didattico a scopo formativo: non sostituisce ' +
      'la formazione abilitante prevista dalla legge né il parere medico.';
    document.body.appendChild(f);
  }

  /* ---------- HOME ---------- */
  function renderHome() {
    var lessons = allLessons();
    var done = lessons.filter(function (x) { return state.lessons[lessonKey(x.m, x.l)]; }).length;
    var exDone = D.exercises.filter(function (e) { return exScore(e) === 100; }).length;
    var quizDone = Object.keys(state.quiz).length;
    $('#stats').innerHTML =
      stat(D.modules.length, 'moduli') + stat(lessons.length, 'lezioni') +
      stat(D.exercises.length, 'esercizi pratici') + stat(countQuiz(), 'domande quiz');
    $('#global-progress').innerHTML = progressBar(pct(done, lessons.length),
      done + ' di ' + lessons.length + ' lezioni completate · ' + exDone + ' esercizi superati · ' + quizDone + ' quiz svolti');
    var next = lessons.filter(function (x) { return !state.lessons[lessonKey(x.m, x.l)]; })[0] || lessons[0];
    $('#continue').href = lessonUrl(next.m, next.l);
    $('#continue').textContent = done ? 'Continua: ' + next.l.title : 'Inizia il corso';

    $('#modules').innerHTML = D.modules.map(function (m) {
      var d = moduleDone(m);
      return '<article class="card"><div style="display:flex;justify-content:space-between;align-items:center">' +
        '<span class="mod-num">' + String(m.n).padStart(2, '0') + '</span>' + badge(m.level) + '</div>' +
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
            return '<li><a class="' + cls.join(' ') + '" href="' + lessonUrl(mm, ll) + '">' + esc(ll.title) + '</a></li>';
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
      l.html;
    if (relatedEx.length && m.lessons.indexOf(l) === m.lessons.length - 1) {
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

    var mark = $('#mark');
    function upd() { mark.textContent = state.lessons[key] ? '✓ Completata' : 'Segna come completata'; mark.classList.toggle('ghost', !!state.lessons[key]); }
    upd();
    mark.addEventListener('click', function () {
      if (state.lessons[key]) delete state.lessons[key]; else state.lessons[key] = Date.now();
      save(); upd(); side();
    });
    $('.menu-toggle').addEventListener('click', function () { $('#sidebar').classList.toggle('open'); });
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
      return '<button class="chip' + (x[0] === 'all' ? ' active' : '') + '" data-f="' + x[0] + '" type="button">' + x[1] + '</button>';
    }).join('');
    bar.addEventListener('click', function (ev) {
      var b = ev.target.closest('.chip'); if (!b) return;
      filter = b.dataset.f;
      bar.querySelectorAll('.chip').forEach(function (c) { c.classList.toggle('active', c === b); });
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
            '<h4>Auto-valutazione</h4><ul class="checklist">' + e.checks.map(function (x, j) {
              return '<li><label><input type="checkbox" data-ex="' + e.id + '" data-i="' + j + '"' + (c[j] ? ' checked' : '') + '> <span>' + esc(x) + '</span></label></li>';
            }).join('') + '</ul>' +
            '<div class="box warn"><strong class="t">Errori frequenti</strong><ul>' + e.mistakes.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul></div>' +
            '</div></div></details>';
        }).join('');
      if (hash) { var t = document.getElementById(hash); if (t) t.scrollIntoView(); }
    }
    draw();
    $('#exercises').addEventListener('change', function (ev) {
      var cb = ev.target; if (!cb.dataset.ex) return;
      var arr = state.checks[cb.dataset.ex] = state.checks[cb.dataset.ex] || [];
      arr[+cb.dataset.i] = cb.checked;
      save();
      var e = D.exercises.filter(function (x) { return x.id === cb.dataset.ex; })[0];
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
        return '<div class="quiz-q"><h3>' + (i + 1) + '. ' + esc(q.q) + '</h3>' + opts.map(function (o) {
          return '<button type="button" class="opt" data-q="' + i + '" data-ok="' + (o.ok ? 1 : 0) + '">' + esc(o.t) + '</button>';
        }).join('') + '<div class="explain" hidden>' + esc(q.e || '') + '</div></div>';
      }).join('') + '</div><div id="qres"></div>';
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
      prog();
      if (answered === qs_.length) {
        var score = pct(correct, qs_.length);
        var prevBest = state.quiz[id];
        state.quiz[id] = Math.max(score, prevBest || 0);
        save();
        var pass = score >= 80;
        $('#qres').innerHTML = '<div class="card result"><b>' + score + '%</b>' +
          '<p>' + correct + ' risposte corrette su ' + qs_.length + '. ' +
          (pass ? 'Ottimo lavoro: obiettivo raggiunto! 🎉' : 'Rivedi le lezioni del modulo e riprova: l\'obiettivo è l\'80%.') + '</p>' +
          '<div class="btn-row" style="justify-content:center"><a class="btn" href="quiz.html?m=' + id + '">Ripeti</a>' +
          '<a class="btn ghost" href="quiz.html">Altri quiz</a></div></div>';
        $('#qres').scrollIntoView({ behavior: 'smooth' });
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

  /* ---------- avvio ---------- */
  var page = document.body.dataset.page;
  header(page);
  ({ home: renderHome, corso: renderCourse, esercizi: renderExercises, quiz: renderQuiz, glossario: renderGlossary }[page] || function () {})();
})();
