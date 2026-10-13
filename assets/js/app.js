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
      ['glossario.html', 'glossario', 'Glossario'],
      ['attestato.html', 'attestato', 'Attestato']
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
            (e.imgs || []).map(function (src) {
              return '<figure><img src="assets/img/' + src + '" alt="Tavola di riferimento: ' + esc(e.title) + '" loading="lazy"></figure>';
            }).join('') +
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
        if (score >= (prevBest || 0)) state.quizAt[id] = Date.now();
        save();
        var pass = score >= 80;
        $('#qres').innerHTML = '<div class="card result"><b>' + score + '%</b>' +
          '<p>' + correct + ' risposte corrette su ' + qs_.length + '. ' +
          (pass ? 'Ottimo lavoro: obiettivo raggiunto! 🎉' : 'Rivedi le lezioni del modulo e riprova: l\'obiettivo è l\'80%.') + '</p>' +
          (pass && id === 'final' ? '<p><a class="btn" href="attestato.html">Vai al tuo attestato →</a></p>' : '') +
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

  /* ---------- zoom immagini ---------- */
  function lightbox() {
    var box = document.createElement('div');
    box.className = 'lightbox';
    box.hidden = true;
    box.innerHTML = '<button type="button" class="lb-close" aria-label="Chiudi">✕</button><img alt="">';
    document.body.appendChild(box);
    function close() { box.hidden = true; document.body.style.overflow = ''; }
    box.addEventListener('click', close);
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
    document.addEventListener('click', function (e) {
      var img = e.target.closest('figure img');
      if (!img) return;
      e.preventDefault();
      var big = box.querySelector('img');
      big.src = img.src;
      big.alt = img.alt;
      box.hidden = false;
      document.body.style.overflow = 'hidden';
    });
  }

  /* ---------- ATTESTATO ---------- */
  var PASS = 80;
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

  function certSvg(name, s, cert) {
    var W = 1123, H = 794, fs = Math.min(58, Math.floor(1500 / Math.max(name.length, 10)));
    var t = function (x, y, str, size, weight, fill, extra) {
      return '<text x="' + x + '" y="' + y + '" text-anchor="middle" font-size="' + size + '" font-weight="' + (weight || 400) +
        '" fill="' + (fill || '#3b2a30') + '"' + (extra || '') + '>' + esc(str) + '</text>';
    };
    var o = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + W + ' ' + H + '" width="' + W + '" height="' + H + '" ' +
      'font-family="Georgia, \'Times New Roman\', serif" role="img" aria-label="Attestato di fine corso">' +
      '<defs><linearGradient id="cg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#c2577a"/><stop offset="1" stop-color="#8e3b5a"/></linearGradient></defs>' +
      '<rect width="' + W + '" height="' + H + '" fill="#fffaf8"/>' +
      '<rect x="22" y="22" width="' + (W - 44) + '" height="' + (H - 44) + '" fill="none" stroke="url(#cg)" stroke-width="10"/>' +
      '<rect x="44" y="44" width="' + (W - 88) + '" height="' + (H - 88) + '" fill="none" stroke="#e7c3cf" stroke-width="2"/>';
    [[60, 60], [W - 60, 60], [60, H - 60], [W - 60, H - 60]].forEach(function (c) {
      o += '<circle cx="' + c[0] + '" cy="' + c[1] + '" r="9" fill="#c2577a"/>';
    });
    o += '<g transform="translate(' + (W / 2 - 28) + ',70) scale(.875)"><rect width="64" height="64" rx="16" fill="#c2577a"/>' +
      '<path d="M20,54 L20,30 C20,14 27,8 32,6 C37,8 44,14 44,30 L44,54 Z" fill="#fff"/>' +
      '<path d="M24,52 L24,31 C24,20 28,14 32,12 C36,14 40,20 40,31 L40,52 Z" fill="#f7c1cf"/></g>';
    o += t(W / 2, 165, 'NAILX · CORSO DI RICOSTRUZIONE UNGHIE', 16, 700, '#8e3b5a', ' letter-spacing="4"');
    o += t(W / 2, 240, 'Attestato di fine corso', 54, 700, '#2b1f22');
    o += t(W / 2, 290, 'Si attesta che', 20, 400, '#6e5a5f', ' font-style="italic"');
    o += t(W / 2, 365, name, fs, 700, '#c2577a');
    o += '<line x1="' + (W / 2 - 260) + '" y1="385" x2="' + (W / 2 + 260) + '" y2="385" stroke="#e7c3cf" stroke-width="2"/>';
    o += t(W / 2, 425, 'ha completato il corso online «Ricostruzione unghie: dalla teoria al banco di lavoro»', 19, 400);
    o += t(W / 2, 455, 'livello base → avanzato · ' + D.modules.length + ' moduli · ' + s.lessons.length + ' lezioni · circa ' + s.hours + ' ore di formazione', 17, 400, '#6e5a5f');
    o += t(W / 2, 485, 'Esame finale superato con il ' + s.final + '% · ' + s.exDone.length + ' esercizi pratici completati', 17, 700, '#2f8a5b');
    var mods = D.modules.map(function (m) { return m.title; });
    var mid = Math.ceil(mods.length / 2);
    o += t(W / 2, 530, 'Programma: ' + mods.slice(0, mid).join(' · '), 12.5, 400, '#6e5a5f', ' font-family="system-ui, sans-serif"');
    o += t(W / 2, 550, mods.slice(mid).join(' · '), 12.5, 400, '#6e5a5f', ' font-family="system-ui, sans-serif"');
    o += '<line x1="150" y1="640" x2="420" y2="640" stroke="#3b2a30"/>' + t(285, 662, 'Data di rilascio', 14, 400, '#6e5a5f') + t(285, 630, fmtDate(cert.date), 19, 700);
    o += '<line x1="' + (W - 420) + '" y1="640" x2="' + (W - 150) + '" y2="640" stroke="#3b2a30"/>' + t(W - 285, 662, 'Codice attestato', 14, 400, '#6e5a5f') + t(W - 285, 630, cert.code, 19, 700, '#2b1f22', ' font-family="ui-monospace, monospace"');
    o += '<circle cx="' + W / 2 + '" cy="630" r="46" fill="url(#cg)"/><circle cx="' + W / 2 + '" cy="630" r="38" fill="none" stroke="#fff" stroke-width="1.5" stroke-dasharray="3 3"/>' +
      t(W / 2, 624, 'CORSO', 12, 700, '#fff', ' letter-spacing="2"') + t(W / 2, 642, 'COMPLETATO', 9, 700, '#fff');
    o += t(W / 2, 722, 'Attestato di partecipazione rilasciato in autovalutazione dalla piattaforma didattica NailX.', 12, 400, '#8a777d', ' font-family="system-ui, sans-serif"');
    o += t(W / 2, 740, 'Non è un titolo abilitante: in Italia l\'esercizio della professione richiede la qualifica di estetista (L. 1/1990).', 12, 400, '#8a777d', ' font-family="system-ui, sans-serif"');
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

  function renderCertificate() {
    var root = $('#cert');
    var s = summary();
    var req = [
      [s.allLessons, 'Completa tutte le lezioni', s.done.length + '/' + s.lessons.length + ' lezioni completate', 'corso.html'],
      [s.finalOk, 'Supera l\'esame finale con almeno l\'' + PASS + '%', s.final != null ? 'miglior risultato: ' + s.final + '%' : 'non ancora svolto', 'quiz.html?m=final']
    ];
    var ok = s.allLessons && s.finalOk;
    var h = '<div class="card"><h2 style="margin-top:.2rem">Requisiti</h2><ul class="req">' + req.map(function (r) {
      return '<li class="' + (r[0] ? 'ok' : 'todo') + '"><span class="ic">' + (r[0] ? '✓' : '•') + '</span><div><strong>' + r[1] + '</strong><br>' +
        '<small class="muted">' + r[2] + '</small></div>' + (r[0] ? '' : '<a class="btn small" href="' + r[3] + '">Vai</a>') + '</li>';
    }).join('') + '<li class="' + (s.exDone.length ? 'ok' : 'opt') + '"><span class="ic">' + (s.exDone.length ? '✓' : '○') + '</span><div><strong>Esercizi pratici (consigliati)</strong><br>' +
      '<small class="muted">' + s.exDone.length + ' di ' + D.exercises.length + ' completati: verranno elencati nell\'attestato</small></div>' +
      '<a class="btn small ghost" href="esercizi.html">Esercizi</a></li></ul></div>';
    if (!ok) {
      root.innerHTML = h + '<p class="muted">Quando avrai soddisfatto i requisiti potrai inserire il tuo nome e scaricare l\'attestato con il dettaglio del percorso svolto.</p>';
      return;
    }
    var cert = state.cert || {};
    h += '<div class="card cert-form"><label for="cname"><strong>Nome e cognome da riportare sull\'attestato</strong></label>' +
      '<div class="row"><input id="cname" class="search" maxlength="60" autocomplete="name" value="' + esc(cert.name || '') + '" placeholder="Es. Maria Rossi">' +
      '<button class="btn" id="cgen" type="button">' + (cert.code ? 'Aggiorna' : 'Genera attestato') + '</button></div></div>' +
      '<div id="cout"></div>';
    root.innerHTML = h;

    function draw() {
      var c = state.cert;
      if (!c || !c.name) return;
      var s2 = summary();
      $('#cout').innerHTML = '<div class="btn-row cert-actions"><button class="btn" id="cprint" type="button">Stampa / salva in PDF</button>' +
        '<button class="btn ghost" id="cpng" type="button">Scarica immagine (PNG)</button></div>' +
        '<div class="cert-print"><div class="cert-page cert-wrap">' + certSvg(c.name, s2, c) + '</div><div class="cert-page">' + certDetail(c.name, s2, c) + '</div></div>';
      $('#cprint').addEventListener('click', function () { window.print(); });
      $('#cpng').addEventListener('click', function () { downloadPng($('.cert-wrap svg'), 'attestato-nailx.png'); });
    }
    $('#cgen').addEventListener('click', function () {
      var name = $('#cname').value.trim().replace(/\s+/g, ' ');
      if (name.length < 3) { $('#cname').focus(); $('#cname').classList.add('invalid'); return; }
      $('#cname').classList.remove('invalid');
      var date = (state.cert && state.cert.date) || Date.now();
      state.cert = { name: name, date: date, code: certCode(name, date, s.final) };
      save();
      $('#cgen').textContent = 'Aggiorna';
      draw();
      $('#cout').scrollIntoView({ behavior: 'smooth' });
    });
    draw();
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

  /* ---------- avvio ---------- */
  var page = document.body.dataset.page;
  header(page);
  lightbox();
  ({ home: renderHome, corso: renderCourse, esercizi: renderExercises, quiz: renderQuiz, glossario: renderGlossary,
    attestato: renderCertificate }[page] || function () {})();
})();
