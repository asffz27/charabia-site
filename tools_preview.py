"""Copie dist/ vers preview/ avec des liens relatifs (.html) pour l'aperçu artifact."""
import re, shutil, pathlib
src, dst = pathlib.Path('dist'), pathlib.Path('preview')
shutil.rmtree(dst, ignore_errors=True); shutil.copytree(src, dst)
(dst / '404.html').unlink(missing_ok=True)
pages = r'(colleges|entreprises|histoire|actualites|contact|mentions-legales)'
def fix(s):
    s = s.replace('href="/"', 'href="index.html"').replace('href="/#', 'href="index.html#')
    s = re.sub(r'(["\'])/' + pages + r'(?=[?#"\'])', r'\1\2.html', s)
    s = re.sub(r'(src="|href="|url\()/(assets|js|favicon)', r'\1\2', s)
    return s
for f in list(dst.glob('*.html')) + list(dst.glob('js/*.js')):
    f.write_text(fix(f.read_text()))
