from common import nav, footer, page, wordmark
from page_index import atout

FACE = ('position:absolute;inset:0;transform:translateZ(0.6px);background-color:#1a2a5c;background-position:center;background-size:cover;'
        'background-repeat:no-repeat;border-radius:8px;backface-visibility:hidden;border:1px solid rgba(11,13,24,0.18);box-sizing:border-box')
BACK = ('position:absolute;inset:0;background:radial-gradient(120% 90% at 30% 18%, rgba(124,160,255,0.16) 0%, rgba(124,160,255,0) 55%), '
        'linear-gradient(160deg,#151d4a 0%,#0b1236 45%,#060a26 100%);border-radius:10px;backface-visibility:hidden;transform:rotateY(180deg) translateZ(0.6px);'
        'border:1px solid rgba(124,160,255,0.42);box-shadow:inset 0 1px 0 rgba(243,240,233,0.12), inset 0 0 0 12px rgba(5,8,28,0.28), '
        'inset 0 0 0 13px rgba(124,160,255,0.28), inset 0 -40px 60px rgba(0,0,0,0.32);box-sizing:border-box;display:flex;align-items:center;justify-content:center')
FLAP = 'position:absolute;width:220px;height:220px;transform-style:preserve-3d;transition:transform 0.9s cubic-bezier(0.4,0,0.2,1);will-change:transform'


def panel(cls, logo=False, rotate=False):
    inner = wordmark("32px", extra="transform:rotate(180deg)" if rotate else "") if logo else ""
    return f'<div class="bx-face {cls}"></div><div class="bx-back">{inner}</div>'


def flap(name, pos, origin, content):
    return f'<div data-flap="{name}" class="bx-flap" style="{pos};transform-origin:{origin}">{content}</div>'


STRIPS = [("77.25px", "7.61px", "-78.75deg", 0.8), ("71.43px", "21.67px", "-56.25deg", 0.9), ("60.67px", "32.43px", "-33.75deg", None),
          ("46.61px", "38.25px", "-11.25deg", 1.08), ("31.39px", "38.25px", "11.25deg", 1.08), ("17.33px", "32.43px", "33.75deg", None),
          ("6.57px", "21.67px", "56.25deg", 0.9), ("0.75px", "7.61px", "78.75deg", 0.8)]


def chest():
    strips = ""
    for y, z, rx, b in STRIPS:
        f = f";filter:brightness({b})" if b else ""
        strips += f'<div class="ch-strip" style="transform:translate3d(0,{y},{z}) rotateX({rx}){f}"></div>'
    return f'''<div data-chest="" style="position:absolute;left:50%;top:50%;width:0;height:0;transform-style:preserve-3d;transform:scale(0);transition:transform 0.65s cubic-bezier(0.34,1.56,0.64,1);will-change:transform">
            <div aria-hidden="true" style="position:absolute;left:-84px;top:-58px;width:168px;height:116px;transform:translateZ(0.8px);background:radial-gradient(closest-side, rgba(11,13,24,0.42), rgba(11,13,24,0))"></div>
            <div aria-hidden="true" style="position:absolute;left:-58px;top:-35px;width:116px;height:70px;transform:translateZ(3px);background:radial-gradient(closest-side, #eef2ff 0%, #9db6ff 38%, #3d5fd8 72%, #1b2560 100%);border-radius:4px"></div>
            <div class="ch-in" style="position:absolute;left:-62px;top:-26px;width:124px;height:52px;transform:translate3d(0,36.5px,26px) rotateX(-90deg) rotateY(180deg)"></div>
            <div class="ch-in" style="position:absolute;left:-62px;top:-26px;width:124px;height:52px;transform:translate3d(0,-36.5px,26px) rotateX(-90deg)"></div>
            <div class="ch-in" style="position:absolute;left:-39px;top:-26px;width:78px;height:52px;transform:translate3d(59.5px,0,26px) rotateZ(90deg) rotateX(-90deg)"></div>
            <div class="ch-in" style="position:absolute;left:-39px;top:-26px;width:78px;height:52px;transform:translate3d(-59.5px,0,26px) rotateZ(-90deg) rotateX(-90deg)"></div>
            <div class="ch-wood" style="position:absolute;left:-62px;top:-26px;width:124px;height:52px;transform:translate3d(0,-39px,26px) rotateX(-90deg) rotateY(180deg);filter:brightness(0.8)"></div>
            <div class="ch-wood" style="position:absolute;left:-39px;top:-26px;width:78px;height:52px;transform:translate3d(-62px,0,26px) rotateZ(90deg) rotateX(-90deg);filter:brightness(0.86)"></div>
            <div class="ch-wood" style="position:absolute;left:-39px;top:-26px;width:78px;height:52px;transform:translate3d(62px,0,26px) rotateZ(-90deg) rotateX(-90deg);filter:brightness(0.86)"></div>
            <div class="ch-wood" style="position:absolute;left:-62px;top:-26px;width:124px;height:52px;transform:translate3d(0,39px,26px) rotateX(-90deg)">
              <div style="position:absolute;left:50%;top:4px;width:20px;height:25px;margin-left:-10px;background:linear-gradient(180deg,#f3dda8,#d9b87a);border:1px solid #8a6a38;border-radius:4px;box-sizing:border-box;display:flex;align-items:center;justify-content:center"><span style="width:6px;height:10px;background:#1c120a;border-radius:3px 3px 1px 1px"></span></div>
            </div>
            <div data-chest-lid="" style="position:absolute;left:0;top:0;width:0;height:0;transform-style:preserve-3d;transform:translate3d(0,-39px,52px) rotateX(0deg);transition:transform 0.8s cubic-bezier(0.34,1.3,0.64,1);will-change:transform">
              {strips}
              <div class="ch-cap" style="transform:translate3d(-62px,39px,19.5px) rotateZ(90deg) rotateX(-90deg);filter:brightness(0.86)"></div>
              <div class="ch-cap" style="transform:translate3d(62px,39px,19.5px) rotateZ(-90deg) rotateX(-90deg);filter:brightness(0.86)"></div>
            </div>
          </div>'''


BRIGHT = [1.03, 0.83, 0.62, 0.62, 0.62, 0.62, 0.62, 0.62, 0.66, 0.91, 1.07, 1.12]


def rocket():
    parts = ""
    for i, b in enumerate(BRIGHT):
        a = f"{i * 30:.1f}deg"
        parts += (f'<div style="position:absolute;left:-4.15px;top:-84px;width:8.30px;height:66px;background:linear-gradient(180deg,#F3F0E9 0 64%,#1B45F2 64% 74%,#F3F0E9 74%);transform:rotateY({a}) translateZ(14px);backface-visibility:hidden;filter:brightness({b})"></div>'
                  f'<div style="position:absolute;left:-4.15px;top:-116px;width:8.30px;height:33px;background:#1B45F2;clip-path:polygon(50% 0,100% 100%,0 100%);transform-origin:50% 100%;transform:rotateY({a}) translateZ(14px) rotateX(23deg);backface-visibility:hidden;filter:brightness({b})"></div>'
                  f'<div style="position:absolute;left:-3.32px;top:-19px;width:6.64px;height:9px;background:#585463;transform:rotateY({a}) translateZ(11.2px);backface-visibility:hidden;filter:brightness({b})"></div>')
    for a, b in [(-45, 0.71), (45, 0.62), (135, 0.62), (225, 1.11)]:
        parts += f'<div style="position:absolute;left:0;top:-48px;width:17px;height:34px;background:#1B45F2;clip-path:polygon(0 0,100% 55%,100% 100%,0 100%);transform-origin:0 50%;transform:rotateY({a}deg) translateX(13px);backface-visibility:visible;filter:brightness({b})"></div>'
    parts += '<div style="position:absolute;left:-6px;top:-66px;width:12px;height:12px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#c9d6ff,#5C86FF 55%,#1B45F2);border:1.5px solid #0B0D18;box-sizing:border-box;transform:translateZ(14.6px)"></div>'
    for a in (0, 90):
        parts += f'<div class="rk-flame" style="position:absolute;left:-10px;top:-11px;width:20px;height:34px;background:radial-gradient(60% 75% at 50% 0%,#F3F0E9 0 22%,#9db6ff 45%,rgba(124,160,255,0) 75%);border-radius:50% 50% 50% 50% / 25% 25% 75% 75%;transform:rotateY({a}deg)"></div>'
    return ('<div data-rocket="" aria-hidden="true" style="position:absolute;left:50%;top:50%;width:0;height:0;transform-style:preserve-3d;transform:translate3d(0,6px,12px) rotateX(-55deg)">'
            f'<div data-rocket-body="" style="position:absolute;left:0;top:0;width:0;height:0;transform-style:preserve-3d;visibility:hidden;will-change:transform">{parts}</div></div>')


CHEST_WORD = ('<div data-chest-word="" aria-hidden="true" style="position:absolute;left:0;right:0;top:46px;z-index:2;display:flex;justify-content:center;pointer-events:none">'
              '<span translate="no" style="display:inline-flex;align-items:baseline;white-space:nowrap;font-family:\'Archivo Black\',system-ui,sans-serif;font-size:46px;line-height:0.8;letter-spacing:-0.015em;color:#0B0D18;text-shadow:0.03em 0.04em 0 #93A9F7">'
              + "".join(f'<span data-cl="" style="display:inline-block;opacity:0{s}">{c}</span>' for c, s in [
                  ("C", ""), ("H", ";font-size:0.6em"), ("A", ";font-size:0.55em"), ("R", ";font-size:0.55em"), ("A", ";font-size:0.55em"),
                  ("B", ";font-size:0.55em"), ("i", ";font-size:1.06em;color:#1B45F2"), ("A", ";color:#1B45F2")])
              + '</span></div>')


def box(p, name, btn_hover):
    is_kl = p == "kl"
    centre = chest() if is_kl else rocket()
    lid = flap("lid", "left:0;top:220px", "50% 0%", panel(f"{p}-lid", logo=True, rotate=True))
    flaps = (flap("T", "left:0;top:-220px", "50% 100%", panel(f"{p}-t"))
             + flap("B", "left:0;top:220px", "50% 0%", panel(f"{p}-b") + lid)
             + flap("L", "left:-220px;top:0", "100% 50%", panel(f"{p}-l", logo=True))
             + flap("R", "left:220px;top:0", "0% 50%", panel(f"{p}-r", logo=True)))
    return f'''<div data-box="" style="width:100%;display:flex;flex-direction:column;align-items:center;gap:16px">
          <div data-box-frame="" style="position:relative;width:100%;height:640px;transition:height 0.6s ease">
            <div data-box-fit="" style="position:absolute;left:50%;top:0;width:640px;height:640px;margin-left:-320px;transform-origin:50% 0;transition:top 0.6s ease;pointer-events:none">
              <div data-box-stage="" aria-hidden="true" style="position:relative;width:640px;height:640px;perspective:1400px;display:flex;align-items:center;justify-content:center;cursor:pointer;touch-action:manipulation">
                <span data-box-hint="" style="position:absolute;left:50%;top:124px;z-index:2;transform:translateX(-50%);background:#F3F0E9;color:#0B0D18;border:1px solid rgba(11,13,24,0.16);box-shadow:0 6px 18px rgba(11,13,24,0.18);font-size:15px;font-weight:700;padding:9px 18px;border-radius:99px;white-space:nowrap;transition:opacity 0.4s ease;animation:bx-bob 1.6s ease-in-out infinite">Ouvrez-moi</span>
                {CHEST_WORD if is_kl else ""}
                <div data-box-shadow="" style="position:absolute;left:50%;top:50%;width:320px;height:64px;margin:170px 0 0 -160px;background:radial-gradient(closest-side, rgba(11,13,24,0.34), rgba(11,13,24,0));transition:opacity 0.8s ease;pointer-events:none"></div>
                <div data-box-root="" style="pointer-events:auto;position:relative;width:220px;height:220px;transform-style:preserve-3d;transition:transform 1.1s cubic-bezier(0.4,0,0.2,1);will-change:transform">
                  <div data-box-wiggle="" style="position:absolute;inset:0;transform-style:preserve-3d">
                    <div data-box-spin="" style="position:absolute;inset:0;transform-style:preserve-3d;transform-origin:50% 50% 110px;will-change:transform">
                      {panel(f"{p}-c", logo=True)}
                      {centre}
                      {flaps}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div aria-hidden="true" style="height:clamp(20px,3vw,32px)"></div>
          <button type="button" data-box-btn="" aria-expanded="false" aria-label="Ouvrir la box {name} et déplier le plateau de jeu" style="position:relative;z-index:3;background:#1B45F2;color:#F3F0E9;border:none;font-family:inherit;font-size:15.5px;font-weight:600;padding:13px 26px;border-radius:99px;cursor:pointer;transition:background 0.22s ease" style-hover="{btn_hover}">Ouvrir la box</button>
          <p style="margin:0;font-size:14px;line-height:1.5;color:inherit;opacity:0.7;text-align:center">La BoxIA se déplie en un plateau de jeu.</p>
        </div>'''


def epreuves(items, dark):
    bg = "#0B0D18" if dark else "#F3F0E9"
    txt = "rgba(243,240,233,0.72)" if dark else "#585463"
    strong = "#F3F0E9" if dark else "#0B0D18"
    acc = "#5C86FF" if dark else "#1B45F2"
    out = ""
    for title, jeu, comprend in items:
        out += f'''<li style="background:{bg};padding:20px 22px">
            <div style="font-size:17.5px;font-weight:600;letter-spacing:-0.015em;margin-bottom:8px">{title}</div>
            <p style="margin:0 0 6px;font-size:15px;line-height:1.55;color:{txt}"><span style="font-weight:600;color:{strong}">Le jeu&nbsp;:</span> {jeu}</p>
            <p style="margin:0;font-size:15px;line-height:1.55;color:{txt}"><span style="font-weight:600;color:{acc}">Ce que l’élève apprend&nbsp;:</span> {comprend}</p>
          </li>
          '''
    return out


KL = [
    ("La Carte des Savoirs Engloutis", "des mots croisés sur le vocabulaire de l’IA.", "restituer les notions clés de l’IA (algorithme, données, entraînement, prompt…) discutées en début d’atelier pour savoir parler de l’IA et de ses enjeux."),
    ("Le Grimoire des Invocations", "associer des cartes pour former des paires cohérentes.", "associer un prompt à sa réponse. Comprendre que la qualité d’un prompt détermine directement la qualité de la réponse produite par l’IA."),
    ("Le Temple des Algorithmes", "une énigme mathématique à résoudre en équipe.", "une machine calcule mais ne comprend pas. Savoir quand demander de l’aide et quand réfléchir par soi-même."),
    ("Les Chroniques du Trésor Invisible", "générer une image à partir d’un récit lu à voix haute.", "élaborer un prompt complet pour générer une image la plus fidèle à une consigne. Les élèves apprennent à détecter les stéréotypes et biais produits par l’IA et à en débattre."),
]
SP = [
    ("Trajectoire", "retrouver la trajectoire qui relie la station spatiale à la Terre grâce aux étoiles.", "une IA relie des données entre elles pour retrouver un chemin ou faire une prédiction. Si les données de départ sont fausses, le résultat l’est aussi."),
    ("Fiabilité", "analyser des réponses produites par l’IA et écarter les réponses corrompues.", "une IA peut produire des réponses inexactes voire fausses. L’utilisation de l’IA nécessite de vérifier et de mobiliser son esprit critique."),
    ("Déduction", "résoudre une énigme mathématique en suivant les indices et relances d’un guidage tutoré interactif.", "développer un raisonnement progressif pour contrôler chaque réponse et consolider ses acquis durablement."),
    ("Mémoire visuelle", "générer une image à partir d’un récit lu à voix haute.", "élaborer un prompt complet pour générer une image la plus fidèle à une consigne. Les élèves apprennent à détecter les stéréotypes et biais produits par l’IA et à en débattre."),
]

PILL = 'background:#EAE6DC;border:1px solid rgba(11,13,24,0.12);border-radius:99px;padding:9px 16px;font-size:14.5px;font-weight:600'


def fondamental(title, text, refs):
    return f'''<div style="background:#EAE6DC;border:1px solid rgba(11,13,24,0.1);border-radius:22px;padding:30px 28px">
          <div style="font-size:22px;font-weight:600;letter-spacing:-0.025em;margin-bottom:12px;color:#1B45F2">{title}</div>
          <p style="margin:0 0 16px;font-size:15.5px;line-height:1.6;color:#3A3642">{text}</p>
          <p style="margin:0;font-size:13.5px;line-height:1.5;color:#585463">{refs}</p>
        </div>'''


def info(dt, dd):
    return f'<div style="flex:1 1 300px;background:#F3F0E9;padding:24px 22px"><dt style="font-size:14px;font-weight:600;color:#1B45F2;margin-bottom:8px">{dt}</dt><dd style="margin:0;font-size:15.5px;line-height:1.55">{dd}</dd></div>'


def chiffre(n, t):
    return f'''<div style="background:#F3F0E9;padding:30px 28px;display:flex;gap:20px;align-items:baseline;flex-wrap:wrap">
          <div style="font-size:clamp(44px,5vw,64px);font-weight:700;letter-spacing:-0.04em;line-height:1;color:#1B45F2;font-variant-numeric:tabular-nums">{n}</div>
          <div style="flex:1 1 180px;font-size:15.5px;line-height:1.5;color:#3A3642">{t}</div>
        </div>'''


PILL2 = 'background:#F3F0E9;border:1px solid rgba(11,13,24,0.12);border-radius:99px;padding:9px 16px;font-size:14.5px;font-weight:600'
ATOUTS = "".join([
    atout("Une approche hybride", 'Des ateliers mêlant un apprentissage sans écran<span aria-hidden="true">*</span> et une application concrète de leurs connaissances.'),
    atout("Équitable", "Un atelier qui n’exclut personne tout en renforçant les compétences de tous."),
    atout("Souverain et sobre", "Une solution française, une production responsable et innovante."),
    atout("Co-éducation", "À la fin de chaque atelier, nous remettons à chaque élève un éventail mémo. Il prolonge l’atelier à la maison, auprès des familles."),
]).replace(' data-reveal=""', '')

BODY = f'''<div style="background:#F3F0E9;min-height:100svh;overflow-x:hidden">
{nav("colleges.html")}

  <header id="top" style="position:relative;background:#0b1a6e radial-gradient(130% 120% at 28% 38%, #1B45F2 0%, #1236b8 42%, #0b1a6e 78%, #070F38 100%);color:#F3F0E9;overflow:hidden;min-height:clamp(580px,43vw,620px)">
    <div style="position:absolute;inset:0;background:linear-gradient(to bottom, rgba(5,6,12,0.3) 0%, rgba(5,6,12,0.34) 50%, rgba(5,6,12,0.72) 100%)"></div>
    <div style="position:relative;max-width:1140px;margin:0 auto;padding:clamp(112px,12vw,152px) 24px clamp(56px,6vw,88px)">
      <h1 style="margin:0 0 30px;display:flex;flex-wrap:wrap;align-items:baseline;gap:0 0.28em;font-weight:400;font-size:clamp(46px,8vw,120px);line-height:0.9">
        <span translate="no" aria-label="CharabIA" style="display:inline-flex;align-items:baseline;font-family:'Archivo Black',system-ui,sans-serif;letter-spacing:-0.02em;text-shadow:0.03em 0.04em 0 #93A9F7"><span>C</span><span style="font-size:0.6em">H</span><span style="font-size:0.55em">A</span><span style="font-size:0.55em">R</span><span style="font-size:0.55em">A</span><span style="font-size:0.55em">B</span><span style="font-size:1.06em;color:#5C86FF">i</span><span style="color:#5C86FF">A</span></span>
        <span style="font-family:'Instrument Sans',system-ui,sans-serif;font-weight:600;font-size:0.62em;letter-spacing:-0.045em;color:rgba(243,240,233,0.92)">Collèges</span>
      </h1>
      <p style="margin:0 0 18px;font-size:clamp(21px,2.4vw,31px);line-height:1.3;font-weight:500;letter-spacing:-0.022em;text-wrap:pretty">Nous formons les collégiens à l’intelligence artificielle.</p>
      <p style="margin:0 0 30px;font-size:16.5px;line-height:1.62;color:rgba(243,240,233,0.78)">En deux heures, dans votre établissement, vos élèves découvrent ce que l’IA sait vraiment faire. Ils la manipulent en équipe autour d’un plateau de jeu mêlant énigmes et défis et repartent avec les bases d’un usage éclairé, sécurisé et critique de l’IA.</p>
      <a href="#ateliers" style="display:inline-flex;background:#F3F0E9;color:#0B0D18;font-size:15.5px;font-weight:600;padding:14px 26px;border-radius:99px;transition:background 0.22s ease,color 0.22s ease" style-hover="background:#1B45F2;color:#F3F0E9">Découvrir les ateliers</a>
    </div>
  </header>

  <section style="background:#EAE6DC;padding:clamp(64px,7vw,112px) 24px">
    <div style="max-width:1140px;margin:0 auto">
      <p style="margin:0 0 40px;font-size:17px;font-weight:600;color:#1B45F2">Pourquoi des ateliers Collèges</p>
      <p style="margin:0;font-size:clamp(30px,4.4vw,64px);line-height:1.08;letter-spacing:-0.035em;font-weight:600;text-wrap:pretty">Nous agissons pour que l’intelligence artificielle ne creuse pas davantage les inégalités entre les élèves.</p>
    </div>
  </section>


  <section id="solution" style="background:#F3F0E9;padding:clamp(56px,6vw,88px) 24px">
    <div style="max-width:1140px;margin:0 auto">
      <div style="margin-bottom:44px">
        <p style="margin:0 0 28px;font-size:17px;font-weight:600;color:#1B45F2">Notre solution</p>
        <h2 style="margin:0;font-size:clamp(30px,4.4vw,64px);line-height:1.06;letter-spacing:-0.04em;font-weight:600;text-wrap:pretty">CharabIA démystifie l’IA et donne aux élèves les clés pour la comprendre, l’utiliser et en tirer parti.</h2>
      </div>
      <a href="#ateliers" aria-label="Collèges : voir les deux ateliers disponibles" style="position:relative;overflow:hidden;display:flex;flex-direction:column;min-height:340px;color:#F3F0E9;background:#0B0D18 radial-gradient(120% 120% at 80% 20%, #1B45F2 0%, #0b1a6e 45%, #0B0D18 85%);border:1px solid rgba(11,13,24,0.12);border-radius:22px;padding:clamp(28px,4vw,48px);transition:transform 0.4s cubic-bezier(0.2,0.8,0.2,1),border-color 0.3s ease" style-hover="transform:translateY(-6px);border-color:#1B45F2">
        <div style="position:relative;margin-top:auto;display:flex;flex-wrap:wrap;gap:28px 48px;align-items:flex-end;justify-content:space-between;color:#F3F0E9">
          <div style="flex:1 1 360px;min-width:0">
            <div style="font-size:clamp(34px,4.4vw,64px);font-weight:600;letter-spacing:-0.04em;line-height:1.02;margin-bottom:14px;text-wrap:pretty">Collèges</div>
            <div style="font-size:17px;line-height:1.55;color:rgba(243,240,233,0.88)">Comprendre l’IA pour mieux grandir avec elle.</div>
          </div>
          <div style="flex:0 1 340px;min-width:0;display:flex;flex-direction:column;gap:10px">
            <div style="font-size:14px;font-weight:600;color:rgba(243,240,233,0.8)">Deux ateliers disponibles</div>
            <div style="display:flex;flex-wrap:wrap;gap:8px">
              <span style="background:rgba(243,240,233,0.14);border:1px solid rgba(243,240,233,0.42);border-radius:99px;padding:10px 18px;font-size:16px;font-weight:600;backdrop-filter:blur(10px)">Koh Lant<span style="color:#A9BEFF">IA</span></span>
              <span style="background:rgba(243,240,233,0.14);border:1px solid rgba(243,240,233,0.42);border-radius:99px;padding:10px 18px;font-size:16px;font-weight:600;backdrop-filter:blur(10px)">Spat<span style="color:#A9BEFF">IA</span>l</span>
            </div>
            <div style="margin-top:8px;font-size:15.5px;font-weight:600;color:#F3F0E9;text-decoration:underline;text-underline-offset:4px">Voir les ateliers</div>
          </div>
        </div>
      </a>
      <h3 style="margin:56px 0 18px;font-size:clamp(24px,2.6vw,34px);line-height:1.1;letter-spacing:-0.03em;font-weight:600">Un dispositif, quatre atouts</h3>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:1px;background:rgba(11,13,24,0.14);border:1px solid rgba(11,13,24,0.14);border-radius:22px;overflow:hidden">
        {ATOUTS}
      </div>
      <p style="margin:14px 0 0;font-size:13px;line-height:1.55;color:#6b6676">* Certains jeux peuvent faire appel à un écran. Ce n’est pas le cœur de l’atelier&nbsp;: c’est une application concrète des connaissances des élèves.</p>
    </div>
  </section>

  <section id="ateliers" style="background:#F3F0E9;border-top:1px solid rgba(11,13,24,0.08);padding:clamp(56px,6vw,88px) 24px">
    <div style="max-width:1140px;margin:0 auto">
      <h2 style="margin:0 0 18px;font-size:clamp(40px,6vw,88px);line-height:0.96;letter-spacing:-0.05em;font-weight:700">Ateliers Collèges</h2>
      <p style="margin:0 0 30px;font-size:clamp(20px,2.4vw,32px);line-height:1.35;letter-spacing:-0.02em;color:#3A3642;text-wrap:pretty">Découvrez deux de nos ateliers Collèges. Chaque atelier se joue en équipe pendant deux heures, autour d’un plateau de jeu.</p>
      <div style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:34px">
        <span style="{PILL}">2&nbsp;h par atelier</span>
        <span style="{PILL}">15 élèves par atelier</span>
        <span style="{PILL}">BoxIA réutilisable</span>
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:10px">
        <a href="#kohlantia" style="background:#0B0D18;color:#F3F0E9;font-size:15.5px;font-weight:600;padding:14px 26px;border-radius:99px;transition:background 0.22s ease" style-hover="background:#1B45F2;color:#F3F0E9">Koh LantIA</a>
        <a href="#spatial" style="background:transparent;color:#0B0D18;border:1px solid rgba(11,13,24,0.3);font-size:15.5px;font-weight:600;padding:13px 26px;border-radius:99px;transition:border-color 0.22s ease,color 0.22s ease" style-hover="border-color:#1B45F2;color:#1B45F2">SpatIAl</a>
      </div>
    </div>
  </section>

  <section id="kohlantia" style="background:#EAE6DC;border-top:1px solid rgba(11,13,24,0.08);padding:clamp(56px,7vw,104px) 24px">
    <div style="max-width:1140px;margin:0 auto;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,380px),1fr));gap:clamp(36px,6vw,80px);align-items:center">
      <div class="kl-boxcol" style="display:flex;justify-content:center;min-width:0">
        {box("kl", "Koh LantIA", "background:#0B0D18")}
      </div>
      <div>
        <div style="font-size:15px;font-weight:600;color:#1B45F2;margin-bottom:12px">Le Grimoire des secrets codés</div>
        <h2 style="margin:0 0 18px;font-size:clamp(40px,5.4vw,76px);line-height:0.98;letter-spacing:-0.045em;font-weight:700">Koh Lant<span style="color:#1B45F2">IA</span></h2>
        <p style="margin:0 0 30px;font-size:18px;line-height:1.6;color:#3A3642">Durant 2&nbsp;heures, vos élèves se transforment en de véritables aventuriers de l’île de Koh&nbsp;LantIA. Ils doivent déjouer les pièges qui leur sont tendus et réussir chacune des épreuves.</p>
        <ul style="list-style:none;margin:0 0 32px;padding:0;display:grid;gap:1px;background:rgba(11,13,24,0.12);border:1px solid rgba(11,13,24,0.12);border-radius:18px;overflow:hidden">
          {epreuves(KL, False)}
        </ul>
        <a href="contact.html?atelier=kohlantia" style="display:inline-flex;background:#0B0D18;color:#F3F0E9;font-size:15.5px;font-weight:600;padding:14px 28px;border-radius:99px;transition:background 0.22s ease" style-hover="background:#1B45F2;color:#F3F0E9">Organiser cet atelier</a>
      </div>
    </div>
  </section>

  <section id="spatial" style="background:#0B0D18;color:#F3F0E9;padding:clamp(56px,7vw,104px) 24px">
    <div style="max-width:1140px;margin:0 auto;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,380px),1fr));gap:clamp(36px,6vw,80px);align-items:center">
      <div>
        <div style="font-size:15px;font-weight:600;color:#5C86FF;margin-bottom:12px">Bienvenue dans l’univers Spat<span style="color:#5C86FF">IA</span>l</div>
        <h2 style="margin:0 0 18px;font-size:clamp(40px,5.4vw,76px);line-height:0.98;letter-spacing:-0.045em;font-weight:700">Spat<span style="color:#5C86FF">IA</span>l</h2>
        <p style="margin:0 0 30px;font-size:18px;line-height:1.6;color:rgba(243,240,233,0.78)">Une tempête a corrompu VEGA, l’intelligence artificielle de la station. Les élèves la remettent en état, jeu après jeu.</p>
        <ul style="list-style:none;margin:0 0 32px;padding:0;display:grid;gap:1px;background:rgba(243,240,233,0.16);border:1px solid rgba(243,240,233,0.16);border-radius:18px;overflow:hidden">
          {epreuves(SP, True)}
        </ul>
        <a href="contact.html?atelier=spatial" style="display:inline-flex;background:#F3F0E9;color:#0B0D18;font-size:15.5px;font-weight:600;padding:14px 28px;border-radius:99px;transition:background 0.22s ease,color 0.22s ease" style-hover="background:#1B45F2;color:#F3F0E9">Organiser cet atelier</a>
      </div>
      <div style="display:flex;justify-content:center;min-width:0">
        {box("sp", "SpatIAl", "background:#F3F0E9;color:#0B0D18")}
      </div>
    </div>
  </section>

  <section style="background:#F3F0E9;padding:clamp(64px,7vw,110px) 24px">
    <div style="max-width:1140px;margin:0 auto">
      <h2 style="margin:0 0 14px;font-size:clamp(30px,4.2vw,58px);line-height:1.03;letter-spacing:-0.04em;font-weight:600;text-wrap:pretty">Comprendre l’IA sans écran<span aria-hidden="true">*</span>, consolider les fondamentaux</h2>
      <p style="margin:0 0 40px;font-size:18px;line-height:1.6;color:#585463">Trois fondamentaux travaillés en équipe, jeu après jeu.</p>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,280px),1fr));gap:14px;margin-bottom:14px">
        {fondamental("Français&nbsp;: écrire avec rigueur", "Orthographe, syntaxe et mots justes deviennent nécessaires pour piloter l’IA&nbsp;: l’élève affine son prompt jusqu’à obtenir une image fidèle.", "Québec&nbsp;: Communiquer · Produire du contenu<br>Pix IA&nbsp;: 2.2 Utiliser une IA générative")}
        {fondamental("Mathématiques&nbsp;: raisonner et arbitrer", "L’énigme mathématique oblige à choisir&nbsp;: quand s’appuyer sur l’IA, quand réfléchir soi-même&nbsp;? Entraide, écoute et décision collective.", "Québec&nbsp;: Résoudre une variété de problèmes · Collaborer")}
        {fondamental("Esprit critique&nbsp;: vérifier, débattre, respecter autrui", "Repérer erreurs, hallucinations et stéréotypes, puis argumenter en équipe&nbsp;: les biais des données deviennent visibles et discutables.", "Québec&nbsp;: Pensée critique · Culture informationnelle<br>Pix IA&nbsp;: 2.2 · 3.5 Expliquer les enjeux culturels et sociaux")}
      </div>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:1px;background:rgba(11,13,24,0.14);border:1px solid rgba(11,13,24,0.14);border-radius:22px;overflow:hidden">
        {chiffre("12/12", "dimensions du Cadre de référence de la compétence numérique du Québec mobilisées")}
        {chiffre("33/41", "compétences Pix IA de niveaux Novice et Indépendant couvertes ou amorcées par l’ensemble des ateliers CharabIA")}
      </div>
      <p style="margin:18px 0 0;font-size:13px;line-height:1.55;color:#6b6676">* Certains jeux peuvent faire appel à un écran. Ce n’est pas le cœur de l’atelier&nbsp;: c’est une application concrète des connaissances des élèves.</p>
      <p style="margin:8px 0 0;font-size:13px;line-height:1.55;color:#6b6676">Sources&nbsp;: Cadre de référence de la compétence numérique, gouvernement du Québec, 2026. Référentiel « Les compétences numériques en intelligence artificielle », Pix, version 2.0, mai 2026.</p>
    </div>
  </section>

  <section style="background:#EAE6DC;border-top:1px solid rgba(11,13,24,0.08);padding:clamp(56px,6vw,88px) 24px">
    <div style="max-width:1140px;margin:0 auto">
      <h2 style="margin:0 0 32px;font-size:clamp(30px,4.2vw,58px);line-height:1.03;letter-spacing:-0.04em;font-weight:600">Infos pratiques</h2>
      <dl style="margin:0;display:flex;flex-wrap:wrap;gap:1px;background:rgba(11,13,24,0.12);border:1px solid rgba(11,13,24,0.12);border-radius:22px;overflow:hidden">
        {info("Niveau", "Collège&nbsp;: 6e et 5e pour ces deux ateliers.")}
        {info("Format", "2&nbsp;heures par atelier, 15 élèves par groupe, dans votre établissement.")}
        {info("Matériel", "La BoxIA est fournie et réutilisable.")}
        {info("Tarif", "Sur devis.")}
        {info("Zone d’intervention", "Toute la France, y compris les départements, régions et collectivités d’outre-mer, ainsi que les pays limitrophes.")}
        {info("Après l’atelier", "Nous fournissons aussi des contenus pour nourrir les échanges en classe et informer les professeurs. Le travail se poursuit ainsi au-delà des deux heures d’escape game.")}
      </dl>
    </div>
  </section>

  <section style="background:#0B0D18;color:#F3F0E9;padding:clamp(64px,7vw,104px) 24px">
    <div style="max-width:1140px;margin:0 auto;display:flex;flex-direction:column;gap:28px">
      <h2 style="margin:0;font-size:clamp(32px,4.6vw,64px);line-height:1;letter-spacing:-0.045em;font-weight:600;text-wrap:pretty">Organiser un atelier dans votre établissement</h2>
      <div>
        <p style="margin:0 0 22px;font-size:17px;line-height:1.6;color:rgba(243,240,233,0.75)">Vous souhaitez organiser un atelier CharabIA dans votre établissement&nbsp;? Écrivez-nous à <a href="mailto:contact.charabia@gmail.com" style="color:#F3F0E9;font-weight:600">contact.charabia@gmail.com</a>. Nous reviendrons vers vous pour planifier votre atelier.</p>
        <a href="contact.html?objet=atelier" style="display:inline-flex;background:#F3F0E9;color:#0B0D18;font-size:15.5px;font-weight:600;padding:14px 28px;border-radius:99px;transition:background 0.22s ease,color 0.22s ease" style-hover="background:#1B45F2;color:#F3F0E9">Organiser un atelier</a>
      </div>
    </div>
  </section>
{footer("colleges.html")}
</div>'''

FACES = "\n".join(f"  .{p}-{f} {{ background-image: url(/assets/box/{p}-{f}.webp); }}" for p in ("kl", "sp") for f in ("c", "t", "b", "lid", "l", "r"))

CSS = FACES + f"\n  .bx-face {{ {FACE} }}\n  .bx-back {{ {BACK} }}\n  .bx-flap {{ {FLAP} }}" + """
  @keyframes rk-flick { 0%, 100% { scale: 1 1; } 50% { scale: 1 1.45; } }
  .rk-flame { transform-origin: 50% 0; animation: rk-flick 0.16s ease-in-out infinite; }
  @keyframes bx-bob { 0%, 100% { transform: translateX(-50%) translateY(0); } 50% { transform: translateX(-50%) translateY(-7px); } }
  .ch-wood { background: linear-gradient(180deg, rgba(255,255,255,0.07), rgba(0,0,0,0.2)), repeating-linear-gradient(180deg, #9c4b27 0 11px, #6c3217 11px 12.5px); border: 1px solid #45210e; box-shadow: inset 0 0 0 5px #e9cf98, inset 0 0 0 6.5px #a8824c; box-sizing: border-box; backface-visibility: visible; }
  .ch-in { background: linear-gradient(180deg, #3b1c0c, #22100a); box-sizing: border-box; backface-visibility: visible; }
  .ch-strip { position: absolute; left: -62px; top: -8px; width: 124px; height: 16.5px; box-sizing: border-box; backface-visibility: visible; background: linear-gradient(90deg, #e9cf98 0 7px, #a8824c 7px 8.5px, rgba(0,0,0,0) 8.5px calc(100% - 8.5px), #a8824c calc(100% - 8.5px) calc(100% - 7px), #e9cf98 calc(100% - 7px)), linear-gradient(180deg, #a8542c, #8a4322 70%, #6c341a); box-shadow: inset 0 -1px 0 rgba(40,18,6,0.55); }
  .ch-cap { position: absolute; left: -39px; top: -19.5px; width: 78px; height: 39px; box-sizing: border-box; border: 5px solid #e9cf98; border-bottom: none; border-radius: 39px 39px 0 0; background: repeating-linear-gradient(180deg, #8f4423 0 9px, #6c3217 9px 10.5px); backface-visibility: visible; }
  @media (max-width: 820px) { .kl-boxcol { order: 2; } }
"""


def build():
    return page("Ateliers d’initiation à l’IA pour les collèges — CharabIA", "#F3F0E9", BODY, CSS, '<script src="/js/colleges.js"></script>',
                desc="Koh LantIA et SpatIAl : deux escape games de deux heures pour initier les élèves de 6e et de 5e à l’intelligence artificielle.")
