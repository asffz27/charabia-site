(function () {
  'use strict';
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var timers = [];
  var later = function (fn, ms) { timers.push(setTimeout(fn, ms)); };

  // La BoxIA : fermée, elle se trémousse ; ouverte, elle se déplie en plateau de jeu.
  function setupBox(box) {
    var q = function (s) { return box.querySelector(s); };
    var frame = q('[data-box-frame]'), fitEl = q('[data-box-fit]');
    var root = q('[data-box-root]'), wiggle = q('[data-box-wiggle]'), spin = q('[data-box-spin]');
    var hint = q('[data-box-hint]'), shadow = q('[data-box-shadow]'), btn = q('[data-box-btn]');
    var T = q('[data-flap="T"]'), B = q('[data-flap="B"]'), L = q('[data-flap="L"]'), R = q('[data-flap="R"]'), lid = q('[data-flap="lid"]');
    var chest = q('[data-chest]'), chestLid = q('[data-chest-lid]');
    var letters = Array.prototype.slice.call(box.querySelectorAll('[data-cl]'));
    var rocket = q('[data-rocket-body]');
    var rocketAnim = null, anims = [];
    var folded = true, ang = 28, lastT = performance.now();

    function fit() {
      var need = folded ? 380 : 600;
      var k = Math.min(1, frame.clientWidth / need);
      var top = folded ? 108 : 0, h = folded ? 430 : 640;
      fitEl.style.transform = 'scale(' + k.toFixed(3) + ')';
      fitEl.style.top = Math.round(-top * k) + 'px';
      frame.style.height = Math.round(h * k) + 'px';
    }

    function apply() {
      root.style.transform = folded ? 'translateY(-10px) rotateX(-24deg)' : 'translateY(-50px) rotateX(55deg) scale(0.78)';
      T.style.transform = folded ? 'rotateX(-90deg)' : 'rotateX(0deg)';
      B.style.transform = folded ? 'rotateX(90deg)' : 'rotateX(0deg)';
      L.style.transform = folded ? 'rotateY(90deg)' : 'rotateY(0deg)';
      R.style.transform = folded ? 'rotateY(-90deg)' : 'rotateY(0deg)';
      lid.style.transform = folded ? 'rotateX(90deg)' : 'rotateX(0deg)';
      [T, B, L, R].forEach(function (x) { x.style.transitionDelay = folded ? '0.3s' : '0s'; });
      lid.style.transitionDelay = folded ? '0s' : '0.5s';
      if (hint) hint.style.opacity = folded ? '1' : '0';
      if (shadow) shadow.style.opacity = folded ? '1' : '0';
      btn.textContent = folded ? 'Ouvrir la box' : 'Refermer la box';
      btn.setAttribute('aria-expanded', folded ? 'false' : 'true');
      btn.setAttribute('aria-label', (folded ? 'Ouvrir' : 'Refermer') + btn.getAttribute('aria-label').replace(/^(Ouvrir|Refermer)/, ''));

      if (chest) {
        chest.style.transform = folded ? 'scale(0)' : 'scale(1.1)';
        chest.style.transitionDelay = folded ? '0s' : '1.05s';
        if (chestLid) {
          chestLid.style.transform = 'translate3d(0,-39px,52px) rotateX(' + (folded ? 0 : 112) + 'deg)';
          chestLid.style.transitionDelay = folded ? '0s' : '1.85s';
        }
        anims.forEach(function (x) { x.cancel(); });
        anims = [];
        if (folded) letters.forEach(function (l) { l.style.opacity = '0'; });
        else later(function () {
          if (folded || !letters.length || !letters[0].animate) { letters.forEach(function (l) { l.style.opacity = '1'; }); return; }
          var word = letters[0].parentElement;
          var mid = word.offsetWidth / 2;
          letters.forEach(function (l, i) {
            var dx = mid - (l.offsetLeft + l.offsetWidth / 2);
            var turn = (i % 2 ? 1 : -1) * (160 + Math.random() * 140);
            l.style.opacity = '1';
            anims.push(l.animate([
              { transform: 'translate(' + dx + 'px, 96px) scale(0.2) rotate(' + turn + 'deg)', opacity: 0 },
              { transform: 'translate(' + (dx * 0.35) + 'px, -46px) scale(1.18) rotate(' + (turn * 0.15) + 'deg)', opacity: 1, offset: 0.55 },
              { transform: 'translate(0, 6px) scale(0.96) rotate(0deg)', opacity: 1, offset: 0.82 },
              { transform: 'none', opacity: 1 }
            ], { duration: 1150, delay: i * 110, easing: 'cubic-bezier(0.3,0.6,0.3,1)', fill: 'both' }));
          });
        }, 2350);
      }

      if (rocket) {
        if (rocketAnim) rocketAnim.cancel();
        rocketAnim = null;
        rocket.style.visibility = 'hidden';
        if (!folded && rocket.animate) later(function () {
          if (folded) return;
          // la fusée sort du poste de pilotage, tremble au démarrage puis décolle
          rocket.style.visibility = 'visible';
          rocketAnim = rocket.animate([
            { transform: 'translateY(30px) scale(0.05) rotateY(0deg)' },
            { transform: 'translateY(0) scale(1) rotateY(20deg)', offset: 0.14 },
            { transform: 'translate(-1.5px, -3px) scale(1) rotateY(30deg)', offset: 0.2 },
            { transform: 'translate(1.5px, -6px) scale(1) rotateY(40deg)', offset: 0.26 },
            { transform: 'translateY(-300px) scale(0.85) rotateY(200deg)', offset: 0.72 },
            { transform: 'translateY(-620px) scale(0.01) rotateY(320deg)' }
          ], { duration: 1900, easing: 'cubic-bezier(0.5,0,0.7,0.5)', fill: 'forwards' });
        }, 1150);
      }
      fit();
    }

    function toggle() { folded = !folded; apply(); }
    btn.addEventListener('click', toggle);
    root.addEventListener('click', toggle);

    if (!reduce && wiggle.animate) {
      var shake = function () {
        if (!folded) return;
        wiggle.animate([
          { transform: 'none' },
          { transform: 'translateY(-16px) rotateZ(-5deg)', offset: 0.25 },
          { transform: 'translateY(-10px) rotateZ(5deg)', offset: 0.5 },
          { transform: 'translateY(-4px) rotateZ(-3deg)', offset: 0.75 },
          { transform: 'none' }
        ], { duration: 900, easing: 'ease-in-out' });
      };
      later(shake, 900);
      setInterval(shake, 3400);
    }

    apply();
    return {
      fit: fit,
      tick: function (now) {
        var dt = Math.min((now - lastT) / 1000, 0.05);
        lastT = now;
        var target = folded ? 28 : 0;
        ang += (target - ang) * Math.min(1, dt * 4);
        spin.style.transform = 'rotateY(' + ang.toFixed(2) + 'deg)';
      }
    };
  }

  var boxes = Array.prototype.map.call(document.querySelectorAll('[data-box]'), setupBox);
  (function loop(now) {
    boxes.forEach(function (b) { b.tick(now); });
    requestAnimationFrame(loop);
  })(performance.now());
  window.addEventListener('resize', function () { boxes.forEach(function (b) { b.fit(); }); });
})();
