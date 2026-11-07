"""Ready-made editable templates (vector only: text, shapes and empty photo frames).

Each template is {'id', 'name', 'cat', 'doc'}; doc uses the editor's element format.
Fonts stay within the bundled four (Jost, Playfair Display, Poppins, Montserrat) so
they work offline in the desktop app too. Centred text uses `wrap` = box width.
"""

def T(id, x, y, text, size, **k):
    e = dict(id=id, name=k.pop('name', id), type='text', x=x, y=y, text=text, family='Jost', weight=500, size=size,
             lh=1.2, ls=0, color='#1f2a44', align='left', italic=False, upper=False, bullet=False, bulletColor='#d23f4a',
             gap=16, bg=None, padX=28, padY=12, radius=60)
    e.update(k)
    return e

def C(id, x, y, w, text, size, **k):          # centred text in a box of width w
    return T(id, x, y, text, size, align='center', wrap=w, **k)

def S(id, kind, x, y, w, h, fill, **k):
    e = dict(id=id, name=k.pop('name', id), type='shape', kind=kind, x=x, y=y, w=w, h=h, fill=fill, stroke=None, radius=0)
    e.update(k)
    return e

def F(id, x, y, w, h, frame=None, **k):        # empty picture frame: drop a photo on it
    e = dict(id=id, name=k.pop('name', 'Photo'), type='image', src=None, x=x, y=y, w=w, h=h, fit='cover', zoom=100,
             posX=50, posY=50, keep=False, radius=0, fade=None, shadow=None)
    if frame: e['frame'] = frame
    e.update(k)
    return e

def tpl(id, name, cat, w, h, bg, els, **k):
    doc = dict(w=w, h=h, bg=bg, name=name, els=els); doc.update(k)
    return {'id': id, 'name': name, 'cat': cat, 'doc': doc}

MS, PF = 'Montserrat', 'Playfair Display'

def big_sale():
    INK, OR = '#111827', '#ff5a36'
    return tpl('t-sale', 'Big sale – offer post', 'Social posts', 1080, 1080, '#ffd23f', [
        S('blob', 'blob', 600, -160, 640, 640, OR, name='Blob', opacity=90),
        S('ring', 'ring', 40, 820, 300, 300, INK, name='Ring', opacity=12),
        T('pill', 80, 150, 'Limited time', 26, name='Pill', weight=600, upper=True, ls=3, color='#ffffff', bg=INK),
        T('title', 74, 230, 'MEGA\nSALE', 230, name='Title', family=MS, weight=800, lh=.9, ls=-4, color=INK),
        S('burst', 'burst', 690, 560, 300, 300, OR, name='Burst badge'),
        C('b1', 690, 622, 300, 'UP TO', 34, name='Badge top', family=MS, weight=700, color='#ffffff'),
        C('b2', 690, 662, 300, '50%', 96, name='Badge number', family=MS, weight=800, lh=1, color='#ffffff'),
        C('b3', 690, 760, 300, 'OFF', 34, name='Badge bottom', family=MS, weight=700, color='#ffffff'),
        T('cta', 80, 900, 'Shop now · www.yourbrand.com', 34, name='Shop line', weight=600, color=INK),
    ])

def quote_card():
    INK, ACC = '#2b2b2b', '#b5835a'
    return tpl('t-quote', 'Quote card', 'Social posts', 1080, 1080, '#f4efe6', [
        S('ring', 'ring', 800, 820, 360, 360, ACC, name='Ring', opacity=25),
        T('mark', 88, 40, '“', 320, name='Quote mark', family=PF, weight=700, lh=1, color=ACC),
        T('quote', 100, 330, 'Take care of your skin. You’ll wear it for the rest of your life.', 64, name='Quote',
          family=PF, weight=500, italic=True, lh=1.25, color=INK, wrap=860),
        S('rule', 'rect', 100, 760, 80, 5, ACC, name='Rule'),
        T('who', 100, 795, '— Dr. Jane Doe', 34, name='Author', weight=600, color=INK),
        T('role', 100, 848, 'Dermatologist', 24, name='Role', upper=True, ls=3, color='#7a7a7a'),
    ])

def product_launch():
    NAVY, RED = '#1f2a44', '#d23f4a'
    return tpl('t-launch', 'Product launch', 'Social posts', 1080, 1350, '#fde2e4', [
        F('photo', 240, 150, 600, 720, 'arch', name='Product photo'),
        C('pill', 390, 110, 300, 'New launch', 26, name='Pill', weight=600, upper=True, ls=3, color='#ffffff', bg=NAVY),
        C('title', 60, 905, 960, 'Meet Your New\nSkin Hero', 78, name='Title', family=PF, weight=700, lh=1.05, color=NAVY),
        C('sub', 60, 1090, 960, 'Gentle. Effective. Dermatologist tested.', 32, name='Sub line', weight=400, color='#4a5568'),
        C('cta', 380, 1170, 320, 'Shop now →', 30, name='Button', weight=600, color='#ffffff', bg=RED),
    ], bgGrad=dict(angle=160, c1='#fde2e4', c2='#e2ece9'))

def tips_cover():
    BG, LIME = '#1f3d36', '#c8f169'
    return tpl('t-tips', 'Tips carousel cover', 'Social posts', 1080, 1350, BG, [
        S('dot', 'ellipse', 740, 1030, 440, 440, LIME, name='Circle'),
        T('pill', 90, 120, 'Skincare 101', 26, name='Pill', weight=700, upper=True, ls=3, color=BG, bg=LIME),
        T('title', 86, 210, '5 Habits for\nHealthy, Clear\nSkin', 96, name='Title', family=MS, weight=800, lh=1.02, ls=-1, color='#ffffff'),
        T('list', 90, 620, 'Cleanse twice a day\nNever skip sunscreen\nDrink enough water\nChange pillowcases weekly\nDon’t pick at pimples',
          38, name='List', list='num', lh=1.6, color='#e6efe9'),
        T('swipe', 850, 1180, 'Swipe →', 36, name='Swipe', weight=700, color=BG),
        T('handle', 90, 1245, '@yourbrand', 26, name='Handle', color='#9fb7ae'),
    ])

def hiring():
    NAVY, BLUE = '#0b2545', '#0a66c2'
    tick = lambda i, t: T(f'job{i}', 80, 500 + i * 72, t, 40, name=f'Role {i + 1}', bullet=True, bulletColor=BLUE, lh=1.4, color=NAVY)
    return tpl('t-hiring', 'We’re hiring', 'Social posts', 1080, 1080, '#eef3f8', [
        S('ring', 'ring', 610, 430, 420, 420, BLUE, name='Ring', inner=.9),
        F('photo', 640, 460, 360, 360, 'ellipse', name='Team photo'),
        T('t1', 76, 120, 'WE’RE', 120, name='Title 1', family=MS, weight=800, lh=1, color=NAVY),
        T('t2', 72, 240, 'HIRING!', 170, name='Title 2', family=MS, weight=800, lh=1, ls=-3, color=BLUE),
        tick(0, 'Content Writer'), tick(1, 'Graphic Designer'), tick(2, 'Video Editor'),
        T('mail', 80, 800, 'Send your CV to careers@yourbrand.com', 30, name='How to apply', color='#33415c'),
        S('bar', 'rect', 0, 960, 1080, 120, NAVY, name='Bottom bar'),
        T('site', 80, 1000, 'yourbrand.com', 30, name='Website', color='#ffffff'),
        T('go', 790, 1000, 'Apply today →', 30, name='Apply', weight=600, color='#ffffff'),
    ])

def testimonial():
    IND = '#4f46e5'
    stars = [S(f'star{i}', 'star', 368 + i * 72, 300, 56, 56, '#f59e0b', name=f'Star {i + 1}') for i in range(5)]
    return tpl('t-review', 'Customer review', 'Social posts', 1080, 1080, '#eef2ff', [
        S('card', 'rect', 80, 160, 920, 760, '#ffffff', name='Card', radius=40,
          style=dict(shadow=dict(x=0, y=20, blur=60, color='#3730a3', alpha=18))),
        F('photo', 450, 70, 180, 180, 'ellipse', name='Customer photo', frameStroke=dict(width=8, color='#ffffff')),
        *stars,
        C('quote', 140, 400, 800, '“Within three weeks my skin felt calmer and clearer. I recommend it to everyone!”', 50,
          name='Review', family=PF, weight=500, italic=True, lh=1.35, color='#1e1b4b'),
        C('who', 80, 760, 920, 'Priya S.', 36, name='Name', weight=700, color='#1e1b4b'),
        C('where', 80, 812, 920, 'Verified buyer · Bengaluru', 26, name='Detail', color=IND),
        C('head', 0, 965, 1080, 'What our customers say', 26, name='Footer', weight=600, upper=True, ls=4, color=IND),
    ])

def festive():
    GOLD = '#fbbf24'
    sparks = [S(f'sp{i}', 'star', x, y, s, s, GOLD, name='Sparkle', points=4, inner=.3, opacity=o)
              for i, (x, y, s, o) in enumerate([(120, 140, 70, 80), (900, 180, 50, 70), (180, 900, 44, 60), (880, 860, 80, 85), (520, 940, 36, 60)])]
    return tpl('t-festive', 'Festive greeting', 'Social posts', 1080, 1080, '#7f1d1d', [
        S('ring', 'ring', 190, 120, 700, 700, GOLD, name='Ring', inner=.97, opacity=40),
        *sparks,
        S('flame', 'drop', 512, 170, 56, 90, '#f59e0b', name='Flame'),
        S('diya', 'ellipse', 470, 262, 140, 44, GOLD, name='Lamp'),
        C('title', 0, 330, 1080, 'Happy\nDiwali', 150, name='Title', family=PF, weight=700, italic=True, lh=1, color='#fde68a'),
        C('wish', 160, 680, 760, 'May this festival of lights bring joy, health and prosperity', 38, name='Wish', lh=1.4, color='#fff7ed'),
        C('from', 0, 860, 1080, '— From all of us at Your Brand', 30, name='From', color='#fcd34d'),
    ], bgGrad=dict(angle=160, c1='#7f1d1d', c2='#b45309'))

def doctor_tip():
    TEAL, DARK = '#0e7490', '#164e63'
    steps = [('Cool the skin', 'Take a cool shower or use a damp cloth for 15 minutes.'),
             ('Moisturise', 'Apply aloe vera gel or a fragrance-free lotion.'),
             ('Drink water', 'Sunburn draws fluid to the skin, so stay hydrated.'),
             ('Protect it', 'Stay out of the sun and wear loose cotton clothes.')]
    els = []
    for i, (h, b) in enumerate(steps):
        y = 430 + i * 190
        els += [S(f'n{i}', 'ellipse', 80, y, 110, 110, TEAL, name=f'Step {i + 1} circle'),
                C(f'nt{i}', 80, y + 28, 110, f'{i + 1}', 48, name=f'Step {i + 1} number', family=MS, weight=800, lh=1.1, color='#ffffff'),
                T(f'h{i}', 230, y + 6, h, 40, name=f'Step {i + 1} title', weight=700, color=DARK),
                T(f'b{i}', 230, y + 60, b, 28, name=f'Step {i + 1} text', color='#475569', wrap=760, lh=1.35)]
    return tpl('t-tip', 'Doctor’s tip – steps', 'Social posts', 1080, 1350, '#ecfeff', [
        S('blob', 'blob', 760, -140, 460, 460, '#a5f3fc', name='Blob', opacity=70),
        T('pill', 80, 90, 'Doctor’s tip', 26, name='Pill', weight=600, upper=True, ls=3, color='#ffffff', bg=TEAL),
        T('title', 78, 170, 'How to treat a\nsunburn at home', 78, name='Title', family=MS, weight=800, lh=1.05, color=DARK),
        *els,
        T('note', 80, 1225, 'See a doctor if you get blisters, fever or chills.', 28, name='Note', italic=True, color=TEAL, wrap=920),
    ])

def story_webinar():
    Y = '#facc15'
    return tpl('t-webinar', 'Webinar / event story', 'Stories', 1080, 1920, '#312e81', [
        T('pill', 90, 220, 'Free webinar', 30, name='Pill', weight=700, upper=True, ls=3, color='#1e1b4b', bg=Y),
        T('title', 86, 320, 'Understanding\nAcne: Causes\n& Cures', 104, name='Title', family=MS, weight=800, lh=1.02, ls=-1, color='#ffffff'),
        S('ring', 'ring', 250, 730, 580, 580, Y, name='Ring', inner=.9),
        F('photo', 280, 760, 520, 520, 'ellipse', name='Speaker photo'),
        C('name', 0, 1330, 1080, 'Dr. Jane Doe', 52, name='Speaker', weight=700, color='#ffffff'),
        C('role', 0, 1400, 1080, 'Consultant Dermatologist', 34, name='Speaker role', color='#ddd6fe'),
        S('box', 'rect', 90, 1490, 900, 180, '#ffffff', name='Date box', radius=30, opacity=14),
        C('date', 90, 1522, 900, 'SAT · 15 NOV · 6:00 PM IST', 44, name='Date', weight=700, color='#ffffff'),
        C('where', 90, 1592, 900, 'Live on Zoom · Link in bio', 30, name='Where', color='#e9d5ff'),
        C('cta', 310, 1730, 460, 'Register now', 38, name='Button', weight=700, color='#1e1b4b', bg=Y),
    ], bgGrad=dict(angle=160, c1='#312e81', c2='#7c3aed'))

def story_arrival():
    INK, ACC = '#2b2b2b', '#b5835a'
    return tpl('t-arrival', 'New arrival story', 'Stories', 1080, 1920, '#f6f1eb', [
        F('photo', 0, 0, 1080, 1150, name='Product photo'),
        S('badge', 'ellipse', 800, 1040, 220, 220, ACC, name='Offer circle'),
        C('off', 800, 1098, 220, '20%\nOFF', 54, name='Offer', family=MS, weight=800, lh=.95, color='#ffffff'),
        T('kick', 90, 1230, 'New arrival', 30, name='Kicker', weight=600, upper=True, ls=6, color=ACC),
        T('title', 86, 1290, 'The Glow\nCollection', 120, name='Title', family=PF, weight=700, lh=1, color=INK),
        T('sub', 90, 1560, 'Natural ingredients for radiant skin', 36, name='Sub line', color='#6b6b6b'),
        T('cta', 90, 1680, 'Shop the range', 32, name='Button', weight=600, color='#ffffff', bg=INK, padX=40, padY=18),
    ])

def youtube():
    SH = dict(shadow=dict(x=0, y=6, blur=0, color='#000000', alpha=70))
    return tpl('t-yt', 'YouTube thumbnail', 'YouTube', 1280, 720, '#0f172a', [
        F('photo', 600, 0, 680, 720, name='Face / photo'),
        S('fade', 'rect', 560, 0, 320, 720, '#0f172a', name='Fade', grad=dict(angle=90, c1='#0f172a', c2='rgba(15,23,42,0)')),
        T('l1', 50, 120, '5 MISTAKES', 92, name='Line 1', family=MS, weight=800, lh=1, color='#ffffff', fx=SH),
        T('l2', 46, 230, 'RUINING', 124, name='Line 2', family=MS, weight=800, lh=1, color='#facc15', fx=SH),
        T('l3', 50, 370, 'YOUR SKIN', 92, name='Line 3', family=MS, weight=800, lh=1, color='#ffffff', fx=SH),
        S('arrow', 'arrow', 500, 470, 170, 110, '#ef4444', name='Arrow', rot=-20),
        T('pill', 50, 560, 'Watch now', 30, name='Pill', weight=700, upper=True, ls=2, color='#ffffff', bg='#ef4444'),
    ])

def linkedin_banner():
    return tpl('t-li-banner', 'LinkedIn profile banner', 'Banners & covers', 1584, 396, '#0b2545', [
        S('ring1', 'ring', 1340, -120, 360, 360, '#1d4e89', name='Ring', inner=.8),
        S('ring2', 'ring', 1180, 250, 160, 160, '#8da9c4', name='Small ring', inner=.8, opacity=40),
        T('line', 560, 110, 'Helping brands grow with research-backed skincare', 44, name='Headline', family=PF, weight=600,
          italic=True, lh=1.2, color='#ffffff', wrap=760),
        T('sub', 560, 250, 'Dermatology · Formulation · Clinical research', 24, name='Sub line', upper=True, ls=2, color='#8da9c4'),
    ], bgGrad=dict(angle=90, c1='#0b2545', c2='#13315c'))

def fb_cover():
    BR = '#7c2d12'
    return tpl('t-fb', 'Facebook cover', 'Banners & covers', 1640, 624, '#fff7ed', [
        F('photo', 980, 0, 660, 624, name='Cover photo'),
        S('leaf', 'leaf', 820, 380, 170, 230, '#fdba74', name='Leaf', rot=30, opacity=80),
        T('title', 116, 150, 'Natural care for\nevery skin', 78, name='Title', family=PF, weight=700, lh=1.05, color=BR),
        T('sub', 120, 370, 'Shop online · Free delivery over ₹499', 30, name='Sub line', color='#9a3412'),
        T('cta', 120, 440, 'Shop now', 28, name='Button', weight=600, color='#ffffff', bg='#ea580c'),
    ])

def slide_title():
    SKY = '#38bdf8'
    return tpl('t-slide1', 'Presentation – title slide', 'Presentations', 1920, 1080, '#0f172a', [
        S('glow', 'ellipse', 1200, -300, 1000, 1000, SKY, name='Glow', opacity=35,
          grad=dict(type='radial', c1=SKY, c2='rgba(56,189,248,0)')),
        S('ring', 'ring', 1450, 620, 380, 380, SKY, name='Ring', inner=.95, opacity=40),
        S('bar', 'rect', 140, 380, 12, 250, SKY, name='Accent bar'),
        T('title', 190, 370, 'Annual Research\nReview 2026', 120, name='Title', family=MS, weight=800, lh=1.02, ls=-2, color='#ffffff'),
        T('sub', 194, 650, 'Dr. JRK’s Research · Strategy meeting', 40, name='Sub line', color='#94a3b8'),
        T('date', 194, 940, 'November 2026', 28, name='Date', upper=True, ls=3, color='#64748b'),
    ])

def slide_three():
    SKY, INK = '#38bdf8', '#0f172a'
    cols = [('Research', 'Clinical studies that prove every claim we make.'),
            ('Products', 'Formulas built on Ayurveda and modern dermatology.'),
            ('People', 'Doctors, chemists and creators working as one team.')]
    els = []
    for i, (h, b) in enumerate(cols):
        x = 140 + i * 560
        els += [S(f'card{i}', 'rect', x, 330, 520, 580, '#f1f5f9', name=f'Card {i + 1}', radius=28),
                S(f'dot{i}', 'ellipse', x + 50, 380, 110, 110, SKY, name=f'Circle {i + 1}'),
                C(f'num{i}', x + 50, 409, 110, f'0{i + 1}', 44, name=f'Number {i + 1}', family=MS, weight=700, lh=1.2, color='#ffffff'),
                T(f'h{i}', x + 50, 540, h, 46, name=f'Heading {i + 1}', family=MS, weight=700, color=INK),
                T(f'b{i}', x + 50, 615, b, 30, name=f'Text {i + 1}', lh=1.45, color='#475569', wrap=420)]
    return tpl('t-slide2', 'Presentation – three points', 'Presentations', 1920, 1080, '#ffffff', [
        T('title', 136, 115, 'Our three focus areas', 72, name='Title', family=MS, weight=700, color=INK),
        S('rule', 'rect', 140, 230, 120, 8, SKY, name='Rule', radius=4),
        *els,
        T('page', 1740, 995, '02', 24, name='Page number', color='#94a3b8'),
    ])

def flyer():
    GREEN, Y = '#14532d', '#facc15'
    tick = lambda i, t: T(f'pt{i}', 200, 2340 + i * 130, t, 80, name=f'Point {i + 1}', bullet=True, bulletColor=Y, gap=40, lh=1.3, color='#ffffff')
    return tpl('t-flyer', 'A4 event flyer', 'Print', 2480, 3508, '#ffffff', [
        F('photo', 0, 0, 2480, 1700, name='Event photo'),
        S('panel', 'rect', 0, 1640, 2480, 1868, GREEN, name='Green panel'),
        T('pill', 200, 1560, 'Open house', 70, name='Pill', weight=700, upper=True, ls=8, color=GREEN, bg=Y, padX=70, padY=30, radius=120),
        T('title', 190, 1790, 'Free Skin\nCheck-up Camp', 230, name='Title', family=MS, weight=800, lh=1, ls=-4, color='#ffffff'),
        tick(0, 'Expert dermatologist consultation'), tick(1, 'Personalised skincare advice'), tick(2, 'Free product samples'),
        T('date', 200, 2800, 'Sunday, 23 November · 10 AM – 4 PM', 84, name='Date', weight=600, color=Y),
        T('addr', 200, 2930, '123 Main Road, Your City · +91 98765 43210', 60, name='Address', color='#d1fae5'),
        S('bar', 'rect', 0, 3250, 2480, 258, '#0f3d22', name='Footer bar'),
        T('site', 200, 3340, 'www.yourbrand.com', 64, name='Website', weight=600, color='#ffffff'),
    ], unit='mm', dpi=300)

def certificate():
    GOLD, NAVY = '#b08d57', '#1f2a44'
    return tpl('t-cert', 'Certificate', 'Print', 3508, 2480, '#fffdf7', [
        S('frame1', 'rect', 100, 100, 3308, 2280, None, name='Outer border', stroke=dict(width=24, color=GOLD)),
        S('frame2', 'rect', 170, 170, 3168, 2140, None, name='Inner border', stroke=dict(width=6, color=GOLD)),
        C('t1', 0, 360, 3508, 'Certificate', 200, name='Title', family=PF, weight=700, upper=True, ls=30, color=NAVY),
        C('t2', 0, 620, 3508, 'Of appreciation', 80, name='Sub title', weight=500, upper=True, ls=20, color=GOLD),
        C('pre', 0, 850, 3508, 'This certificate is proudly presented to', 70, name='Intro', italic=True, color='#555555'),
        C('who', 0, 990, 3508, 'Recipient Name', 220, name='Name', family=PF, weight=600, italic=True, color=NAVY),
        S('rule', 'rect', 954, 1300, 1600, 6, GOLD, name='Rule'),
        C('body', 554, 1380, 2400, 'For outstanding contribution and dedication to the team’s research and growth throughout 2026.', 64,
          name='Reason', lh=1.45, color='#555555'),
        S('seal', 'badge', 1554, 1760, 400, 400, GOLD, name='Seal'),
        C('year', 1554, 1910, 400, '2026', 84, name='Seal year', family=PF, weight=700, lh=1.2, color='#ffffff'),
        S('sig1', 'rect', 500, 1960, 800, 5, NAVY, name='Signature line 1'),
        S('sig2', 'rect', 2208, 1960, 800, 5, NAVY, name='Signature line 2'),
        C('l1', 500, 1990, 800, 'Director', 56, name='Signature label 1', color=NAVY),
        C('l2', 2208, 1990, 800, 'Date', 56, name='Signature label 2', color=NAVY),
    ], unit='mm', dpi=300)

def business_card():
    NAVY, RED = '#1f2a44', '#d23f4a'
    return tpl('t-card', 'Business card', 'Print', 1050, 600, NAVY, [
        S('bar', 'rect', 0, 0, 24, 600, RED, name='Accent bar'),
        S('logo', 'ring', 810, 70, 160, 160, '#ffffff', name='Logo ring', inner=.92, opacity=40),
        C('logot', 810, 133, 160, 'LOGO', 26, name='Logo text', weight=600, ls=3, color='#ffffff'),
        T('name', 88, 140, 'Jane Doe', 64, name='Name', family=MS, weight=700, color='#ffffff'),
        T('role', 90, 230, 'Brand Designer', 28, name='Role', weight=600, upper=True, ls=3, color=RED),
        T('info', 90, 330, '+91 98765 43210\njane@yourbrand.com\nwww.yourbrand.com', 28, name='Contact', lh=1.6, color='#cbd5e1'),
    ], unit='in', dpi=300)

LIBRARY = [big_sale, quote_card, product_launch, tips_cover, hiring, testimonial, festive, doctor_tip,
           story_webinar, story_arrival, youtube, linkedin_banner, fb_cover, slide_title, slide_three,
           flyer, certificate, business_card]
