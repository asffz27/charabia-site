(function () {
  'use strict';

  /* ▼▼▼ ENVOI DU FORMULAIRE ▼▼▼
     Pour recevoir les demandes automatiquement, coller entre les apostrophes l'adresse
     « Application Web » du Google Apps Script (elle se termine par /exec).
     Laissée vide, le formulaire ouvre la messagerie du visiteur avec un e-mail prérempli
     adressé à contact.charabia@gmail.com. */
  var SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbyt4lXZ8Rx4Iwu-YgXNOEHU_KdVlnGqLZn6YdLswqqr3b_jWw2-qzKBq97NyLw6LtkG/exec';
  var CONTACT_EMAIL = 'contact.charabia@gmail.com';
  /* ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲ */

  var PROFILS = {
    ecole: { label: 'Établissement scolaire', orgLabel: 'Établissement', orgPh: 'Collège, lycée…', emailPh: 'prenom.nom@ac-academie.fr', rolePh: '' },
    entreprise: { label: 'Entreprise', orgLabel: 'Entreprise', orgPh: 'Nom de l’entreprise', emailPh: 'prenom.nom@entreprise.fr', rolePh: 'Responsable RSE, direction…' },
    autre: { label: 'Autre structure', orgLabel: 'Structure', orgPh: 'Collectivité, association…', emailPh: 'prenom.nom@exemple.fr', rolePh: 'Chargé·e de mission, élu·e…' }
  };
  var OBJETS = { atelier: 'Organiser un atelier', partenariat: 'Partenariat', autre: 'Autre' };
  var ATELIERS = { kohlantia: 'Koh LantIA', spatial: 'SpatIAl', 'les-deux': 'Les deux' };
  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

  var $ = function (id) { return document.getElementById(id); };
  var form = $('cform');
  var st = { profil: 'ecole', objet: 'atelier', atelier: '', tried: false, sending: false };

  try {
    var p = new URLSearchParams(location.search);
    var o = p.get('objet'), a = p.get('atelier'), pr = p.get('profil');
    if (pr && PROFILS[pr]) st.profil = pr;
    if (o && OBJETS[o]) st.objet = o;
    if (a && ATELIERS[a]) { st.atelier = a; st.objet = 'atelier'; st.profil = 'ecole'; }
  } catch (e) {}

  function chips(group) { return form.querySelectorAll('[data-group="' + group + '"] .chip'); }

  function render() {
    var prof = PROFILS[st.profil];
    var ent = st.profil === 'entreprise';
    if (ent && st.objet === 'atelier') st.objet = 'partenariat';
    chips('profil').forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.v === st.profil)); });
    chips('objet').forEach(function (b) {
      b.hidden = ent && b.dataset.v === 'atelier';
      b.setAttribute('aria-pressed', String(b.dataset.v === st.objet));
    });
    chips('atelier').forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.v === st.atelier)); });
    $('atelier-set').hidden = !(st.objet === 'atelier' && !ent);
    $('c-org-label').textContent = prof.orgLabel;
    $('c-org').placeholder = prof.orgPh;
    $('c-email').placeholder = prof.emailPh;
    var isEcole = st.profil === 'ecole';
    $('c-role-sel').hidden = !isEcole;
    $('c-role-txt').hidden = isEcole;
    $('c-role-txt').placeholder = prof.rolePh;
    $('c-role-label').setAttribute('for', isEcole ? 'c-role-sel' : 'c-role-txt');
    validate();
  }

  function validate() {
    var emailOk = EMAIL_RE.test($('c-email').value.trim());
    var deptOk = !!$('c-dept').value;
    var consentOk = $('c-consent').checked;
    var show = function (id, field, bad) {
      $(id).hidden = !(st.tried && bad);
      if (field) field.setAttribute('aria-invalid', String(st.tried && bad));
    };
    show('c-email-err', $('c-email'), !emailOk);
    show('c-dept-err', $('c-dept'), !deptOk);
    show('c-consent-err', $('c-consent'), !consentOk);
    return emailOk && deptOk && consentOk;
  }

  ['profil', 'objet', 'atelier'].forEach(function (g) {
    chips(g).forEach(function (b) {
      b.addEventListener('click', function () {
        st[g] = b.dataset.v;
        if (g === 'profil') { $('c-role-sel').value = ''; $('c-role-txt').value = ''; }
        render();
      });
    });
  });
  ['c-email', 'c-dept', 'c-consent'].forEach(function (id) {
    $(id).addEventListener('input', validate);
    $(id).addEventListener('change', validate);
  });

  function payload() {
    var ent = st.profil === 'entreprise';
    return {
      profil: st.profil,
      email: $('c-email').value.trim(),
      dept: $('c-dept').value,
      role: st.profil === 'ecole' ? $('c-role-sel').value : $('c-role-txt').value,
      name: $('c-name').value,
      org: $('c-org').value,
      objet: st.objet,
      atelier: ent || st.objet !== 'atelier' ? '' : st.atelier,
      message: $('c-msg').value,
      website: $('c-website').value
    };
  }

  function showSent(email, viaMail) {
    form.hidden = true;
    $('c-sent').hidden = false;
    var t = $('c-sent-text');
    t.textContent = '';
    if (viaMail) {
      t.append('Votre messagerie s’est ouverte avec votre demande déjà rédigée. Il ne vous reste plus qu’à l’envoyer. Si rien ne s’est ouvert, écrivez-nous à ');
      var a = document.createElement('a'); a.href = 'mailto:' + CONTACT_EMAIL; a.textContent = CONTACT_EMAIL; t.append(a, '.');
    } else {
      t.append('Votre demande a bien été envoyée. Un e-mail de confirmation vous a été adressé à ');
      var s = document.createElement('strong'); s.style.fontWeight = '600'; s.style.color = '#0B0D18'; s.textContent = email;
      t.append(s, '. Nous revenons vers vous très rapidement.');
    }
    $('c-sent').scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  function mailto(d) {
    var lines = [
      'Profil : ' + PROFILS[d.profil].label,
      'Demande : ' + OBJETS[d.objet] + (d.atelier ? ' (' + ATELIERS[d.atelier] + ')' : ''),
      'Nom : ' + (d.name || '—'),
      'Fonction : ' + (d.role || '—'),
      PROFILS[d.profil].orgLabel + ' : ' + (d.org || '—'),
      'Département : ' + d.dept,
      'E-mail : ' + d.email,
      '',
      d.message
    ];
    var subject = 'Demande via le site : ' + OBJETS[d.objet] + (d.org ? ' – ' + d.org : '');
    location.href = 'mailto:' + CONTACT_EMAIL + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (st.sending) return;
    st.tried = true;
    if (!validate()) {
      var bad = form.querySelector('[aria-invalid="true"]');
      if (bad) bad.focus();
      return;
    }
    var d = payload();
    if (d.website) return; // champ piège anti-robots
    $('c-send-err').hidden = true;
    if (!SCRIPT_URL) { mailto(d); showSent(d.email, true); return; }

    st.sending = true;
    var btn = $('c-submit');
    btn.disabled = true; btn.setAttribute('aria-busy', 'true'); btn.textContent = 'Envoi en cours…';
    fetch(SCRIPT_URL, { method: 'POST', body: new URLSearchParams(d) })
      .then(function (r) { return r.json(); })
      .then(function (res) {
        if (!res || !res.ok) throw new Error((res && res.erreur) || 'envoi');
        showSent(d.email, false);
      })
      .catch(function () { $('c-send-err').hidden = false; })
      .then(function () {
        st.sending = false;
        btn.disabled = false; btn.removeAttribute('aria-busy'); btn.textContent = 'Envoyer ma demande';
      });
  });

  $('c-reset').addEventListener('click', function () {
    form.reset();
    st = { profil: 'ecole', objet: 'atelier', atelier: '', tried: false, sending: false };
    form.hidden = false;
    $('c-sent').hidden = true;
    render();
  });

  render();
})();
