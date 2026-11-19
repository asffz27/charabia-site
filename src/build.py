import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import page_index, page_colleges, page_entreprises, page_autres, page_contact
from common import nav, footer, page

OUT = os.path.join(os.path.dirname(__file__), "..", "dist")
NOT_FOUND = f'''<div style="background:#F3F0E9;min-height:100svh;display:flex;flex-direction:column">
{nav("")}
  <main style="flex:1;padding:clamp(150px,17vw,220px) 24px 96px">
    <div style="max-width:1140px;margin:0 auto">
      <p style="margin:0 0 22px;font-size:17px;font-weight:600;color:#1B45F2">Erreur 404</p>
      <h1 style="margin:0 0 22px;font-size:clamp(44px,7vw,104px);line-height:0.94;letter-spacing:-0.05em;font-weight:700">Ça, c’est du charabia.</h1>
      <p style="margin:0 0 32px;font-size:clamp(18px,2vw,24px);line-height:1.45;color:#3A3642;max-width:46ch">Cette page n’existe pas ou a été déplacée.</p>
      <a href="/" style="display:inline-flex;background:#0B0D18;color:#F3F0E9;font-size:15.5px;font-weight:600;padding:14px 28px;border-radius:99px" style-hover="background:#1B45F2;color:#F3F0E9">Revenir à l’accueil</a>
    </div>
  </main>
{footer("")}
</div>'''

pages = {
    "index.html": page_index.build(),
    "colleges.html": page_colleges.build(),
    "entreprises.html": page_entreprises.build(),
    "histoire.html": page_autres.build_histoire(),
    "actualites.html": page_autres.build_actualites(),
    "contact.html": page_contact.build(),
    "mentions-legales.html": page_autres.build_mentions(),
    "404.html": page("Page introuvable — CharabIA", "#F3F0E9", NOT_FOUND),
}
for name, html in pages.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"{name}: {len(html)//1024} Ko")
