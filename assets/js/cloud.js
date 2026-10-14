/* NailX – area online (Supabase): accesso via e-mail, sincronizzazione dei progressi,
 * esame finale corretto dal server, attestato verificabile con QR code, gestione account.
 * Si attiva solo se assets/js/config.js contiene supabaseUrl e supabaseAnonKey.
 * Va caricato PRIMA di app.js; usa window.NAILX_APP (definito da app.js) al momento delle chiamate.
 */
(function () {
  'use strict';
  var C = window.NAILX_CONFIG || {};
  if (!C.supabaseUrl || !C.supabaseAnonKey) return;

  var SUPABASE_JS = 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/dist/umd/supabase.min.js';
  var QR_JS = 'https://cdn.jsdelivr.net/npm/qrcode-generator@1.4.4/qrcode.min.js';
  var SYNC_FLAG = 'nailx-synced-user';

  function A() { return window.NAILX_APP; }
  function loadScript(src) {
    return new Promise(function (res, rej) {
      var s = document.createElement('script');
      s.src = src; s.async = true; s.crossOrigin = 'anonymous';
      s.onload = res; s.onerror = function () { rej(new Error('Impossibile caricare ' + src)); };
      document.head.appendChild(s);
    });
  }
  function errMsg(e) { return (e && (e.message || e.error_description)) || 'Errore imprevisto, riprova.'; }

  /* ---------- client ---------- */
  var clientP = null;
  function client() {
    if (!clientP) {
      clientP = (window.supabase ? Promise.resolve() : loadScript(SUPABASE_JS)).then(function () {
        return window.supabase.createClient(C.supabaseUrl, C.supabaseAnonKey, {
          auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: true },
          // keepalive: un salvataggio partito mentre si cambia pagina non viene interrotto
          global: {
            fetch: function (url, opts) {
              opts = opts || {};
              var small = typeof opts.body === 'string' && opts.body.length < 60000;
              return fetch(url, small && opts.method && opts.method !== 'GET' ? Object.assign({}, opts, { keepalive: true }) : opts);
            }
          }
        });
      });
    }
    return clientP;
  }
  var session = null;
  var ready = client().then(function (sb) {
    return sb.auth.getSession().then(function (r) {
      session = r.data && r.data.session;
      sb.auth.onAuthStateChange(function (ev, s) {
        var was = session && session.user.id;
        session = s;
        navLabel();
        if (s && s.user.id !== was) pull();
      });
      navLabel();
      if (session) return pull();
    });
  }).catch(function (e) { console.warn('NailX cloud:', errMsg(e)); });

  function navLabel() {
    var a = document.getElementById('nav-account');
    if (a) a.textContent = session ? 'Account' : 'Accedi';
    // l'intestazione viene creata da app.js: se non c'è ancora, riprova a pagina caricata
    else if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', navLabel, { once: true });
  }

  /* ---------- sincronizzazione progressi ---------- */
  function merge(local, remote) {
    var out = JSON.parse(JSON.stringify(local));
    ['lessons', 'exAt'].forEach(function (k) {
      out[k] = out[k] || {};
      Object.keys(remote[k] || {}).forEach(function (x) {
        out[k][x] = out[k][x] ? Math.min(out[k][x], remote[k][x]) : remote[k][x];
      });
    });
    ['quiz', 'timed'].forEach(function (k) {
      out[k] = out[k] || {};
      Object.keys(remote[k] || {}).forEach(function (x) { out[k][x] = Math.max(out[k][x] || 0, remote[k][x] || 0); });
    });
    out.quizAt = Object.assign({}, remote.quizAt || {}, out.quizAt || {});
    out.checks = out.checks || {};
    Object.keys(remote.checks || {}).forEach(function (x) {
      var a = out.checks[x] || [], b = remote.checks[x] || [];
      var n = Math.max(a.length, b.length), r = [];
      for (var i = 0; i < n; i++) r[i] = !!(a[i] || b[i]);
      out.checks[x] = r;
    });
    out.cards = Object.assign({}, remote.cards || {}, out.cards || {});
    return out;
  }
  function apply(newState) {
    var st = A().state;
    Object.keys(st).forEach(function (k) { delete st[k]; });
    Object.assign(st, newState);
  }
  var pulling = false;
  function pull() {
    if (!session || pulling) return Promise.resolve();
    pulling = true;
    var uid = session.user.id;
    return client().then(function (sb) {
      return sb.from('progress').select('data').eq('user_id', uid).maybeSingle();
    }).then(function (r) {
      if (r.error) throw r.error;
      var remote = (r.data && r.data.data) || {};
      var local = JSON.parse(JSON.stringify(A().state));
      var first;
      try { first = localStorage.getItem(SYNC_FLAG) !== uid; } catch (e) { first = true; }
      // primo accesso su questo dispositivo: unione; poi vince la versione più recente
      var next = first ? merge(local, remote) : ((remote.updatedAt || 0) > (local.updatedAt || 0) ? remote : local);
      next.lessons = next.lessons || {}; next.checks = next.checks || {}; next.quiz = next.quiz || {};
      next.quizAt = next.quizAt || {}; next.exAt = next.exAt || {};
      try { localStorage.setItem(SYNC_FLAG, uid); } catch (e) { /* ignore */ }
      var changed = JSON.stringify(next) !== JSON.stringify(local);
      apply(next);
      pulling = false;
      if (changed) {
        A().save();
        push(true);
        // ricarica una volta per mostrare i progressi recuperati
        try {
          if (!sessionStorage.getItem('nailx-reloaded')) { sessionStorage.setItem('nailx-reloaded', '1'); location.reload(); }
        } catch (e) { /* ignore */ }
      } else if (JSON.stringify(remote) !== JSON.stringify(next)) {
        push(true);
      }
    }).catch(function (e) { pulling = false; console.warn('NailX sync:', errMsg(e)); });
  }
  var pushTimer = null;
  function push(now) {
    if (!session || pulling) return Promise.resolve();
    clearTimeout(pushTimer);
    var run = function () {
      return client().then(function (sb) {
        return sb.from('progress').upsert({ user_id: session.user.id, data: A().state, updated_at: new Date().toISOString() });
      }).then(function (r) { if (r && r.error) throw r.error; })
        .catch(function (e) {
          // account eliminato da un altro dispositivo: esci anche da qui
          if (e && (e.code === '23503' || /foreign key/i.test(e.message || ''))) {
            stopSync();
            try { localStorage.removeItem(SYNC_FLAG); } catch (x) { /* ignore */ }
            client().then(function (sb) { return sb.auth.signOut(); });
            return;
          }
          if (!leaving) console.warn('NailX sync:', errMsg(e));
        });
    };
    if (now) { pushTimer = null; return run(); }
    return new Promise(function (res) { pushTimer = setTimeout(function () { pushTimer = null; run().then(res); }, 1200); });
  }
  // se la pagina viene nascosta o chiusa con un salvataggio in sospeso, invialo subito
  document.addEventListener('visibilitychange', function () {
    if (document.visibilityState === 'hidden' && pushTimer) push(true);
  });
  // durante il cambio pagina la risposta può andare persa (la richiesta parte comunque): niente avvisi
  var leaving = false;
  window.addEventListener('pagehide', function () { leaving = true; });
  function stopSync() { clearTimeout(pushTimer); pushTimer = null; session = null; }

  /* ---------- ESAME FINALE (corretto dal server) ---------- */
  function renderExam(root) {
    var app = A(), esc = app.esc;
    root.innerHTML = '<p><a href="quiz.html">← Tutti i quiz</a></p><h1>Esame finale</h1><div id="xbody"><p class="muted">Caricamento…</p></div>';
    var body = root.querySelector('#xbody');
    ready.then(function () {
      if (!session) {
        body.innerHTML = '<div class="box info"><strong class="t">Accedi per sostenere l\'esame</strong>' +
          'L\'esame finale valido per l\'attestato viene corretto online: <a href="accedi.html">accedi con la tua e-mail</a>, poi torna qui.</div>' +
          '<p class="muted">Per allenarti senza account usa il <a href="ripasso.html#tempo">quiz a tempo</a> o i quiz dei moduli.</p>';
        return;
      }
      body.innerHTML = '<div class="card"><p><strong>40 domande</strong> estratte da tutti i moduli. Rispondi a tutte e poi consegna: ' +
        'la correzione avviene sul server. Soglia di superamento: <strong>' + app.PASS + '%</strong>. Hai 90 minuti e fino a 10 tentativi al giorno.</p>' +
        '<button class="btn" id="xstart" type="button">Inizia l\'esame</button></div>';
      body.querySelector('#xstart').addEventListener('click', start);
    });

    function start() {
      body.innerHTML = '<p class="muted">Preparo le domande…</p>';
      client().then(function (sb) { return sb.rpc('start_exam'); }).then(function (r) {
        if (r.error) throw r.error;
        var ex = r.data, answers = {};
        var html = '<div id="qprog"></div>' + ex.questions.map(function (q, i) {
          var opts = app.shuffle(q.options.map(function (o, j) { return { t: o, j: j }; }));
          return '<div class="quiz-q" data-q="' + q.id + '" role="group" aria-labelledby="xq-' + i + '"><h3 id="xq-' + i + '">' + (i + 1) + '. ' + esc(q.question) + '</h3>' + opts.map(function (o) {
            return '<button type="button" class="opt" data-j="' + o.j + '" aria-pressed="false">' + esc(o.t) + '</button>';
          }).join('') + '<div class="explain" hidden></div></div>';
        }).join('') + '<div class="btn-row"><button class="btn" id="xsubmit" type="button" disabled>Consegna l\'esame</button></div><div id="qres" aria-live="polite"></div>';
        body.innerHTML = html;
        function prog() {
          var n = Object.keys(answers).length;
          body.querySelector('#qprog').innerHTML = app.progressBar(app.pct(n, ex.questions.length), n + '/' + ex.questions.length + ' risposte date');
          body.querySelector('#xsubmit').disabled = n < ex.questions.length;
        }
        prog();
        body.addEventListener('click', function (e) {
          var b = e.target.closest('.opt'); if (!b || b.disabled) return;
          var box = b.closest('.quiz-q');
          box.querySelectorAll('.opt').forEach(function (o) { o.classList.toggle('chosen', o === b); o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
          answers[box.dataset.q] = +b.dataset.j;
          prog();
        });
        body.querySelector('#xsubmit').addEventListener('click', function () {
          this.disabled = true; this.textContent = 'Correzione in corso…';
          client().then(function (sb) { return sb.rpc('submit_exam', { p_attempt: ex.attempt_id, p_answers: answers }); }).then(function (r2) {
            if (r2.error) throw r2.error;
            showResult(r2.data, answers);
          }).catch(function (e2) { body.querySelector('#qres').innerHTML = '<div class="box danger">' + esc(errMsg(e2)) + '</div>'; });
        });
      }).catch(function (e) {
        body.innerHTML = '<div class="box danger"><strong class="t">Impossibile avviare l\'esame</strong>' + esc(errMsg(e)) + '</div>';
      });
    }
    function showResult(res, answers) {
      var byId = {};
      res.results.forEach(function (x) { byId[x.id] = x; });
      body.querySelectorAll('.quiz-q').forEach(function (box) {
        var r = byId[box.dataset.q];
        box.querySelectorAll('.opt').forEach(function (o) {
          o.disabled = true;
          o.removeAttribute('aria-pressed');
          if (+o.dataset.j === r.answer) o.classList.add('right');
          else if (+o.dataset.j === answers[box.dataset.q]) o.classList.add('wrong');
        });
        var ex = box.querySelector('.explain'); ex.textContent = r.explanation || ''; ex.hidden = !r.explanation;
      });
      body.querySelector('#xsubmit').remove();
      var st = app.state;
      st.quiz.final = Math.max(st.quiz.final || 0, res.score);
      if (res.score >= (st.quiz.final || 0)) st.quizAt.final = Date.now();
      app.save();
      var pass = res.score >= app.PASS;
      body.querySelector('#qres').innerHTML = '<div class="card result"><b>' + res.score + '%</b><p>' + res.correct + ' risposte corrette su ' + res.total + '. ' +
        (pass ? 'Esame superato! 🎉' : 'Non ancora: rivedi le spiegazioni qui sopra e riprova.') + '</p><div class="btn-row" style="justify-content:center">' +
        (pass ? '<a class="btn" href="attestato.html">Vai al tuo attestato →</a>' : '<a class="btn" href="quiz.html?m=final">Nuovo tentativo</a>') + '</div></div>';
      var rm = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
      body.querySelector('#qres').scrollIntoView({ behavior: rm ? 'auto' : 'smooth' });
    }
  }

  /* ---------- ATTESTATO verificabile ---------- */
  function qrSvg(text, size) {
    var qr = window.qrcode(0, 'M');
    qr.addData(text); qr.make();
    var n = qr.getModuleCount(), cell = size / (n + 8), d = '';
    for (var r = 0; r < n; r++) for (var c = 0; c < n; c++) {
      if (qr.isDark(r, c)) d += 'M' + ((c + 4) * cell).toFixed(2) + ',' + ((r + 4) * cell).toFixed(2) + 'h' + cell.toFixed(2) + 'v' + cell.toFixed(2) + 'h-' + cell.toFixed(2) + 'z';
    }
    return '<rect width="' + size + '" height="' + size + '" fill="#fff"/><path d="' + d + '" fill="#2b1f22"/>' +
      '<text x="' + size / 2 + '" y="' + (size + 14) + '" text-anchor="middle" font-size="11" fill="#6e5a5f" font-family="system-ui, sans-serif">Scansiona per verificare</text>';
  }
  function verifyUrl(code) { return new URL('verifica.html?c=' + encodeURIComponent(code), location.href).href; }

  function renderCertificate(root) {
    var app = A(), esc = app.esc;
    root.innerHTML = '<p class="muted">Caricamento…</p>';
    function mapCert(c) {
      return c ? { name: c.full_name, code: c.code, date: Date.parse(c.issued_at), final: c.final_score, hours: c.hours, exercises: c.exercises || [] } : null;
    }
    ready.then(function () {
      if (!session) {
        root.innerHTML = '<div class="box info"><strong class="t">Accedi per ottenere l\'attestato</strong>' +
          'L\'attestato viene registrato online, così chiunque può verificarne l\'autenticità con il codice o il QR code. ' +
          '<a href="accedi.html">Accedi con la tua e-mail</a>: i progressi di questo dispositivo verranno salvati nel tuo account.</div>';
        return;
      }
      return client().then(function (sb) {
        return Promise.all([
          sb.from('exam_attempts').select('score').not('submitted_at', 'is', null).order('score', { ascending: false }).limit(1),
          sb.from('certificates').select('*').maybeSingle()
        ]);
      }).then(function (rs) {
        var best = rs[0].data && rs[0].data[0] ? rs[0].data[0].score : null;
        var s = app.summary();
        app.certUI(root, {
          lessonsDone: s.done.length, lessonsTotal: s.lessons.length, best: best,
          cert: mapCert(rs[1].data), verifiable: true,
          generate: function (name) {
            return push(true).then(client).then(function (sb) { return sb.rpc('issue_certificate', { p_full_name: name }); })
              .then(function (r) { if (r.error) throw r.error; return mapCert(r.data); });
          },
          qr: function (c) {
            return (window.qrcode ? Promise.resolve() : loadScript(QR_JS)).then(function () { return qrSvg(verifyUrl(c.code), 112); })
              .catch(function () { return null; });
          },
          verifyUrl: function (c) { return verifyUrl(c.code); }
        });
      });
    }).catch(function (e) { root.innerHTML = '<div class="box danger">' + esc(errMsg(e)) + '</div>'; });
  }

  /* ---------- ACCOUNT ---------- */
  function renderAccount(root) {
    var app = A(), esc = app.esc;
    root.innerHTML = '<p class="muted">Caricamento…</p>';
    ready.then(function () { session ? loggedIn() : loggedOut(); });

    function loggedOut() {
      root.innerHTML = '<form class="card cert-form" id="lform"><h2 style="margin-top:.2rem">Accedi o registrati</h2>' +
        '<p>Inserisci la tua e-mail: riceverai un <strong>link di accesso</strong> (nessuna password da ricordare).</p>' +
        '<label for="lemail"><strong>E-mail</strong></label><div class="row"><input id="lemail" class="search" type="email" required autocomplete="email" placeholder="nome@esempio.it"></div>' +
        '<ul class="checklist"><li><label><input type="checkbox" id="lpriv" required> <span>Ho letto l\'<a href="privacy.html" target="_blank">informativa privacy</a> e ' +
        'chiedo di creare l\'account per seguire il corso e ottenere l\'attestato.</span></label></li>' +
        '<li><label><input type="checkbox" id="lage" required> <span>Dichiaro di avere almeno 14 anni.</span></label></li></ul>' +
        '<button class="btn" type="submit">Inviami il link</button><div id="lmsg" aria-live="polite"></div></form>' +
        '<p class="muted"><small>Puoi seguire tutto il corso anche senza account: l\'account serve a salvare i progressi online e a ottenere l\'attestato verificabile.</small></p>';
      root.querySelector('#lform').addEventListener('submit', function (e) {
        e.preventDefault();
        var email = root.querySelector('#lemail').value.trim(), msg = root.querySelector('#lmsg');
        if (!root.querySelector('#lpriv').checked || !root.querySelector('#lage').checked) {
          msg.innerHTML = '<div class="box warn">Per continuare conferma le due caselle.</div>'; return;
        }
        var redirect = new URL('accedi.html', location.href).href;
        msg.innerHTML = '<p class="muted">Invio in corso…</p>';
        client().then(function (sb) {
          return sb.auth.signInWithOtp({ email: email, options: { emailRedirectTo: redirect, data: { privacy_version: C.privacyVersion || '' } } });
        }).then(function (r) {
          if (r.error) throw r.error;
          msg.innerHTML = '<div class="box tip"><strong class="t">Controlla la posta</strong>Abbiamo inviato un link a ' + esc(email) +
            '. Aprilo da questo dispositivo per accedere. Se non lo trovi, guarda nello spam.</div>';
        }).catch(function (err) { msg.innerHTML = '<div class="box danger">' + esc(errMsg(err)) + '</div>'; });
      });
    }

    function loggedIn() {
      var s = app.summary();
      root.innerHTML = '<div class="card"><h2 style="margin-top:.2rem">Il tuo account</h2><p>Accesso effettuato come <strong>' + esc(session.user.email) + '</strong>.</p>' +
        app.progressBar(app.pct(s.done.length, s.lessons.length), s.done.length + ' di ' + s.lessons.length + ' lezioni · ' + s.exDone.length + ' esercizi completati') +
        '<p class="muted"><small>I progressi vengono salvati automaticamente nel tuo account e li ritrovi su ogni dispositivo.</small></p>' +
        '<div class="btn-row"><a class="btn" href="corso.html">Continua il corso</a><a class="btn ghost" href="attestato.html">Attestato</a>' +
        '<button class="btn ghost" id="async" type="button">Sincronizza ora</button><button class="btn ghost" id="aout" type="button">Esci</button></div></div>' +
        '<div class="card" style="margin-top:1rem"><h3 style="margin-top:.2rem">I tuoi dati (GDPR)</h3>' +
        '<p>Puoi scaricare una copia di tutti i dati che conserviamo su di te, oppure cancellare definitivamente l\'account. ' +
        'Dettagli nell\'<a href="privacy.html">informativa privacy</a>.</p>' +
        '<div class="btn-row"><button class="btn ghost" id="aexport" type="button">Scarica i miei dati (JSON)</button>' +
        '<button class="btn ghost danger-btn" id="adel" type="button">Elimina account</button></div><div id="amsg" aria-live="polite"></div></div>';
      var msg = root.querySelector('#amsg');
      root.querySelector('#async').addEventListener('click', function () {
        var b = this; b.disabled = true;
        push(true).then(pull).then(function () { b.disabled = false; b.textContent = 'Sincronizzato ✓'; });
      });
      root.querySelector('#aout').addEventListener('click', function () {
        push(true).then(client).then(function (sb) { return sb.auth.signOut(); }).then(function () {
          try { localStorage.removeItem(SYNC_FLAG); } catch (e) { /* ignore */ }
          location.reload();
        });
      });
      root.querySelector('#aexport').addEventListener('click', function () {
        client().then(function (sb) {
          return Promise.all([
            sb.from('profiles').select('*').maybeSingle(), sb.from('progress').select('*').maybeSingle(),
            sb.from('exam_attempts').select('id, started_at, submitted_at, score'), sb.from('certificates').select('*').maybeSingle()
          ]);
        }).then(function (rs) {
          var data = { esportato_il: new Date().toISOString(), email: session.user.email, profilo: rs[0].data, progressi: rs[1].data,
            tentativi_esame: rs[2].data, attestato: rs[3].data };
          var a = document.createElement('a');
          a.href = URL.createObjectURL(new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' }));
          a.download = 'nailx-miei-dati.json';
          document.body.appendChild(a); a.click();
          setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 1000);
        }).catch(function (e) { msg.innerHTML = '<div class="box danger">' + esc(errMsg(e)) + '</div>'; });
      });
      root.querySelector('#adel').addEventListener('click', function () {
        var ok = prompt('Questa operazione cancella definitivamente account, progressi online, tentativi d\'esame e attestato ' +
          '(il codice non sarà più verificabile). Scrivi ELIMINA per confermare.');
        if (ok !== 'ELIMINA') return;
        client().then(function (sb) {
          return sb.rpc('delete_my_account').then(function (r) { if (r.error) throw r.error; stopSync(); return sb.auth.signOut(); });
        }).then(function () {
          try { localStorage.removeItem(SYNC_FLAG); } catch (e) { /* ignore */ }
          root.innerHTML = '<div class="box tip"><strong class="t">Account eliminato</strong>Tutti i tuoi dati online sono stati cancellati. ' +
            'I progressi restano solo in questo browser: puoi cancellarli dalle impostazioni del browser.</div>';
        }).catch(function (e) { msg.innerHTML = '<div class="box danger">' + esc(errMsg(e)) + '</div>'; });
      });
    }
  }

  window.NAILX_CLOUD = { queuePush: function () { push(false); }, renderExam: renderExam, renderCertificate: renderCertificate, renderAccount: renderAccount };
})();
