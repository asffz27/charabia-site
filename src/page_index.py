from common import nav, page, wordmark, TEAM, partners_grid, footer_links

INTRO_WORD = (
    '<span style="display:inline-flex;align-items:baseline;font-family:\'Archivo Black\',system-ui,sans-serif;font-size:clamp(52px,12vw,190px);line-height:0.78;letter-spacing:-0.02em;color:#F3F0E9">'
    '<span data-l="">C</span><span data-l="" style="font-size:0.6em">H</span><span data-l="" style="font-size:0.55em">A</span>'
    '<span data-l="" style="font-size:0.55em">R</span><span data-l="" style="font-size:0.55em">A</span><span data-l="" style="font-size:0.55em">B</span>'
    '<span data-l="" data-ia="" style="font-size:1.06em">i</span><span data-l="" data-ia="">A</span></span>'
)

HERO_GRAD = ("https://www.shadergradient.co/customize?animate=on&amp;axesHelper=off&amp;bgColor1=%23000000&amp;bgColor2=%23000000&amp;brightness=1.2&amp;cAzimuthAngle=180&amp;cDistance=3.6&amp;cPolarAngle=90&amp;cameraZoom=1&amp;color1=%231B45F2&amp;color2=%23070F38&amp;color3=%237CA0FF&amp;destination=onCanvas&amp;embedMode=off&amp;envPreset=city&amp;format=gif&amp;fov=45&amp;frameRate=10&amp;gizmoHelper=hide&amp;grain=on&amp;lightType=3d&amp;pixelDensity=1&amp;positionX=-1.4&amp;positionY=0&amp;positionZ=0&amp;range=disabled&amp;rangeEnd=40&amp;rangeStart=0&amp;reflection=0.1&amp;rotationX=0&amp;rotationY=10&amp;rotationZ=50&amp;shader=defaults&amp;type=plane&amp;uAmplitude=1&amp;uDensity=1.3&amp;uFrequency=5.5&amp;uSpeed=0.15&amp;uStrength=4&amp;uTime=0&amp;wireframe=false")

NEWS = [
    ("Atelier", "Dix ateliers Koh LantIA au collège de l’Agiot", "Novembre 2026", "college-agiot"),
    ("Partenariat", "CharabIA devient partenaire du LIEPP au sein du programme PEPPS", "Octobre 2026", "liepp-pepps"),
    ("Événement", "Les jeux CharabIA à Bois-Colombes et à l’École 42", "Septembre 2026", "bois-colombes-ecole-42"),
]

PILL = 'background:#F3F0E9;border:1px solid rgba(11,13,24,0.12);border-radius:99px;padding:9px 16px;font-size:14.5px;font-weight:600'


def atout(title, text):
    return (f'<div data-reveal="" style="background:#F3F0E9;padding:32px 28px"><div style="font-size:22px;font-weight:600;letter-spacing:-0.025em;margin-bottom:12px;color:#1B45F2">{title}</div>'
            f'<p style="margin:0;font-size:15.5px;line-height:1.6;color:#585463">{text}</p></div>')


def team_cards():
    out = ""
    for name, role, photo, url in TEAM:
        out += f'''<a href="{url}" target="_blank" rel="noopener" data-reveal="" aria-label="Profil LinkedIn de {name}" style="display:block;color:inherit;background:#F3F0E9;border:1px solid rgba(11,13,24,0.1);border-radius:18px;overflow:hidden;transition:border-color 0.3s ease,transform 0.3s ease" style-hover="border-color:#1B45F2;transform:translateY(-4px)">
            <div style="aspect-ratio:3/4;background:#0B0D18;display:flex;align-items:center;justify-content:center;overflow:hidden"><img src="{photo}" alt="Portrait de {name}" loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block"></div>
            <div style="padding:16px 18px 18px"><div style="font-size:13px;font-weight:600;color:#1B45F2;margin-bottom:5px">{role}</div><div style="font-size:17px;font-weight:600;letter-spacing:-0.02em">{name}</div></div>
          </a>
          '''
    return out


def news_rows():
    out = ""
    for tag, title, date, anchor in NEWS:
        out += f'''<a href="actualites.html#{anchor}" style="display:flex;flex-wrap:wrap;gap:10px 26px;align-items:center;background:#0B0D18;color:#F3F0E9;padding:26px 24px;transition:background 0.25s ease" style-hover="background:#151A2E">
            <span style="flex:0 0 auto;font-size:14px;font-weight:600;color:#5C86FF">{tag}</span>
            <span style="flex:1 1 240px;min-width:0;font-size:clamp(19px,2.1vw,27px);font-weight:500;letter-spacing:-0.025em;line-height:1.24;text-wrap:pretty">{title}</span>
            <span style="flex:0 0 auto;margin-left:auto;font-size:14px;color:rgba(243,240,233,0.5);font-variant-numeric:tabular-nums">{date}</span>
          </a>
          '''
    return out


BODY = f'''<div style="background:#F3F0E9;overflow-x:hidden">

  <div id="intro" style="position:fixed;inset:0;z-index:200;background:transparent;overflow:hidden;transition:opacity 0.9s ease;pointer-events:auto">
    <div style="position:absolute;inset:0;background:radial-gradient(120% 95% at 50% 46%, rgba(5,6,12,0.14) 0%, rgba(5,6,12,0.4) 58%, rgba(5,6,12,0.68) 100%)"></div>
    <div id="introWord" translate="no" aria-label="CharabIA" style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;padding:24px;box-sizing:border-box">
      {INTRO_WORD}
    </div>
    <div style="position:absolute;left:0;right:0;bottom:38px;display:flex;justify-content:center">
      <button id="introSkip" type="button" style="background:rgba(243,240,233,0.1);color:#F3F0E9;border:1px solid rgba(243,240,233,0.4);font-family:inherit;font-size:15px;font-weight:600;padding:12px 28px;border-radius:99px;cursor:pointer;backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);transition:background 0.25s ease,color 0.25s ease" style-hover="background:#F3F0E9;color:#0B0D18">Entrer</button>
    </div>
  </div>
{nav("index.html")}

  <header id="top" style="position:relative;min-height:100svh;background:#0b1a6e radial-gradient(130% 120% at 28% 38%, #1B45F2 0%, #1236b8 42%, #0b1a6e 78%, #070F38 100%);color:#F3F0E9;overflow:hidden;display:flex;flex-direction:column;justify-content:flex-end">
    <shader-gradient id="heroGrad" style="position:absolute;inset:0;opacity:0;transition:opacity 0.7s ease" url="{HERO_GRAD}"></shader-gradient>
    <div style="position:absolute;inset:0;background:linear-gradient(to bottom, rgba(5,6,12,0.34) 0%, rgba(5,6,12,0.38) 44%, rgba(5,6,12,0.8) 100%)"></div>
    <div style="position:relative;width:100%;max-width:1560px;margin:0 auto;box-sizing:border-box;padding:124px 24px 64px">
      <h1 data-reveal="" translate="no" aria-label="CharabIA" style="margin:0 0 36px;display:flex;align-items:baseline;font-family:'Archivo Black',system-ui,sans-serif;font-weight:400;font-size:clamp(58px,14vw,212px);line-height:0.78;letter-spacing:-0.02em;text-shadow:0.03em 0.04em 0 #93A9F7"><span>C</span><span style="font-size:0.6em">H</span><span style="font-size:0.55em">A</span><span style="font-size:0.55em">R</span><span style="font-size:0.55em">A</span><span style="font-size:0.55em">B</span><span style="font-size:1.06em;color:#5C86FF">i</span><span style="color:#5C86FF">A</span></h1>
      <div style="display:flex;flex-direction:column;align-items:flex-start;gap:20px;max-width:860px">
        <p data-reveal="" style="margin:0;font-size:clamp(21px,2.4vw,31px);line-height:1.3;font-weight:500;letter-spacing:-0.022em;text-wrap:pretty">Nous formons les collégiens et les professionnels à l’intelligence artificielle.</p>
        <p data-reveal="" style="margin:0;font-size:16.5px;line-height:1.62;color:rgba(243,240,233,0.75)">En deux heures, dans votre établissement ou dans vos locaux, nous vous formons aux enjeux d’IA par une approche ludique et centrée sur l’humain.</p>
        <div data-reveal="" style="display:flex;flex-wrap:wrap;gap:10px;margin-top:6px">
          <a href="colleges.html" style="background:#F3F0E9;color:#0B0D18;font-size:15.5px;font-weight:600;padding:14px 26px;border-radius:99px;transition:background 0.22s ease,color 0.22s ease" style-hover="background:#1B45F2;color:#F3F0E9">Découvrir les ateliers collèges</a>
          <a href="entreprises.html" style="background:rgba(243,240,233,0.1);color:#F3F0E9;border:1px solid rgba(243,240,233,0.55);font-size:15.5px;font-weight:600;padding:13px 26px;border-radius:99px;backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);transition:background 0.22s ease,color 0.22s ease" style-hover="background:#F3F0E9;color:#0B0D18">Découvrir les ateliers entreprises</a>
        </div>
      </div>
    </div>
  </header>

  <section style="background:#F3F0E9;padding:clamp(64px,7vw,110px) 24px">
    <div style="max-width:1140px;margin:0 auto">
      <p data-reveal="" style="margin:0 0 40px;font-size:17px;font-weight:600;color:#1B45F2">Pourquoi nous existons</p>
      <p data-reveal="" style="margin:0;font-size:clamp(30px,4.4vw,64px);line-height:1.08;letter-spacing:-0.035em;font-weight:600;text-wrap:pretty">Former les citoyens de demain à l’intelligence artificielle, dès aujourd’hui, pour que l’IA ne creuse pas davantage les inégalités sociales.</p>
    </div>
  </section>

  <section style="background:#EAE6DC;padding:clamp(56px,6vw,88px) 24px;border-top:1px solid rgba(11,13,24,0.08)">
    <div style="max-width:1140px;margin:0 auto;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:clamp(40px,6vw,88px);align-items:center">
      <div data-reveal="">
        <h2 style="margin:0 0 20px;font-size:clamp(30px,4vw,56px);line-height:1.03;letter-spacing:-0.038em;font-weight:600;text-wrap:pretty">Garantir un socle commun sur l’IA, une utilisation éclairée et sécurisée.</h2>
        <p style="margin:0 0 28px;font-size:18px;line-height:1.6;color:#585463">Un atelier complet de deux heures combinant théorie, jeu et réflexion.</p>
        <div style="display:flex;flex-wrap:wrap;gap:8px">
          <span style="{PILL}">2&nbsp;h par atelier</span>
          <span style="{PILL}">Solution clés en main</span>
          <span style="{PILL}">Alignement sur les grands cadres de l’IA</span>
        </div>
      </div>
      <div data-reveal="" style="background:#0B0D18;color:#F3F0E9;border-radius:22px;padding:30px 28px 28px;display:flex;flex-direction:column;min-height:380px">
        <div style="display:flex;justify-content:space-between;align-items:baseline;gap:12px;margin-bottom:20px">
          <div style="font-size:16px;font-weight:600;color:#F3F0E9">Info ou charabia&nbsp;?</div>
          <div id="quizStep" style="font-size:13px;color:rgba(243,240,233,0.5);font-variant-numeric:tabular-nums">1 / 4</div>
        </div>
        <p style="margin:-8px 0 22px;font-size:14.5px;line-height:1.55;color:rgba(243,240,233,0.72)">Un charabia, c’est un discours confus ou faux. Lisez chaque affirmation sur l’IA et dites s’il s’agit d’une information exacte ou de charabia.</p>
        <div id="quiz" style="display:flex;flex-direction:column;flex:1"></div>
      </div>
    </div>
  </section>

  <section id="equipe" style="background:#EAE6DC;padding:clamp(56px,6vw,88px) 24px;border-top:1px solid rgba(11,13,24,0.08)">
    <div style="max-width:1140px;margin:0 auto">
      <div data-reveal="" style="display:flex;flex-wrap:wrap;gap:12px 24px;align-items:baseline;justify-content:space-between;margin:0 0 44px">
        <h2 style="margin:0;font-size:clamp(30px,4.2vw,58px);line-height:1.03;letter-spacing:-0.04em;font-weight:600">Qui sommes-nous&nbsp;?</h2>
        <a href="histoire.html" style="font-size:15px;font-weight:600;color:#1B45F2" style-hover="color:#0B0D18">Découvrir notre histoire</a>
      </div>
      <div style="display:grid;grid-template-columns:repeat(2,minmax(0,280px));justify-content:center;gap:clamp(10px,2vw,14px)">
          {team_cards()}
      </div>
    </div>
  </section>

  <section id="actualites" style="background:#0B0D18;color:#F3F0E9;padding:clamp(64px,7vw,104px) 24px">
    <div style="max-width:1140px;margin:0 auto">
      <div data-reveal="" style="display:flex;flex-wrap:wrap;gap:12px 24px;align-items:baseline;justify-content:space-between;margin-bottom:36px">
        <h2 style="margin:0;font-size:clamp(30px,4.2vw,58px);line-height:1.03;letter-spacing:-0.04em;font-weight:600">Actualités</h2>
        <a href="actualites.html" style="font-size:15px;font-weight:600;color:#5C86FF" style-hover="color:#F3F0E9">Toutes les actualités</a>
      </div>
      <div style="display:grid;gap:1px;background:rgba(243,240,233,0.16);border:1px solid rgba(243,240,233,0.16);border-radius:20px;overflow:hidden">
          {news_rows()}
      </div>
    </div>
  </section>

  <section style="background:#F3F0E9;padding:clamp(48px,5vw,72px) 24px clamp(36px,4vw,56px);border-top:1px solid rgba(11,13,24,0.08)">
    <div style="max-width:1140px;margin:0 auto">
      <p data-reveal="" style="margin:0 0 28px;font-size:14px;font-weight:600;color:#1B45F2">Ils nous ont accompagnés</p>
      {partners_grid(reveal=True)}
    </div>
  </section>

  <footer id="contact" style="background:#F3F0E9;padding:clamp(48px,6vw,80px) 24px 40px">
    <div style="max-width:1140px;margin:0 auto">
      <div data-reveal="" style="display:flex;flex-direction:column;gap:28px;padding-bottom:56px;border-bottom:1px solid rgba(11,13,24,0.14)">
        <h2 style="margin:0;font-size:clamp(34px,5.6vw,80px);line-height:0.98;letter-spacing:-0.045em;font-weight:600;text-wrap:pretty">Nous sommes à votre écoute.</h2>
        <div style="min-width:0">
          <p style="margin:0 0 22px;font-size:17px;line-height:1.6;color:#585463">Vous pouvez nous contacter par e-mail à l'adresse&nbsp;: <a href="mailto:contact.charabia@gmail.com" style="color:#0B0D18;font-weight:600">contact.charabia@gmail.com</a> mais aussi sur <a href="https://www.linkedin.com/company/charab-ia/" target="_blank" rel="noopener">LinkedIn</a>&nbsp;!</p>
          <a href="contact.html?objet=atelier" style="display:inline-flex;background:#0B0D18;color:#F3F0E9;font-size:15.5px;font-weight:600;padding:14px 28px;border-radius:99px;transition:background 0.22s ease" style-hover="background:#1B45F2;color:#F3F0E9">Organiser un atelier</a>
        </div>
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:20px 24px;align-items:center;justify-content:space-between;padding-top:26px;font-size:13.5px;color:rgba(11,13,24,0.55)">
        <span>© 2026 – CharabIA</span>
        <div style="display:flex;flex-wrap:wrap;gap:22px">
        {footer_links("index.html")}
        </div>
      </div>
    </div>
  </footer>

</div>'''

CSS = """  body { background: #05060C; }
  @keyframes cb-ripple { 0% { transform: scale(0.2); opacity: 0.9; } 100% { transform: scale(10); opacity: 0; } }
  .q-btn { flex:1; background:transparent; color:#F3F0E9; border:1px solid rgba(243,240,233,0.32); font-family:inherit; font-size:15.5px; font-weight:600; padding:13px 10px; border-radius:99px; cursor:pointer; transition:background 0.2s ease,border-color 0.2s ease; }
  .q-btn:hover { background:#1B45F2; border-color:#1B45F2; }
  .q-main { background:#F3F0E9; color:#0B0D18; border:none; font-family:inherit; font-size:15px; font-weight:600; padding:12px 24px; border-radius:99px; cursor:pointer; transition:background 0.2s ease,color 0.2s ease; display:inline-flex; }
  .q-main:hover { background:#1B45F2; color:#F3F0E9; }
  .q-ghost { background:transparent; color:#F3F0E9; border:1px solid rgba(243,240,233,0.32); font-family:inherit; font-size:15px; font-weight:600; padding:12px 24px; border-radius:99px; cursor:pointer; transition:border-color 0.2s ease; }
  .q-ghost:hover { border-color:#F3F0E9; }
"""

SCRIPTS = '<script src="/js/shader-gradient.js"></script>\n<script src="/js/accueil.js"></script>'


def build():
    return page("CharabIA — former à l'intelligence artificielle", "#05060C", BODY, CSS, SCRIPTS, body_bg="#05060C")
