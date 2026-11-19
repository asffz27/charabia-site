from common import nav, footer, page

DEPTS = """01 Ain|02 Aisne|03 Allier|04 Alpes-de-Haute-Provence|05 Hautes-Alpes|06 Alpes-Maritimes|07 Ardèche|08 Ardennes|09 Ariège|10 Aube|11 Aude|12 Aveyron|13 Bouches-du-Rhône|14 Calvados|15 Cantal|16 Charente|17 Charente-Maritime|18 Cher|19 Corrèze|2A Corse-du-Sud|2B Haute-Corse|21 Côte-d’Or|22 Côtes-d’Armor|23 Creuse|24 Dordogne|25 Doubs|26 Drôme|27 Eure|28 Eure-et-Loir|29 Finistère|30 Gard|31 Haute-Garonne|32 Gers|33 Gironde|34 Hérault|35 Ille-et-Vilaine|36 Indre|37 Indre-et-Loire|38 Isère|39 Jura|40 Landes|41 Loir-et-Cher|42 Loire|43 Haute-Loire|44 Loire-Atlantique|45 Loiret|46 Lot|47 Lot-et-Garonne|48 Lozère|49 Maine-et-Loire|50 Manche|51 Marne|52 Haute-Marne|53 Mayenne|54 Meurthe-et-Moselle|55 Meuse|56 Morbihan|57 Moselle|58 Nièvre|59 Nord|60 Oise|61 Orne|62 Pas-de-Calais|63 Puy-de-Dôme|64 Pyrénées-Atlantiques|65 Hautes-Pyrénées|66 Pyrénées-Orientales|67 Bas-Rhin|68 Haut-Rhin|69 Rhône|70 Haute-Saône|71 Saône-et-Loire|72 Sarthe|73 Savoie|74 Haute-Savoie|75 Paris|76 Seine-Maritime|77 Seine-et-Marne|78 Yvelines|79 Deux-Sèvres|80 Somme|81 Tarn|82 Tarn-et-Garonne|83 Var|84 Vaucluse|85 Vendée|86 Vienne|87 Haute-Vienne|88 Vosges|89 Yonne|90 Territoire de Belfort|91 Essonne|92 Hauts-de-Seine|93 Seine-Saint-Denis|94 Val-de-Marne|95 Val-d’Oise|971 Guadeloupe|972 Martinique|973 Guyane|974 La Réunion|976 Mayotte"""

OPTIONS = "\n                  ".join(
    f'<option value="{d.split(" ", 1)[0]}">{d.split(" ", 1)[0]} – {d.split(" ", 1)[1]}</option>' for d in DEPTS.split("|"))

LABEL = "display:block;font-size:14.5px;font-weight:600;margin-bottom:8px"
LEGEND = "padding:0;font-size:14.5px;font-weight:600;margin-bottom:10px"
STAR = '<span aria-hidden="true" style="color:#1B45F2">*</span>'
ERR = "margin:7px 0 0;font-size:13.5px;color:#B42318"

BODY = f'''<div style="background:#F3F0E9;min-height:100svh;overflow-x:hidden">
{nav("contact.html")}

  <header style="padding:clamp(112px,12vw,152px) 24px clamp(40px,5vw,64px)">
    <div style="max-width:1140px;margin:0 auto">
      <p style="margin:0 0 22px;font-size:17px;font-weight:600;color:#1B45F2">Nous contacter</p>
      <h1 style="margin:0 0 20px;font-size:clamp(40px,6vw,80px);line-height:1;letter-spacing:-0.035em;font-weight:600">Parlons de votre projet.</h1>
      <p style="margin:0;font-size:clamp(17px,1.8vw,21px);line-height:1.55;color:#585463;max-width:54ch">Établissement scolaire, entreprise ou autre structure&nbsp;: un atelier à organiser, un partenariat à imaginer ou une simple question&nbsp;? Laissez-nous quelques informations, nous revenons vers vous.</p>
    </div>
  </header>

  <main style="padding:0 24px clamp(90px,11vw,150px)">
    <div style="max-width:1140px;margin:0 auto;display:flex;flex-wrap:wrap;gap:clamp(32px,5vw,64px);align-items:flex-start">

      <aside style="flex:1 1 280px;min-width:0;display:flex;flex-direction:column;gap:28px;padding-top:8px">
        <div>
          <div style="font-size:14px;font-weight:600;color:#1B45F2;margin-bottom:8px">Par e-mail</div>
          <a href="mailto:contact.charabia@gmail.com" style="font-size:18px;font-weight:600;color:#0B0D18" style-hover="color:#1B45F2">contact.charabia@gmail.com</a>
        </div>
        <div>
          <div style="font-size:14px;font-weight:600;color:#1B45F2;margin-bottom:8px">Sur LinkedIn</div>
          <a href="https://www.linkedin.com/company/charab-ia/" target="_blank" rel="noopener" style="font-size:18px;font-weight:600;color:#0B0D18" style-hover="color:#1B45F2">CharabIA</a>
        </div>
        <div style="border-top:1px solid rgba(11,13,24,0.14);padding-top:24px">
          <div style="font-size:14px;font-weight:600;color:#0B0D18;margin-bottom:8px">Vos données</div>
          <p style="margin:0;font-size:14.5px;line-height:1.6;color:#585463">Les informations de ce formulaire servent uniquement à répondre à votre demande. Vous pouvez demander leur suppression à tout moment. <a href="mentions-legales.html">Mentions légales</a></p>
        </div>
      </aside>

      <section aria-label="Formulaire de contact" style="flex:999 1 560px;min-width:0;background:#EAE6DC;border:1px solid rgba(11,13,24,0.1);border-radius:24px;padding:clamp(24px,4vw,44px);position:relative">

        <form id="cform" novalidate style="display:flex;flex-direction:column;gap:22px">
          <fieldset style="margin:0;padding:0;border:0;min-width:0">
            <legend style="{LEGEND}">Vous êtes</legend>
            <div class="chips" data-group="profil">
              <button type="button" class="chip" data-v="ecole">Établissement scolaire</button>
              <button type="button" class="chip" data-v="entreprise">Entreprise</button>
              <button type="button" class="chip" data-v="autre">Autre structure</button>
            </div>
          </fieldset>

          <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:22px 18px">
            <div>
              <label for="c-email" style="{LABEL}">Adresse e-mail {STAR}</label>
              <input id="c-email" name="email" class="f-in" type="email" autocomplete="email" inputmode="email" aria-required="true" aria-describedby="c-email-err">
              <p id="c-email-err" hidden style="{ERR}">Indiquez une adresse e-mail valide.</p>
            </div>
            <div>
              <label for="c-dept" style="{LABEL}">Département {STAR}</label>
              <select id="c-dept" name="dept" class="f-in" aria-required="true" aria-describedby="c-dept-err">
                  <option value="">Choisir un département</option>
                  {OPTIONS}
                  <option value="autre">Autre (hors départements)</option>
              </select>
              <p id="c-dept-err" hidden style="{ERR}">Choisissez votre département.</p>
            </div>
          </div>

          <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:22px 18px">
            <div>
              <label for="c-role-sel" id="c-role-label" style="{LABEL}">Votre fonction</label>
              <select id="c-role-sel" class="f-in">
                <option value="">Choisir</option>
                <option value="Professeur·e">Professeur·e</option>
                <option value="Chef·fe d’établissement">Chef·fe d’établissement</option>
                <option value="Conseiller·e principal·e d’éducation">Conseiller·e principal·e d’éducation</option>
                <option value="Autre">Autre</option>
              </select>
              <input id="c-role-txt" class="f-in" type="text" autocomplete="organization-title" hidden aria-labelledby="c-role-label">
            </div>
            <div>
              <label for="c-name" style="{LABEL}">Nom et prénom</label>
              <input id="c-name" name="name" class="f-in" type="text" autocomplete="name">
            </div>
          </div>

          <div>
            <label for="c-org" id="c-org-label" style="{LABEL}">Établissement</label>
            <input id="c-org" name="org" class="f-in" type="text" autocomplete="organization">
          </div>

          <fieldset style="margin:0;padding:0;border:0;min-width:0">
            <legend style="{LEGEND}">Votre demande concerne</legend>
            <div class="chips" data-group="objet">
              <button type="button" class="chip" data-v="atelier">Organiser un atelier</button>
              <button type="button" class="chip" data-v="partenariat">Partenariat</button>
              <button type="button" class="chip" data-v="autre">Autre</button>
            </div>
          </fieldset>

          <fieldset id="atelier-set" style="margin:0;padding:0;border:0;min-width:0">
            <legend style="{LEGEND}">Atelier souhaité</legend>
            <div class="chips blue" data-group="atelier">
              <button type="button" class="chip" data-v="kohlantia">Koh LantIA</button>
              <button type="button" class="chip" data-v="spatial">SpatIAl</button>
              <button type="button" class="chip" data-v="les-deux">Les deux</button>
            </div>
          </fieldset>

          <div>
            <label for="c-msg" style="{LABEL}">Message</label>
            <textarea id="c-msg" name="message" class="f-in" rows="5" placeholder="Présentez-nous votre projet ou votre question en quelques lignes : contexte, public concerné, calendrier envisagé…" style="resize:vertical;min-height:132px"></textarea>
          </div>

          <div>
            <label style="display:flex;gap:12px;align-items:flex-start;font-size:14.5px;line-height:1.55;color:#3A3642;cursor:pointer">
              <input id="c-consent" class="f-check" type="checkbox" aria-required="true">
              <span>J’accepte que CharabIA utilise ces informations pour répondre à ma demande. {STAR}</span>
            </label>
            <p id="c-consent-err" hidden style="margin:7px 0 0 32px;font-size:13.5px;color:#B42318">Votre accord est nécessaire pour que nous puissions vous répondre.</p>
          </div>

          <div aria-hidden="true" style="position:absolute;left:-10000px;top:auto;width:1px;height:1px;overflow:hidden">
            <label for="c-website">Ne pas remplir ce champ</label>
            <input id="c-website" type="text" tabindex="-1" autocomplete="off">
          </div>

          <p id="c-send-err" role="alert" hidden style="margin:0;padding:14px 16px;border-radius:12px;background:#FBE9E7;border:1px solid rgba(180,35,24,0.3);font-size:14.5px;line-height:1.55;color:#7A1A12">L’envoi n’a pas abouti. Réessayez dans un instant, ou écrivez-nous directement à <a href="mailto:contact.charabia@gmail.com" style="color:#7A1A12;font-weight:600;text-decoration:underline">contact.charabia@gmail.com</a>.</p>

          <div style="display:flex;flex-wrap:wrap;gap:14px 20px;align-items:center;padding-top:4px">
            <button id="c-submit" type="submit" style="min-height:48px;background:#0B0D18;color:#F3F0E9;border:none;font-family:inherit;font-size:15.5px;font-weight:600;padding:14px 30px;border-radius:99px;cursor:pointer;transition:background 0.22s ease" style-hover="background:#1B45F2">Envoyer ma demande</button>
            <span style="font-size:13.5px;color:#585463">{STAR} Champs obligatoires</span>
          </div>
        </form>

        <div id="c-sent" role="status" hidden style="flex-direction:column;align-items:flex-start;gap:18px;padding:clamp(8px,2vw,24px) 0">
          <div style="width:56px;height:56px;border-radius:50%;background:#1B45F2;color:#F3F0E9;display:flex;align-items:center;justify-content:center">
            <svg aria-hidden="true" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg>
          </div>
          <h2 style="margin:0;font-size:clamp(28px,3.4vw,44px);line-height:1.04;letter-spacing:-0.035em;font-weight:600">Merci pour votre prise de contact&nbsp;!</h2>
          <p id="c-sent-text" style="margin:0;font-size:16.5px;line-height:1.6;color:#3A3642;max-width:52ch"></p>
          <button id="c-reset" type="button" style="min-height:44px;background:transparent;color:#0B0D18;border:1px solid rgba(11,13,24,0.25);font-family:inherit;font-size:15px;font-weight:600;padding:11px 22px;border-radius:99px;cursor:pointer;transition:border-color 0.2s ease" style-hover="border-color:#1B45F2">Envoyer une autre demande</button>
        </div>
      </section>
    </div>
  </main>
{footer("contact.html")}
</div>'''

CSS = """  .f-in { width: 100%; box-sizing: border-box; background: #F3F0E9; border: 1px solid rgba(11,13,24,0.2); border-radius: 12px; padding: 13px 14px; font: inherit; font-size: 16px; color: #0B0D18; transition: border-color 0.2s ease, box-shadow 0.2s ease; }
  .f-in[hidden] { display: none; }
  .f-in::placeholder { color: #6b6676; }
  .f-in:focus { outline: none; border-color: #1B45F2; box-shadow: 0 0 0 3px rgba(27,69,242,0.18); }
  .f-in[aria-invalid="true"] { border-color: #B42318; }
  .f-check { width: 20px; height: 20px; margin: 2px 0 0; accent-color: #1B45F2; flex: 0 0 auto; }
  .chips { display: flex; flex-wrap: wrap; gap: 8px; }
  .chip { min-height: 44px; background: #F3F0E9; color: #0B0D18; border: 1px solid rgba(11,13,24,0.2); font-family: inherit; font-size: 15px; font-weight: 600; padding: 10px 18px; border-radius: 99px; cursor: pointer; transition: border-color 0.2s ease; }
  .chip:hover { border-color: #1B45F2; }
  .chip[hidden] { display: none; }
  .chip[aria-pressed="true"] { background: #0B0D18; color: #F3F0E9; border-color: #0B0D18; }
  .chips.blue .chip[aria-pressed="true"] { background: #1B45F2; border-color: #1B45F2; }
  #c-sent:not([hidden]) { display: flex; }
  #c-submit[disabled] { opacity: 0.7; cursor: progress; }
"""


def build():
    return page("Nous contacter — CharabIA", "#F3F0E9", BODY, CSS, '<script src="/js/contact.js"></script>',
                desc="Contactez CharabIA pour organiser un atelier d’initiation à l’IA dans votre établissement ou imaginer un partenariat.")
