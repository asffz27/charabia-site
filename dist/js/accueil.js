(function () {
  'use strict';
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var timers = [];
  var later = function (fn, ms) { timers.push(setTimeout(fn, ms)); };

  /* ---------- Quiz « Info ou charabia ? » ---------- */
  var QUIZ = [
    { s: "Plus la consigne donnée à une IA est précise, meilleure est sa réponse.", truth: 'info', why: "La qualité de ce qu’on envoie à la machine détermine directement la qualité de ce qui en sort. Les apprenants s’initient au prompting durant l’escape-game." },
    { s: "Une IA comprend ce qu’elle écrit, comme le ferait un humain.", truth: 'charabia', why: "Une IA générative calcule le mot le plus probable à partir d’immenses quantités de textes. Elle ne comprend pas le sens de ce qu’elle produit et peut donc se tromper avec beaucoup d’assurance." },
    { s: "Si une IA cite un livre ou une étude, c’est qu’ils existent.", truth: 'charabia', why: "Une IA peut inventer des sources de toutes pièces. On parle d’hallucination. Le bon réflexe consiste à toujours vérifier." },
    { s: "Une image créée par une IA peut reproduire des stéréotypes.", truth: 'info', why: "Une IA apprend à partir d’images existantes. Si ces images sont déséquilibrées, ses créations le sont aussi. On parle de biais de représentation." }
  ];
  var qs = { qi: 0, pick: null, score: 0 };
  var quizEl = document.getElementById('quiz');
  var stepEl = document.getElementById('quizStep');

  function el(tag, attrs, text) {
    var e = document.createElement(tag);
    for (var k in attrs || {}) e.setAttribute(k, attrs[k]);
    if (text != null) e.textContent = text;
    return e;
  }

  function renderQuiz() {
    if (!quizEl) return;
    quizEl.innerHTML = '';
    var q = QUIZ[qs.qi];
    stepEl.textContent = Math.min(qs.qi + 1, QUIZ.length) + ' / ' + QUIZ.length;
    if (q) {
      quizEl.appendChild(el('p', { style: 'margin:0;font-size:clamp(19px,1.8vw,24px);line-height:1.42;font-weight:500;letter-spacing:-0.015em;text-wrap:pretty' }, '« ' + q.s + ' »'));
      var bottom = el('div', { style: 'margin-top:auto;padding-top:26px' });
      if (qs.pick === null) {
        var row = el('div', { style: 'display:flex;gap:10px' });
        var b1 = el('button', { type: 'button', 'class': 'q-btn' }, 'C’est vrai');
        var b2 = el('button', { type: 'button', 'class': 'q-btn' }, 'C’est du charabia');
        b1.onclick = function () { pick('info'); };
        b2.onclick = function () { pick('charabia'); };
        row.appendChild(b1); row.appendChild(b2); bottom.appendChild(row);
      } else {
        var ok = qs.pick === q.truth;
        var live = el('div', { 'aria-live': 'polite' });
        live.appendChild(el('div', { style: 'font-size:15.5px;font-weight:600;margin-bottom:8px;color:' + (ok ? '#5C86FF' : '#FF9A5C') },
          (ok ? 'Bonne réponse.' : 'Mauvaise réponse.') + ' C’est ' + (q.truth === 'info' ? 'vrai.' : 'du charabia.')));
        live.appendChild(el('p', { style: 'margin:0 0 18px;font-size:14.5px;line-height:1.55;color:rgba(243,240,233,0.75)' }, q.why));
        bottom.appendChild(live);
        var next = el('button', { type: 'button', 'class': 'q-main' }, qs.qi < QUIZ.length - 1 ? 'Suivant' : 'Voir le résultat');
        next.onclick = function () { qs.qi++; qs.pick = null; renderQuiz(); };
        bottom.appendChild(next);
      }
      quizEl.appendChild(bottom);
    } else {
      var s = qs.score;
      quizEl.appendChild(el('p', { style: 'margin:0;font-size:clamp(21px,2vw,27px);line-height:1.35;font-weight:600;letter-spacing:-0.02em' },
        s + ' bonne' + (s > 1 ? 's' : '') + ' réponse' + (s > 1 ? 's' : '') + ' sur ' + QUIZ.length + '.'));
      quizEl.appendChild(el('p', { style: 'margin:12px 0 0;font-size:15px;line-height:1.6;color:rgba(243,240,233,0.75)' },
        'En atelier, les apprenants vont plus loin : ils mettent ces idées à l’épreuve en équipe, face à une vraie IA.'));
      var foot = el('div', { style: 'margin-top:auto;padding-top:24px;display:flex;flex-wrap:wrap;gap:10px' });
      var a = el('a', { href: '/contact?objet=atelier', 'class': 'q-main' }, 'Organiser un atelier');
      var again = el('button', { type: 'button', 'class': 'q-ghost' }, 'Rejouer');
      again.onclick = function () { qs = { qi: 0, pick: null, score: 0 }; renderQuiz(); };
      foot.appendChild(a); foot.appendChild(again); quizEl.appendChild(foot);
    }
  }
  function pick(choice) {
    if (qs.pick !== null) return;
    qs.pick = choice;
    if (QUIZ[qs.qi] && choice === QUIZ[qs.qi].truth) qs.score++;
    renderQuiz();
  }
  renderQuiz();

  /* ---------- Apparition au défilement ---------- */
  function hideReveals() {
    if (reduce) return;
    document.querySelectorAll('[data-reveal]').forEach(function (e) {
      e.style.opacity = '0';
      e.style.transform = 'translateY(24px)';
      e.style.transition = 'opacity 0.85s cubic-bezier(0.2,0.8,0.2,1), transform 0.85s cubic-bezier(0.2,0.8,0.2,1)';
    });
  }
  function reveals() {
    if (reduce || !('IntersectionObserver' in window)) {
      document.querySelectorAll('[data-reveal]').forEach(function (e) { e.style.opacity = '1'; e.style.transform = 'none'; });
      return;
    }
    hideReveals();
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e, i) {
        if (!e.isIntersecting) return;
        var t = e.target;
        later(function () { t.style.opacity = '1'; t.style.transform = 'none'; }, i * 65);
        io.unobserve(t);
      });
    }, { rootMargin: '0px 0px -12% 0px' });
    document.querySelectorAll('[data-reveal]').forEach(function (e) { io.observe(e); });
  }

  /* ---------- Dégradé animé du hero ---------- */
  var hg = document.getElementById('heroGrad');
  if (hg) {
    var show = function () { later(function () { hg.style.opacity = '1'; }, 1100); };
    if (hg._ready) show(); else hg.addEventListener('ready', show, { once: true });
  }

  /* ---------- Séquence d'ouverture ---------- */
  var overlay = document.getElementById('intro');
  function intro() {
    var seen = false;
    try { seen = sessionStorage.getItem('cb-intro') === '1'; sessionStorage.setItem('cb-intro', '1'); } catch (e) {}
    if (seen || new URLSearchParams(location.search).get('intro') === '0') {
      overlay.style.display = 'none';
      if (hg) hg.style.opacity = '1';
      document.documentElement.classList.remove('intro-pending');
      reveals();
      return;
    }
    hideReveals();
    var skip = document.getElementById('introSkip');
    var letters = Array.prototype.slice.call(overlay.querySelectorAll('[data-l]'));
    document.body.style.overflow = 'hidden';
    var navEl = document.querySelector('nav');
    if (navEl) { navEl.style.transition = 'opacity 0.85s ease'; navEl.style.opacity = '0'; }
    document.documentElement.classList.remove('intro-pending');
    var done = false;
    var exit = function () {
      if (done) return;
      done = true;
      overlay.style.opacity = '0';
      overlay.style.pointerEvents = 'none';
      document.body.style.overflow = '';
      if (navEl) navEl.style.opacity = '1';
      reveals();
      later(function () { overlay.style.display = 'none'; }, 950);
    };
    if (skip) skip.addEventListener('click', exit);
    if (reduce) { later(exit, 900); return; }

    var GLYPHS = 'BCDEFGHKLNPRSTUVXYZ245789';
    var HALO = '0.03em 0.04em 0 rgba(147,169,247,0.9)';
    var fontReady = (document.fonts && document.fonts.load) ? document.fonts.load('400 100px "Archivo Black"') : Promise.resolve();
    fontReady.catch(function () {}).then(function () {
      letters.forEach(function (l) {
        l._final = l.textContent;
        l.style.display = 'inline-block';
        l.style.width = l.getBoundingClientRect().width + 'px';
        l.style.textAlign = 'center';
        l.style.color = 'rgba(243,240,233,0.4)';
        l.style.transition = 'transform 0.22s cubic-bezier(0.34,1.56,0.64,1), color 0.18s ease';
        l._cycle = setInterval(function () { l.textContent = GLYPHS[(Math.random() * GLYPHS.length) | 0]; }, 55);
      });
      var started = false;
      var start = function () {
        if (started || done) return;
        started = true;
        if (hg) hg.style.opacity = '1';
        letters.forEach(function (l, i) {
          var isIA = l.hasAttribute('data-ia');
          later(function () {
            clearInterval(l._cycle);
            l.textContent = l._final;
            l.style.color = isIA ? '#5C86FF' : '#F3F0E9';
            l.style.textShadow = HALO;
            l.style.transform = 'scale(1.14)';
            later(function () { l.style.transform = 'none'; }, 180);
          }, 650 + i * 175 + (isIA ? 180 : 0));
        });
        later(exit, 3300);
      };
      if (hg && hg._ready) start();
      else if (hg) hg.addEventListener('ready', start, { once: true });
      later(start, 2400);
    });
  }
  if (overlay) intro(); else reveals();
})();
