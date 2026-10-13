#!/usr/bin/env python3
"""Genera le illustrazioni tutorial SVG del corso in assets/img/.

Uso:  python3 tools/gen_svg.py
Tutte le figure condividono palette e primitive (dito + unghia vista dall'alto,
profilo laterale, pannelli step-by-step) per avere uno stile coerente.
"""
import math
import random
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'img')

# Palette
SKIN, SKIN_D = '#f3cdb6', '#d39c80'
NAIL, NAIL_S = '#f7c1cf', '#b9496f'
FREE = '#fff7f9'
INK, MUTED = '#3b2a30', '#7a6369'
ACC, ACC2 = '#c2577a', '#8e3b5a'
OK, ERR, WARN = '#2f8a5b', '#c0392b', '#b7791f'
PANEL = '#fbf1ee'
GEL = '#e9a7bd'
FONT = "system-ui, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif"

_uid = [0]


def uid(p='c'):
    _uid[0] += 1
    return '%s%d' % (p, _uid[0])


def svg(w, h, body, title):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
            'font-family="%s" role="img"><title>%s</title>'
            '<rect width="100%%" height="100%%" fill="#ffffff"/>%s</svg>\n') % (w, h, w, h, FONT, title, body)


def text(x, y, s, size=15, anchor='middle', weight=400, fill=INK, style=''):
    return ('<text x="%.1f" y="%.1f" font-size="%s" text-anchor="%s" font-weight="%s" fill="%s"%s>%s</text>'
            % (x, y, size, anchor, weight, fill, (' font-style="%s"' % style) if style else '', s))


def mtext(x, y, lines, size=14, anchor='middle', weight=400, fill=INK, lh=1.25):
    return ''.join(text(x, y + i * size * lh, l, size, anchor, weight, fill) for i, l in enumerate(lines))


def leader(x1, y1, x2, y2, label, anchor='start', size=14, weight=600, fill=INK):
    """Linea di richiamo con pallino sul punto indicato ed etichetta all'altra estremità."""
    dx = 6 if anchor == 'start' else (-6 if anchor == 'end' else 0)
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.3"/>'
            '<circle cx="%.1f" cy="%.1f" r="3.5" fill="%s"/>' % (x1, y1, x2, y2, MUTED, x1, y1, ACC2)
            + text(x2 + dx, y2 + 5, label, size, anchor, weight, fill))


def arrow_defs():
    return ('<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            '<path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker>'
            '<marker id="arw" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            '<path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>') % (ACC2, MUTED)


def arrow(x1, y1, x2, y2, color=ACC2, w=2.2, both=False, dash=''):
    m = 'ar' if color == ACC2 else 'arw'
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s"%s marker-end="url(#%s)"%s/>'
            % (x1, y1, x2, y2, color, w, (' marker-start="url(#%s)"' % m) if both else '', m,
               (' stroke-dasharray="%s"' % dash) if dash else ''))


def panel(x, y, w, h, title, num=None, color=ACC):
    s = '<rect x="%d" y="%d" width="%d" height="%d" rx="16" fill="%s"/>' % (x, y, w, h, PANEL)
    if num is not None:
        s += '<circle cx="%d" cy="%d" r="15" fill="%s"/>' % (x + 26, y + 26, color)
        s += text(x + 26, y + 31.5, str(num), 15, weight=800, fill='#fff')
        s += text(x + 50, y + 31, title, 15, 'start', 700)
    else:
        s += text(x + w / 2, y + 30, title, 16, weight=700)
    return s


def mark(x, y, ok=True, r=14):
    c = OK if ok else ERR
    sym = ('<path d="M%.1f,%.1f l5,5 l9,-10" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
           % (x - 7, y)) if ok else (
        '<path d="M%.1f,%.1f l10,10 M%.1f,%.1f l-10,10" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
        % (x - 5, y - 5, x + 5, y - 5))
    return '<circle cx="%.1f" cy="%.1f" r="%d" fill="%s"/>%s' % (x, y, r, c, sym)


# ---------------------------------------------------------------- unghia vista dall'alto
def nail_outline(cx, y_c, y_s, y_t, hw, shape):
    """Contorno della lamina (punta verso l'alto). y_c=base, y_s=linea del sorriso, y_t=punta."""
    L = y_s - y_t
    p = 'M%.1f,%.1f L%.1f,%.1f ' % (cx - hw, y_c + 6, cx + hw, y_c + 6)
    p += 'L%.1f,%.1f ' % (cx + hw, y_s)
    if shape == 'quadrata':
        p += 'L%.1f,%.1f L%.1f,%.1f ' % (cx + hw, y_t, cx - hw, y_t)
    elif shape == 'squoval':
        r = hw * 0.38
        p += 'L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f ' % (
            cx + hw, y_t + r, cx + hw, y_t, cx + hw - r, y_t, cx - hw + r, y_t, cx - hw, y_t, cx - hw, y_t + r)
    elif shape == 'tonda':
        top = max(y_t + hw * 0.75, y_t)
        p += 'L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f ' % (
            cx + hw, top, cx + hw, y_t + hw * 0.2, cx + hw * 0.55, y_t, cx, y_t,
            cx - hw * 0.55, y_t, cx - hw, y_t + hw * 0.2, cx - hw, top)
    elif shape == 'ovale':
        p += 'L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f ' % (
            cx + hw, y_s - L * 0.35, cx + hw, y_t + L * 0.1, cx + hw * 0.5, y_t, cx, y_t,
            cx - hw * 0.5, y_t, cx - hw, y_t + L * 0.1, cx - hw, y_s - L * 0.35)
    elif shape == 'mandorla':
        p += 'C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f ' % (
            cx + hw, y_s - L * 0.55, cx + hw * 0.42, y_t, cx, y_t,
            cx - hw * 0.42, y_t, cx - hw, y_s - L * 0.55, cx - hw, y_s)
    elif shape == 'stiletto':
        p += 'C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f ' % (
            cx + hw, y_s - L * 0.4, cx + hw * 0.18, y_t + L * 0.25, cx, y_t,
            cx - hw * 0.18, y_t + L * 0.25, cx - hw, y_s - L * 0.4, cx - hw, y_s)
    elif shape == 'ballerina':
        p += 'L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f ' % (
            cx + hw, y_s - L * 0.12, cx + hw * 0.52, y_t, cx - hw * 0.52, y_t, cx - hw, y_s - L * 0.12)
    elif shape == 'lipstick':
        p += 'L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f ' % (
            cx + hw, y_t + L * 0.45, cx + hw, y_t + L * 0.38, cx + hw - 8, y_t + L * 0.36, cx - hw, y_t)
    else:
        raise ValueError(shape)
    p += 'L%.1f,%.1f Z' % (cx - hw, y_s)
    return p


def finger_nail(cx, y_c, hw=40, nail_len=95, free_len=40, shape='squoval', smile=10,
                plate=NAIL, free=FREE, finger_len=80, lunula=True, free_grad=None, extra=''):
    """Dito con unghia vista dall'alto. Restituisce (svg, dict di punti utili)."""
    y_s = y_c - nail_len
    y_t = y_s - free_len
    fw = hw * 1.42
    f_top = y_s - 0.45 * hw
    out = ('<path d="M%.1f,%.1f L%.1f,%.1f A%.1f,%.1f 0 0 1 %.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
           % (cx - fw, y_c + finger_len, cx - fw, f_top + fw, fw, fw, cx + fw, f_top + fw, cx + fw, y_c + finger_len, SKIN, SKIN_D))
    outline = nail_outline(cx, y_c, y_s, y_t, hw, shape)
    clip = uid()
    out += '<defs><clipPath id="%s"><path d="%s"/></clipPath></defs>' % (clip, outline)
    out += '<path d="%s" fill="%s"/>' % (outline, plate)
    if lunula:
        out += '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="#fff" opacity=".55" clip-path="url(#%s)"/>' % (
            cx, y_c - 18, hw * 0.5, 26, clip)
    if free_len > 0 or free_grad:
        fp = 'M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (
            cx - hw - 6, y_s + smile, cx, y_s - smile, cx + hw + 6, y_s + smile, cx + hw + 6, y_t - 60, cx - hw - 6, y_t - 60)
        if free_grad:
            out += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" clip-path="url(#%s)"/>' % (
                cx - hw - 6, y_t - 5, 2 * hw + 12, y_c - y_t, free_grad, clip)
        else:
            out += '<path d="%s" fill="%s" clip-path="url(#%s)"/>' % (fp, free, clip)
    out += extra.replace('CLIP', clip)
    out += '<path d="%s" fill="none" stroke="%s" stroke-width="1.8"/>' % (outline, NAIL_S)
    # eponichio (piega prossimale a "U") + pieghe laterali
    out += ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s"/>'
            % (cx - fw + 1, y_c - 28, cx - hw - 4, y_c - 28, cx, y_c + 22, cx + hw + 4, y_c - 28, cx + fw - 1, y_c - 28,
               cx + fw - 1, y_c + 30, cx - fw + 1, y_c + 30, SKIN))
    out += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="1.8"/>'
            % (cx - hw - 4, y_c - 28, cx, y_c + 22, cx + hw + 4, y_c - 28, SKIN_D))
    for sx in (-1, 1):
        out += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="1.6"/>' % (
            cx + sx * (hw + 4), y_c - 28, cx + sx * (hw + 4), y_s + 8, SKIN_D)
    pts = dict(cx=cx, y_c=y_c, y_s=y_s, y_t=y_t, hw=hw, fw=fw, clip=clip)
    return out, pts


# ---------------------------------------------------------------- profilo laterale
def side_profile(ox, oy, w=300, stress=0.62, apex=0.45, apex_h=26, tip_h=7, root_h=3,
                 ext=True, regrowth=0, product=GEL, show_labels=False, finger=True, gap=0):
    """Profilo laterale (punta verso destra). oy = quota della lamina naturale."""
    xa = ox + regrowth + gap  # inizio prodotto
    xs = ox + w * stress
    xb = ox + w if ext else xs + 10
    ax = ox + w * apex
    s = ''
    if finger:
        s += ('<path d="M%.1f,%.1f L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" '
              'fill="%s" stroke="%s" stroke-width="1.5"/>'
              % (ox - 70, oy - 10, ox - 6, oy - 10, ox + 4, oy - 10, ox + 6, oy + 2, xs - 10, oy + 3,
                 xs + 40, oy + 6, xs + 40, oy + 75, xs - 20, oy + 80, ox - 70, oy + 80, SKIN, SKIN_D))
    # lamina naturale
    s += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="4" stroke-linecap="round"/>' % (ox, oy + 1, xs + 4, oy + 3, NAIL_S)
    # prodotto
    top = 'M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (
        xa, oy - root_h, (xa + ax) / 2, oy - apex_h, ax, oy - apex_h, (ax + xb) / 2, oy - apex_h, xb, oy - tip_h)
    s += '<path d="%s L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.6" opacity=".95"/>' % (
        top, xb, oy + 3, xs, oy + 3, xa, oy, product, NAIL_S)
    if regrowth:
        s += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="6" stroke-linecap="round"/>' % (ox, oy, xa, oy, '#f6a7bb')
    return s, dict(xa=xa, xs=xs, xb=xb, ax=ax, oy=oy, ah=oy - apex_h)


# ---------------------------------------------------------------- strumenti
def tool_file(x, y, ang=0, l=150, w=22, c1='#8a7d74', c2='#d9cfc6'):
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f)"><rect x="%.1f" y="%.1f" width="%d" height="%d" rx="%d" fill="%s"/>'
            '<rect x="%.1f" y="%.1f" width="%d" height="%d" rx="%d" fill="%s"/></g>'
            % (x, y, ang, -l / 2, -w / 2, l, w / 2, w / 2, c1, -l / 2, 0, l, w / 2, w / 4, c2))


def tool_pusher(x, y, ang=0, l=150):
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f)"><rect x="0" y="-4" width="%d" height="8" rx="4" fill="#9aa3ad"/>'
            '<path d="M0,-4 L-22,-11 L-24,11 L0,4 Z" fill="#7d8792"/></g>' % (x, y, ang, l))


def tool_brush(x, y, ang=0, l=140, bristle=ACC):
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f)"><rect x="18" y="-5" width="%d" height="10" rx="5" fill="#4b3a40"/>'
            '<rect x="10" y="-6" width="12" height="12" fill="#c9b8a0"/>'
            '<path d="M10,-6 L-14,-4 Q-20,0 -14,4 L10,6 Z" fill="%s"/></g>' % (x, y, ang, l, bristle))


def tool_stick(x, y, ang=0, l=130):
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f)"><path d="M0,-5 L%d,-5 L%d,5 L0,5 L-16,0 Z" fill="#e0bf8f" stroke="#b8956a"/></g>'
            % (x, y, ang, l, l))


# ================================================================= FIGURE
FIGS = {}


def fig(name):
    def deco(f):
        FIGS[name] = f
        return f
    return deco


@fig('logo.svg')
def logo():
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><title>NailX</title>'
            '<rect width="64" height="64" rx="16" fill="%s"/>'
            '<path d="M20,54 L20,30 C20,14 27,8 32,6 C37,8 44,14 44,30 L44,54 Z" fill="#fff"/>'
            '<path d="M24,52 L24,31 C24,20 28,14 32,12 C36,14 40,20 40,31 L40,52 Z" fill="%s"/>'
            '<ellipse cx="32" cy="48" rx="7" ry="4" fill="#fff" opacity=".6"/></svg>\n') % (ACC, NAIL)


@fig('hero.svg')
def hero():
    b = '<defs><linearGradient id="hg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fbe3ea"/><stop offset="1" stop-color="#fff"/></linearGradient></defs>'
    b += '<rect width="600" height="420" fill="url(#hg)"/>'
    b += '<circle cx="470" cy="90" r="60" fill="%s" opacity=".35"/><circle cx="90" cy="330" r="80" fill="%s" opacity=".25"/>' % (GEL, GEL)
    # quattro dita con forme diverse
    for i, (cx, yc, sh, col, ang) in enumerate([(175, 245, 'mandorla', '#e46f8f', -12), (265, 215, 'mandorla', '#e46f8f', -4),
                                                (355, 225, 'mandorla', '#e46f8f', 4), (440, 260, 'mandorla', '#e46f8f', 12)]):
        f, _ = finger_nail(0, 0, hw=30, nail_len=72, free_len=50, shape=sh, plate=col, free=col, finger_len=220, lunula=False)
        b += '<g transform="translate(%d,%d) rotate(%d)">%s</g>' % (cx, yc, ang, f)
    # palmo
    b += '<path d="M120,330 Q300,300 500,330 L520,420 L100,420 Z" fill="%s" stroke="%s" stroke-width="1.5"/>' % (SKIN, SKIN_D)
    # riflessi
    for cx, yc, ang in [(175, 245, -12), (265, 215, -4), (355, 225, 4), (440, 260, 12)]:
        b += '<g transform="translate(%d,%d) rotate(%d)"><path d="M-12,-60 Q-14,-95 -4,-115" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round" opacity=".7"/></g>' % (cx, yc, ang)
    b += tool_brush(520, 330, -60, 120)
    b += tool_file(80, 120, 35, 170, 24)
    return svg(600, 420, b, 'Mano con unghie ricostruite a mandorla, pennello e lima')


@fig('anatomia-alto.svg')
def anat_top():
    f, p = finger_nail(280, 400, hw=78, nail_len=200, free_len=55, shape='tonda', smile=16, finger_len=90)
    b = f
    cx, ys, yt, yc, hw = p['cx'], p['y_s'], p['y_t'], p['y_c'], p['hw']
    # cuticola: banda sottile semitrasparente sopra la piega
    b += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="#fff" stroke-width="6" opacity=".8"/>'
          % (cx - hw + 2, yc - 34, cx, yc + 10, cx + hw - 2, yc - 34))
    b += leader(cx + 20, yt + 12, 520, 70, 'Bordo libero')
    b += leader(cx + 50, ys + 2, 520, 120, 'Linea del sorriso (smile line)')
    b += leader(cx + hw - 1, ys + 14, 520, 165, 'Punto di stress (lato)')
    b += leader(cx + 30, ys + 80, 520, 215, 'Lamina ungueale (sopra il letto)')
    b += leader(cx + hw + 4, ys + 120, 520, 262, 'Solco / piega laterale')
    b += leader(cx + 22, yc - 22, 520, 308, 'Lunula (parte visibile della matrice)')
    b += leader(cx - 50, yc - 18, 520, 352, 'Cuticola (pelle morta sulla lamina)')
    b += leader(cx + 60, yc + 14, 520, 398, 'Eponichio (piega prossimale viva)')
    b += text(40, 40, 'Vista dall\'alto', 20, 'start', 800, ACC2)
    return svg(860, 500, b, 'Anatomia dell\'unghia vista dall\'alto')


@fig('anatomia-sezione.svg')
def anat_sec():
    b = ''
    b += ('<path d="M40,150 L380,150 Q425,150 432,168 L640,172 C705,175 725,215 718,255 C710,305 660,330 600,330 L40,330 Z" '
          'fill="%s" stroke="%s" stroke-width="1.5"/>' % (SKIN, SKIN_D))
    b += '<path d="M60,215 L520,212 C590,210 622,228 616,252 C610,272 585,280 520,278 L60,282 Z" fill="#efe3d0" stroke="#cdb894" stroke-width="1.5"/>'
    b += '<path d="M430,172 L640,174 C660,175 672,180 676,188 L430,190 Z" fill="#ee8ea7"/>'
    b += '<path d="M352,170 Q392,196 432,190 L432,176 Q396,178 356,162 Z" fill="#d9577c"/>'
    b += '<path d="M352,164 C450,160 600,162 740,166 L741,177 C600,172 450,172 356,174 Z" fill="#f7d4dd" stroke="%s" stroke-width="1.6"/>' % NAIL_S
    b += '<path d="M670,176 Q692,178 694,192 L676,194 Z" fill="#e4a48a"/>'
    b += ('<path d="M330,150 L390,150 Q428,150 434,166 L424,168 Q404,160 340,166 Z" fill="%s" stroke="%s" stroke-width="1.2"/>'
          % (SKIN, SKIN_D))
    b += '<path d="M433,164 L462,163" stroke="#fff" stroke-width="4" opacity=".9"/>'
    b += '<circle cx="676" cy="175" r="6" fill="none" stroke="%s" stroke-width="2.5"/>' % ERR
    b += leader(395, 182, 360, 380, 'Matrice (produce la lamina)', 'middle')
    b += leader(420, 156, 360, 90, 'Eponichio / piega prossimale', 'middle')
    b += leader(448, 163, 500, 60, 'Cuticola', 'start')
    b += leader(560, 166, 610, 105, 'Lamina ungueale', 'start')
    b += leader(560, 182, 520, 380, 'Letto ungueale', 'middle')
    b += leader(676, 175, 760, 120, 'Punto di stress', 'start')
    b += leader(720, 171, 770, 155, 'Bordo libero', 'start')
    b += leader(686, 188, 740, 380, 'Iponichio (barriera)', 'middle')
    b += leader(200, 248, 110, 380, 'Falange distale (osso)', 'middle')
    b += text(40, 40, 'Sezione laterale', 20, 'start', 800, ACC2)
    return svg(900, 420, arrow_defs() + b, 'Anatomia dell\'unghia in sezione laterale')


@fig('zone-costruzione.svg')
def zones():
    s, p = side_profile(220, 230, w=520, stress=0.55, apex=0.42, apex_h=34, tip_h=6, root_h=2, gap=16)
    clip = uid()
    # ripeto il contorno del prodotto come clip per colorare le zone
    xa, xs, xb, ax, oy = p['xa'], p['xs'], p['xb'], p['ax'], p['oy']
    top = 'M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (
        xa, oy - 2, (xa + ax) / 2, oy - 34, ax, oy - 34, (ax + xb) / 2, oy - 34, xb, oy - 6, xb, oy + 3, xs, oy + 3, xa, oy)
    b = s + '<defs><clipPath id="%s"><path d="%s"/></clipPath></defs>' % (clip, top)
    z3, z2 = xa + 110, xs + 40
    for x0, x1, c in [(xa - 5, z3, '#f9d7e1'), (z3, z2, '#e46f8f'), (z2, xb + 5, '#f2a5bb')]:
        b += '<rect x="%.1f" y="150" width="%.1f" height="100" fill="%s" clip-path="url(#%s)"/>' % (x0, x1 - x0, c, clip)
    b += '<path d="%s" fill="none" stroke="%s" stroke-width="1.6"/>' % (top, NAIL_S)
    for x in (z3, z2):
        b += '<line x1="%.1f" y1="120" x2="%.1f" y2="250" stroke="%s" stroke-dasharray="5 5"/>' % (x, x, MUTED)
    b += mtext((xa + z3) / 2, 90, ['ZONA 3', 'cuticola: strato', 'sottilissimo'], 14, weight=700)
    b += mtext((z3 + z2) / 2, 90, ['ZONA 2', 'apex: struttura', 'e spessore'], 14, weight=700, fill=ACC2)
    b += mtext((z2 + xb) / 2, 90, ['ZONA 1', 'bordo libero: si', 'assottiglia in punta'], 14, weight=700)
    b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>' % (ax, oy - 34, ax, oy + 3, ACC2)
    b += leader(ax, oy - 34, ax - 40, 300, 'Apex: punto più alto', 'end')
    b += leader(xs, oy + 3, xs + 30, 330, 'Punto di stress (sotto l\'apex)', 'start')
    b += arrow(xa - 18, oy - 16, xa, oy - 16, MUTED, 1.5, True)
    b += text(xa - 24, oy - 30, '≈1,5 mm dalla pelle', 13, 'end', 600, MUTED)
    b += text(40, 40, 'Le 3 zone della ricostruzione', 20, 'start', 800, ACC2)
    return svg(860, 380, arrow_defs() + b, 'Le tre zone di costruzione e l\'apex')


@fig('apex-confronto.svg')
def apex_cmp():
    b = ''
    cases = [('Corretto', True, dict(apex=0.47, apex_h=26, tip_h=5, root_h=2), 'Apex sopra il punto di stress'),
             ('Piatto', False, dict(apex=0.5, apex_h=8, tip_h=6, root_h=4), 'Nessuna struttura: si rompe'),
             ('Gobba / spesso', False, dict(apex=0.2, apex_h=34, tip_h=14, root_h=20), 'Spesso alla cuticola e in punta')]
    for i, (t, ok, kw, sub) in enumerate(cases):
        x = 30 + i * 300
        b += panel(x, 20, 280, 260, t)
        b += mark(x + 250, 48, ok)
        s, p = side_profile(x + 80, 170, w=180, stress=0.62, **kw)
        b += s
        b += '<circle cx="%.1f" cy="%.1f" r="4" fill="%s"/>' % (p['xs'], p['oy'] + 3, ERR)
        b += text(x + 140, 265, sub, 13.5, weight=600, fill=OK if ok else ERR)
    b += text(470, 310, 'Il pallino rosso indica il punto di stress: l\'apex deve stare lì sopra.', 14, fill=MUTED)
    return svg(940, 330, b, 'Apex corretto, piatto e troppo spesso a confronto')


@fig('curva-c.svg')
def ccurve():
    b = text(40, 40, 'Curva a C – vista frontale dal bordo libero', 20, 'start', 800, ACC2)
    for i, (k, lab, sub) in enumerate([(14, 'Bassa (piatta)', 'unghie piatte, corte'), (32, 'Media', 'uso quotidiano'),
                                       (52, 'Alta (pinching)', 'gara / unghie lunghe')]):
        cx = 150 + i * 260
        b += '<circle cx="%d" cy="%d" r="62" fill="none" stroke="#e5d6d2" stroke-dasharray="4 5"/>' % (cx, 160 + 62 - k)
        b += ('<path d="M%d,170 Q%d,%d %d,170" fill="none" stroke="%s" stroke-width="12" stroke-linecap="round"/>'
              % (cx - 75, cx, 170 - 2 * k, cx + 75, ACC))
        b += '<path d="M%d,170 Q%d,%d %d,170" fill="none" stroke="#fff" stroke-width="2" opacity=".6"/>' % (cx - 70, cx, 170 - 2 * k + 3, cx + 70)
        b += text(cx, 220, lab, 16, weight=700)
        b += text(cx, 242, sub, 13.5, fill=MUTED)
    b += text(410, 285, 'La curva segue quella naturale della cliente: non esiste un valore unico per tutti.', 14, fill=MUTED)
    return svg(820, 310, b, 'Curva a C bassa, media e alta')


SHAPES = [('quadrata', 'Quadrata', 'Netta, accorcia il dito'), ('squoval', 'Squoval', 'Robusta, la più versatile'),
          ('tonda', 'Tonda', 'Corta, pratica'), ('ovale', 'Ovale', 'Elegante, allunga'),
          ('mandorla', 'Mandorla', 'Slancia molto il dito'), ('stiletto', 'Stiletto', 'A punta, richiede lunghezza'),
          ('ballerina', 'Ballerina / Coffin', 'Rastremata, punta piatta'), ('lipstick', 'Lipstick', 'Taglio obliquo')]


@fig('forme.svg')
def forme():
    b = ''
    for i, (sh, name, sub) in enumerate(SHAPES):
        col, row = i % 4, i // 4
        cx, yc = 120 + col * 220, 230 + row * 290
        f, _ = finger_nail(cx, yc, hw=36, nail_len=80, free_len=70 if sh not in ('quadrata', 'squoval', 'tonda') else 45,
                           shape=sh, smile=10, finger_len=24)
        b += f
        b += text(cx, yc + 52, name, 16, weight=800)
        b += text(cx, yc + 72, sub, 13, fill=MUTED)
    return svg(880, 590, b, 'Le otto forme principali dell\'unghia')


@fig('lime-grane.svg')
def grit():
    b = text(40, 40, 'Grane delle lime: più il numero è basso, più la lima è aggressiva', 19, 'start', 800, ACC2)
    segs = [(80, 100, '#5b4a44', '80–100', 'Accorciare, togliere', 'materiale artificiale'),
            (100, 180, '#8a7469', '100/180', 'Dare forma alla', 'ricostruzione'),
            (180, 240, '#c3ad9f', '180–240', 'Unghia naturale,', 'opacizzare, rifinire'),
            (240, 400, '#ece1d8', '240+ / buffer', 'Levigare e', 'lucidare')]
    x0, W = 60, 760
    xs = [x0, x0 + 150, x0 + 350, x0 + 550, x0 + W]
    for i, (a, c, col, lab, l1, l2) in enumerate(segs):
        x, w = xs[i], xs[i + 1] - xs[i]
        b += '<rect x="%d" y="80" width="%d" height="46" fill="%s"%s/>' % (x, w, col, ' rx="0"')
        b += text(x + w / 2, 109, lab, 16, weight=800, fill='#fff' if i < 2 else INK)
        b += mtext(x + w / 2, 156, [l1, l2], 14)
    b += arrow(80, 210, 800, 210, MUTED, 1.6)
    b += text(80, 235, 'più abrasiva', 13, 'start', fill=MUTED)
    b += text(800, 235, 'più fine', 13, 'end', fill=MUTED)
    b += '<rect x="60" y="80" width="760" height="46" fill="none" stroke="%s" rx="4"/>' % MUTED
    b += text(440, 280, 'Sulla lamina naturale non scendere sotto 180: serve solo togliere la lucidità, mai assottigliare.', 14, weight=600, fill=ERR)
    return svg(880, 300, arrow_defs() + b, 'Scala delle grane delle lime')


@fig('punte-fresa.svg')
def bits():
    b = text(40, 40, 'Punte per fresa: forme, colori e velocità', 20, 'start', 800, ACC2)

    def shank(x, y):
        return '<rect x="%d" y="%d" width="10" height="70" fill="#b8bfc6"/>' % (x - 5, y)
    items = [('Cilindro', ['superficie,', 'accorciare'], '<rect x="-14" y="-50" width="28" height="50" rx="3"/>'),
             ('Cil. sicurezza', ['bordo liscio:', 'lati e cuticola'], '<rect x="-14" y="-50" width="28" height="50" rx="12"/>'),
             ('Cono', ['sotto il bordo', 'libero, lati'], '<path d="M-14,0 L-3,-56 L3,-56 L14,0 Z"/>'),
             ('Fiamma', ['zona cuticolare,', 'pterigio'], '<path d="M-9,0 C-14,-20 -6,-44 0,-58 C6,-44 14,-20 9,0 Z"/>'),
             ('Pallina', ['pulizia cuticole', 'e solchi'], '<circle cx="0" cy="-12" r="12"/>'),
             ('Mandrino', ['con rullino', 'abrasivo monouso'], '<rect x="-15" y="-46" width="30" height="46" rx="4" fill="#cdb79e"/>')]
    for i, (n, sub, shape) in enumerate(items):
        x = 90 + i * 140
        b += shank(x, 160)
        b += '<g transform="translate(%d,160)" fill="#9aa3ad" stroke="#6f7a85" stroke-width="1.5">%s</g>' % (x, shape)
        b += text(x, 255, n, 14, weight=700)
        b += mtext(x, 274, sub, 12, fill=MUTED)
    # codici colore
    b += text(40, 330, 'Codice colore della grana (indicativo, varia tra marchi)', 15, 'start', 700)
    for i, (c, l) in enumerate([('#f2c94c', 'Extra fine'), ('#e05252', 'Fine'), ('#4a7fd4', 'Media'),
                                ('#3aa35b', 'Grossa'), ('#333333', 'Extra grossa')]):
        x = 60 + i * 160
        b += '<rect x="%d" y="335" width="34" height="18" rx="4" fill="%s"/>' % (x, c)
        b += text(x + 42, 349, l, 14, 'start')
    # RPM
    b += text(40, 400, 'Velocità indicative (RPM)', 15, 'start', 700)
    for i, (lab, a, z, col) in enumerate([('Cuticola / unghia naturale', 5000, 10000, OK),
                                          ('Sfumare la superficie', 10000, 15000, WARN),
                                          ('Rimuovere prodotto', 15000, 25000, ERR)]):
        y = 420 + i * 34
        b += text(270, y + 15, lab, 14, 'end')
        x1, x2 = 290 + a / 30000 * 520, 290 + z / 30000 * 520
        b += '<rect x="290" y="%d" width="520" height="20" rx="10" fill="#f0e6e2"/>' % y
        b += '<rect x="%.1f" y="%d" width="%.1f" height="20" rx="10" fill="%s"/>' % (x1, y, x2 - x1, col)
        b += text(x2 + 8, y + 15, '%s–%s' % (format(a, ',').replace(',', '.'), format(z, ',').replace(',', '.')), 13, 'start', 600)
    b += text(450, 540, 'Carburo solo su prodotto artificiale · diamantate su unghia naturale e cuticola · pressione leggera, punta sempre in movimento', 13, fill=MUTED)
    return svg(900, 560, b, 'Punte per fresa elettrica, codici colore e velocità')


@fig('preparazione.svg')
def prep():
    b = ''
    titles = ['Igienizza mani e strumenti', 'Arretra la cuticola', 'Rimuovi il pterigio',
              'Opacizza (grana 180–240)', 'Elimina la polvere', 'Disidratante + primer']
    for i, t in enumerate(titles):
        col, row = i % 3, i // 3
        x, y = 20 + col * 300, 20 + row * 300
        b += panel(x, y, 280, 280, t, i + 1)
        cx, yc = x + 140, y + 225
        extra = ''
        if i == 3:
            extra = ''.join('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#fff" stroke-width="1.4" opacity=".9" clip-path="url(#CLIP)"/>'
                            % (cx - 40 + k * 9, yc - 130, cx - 55 + k * 9, yc) for k in range(12))
        f, p = finger_nail(cx, yc, hw=38, nail_len=110, free_len=18, shape='tonda', smile=8, finger_len=40, extra=extra)
        b += f
        if i == 0:
            for k, (dx, dy) in enumerate([(-60, -150), (55, -120), (-70, -60), (65, -40)]):
                b += '<circle cx="%d" cy="%d" r="%d" fill="#cfe9f7" stroke="#86bfe0"/>' % (cx + dx, yc + dy, 9 + k % 2 * 4)
            b += '<path d="M%d,%d l0,-30 l16,0 l0,30 z" fill="#86bfe0" opacity=".0"/>' % (cx, yc)
        elif i == 1:
            b += tool_pusher(cx + 5, yc - 28, -60, 120)
            b += arrow(cx - 40, yc - 70, cx - 40, yc - 35)
        elif i == 2:
            b += '<path d="M%d,%d Q%d,%d %d,%d" stroke="#fff" stroke-width="5" fill="none"/>' % (cx - 30, yc - 22, cx, yc - 42, cx + 30, yc - 22)
            b += tool_stick(cx + 12, yc - 34, -55, 120)
        elif i == 3:
            b += tool_file(cx + 30, yc - 80, -70, 140, 20)
            b += arrow(cx - 70, yc - 100, cx - 70, yc - 50, MUTED, 1.5, True)
        elif i == 4:
            b += tool_brush(cx + 50, yc - 90, -40, 100, '#c9b8a0')
            for k in range(7):
                b += '<circle cx="%d" cy="%d" r="2.5" fill="#bfae9f"/>' % (cx + 50 + k * 9, yc - 150 + (k * 13) % 30)
        elif i == 5:
            b += tool_brush(cx + 12, yc - 70, -50, 70, '#f1e3a0')
            b += '<circle cx="%d" cy="%d" r="5" fill="#f1e3a0" opacity=".9"/>' % (cx - 4, yc - 60)
            b += text(cx, y + 265, 'solo sulla lamina, poco prodotto', 12.5, fill=MUTED)
    return svg(920, 620, arrow_defs() + b, 'Preparazione dell\'unghia naturale in sei passaggi')


@fig('tip-applicazione.svg')
def tip_app():
    b = ''
    T = ['Scegli la misura', 'Incolla a ~45°', 'Taglia la lunghezza', 'Fondi il contatto']
    for i, t in enumerate(T):
        x = 20 + i * 230
        b += panel(x, 20, 215, 300, t, i + 1)
    # 1 misura
    cx = 20 + 107
    f, p = finger_nail(cx, 275, hw=34, nail_len=95, free_len=8, shape='tonda', finger_len=25)
    b += f
    b += arrow(cx - 34, 120, cx + 34, 120, ACC2, 1.8, True)
    b += text(cx, 108, 'da solco a solco', 12.5, weight=600)
    # 2 angolo (vista laterale)
    x = 250
    b += ('<path d="M%d,250 L%d,250 C%d,250 %d,290 %d,300 L%d,300 Z" fill="%s" stroke="%s"/>'
          % (x + 10, x + 120, x + 160, x + 160, x + 120, x + 10, SKIN, SKIN_D))
    b += '<path d="M%d,249 L%d,249" stroke="%s" stroke-width="4"/>' % (x + 40, x + 140, NAIL_S)
    b += '<g transform="translate(%d,247) rotate(-40)"><rect x="0" y="-5" width="120" height="7" rx="3" fill="#f3eee6" stroke="#cbbfae"/></g>' % (x + 110)
    b += '<path d="M%d,247 A40,40 0 0 0 %d,222" fill="none" stroke="%s" stroke-width="1.6" stroke-dasharray="3 3"/>' % (x + 150, x + 140, ACC2)
    b += text(x + 165, 225, '45°', 14, 'start', 800, ACC2)
    b += arrow(x + 190, 150, x + 200, 210, ACC2, 1.8)
    b += text(x + 107, 92, 'colla sull\'incavo (well)', 12.5, fill=MUTED)
    b += text(x + 107, 110, 'premi 5–10 s, niente bolle', 12.5, fill=MUTED)
    # 3 taglio
    cx = 480 + 107
    extra = ''
    f, p = finger_nail(cx, 285, hw=32, nail_len=70, free_len=110, shape='quadrata', smile=4, free='#f3eee6', finger_len=15)
    b += f
    b += '<line x1="%d" y1="140" x2="%d" y2="140" stroke="%s" stroke-width="2" stroke-dasharray="6 4"/>' % (cx - 60, cx + 60, ERR)
    b += text(cx, 130, 'linea di taglio', 12.5, weight=700, fill=ERR)
    # 4 blending
    cx = 710 + 107
    extra = '<rect x="%d" y="%d" width="80" height="22" fill="url(#hatch)" clip-path="url(#CLIP)"/>' % (cx - 40, 285 - 95 - 10)
    f, p = finger_nail(cx, 285, hw=32, nail_len=95, free_len=55, shape='squoval', smile=4, free='#f3eee6', finger_len=15, extra=extra)
    b += f
    b += leader(cx + 20, 285 - 95, cx + 40, 95, 'zona da fondere', 'middle', 12.5)
    b += text(cx, 315 - 5, 'non limare l\'unghia naturale', 12, fill=ERR, weight=600)
    defs = ('<defs><pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
            '<line x1="0" y1="0" x2="0" y2="6" stroke="%s" stroke-width="2.5"/></pattern></defs>' % ACC)
    return svg(950, 340, arrow_defs() + defs + b, 'Applicazione del tip in quattro passaggi')


@fig('cartina.svg')
def form_place():
    b = ''
    cases = [('Corretta', True, 0, 0, 'a filo del bordo libero, in asse'),
             ('Spazio sotto il bordo', False, 0, 14, 'il prodotto cola: sollevamenti'),
             ('Fuori asse', False, 16, 0, 'l\'unghia cresce storta')]
    for i, (t, ok, ang, gap, sub) in enumerate(cases):
        x = 20 + i * 300
        b += panel(x, 20, 280, 340, t)
        b += mark(x + 250, 48, ok)
        cx, yc = x + 140, 300
        ys = yc - 95
        # cartina (dietro il dito), ritagliata al pannello
        pc = uid()
        b += '<defs><clipPath id="%s"><rect x="%d" y="62" width="280" height="270"/></clipPath></defs>' % (pc, x)
        hole = 50 + gap
        form = ('<g clip-path="url(#%s)"><g transform="rotate(%d %d %d)"><path d="M%d,%d L%d,%d L%d,%d L%d,%d L%d,%d A%d,%d 0 0 0 %d,%d Z" fill="#f6e7a8" stroke="#d8c26a"/>'
                % (pc, ang, cx, ys, cx - 90, ys + 40, cx - 90, ys - 140, cx + 90, ys - 140, cx + 90, ys + 40, cx + 52, ys + 40,
                   52, hole, cx - 52, ys + 40))
        for k in range(1, 6):
            form += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#d8c26a" stroke-width="1"/>' % (cx - 80, ys - k * 24 + 4, cx + 80, ys - k * 24 + 4)
        form += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.6" stroke-dasharray="5 4"/></g></g>' % (cx, ys - 140, cx, ys - 10, ACC2)
        b += form
        f, p = finger_nail(cx, yc, hw=34, nail_len=95, free_len=8, shape='tonda', smile=6, finger_len=30)
        b += f
        if gap:
            b += '<path d="M%d,%d Q%d,%d %d,%d" stroke="%s" stroke-width="3" fill="none"/>' % (cx - 30, ys - 4, cx, ys - 22, cx + 30, ys - 4, ERR)
        b += text(cx, 350, sub, 13, weight=600, fill=OK if ok else ERR)
    return svg(920, 380, b, 'Posizionamento corretto ed errato della cartina')


@fig('perla-acrilico.svg')
def bead():
    b = text(40, 40, 'Rapporto liquido/polvere: la "perla" di acrilico', 20, 'start', 800, ACC2)
    cases = [('Bagnata', '≈ 2 : 1', False, 'cola nei solchi, ritira,', 'monomero a contatto con la pelle'),
             ('Media', '≈ 1,5 : 1', True, 'lucida e bombata, resta in', 'forma qualche secondo'),
             ('Asciutta', '≈ 1 : 1', False, 'granulosa e opaca: poca', 'adesione, bolle e porosità')]
    for i, (t, r, ok, l1, l2) in enumerate(cases):
        x = 20 + i * 300
        b += panel(x, 60, 280, 290, t)
        b += mark(x + 250, 88, ok)
        cx, base = x + 140, 230
        b += '<rect x="%d" y="%d" width="200" height="10" rx="5" fill="#d9cfc6"/>' % (cx - 100, base)
        if i == 0:
            b += '<path d="M%d,%d Q%d,%d %d,%d Q%d,%d %d,%d Z" fill="#f8e8ee" stroke="%s"/>' % (cx - 85, base, cx - 20, base - 22, cx + 30, base - 18, cx + 80, base - 6, cx + 90, base, NAIL_S)
            b += '<path d="M%d,%d q4,14 0,22 q-4,-8 0,-22" fill="#f8e8ee" stroke="%s"/>' % (cx + 70, base + 8, NAIL_S)
        elif i == 1:
            b += '<path d="M%d,%d C%d,%d %d,%d %d,%d Z" fill="#f8e8ee" stroke="%s"/>' % (cx - 45, base, cx - 45, base - 70, cx + 45, base - 70, cx + 45, base, NAIL_S)
            b += '<ellipse cx="%d" cy="%d" rx="12" ry="7" fill="#fff"/>' % (cx - 14, base - 38)
        else:
            pts = []
            for k in range(13):
                a = math.pi * k / 12
                rr = 40 + (6 if k % 2 else -4)
                pts.append('%.1f,%.1f' % (cx - math.cos(a) * rr, base - math.sin(a) * rr * 0.9))
            b += '<polygon points="%s" fill="#efe4e8" stroke="%s"/>' % (' '.join(pts), NAIL_S)
            for k in range(14):
                b += '<circle cx="%d" cy="%d" r="2" fill="#cfbfc4"/>' % (cx - 28 + (k * 17) % 56, base - 8 - (k * 11) % 26)
        b += tool_brush(cx + 30, base - 85, -40, 90, '#f3eee6')
        b += text(cx, 285, r, 18, weight=800, fill=ACC2)
        b += mtext(cx, 310, [l1, l2], 13, fill=MUTED)
    return svg(920, 370, b, 'Perla di acrilico bagnata, media e asciutta')


@fig('smile-line.svg')
def smile():
    b = text(40, 40, 'French: la linea del sorriso (smile line)', 20, 'start', 800, ACC2)
    cases = [('Simmetrica', True, 0, 22), ('Asimmetrica', False, 14, 18), ('Piatta', False, 0, 3), ('A "V"', True, 0, -1)]
    for i, (t, ok, skew, d) in enumerate(cases):
        x = 20 + i * 225
        b += panel(x, 60, 210, 330, t)
        b += mark(x + 182, 88, ok)
        cx, yc = x + 105, 345
        hw, ys = 38, yc - 110
        extra = ''
        if d >= 0:
            fp = 'M%d,%d Q%d,%d %d,%d L%d,%d L%d,%d Z' % (cx - hw - 4, ys + d, cx + skew, ys - d - 2 + skew, cx + hw + 4, ys + d - skew, cx + hw + 4, 60, cx - hw - 4, 60)
        else:
            fp = 'M%d,%d L%d,%d L%d,%d L%d,%d L%d,%d Z' % (cx - hw - 4, ys + 20, cx, ys - 16, cx + hw + 4, ys + 20, cx + hw + 4, 60, cx - hw - 4, 60)
        extra = '<path d="%s" fill="#ffffff" clip-path="url(#CLIP)"/>' % fp
        f, p = finger_nail(cx, yc, hw=hw, nail_len=110, free_len=70, shape='squoval', smile=0, plate='#f6c9d4', free='#f6c9d4', finger_len=20, extra=extra, lunula=False)
        b += f
        b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-dasharray="4 4"/>' % (cx, ys - 85, cx, yc - 10, MUTED)
    b += text(470, 412, 'Controlla la simmetria guardando l\'unghia dal davanti e capovolgendo la mano della cliente.', 13.5, fill=MUTED)
    return svg(940, 425, b, 'Smile line del french: corretta ed errata')


@fig('baby-boomer.svg')
def bboom():
    b = text(40, 40, 'Baby boomer: sfumatura dal nude al bianco', 20, 'start', 800, ACC2)
    defs = ('<defs><linearGradient id="bb" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#f6c9d4"/>'
            '<stop offset=".45" stop-color="#f6c9d4"/><stop offset=".85" stop-color="#ffffff"/></linearGradient>'
            '<linearGradient id="bb2" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#f6c9d4"/>'
            '<stop offset=".62" stop-color="#f6c9d4"/><stop offset=".75" stop-color="#fbe9ee"/><stop offset="1" stop-color="#ffffff"/></linearGradient></defs>')
    steps = [('Base nude/rosa', None), ('Bianco sulla punta', 'url(#bb2)'), ('Sfuma verso la cuticola', 'url(#bb)')]
    for i, (t, g) in enumerate(steps):
        x = 20 + i * 300
        b += panel(x, 60, 280, 330, t, i + 1)
        cx, yc = x + 140, 350
        f, p = finger_nail(cx, yc, hw=42, nail_len=120, free_len=70, shape='mandorla', smile=0, plate='#f6c9d4', free='#f6c9d4',
                           free_grad=g, finger_len=25, lunula=False)
        b += f
        if i == 2:
            b += tool_brush(cx + 70, yc - 160, -30, 70, '#fff')
            b += '<rect x="%d" y="%d" width="38" height="26" rx="6" fill="#f3e3d0" stroke="#d6bf9f" transform="rotate(-20 %d %d)"/>' % (cx + 55, yc - 230, cx + 55, yc - 230)
    return svg(920, 410, defs + b, 'Baby boomer in tre passaggi')


@fig('refill.svg')
def refill():
    b = text(40, 40, 'Perché serve il refill (ogni 3–4 settimane)', 20, 'start', 800, ACC2)
    cases = [('Appena fatta', 0, 0.45, True, 'apex sopra il punto di stress'),
             ('Dopo 3–4 settimane', 42, 0.62, False, 'ricrescita + apex spostato in avanti'),
             ('Dopo il refill', 0, 0.45, True, 'struttura ribilanciata')]
    for i, (t, rg, apx, ok, sub) in enumerate(cases):
        x = 20 + i * 300
        b += panel(x, 60, 280, 260, t, i + 1)
        b += mark(x + 250, 88, ok)
        s, p = side_profile(x + 80, 210, w=180, stress=0.6, apex=apx, apex_h=24, tip_h=5, root_h=2 if not rg else 6, regrowth=rg)
        b += s
        b += '<circle cx="%.1f" cy="%.1f" r="4" fill="%s"/>' % (p['xs'], p['oy'] + 3, ERR)
        b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-dasharray="3 3"/>' % (p['ax'], p['ah'], p['ax'], p['oy'], ACC2)
        if rg:
            b += leader(x + 100, 210, x + 80, 140, 'ricrescita', 'middle', 13)
        b += text(x + 140, 305, sub, 13, weight=600, fill=OK if ok else ERR)
    b += text(470, 350, 'L\'unghia cresce ≈ 3 mm al mese: il peso si sposta in avanti e aumenta il rischio di rottura e sollevamento.', 13.5, fill=MUTED)
    return svg(940, 370, b, 'Ricrescita e refill: profilo prima e dopo')


@fig('rimozione.svg')
def removal():
    b = ''
    T = ['Opacizza il top', 'Cotone con acetone', 'Avvolgi: 10–15 min', 'Spingi via e nutri']
    for i, t in enumerate(T):
        x = 20 + i * 230
        b += panel(x, 20, 215, 300, t, i + 1)
        cx, yc = x + 107, 280
        if i == 2:
            b += ('<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Z" fill="#cfd4da" stroke="#9aa3ad"/>'
                  % (cx - 52, yc + 15, cx - 52, yc - 150, cx, yc - 200, cx + 52, yc - 150, cx + 52, yc + 15))
            for k in range(4):
                b += '<path d="M%d,%d L%d,%d" stroke="#eef1f4" stroke-width="3"/>' % (cx - 40, yc - 140 + k * 35, cx + 40, yc - 120 + k * 35)
            b += '<circle cx="%d" cy="80" r="18" fill="none" stroke="%s" stroke-width="2.5"/><path d="M%d,80 l0,-11 M%d,80 l8,5" stroke="%s" stroke-width="2.5"/>' % (cx + 70, ACC2, cx + 70, cx + 70, ACC2)
            continue
        f, p = finger_nail(cx, yc, hw=34, nail_len=110, free_len=40, shape='squoval', plate='#e46f8f', free='#e46f8f', finger_len=20, lunula=False)
        b += f
        if i == 0:
            b += tool_file(cx + 30, yc - 90, -70, 130, 18)
            b += text(cx, 308, 'togli la lucidità, non limare a fondo', 12, fill=MUTED)
        elif i == 1:
            b += '<ellipse cx="%d" cy="%d" rx="40" ry="34" fill="#ffffff" stroke="#d8d0cc"/>' % (cx, yc - 95)
            b += '<path d="M%d,%d q20,-10 40,0 q-20,10 -40,0" fill="#e8f3fb"/>' % (cx - 20, yc - 98)
        elif i == 3:
            b += tool_stick(cx - 8, yc - 115, -65, 120)
            b += '<circle cx="%d" cy="%d" r="7" fill="#f1d27a"/>' % (cx - 28, yc - 30)
            b += text(cx, 308, 'senza grattare né fare leva', 12, fill=ERR, weight=600)
    return svg(950, 340, b, 'Rimozione soak-off in quattro passaggi')


@fig('lifting.svg')
def lifting():
    b = text(40, 40, 'Sollevamento (lifting): dove nasce e perché', 20, 'start', 800, ACC2)
    extra = ('<path d="M%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="#fff" opacity=".85" clip-path="url(#CLIP)"/>'
             % (180 - 40, 400 - 14, 180, 400 - 50, 180 + 40, 400 - 14, 180 + 40, 400 - 34, 180, 400 - 70, 180 - 40, 400 - 34))
    extra += '<path d="M%d,%d L%d,%d L%d,%d Z" fill="#fff" opacity=".85" clip-path="url(#CLIP)"/>' % (180 + 46, 300, 180 + 30, 330, 180 + 46, 360)
    f, p = finger_nail(180, 400, hw=46, nail_len=150, free_len=55, shape='squoval', plate='#e9a7bd', free='#e9a7bd', finger_len=40, extra=extra, lunula=False)
    b += f
    b += leader(180, 360, 330, 360, 'Sollevamento in zona cuticola')
    b += leader(222, 330, 330, 300, 'Sollevamento laterale')
    causes = ['Cuticola/pterigio non rimossi', 'Olio o umidità sulla lamina', 'Disidratante o primer saltati',
              'Prodotto a contatto con la pelle', 'Bordo libero non sigillato', 'Perla troppo bagnata o asciutta',
              'Refill fatto in ritardo', 'Polimerizzazione incompleta']
    b += text(560, 95, 'Cause più frequenti', 16, 'start', 800)
    for i, c in enumerate(causes):
        y = 125 + i * 33
        b += '<circle cx="572" cy="%d" r="11" fill="%s"/>' % (y - 5, ACC)
        b += text(572, y, str(i + 1), 12, weight=800, fill='#fff')
        b += text(592, y, c, 14.5, 'start')
    b += '<rect x="550" y="400" width="320" height="56" rx="10" fill="#fbe7e4"/>'
    b += mtext(565, 423, ['Mai incollare sopra un sollevamento:', 'umidità e batteri (Pseudomonas) si infiltrano.'], 13.5, 'start', 600, ERR)
    return svg(900, 480, b, 'Sollevamento della ricostruzione e sue cause')


@fig('igiene.svg')
def hygiene():
    b = text(40, 40, 'I tre livelli di trattamento igienico', 20, 'start', 800, ACC2)
    levels = [('Detersione / sanificazione', 'Riduce sporco e carica microbica', 'mani, superfici, lime monouso', '#f8dfe7'),
              ('Disinfezione', 'Elimina la maggior parte dei patogeni', 'strumenti non sterilizzabili, superfici', '#eeaabf'),
              ('Sterilizzazione', 'Elimina ogni forma di vita, spore incluse', 'autoclave classe B (EN 13060), con tracciabilità', ACC)]
    for i, (t, d, u, c) in enumerate(levels):
        w = 760 - i * 160
        x = 450 - w / 2
        y = 290 - i * 95
        b += '<rect x="%.1f" y="%d" width="%d" height="82" rx="12" fill="%s"/>' % (x, y, w, c)
        fc = '#fff' if i == 2 else INK
        b += text(450, y + 28, t, 17, weight=800, fill=fc)
        b += text(450, y + 50, d, 13.5, fill=fc)
        b += text(450, y + 70, 'Per: ' + u, 13, fill=fc, style='italic')
    b += arrow(860, 360, 860, 110, MUTED, 1.6)
    b += text(850, 100, 'più efficace', 13, 'end', fill=MUTED)
    return svg(900, 390, arrow_defs() + b, 'Detersione, disinfezione e sterilizzazione')


@fig('lampade.svg')
def lamps():
    b = text(40, 40, 'Lampade: lunghezze d\'onda di emissione', 20, 'start', 800, ACC2)
    x0, x1, base = 80, 820, 300

    def X(nm):
        return x0 + (nm - 290) / (460 - 290) * (x1 - x0)
    defs = '<defs><linearGradient id="vis" x1="0" x2="1"><stop offset="0" stop-color="#7b4bd6"/><stop offset=".5" stop-color="#3f6fe0"/><stop offset="1" stop-color="#2bb0c9"/></linearGradient></defs>'
    b += '<rect x="%.1f" y="150" width="%.1f" height="150" fill="#f5f1fb"/>' % (X(400), X(460) - X(400))
    b += text(X(430), 170, 'luce visibile →', 13, fill=MUTED)

    for i, (col, lab) in enumerate([('#7b4bd6', 'UV classica: ~300–410 nm, picco ~365 nm'), ('#3f6fe0', 'LED: ~375–425 nm, picco ~385–405 nm'),
                                    (ACC, 'Dual UV/LED: due picchi, es. 365 + 405 nm')]):
        b += '<rect x="90" y="%d" width="22" height="6" rx="3" fill="%s"/>' % (78 + i * 24, col)
        b += text(120, 85 + i * 24, lab, 13.5, 'start', 600)

    def curve(peak, sd, h, col, lab):
        pts = []
        for nm in range(290, 461, 2):
            y = base - h * math.exp(-((nm - peak) ** 2) / (2 * sd * sd))
            pts.append('%.1f,%.1f' % (X(nm), y))
        return ('<polyline points="%s" fill="none" stroke="%s" stroke-width="3"/>' % (' '.join(pts), col)
                + text(X(peak), base - h - 10, lab, 14, weight=700, fill=col))
    b += curve(366, 20, 130, '#7b4bd6', '')
    b += curve(395, 9, 110, '#3f6fe0', '')
    b += curve(366, 6, 80, ACC, '')
    b += curve(405, 6, 80, ACC, '')
    b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s"/>' % (x0, base, x1, base, INK)
    for nm in range(300, 461, 20):
        b += '<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s"/>' % (X(nm), base, X(nm), base + 6, INK)
        b += text(X(nm), base + 22, str(nm), 12.5, fill=MUTED)
    b += text((x0 + x1) / 2, base + 45, 'nm', 13, fill=MUTED)
    b += text(450, 380, 'Conta l\'abbinamento lampada ↔ fotoiniziatori del gel, non i watt: usa la lampada del tuo sistema.', 14, weight=600)
    return svg(900, 400, defs + b, 'Spettri di emissione delle lampade UV e LED')


@fig('limatura-direzioni.svg')
def file_dir():
    b = ''
    T = ['Lati: lima parallela al solco', 'Punta: dai lati verso il centro', 'Superficie: segui la curva']
    for i, t in enumerate(T):
        x = 20 + i * 300
        b += panel(x, 20, 280, 320, t, i + 1)
        cx, yc = x + 140, 300
        f, p = finger_nail(cx, yc, hw=38, nail_len=110, free_len=60, shape='squoval', finger_len=20)
        b += f
        ys, yt = p['y_s'], p['y_t']
        if i == 0:
            b += tool_file(cx + 46, ys + 5, -90, 120, 16)
            b += arrow(cx + 75, ys + 40, cx + 75, ys - 40, ACC2, 2)
        elif i == 1:
            b += tool_file(cx, yt - 12, 0, 130, 16)
            b += arrow(cx - 70, yt - 34, cx - 10, yt - 34)
            b += arrow(cx + 70, yt - 34, cx + 10, yt - 34)
        else:
            for k in (-20, 0, 20):
                b += ('<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="%s" stroke-width="2" marker-end="url(#ar)"/>'
                      % (cx + k, yc - 30, cx + k * 1.2, (yc + yt) / 2, cx + k, yt + 10, ACC2))
        b += text(cx, 330, ['evita di limare dentro il solco', 'una direzione, no "sega"', 'dalla cuticola verso la punta'][i], 12.5, fill=MUTED)
    return svg(920, 360, arrow_defs() + b, 'Direzioni corrette di limatura')


@fig('sistemi.svg')
def systems():
    b = text(40, 40, 'I sistemi di ricostruzione a confronto', 20, 'start', 800, ACC2)
    items = [('Gel UV/LED', 'flacone/vasetto + lampada', ['nessun odore', 'autolivellante', 'rischio picco di calore']),
             ('Acrilico', 'liquido (monomero) + polvere', ['il più resistente', 'ottimo per lunghezze', 'odore e vapori']),
             ('Polygel', 'pasta + slip solution + lampada', ['tempo di lavoro libero', 'leggero', 'curva di apprendimento']),
             ('Fibra / seta', 'tessuto + resina + attivatore', ['sottile e naturale', 'riparazioni', 'meno strutturale'])]
    for i, (t, comp, pts) in enumerate(items):
        x = 20 + i * 225
        b += panel(x, 60, 210, 300, t)
        cx = x + 105
        if i == 0:
            b += '<rect x="%d" y="110" width="60" height="80" rx="10" fill="%s"/><rect x="%d" y="100" width="40" height="18" rx="4" fill="#4b3a40"/>' % (cx - 30, GEL, cx - 20)
        elif i == 1:
            b += '<path d="M%d,110 l40,0 l-6,80 l-28,0 z" fill="#e8f3fb" stroke="#9cc3dc"/><rect x="%d" y="140" width="50" height="50" rx="8" fill="#f8e8ee" stroke="%s"/>' % (cx - 50, cx + 5, NAIL_S)
        elif i == 2:
            b += '<rect x="%d" y="110" width="22" height="80" rx="6" fill="%s"/><path d="M%d,110 l11,-14 l11,14 z" fill="#4b3a40"/>' % (cx - 11, GEL, cx - 11)
        else:
            b += ''.join('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#d8cbb5" stroke-width="2"/>' % (cx - 35, 110 + k * 10, cx + 35, 110 + k * 10) for k in range(8))
            b += ''.join('<line x1="%d" y1="110" x2="%d" y2="180" stroke="#d8cbb5" stroke-width="2"/>' % (cx - 35 + k * 10, cx - 35 + k * 10) for k in range(8))
        b += text(cx, 218, comp, 12.5, fill=MUTED)
        for k, pt in enumerate(pts):
            col = ERR if k == 2 else OK
            b += text(cx, 255 + k * 26, ('− ' if k == 2 else '+ ') + pt, 13.5, weight=600, fill=col)
    return svg(940, 380, b, 'Confronto tra gel, acrilico, polygel e fibra')


@fig('problemi.svg')
def problems():
    b = text(40, 40, 'Riconosci il difetto', 20, 'start', 800, ACC2)
    names = [('Crepa / rottura', 'apex assente o mal posizionato'), ('Bolle', 'gel agitato, perla asciutta'),
             ('Grinze', 'strato troppo spesso'), ('Ingiallimento', 'top non polimerizzato, UV')]
    for i, (n, sub) in enumerate(names):
        x = 20 + i * 225
        b += panel(x, 60, 210, 320, n)
        cx, yc = x + 105, 330
        extra = ''
        plate = '#f2b6c6'
        if i == 0:
            extra = '<path d="M%d,%d l12,18 l-8,10 l14,20 l-6,12" stroke="%s" stroke-width="2.5" fill="none"/>' % (cx - 22, yc - 160, INK)
        elif i == 1:
            extra = ''.join('<circle cx="%d" cy="%d" r="%d" fill="#fff" opacity=".9" stroke="#d48aa2"/>' % (cx - 20 + (k * 13) % 44, yc - 150 + (k * 29) % 110, 3 + k % 3 * 2) for k in range(10))
        elif i == 2:
            extra = ''.join('<path d="M%d,%d q8,-6 16,0 q8,6 16,0 q8,-6 16,0" stroke="#c46784" stroke-width="2" fill="none" clip-path="url(#CLIP)"/>' % (cx - 30, yc - 170 + k * 18) for k in range(7))
        else:
            plate = '#f2dfa8'
        f, p = finger_nail(cx, yc, hw=40, nail_len=130, free_len=50, shape='squoval', plate=plate, free=plate, finger_len=20, extra=extra, lunula=False)
        b += f
        b += text(cx, 370, sub, 12.5, fill=MUTED)
    return svg(940, 395, b, 'Difetti comuni: crepa, bolle, grinze, ingiallimento')


@fig('nail-art.svg')
def nailart():
    b = text(40, 40, 'Tecniche base di nail art', 20, 'start', 800, ACC2)
    T = [('Dotting', 'puntini con il dotter'), ('Striping', 'linee con pennello fine'), ('Incapsulato', 'glitter tra due strati'), ('Stamping', 'disegno da piastra')]
    for i, (t, sub) in enumerate(T):
        x = 20 + i * 225
        b += panel(x, 60, 210, 320, t)
        cx, yc = x + 105, 330
        if i == 0:
            extra = ''.join('<circle cx="%d" cy="%d" r="%d" fill="#fff"/>' % (cx + dx, yc + dy, r) for dx, dy, r in
                            [(0, -150, 9), (-16, -125, 6), (16, -125, 6), (0, -100, 5), (-22, -175, 4), (22, -175, 4), (0, -190, 3)])
        elif i == 1:
            extra = ''.join('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#fff" stroke-width="2.5" clip-path="url(#CLIP)"/>' % (cx - 60 + k * 22, yc - 220, cx - 10 + k * 22, yc - 70) for k in range(5))
        elif i == 2:
            rng = random.Random(7)
            extra = ''
            for k in range(40):
                gx, gy = cx + rng.uniform(-38, 38), yc + rng.uniform(-230, -60)
                extra += '<rect x="%.1f" y="%.1f" width="5" height="5" fill="%s" transform="rotate(%d %.1f %.1f)"/>' % (
                    gx, gy, ['#d4af37', '#ffffff', '#9a9aa6'][k % 3], rng.randint(0, 90), gx + 2.5, gy + 2.5)
        else:
            extra = ''.join('<path d="M%d,%d c-10,-14 10,-22 0,-6 c-10,-16 10,-16 0,6" stroke="#fff" stroke-width="2" fill="none" clip-path="url(#CLIP)"/>' % (cx - 20 + (k % 3) * 20, yc - 180 + (k // 3) * 40) for k in range(9))
        extra = '<g clip-path="url(#CLIP)">' + extra.replace(' clip-path="url(#CLIP)"', '') + '</g>'
        f, p = finger_nail(cx, yc, hw=40, nail_len=130, free_len=55, shape='mandorla', plate=['#c2577a', '#3b2a30', '#f6c9d4', '#8e3b5a'][i],
                           free=['#c2577a', '#3b2a30', '#f6c9d4', '#8e3b5a'][i], finger_len=20, extra=extra, lunula=False)
        b += f
        b += text(cx, 372, sub, 12.5, fill=MUTED)
    return svg(940, 390, b, 'Dotting, striping, incapsulato e stamping')


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, f in FIGS.items():
        with open(os.path.join(OUT, name), 'w', encoding='utf-8') as fh:
            fh.write(f())
    print('Generate %d illustrazioni in %s' % (len(FIGS), os.path.normpath(OUT)))


if __name__ == '__main__':
    main()
