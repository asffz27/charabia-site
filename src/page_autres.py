from common import nav, footer, page, TEAM, partners_grid

H1 = "margin:0 0 20px;font-size:clamp(40px,6vw,80px);line-height:1;letter-spacing:-0.035em;font-weight:600"
LEAD = "margin:0;font-size:clamp(19px,2vw,26px);line-height:1.4;letter-spacing:-0.015em;color:#3A3642;text-wrap:pretty"

# ---------------- Histoire ----------------
STEPS = [
    ("01", "Le point de départ", "Une interrogation", "Au sein de l’Incubateur des politiques publiques de Sciences Po, l’équipe s’est penchée, avec le think tank Renaissance Numérique, sur l’arrivée de l’IA générative chez les plus jeunes. Une question s’est vite imposée : comment éviter que cette technologie ne creuse les inégalités entre les élèves ?"),
    ("02", "Une réponse", "Un escape game pédagogique", "Plutôt qu’un cours, un jeu : un plateau qui transforme la salle de classe en terrain d’aventure. Les élèves manipulent des cartes, ouvrent des coffres et résolvent des énigmes en équipe."),
    ("03", "Une structure", "Une équipe, puis une association", "Le projet s’est structuré en association loi 1901, avec l’ambition de déployer les ateliers dans les établissements scolaires."),
    ("04", "Février 2026", "Le premier atelier officiel", "Au Foyer Saint-Rémi de Reims, huit élèves de 6e se sont pris au jeu pendant deux heures et sont parvenus à résoudre l’escape game&nbsp;!"),
    ("05", "Aujourd’hui", "Des ateliers qui se multiplient", "Depuis ce premier atelier, les interventions se multiplient. Avec Koh LantIA et SpatIAl, de plus en plus d’élèves découvrent l’IA en jouant et repartent avec les clés pour s’en servir avec esprit critique."),
]


def steps():
    out = ""
    for num, when, title, text in STEPS:
        out += f'''<li style="display:flex;flex-wrap:wrap;gap:12px clamp(24px,5vw,72px);padding:clamp(24px,3vw,32px) 0;border-bottom:1px solid rgba(11,13,24,0.14)">
            <div style="flex:0 0 220px;display:flex;align-items:baseline;gap:16px">
              <span style="font-size:15px;font-weight:600;color:#1B45F2;font-variant-numeric:tabular-nums">{num}</span>
              <span style="font-size:15px;font-weight:600;color:#585463">{when}</span>
            </div>
            <div style="flex:1 1 420px;min-width:0">
              <h3 style="margin:0 0 10px;font-size:clamp(21px,2.2vw,28px);line-height:1.15;letter-spacing:-0.025em;font-weight:600;text-wrap:pretty">{title}</h3>
              <p style="margin:0;font-size:16.5px;line-height:1.65;color:#3A3642">{text}</p>
            </div>
          </li>
          '''
    return out


def team():
    out = ""
    for name, role, photo, url in TEAM:
        out += f'''<a href="{url}" target="_blank" rel="noopener" aria-label="Profil LinkedIn de {name}" style="display:block;color:inherit;background:#EAE6DC;border:1px solid rgba(11,13,24,0.1);border-radius:18px;overflow:hidden;transition:border-color 0.3s ease,transform 0.3s ease" style-hover="border-color:#1B45F2;transform:translateY(-4px);color:#0B0D18">
            <div style="aspect-ratio:3/4;background:#0B0D18;overflow:hidden"><img src="{photo}" alt="Portrait de {name}" loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block"></div>
            <div style="padding:16px 18px 18px;background:#F3F0E9"><div style="font-size:13px;font-weight:600;color:#1B45F2;margin-bottom:5px">{role}</div><div style="font-size:17px;font-weight:600;letter-spacing:-0.02em">{name}</div></div>
          </a>
          '''
    return out


HISTOIRE = f'''<div style="background:#F3F0E9;min-height:100svh;overflow-x:hidden">
{nav("histoire.html")}

  <header style="background:#F3F0E9">
    <div style="max-width:1140px;margin:0 auto;padding:clamp(112px,12vw,152px) 24px clamp(32px,4vw,48px)">
      <h1 style="margin:0 0 20px;font-size:clamp(40px,6vw,80px);line-height:1;letter-spacing:-0.035em;font-weight:600">L’histoire de l’association</h1>
      <p style="margin:0;font-size:clamp(19px,2vw,26px);line-height:1.4;font-weight:500;letter-spacing:-0.015em;color:#3A3642;text-wrap:pretty">CharabIA est née d’une inquiétude&nbsp;: voir l’intelligence artificielle creuser davantage les inégalités entre les élèves.</p>
    </div>
  </header>

  <section style="background:#0B0D18;color:#F3F0E9;padding:clamp(48px,5vw,72px) 24px">
    <div style="max-width:1140px;margin:0 auto">
      <p style="margin:0 0 20px;font-size:15px;font-weight:600;color:#5C86FF">La question de départ</p>
      <blockquote style="margin:0;font-size:clamp(26px,3.4vw,48px);line-height:1.14;letter-spacing:-0.03em;font-weight:600;text-wrap:pretty">«&nbsp;Comment former et informer les plus jeunes, afin de s’assurer que le déploiement des technologies d’intelligence artificielle ne renforce pas les inégalités existantes&nbsp;?&nbsp;»</blockquote>
      <p style="margin:20px 0 0;font-size:16px;line-height:1.6;color:rgba(243,240,233,0.72)">Posée avec le think tank Renaissance Numérique, au sein de l’Incubateur des politiques publiques de Sciences Po.</p>
    </div>
  </section>

  <section style="background:#EAE6DC;border-top:1px solid rgba(11,13,24,0.08);padding:clamp(40px,4vw,56px) 24px">
    <div style="max-width:1140px;margin:0 auto">
      <p style="margin:0 0 24px;font-size:15px;font-weight:600;color:#1B45F2">Ils nous ont accompagnés</p>
      {partners_grid()}
    </div>
  </section>

  <section style="padding:clamp(56px,6vw,88px) 24px">
    <div style="max-width:1140px;margin:0 auto">
      <h2 style="margin:0 0 32px;font-size:clamp(30px,4.2vw,56px);line-height:1.04;letter-spacing:-0.035em;font-weight:600">Les grandes étapes</h2>
      <ol style="list-style:none;margin:0;padding:0;display:grid;gap:0;border-top:1px solid rgba(11,13,24,0.14)">
          {steps()}
      </ol>
    </div>
  </section>

  <section id="equipe" style="background:#EAE6DC;border-top:1px solid rgba(11,13,24,0.08);padding:clamp(56px,6vw,88px) 24px">
    <div style="max-width:1140px;margin:0 auto">
      <h2 style="margin:0 0 12px;font-size:clamp(30px,4.2vw,56px);line-height:1.04;letter-spacing:-0.035em;font-weight:600;text-align:center">L’équipe</h2>
      <p style="margin:0 0 32px;font-size:17px;line-height:1.6;color:#585463;text-align:center">Les fondateurs de CharabIA. Cliquez sur un portrait pour retrouver son profil LinkedIn.</p>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),280px));justify-content:center;gap:clamp(10px,2vw,16px)">
          {team()}
      </div>
    </div>
  </section>
{footer("histoire.html")}
</div>'''

# ---------------- Actualités ----------------
ARTICLES = [
    ("college-agiot", "Atelier", "16-17 novembre 2026", "Dix ateliers Koh LantIA au collège de l’Agiot (La Verrière)",
     ["Les 16 et 17 novembre derniers, CharabIA a formé près de 150 élèves de 6e aux enjeux de l’IA grâce à son escape game pédagogique Koh LantIA. Les étudiants du programme PEPPS étaient présents pour recueillir leurs premières données de terrain.",
      "Un grand merci au collège de l’Agiot ainsi qu’aux enseignantes de mathématiques qui ont rendu cette intervention possible&nbsp;!"], ""),
    ("liepp-pepps", "Partenariat", "Octobre 2026", "CharabIA devient partenaire du LIEPP au sein du programme PEPPS",
     ["Le 3 octobre a marqué le lancement officiel du partenariat entre le programme PEPPS du LIEPP (Sciences Po) et l’association CharabIA.",
      "À cette occasion, Alice et Alexis ont rencontré les cinq étudiants chargés de mener, dans les prochains mois, une mesure d’impact de nos ateliers en collège. Ils travaillent sous la supervision de leur tutrice, chercheuse postdoctorale en sociologie au médialab."], ""),
    ("bois-colombes-ecole-42", "Événement", "Septembre 2026", "Les jeux CharabIA à Bois-Colombes et à l’École 42 avec Magic Makers et SOS Tech",
     ["CharabIA a eu le plaisir de présenter ses ressources éducatives lors de la journée «&nbsp;Jeunesse en fête&nbsp;» à Bois-Colombes et lors de la journée du Grand Challenge IA à l’École 42. Lors de ces deux journées, les élèves ont pu découvrir l’IA d’une autre manière&nbsp;: sans écran, en équipe, tout en renforçant leurs savoirs fondamentaux.",
      "Ces nouvelles expériences de terrain nous confirment à nouveau que le sans écran est possible pour initier les plus jeunes aux enjeux d’IA et pour les orienter vers des pratiques raisonnées. Un immense merci à Magic Makers et à SOS Tech pour leur invitation et leur confiance&nbsp;!"], ""),
    ("renaissance-numerique", "Publication", "11 février 2026", "Renaissance Numérique soutient le lancement de CharabIA",
     ["Le think tank Renaissance Numérique consacre un entretien au lancement de CharabIA. On y raconte ce qu'est un atelier : un plateau de jeu qui transforme la salle de classe en terrain d'aventure, où les élèves manipulent des cartes, ouvrent des coffres, résolvent des énigmes et interrogent l'IA pour progresser dans l'histoire — de l'exploration spatiale avec SpatIAl à la survie avec Koh\u00a0LantIA.",
      "Chaque élève repart avec un fascicule pour prolonger la découverte à la maison et un diplôme de « jeune explorateur de l'IA ». L'entretien revient aussi sur la genèse du projet à l'Incubateur des politiques publiques de Sciences Po et sur le choix de l'entrée en 6e, ce moment charnière où les écarts se creusent."],
     "https://www.renaissancenumerique.org/actualites/renaissance-numerique-soutient-le-lancement-de-charabia/"),
    ("foyer-saint-remi", "Atelier", "Février 2026", "Premier atelier officiel au Foyer Saint-Rémi de Reims",
     ["Le Foyer Saint-Rémi de Reims a fait confiance à CharabIA pour l'organisation de notre premier atelier officiel, avec des élèves de 6e. Au programme : huit enfants, deux heures, un escape game — suivi du début à la fin, sans aucun abandon. L'énigme mathématique, celle que nous redoutions le plus, est devenue le moment fort de l'atelier : ensemble, ils ont posé les calculs, débattu, corrigé, avancé, sans jamais dire « on fait des maths ». C'est l'étape où l'intelligence collective s'est le plus exprimée.",
      "Chaque étape du parcours leur a permis de comprendre l'origine et le fonctionnement de l'IA générative, de manipuler la notion de prompt et d'expérimenter les conséquences d'une formulation imprécise, et surtout de comprendre que l'IA n'est pas neutre. La génération d'images à partir d'une histoire lue à voix haute l'a confirmé : les biais de l'IA ne sont pas intuitivement compris par les enfants. C'est précisément pour cela que cibler les élèves de 6e est stratégique — ils utilisent déjà ces outils, sans toujours en mesurer les enjeux. Merci au Foyer Saint-Rémi de Reims pour sa confiance."], ""),
]

def articles():
    out = ""
    for aid, tag, date, title, paras, href in ARTICLES:
        link = f'<p style="margin:18px 0 0"><a href="{href}" target="_blank" rel="noopener" style="font-size:15px;font-weight:600">Lire l\'article sur renaissancenumerique.org</a></p>' if href else ""
        out += f'''<article id="{aid}" style="background:#EAE6DC;border:1px solid rgba(11,13,24,0.1);border-radius:24px;padding:clamp(28px,4vw,48px)">
          <div style="display:flex;flex-wrap:wrap;gap:8px 18px;align-items:baseline;margin-bottom:18px">
            <span style="font-size:14px;font-weight:600;color:#1B45F2">{tag}</span>
            <span style="font-size:14px;color:#585463;font-variant-numeric:tabular-nums">{date}</span>
          </div>
          <h2 style="margin:0 0 16px;font-size:clamp(26px,3.2vw,44px);line-height:1.06;letter-spacing:-0.035em;font-weight:600;text-wrap:pretty">{title}</h2>
          {"".join(f'<p style="margin:{"0" if i == len(paras) - 1 else "0 0 14px"};font-size:16.5px;line-height:1.65;color:#3A3642">{x}</p>' for i, x in enumerate(paras))}
          {link}
        </article>
        '''
    return out


ACTUS = f'''<div style="background:#F3F0E9;min-height:100svh;overflow-x:hidden">
{nav("actualites.html")}

  <header style="padding:clamp(112px,12vw,152px) 24px clamp(40px,5vw,64px)">
    <div style="max-width:1140px;margin:0 auto">
      <h1 style="{H1}">Actualités</h1>
      <p style="{LEAD}">Ce que nous faisons, où nous intervenons, et ce qui s'écrit avec nous.</p>
    </div>
  </header>

  <main style="padding:0 24px clamp(90px,11vw,160px)">
    <div style="max-width:1140px;margin:0 auto;display:grid;gap:16px">
        {articles()}
    </div>
  </main>

  <section id="linkedin" aria-labelledby="li-title" style="background:#0B0D18;color:#F3F0E9;padding:clamp(64px,7vw,104px) 24px">
    <div style="max-width:1140px;margin:0 auto">
      <div style="display:flex;flex-wrap:wrap;gap:24px 32px;align-items:flex-end;justify-content:space-between">
        <div style="flex:1 1 420px;min-width:0">
          <p style="margin:0 0 16px;font-size:15px;font-weight:600;color:#5C86FF">Sur LinkedIn</p>
          <h2 id="li-title" style="margin:0 0 14px;font-size:clamp(30px,4.2vw,58px);line-height:1.03;letter-spacing:-0.04em;font-weight:600">Suivez nos actualités</h2>
          <p style="margin:0;font-size:16.5px;line-height:1.6;color:rgba(243,240,233,0.72)">Nos derniers ateliers, nos rencontres et les coulisses du projet sont publiés sur la page LinkedIn de CharabIA.</p>
        </div>
        <a href="https://www.linkedin.com/company/charab-ia/" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;gap:10px;min-height:52px;box-sizing:border-box;background:#F3F0E9;color:#0B0D18;font-size:16px;font-weight:600;padding:14px 28px;border-radius:99px;transition:background 0.22s ease,color 0.22s ease" style-hover="background:#1B45F2;color:#F3F0E9">Voir la page LinkedIn <svg aria-hidden="true" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17L17 7M9 7h8v8"></path></svg></a>
      </div>
    </div>
  </section>
{footer("actualites.html")}
</div>'''

# ---------------- Mentions légales ----------------
LEGAL = [
    ("Éditeur du site", 'CharabIA<br>Association loi 1901<br>Numéro RNA&nbsp;: W751281534<br>Siège social&nbsp;: 114 rue de la Convention 75015 Paris<br>Email&nbsp;: <a href="mailto:contact.charabia@gmail.com">contact.charabia@gmail.com</a><br>Directeur de la publication&nbsp;: Alexis Souffez'),
    ("Hébergement", "Le site CharabIA est hébergé par&nbsp;:<br>Vercel Inc.<br>440 North Barranca Avenue, Suite 4133<br>Covina, CA 91723<br>États-Unis"),
    ("Propriété intellectuelle", "L'ensemble du contenu de ce site (textes, images, vidéos, logos, graphismes) est la propriété exclusive de l'association CharabIA, sauf mention contraire. Toute reproduction, représentation, modification ou exploitation, totale ou partielle, sans autorisation préalable est interdite."),
    ("Protection des données personnelles", 'Les informations collectées via ce site font l\'objet d\'un traitement informatique destiné à répondre aux demandes de contact et d\'information sur nos formations. Les demandes envoyées via le formulaire de contact sont transmises par e-mail et enregistrées dans un tableur, au moyen des services Gmail et Google Sheets (Google). Elles sont conservées au maximum 3 ans après notre dernier échange, puis supprimées. Conformément au Règlement Général sur la Protection des Données (RGPD) et à la loi Informatique et Libertés, vous disposez d\'un droit d\'accès, de rectification, de suppression et d\'opposition aux données vous concernant.<br>Pour exercer ces droits, contactez-nous à&nbsp;: <a href="mailto:contact.charabia@gmail.com">contact.charabia@gmail.com</a>'),
    ("Cookies", "Ce site utilise uniquement des cookies techniques strictement nécessaires à son fonctionnement. Aucun cookie de suivi ou de marketing n'est déposé sans votre consentement préalable."),
    ("Limitation de responsabilité", "CharabIA s'efforce d'assurer l'exactitude et la mise à jour des informations diffusées sur ce site. Toutefois, l'association ne peut garantir l'exactitude, la précision ou l'exhaustivité des informations mises à disposition.<br>L'association ne saurait être tenue responsable des dommages directs ou indirects résultant de l'accès au site ou de l'utilisation de celui-ci."),
    ("Liens hypertextes", "Le site peut contenir des liens vers des sites externes. CharabIA n'exerce aucun contrôle sur ces sites et décline toute responsabilité quant à leur contenu."),
    ("Droit applicable", "Les présentes mentions légales sont soumises au droit français. En cas de litige, les tribunaux français seront seuls compétents."),
]

MENTIONS = f'''<div style="background:#F3F0E9;min-height:100svh">
{nav("mentions-legales.html")}

  <main style="padding:clamp(112px,12vw,152px) 24px clamp(72px,8vw,112px)">
    <div style="max-width:760px;margin:0 auto">
      <h1 style="margin:0 0 56px;font-size:clamp(38px,5.5vw,72px);line-height:0.98;letter-spacing:-0.045em;font-weight:700">Mentions légales</h1>
      <div style="display:grid;gap:44px">
        {"".join(f'<section><h2 style="margin:0 0 14px;font-size:21px;font-weight:600;letter-spacing:-0.02em;color:#1B45F2">{t}</h2><p style="margin:0;font-size:16px;line-height:1.7;color:#3A3642">{x}</p></section>' for t, x in LEGAL)}
      </div>
    </div>
  </main>
{footer("mentions-legales.html")}
</div>'''


def build_histoire():
    return page("Notre histoire : une association née à Sciences Po — CharabIA", "#F3F0E9", HISTOIRE, desc="L’histoire de CharabIA, association née à l’Incubateur des politiques publiques de Sciences Po.")


def build_actualites():
    return page("Actualités : ateliers IA en collège et partenariats — CharabIA", "#F3F0E9", ACTUS, desc="Les dernières actualités de CharabIA : ateliers, publications et événements.")


def build_mentions():
    return page("Mentions légales — CharabIA", "#F3F0E9", MENTIONS)
