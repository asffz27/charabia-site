import re

PAGES = [
    ("index.html", "Accueil"),
    ("colleges.html", "Collèges"),
    ("entreprises.html", "Entreprises"),
    ("histoire.html", "Histoire"),
    ("actualites.html", "Actualités"),
    ("contact.html", "Contact"),
    ("mentions-legales.html", "Mentions légales"),
]


def wordmark(size, color="#F3F0E9", accent="#5C86FF", extra=""):
    return (
        f'<span translate="no" style="display:inline-flex;align-items:baseline;font-family:\'Archivo Black\',system-ui,sans-serif;'
        f'font-size:{size};line-height:0.8;letter-spacing:-0.015em;color:{color};{extra}">'
        '<span>C</span><span style="font-size:0.6em">H</span><span style="font-size:0.55em">A</span>'
        '<span style="font-size:0.55em">R</span><span style="font-size:0.55em">A</span><span style="font-size:0.55em">B</span>'
        f'<span style="font-size:1.06em;color:{accent}">i</span><span style="color:{accent}">A</span></span>'
    )


BASE_CSS = """
  html { scroll-behavior: smooth; }
  body { margin: 0; background: #F3F0E9; color: #0B0D18; font-family: "Instrument Sans", system-ui, sans-serif; -webkit-font-smoothing: antialiased; touch-action: manipulation; -webkit-tap-highlight-color: rgba(27,69,242,0.18); }
  section[id], header[id], footer[id], article[id] { scroll-margin-top: 88px; }
  a { color: #1B45F2; text-decoration: none; }
  a:hover { color: #0B0D18; }
  a:focus-visible, [tabindex]:focus-visible, button:focus-visible { outline: 2px solid #1B45F2; outline-offset: 3px; border-radius: 4px; }
  ::selection { background: #1B45F2; color: #F3F0E9; }
  .partner-tile:hover { border-color: rgba(27,69,242,0.35) !important; }
  .partner-tile:hover img { filter: none !important; opacity: 1 !important; }
  @media (prefers-reduced-motion: reduce) {
    html { scroll-behavior: auto; }
    *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
  }
  @media (max-width: 760px) {
    .nav-cta { display: none !important; }
    .nav-bar { flex-wrap: wrap !important; padding: 10px 14px 6px !important; gap: 6px 8px !important; }
    .nav-links { flex-wrap: nowrap !important; width: 100%; justify-content: flex-start !important; overflow-x: auto; scrollbar-width: none; -webkit-overflow-scrolling: touch; }
    .nav-links::-webkit-scrollbar { display: none; }
    .nav-links a { padding: 7px 11px !important; font-size: 14px !important; white-space: nowrap; flex: 0 0 auto; }
  }
"""

NAV_LINK = 'color:rgba(243,240,233,0.74);font-size:14.5px;padding:8px 14px;border-radius:99px;transition:color 0.2s ease,background 0.2s ease'
NAV_LINK_ON = 'color:#F3F0E9;font-size:14.5px;padding:8px 14px;border-radius:99px;background:rgba(255,255,255,0.12)'
NAV_HOVER = 'color:#F3F0E9;background:rgba(255,255,255,0.09)'
CTA = ('margin-left:8px;backdrop-filter:blur(16px) saturate(170%);-webkit-backdrop-filter:blur(16px) saturate(170%);'
       'box-shadow:inset 0 1px 0 rgba(255,255,255,0.45), inset 0 -8px 16px rgba(255,255,255,0.07), 0 4px 16px rgba(5,6,12,0.25);'
       'color:#F3F0E9;font-size:14.5px;font-weight:600;padding:9px 20px;border-radius:99px;transition:background 0.25s ease,border-color 0.25s ease')


def nav(active):
    home = "#top" if active == "index.html" else "index.html"
    links = ""
    for href, label in [("colleges.html", "Collèges"), ("entreprises.html", "Entreprises"), ("histoire.html", "Histoire"), ("actualites.html", "Actualités")]:
        if href == active:
            links += f'<a href="{href}" aria-current="page" style="{NAV_LINK_ON}">{label}</a>\n      '
        else:
            links += f'<a href="{href}" style="{NAV_LINK}" style-hover="{NAV_HOVER}">{label}</a>\n      '
    if active == "contact.html":
        cta = f'<a class="nav-cta" href="contact.html" aria-current="page" style="{CTA};background:rgba(243,240,233,0.3);border:1px solid rgba(255,255,255,0.65)">Nous contacter</a>'
    else:
        cta = (f'<a class="nav-cta" href="contact.html" style="{CTA};background:rgba(243,240,233,0.12);border:1px solid rgba(255,255,255,0.35)" '
               'style-hover="background:rgba(243,240,233,0.3);border-color:rgba(255,255,255,0.65)">Nous contacter</a>')
    return f'''
  <nav class="nav-bar" style="position:fixed;top:0;left:0;right:0;z-index:50;display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:8px 24px;padding:12px 20px;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);background:rgba(11,13,24,0.62);border-bottom:1px solid rgba(243,240,233,0.1)">
    <a href="{home}" aria-label="CharabIA, retour à l’accueil" style="display:flex;align-items:center;gap:11px;color:#F3F0E9;margin-right:auto">
      {wordmark("22px")}
    </a>
    <div class="nav-links" style="display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:2px 4px">
      {links}{cta}
    </div>
  </nav>'''


def footer_links(active):
    out = ""
    for href, label in PAGES:
        target = "#top" if (href == active == "index.html") else href
        if href == active:
            out += f'<a href="{target}" aria-current="page" style="color:#0B0D18;font-weight:600">{label}</a>\n        '
        else:
            out += f'<a href="{href}" style="color:rgba(11,13,24,0.55)" style-hover="color:#1B45F2">{label}</a>\n        '
    return out


def footer(active):
    return f'''
  <footer style="background:#EAE6DC;border-top:1px solid rgba(11,13,24,0.1);padding:40px 24px">
    <div style="max-width:1140px;margin:0 auto;display:flex;flex-wrap:wrap;gap:20px 24px;align-items:center;justify-content:space-between;font-size:13.5px;color:rgba(11,13,24,0.55)">
      <span>© 2026 – CharabIA</span>
      <div style="display:flex;flex-wrap:wrap;gap:22px">
        {footer_links(active)}
      </div>
    </div>
  </footer>'''


def hover_to_css(html):
    """Convertit les attributs style-hover="..." en classes CSS :hover."""
    rules = []

    def repl(m):
        tag = m.group(0)
        hv = re.search(r'\sstyle-hover="([^"]*)"', tag).group(1)
        idx = len(rules)
        decls = ";".join(d.strip() + " !important" for d in hv.split(";") if d.strip())
        rules.append(f".hv{idx}:hover{{{decls}}}")
        tag = re.sub(r'\sstyle-hover="[^"]*"', "", tag)
        if re.search(r'\sclass="', tag):
            tag = re.sub(r'\sclass="([^"]*)"', lambda c: f' class="{c.group(1)} hv{idx}"', tag, count=1)
        else:
            tag = tag[:-1] + f' class="hv{idx}">' if not tag.endswith("/>") else tag[:-2] + f' class="hv{idx}"/>'
        return tag

    html = re.sub(r'<[a-zA-Z][^<>]*\sstyle-hover="[^"]*"[^<>]*>', repl, html)
    return html, "\n  ".join(rules)


def page(title, theme, body, extra_css="", scripts="", desc="", body_bg="#F3F0E9", head_js=""):
    body, hover_css = hover_to_css(body)
    # liens internes en chemins absolus « propres » (Vercel cleanUrls)
    body = re.sub(r'href="index\.html(#[^"]*)?"', lambda m: f'href="/{m.group(1) or ""}"', body)
    body = re.sub(r'href="([a-z-]+)\.html', r'href="/\1', body)
    body = re.sub(r'(src|url\()="?assets/', lambda m: m.group(0).replace("assets/", "/assets/"), body)
    body = body.replace('src="assets/', 'src="/assets/')
    desc = desc or "CharabIA forme les collégiens et les lycéens à l’intelligence artificielle grâce à des escape games pédagogiques."
    return minify(f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="{theme}">
<meta name="google-site-verification" content="ud0AhfVXFh4JOHHhsf3M71Nomx246Tx-Gst28suZ_NQ">
{head_js}
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo+Black&amp;family=Instrument+Sans:wght@400;500;600;700&amp;display=swap">
<style>{BASE_CSS}  body {{ background: {body_bg}; }}
{extra_css}
  {hover_css}
</style>
</head>
<body>
{body}
{scripts}
</body>
</html>
''')


# Images partagées
TEAM = [
    ("Alice SAURI", "Co-fondatrice", "assets/team-alice.webp", "https://www.linkedin.com/in/alice-sauri-82b727224/"),
    ("Alexis SOUFFEZ", "Co-fondateur", "assets/team-alexis.webp", "https://www.linkedin.com/in/alexissouffez/"),
]
PARTNERS = [
    ("Renaissance Numérique", "assets/logo-renaissance.webp", 76),
    ("CNIL", "assets/logo-cnil.webp", 46),
    ("Ministère de l’Éducation nationale et de la Jeunesse", "assets/logo-ministere.webp", 82),
    ("Réseau Canopé", "assets/logo-canope.webp", 56),
    ("Sciences Po", "assets/logo-sciencespo.webp", 40),
    ("Département de Maine-et-Loire — Anjou", "assets/logo-anjou.webp", 62),
    ("LIEPP — Laboratoire interdisciplinaire d’évaluation des politiques publiques de Sciences Po", "assets/logo-liepp.webp", 60),
]


def partners_grid(reveal=False):
    r = ' data-reveal=""' if reveal else ""
    tiles = ""
    for name, src, h in PARTNERS:
        tiles += (f'<div class="partner-tile" style="background:#EAE6DC;border:1px solid rgba(11,13,24,0.08);border-radius:clamp(12px,1.6vw,16px);transition:border-color 0.3s ease;display:flex;align-items:center;justify-content:center;padding:clamp(10px,2.2vw,22px) clamp(8px,1.8vw,20px);min-height:clamp(64px,9vw,96px)">'
                  f'<img src="{src}" alt="{name}" loading="lazy" style="max-width:100%;max-height:{h}px;width:auto;height:auto;object-fit:contain;filter:grayscale(1);opacity:0.75;transition:filter 0.3s ease,opacity 0.3s ease"></div>\n        ')
    return f'<div{r} style="display:grid;grid-template-columns:repeat(auto-fit,minmax(92px,1fr));gap:clamp(8px,1.4vw,14px);align-items:stretch">\n        {tiles}</div>'


def minify(html):
    # retire l'indentation et les lignes vides (hors <pre>/<textarea>, absents du site)
    lines = [l.strip() for l in html.split("\n")]
    return "\n".join(l for l in lines if l) + "\n"
