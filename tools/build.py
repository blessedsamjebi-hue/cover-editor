"""Build the Cover Editor page.

  python3 -I tools/build.py            -> renderer/index.html (desktop app, bundled fonts)
  python3 -I tools/build.py --web OUT  -> one self-contained HTML for a browser (Google Fonts)

Templates live in TEMPLATES below; each one's images are embedded as data URIs
(keeps canvas exports untainted, and the app works offline).
"""
import base64, json, pathlib, subprocess, sys

APP = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP / 'tools'))
from templates import LIBRARY   # ready-made editable templates (no pictures)
SAM = APP.parent

def uri(path, mime):
    return f'data:{mime};base64,' + base64.b64encode(pathlib.Path(path).read_bytes()).decode()

# ---------- template: Verdura Clear Skin Pack – LinkedIn cover (approved 2026-11-03) ----------
VCSP = SAM / 'Social media/LinkedIn/November 2026/Verdura Clear Skin Pack/assets'

def verdura_cover():
    big = VCSP / 'photo-3800.jpg'
    if not big.exists():
        subprocess.run(['sips', '-Z', '3800', '-s', 'formatOptions', '85', str(VCSP / 'photo.jpg'), '--out', str(big)], check=True, capture_output=True)
    svg = (VCSP / 'clear-skin-pack-logo.svg').read_text()
    svg = svg.replace('viewBox="0 0 1612.85 1174">', 'viewBox="0 0 1612.85 1174" width="1612.85" height="1174">', 1)
    assets = {
        'vcsp-photo': uri(big, 'image/jpeg'),
        'vcsp-pack': uri(VCSP / 'pack.png', 'image/png'),
        'vcsp-logo': 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode()).decode(),
    }
    NAVY, RED, INK, BLUSH = '#1f2a44', '#d23f4a', '#33394a', '#fdf3f2'

    def text(id, name, x, y, t, **k):
        e = dict(id=id, name=name, type='text', x=x, y=y, text=t, family='Jost', weight=500, size=30, lh=1.2, ls=0,
                 color=INK, align='left', italic=False, upper=False, bullet=False, bulletColor=RED, gap=16, bg=None,
                 padX=28, padY=12, radius=40)
        e.update(k)
        return e

    pack_h = 500
    doc = {
        'w': 1920, 'h': 1080, 'bg': BLUSH, 'name': 'Verdura Clear Skin Pack - LinkedIn featured',
        'els': [
            dict(id='photo', name='Photo', type='image', src='asset:vcsp-photo', x=0, y=0, w=1240, h=1080, fit='cover',
                 zoom=100, posX=40, posY=50, radius=0, fade=dict(side='right', color=BLUSH, size=30), shadow=None),
            dict(id='floor', name='Pack floor shadow', type='shadow', x=880, y=994, w=380, h=44, color='#501419', alpha=28),
            dict(id='pack', name='Clear Skin Pack', type='image', src='asset:vcsp-pack', x=930, y=1080 - 60 - pack_h,
                 w=round(pack_h * 618 / 1186, 1), h=pack_h, fit='contain', keep=True, radius=0, fade=None,
                 shadow=dict(blur=28, y=26, color='#501419', alpha=28)),
            dict(id='logo', name='Clear Skin Pack logo', type='image', src='asset:vcsp-logo', x=round(1920 - 64 - 132 * 1612.85 / 1174, 1),
                 y=56, w=round(132 * 1612.85 / 1174, 1), h=132, fit='contain', keep=True, radius=0, fade=None, shadow=None),
            text('pill', 'Pill – Acne care', 1220, 150, 'Acne care', weight=600, size=26, lh=1.45, ls=1.56, color='#ffffff',
                 upper=True, bg=RED, padX=28, padY=12, radius=40),
            text('title', 'Title', 1216, 225, 'The Multi-\nDimensional Way\nto Fight Acne', weight=700, size=78, lh=1.04,
                 ls=-0.78, color=NAVY),
            text('tag', 'Sub line', 1220, 491, 'with Verdura Clear Skin Pack', family='Playfair Display', weight=600,
                 size=44, italic=True, color=RED),
            dict(id='rule', name='Red rule', type='rect', x=1220, y=578, w=120, h=6, color=RED, radius=3),
            text('b1', 'Benefit 1', 1220, 622, 'Fights acne causing microbes', lh=1.45, bullet=True),
            text('b2', 'Benefit 2', 1220, 687, 'Removes comedones – white & black heads', lh=1.45, bullet=True),
            text('b3', 'Benefit 3', 1220, 753, 'Reduces excess sebum and pimple marks', lh=1.45, bullet=True),
        ],
    }
    return {'id': 'vcsp-linkedin', 'name': 'Verdura Clear Skin Pack – LinkedIn featured', 'cat': 'Banners & covers', 'doc': doc}, assets

TEMPLATES = [verdura_cover] + [lambda f=f: (f(), {}) for f in LIBRARY]

def build(web_out=None):
    assets, templates = {}, []
    for make in TEMPLATES:
        t, a = make(); templates.append(t); assets.update(a)
    if web_out:
        fonts = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,500;1,600'
                 '&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,500;1,600;1,700&family=Poppins:ital,wght@0,400;0,500;0,600;0,700;1,500'
                 '&family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;1,600&display=swap" rel="stylesheet">')
        doc_id, out = 'verdura-clear-skin-pack-linkedin-v1', pathlib.Path(web_out)   # same id keeps Sam's autosave
    else:
        fonts, doc_id, out = '<link href="fonts/fonts.css" rel="stylesheet">', 'app', APP / 'renderer' / 'index.html'
    src = (APP / 'src' / 'editor.html').read_text()
    html = (src.replace('__FONTS_LINK__', fonts).replace('__ASSETS__', json.dumps(assets))
               .replace('__DOC__', json.dumps({'id': doc_id, 'templates': templates}, ensure_ascii=False)))
    out.write_text(html)
    print('wrote', out, f'{len(html) / 1e6:.1f} MB')

if __name__ == '__main__':
    build(sys.argv[2] if len(sys.argv) > 2 and sys.argv[1] == '--web' else None)
