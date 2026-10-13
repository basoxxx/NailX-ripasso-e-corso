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


# ================================================================= TUTORIAL PASSO-PASSO
def steps_fig(title, labels, cols, pw, ph, draw, desc, top=60):
    """Griglia di pannelli numerati; draw(i, x, y) restituisce il contenuto del pannello i."""
    rows = (len(labels) + cols - 1) // cols
    W = 20 + cols * (pw + 14) + 6
    H = top + rows * (ph + 14) + 6
    b = text(20, 38, title, 20, 'start', 800, ACC2)
    for i, lab in enumerate(labels):
        x = 20 + (i % cols) * (pw + 14)
        y = top + (i // cols) * (ph + 14)
        pc = uid('p')
        b += '<defs><clipPath id="%s"><rect x="%d" y="%d" width="%d" height="%d" rx="16"/></clipPath></defs>' % (pc, x, y, pw, ph)
        b += panel(x, y, pw, ph, lab, i + 1)
        b += '<g clip-path="url(#%s)">%s</g>' % (pc, draw(i, x, y))
    return svg(W, H, arrow_defs() + b, desc)


def lamp(cx, y, w=120, label=''):
    """Lampada vista di lato (cupola) con luce viola; y = piano d'appoggio."""
    s = ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f" fill="#f4f1f8" stroke="#8a7d9e" stroke-width="2"/>'
         % (cx - w / 2, y, cx - w / 2, y - 45, cx, y - 95, cx + w / 2, y - 45, cx + w / 2, y))
    for k in (-0.3, 0, 0.3):
        s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#9a6be0" stroke-width="2" opacity=".55" stroke-dasharray="4 4"/>' % (
            cx + k * w * 0.4, y - 66, cx + k * w * 0.9, y - 14)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="8" rx="4" fill="#8a7d9e"/>' % (cx - w / 2 - 6, y, w + 12)
    if label:
        s += text(cx, y - 72, label, 13, weight=800, fill='#6b4fa0')
    return s


def timer(x, y, label):
    return ('<circle cx="%.1f" cy="%.1f" r="15" fill="#fff" stroke="%s" stroke-width="2"/>'
            '<path d="M%.1f,%.1f l0,-9 M%.1f,%.1f l6,4" stroke="%s" stroke-width="2"/>' % (x, y, ACC2, x, y, x, y, ACC2)
            + text(x + 22, y + 5, label, 13, 'start', 700, ACC2))


def form_top(cx, ys, w=80, h=130):
    s = ('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f A%.1f,%.1f 0 0 0 %.1f,%.1f Z" fill="#f6e7a8" stroke="#d8c26a"/>'
         % (cx - w, ys + 36, cx - w, ys - h, cx + w, ys - h, cx + w, ys + 36, cx + 46, ys + 36, 46, 48, cx - 46, ys + 36))
    for k in range(1, 5):
        s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#d8c26a"/>' % (cx - w + 8, ys - k * 26 + 6, cx + w - 8, ys - k * 26 + 6)
    s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-dasharray="4 4"/>' % (cx, ys - h, cx, ys - 8, ACC2)
    return s


def bead(cx, cy, r, col='#ffffff', stroke=NAIL_S):
    return ('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s" stroke="%s" stroke-width="1.4"/>'
            '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="#fff" opacity=".8"/>'
            % (cx, cy, r, r * 0.8, col, stroke, cx - r * 0.35, cy - r * 0.3, r * 0.28, r * 0.18))


def drop(cx, cy, col='#f1d27a'):
    return '<path d="M%.1f,%.1f q8,12 0,18 q-8,-6 0,-18 z" fill="%s" stroke="#c9a54a"/>' % (cx, cy - 9, col)


def sparkle(cx, cy, r=8):
    return ('<path d="M%.1f,%.1f L%.1f,%.1f M%.1f,%.1f L%.1f,%.1f" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/>'
            % (cx - r, cy, cx + r, cy, cx, cy - r, cx, cy + r))


@fig('tut-gel-cartina.svg')
def tut_gel():
    labels = ['Prepara e primer', 'Applica la cartina', 'Base sottile', 'Allunga in zona 1',
              'Perla in zona 2 (apex)', 'Capovolgi 5–10 s', 'Togli cartina e lima', 'Cleaner e top']
    GELC = '#f6d6df'

    def d(i, x, y):
        cx, yb = x + 110, y + 255
        s = ''
        if i in (0, 2):
            f, p = finger_nail(cx, yb, hw=30, nail_len=90, free_len=10, shape='tonda', finger_len=18,
                               plate=NAIL if i == 0 else '#f3b3c6')
            s += f
            if i == 0:
                s += tool_brush(cx + 14, yb - 70, -50, 70, '#f1e3a0')
            else:
                s += timer(x + 40, y + 70, 'LED 30–60 s')
        elif i in (1, 3):
            ys = yb - 90
            s += form_top(cx, ys)
            if i == 3:
                s += ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5" opacity=".95"/>'
                      % (cx - 30, ys + 4, cx - 30, ys - 74, cx, ys - 80, cx + 30, ys - 74, cx + 30, ys + 4, GELC, NAIL_S))
                s += tool_brush(cx + 40, ys - 60, -40, 60, GEL)
            f, p = finger_nail(cx, yb, hw=30, nail_len=90, free_len=8, shape='tonda', finger_len=18)
            s += f
        elif i in (4, 5):
            sp, p = side_profile(x + 75, y + 170, w=130, stress=0.55, apex=0.45, apex_h=24 if i == 5 else 18, tip_h=5, root_h=2, gap=6)
            if i == 4:
                s += sp + bead(p['ax'], p['ah'] - 10, 13, GEL)
                s += text(cx, y + 230, 'il gel più spesso al centro', 12.5, fill=MUTED)
            else:
                s += '<g transform="rotate(180 %.1f %.1f)">%s</g>' % (cx, y + 175, sp)
                s += ('<path d="M%.1f,%.1f A50,50 0 1 1 %.1f,%.1f" fill="none" stroke="%s" stroke-width="2" marker-end="url(#ar)"/>'
                      % (cx - 60, y + 90, cx + 60, y + 90, ACC2))
                s += text(cx, y + 240, 'il gel scende verso l\'apex', 12.5, fill=MUTED)
        elif i == 6:
            f, p = finger_nail(cx, yb, hw=30, nail_len=90, free_len=70, shape='squoval', finger_len=18, plate='#f3b3c6', free=GELC)
            s += f + tool_file(cx + 42, yb - 140, -80, 120, 16)
        else:
            f, p = finger_nail(cx, yb, hw=30, nail_len=90, free_len=70, shape='squoval', finger_len=18, plate='#f3b3c6', free=GELC)
            s += f + '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round"/>' % (
                cx - 14, yb - 60, cx - 18, yb - 110, cx - 10, yb - 150)
            s += sparkle(cx + 18, yb - 140) + sparkle(cx + 50, yb - 175, 6)
        return s
    return steps_fig('Tutorial: ricostruzione in gel su cartina', labels, 4, 220, 270, d, 'Ricostruzione in gel su cartina in otto passaggi')


@fig('tut-acrilico.svg')
def tut_acr():
    labels = ['Perla in zona 1', 'Picchietta e modella', 'Perla in zona 2', 'Zona 3 sottilissima', 'Pinching (curva a C)', 'Lima e rifinisci']

    def d(i, x, y):
        cx, yb = x + 140, y + 255
        ys = yb - 90
        s = ''
        if i < 4:
            s += form_top(cx, ys)
            if i >= 1:
                s += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="#fffdfd" stroke="%s" stroke-width="1.4"/>'
                      % (cx - 32, ys + 10, cx, ys - 6, cx + 32, ys + 10, cx + 32, ys - 70, cx, ys - 78, cx - 32, ys - 70, NAIL_S))
            f, p = finger_nail(cx, yb, hw=30, nail_len=90, free_len=6, shape='tonda', finger_len=18)
            s += f
            if i == 0:
                s += bead(cx, ys - 40, 20, '#ffffff')
            elif i == 1:
                s += tool_brush(cx + 35, ys - 45, -35, 70, '#f3eee6')
                s += arrow(cx - 60, ys - 40, cx - 36, ys - 40, MUTED, 1.5) + arrow(cx + 70, ys - 10, cx + 40, ys - 10, MUTED, 1.5)
            elif i == 2:
                s += bead(cx, ys + 30, 18, '#f9dbe4')
            else:
                s += bead(cx, yb - 22, 11, '#f9dbe4')
                s += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="%s" stroke-width="1.6" stroke-dasharray="3 3" fill="none"/>' % (
                    cx - 30, yb - 30, cx, yb - 48, cx + 30, yb - 30, ERR)
                s += text(cx, y + 64, '≈1,5 mm dalla pelle', 12.5, weight=700, fill=ERR)
        elif i == 4:
            s += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="12" stroke-linecap="round"/>' % (
                cx - 70, y + 170, cx, y + 90, cx + 70, y + 170, ACC)
            s += arrow(cx - 115, y + 150, cx - 82, y + 160) + arrow(cx + 115, y + 150, cx + 82, y + 160)
            s += text(cx, y + 210, 'vista dal bordo libero', 12.5, fill=MUTED)
            s += text(cx, y + 230, 'quando il prodotto è ancora morbido', 12.5, fill=MUTED)
        else:
            sp, p = side_profile(x + 90, y + 170, w=170, stress=0.6, apex=0.47, apex_h=22, tip_h=5, root_h=2, gap=6, product='#f9dbe4')
            s += sp + tool_file(cx + 10, y + 120, -10, 140, 16)
            s += text(cx, y + 255, 'controlla l\'apex di profilo', 12.5, fill=MUTED)
        return s
    return steps_fig('Tutorial: ricostruzione in acrilico su cartina', labels, 3, 280, 270, d, 'Ricostruzione in acrilico in sei passaggi')


@fig('tut-semipermanente.svg')
def tut_semi():
    labels = ['Preparazione', 'Base + lampada', 'Colore: 1° strato', 'Colore: 2° strato', 'Top e sigilla il bordo', 'Cleaner e olio']
    COL = '#c2577a'

    def d(i, x, y):
        cx, yb = x + 140, y + 255
        plate = [NAIL, '#f3b3c6', '#d98aa3', COL, COL, COL][i]
        f, p = finger_nail(cx, yb, hw=32, nail_len=110, free_len=14, shape='tonda', finger_len=18, plate=plate, free=plate if i else FREE, lunula=i == 0)
        s = f
        if i == 0:
            s += tool_file(cx + 40, yb - 90, -70, 110, 14)
        elif i == 1:
            s += timer(x + 40, y + 70, '30–60 s')
        elif i == 2:
            s += text(cx, y + 64, 'strato sottile, non colorare la pelle', 12.5, fill=MUTED)
        elif i == 3:
            s += timer(x + 40, y + 70, 'in lampada')
        elif i == 4:
            s += tool_brush(cx + 8, p['y_t'] - 4, -20, 70, '#fff')
            s += leader(cx, p['y_t'] + 4, cx + 70, y + 72, 'passa sul bordo', 'middle', 12.5)
            s += sparkle(cx - 12, yb - 80)
        else:
            s += drop(cx, yb - 30) + sparkle(cx - 12, yb - 80)
        return s
    return steps_fig('Tutorial: semipermanente', labels, 3, 280, 270, d, 'Applicazione del semipermanente in sei passaggi')


@fig('tut-soft-gel-tips.svg')
def tut_sgt():
    labels = ['Scegli la misura', 'Gel adesivo nel tip', 'Applica a 45°, flash', 'Lampada e rifinisci']

    def d(i, x, y):
        cx, yb = x + 110, y + 270
        s = ''
        if i == 0:
            f, p = finger_nail(cx, yb, hw=30, nail_len=90, free_len=6, shape='tonda', finger_len=20)
            s += f + arrow(cx - 30, y + 80, cx + 30, y + 80, ACC2, 1.8, True) + text(cx, y + 70, 'da solco a solco', 12.5, weight=600)
        elif i == 1:
            tip = nail_outline(cx, y + 230, y + 150, y + 70, 32, 'mandorla')
            s += '<path d="%s" fill="#fbeaf0" stroke="%s" stroke-width="1.6"/>' % (tip, NAIL_S)
            s += '<ellipse cx="%.1f" cy="%.1f" rx="22" ry="30" fill="%s" opacity=".75"/>' % (cx, y + 195, GEL)
            s += tool_brush(cx + 40, y + 180, -40, 60, GEL)
        elif i == 2:
            s += ('<path d="M%d,%d L%d,%d C%d,%d %d,%d %d,%d L%d,%d Z" fill="%s" stroke="%s"/>'
                  % (x + 10, y + 200, x + 120, y + 200, x + 160, y + 200, x + 160, y + 240, x + 120, y + 250, x + 10, y + 250, SKIN, SKIN_D))
            s += '<path d="M%d,%d L%d,%d" stroke="%s" stroke-width="4"/>' % (x + 50, y + 199, x + 140, y + 199, NAIL_S)
            s += '<g transform="translate(%d,%d) rotate(-38)"><rect x="0" y="-5" width="120" height="8" rx="3" fill="#fbeaf0" stroke="%s"/></g>' % (x + 52, y + 196, NAIL_S)
            s += arrow(x + 170, y + 90, x + 175, y + 160)
            s += text(cx, y + 70, 'parti dalla zona cuticolare', 12.5, fill=MUTED)
        else:
            s += lamp(cx, y + 230, 150, 'LED 60 s')
            s += '<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Z" fill="%s" stroke="%s"/>' % (x - 5, y + 218, cx + 40, y + 212, cx + 62, y + 212, cx + 64, y + 222, x - 5, y + 230, SKIN, SKIN_D)
            s += text(cx, y + 262, 'poi lima, cleaner e top', 12.5, fill=MUTED)
        return s
    return steps_fig('Tutorial: soft gel tips', labels, 4, 220, 290, d, 'Applicazione dei soft gel tips in quattro passaggi')


@fig('tut-french.svg')
def tut_french():
    labels = ['Segna i punti laterali', 'Traccia la curva', 'Riempi la punta', 'Sigilla con il top']

    def d(i, x, y):
        cx, yb = x + 110, y + 280
        hw, ys = 32, yb - 100
        extra = ''
        if i >= 1:
            path = 'M%d,%d Q%d,%d %d,%d' % (cx - hw - 3, ys + 18, cx, ys - 22, cx + hw + 3, ys + 18)
            if i == 1:
                extra = '<path d="%s" fill="none" stroke="#fff" stroke-width="4" clip-path="url(#CLIP)"/>' % path
            else:
                extra = '<path d="%s L%d,%d L%d,%d Z" fill="#fff" clip-path="url(#CLIP)"/>' % (path, cx + hw + 3, y + 40, cx - hw - 3, y + 40)
        f, p = finger_nail(cx, yb, hw=hw, nail_len=100, free_len=60, shape='squoval', smile=0, plate='#f6c9d4', free='#f6c9d4', finger_len=10, extra=extra, lunula=False)
        s = f
        if i == 0:
            s += '<circle cx="%d" cy="%d" r="4" fill="#fff" stroke="%s"/><circle cx="%d" cy="%d" r="4" fill="#fff" stroke="%s"/>' % (cx - hw + 3, ys + 16, NAIL_S, cx + hw - 3, ys + 16, NAIL_S)
            s += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-dasharray="3 3"/>' % (cx - hw - 20, ys + 16, cx + hw + 20, ys + 16, ACC2)
            s += text(cx, y + 64, 'stessa altezza sui due lati', 12.5, fill=MUTED)
        elif i == 1:
            s += tool_brush(cx + 18, ys - 14, -50, 70, '#fff')
        elif i == 3:
            s += sparkle(cx - 10, ys - 40) + sparkle(cx + 14, yb - 60, 6)
        return s
    return steps_fig('Tutorial: french con la smile line', labels, 4, 220, 300, d, 'French in quattro passaggi')


@fig('tut-fibra.svg')
def tut_fibra():
    labels = ['Taglia la fibra', 'Stendi la resina', 'Attivatore a pennello', 'Lima e sigilla']

    def d(i, x, y):
        cx, yb = x + 110, y + 270
        s = ''
        mesh = ''.join('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#cdbb9c" stroke-width="1.2" clip-path="url(#CLIP)"/>' % (cx - 40, yb - 160 + k * 8, cx + 40, yb - 160 + k * 8) for k in range(22))
        mesh += ''.join('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#cdbb9c" stroke-width="1.2" clip-path="url(#CLIP)"/>' % (cx - 40 + k * 8, yb - 170, cx - 40 + k * 8, yb - 20) for k in range(11))
        if i == 0:
            s += '<rect x="%d" y="%d" width="90" height="120" fill="#f8f2e6" stroke="#cdbb9c"/>' % (cx - 45, y + 80)
            s += ''.join('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#cdbb9c"/>' % (cx - 45, y + 80 + k * 10, cx + 45, y + 80 + k * 10) for k in range(12))
            s += '<path d="M%d,%d Q%d,%d %d,%d" stroke="%s" stroke-width="2" stroke-dasharray="5 4" fill="none"/>' % (cx - 30, y + 190, cx, y + 70, cx + 30, y + 190, ERR)
            s += text(cx, y + 230, 'a forma dell\'unghia,', 12.5, fill=MUTED) + text(cx, y + 248, '≈1,5 mm dalla pelle', 12.5, fill=MUTED)
            return s
        plate = '#f7d3dd'
        f, p = finger_nail(cx, yb, hw=32, nail_len=110, free_len=40, shape='squoval', finger_len=10, plate=plate, free=plate, extra=mesh if i < 3 else '', lunula=False)
        s += f
        if i == 1:
            s += tool_brush(cx + 30, yb - 120, -50, 60, '#fdf2c4')
        elif i == 2:
            s += tool_brush(cx + 30, yb - 120, -50, 60, '#cfe9f7')
            s += text(cx, y + 64, 'poco prodotto: evita il calore', 12.5, fill=ERR, weight=600)
        else:
            s += tool_file(cx + 42, yb - 110, -80, 110, 14) + sparkle(cx - 12, yb - 90)
        return s
    return steps_fig('Tutorial: rinforzo in fibra di vetro o seta', labels, 4, 220, 290, d, 'Applicazione della fibra in quattro passaggi')


@fig('refill-step.svg')
def refill_steps():
    labels = ['Ricrescita visibile', 'Accorcia e assottiglia', 'Prepara la ricrescita', 'Ricostruisci e sigilla']

    def d(i, x, y):
        cx, yb = x + 110, y + 280
        GELC = '#e9a7bd'
        ext = ''
        if i < 3:
            ext = '<rect x="%d" y="%d" width="80" height="34" fill="%s" clip-path="url(#CLIP)"/>' % (cx - 40, yb - 34, NAIL)
            ext += '<path d="M%d,%d Q%d,%d %d,%d" stroke="%s" stroke-width="2" fill="none" clip-path="url(#CLIP)"/>' % (cx - 40, yb - 30, cx, yb - 44, cx + 40, yb - 30, NAIL_S)
        free_len = 70 if i == 0 else 50
        f, p = finger_nail(cx, yb, hw=32, nail_len=110, free_len=free_len, shape='squoval', finger_len=10,
                           plate=GELC if i != 1 else '#efbccb', free=GELC if i != 1 else '#efbccb', extra=ext, lunula=False)
        s = f
        if i == 0:
            s += leader(cx + 20, yb - 22, cx, y + 70, 'ricrescita (≈3 mm/mese)', 'middle', 12)
        elif i == 1:
            s += tool_file(cx + 44, yb - 120, -80, 110, 14)
            s += text(cx, y + 64, 'via ogni parte sollevata', 12.5, fill=ERR, weight=600)
        elif i == 2:
            s += tool_pusher(cx + 6, yb - 34, -60, 100)
        else:
            s += sparkle(cx - 10, yb - 100)
            s += text(cx, y + 64, 'apex di nuovo al suo posto', 12.5, fill=OK, weight=600)
        return s
    return steps_fig('Tutorial: il refill passo passo', labels, 4, 220, 300, d, 'Refill in quattro passaggi')


@fig('forme-limatura-step.svg')
def shape_steps():
    labels = ['Parti da una quadrata', 'Traccia l\'asse', 'Affina i lati', 'Arrotonda la punta']

    def d(i, x, y):
        cx, yb = x + 110, y + 280
        sh = ['quadrata', 'quadrata', 'ballerina', 'mandorla'][i]
        f, p = finger_nail(cx, yb, hw=32, nail_len=100, free_len=80, shape=sh, finger_len=10)
        s = f
        target = nail_outline(cx, yb, yb - 100, yb - 180, 32, 'mandorla')
        if i < 3:
            tc = uid()
            s += '<defs><clipPath id="%s"><rect x="%d" y="%d" width="%d" height="%d"/></clipPath></defs>' % (tc, x, y, 220, 280 - 100 - 6)
            s += '<path d="%s" fill="none" stroke="%s" stroke-width="1.6" stroke-dasharray="5 4" clip-path="url(#%s)"/>' % (target, ACC2, tc)
        if i == 1:
            s += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.6"/>' % (cx, yb - 190, cx, yb - 20, ERR)
        if i == 2:
            s += tool_file(cx + 30, yb - 150, -70, 110, 14)
        if i == 3:
            s += tool_file(cx, yb - 192, 0, 90, 14)
        s += text(cx, y + 64, ['tratteggio = forma finale', 'controlla la simmetria', 'stesso angolo per i 2 lati', 'punta centrata sull\'asse'][i], 12.5, fill=MUTED)
        return s
    return steps_fig('Come limare una mandorla partendo da una quadrata', labels, 4, 220, 300, d, 'Limatura della forma a mandorla in quattro passaggi')


@fig('cuticola.svg')
def cuticle():
    b = text(20, 38, 'Zona cuticolare: cosa si tocca e cosa no', 20, 'start', 800, ACC2)
    for k, (t, ok) in enumerate([('Arretra l\'eponichio con delicatezza', True), ('Rimuovi il pterigio dalla lamina', True), ('Non tagliare la pelle viva', False)]):
        x = 20 + k * 300
        b += panel(x, 60, 285, 270, t if len(t) < 30 else t)
        b += mark(x + 258, 120, ok)
        ox, oy = x + 120, 220
        b += ('<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d L%d,%d Z" fill="%s" stroke="%s"/>'
              % (x + 15, oy - 30, ox - 5, oy - 30, ox + 22, oy - 30, ox + 26, oy - 4, ox + 140, oy, x + 15, oy + 60, SKIN, SKIN_D))
        b += '<path d="M%d,%d L%d,%d" stroke="%s" stroke-width="6" stroke-linecap="round"/>' % (ox - 20, oy - 2, ox + 150, oy + 2, NAIL_S)
        if k == 0:
            b += tool_pusher(ox + 32, oy - 12, -30, 110)
            b += arrow(ox + 60, oy - 40, ox + 30, oy - 40)
        elif k == 1:
            b += '<path d="M%d,%d L%d,%d" stroke="#fff" stroke-width="4"/>' % (ox + 28, oy - 4, ox + 60, oy - 3)
            b += tool_stick(ox + 44, oy - 8, -20, 110)
        else:
            b += ('<g transform="translate(%d,%d) rotate(-30)"><path d="M0,0 L60,-6 L60,6 Z" fill="#9aa3ad"/><path d="M0,0 L60,10 L60,20 Z" fill="#7d8792"/></g>' % (ox + 10, oy - 40))
            b += '<circle cx="%d" cy="%d" r="22" fill="none" stroke="%s" stroke-width="3"/>' % (ox + 12, oy - 22, ERR)
        b += text(x + 142, 315, ['lo spingicuticole quasi piatto, senza forza', 'solo pelle morta, a lama piatta', 'eponichio e pieghe sono vivi: rischio infezioni'][k], 12, fill=MUTED)
    return svg(925, 345, arrow_defs() + b, 'Gestione corretta della zona cuticolare')


@fig('lampada-posizione.svg')
def lamp_pos():
    b = text(20, 38, 'In lampada: posizione e picco di calore', 20, 'start', 800, ACC2)
    b += panel(20, 60, 285, 280, 'Mano piatta, dita dentro')
    b += mark(278, 88, True)
    b += lamp(162, 280, 200)
    b += '<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Z" fill="%s" stroke="%s"/>' % (40, 270, 200, 262, 230, 262, 232, 272, 40, 280, SKIN, SKIN_D)
    b += text(162, 325, 'il pollice si polimerizza a parte', 12.5, fill=MUTED)
    b += panel(320, 60, 285, 280, 'Dita fuori o inclinate')
    b += mark(578, 88, False)
    b += lamp(462, 280, 200)
    b += '<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="%s" stroke="%s" transform="rotate(-14 420 270)"/>' % (330, 266, 450, 258, 452, 270, 330, 280, SKIN, SKIN_D)
    b += text(462, 325, 'zone in ombra = gel non polimerizzato', 12.5, fill=ERR, weight=600)
    # grafico flash and pull
    b += panel(620, 60, 300, 280, '"Flash and pull"')
    ox, oy = 650, 290
    b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s"/><line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s"/>' % (ox, oy, ox + 250, oy, INK, ox, oy, ox, 110, INK)
    b += text(ox + 125, oy + 20, 'tempo', 12, fill=MUTED)
    b += '<text x="%d" y="%d" font-size="12" fill="%s" transform="rotate(-90 %d %d)" text-anchor="middle">calore</text>' % (ox - 8, 200, MUTED, ox - 8, 200)
    b += '<line x1="%d" y1="150" x2="%d" y2="150" stroke="%s" stroke-dasharray="5 4"/>' % (ox, ox + 250, ERR)
    b += text(ox + 248, 144, 'soglia di bruciore', 11.5, 'end', 600, ERR)
    b += '<polyline points="%d,%d %d,%d %d,%d" fill="none" stroke="%s" stroke-width="2.5"/>' % (ox, oy - 10, ox + 60, 125, ox + 240, 200, ERR)
    b += '<polyline points="%d,%d %d,%d %d,%d %d,%d %d,%d %d,%d %d,%d" fill="none" stroke="%s" stroke-width="3"/>' % (
        ox, oy - 10, ox + 30, 175, ox + 45, 230, ox + 80, 180, ox + 95, 225, ox + 150, 200, ox + 240, 215, OK)
    b += text(ox + 125, 330, 'verde: togli la mano 5 s e rientra', 12, weight=700, fill=OK)
    return svg(940, 355, b, 'Posizione della mano in lampada e tecnica flash and pull')


@fig('dpi.svg')
def ppe():
    b = text(20, 38, 'Dispositivi di protezione individuale (DPI)', 20, 'start', 800, ACC2)
    items = ['Guanti in nitrile', 'Mascherina FFP2', 'Occhiali protettivi', 'Aspiratore da tavolo']
    subs = ['il lattice non ferma i monomeri', 'durante la limatura', 'polveri e schizzi', 'polveri e vapori alla fonte']
    for k, t in enumerate(items):
        x = 20 + k * 225
        b += panel(x, 60, 210, 250, t)
        cx, cy = x + 105, 190
        if k == 0:
            g = '<g fill="#7aa6e0" stroke="#4f7fbf" stroke-width="2">'
            g += '<rect x="%d" y="%d" width="70" height="80" rx="16"/>' % (cx - 35, cy - 20)
            for j, hgt in enumerate((55, 66, 62, 50)):
                g += '<rect x="%d" y="%d" width="16" height="%d" rx="8"/>' % (cx - 35 + j * 18, cy - 10 - hgt, hgt + 20)
            g += '<rect x="%d" y="%d" width="16" height="48" rx="8" transform="rotate(40 %d %d)"/>' % (cx + 30, cy - 10, cx + 38, cy + 14)
            g += '<rect x="%d" y="%d" width="70" height="14" fill="#5d8fcf"/></g>' % (cx - 35, cy + 60)
            b += g
        elif k == 1:
            b += '<path d="M%d,%d Q%d,%d %d,%d Q%d,%d %d,%d Z" fill="#f3f3f3" stroke="#9aa3ad" stroke-width="2"/>' % (cx - 60, cy - 10, cx, cy - 60, cx + 60, cy - 10, cx, cy + 60, cx - 60, cy - 10)
            b += '<path d="M%d,%d L%d,%d M%d,%d L%d,%d" stroke="#9aa3ad" stroke-width="2"/>' % (cx - 60, cy - 10, cx - 85, cy - 30, cx + 60, cy - 10, cx + 85, cy - 30)
            b += '<circle cx="%d" cy="%d" r="9" fill="#d8dde3"/>' % (cx + 20, cy + 8)
        elif k == 2:
            for sx in (-1, 1):
                b += '<ellipse cx="%d" cy="%d" rx="34" ry="26" fill="#e8f3fb" stroke="#4b3a40" stroke-width="4"/>' % (cx + sx * 40, cy)
            b += '<path d="M%d,%d q8,-8 16,0" stroke="#4b3a40" stroke-width="4" fill="none"/>' % (cx - 8, cy - 4)
        else:
            b += '<rect x="%d" y="%d" width="130" height="70" rx="10" fill="#d8dde3" stroke="#9aa3ad" stroke-width="2"/>' % (cx - 65, cy - 20)
            b += ''.join('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#9aa3ad" stroke-width="2"/>' % (cx - 50 + j * 12, cy - 10, cx - 50 + j * 12, cy + 40) for j in range(9))
            b += ''.join('<path d="M%d,%d q6,-14 0,-26" stroke="%s" stroke-width="2" fill="none" marker-end="url(#ar)"/>' % (cx - 30 + j * 30, cy - 30, ACC2) for j in range(3))
        b += text(cx, 292, subs[k], 12.5, fill=MUTED)
    return svg(940, 325, arrow_defs() + b, 'Guanti, mascherina, occhiali e aspiratore')


@fig('ciclo-sterilizzazione.svg')
def steril_cycle():
    b = text(20, 38, 'Il ciclo degli strumenti dopo ogni cliente', 20, 'start', 800, ACC2)
    steps = [('Detergi', 'acqua e detergente'), ('Disinfetta', 'per immersione'), ('Risciacqua', 'e asciuga bene'),
             ('Imbusta', 'buste sigillate'), ('Autoclave', 'classe B (EN 13060)'), ('Registra', 'conserva la stampa')]
    for k, (t, sub) in enumerate(steps):
        cx = 90 + k * 150
        cy = 140
        b += '<circle cx="%d" cy="%d" r="50" fill="%s"/>' % (cx, cy, ['#f8dfe7', '#f3c4d3', '#eeaabf', '#e48fa9', ACC, ACC2][k])
        b += text(cx, cy - 4, str(k + 1), 22, weight=800, fill='#fff' if k > 2 else ACC2)
        b += text(cx, cy + 18, t, 14, weight=800, fill='#fff' if k > 2 else INK)
        b += text(cx, cy + 75, sub, 12, fill=MUTED)
        if k < 5:
            b += arrow(cx + 54, cy, cx + 94, cy)
    b += '<rect x="40" y="245" width="860" height="44" rx="10" fill="#fbe7e4"/>'
    b += text(470, 273, 'Lime in carta e buffer non si sterilizzano: sono monouso o si regalano alla cliente.', 14, weight=600, fill=ERR)
    return svg(940, 305, arrow_defs() + b, 'Ciclo di ricondizionamento degli strumenti')


@fig('pennelli.svg')
def brushes():
    b = text(20, 38, 'I pennelli e gli strumenti di stesura', 20, 'start', 800, ACC2)
    items = [('Piatto per gel', 'base e costruttore'), ('Ovale / tondo', 'gel, zona cuticolare'), ('Acrilico 8–12', 'raccoglie la perla'),
             ('Liner / striper', 'linee e dettagli'), ('Ventaglio', 'polveri e glitter'), ('Dotter', 'puntini')]
    for k, (t, sub) in enumerate(items):
        cx = 90 + k * 152
        b += '<rect x="%d" y="150" width="12" height="130" rx="6" fill="#4b3a40"/>' % (cx - 6)
        b += '<rect x="%d" y="128" width="16" height="26" fill="#c9b8a0"/>' % (cx - 8)
        if k == 0:
            b += '<path d="M%d,128 L%d,80 L%d,80 L%d,128 Z" fill="%s"/>' % (cx - 8, cx - 11, cx + 11, cx + 8, GEL)
        elif k == 1:
            b += '<path d="M%d,128 C%d,100 %d,80 %d,78 C%d,80 %d,100 %d,128 Z" fill="%s"/>' % (cx - 8, cx - 12, cx - 6, cx, cx + 6, cx + 12, cx + 8, GEL)
        elif k == 2:
            b += '<path d="M%d,128 C%d,100 %d,82 %d,70 C%d,82 %d,100 %d,128 Z" fill="#f3eee6" stroke="#cbbfae"/>' % (cx - 8, cx - 16, cx - 8, cx, cx + 8, cx + 16, cx + 8)
        elif k == 3:
            b += '<path d="M%d,128 L%d,60 L%d,60 L%d,128 Z" fill="#3b2a30"/>' % (cx - 3, cx - 1, cx + 1, cx + 3)
        elif k == 4:
            b += '<path d="M%d,128 L%d,80 Q%d,66 %d,80 Z" fill="#f3eee6" stroke="#cbbfae"/>' % (cx - 4, cx - 36, cx, cx + 36)
            b += '<path d="M%d,128 L%d,80 Q%d,66 %d,80 Z" fill="none" stroke="#cbbfae"/>' % (cx + 4, cx - 30, cx, cx + 30)
        else:
            b += '<path d="M%d,128 L%d,70" stroke="#9aa3ad" stroke-width="3"/><circle cx="%d" cy="68" r="7" fill="#9aa3ad"/>' % (cx, cx, cx)
        b += text(cx, 305, t, 14, weight=700)
        b += text(cx, 324, sub, 12, fill=MUTED)
    b += text(470, 360, 'Pulisci i pennelli per gel con il cleaner e quelli per acrilico con il monomero; conservali al riparo dalla luce.', 13, fill=MUTED)
    return svg(940, 375, b, 'Tipi di pennelli per la ricostruzione')


@fig('tip-tipi.svg')
def tip_types():
    b = text(20, 38, 'Tip: tipi e misure', 20, 'start', 800, ACC2)
    b += panel(20, 60, 300, 280, 'Con incavo (well)')
    b += panel(335, 60, 300, 280, 'A contatto (contact)')
    for k, x in enumerate((170, 485)):
        tip = nail_outline(x, 300, 220, 110, 42, 'squoval')
        b += '<path d="%s" fill="#f8f4ee" stroke="#cbbfae" stroke-width="1.6"/>' % tip
        if k == 0:
            b += '<path d="M%d,%d Q%d,%d %d,%d L%d,%d L%d,%d Z" fill="url(#hatch2)" stroke="%s"/>' % (x - 42, 258, x, 236, x + 42, 258, x + 42, 306, x - 42, 306, ACC)
            b += text(x, 330, 'l\'incavo va fuso dopo l\'applicazione', 12.5, fill=MUTED)
        else:
            b += text(x, 330, 'nessun incavo: niente fusione', 12.5, fill=MUTED)
    b += panel(650, 60, 270, 280, 'Misure (0 = la più larga)')
    for k in range(10):
        w = 46 - k * 3.2
        x = 690 + (k % 5) * 50
        y = 150 + (k // 5) * 105
        b += '<path d="%s" fill="#f8f4ee" stroke="#cbbfae"/>' % nail_outline(x, y + 4, y - 20, y - 45, w / 2, 'squoval')
        b += text(x, y + 30, str(k), 12.5, weight=700)
    defs = ('<defs><pattern id="hatch2" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
            '<line x1="0" y1="0" x2="0" y2="6" stroke="%s" stroke-width="2"/></pattern></defs>' % GEL)
    return svg(940, 355, defs + b, 'Tip con incavo, tip a contatto e scala delle misure')


@fig('scheda-cliente.svg')
def client_card():
    b = '<rect x="30" y="20" width="620" height="520" rx="14" fill="#fff" stroke="#e5d6d2" stroke-width="2"/>'
    b += '<rect x="30" y="20" width="620" height="60" rx="14" fill="%s"/><rect x="30" y="60" width="620" height="20" fill="%s"/>' % (ACC, ACC)
    b += text(60, 58, 'Scheda cliente', 22, 'start', 800, '#fff')
    b += text(620, 58, 'n. ____', 15, 'end', 600, '#fff')
    rows = [('Nome e cognome', 'line'), ('Telefono / e-mail', 'line'), ('Consenso privacy (GDPR)', 'check'),
            ('Allergie (acrilati, lattice…)', 'line'), ('Farmaci, diabete, gravidanza, terapie', 'line'),
            ('Abitudini (onicofagia, acqua…)', 'line'), ('Stato della lamina / controindicazioni', 'line'),
            ('Servizio e prodotti (lotti)', 'line'), ('Foto prima / dopo', 'check'), ('Prossimo refill', 'line')]
    for k, (lab, kind) in enumerate(rows):
        y = 115 + k * 42
        b += text(60, y, lab, 14, 'start', 600)
        if kind == 'line':
            b += '<line x1="340" y1="%d" x2="620" y2="%d" stroke="#d8c8c4" stroke-width="1.5"/>' % (y + 3, y + 3)
        else:
            b += '<rect x="340" y="%d" width="16" height="16" rx="3" fill="none" stroke="%s" stroke-width="2"/>' % (y - 12, ACC2)
            b += '<path d="M343,%d l4,5 l8,-10" stroke="%s" stroke-width="2.5" fill="none"/>' % (y - 4, OK)
    b += text(60, 530, 'Firma della cliente ______________________     Data ___/___/______', 13.5, 'start', fill=MUTED)
    return svg(680, 560, b, 'Esempio di scheda cliente')


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, f in FIGS.items():
        with open(os.path.join(OUT, name), 'w', encoding='utf-8') as fh:
            fh.write(f())
    print('Generate %d illustrazioni in %s' % (len(FIGS), os.path.normpath(OUT)))


if __name__ == '__main__':
    main()
