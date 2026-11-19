from common import nav, footer, page

# ⚠️ Brouillon : la section Entreprises n'a pas encore de wording validé (document d'Alice, 19/11/2026).
MODULES = [
    ("Module 1", "Escape game : fondamentaux et gouvernance de l’IA",
     "Vos équipes découvrent en jouant ce que l’IA sait vraiment faire, ses limites et ses risques. L’atelier pose les bases d’un usage éclairé, sécurisé et responsable, et ouvre la discussion sur les règles à se donner collectivement."),
    ("Module 2", "Usages avancés des outils d’IA",
     "Des cas concrets tirés de votre métier pour gagner en efficacité avec les assistants d’IA : bien formuler ses demandes, vérifier les réponses, protéger ses données."),
    ("Module 3", "Automatiser avec l’IA",
     "Une prise en main guidée des outils d’automatisation (n8n par exemple) pour construire vos premiers flux de travail et comprendre ce qu’il est utile d’automatiser."),
]


def modules():
    out = ""
    for k, t, x in MODULES:
        out += f'''<div style="background:#F3F0E9;border:1px solid rgba(11,13,24,0.1);border-radius:22px;padding:30px 28px;display:flex;flex-direction:column;gap:12px">
          <div style="font-size:14px;font-weight:600;color:#1B45F2">{k} · 2&nbsp;h</div>
          <div style="font-size:clamp(21px,2vw,26px);font-weight:600;letter-spacing:-0.025em;line-height:1.15">{t}</div>
          <p style="margin:0;font-size:15.5px;line-height:1.6;color:#3A3642">{x}</p>
        </div>
        '''
    return out


def info(dt, dd):
    return f'<div style="flex:1 1 260px;background:#F3F0E9;padding:24px 22px"><dt style="font-size:14px;font-weight:600;color:#1B45F2;margin-bottom:8px">{dt}</dt><dd style="margin:0;font-size:15.5px;line-height:1.55">{dd}</dd></div>'


BODY = f'''<div style="background:#F3F0E9;min-height:100svh;overflow-x:hidden">
{nav("entreprises.html")}

  <header style="position:relative;background:#0B0D18 radial-gradient(120% 120% at 80% 20%, #1B45F2 0%, #0b1a6e 45%, #0B0D18 85%);color:#F3F0E9;overflow:hidden">
    <div style="position:relative;max-width:1140px;margin:0 auto;padding:clamp(112px,12vw,152px) 24px clamp(56px,6vw,88px)">
      <h1 style="margin:0 0 30px;display:flex;flex-wrap:wrap;align-items:baseline;gap:0 0.28em;font-weight:400;font-size:clamp(46px,8vw,120px);line-height:0.9">
        <span translate="no" aria-label="CharabIA" style="display:inline-flex;align-items:baseline;font-family:'Archivo Black',system-ui,sans-serif;letter-spacing:-0.02em;text-shadow:0.03em 0.04em 0 #93A9F7"><span>C</span><span style="font-size:0.6em">H</span><span style="font-size:0.55em">A</span><span style="font-size:0.55em">R</span><span style="font-size:0.55em">A</span><span style="font-size:0.55em">B</span><span style="font-size:1.06em;color:#5C86FF">i</span><span style="color:#5C86FF">A</span></span>
        <span style="font-family:'Instrument Sans',system-ui,sans-serif;font-weight:600;font-size:0.62em;letter-spacing:-0.045em;color:rgba(243,240,233,0.92)">Entreprises</span>
      </h1>
      <p style="margin:0 0 18px;font-size:clamp(21px,2.4vw,31px);line-height:1.3;font-weight:500;letter-spacing:-0.022em;text-wrap:pretty">Nous formons les professionnels à l’intelligence artificielle.</p>
      <p style="margin:0 0 30px;font-size:16.5px;line-height:1.62;color:rgba(243,240,233,0.78);max-width:60ch">Dans vos locaux, nous formons vos équipes aux enjeux d’IA par une approche ludique et centrée sur l’humain. Chaque module dure deux heures et peut se suivre seul ou en parcours.</p>
      <a href="contact.html?profil=entreprise" style="display:inline-flex;background:#F3F0E9;color:#0B0D18;font-size:15.5px;font-weight:600;padding:14px 26px;border-radius:99px;transition:background 0.22s ease,color 0.22s ease" style-hover="background:#1B45F2;color:#F3F0E9">Nous contacter</a>
    </div>
  </header>

  <section style="background:#EAE6DC;padding:clamp(56px,6vw,96px) 24px">
    <div style="max-width:1140px;margin:0 auto">
      <p style="margin:0 0 20px;font-size:17px;font-weight:600;color:#1B45F2">Notre offre</p>
      <h2 style="margin:0 0 40px;font-size:clamp(30px,4.2vw,58px);line-height:1.04;letter-spacing:-0.04em;font-weight:600;text-wrap:pretty">Trois modules pour un usage éclairé et sécurisé de l’IA.</h2>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:14px">
        {modules()}
      </div>
    </div>
  </section>

  <section style="background:#F3F0E9;border-top:1px solid rgba(11,13,24,0.08);padding:clamp(56px,6vw,88px) 24px">
    <div style="max-width:1140px;margin:0 auto">
      <h2 style="margin:0 0 32px;font-size:clamp(30px,4.2vw,58px);line-height:1.03;letter-spacing:-0.04em;font-weight:600">Infos pratiques</h2>
      <dl style="margin:0;display:flex;flex-wrap:wrap;gap:1px;background:rgba(11,13,24,0.12);border:1px solid rgba(11,13,24,0.12);border-radius:22px;overflow:hidden">
        {info("Format", "Modules de 2&nbsp;heures, dans vos locaux.")}
        {info("Sur mesure", "Les cas pratiques sont adaptés à votre secteur et à vos outils.")}
        {info("Tarif", "Sur devis.")}
      </dl>
    </div>
  </section>

  <section style="background:#0B0D18;color:#F3F0E9;padding:clamp(64px,7vw,104px) 24px">
    <div style="max-width:1140px;margin:0 auto;display:flex;flex-direction:column;gap:28px">
      <h2 style="margin:0;font-size:clamp(32px,4.6vw,64px);line-height:1;letter-spacing:-0.045em;font-weight:600;text-wrap:pretty">Former vos équipes à l’IA</h2>
      <div style="max-width:64ch">
        <p style="margin:0 0 22px;font-size:17px;line-height:1.6;color:rgba(243,240,233,0.75)">Vous souhaitez former vos équipes&nbsp;? Écrivez-nous à <a href="mailto:contact.charabia@gmail.com" style="color:#F3F0E9;font-weight:600">contact.charabia@gmail.com</a>. Nous reviendrons vers vous pour construire votre parcours.</p>
        <a href="contact.html?profil=entreprise" style="display:inline-flex;background:#F3F0E9;color:#0B0D18;font-size:15.5px;font-weight:600;padding:14px 28px;border-radius:99px;transition:background 0.22s ease,color 0.22s ease" style-hover="background:#1B45F2;color:#F3F0E9">Nous contacter</a>
      </div>
    </div>
  </section>
{footer("entreprises.html")}
</div>'''


def build():
    return page("Entreprises — CharabIA", "#0B0D18", BODY,
                desc="CharabIA forme les professionnels à l’intelligence artificielle : des modules de deux heures, ludiques et centrés sur l’humain.")
