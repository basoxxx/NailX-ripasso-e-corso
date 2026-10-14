#!/usr/bin/env python3
"""Genera le illustrazioni tutorial SVG del corso in assets/img/.

Uso:  python3 tools/gen_svg.py
Tutte le figure condividono palette e primitive (dito + unghia vista dall'alto,
profilo laterale, pannelli step-by-step) per avere uno stile coerente.
"""
import math
import re
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


# ---------------------------------------------------------------- finitura "professionale"
# Le figure usano colori piatti; svg() li sostituisce con sfumature e ombre leggere condivise,
# così tutte le illustrazioni (anche quelle di tools/svg_*.py) hanno lo stesso aspetto curato.
FINISH_DEFS = {
    'nxSkin': '<linearGradient id="nxSkin" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e2b29b"/>'
              '<stop offset=".22" stop-color="#f3cdb6"/><stop offset=".55" stop-color="#f8dccb"/>'
              '<stop offset=".82" stop-color="#f1c7af"/><stop offset="1" stop-color="#dfac94"/></linearGradient>',
    'nxNail': '<linearGradient id="nxNail" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fbd6e0"/>'
              '<stop offset=".45" stop-color="#f7c1cf"/><stop offset="1" stop-color="#eeaabd"/></linearGradient>',
    'nxFree': '<linearGradient id="nxFree" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/>'
              '<stop offset="1" stop-color="#fbeef2"/></linearGradient>',
    'nxMetal': '<linearGradient id="nxMetal" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c9d0d7"/>'
               '<stop offset=".45" stop-color="#9aa3ad"/><stop offset="1" stop-color="#7c8691"/></linearGradient>',
    'nxMetalD': '<linearGradient id="nxMetalD" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9aa4ae"/>'
                '<stop offset=".5" stop-color="#6f7983"/><stop offset="1" stop-color="#565f68"/></linearGradient>',
    'nxPanel': '<linearGradient id="nxPanel" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fdf6f3"/>'
               '<stop offset="1" stop-color="#f8ece8"/></linearGradient>',
    'nxSh': '<filter id="nxSh" x="-5%" y="-5%" width="110%" height="115%"><feDropShadow dx="0" dy="1.5" stdDeviation="2.2" '
            'flood-color="#5a2a3a" flood-opacity=".13"/></filter>',
    'nxShS': '<filter id="nxShS" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="1" stdDeviation="1.2" '
             'flood-color="#3b2a30" flood-opacity=".25"/></filter>',
}
_FINISH = [
    ('fill="%s"' % SKIN, 'fill="url(#nxSkin)"', 'nxSkin'),
    ('fill="%s"' % NAIL, 'fill="url(#nxNail)"', 'nxNail'),
    ('fill="%s"' % FREE, 'fill="url(#nxFree)"', 'nxFree'),
    ('fill="#9aa3ad"', 'fill="url(#nxMetal)"', 'nxMetal'),
    ('fill="#6f7983"', 'fill="url(#nxMetalD)"', 'nxMetalD'),
]


def finish(body):
    used = []
    for old, new, d in _FINISH:
        if old in body:
            body = body.replace(old, new)
            used.append(d)
    # pannelli: fondo sfumato, bordo sottile e ombra morbida
    def panel_rect(m):
        tag = m.group(0).replace('fill="%s"' % PANEL, 'fill="url(#nxPanel)"')
        extra = ('' if ' stroke=' in tag else ' stroke="#efdcd6" stroke-width="1"') + ('' if ' filter=' in tag else ' filter="url(#nxSh)"')
        return tag[:-2] + extra + '/>' if tag.endswith('/>') else tag[:-1] + extra + '>'
    body, n = re.subn(r'<rect [^>]*fill="%s"[^>]*>' % PANEL, panel_rect, body)
    if n:
        used += ['nxPanel', 'nxSh']
    for d in ('nxSh', 'nxShS'):
        if 'url(#%s)' % d in body:
            used.append(d)
    return ('<defs>%s</defs>' % ''.join(FINISH_DEFS[d] for d in dict.fromkeys(used)) if used else '') + body


def svg(w, h, body, title):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
            'font-family="%s" role="img"><title>%s</title>'
            '<rect width="100%%" height="100%%" fill="#ffffff"/>%s</svg>\n') % (w, h, w, h, FONT, title, finish(body))


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
        s += '<circle cx="%d" cy="%d" r="15" fill="%s" stroke="#fff" stroke-width="2" filter="url(#nxShS)"/>' % (x + 26, y + 26, color)
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
    return '<circle cx="%.1f" cy="%.1f" r="%d" fill="%s" stroke="#fff" stroke-width="2" filter="url(#nxShS)"/>%s' % (x, y, r, c, sym)


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
    # riflesso di luce sulla lamina
    out += ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="#fff" opacity=".32" clip-path="url(#%s)"/>'
            % (cx - hw * 0.62, y_t + 6, hw * 0.22, (y_c - 24) - (y_t + 6), hw * 0.11, clip))
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


# ---------------------------------------------------------------- dettagli locali delle figure di base
# Varianti più realistiche di strumenti e soggetti, usate solo dalle figure qui sotto.
# Il prefisso "_" le esclude da "from gen_svg import *": le primitive condivise restano invariate.
def _rot(x, y, ang, inner, shadow=True):
    g = '<g transform="translate(%.1f,%.1f) rotate(%.1f)">%s</g>' % (x, y, ang, inner)
    return '<g filter="url(#nxShS)">%s</g>' % g if shadow else g


def _skinv(y0, y1, x0=0, x1=0):
    """Sfumatura della pelle per dita viste di profilo (chiaro in alto, ombra in basso), in coordinate assolute."""
    gid = uid('sv')
    return gid, ('<defs><linearGradient id="%s" gradientUnits="userSpaceOnUse" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f">'
                 '<stop offset="0" stop-color="#f8dccb"/><stop offset=".45" stop-color="#f3cdb6"/>'
                 '<stop offset="1" stop-color="#dba98f"/></linearGradient></defs>' % (gid, x0, y0, x1, y1))


def _file(x, y, ang=0, l=150, w=20, grit='#8f8178', dots='#5e5049', rim='#efe7df', label='', shadow=True, lsize=12):
    """Lima a sandwich vista dall'alto: bordo chiaro (anima in spugna) e superficie abrasiva granulosa."""
    pid = uid('gr')
    s = ('<defs><pattern id="%s" width="5" height="5" patternUnits="userSpaceOnUse"><rect width="5" height="5" fill="%s"/>'
         '<circle cx="1.2" cy="1.3" r=".75" fill="%s"/><circle cx="3.7" cy="3.4" r=".6" fill="#fff" opacity=".4"/>'
         '<circle cx="3.9" cy="1" r=".45" fill="%s"/></pattern></defs>' % (pid, grit, dots, dots))
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s" stroke="#cbbdb0" stroke-width="1"/>' % (
        -l / 2, -w / 2 - 2.5, l, w + 5, (w + 5) / 2, rim)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="url(#%s)"/>' % (-l / 2 + 2.5, -w / 2, l - 5, w, w / 2, pid)
    s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#fff" stroke-width="1.4" opacity=".35" stroke-linecap="round"/>' % (
        -l / 2 + w / 2, -w / 2 + 2.5, l / 2 - w / 2, -w / 2 + 2.5)
    if label:
        s += text(0, lsize * .375, label, lsize, weight=800, fill='#fff')
    return _rot(x, y, ang, s, shadow)


def _pusher(x, y, ang=0, l=150, shadow=True):
    """Spingicuticole in acciaio: spatola a cucchiaio (punta in x,y, verso -x), collo e impugnatura zigrinata."""
    pid = uid('kn')
    s = ('<defs><pattern id="%s" width="4" height="4" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
         '<rect width="4" height="4" fill="#a3acb6"/><line x1="0" y1="0" x2="0" y2="4" stroke="#717b86" stroke-width="1.3"/></pattern></defs>'
         % pid)
    s += '<path d="M3,-3 L-7,-8.5 Q-25,-10.5 -28,0 Q-25,10.5 -7,8.5 L3,3 Z" fill="#9aa3ad" stroke="#5f6973" stroke-width="1"/>'
    s += '<path d="M-9,-5 Q-22,-6.5 -24,0" stroke="#fff" stroke-width="1.5" fill="none" opacity=".75" stroke-linecap="round"/>'
    s += '<rect x="0" y="-2.8" width="28" height="5.6" rx="2.8" fill="#9aa3ad" stroke="#5f6973" stroke-width=".8"/>'
    hl = l - 28 - 16
    s += '<rect x="26" y="-6.5" width="%.1f" height="13" rx="6.5" fill="url(#%s)" stroke="#5f6973" stroke-width="1"/>' % (hl, pid)
    s += '<rect x="%.1f" y="-3.5" width="18" height="7" rx="3.5" fill="#9aa3ad" stroke="#5f6973" stroke-width=".8"/>' % (26 + hl - 2)
    s += '<line x1="32" y1="-3.6" x2="%.1f" y2="-3.6" stroke="#fff" stroke-width="1.6" opacity=".5" stroke-linecap="round"/>' % (26 + hl - 6)
    return _rot(x, y, ang, s, shadow)


def _stick(x, y, ang=0, l=130, shadow=True):
    """Bastoncino d'arancio: punta a scalpello in (x,y) verso -x, venature del legno."""
    s = ('<path d="M0,0 L18,-5 L%.1f,-5 L%.1f,0 L%.1f,5 L18,5 Z" fill="#e8c592" stroke="#b28a57" stroke-width="1"/>'
         % (l - 16, l, l - 16))
    s += '<path d="M0,0 L18,-5 L18,5 Z" fill="#f5e0be" stroke="#b28a57" stroke-width=".8"/>'
    s += ('<path d="M24,-2 L%.1f,-1.6 M30,1.8 L%.1f,2.1 M%.1f,-.2 L%.1f,0" stroke="#c9a06a" stroke-width=".9" fill="none"/>'
          % (l * .55, l * .8, l * .6, l - 22))
    return _rot(x, y, ang, s, shadow)


def _brush(x, y, ang=0, l=130, bristle='#f3eee6', kind='flat', load=None, handle='#4b3a40', shadow=True):
    """Pennello: punta delle setole in (x,y) verso -x, ghiera metallica crimpata, manico affusolato."""
    shapes = {
        'flat': (22, 'M0,-6.5 Q-1.5,0 0,6.5 L22,6 L22,-6 Z'),
        'oval': (24, 'M24,-6.5 C12,-7.5 1,-6 0,0 C1,6 12,7.5 24,6.5 Z'),
        'acrylic': (30, 'M30,-7 C17,-9.5 5,-4 0,0 C5,4 17,9.5 30,7 Z'),
        'liner': (30, 'M30,-2.6 L0,-.7 L0,.7 L30,2.6 Z'),
        'dust': (34, 'M34,-7 C22,-16 4,-16 0,0 C4,16 22,16 34,7 Z'),
    }
    B, path = shapes[kind]
    l = max(l, B + 80)  # manico sempre riconoscibile, anche nei pennelli corti
    s = '<path d="%s" fill="%s" stroke="#00000022" stroke-width="1"/>' % (path, bristle)
    for k in (-.5, 0, .5):
        s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#000" stroke-width=".7" opacity=".14"/>' % (
            B - 1, k * 9, B * .3, k * 4)
    if load:
        s += '<ellipse cx="2" cy="0" rx="6" ry="5" fill="%s" stroke="#00000033"/>' % load
    s += '<rect x="%.1f" y="-7" width="17" height="14" rx="2" fill="#9aa3ad" stroke="#6f7983" stroke-width=".8"/>' % (B - 1)
    s += '<path d="M%.1f,-7 L%.1f,7 M%.1f,-7 L%.1f,7" stroke="#6f7983" stroke-width="1"/>' % (B + 3, B + 3, B + 12, B + 12)
    s += ('<path d="M%.1f,-5.5 L%.1f,-3.4 Q%.1f,0 %.1f,3.4 L%.1f,5.5 Z" fill="%s"/>'
          % (B + 16, l, l + 4, l, B + 16, handle))
    s += '<line x1="%.1f" y1="-3" x2="%.1f" y2="-2" stroke="#fff" stroke-width="1.4" opacity=".28" stroke-linecap="round"/>' % (B + 20, l - 6)
    return _rot(x, y, ang, s, shadow)


def _bottle(cx, base, col='#e46f8f', h=62, w=40, cap='#3b2a30', label='', lsize=12):
    """Flacone tipo smalto/gel: vetro con riflesso, prodotto colorato, tappo alto con pennello interno."""
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="#f7f2f4" stroke="#bfb1b6" stroke-width="1.4"/>' % (
        cx - w / 2, base - h, w, h, w * .28)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s"/>' % (
        cx - w / 2 + 4, base - h * .78, w - 8, h * .78 - 4, w * .22, col)
    s += '<rect x="%.1f" y="%.1f" width="5" height="%.1f" rx="2.5" fill="#fff" opacity=".6"/>' % (cx - w / 2 + 7, base - h * .7, h * .5)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="9" rx="2" fill="#d8ccd0"/>' % (cx - w * .22, base - h - 7, w * .44)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="5" fill="%s"/>' % (cx - w * .2, base - h - 7 - h * .55, w * .4, h * .55, cap)
    s += '<rect x="%.1f" y="%.1f" width="3" height="%.1f" rx="1.5" fill="#fff" opacity=".25"/>' % (cx - w * .2 + 3, base - h - 3 - h * .55, h * .45)
    if label:
        s += text(cx, base - h * .35, label, lsize, weight=800, fill='#fff')
    return '<g filter="url(#nxShS)">%s</g>' % s


def _jar(cx, base, col='#e9a7bd', w=72, h=38, lid='#3b2a30', label='', lsize=12):
    """Vasetto (gel / polvere): corpo basso con etichetta e coperchio a vite."""
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="8" fill="%s" stroke="#00000022"/>' % (cx - w / 2, base - h, w, h, col)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="#fff" opacity=".85"/>' % (cx - w / 2 + 8, base - h + 9, w - 16, h - 18)
    if label:
        s += text(cx, base - h / 2 + lsize * .375, label, lsize, weight=800, fill=INK)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="16" rx="5" fill="%s"/>' % (cx - w / 2 - 3, base - h - 14, w + 6, lid)
    for k in range(1, 8):
        s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#fff" stroke-width="1" opacity=".18"/>' % (
            cx - w / 2 + k * w / 8, base - h - 12, cx - w / 2 + k * w / 8, base - h)
    s += '<rect x="%.1f" y="%.1f" width="6" height="%.1f" rx="3" fill="#fff" opacity=".35"/>' % (cx - w / 2 + 4, base - h + 4, h - 8)
    return '<g filter="url(#nxShS)">%s</g>' % s


def _dappen(cx, base, liquid='#dff0fa', w=64):
    """Bicchierino dappen in vetro con monomero."""
    s = ('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="#eef6fb" stroke="#9cc3dc" stroke-width="1.6"/>'
         % (cx - w / 2, base - 40, cx + w / 2, base - 40, cx + w / 2 - 8, base, cx - w / 2 + 8, base))
    s += '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="6" fill="%s" stroke="#9cc3dc"/>' % (cx, base - 30, w / 2 - 6, liquid)
    s += '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="7" fill="none" stroke="#9cc3dc" stroke-width="1.6"/>' % (cx, base - 40, w / 2)
    s += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="#fff" stroke-width="3" opacity=".8" stroke-linecap="round"/>' % (
        cx - w / 2 + 7, base - 30, cx - w / 2 + 12, base - 6)
    return '<g filter="url(#nxShS)">%s</g>' % s


def _finger_side(x0, y, xf, xe, free=0, nail='#f6d3dc', nail_t=5, thick=64, fold=True, cuticle=True, extra_nail='', plate=True):
    """Dito di profilo con punta a destra. y = superficie della lamina, xf = piega prossimale, xe = fine del letto ungueale.
    free = lunghezza del bordo libero oltre il polpastrello."""
    gid, defs = _skinv(y - 10, y + thick)
    tip = xe + 30
    s = defs
    s += ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f '
          'C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="url(#%s)" stroke="%s" stroke-width="1.5"/>'
          % (x0, y - 9, xf - 14, y - 9, xf + 2, y - 8, xf + 4, y,
             xe, y + nail_t, xe + 20, y + nail_t, tip, y + 14, tip, y + thick * .42,
             tip, y + thick * .85, xe, y + thick, xe - 50, y + thick, x0, y + thick, gid, SKIN_D))
    # lamina (con eventuale bordo libero)
    xn = xe + free
    if plate:
        s += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.4"/>'
              % (xf - 16, y + 1, (xf + xn) / 2, y - 4, xn, y - 1, xn + 4, y + nail_t / 2, xn, y + nail_t,
                 xf - 16, y + nail_t, xf - 18, y + nail_t / 2, xf - 16, y + 1, nail, NAIL_S))
    s += extra_nail
    # iponichio (sigillo sotto il bordo libero)
    s += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="%s" stroke-width="2.5" fill="none" stroke-linecap="round"/>' % (
        xe - 6, y + nail_t + 1, xe + 6, y + nail_t + 1, xe + 10, y + nail_t + 7, '#e3a08a')
    if fold:
        s += ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="url(#%s)"/>'
              % (xf - 40, y - 9, xf - 14, y - 9, xf + 2, y - 8, xf + 4, y, xf - 10, y + 3, xf - 40, y + 3, gid))
        s += '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="%s" stroke-width="1.5" fill="none"/>' % (
            xf - 40, y - 9, xf - 14, y - 9, xf + 2, y - 8, xf + 4, y, SKIN_D)
    if cuticle:
        s += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="#fff" stroke-width="3" opacity=".85" fill="none" stroke-linecap="round"/>' % (
            xf + 5, y - 1, xf + 14, y - 2.5, xf + 24, y - 2.5)
    return s, dict(xf=xf, xe=xe, tip=tip, xn=xn, y=y)


def _ctip(cx, y, sag, hw=72, col=ACC, thick=9, finger=True):
    """Polpastrello visto dal bordo libero con la lamina ad arco (curva a C). y = estremi dell'arco, sag = freccia della curva."""
    s = ''
    if finger:
        gid, defs = _skinv(y - 2 * sag, y + 95)
        s += defs
        s += ('<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" '
              'fill="url(#%s)" stroke="%s" stroke-width="1.5"/>'
              % (cx - hw + 4, y + 4, cx - hw - 6, y + 60, cx - 40, y + 92, cx, y + 92,
                 cx + 40, y + 92, cx + hw + 6, y + 60, cx + hw - 4, y + 4, cx, y + 4 - 2 * sag + 2 * thick, cx - hw + 4, y + 4, gid, SKIN_D))
    s += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" '
          'fill="%s" stroke="%s" stroke-width="1.4"/>'
          % (cx - hw, y, cx, y - 2 * sag, cx + hw, y, cx + hw + 3, y + thick / 2 + 1, cx + hw - 2, y + thick,
             cx, y - 2 * sag + 2 * thick, cx - hw + 2, y + thick, cx - hw - 3, y + thick / 2 + 1, cx - hw, y, col, NAIL_S))
    s += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="#fff" stroke-width="2" opacity=".55" fill="none" stroke-linecap="round"/>' % (
        cx - hw * .7, y - sag * .55 + 2, cx, y - 2 * sag + 4, cx + hw * .7, y - sag * .55 + 2)
    return s


def _hand_side(x, y, L=210, ang=0, nail='#e46f8f'):
    """Mano piatta vista di lato, dita verso destra; (x,y) = polso all'altezza del dorso."""
    gid, defs = _skinv(-34, 26)
    s = defs
    s += ('<path d="M0,-30 C%.1f,-36 %.1f,-30 %.1f,-18 L%.1f,-12 Q%.1f,-12 %.1f,-4 Q%.1f,4 %.1f,5 L%.1f,8 '
          'C%.1f,12 %.1f,24 %.1f,24 L0,24 Z" fill="url(#%s)" stroke="%s" stroke-width="1.5"/>'
          % (L * .25, L * .45, L * .58, L - 12, L, L + 2, L + 1, L - 12, L * .6, L * .45, L * .25, L * .1, gid, SKIN_D))
    # pollice (sul lato verso chi guarda)
    s += ('<path d="M%.1f,2 C%.1f,-4 %.1f,-2 %.1f,4 C%.1f,10 %.1f,14 %.1f,14" fill="none" stroke="%s" stroke-width="1.5"/>'
          % (L * .2, L * .35, L * .5, L * .55, L * .5, L * .35, L * .22, SKIN_D))
    s += '<path d="M%.1f,-14 Q%.1f,-16 %.1f,-12 L%.1f,-6 L%.1f,-7 Z" fill="%s" stroke="%s" stroke-width="1"/>' % (
        L - 38, L - 18, L - 4, L - 6, L - 38, nail, NAIL_S)
    return '<g transform="translate(%.1f,%.1f) rotate(%.1f)">%s</g>' % (x, y, ang, s)


def _lamp_side(cx, base, w=230, h=100, rays=True, opening=0):
    """Lampada UV/LED in sezione laterale: scocca, LED sul soffitto, base riflettente."""
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="10" rx="5" fill="#8a7d9e"/>' % (cx - w / 2 - 6, base, w + 12)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="5" rx="2" fill="#d9d2e6"/>' % (cx - w / 2 + 10, base - 4, w - 20)
    shell = ('M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f'
             % (cx - w / 2, base - opening, cx - w / 2, base - h * .55, cx - w / 2, base - h, cx - w / 2 + 40, base - h,
                cx + w / 2 - 40, base - h, cx + w / 2, base - h, cx + w / 2, base - h * .55, cx + w / 2, base))
    s += ('<path d="%s" fill="#f4f1f8"%s/>' % (shell + (' L%.1f,%.1f' % (cx - w / 2, base) if opening else ''),
                                               '' if opening else ' stroke="#8a7d9e" stroke-width="3"'))
    if opening:
        s += '<path d="%s" fill="none" stroke="#8a7d9e" stroke-width="3" stroke-linecap="round"/>' % shell
    if rays:
        gid = uid('uv')
        s += ('<defs><linearGradient id="%s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9a6be0" stop-opacity=".35"/>'
              '<stop offset="1" stop-color="#9a6be0" stop-opacity=".04"/></linearGradient></defs>' % gid)
        s += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="url(#%s)"/>' % (
            cx - w / 2 + 30, base - h + 8, cx + w / 2 - 30, base - h + 8, cx + w / 2 - 6, base - 5, cx - w / 2 + 6, base - 5, gid)
    for k in range(7):
        lx = cx - w / 2 + 34 + k * (w - 68) / 6
        s += '<rect x="%.1f" y="%.1f" width="12" height="5" rx="2" fill="#7b4bd6"/>' % (lx - 6, base - h + 2)
    return s


def _num(x, y, n, col=ACC2, r=11, size=12):
    return ('<circle cx="%.1f" cy="%.1f" r="%d" fill="%s" stroke="#fff" stroke-width="1.5"/>' % (x, y, r, col)
            + text(x, y + 4.3 * size / 12, str(n), size, weight=800, fill='#fff'))


def _tag(x, y, s, col=ACC2, size=12.5, anchor='middle', bg='#fff'):
    """Etichetta breve su fondo chiaro, leggibile anche sopra l'illustrazione."""
    w = len(s) * size * .56 + 14
    x0 = x - w / 2 if anchor == 'middle' else (x if anchor == 'start' else x - w)
    return ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s" stroke="%s" stroke-width="1" opacity=".96"/>'
            % (x0, y - size - 3, w, size + 10, (size + 10) / 2, bg, col)
            + text(x0 + w / 2, y + 1.5, s, size, weight=700, fill=col))



def _callout(x1, y1, x2, y2, lines, size=13, weight=600, fill=INK):
    """Linea di richiamo con pallino; il testo (una o più righe) sta sopra o sotto l'estremità, senza toccare la linea."""
    if isinstance(lines, str):
        lines = [lines]
    s = ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.3"/><circle cx="%.1f" cy="%.1f" r="3.5" fill="%s"/>'
         % (x1, y1, x2, y2, MUTED, x1, y1, ACC2))
    lh = size * 1.25
    y0 = y2 - 6 - (len(lines) - 1) * lh if y2 <= y1 else y2 + size + 3
    return s + mtext(x2, y0, lines, size, 'middle', weight, fill)


def _form(cx, ys, w=80, h=130):
    """Cartina vista dall'alto (come form_top) con righe graduate solo dentro il foglio, per altezze ridotte."""
    s = ('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f A%.1f,%.1f 0 0 0 %.1f,%.1f Z" fill="#f6e7a8" stroke="#d8c26a"/>'
         % (cx - w, ys + 36, cx - w, ys - h, cx + w, ys - h, cx + w, ys + 36, cx + 46, ys + 36, 46, 48, cx - 46, ys + 36))
    k = 1
    while ys - k * 26 + 6 > ys - h + 6:
        s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#d8c26a"/>' % (cx - w + 8, ys - k * 26 + 6, cx + w - 8, ys - k * 26 + 6)
        k += 1
    s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-dasharray="4 4"/>' % (cx, ys - h, cx, ys - 8, ACC2)
    return s


# ---------------------------------------------------------------- helper locali (igiene, piedi, difetti)
def _P(d, fill='none', stroke=INK, sw=2, extra=''):
    return '<path d="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round"%s/>' % (d, fill, stroke, sw, extra)


def _ln(x1, y1, x2, y2, col=INK, w=2, extra=''):
    return '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s" stroke-linecap="round"%s/>' % (x1, y1, x2, y2, col, w, extra)


def _mixc(c1, c2, t):
    a = [int(c1[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
    return '#%02x%02x%02x' % tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))


def _lgrad(stops, x2=1, y2=0, x1=0, y1=0, p='lg'):
    gid = uid(p)
    st = ''.join('<stop offset="%s" stop-color="%s" stop-opacity="%s"/>' % s if len(s) == 3 else
                 '<stop offset="%s" stop-color="%s"/>' % s for s in stops)
    return gid, '<defs><linearGradient id="%s" x1="%s" y1="%s" x2="%s" y2="%s">%s</linearGradient></defs>' % (gid, x1, y1, x2, y2, st)


def _toe_top(cx, by, hw=46, nail_len=78, free=6, plate='#f3cbc6', free_col=None, finger_len=40, extra='', shape='squoval', deep=True):
    """Alluce visto dall'alto (da tools/svg_d.toe_top): polpastrello largo che sporge oltre l'unghia,
    lamina larga quasi quadrata, pieghe laterali morbide, piega prossimale bassa."""
    y_c = by
    y_s = y_c - nail_len
    y_t = y_s - free
    tw = hw * 1.5
    bw = hw * 1.3
    yp = min(y_s, y_t) - hw * 0.52
    yb = by + finger_len
    toe = ('M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f '
           'C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z') % (
        cx - bw, yb + 30,
        cx - bw, y_c, cx - tw, y_s + hw * 1.0, cx - tw, y_s + hw * 0.45,
        cx - tw * 0.97, yp + hw * 0.3, cx - tw * 0.58, yp, cx, yp,
        cx + tw * 0.58, yp, cx + tw * 0.97, yp + hw * 0.3, cx + tw, y_s + hw * 0.45,
        cx + tw, y_s + hw * 1.0, cx + bw, y_c, cx + bw, yb + 30,
        cx + bw * 0.4, yb + 40, cx - bw * 0.4, yb + 40, cx - bw, yb + 30)
    nat = plate == '#f3cbc6'
    gn, dn = _lgrad([(0, '#eab0a4'), (.2, '#f7d5cc'), (.5, '#fde6df'), (.8, '#f6d0c6'), (1, '#e6ab9f')], p='tn')
    gs, ds = _lgrad([(0, '#8a3f2e', .3), (.18, '#8a3f2e', .05), (.5, '#8a3f2e', 0), (.82, '#8a3f2e', .06), (1, '#8a3f2e', .32)], p='ts')
    gh, dh = _lgrad([(0, '#fff', .9), (.6, '#fff', .35), (1, '#fff', 0)], 0, 1, p='th')
    tc = uid('toe')
    o = dn + ds + dh + '<defs><clipPath id="%s"><path d="%s"/></clipPath></defs>' % (tc, toe)
    o += '<path d="%s" fill="%s"/>' % (toe, SKIN)
    o += '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="#fff" opacity=".28" clip-path="url(#%s)"/>' % (
        cx - hw * 0.15, yp + hw * 0.32, tw * 0.62, hw * 0.24, tc)
    outline = nail_outline(cx, y_c, y_s, y_t, hw, shape)
    clip = uid()
    o += '<defs><clipPath id="%s"><path d="%s"/></clipPath></defs>' % (clip, outline)
    o += '<path d="%s" fill="%s"/>' % (outline, 'url(#%s)' % gn if nat else plate)
    if free > 0:
        fc = free_col or (_mixc(plate, '#ffffff', .55) if nat else plate)
        o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" clip-path="url(#%s)"/>' % (cx - hw - 4, y_t - 10, 2 * hw + 8, free + 10, fc, clip)
        o += _ln(cx - hw, y_s, cx + hw, y_s, _mixc(plate, '#000000', .12), 1, ' opacity=".6"')
    o += extra.replace('CLIP', clip)
    o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#%s)" clip-path="url(#%s)"/>' % (cx - hw, y_t - 4, 2 * hw, nail_len + free + 12, gs, clip)
    o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="url(#%s)" opacity=".6" clip-path="url(#%s)"/>' % (
        cx - hw * 0.55, y_t + 8, hw * 0.2, nail_len * 0.62, hw * 0.1, gh, clip)
    o += '<path d="%s" fill="none" stroke="%s" stroke-width="1.5"/>' % (outline, '#c98f88' if nat else _mixc(plate, '#000000', .35))
    for sx in (-1, 1):
        x_in = cx + sx * (hw - 3)
        x_out = cx + sx * (tw + 2)
        fold = 'M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (
            x_in, y_c - 6, x_in - sx * 3, y_c - nail_len * 0.45, x_in + sx * 1, y_s + 18, cx + sx * (hw + 3), y_s + 4,
            x_out, y_s, x_out, y_c + 10)
        o += '<path d="%s" fill="%s" clip-path="url(#%s)"/>' % (fold, SKIN, tc)
        o += _P('M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f' % (x_in, y_c - 6, x_in - sx * 3, y_c - nail_len * 0.45, x_in + sx * 1, y_s + 18,
                                                                cx + sx * (hw + 3), y_s + 4), 'none', SKIN_D, 1.6)
        if deep:
            o += _P('M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f' % (x_in + sx * 3, y_c - 10, x_in + sx * 1, y_c - nail_len * 0.45, x_in + sx * 4, y_s + 20,
                                                                    cx + sx * (hw + 5), y_s + 8), 'none', '#b07a62', 1.4, ' opacity=".7"')
        o += _P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (x_in + sx * 8, y_c - 14, x_in + sx * 9, y_c - nail_len * 0.5, x_in + sx * 8, y_s + 16),
                'none', '#fff', 3, ' opacity=".25"')
    pf = 'M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (cx - tw - 2, y_c - 12, cx, y_c + 16, cx + tw + 2, y_c - 12,
                                                                     cx + tw + 2, yb + 50, cx - tw - 2, yb + 50)
    o += '<path d="%s" fill="%s" clip-path="url(#%s)"/>' % (pf, SKIN, tc)
    o += _P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - hw - 2, y_c - 8, cx, y_c + 12, cx + hw + 2, y_c - 8), 'none', '#f7e3da', 2.4)
    o += _P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - hw - 4, y_c - 6, cx, y_c + 15, cx + hw + 4, y_c - 6), 'none', SKIN_D, 1.6)
    if finger_len >= 22:
        for j, dy in enumerate((0.55, 0.75)):
            yy = y_c + finger_len * dy + 6
            o += _P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - hw * (0.7 - j * 0.15), yy, cx, yy + 5, cx + hw * (0.7 - j * 0.15), yy),
                    'none', SKIN_D, 1.1, ' opacity=".6"')
    o += '<path d="%s" fill="none" stroke="%s" stroke-width="1.6"/>' % (toe, SKIN_D)
    return o, dict(cx=cx, y_c=y_c, y_s=y_s, y_t=y_t, hw=hw, fw=tw, clip=clip, yp=yp, tw=tw)


def _lens(cx, cy, r, inner, px=None, py=None, ring=ACC2):
    """Ingrandimento circolare (lente) con contenuto ritagliato e linea di richiamo verso il punto (px, py)."""
    c = uid('ln')
    s = ''
    if px is not None:
        a = math.atan2(py - cy, px - cx)
        s += _ln(cx + r * math.cos(a), cy + r * math.sin(a), px, py, ring, 1.4, ' stroke-dasharray="4 3"')
        s += '<circle cx="%.1f" cy="%.1f" r="4" fill="none" stroke="%s" stroke-width="1.6"/>' % (px, py, ring)
    s += '<defs><clipPath id="%s"><circle cx="%.1f" cy="%.1f" r="%.1f"/></clipPath></defs>' % (c, cx, cy, r)
    s += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#fff" filter="url(#nxShS)"/>' % (cx, cy, r)
    s += '<g clip-path="url(#%s)">%s</g>' % (c, inner)
    s += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" stroke-width="2.5"/>' % (cx, cy, r, ring)
    return s


# icone (centrate in 0,0, ingombro ~60x60) per igiene e ciclo degli strumenti
def _ic_soap():
    s = '<ellipse cx="0" cy="27" rx="30" ry="4" fill="#000" opacity=".08"/>'
    s += '<rect x="-15" y="-6" width="30" height="33" rx="7" fill="#e6f2fa" stroke="#7fa8c2" stroke-width="1.6"/>'
    s += '<rect x="-11" y="4" width="22" height="19" rx="5" fill="#bcdcef"/>'
    s += '<rect x="-9" y="-1" width="4" height="22" rx="2" fill="#fff" opacity=".7"/>'
    s += '<rect x="-6" y="-13" width="12" height="8" rx="2" fill="#5f8fae"/>'
    s += '<rect x="-3" y="-21" width="6" height="9" fill="#5f8fae"/>'
    s += '<path d="M-6,-24 L16,-24 L16,-19 L10,-19 L10,-21 L-6,-21 Z" fill="#4b7896"/>'
    for (x, y, r) in [(22, -8, 5), (27, 4, 3.5), (19, 10, 2.6), (-24, 8, 4)]:
        s += '<circle cx="%d" cy="%d" r="%.1f" fill="#fff" stroke="#9cc3dc" stroke-width="1.2"/>' % (x, y, r)
        s += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#9cc3dc" opacity=".6"/>' % (x - r * .35, y - r * .35, r * .25)
    return s


def _ic_tray(tools=True):
    """Vaschetta per disinfezione a immersione: coperchio sollevato, liquido, strumenti immersi."""
    s = '<ellipse cx="0" cy="25" rx="32" ry="4" fill="#000" opacity=".08"/>'
    s += '<path d="M-30,-2 L30,-2 L26,22 Q25,25 21,25 L-21,25 Q-25,25 -26,22 Z" fill="#eef4f8" stroke="#7d8792" stroke-width="1.6"/>'
    s += '<path d="M-28,6 L28,6 L26,21 Q25,23 21,23 L-21,23 Q-25,23 -26,21 Z" fill="#a9d5ee" opacity=".85"/>'
    s += _ln(-26, 6, 26, 6, '#5ea3c9', 1.4)
    if tools:
        s += '<g transform="rotate(-18)"><rect x="-22" y="0" width="40" height="4.5" rx="2.2" fill="#9aa3ad" stroke="#5f6973" stroke-width=".8"/>'
        s += '<path d="M-22,0.5 L-30,-2 L-30,6.5 L-22,4 Z" fill="#9aa3ad" stroke="#5f6973" stroke-width=".8"/></g>'
        s += '<g transform="rotate(14)"><rect x="-14" y="2" width="34" height="4" rx="2" fill="#9aa3ad" stroke="#5f6973" stroke-width=".8"/>'
        s += '<circle cx="21" cy="4" r="3.2" fill="#9aa3ad" stroke="#5f6973" stroke-width=".8"/></g>'
    s += '<path d="M-30,-2 L30,-2" stroke="#7d8792" stroke-width="1.6"/>'
    s += '<path d="M-26,-10 L22,-22 L24,-17 L-24,-5 Z" fill="#dfe6ec" stroke="#7d8792" stroke-width="1.4"/>'
    s += '<rect x="-4" y="-21" width="10" height="4" rx="2" fill="#7d8792" transform="rotate(-14 1 -19)"/>'
    for (x, y) in [(-10, 13), (8, 16), (16, 10)]:
        s += '<circle cx="%d" cy="%d" r="1.8" fill="#fff" opacity=".9"/>' % (x, y)
    return s


def _ic_autoclave():
    s = '<ellipse cx="0" cy="27" rx="34" ry="4" fill="#000" opacity=".08"/>'
    s += '<rect x="-32" y="-22" width="64" height="47" rx="9" fill="#eef1f4" stroke="#7d8792" stroke-width="1.6"/>'
    s += '<rect x="-32" y="17" width="64" height="8" rx="3" fill="#cfd6dd"/>'
    s += '<circle cx="-10" cy="-1" r="15" fill="#cfd6dd" stroke="#7d8792" stroke-width="1.6"/>'
    s += '<circle cx="-10" cy="-1" r="10" fill="#f7f9fb" stroke="#9aa3ad" stroke-width="1.2"/>'
    s += '<path d="M-16,-5 Q-12,-9 -6,-8" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/>'
    s += '<rect x="10" y="-14" width="17" height="10" rx="2" fill="#2f3b45"/>'
    s += '<rect x="12" y="-12" width="9" height="2.5" rx="1" fill="#7fe0a8"/>'
    s += '<circle cx="13" cy="5" r="2.4" fill="%s"/><circle cx="20" cy="5" r="2.4" fill="#e8b23a"/><circle cx="27" cy="5" r="2.4" fill="#9aa3ad"/>' % OK
    return s


def _ic_pouch():
    """Busta per sterilizzazione: lato carta e lato film, strumento dentro, indicatore di processo."""
    s = '<g transform="rotate(-8)">'
    s += '<rect x="-30" y="-22" width="60" height="44" rx="3" fill="#f6f2e8" stroke="#a9a08a" stroke-width="1.4"/>'
    s += '<rect x="-26" y="-18" width="52" height="34" rx="2" fill="#dceaf4" opacity=".85"/>'
    s += '<rect x="-30" y="16" width="60" height="6" fill="#efe8d4"/>'
    s += _ln(-30, 16, 30, 16, '#a9a08a', 1, ' stroke-dasharray="3 2"')
    s += '<rect x="-20" y="-6" width="34" height="5" rx="2.5" fill="#9aa3ad" stroke="#5f6973" stroke-width=".8"/>'
    s += '<path d="M-20,-5.5 L-27,-8 L-27,1 L-20,-1 Z" fill="#9aa3ad" stroke="#5f6973" stroke-width=".8"/>'
    s += '<rect x="2" y="-15" width="16" height="5" rx="1.5" fill="#8a5a2b"/>'
    s += '<rect x="-24" y="5" width="22" height="3" rx="1.5" fill="#a9a08a" opacity=".6"/>'
    return s + '</g>'


def _ic_tap():
    """Rubinetto con acqua che scorre su uno strumento + panno per asciugare."""
    s = '<path d="M-28,-24 L-6,-24 Q4,-24 4,-14 L4,-10 L-4,-10 L-4,-14 Q-4,-16 -6,-16 L-28,-16 Z" fill="#9aa3ad" stroke="#5f6973" stroke-width="1.3"/>'
    s += '<rect x="-34" y="-28" width="8" height="16" rx="2" fill="#6f7983"/>'
    s += '<rect x="-20" y="-31" width="8" height="7" rx="2" fill="#6f7983"/>'
    s += '<path d="M-3,-10 L3,-10 L4,12 L-4,12 Z" fill="#bfe0f3" opacity=".9"/>'
    for (x, y) in [(-7, 4), (7, 8), (0, 16)]:
        s += '<path d="M%d,%d q3,4.5 0,6.5 q-3,-2 0,-6.5 z" fill="#7fbfe3"/>' % (x, y)
    s += '<rect x="-24" y="16" width="44" height="5" rx="2.5" fill="#9aa3ad" stroke="#5f6973" stroke-width=".8"/>'
    s += '<path d="M8,22 L32,14 L34,26 L12,30 Z" fill="#f4c9d6" stroke="#c98ea2" stroke-width="1.2"/>'
    s += _ln(14, 24, 30, 19, '#c98ea2', 1)
    return s


def _ic_register():
    """Registro: scontrino dell'autoclave e cartella con spunta."""
    s = '<rect x="-26" y="-24" width="40" height="50" rx="4" fill="#fff" stroke="#7d8792" stroke-width="1.5"/>'
    s += '<rect x="-14" y="-28" width="16" height="7" rx="2" fill="#9aa3ad"/>'
    for k in range(4):
        s += _ln(-19, -12 + k * 9, 6, -12 + k * 9, '#c9ced4', 2)
        s += '<path d="M-22,%d l2,2 l3,-4" stroke="%s" stroke-width="1.6" fill="none" stroke-linecap="round"/>' % (-11 + k * 9, OK)
    s += '<path d="M8,-6 L30,-6 L30,24 L27,21 L24,24 L21,21 L18,24 L15,21 L12,24 L8,21 Z" fill="#fbfbf8" stroke="#a9a08a" stroke-width="1.2"/>'
    for k in range(4):
        s += _ln(12, k * 5 - 1, 26 - (k % 2) * 5, k * 5 - 1, '#b9b4a6', 1.4)
    return s


def _ic_brushwash():
    """Detersione: spazzolino che strofina uno strumento nella bacinella con schiuma."""
    s = '<ellipse cx="0" cy="25" rx="32" ry="4" fill="#000" opacity=".08"/>'
    s += '<path d="M-30,0 L30,0 L25,22 Q24,25 20,25 L-20,25 Q-24,25 -25,22 Z" fill="#eef4f8" stroke="#7d8792" stroke-width="1.6"/>'
    s += '<path d="M-28,8 L28,8 L25,21 Q24,23 20,23 L-20,23 Q-24,23 -25,21 Z" fill="#cfe7f5"/>'
    for (x, y, r) in [(-18, 6, 5), (-9, 3, 6), (2, 5, 5), (12, 3, 6), (21, 6, 4.5), (-2, -2, 4), (9, -3, 3.5)]:
        s += '<circle cx="%d" cy="%d" r="%.1f" fill="#fff" stroke="#b8d6e8" stroke-width="1"/>' % (x, y, r)
    s += '<g transform="translate(6,-14) rotate(-28)"><rect x="-22" y="-5" width="30" height="10" rx="4" fill="#3d7fb3"/>'
    s += '<rect x="-20" y="5" width="26" height="6" fill="#f2f2f2" stroke="#cfd6dd" stroke-width=".8"/>'
    s += '<rect x="8" y="-3" width="20" height="6" rx="3" fill="#2f6a99"/></g>'
    return s



# ---------------------------------------------------------------- dita e mani "naturali" (usate anche da svg_a/b/c come gen_svg._digit)
_HAND, _HAND_D, _HAND_S = '#f2c9b0', '#e3b296', '#c98d72'


def _smooth(pts):
    """Curva Catmull-Rom (come comandi C) che passa per i punti dati, a partire dal primo (senza M)."""
    d = ''
    n = len(pts)
    for i in range(n - 1):
        p0 = pts[i - 1] if i > 0 else pts[i]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < n else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += ' C%.1f,%.1f %.1f,%.1f %.1f,%.1f' % (c1[0], c1[1], c2[0], c2[1], p2[0], p2[1])
    return d


def _digit(pts, ws, nail=1, view='side', fill=_HAND, stroke=_HAND_S, creases=(), nail_col='#f4c7d3', sw=1.4, knuckles=True):
    """Dito affusolato lungo la linea media pts (base -> punta) con semi-larghezze ws.
    nail = lato del dorso (+1 a sinistra della direzione di marcia, -1 a destra, 0 = nessuna unghia);
    view='side' mette l'unghia sul bordo dorsale, view='top' la centra (dorso verso chi guarda).
    creases = indici delle articolazioni (pieghe/nocche)."""
    n = len(pts)
    nrm = []
    for i in range(n):
        a = pts[max(i - 1, 0)]
        b = pts[min(i + 1, n - 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        L = math.hypot(dx, dy) or 1
        nrm.append((-dy / L, dx / L))
    left = [(p[0] + nn[0] * w, p[1] + nn[1] * w) for p, nn, w in zip(pts, nrm, ws)]
    right = [(p[0] - nn[0] * w, p[1] - nn[1] * w) for p, nn, w in zip(pts, nrm, ws)]
    tx, ty = pts[-1][0] - pts[-2][0], pts[-1][1] - pts[-2][1]
    L = math.hypot(tx, ty) or 1
    tx, ty = tx / L, ty / L
    w = ws[-1]
    tip = (pts[-1][0] + tx * w * 1.05, pts[-1][1] + ty * w * 1.05)
    nx, ny = nrm[-1]
    d = 'M%.1f,%.1f' % left[0] + _smooth(left)
    d += ' C%.1f,%.1f %.1f,%.1f %.1f,%.1f' % (left[-1][0] + tx * w * .55, left[-1][1] + ty * w * .55,
                                             tip[0] + nx * w * .6, tip[1] + ny * w * .6, tip[0], tip[1])
    d += ' C%.1f,%.1f %.1f,%.1f %.1f,%.1f' % (tip[0] - nx * w * .6, tip[1] - ny * w * .6,
                                             right[-1][0] + tx * w * .55, right[-1][1] + ty * w * .55, right[-1][0], right[-1][1])
    d += _smooth(right[::-1])
    # riempimento chiuso + contorno aperto alla base (così il dito si fonde con il dorso senza giunture)
    s = '<path d="%s Z" fill="%s"/>' % (d, fill)
    s += '<path d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round" stroke-linecap="round"/>' % (d, stroke, sw)
    # luce sul dorso
    if nail:
        side = left if nail > 0 else right
        sgn = 1 if nail > 0 else -1
        hl = [(p[0] - nn[0] * sgn * w * .45, p[1] - nn[1] * sgn * w * .45) for p, nn, w in zip(side, nrm, ws)]
        s += '<path d="M%.1f,%.1f%s" fill="none" stroke="#fff" stroke-width="%.1f" opacity=".22" stroke-linecap="round"/>' % (
            hl[1][0], hl[1][1], _smooth(hl[1:-1]), max(1.5, ws[0] * .3))
    # articolazioni: pieghe sul lato palmare, nocche (piccole pieghe) sul dorso
    for i in creases:
        p, nn, w = pts[i], nrm[i], ws[i]
        for sgn, k in ((1, .55), (-1, .55)):
            if not knuckles and sgn == (1 if nail >= 0 else -1):
                continue
            a = (p[0] + nn[0] * sgn * w * .98, p[1] + nn[1] * sgn * w * .98)
            b2 = (p[0] + nn[0] * sgn * w * (1 - k), p[1] + nn[1] * sgn * w * (1 - k))
            s += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="%s" stroke-width="1.1" fill="none" opacity=".55" stroke-linecap="round"/>' % (
                a[0], a[1], (a[0] + b2[0]) / 2 + tx * 2, (a[1] + b2[1]) / 2 + ty * 2, b2[0], b2[1], stroke)
    # unghia
    if nail:
        sgn = 1 if nail > 0 else -1
        p1 = pts[-1]
        ln_ = w * 1.5
        if view == 'top':
            # unghia centrata: ovale allungato verso la punta
            c0 = (p1[0] - tx * ln_ * .55 + tx * w * .25, p1[1] - ty * ln_ * .55 + ty * w * .25)
            ang = math.degrees(math.atan2(ty, tx))
            s += ('<g transform="translate(%.1f,%.1f) rotate(%.1f)"><path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,0 %.1f,%.1f L%.1f,%.1f Q%.1f,0 %.1f,%.1f Z" '
                  'fill="%s" stroke="%s" stroke-width="1"/><rect x="%.1f" y="%.1f" width="%.1f" height="2" rx="1" fill="#fff" opacity=".6"/></g>'
                  % (c0[0], c0[1], ang, -ln_ * .5, -w * .62, ln_ * .5, -w * .62, ln_ * .5 + w * .5, ln_ * .5, w * .62, -ln_ * .5, w * .62,
                     -ln_ * .5 - w * .12, -ln_ * .5, -w * .62, nail_col, NAIL_S, -ln_ * .3, -w * .35, ln_ * .55))
        else:
            # unghia di profilo: lamina sottile sul bordo dorsale verso la punta
            e = lambda t, off: (p1[0] - tx * t + nrm[-1][0] * sgn * off, p1[1] - ty * t + nrm[-1][1] * sgn * off)
            a0, a1 = e(ln_, w * .98), e(-w * .55, w * .62)
            b0, b1 = e(ln_, w * .62), e(-w * .45, w * .3)
            s += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1"/>'
                  % (a0[0], a0[1], e(-w * .1, w * 1.08)[0], e(-w * .1, w * 1.08)[1], a1[0], a1[1],
                     e(-w * .62, w * .42)[0], e(-w * .62, w * .42)[1], b1[0], b1[1],
                     e(ln_ * .4, w * .6)[0], e(ln_ * .4, w * .6)[1], b0[0], b0[1], nail_col, NAIL_S))
    return s


def _blob(pts, fill=_HAND, stroke=_HAND_S, sw=1.4, extra=''):
    """Forma chiusa morbida (dorso, palmo, avambraccio) che passa per i punti dati (Catmull-Rom chiusa)."""
    n = len(pts)
    d = 'M%.1f,%.1f' % pts[0]
    for i in range(n):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
        d += ' C%.1f,%.1f %.1f,%.1f %.1f,%.1f' % (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6,
                                                 p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6, p2[0], p2[1])
    return '<path d="%s Z" fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round"%s/>' % (d, fill, stroke, sw, extra)


LOGO_INNER = (
    '<defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d2668a"/>'
    '<stop offset="1" stop-color="#8e3b5a"/></linearGradient></defs>'
    '<rect width="64" height="64" rx="16" fill="url(#lg)"/>'
    # boccetta di smalto: tappo, collo, corpo con smalto e riflesso
    '<rect x="25" y="7" width="14" height="19" rx="3.5" fill="#fff"/>'
    '<rect x="22" y="24" width="20" height="6" rx="2" fill="#fff"/>'
    '<rect x="14" y="29" width="36" height="28" rx="9" fill="#fff"/>'
    '<rect x="18" y="35" width="28" height="18" rx="6" fill="#f3a9c0"/>'
    '<rect x="21" y="37" width="4" height="12" rx="2" fill="#fff" opacity=".75"/>'
    # scintilla
    '<path d="M50 8 C50.8 12.2 51.8 13.2 56 14 C51.8 14.8 50.8 15.8 50 20 C49.2 15.8 48.2 14.8 44 14 C48.2 13.2 49.2 12.2 50 8 Z" fill="#fff"/>'
)


@fig('logo.svg')
def logo():
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><title>NailX</title>%s</svg>\n' % LOGO_INNER


# ---------- immagine di copertina (hero) ----------
_HW, _HH = 600, 420


def _hero_finger(bx, by, ang, L, w0, w1, free, nail='url(#nailG)', gid='skinF', accent=None):
    """Dito visto dal dorso, base in (bx,by), puntato verso l'alto ruotato di ang gradi."""
    r = w1 / 2
    body = ('M%.1f,0 C%.1f,%.1f %.1f,%.1f %.1f,%.1f A%.1f,%.1f 0 0 1 %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,0 Z'
            % (-w0 / 2, -w0 / 2, -L * .45, -r, -L * .62, -r, -L + r, r, r, r, -L + r, r, -L * .62, w0 / 2, -L * .45, w0 / 2))
    nw = w1 * .80
    yc = -L + w1 * 1.95          # cuticola
    ys = -L + w1 * .62           # fine del letto (punto in cui la lamina lascia il dito)
    yt = -L - free               # punta della mandorla
    hw = nw / 2
    nailp = ('M%.1f,%.1f L%.1f,%.1f C%.1f,%.1f %.1f,%.1f 0,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f Q0,%.1f %.1f,%.1f Z'
             % (-hw, yc, -hw * 1.03, ys, -hw * 1.04, ys - free * .62, -hw * .58, yt, yt,
                hw * .58, yt, hw * 1.04, ys - free * .62, hw * 1.03, ys, hw, yc, yc + nw * .42, -hw, yc))
    s = '<g transform="translate(%.1f,%.1f) rotate(%.1f)">' % (bx, by, ang)
    s += '<path d="%s" fill="url(#%s)" stroke="#d99c80" stroke-width="1"/>' % (body, gid)
    # piega dell'eponichio (ombra morbida sopra la cuticola)
    s += '<path d="M%.1f,%.1f Q0,%.1f %.1f,%.1f" fill="none" stroke="#e2a98e" stroke-width="2.2" stroke-linecap="round" opacity=".7"/>' % (
        -hw - 2, yc - 1, yc + nw * .5 + 3, hw + 2, yc - 1)
    # nocca distale
    s += '<path d="M%.1f,%.1f q%.1f,-3 %.1f,0" fill="none" stroke="#dca085" stroke-width="1.1" opacity=".55" stroke-linecap="round"/>' % (
        -w0 * .22, -L * .42, w0 * .22, w0 * .44)
    # ombra portata dell'unghia sul dito
    s += '<path d="%s" fill="#b8556f" opacity=".18" transform="translate(1.5,2.5)"/>' % nailp
    s += '<path d="%s" fill="%s" stroke="#9c2f57" stroke-width="1"/>' % (nailp, nail)
    if accent:
        s += accent(hw, yc, ys, yt, nailp)
    # riflessi: banda lunga + punto luce
    s += ('<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" stroke="#fff" stroke-width="%.1f" stroke-linecap="round" opacity=".75"/>'
          % (-hw * .45, yc - 6, -hw * .62, ys, -hw * .55, ys - free * .5, -hw * .2, yt + free * .22, max(2.4, nw * .13)))
    s += '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="#fff" opacity=".55"/>' % (hw * .38, yc - (yc - ys) * .35, nw * .07, (yc - ys) * .16)
    return s + '</g>'


def _hero_glitter(hw, yc, ys, yt, nailp):
    rnd = random.Random(7)
    out = '<clipPath id="gclip"><path d="%s"/></clipPath><g clip-path="url(#gclip)">' % nailp
    out += '<path d="%s" fill="url(#chromeG)"/>' % nailp
    for _ in range(46):
        x = rnd.uniform(-hw, hw)
        y = rnd.uniform(yt, ys + (yc - ys) * .55)
        r = rnd.uniform(.5, 1.5)
        out += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" opacity="%.2f"/>' % (x, y, r, rnd.choice(['#fff', '#f9e3b0', '#f4c6d6']), rnd.uniform(.6, 1))
    return out + '</g>'


def _hero_sparkle(x, y, r, op=.95, col='#fff'):
    return ('<path d="M{x},{a} C{x1},{b1} {x2},{c1} {x3},{y} C{x2},{c2} {x1},{b2} {x},{d} C{x4},{b2} {x5},{c2} {x6},{y} C{x5},{c1} {x4},{b1} {x},{a} Z" fill="{col}" opacity="{op}"/>'
            .format(x=x, y=y, a=y - r, d=y + r, x1=x + r * .12, x2=x + r * .28, x3=x + r, x4=x - r * .12, x5=x - r * .28, x6=x - r,
                    b1=y - r * .28, c1=y - r * .12, c2=y + r * .12, b2=y + r * .28, col=col, op=op))


def _hero_leaf_sprig(x, y, ang, n=5, L=90):
    s = '<g transform="translate(%d,%d) rotate(%d)">' % (x, y, ang)
    s += '<path d="M0,0 C4,-%d 2,-%d -4,-%d" stroke="#8fa98a" stroke-width="2" fill="none" stroke-linecap="round"/>' % (L * .4, L * .75, L)
    for i in range(n):
        t = (i + 1) / (n + .6)
        yy = -L * t
        side = 1 if i % 2 else -1
        s += ('<g transform="translate(%.1f,%.1f) rotate(%d)"><path d="M0,0 C6,-9 18,-10 24,-4 C18,4 6,5 0,0 Z" fill="url(#leafG)"/>'
              '<path d="M1,0 C8,-4 15,-5 22,-4" stroke="#7e9879" stroke-width=".8" fill="none" opacity=".7"/></g>') % (
            2 - 3 * t, yy, -35 if side > 0 else -145)
    return s + '</g>'


def _hero_bottle(x, y):
    """Boccetta di smalto con logo; (x,y) = base al centro."""
    s = '<g transform="translate(%d,%d)">' % (x, y)
    s += '<ellipse cx="0" cy="2" rx="40" ry="7" fill="#c98a9e" opacity=".25"/>'
    # corpo in vetro
    s += '<rect x="-36" y="-78" width="72" height="80" rx="18" fill="url(#glassG)" stroke="#e7b9c8" stroke-width="1.2"/>'
    s += '<rect x="-30" y="-70" width="60" height="66" rx="14" fill="url(#polishG)"/>'
    s += '<rect x="-25" y="-66" width="7" height="52" rx="3.5" fill="#fff" opacity=".45"/>'
    # etichetta
    s += '<rect x="-17" y="-48" width="34" height="22" rx="5" fill="#fff" opacity=".92"/>'
    s += '<text x="0" y="-33" text-anchor="middle" font-size="11" font-weight="800" fill="#8e3b5a" letter-spacing=".3">Nail<tspan fill="#c2577a">X</tspan></text>'
    # collo e tappo
    s += '<rect x="-14" y="-88" width="28" height="12" rx="3" fill="#f2d6df"/>'
    s += '<rect x="-15" y="-150" width="30" height="64" rx="6" fill="url(#capG)"/>'
    s += '<rect x="-10" y="-146" width="5" height="56" rx="2.5" fill="#fff" opacity=".22"/>'
    return s + '</g>'


def _hero_jar(x, y):
    s = '<g transform="translate(%d,%d)">' % (x, y)
    s += '<ellipse cx="0" cy="2" rx="34" ry="6" fill="#c98a9e" opacity=".22"/>'
    s += '<path d="M-30,-30 L-30,-4 Q-30,2 -24,2 L24,2 Q30,2 30,-4 L30,-30 Z" fill="url(#glassG)" stroke="#e7b9c8" stroke-width="1.2"/>'
    s += '<path d="M-26,-22 L-26,-6 Q-26,-2 -22,-2 L22,-2 Q26,-2 26,-6 L26,-22 Z" fill="#f7c9d6"/>'
    s += '<rect x="-32" y="-46" width="64" height="18" rx="5" fill="url(#capG)"/>'
    s += '<rect x="-26" y="-43" width="20" height="3" rx="1.5" fill="#fff" opacity=".3"/>'
    s += '<rect x="-22" y="-18" width="5" height="12" rx="2.5" fill="#fff" opacity=".5"/>'
    return s + '</g>'


def _hero_defs():
    d = '<defs>'
    d += ('<linearGradient id="bgG" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff5f8"/>'
          '<stop offset=".55" stop-color="#fce6ee"/><stop offset="1" stop-color="#f7d6e2"/></linearGradient>')
    d += ('<radialGradient id="glowG" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#fff" stop-opacity=".95"/>'
          '<stop offset=".6" stop-color="#fff" stop-opacity=".35"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>')
    d += ('<linearGradient id="skinF" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9b49a"/>'
          '<stop offset=".3" stop-color="#f7d8c7"/><stop offset=".55" stop-color="#fbe3d6"/><stop offset="1" stop-color="#e6ad92"/></linearGradient>')
    d += ('<linearGradient id="skinT" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e3a98d"/>'
          '<stop offset=".45" stop-color="#f6d4c2"/><stop offset="1" stop-color="#e8b29a"/></linearGradient>')
    d += ('<radialGradient id="backG" cx=".45" cy=".25" r=".85"><stop offset="0" stop-color="#fbe2d4"/>'
          '<stop offset=".55" stop-color="#f3cbb6"/><stop offset="1" stop-color="#e4a98c"/></radialGradient>')
    d += ('<linearGradient id="nailG" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#e2557f"/>'
          '<stop offset=".55" stop-color="#d23e6c"/><stop offset="1" stop-color="#b52c5a"/></linearGradient>')
    d += ('<linearGradient id="chromeG" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#f9d7e2"/>'
          '<stop offset=".35" stop-color="#f3b4c9"/><stop offset=".6" stop-color="#fbe9ef"/><stop offset="1" stop-color="#e693b0"/></linearGradient>')
    d += ('<linearGradient id="glassG" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity=".9"/>'
          '<stop offset=".5" stop-color="#fdeef3" stop-opacity=".7"/><stop offset="1" stop-color="#f6d3df" stop-opacity=".9"/></linearGradient>')
    d += ('<linearGradient id="polishG" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e6608a"/>'
          '<stop offset="1" stop-color="#b52c5a"/></linearGradient>')
    d += ('<linearGradient id="capG" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#6a2f45"/>'
          '<stop offset=".45" stop-color="#9a4a68"/><stop offset="1" stop-color="#4f2133"/></linearGradient>')
    d += ('<linearGradient id="cushG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fffafb"/>'
          '<stop offset="1" stop-color="#f3d9e2"/></linearGradient>')
    d += ('<linearGradient id="leafG" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#a9c2a2"/>'
          '<stop offset="1" stop-color="#cfdec9"/></linearGradient>')
    d += '<filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#a2456a" flood-opacity=".18"/></filter>'
    d += '<filter id="blur8"><feGaussianBlur stdDeviation="8"/></filter>'
    return d + '</defs>'


def _hero_hero_body():
    b = _hero_defs()
    b += '<rect width="%d" height="%d" fill="url(#bgG)"/>' % (_HW, _HH)
    # forme decorative di sfondo
    b += '<circle cx="330" cy="190" r="168" fill="#f9d3df" opacity=".55"/>'
    b += '<circle cx="330" cy="190" r="168" fill="none" stroke="#f1b9cb" stroke-width="1.2" stroke-dasharray="2 7" opacity=".9"/>'
    b += '<ellipse cx="320" cy="170" rx="190" ry="150" fill="url(#glowG)"/>'
    b += '<circle cx="548" cy="64" r="34" fill="#f7cad9" opacity=".6"/><circle cx="52" cy="92" r="22" fill="#f7cad9" opacity=".5"/>'
    b += _hero_leaf_sprig(512, 350, -24, 6, 140)
    b += _hero_leaf_sprig(548, 352, 10, 5, 110)
    b += _hero_leaf_sprig(70, 350, 20, 4, 90)
    # piano
    b += '<path d="M0,352 C150,340 450,340 600,352 L600,420 L0,420 Z" fill="#f6dbe4"/>'
    # cuscino poggiamano
    b += '<g filter="url(#soft)"><path d="M190,360 C190,330 240,322 330,322 C420,322 470,330 470,360 C470,392 420,400 330,400 C240,400 190,392 190,360 Z" fill="url(#cushG)"/>'
    b += '<path d="M206,360 C220,342 440,342 454,360" fill="none" stroke="#efc6d4" stroke-width="1.4" stroke-dasharray="3 5"/></g>'
    # prodotti
    b += _hero_bottle(108, 372)
    b += _hero_jar(188, 392)
    # lima appoggiata
    b += ('<g transform="translate(468,392) rotate(-6)"><rect x="0" y="-7" width="118" height="14" rx="7" fill="#f4e6dd" stroke="#e3cbbd"/>'
          '<rect x="5" y="-4.5" width="108" height="9" rx="4.5" fill="#d9b8c4"/><rect x="5" y="-4.5" width="54" height="9" rx="4.5" fill="#c99aab"/></g>')
    # mano
    h = '<g filter="url(#soft)" transform="translate(4,-6) rotate(-4 330 330)">'
    # pollice
    h += _hero_finger(280, 336, -38, 92, 42, 28, 15, gid='skinT')
    fingers = [(292, 270, -9, 150, 35, 29, 23), (324, 260, -2, 166, 36, 30, 25), (356, 264, 5, 156, 34, 28, 24), (386, 282, 12, 124, 29, 24, 19)]
    for i, (bx, by, a, L, w0, w1, fr) in enumerate(fingers):
        h += _hero_finger(bx, by, a, L, w0, w1, fr, accent=_hero_glitter if i == 2 else None)
    # dorso (senza contorno in alto, così le dita si fondono)
    back = ('M272,266 C288,252 306,248 324,248 C348,248 376,254 398,272 C410,290 408,314 400,334 C390,360 374,382 368,420 '
            'L306,420 C302,394 286,374 276,352 C268,334 262,312 264,292 C265,282 268,272 272,266 Z')
    h += '<path d="%s" fill="url(#backG)"/>' % back
    h += '<path d="M398,272 C410,290 408,314 400,334 C390,360 374,382 368,420" fill="none" stroke="#d99c80" stroke-width="1"/>'
    h += '<path d="M306,420 C302,394 286,374 276,352" fill="none" stroke="#d99c80" stroke-width="1"/>'
    # attacco del pollice: ombra morbida
    h += '<path d="M268,318 C276,336 286,350 296,360" fill="none" stroke="#e3ad93" stroke-width="2" opacity=".55" stroke-linecap="round"/>'
    # tendini e nocche, appena accennati
    for x, y in [(295, 264), (325, 256), (356, 260), (384, 276)]:
        h += '<path d="M%d,%d q8,-4 16,0" stroke="#dca085" stroke-width="1.2" fill="none" opacity=".5" stroke-linecap="round"/>' % (x - 8, y + 8)
    h += '<path d="M314,292 C318,320 320,350 320,384" stroke="#e6b39b" stroke-width="2" fill="none" opacity=".45" stroke-linecap="round"/>'
    h += '<path d="M360,292 C358,322 356,350 356,384" stroke="#e6b39b" stroke-width="2" fill="none" opacity=".45" stroke-linecap="round"/>'
    h += '</g>'
    b += h
    # scintille
    for x, y, r, op in [(176, 118, 12, .95), (204, 150, 6, .8), (470, 128, 10, .95), (496, 160, 5, .8), (440, 60, 6, .7), (140, 220, 5, .7)]:
        b += _hero_sparkle(x, y, r, op)
    b += _hero_sparkle(447, 228, 7, .9, '#f6d48f')
    return b


@fig('hero.svg')
def hero():
    return svg(_HW, _HH, _hero_hero_body(), 'Mano con unghie ricostruite a mandorla, smalto e prodotti NailX')


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
    gid, defs = _skinv(140, 340)
    b = defs
    # dito: dorso, piega prossimale, polpastrello
    b += ('<path d="M40,146 L330,144 C366,144 392,150 404,163 L650,177 C700,178 726,206 726,246 C726,300 684,334 612,334 '
          'L40,334 Z" fill="url(#%s)" stroke="%s" stroke-width="1.6"/>' % (gid, SKIN_D))
    # falange distale con tuberosità
    b += ('<path d="M52,224 C150,214 360,212 470,214 C540,214 584,222 604,238 C618,250 608,268 586,270 C550,272 520,266 470,266 '
          'C360,268 150,272 52,276 Z" fill="#efe3d0" stroke="#cdb894" stroke-width="1.5"/>')
    b += '<path d="M90,232 C200,226 380,224 470,226" stroke="#fff" stroke-width="3" opacity=".6" fill="none" stroke-linecap="round"/>'
    # letto ungueale (capillari) e matrice
    b += '<path d="M430,176 L650,179 C664,180 671,185 669,192 L430,191 Z" fill="#ee8ea7"/>'
    for k in range(9):
        b += '<line x1="%d" y1="179" x2="%d" y2="190" stroke="#d9577c" stroke-width="1" opacity=".55"/>' % (446 + k * 24, 442 + k * 24)
    b += '<path d="M346,168 Q352,196 432,192 L432,178 Q382,177 352,163 Z" fill="#d9577c"/>'
    # lamina ungueale (dalla radice sotto la piega fino al bordo libero)
    b += ('<path d="M348,160 C460,156 610,159 752,165 Q760,170 752,175 C610,171 460,172 350,170 Q344,165 348,160 Z" '
          'fill="#f7d4dd" stroke="%s" stroke-width="1.6"/>' % NAIL_S)
    b += '<path d="M440,161 C540,159 640,161 730,166" stroke="#fff" stroke-width="2" opacity=".75" fill="none" stroke-linecap="round"/>'
    # piega prossimale (eponichio) sopra la radice
    b += ('<path d="M300,145 L330,144 C366,144 392,150 405,163 Q380,166 350,163 Q322,158 300,157 Z" fill="url(#%s)"/>' % gid)
    b += '<path d="M300,145 L330,144 C366,144 392,150 405,163" stroke="%s" stroke-width="1.6" fill="none"/>' % SKIN_D
    # cuticola sulla lamina
    b += '<path d="M405,161 Q424,159 448,159" stroke="#fff" stroke-width="4" opacity=".95" fill="none" stroke-linecap="round"/>'
    # iponichio
    b += '<path d="M650,179 Q666,181 672,194" stroke="#d98a73" stroke-width="3" fill="none" stroke-linecap="round"/>'
    # punto di stress
    b += '<circle cx="662" cy="170" r="7" fill="none" stroke="%s" stroke-width="2.5"/>' % ERR
    b += leader(420, 152, 330, 92, 'Eponichio (piega prossimale)', 'end')
    b += leader(436, 159, 470, 62, 'Cuticola', 'start')
    b += leader(560, 160, 600, 96, 'Lamina ungueale', 'start')
    b += leader(662, 163, 728, 112, 'Punto di stress', 'start')
    b += leader(748, 170, 790, 148, 'Bordo libero', 'start')
    b += leader(390, 184, 360, 382, 'Matrice (produce la lamina)', 'middle')
    b += leader(560, 186, 560, 382, 'Letto ungueale', 'middle')
    b += leader(670, 190, 770, 382, 'Iponichio (barriera)', 'middle')
    b += leader(220, 246, 140, 382, 'Falange distale (osso)', 'middle')
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
    b += text(xa - 22, oy - 30, '≈1 mm dalla pelle', 15, 'end', 600, MUTED)
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
        b += text(x + 140, 265, sub, 15, weight=600, fill=OK if ok else ERR)
    b += text(470, 310, 'Il pallino rosso indica il punto di stress: l\'apex deve stare lì sopra.', 15, fill=MUTED)
    return svg(940, 330, b, 'Apex corretto, piatto e troppo spesso a confronto')


@fig('curva-c.svg')
def ccurve():
    b = text(40, 40, 'Curva a C – vista frontale dal bordo libero', 20, 'start', 800, ACC2)
    for i, (k, lab, sub, hw) in enumerate([(12, 'Bassa (piatta)', 'unghie piatte, corte', 74), (26, 'Media', 'uso quotidiano', 70),
                                           (42, 'Alta (pinching)', 'gara / unghie lunghe', 62)]):
        cx = 150 + i * 260
        b += _ctip(cx, 160, k, hw=hw, col='#eaa0b6')
        # misura della curva: freccia tra corda e colmo
        b += '<line x1="%d" y1="160" x2="%d" y2="160" stroke="%s" stroke-dasharray="4 4"/>' % (cx - hw - 14, cx + hw + 14, MUTED)
        b += text(cx, 290, lab, 16, weight=800)
        b += text(cx, 312, sub, 15, fill=MUTED)
    b += text(410, 346, 'La curva segue quella naturale della cliente: non esiste un valore unico per tutti.', 14, fill=MUTED)
    return svg(820, 365, arrow_defs() + b, 'Curva a C bassa, media e alta vista dal bordo libero')


SHAPES = [('quadrata', 'Quadrata', 'Netta, accorcia il dito'), ('squoval', 'Squoval', 'Robusta, la più versatile'),
          ('tonda', 'Tonda', 'Corta, pratica'), ('ovale', 'Ovale', 'Elegante, allunga'),
          ('mandorla', 'Mandorla', 'Slancia molto il dito'), ('stiletto', 'Stiletto', 'A punta, serve lunghezza'),
          ('ballerina', 'Ballerina / Coffin', 'Rastremata, punta piatta'), ('lipstick', 'Lipstick', 'Taglio obliquo')]


@fig('forme.svg')
def forme():
    b = text(30, 36, 'Le 8 forme principali', 20, 'start', 800, ACC2)
    for i, (sh, name, sub) in enumerate(SHAPES):
        col, row = i % 4, i // 4
        cx, yc = 118 + col * 215, 236 + row * 282
        b += '<rect x="%d" y="%d" width="196" height="262" rx="16" fill="%s"/>' % (cx - 98, yc - 184, PANEL)
        f, _ = finger_nail(cx, yc, hw=34, nail_len=78, free_len=66 if sh not in ('quadrata', 'squoval', 'tonda') else 44,
                           shape=sh, smile=10, finger_len=22)
        b += f
        b += text(cx, yc + 46, name, 16, weight=800)
        b += text(cx, yc + 68, sub, 14.5, fill=MUTED)
    return svg(880, 606, b, 'Le otto forme principali dell\'unghia')


@fig('lime-grane.svg')
def grit():
    b = text(40, 40, 'Grane delle lime: più il numero è basso, più la lima è aggressiva', 19, 'start', 800, ACC2)
    segs = [('80–100', 'Accorciare, togliere', 'materiale artificiale', '#5b4a44', '#2e2420', 2.1, 6),
            ('100/180', 'Dare forma alla', 'ricostruzione', '#8a7469', '#55443d', 1.5, 5),
            ('180–240', 'Unghia naturale,', 'opacizzare, rifinire', '#c3ad9f', '#8d7768', 1.0, 4),
            ('240+ / buffer', 'Levigare e', 'lucidare', '#ece1d8', '#c9b9ab', .6, 3)]
    # scala continua
    gid = uid('gs')
    b += ('<defs><linearGradient id="%s" x1="0" x2="1"><stop offset="0" stop-color="#5b4a44"/><stop offset="1" stop-color="#ece1d8"/>'
          '</linearGradient></defs>' % gid)
    b += '<rect x="80" y="66" width="720" height="10" rx="5" fill="url(#%s)"/>' % gid
    b += text(80, 98, '◀ più abrasiva', 15, 'start', 700, MUTED)
    b += text(800, 98, 'più fine ▶', 15, 'end', 700, MUTED)
    for i, (lab, l1, l2, col, dot, r, step) in enumerate(segs):
        cx = 140 + i * 200
        b += '<rect x="%d" y="108" width="180" height="250" rx="16" fill="%s"/>' % (cx - 90, PANEL)
        # superficie abrasiva (granulometria visibile) sulla lima vista dall'alto
        pid = uid('gp')
        rng = random.Random(3 + i)
        T = 24
        grains = ''.join('<circle cx="%.1f" cy="%.1f" r="%.2f" fill="%s"/>' % (
            rng.uniform(0, T), rng.uniform(0, T), r * rng.uniform(.7, 1.25), dot if k % 3 else '#ffffff" opacity=".45')
            for k in range(int(T * T / (step * step) * 1.6)))
        b += ('<defs><pattern id="%s" width="%d" height="%d" patternUnits="userSpaceOnUse"><rect width="%d" height="%d" fill="%s"/>%s</pattern></defs>'
              % (pid, T, T, T, T, col, grains))
        if i < 3:
            b += '<g filter="url(#nxShS)"><rect x="%d" y="126" width="56" height="150" rx="28" fill="#efe7df" stroke="#cbbdb0"/>' % (cx - 28)
            b += '<rect x="%d" y="130" width="48" height="142" rx="24" fill="url(#%s)"/></g>' % (cx - 24, pid)
        else:
            # buffer: blocchetto spesso con facce di grana diversa
            b += '<g filter="url(#nxShS)"><rect x="%d" y="132" width="58" height="140" rx="10" fill="#f6efe8" stroke="#cbbdb0"/>' % (cx - 34)
            b += '<rect x="%d" y="136" width="44" height="132" rx="7" fill="url(#%s)"/>' % (cx - 30, pid)
            b += '<path d="M%d,136 L%d,128 L%d,128 L%d,264 L%d,272 Z" fill="#e0d3c7" stroke="#cbbdb0"/></g>' % (cx + 24, cx + 34, cx + 34, cx + 34, cx + 24)
        # zoom sulla grana
        b += '<circle cx="%d" cy="166" r="17" fill="url(#%s)" stroke="#fff" stroke-width="3" filter="url(#nxShS)"/>' % (cx + 52, pid)
        b += text(cx, 300, lab, 16, weight=800, fill=INK)
        b += mtext(cx, 323, [l1, l2], 15, fill=MUTED)
    b += '<rect x="60" y="374" width="760" height="40" rx="10" fill="#fbe7e4"/>'
    b += text(440, 399, 'Sulla lamina naturale non scendere sotto 180: serve solo togliere la lucidità, mai assottigliare.', 14, weight=700, fill=ERR)
    return svg(880, 430, b, 'Scala delle grane delle lime, dalla più abrasiva alla più fine')


@fig('punte-fresa.svg')
def bits():
    b = text(40, 40, 'Punte per fresa: forme, colori e velocità', 20, 'start', 800, ACC2)
    dpat = uid('dm')
    cpat = uid('cb')
    b += ('<defs><pattern id="%s" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="4" fill="#b7bfc7"/>'
          '<circle cx="1" cy="1" r=".9" fill="#6f7983"/><circle cx="3" cy="3" r=".7" fill="#fff"/></pattern>'
          '<pattern id="%s" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(30)"><rect width="6" height="6" fill="#aeb6bf"/>'
          '<rect width="2.2" height="6" fill="#68727d"/></pattern></defs>' % (dpat, cpat))
    items = [('Cilindro', ['superficie,', 'accorciare'], 'cyl', '#4a7fd4', cpat),
             ('Cil. sicurezza', ['bordo liscio:', 'lati e cuticola'], 'safe', '#e05252', cpat),
             ('Cono', ['sotto il bordo', 'libero, lati'], 'cone', '#e05252', dpat),
             ('Fiamma', ['zona cuticolare,', 'cuticola'], 'flame', '#f2c94c', dpat),
             ('Pallina', ['pulizia cuticole', 'e solchi'], 'ball', '#4a7fd4', dpat),
             ('Mandrino', ['con rullino', 'abrasivo monouso'], 'mand', None, None)]
    heads = {'cyl': '<rect x="-15" y="-54" width="30" height="54" rx="2"/>',
             'safe': '<path d="M-15,0 L-15,-40 Q-15,-54 0,-54 Q15,-54 15,-40 L15,0 Z"/>',
             'cone': '<path d="M-15,0 L-4,-62 Q0,-66 4,-62 L15,0 Z"/>',
             'flame': '<path d="M-9,0 C-16,-22 -7,-46 0,-64 C7,-46 16,-22 9,0 Z"/>',
             'ball': '<circle cx="0" cy="-14" r="14"/>'}
    for i, (n, sub, kind, band, pat) in enumerate(items):
        x, y = 90 + i * 140, 168
        s = '<rect x="-4.5" y="0" width="9" height="78" rx="2" fill="#9aa3ad" stroke="#6f7983" stroke-width=".8"/>'
        s += '<line x1="-2" y1="4" x2="-2" y2="74" stroke="#fff" stroke-width="1.5" opacity=".6"/>'
        if kind == 'mand':
            s += '<rect x="-6" y="-58" width="12" height="62" rx="3" fill="#9aa3ad" stroke="#6f7983"/>'
            s += '<rect x="-17" y="-52" width="34" height="46" rx="4" fill="#cdb79e" stroke="#9c8364" stroke-width="1.2"/>'
            for k in range(6):
                s += '<line x1="-17" y1="%d" x2="17" y2="%d" stroke="#9c8364" stroke-width=".9" opacity=".7"/>' % (-48 + k * 8, -44 + k * 8)
            s += '<rect x="-12" y="-50" width="4" height="42" rx="2" fill="#fff" opacity=".35"/>'
        else:
            s += '<rect x="-7" y="-4" width="14" height="10" rx="2" fill="%s" stroke="#00000033"/>' % band
            s += '<g fill="url(#%s)" stroke="#5f6973" stroke-width="1.3">%s</g>' % (pat, heads[kind])
            if kind == 'safe':
                s += '<path d="M-10,-44 Q0,-56 10,-44" stroke="#fff" stroke-width="3" fill="none" opacity=".9"/>'
        b += '<g transform="translate(%d,%d)" filter="url(#nxShS)">%s</g>' % (x, y, s)
        b += text(x, 276, n, 16, weight=700)
        b += mtext(x, 297, sub, 15, fill=MUTED)
    b += text(160, 92, 'carburo: lame a spirale', 15, fill=MUTED)
    b += text(370, 92, 'diamantata: granuli', 15, fill=MUTED)
    # codici colore
    b += text(40, 368, 'Codice colore della grana (indicativo, varia tra marchi)', 15, 'start', 700)
    for i, (c, l) in enumerate([('#f2c94c', 'Extra fine'), ('#e05252', 'Fine'), ('#4a7fd4', 'Media'),
                                ('#3aa35b', 'Grossa'), ('#333333', 'Extra grossa')]):
        x = 60 + i * 165
        b += '<rect x="%d" y="380" width="30" height="16" rx="4" fill="%s"/>' % (x, c)
        b += '<rect x="%d" y="384" width="30" height="3" fill="#fff" opacity=".35"/>' % x
        b += text(x + 38, 393, l, 15, 'start')
    # RPM
    b += text(40, 436, 'Velocità indicative (RPM)', 15, 'start', 700)
    for i, (lab, a, z, col) in enumerate([('Cuticola / unghia naturale', 5000, 10000, OK),
                                          ('Sfumare la superficie', 10000, 15000, WARN),
                                          ('Rimuovere prodotto', 15000, 25000, ERR)]):
        y = 450 + i * 32
        b += text(270, y + 15, lab, 15, 'end')
        x1, x2 = 290 + a / 30000 * 500, 290 + z / 30000 * 500
        b += '<rect x="290" y="%d" width="500" height="20" rx="10" fill="#f0e6e2"/>' % y
        b += '<rect x="%.1f" y="%d" width="%.1f" height="20" rx="10" fill="%s"/>' % (x1, y, x2 - x1, col)
        b += text(x2 + 8, y + 15, '%s–%s' % (format(a, ',').replace(',', '.'), format(z, ',').replace(',', '.')), 15, 'start', 600)
    b += mtext(450, 572, ['Carburo solo su prodotto artificiale · diamantate su unghia naturale e cuticola', 'pressione leggera, punta sempre in movimento'], 15, fill=MUTED)
    return svg(900, 608, b, 'Punte per fresa elettrica, codici colore e velocità')


@fig('preparazione.svg')
def prep():
    b = ''
    titles = ['Igienizza mani e strumenti', 'Arretra la cuticola', 'Rimuovi la cuticola',
              'Opacizza (grana 180–240)', 'Elimina la polvere', 'Disidratante + primer']
    notes = ['gel o spray igienizzante', 'spingicuticole quasi piatto', 'solo la pellicina sulla lamina',
             'via la lucidità, non lo spessore', 'pennello pulito e asciutto', 'solo sulla lamina, poco prodotto']
    for i, t in enumerate(titles):
        col, row = i % 3, i // 3
        x, y = 20 + col * 300, 20 + row * 300
        b += panel(x, y, 280, 280, t, i + 1)
        b += text(x + 140, y + 66, notes[i], 15, fill=MUTED)
        cx, yc = x + 120, y + 236
        extra = ''
        if i == 2:
            extra = '<path d="M%d,%d Q%d,%d %d,%d" stroke="#fff" stroke-width="7" fill="none" opacity=".9" stroke-linecap="round" clip-path="url(#CLIP)"/>' % (
                cx - 36, yc - 30, cx, yc - 50, cx + 36, yc - 30)
        if i >= 3:
            pid = uid('mt')
            extra = ('<defs><pattern id="%s" width="4" height="4" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".8" fill="#fff" opacity=".8"/>'
                     '<circle cx="3" cy="3" r=".6" fill="#b9496f" opacity=".25"/></pattern></defs>' % pid)
            extra += '<rect x="%d" y="%d" width="%d" height="140" fill="url(#%s)" clip-path="url(#CLIP)"/>' % (
                cx - 40, yc - 140, 80 if i > 3 else 46, pid)
        f, p = finger_nail(cx, yc, hw=38, nail_len=108, free_len=16, shape='tonda', smile=8, finger_len=40, extra=extra)
        b += f
        if i == 0:
            # flacone con erogatore spray e nebulizzazione verso il dito
            bx = x + 222
            b += '<g filter="url(#nxShS)"><rect x="%d" y="%d" width="40" height="88" rx="10" fill="#e6f1f8" stroke="#7fb0cc" stroke-width="1.5"/>' % (bx - 20, y + 172)
            b += '<rect x="%d" y="%d" width="32" height="34" rx="6" fill="#7fb0cc" opacity=".35"/>' % (bx - 16, y + 216)
            b += '<rect x="%d" y="%d" width="16" height="16" fill="#cfd8df"/>' % (bx - 8, y + 158)
            b += '<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="#4b3a40"/></g>' % (bx - 12, y + 158, bx + 10, y + 158, bx + 6, y + 142, bx - 22, y + 146)
            b += text(bx, y + 241, '70%', 14, weight=800, fill='#4f7fa0')
            for k in range(14):
                a = math.radians(200 + (k * 37) % 50)
                rr = 14 + (k * 13) % 34
                b += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#86bfe0" opacity=".75"/>' % (bx - 24 + rr * math.cos(a), y + 146 + rr * math.sin(a), 1.4 + k % 3 * .6)
        elif i == 1:
            b += _pusher(cx + 4, yc - 30, -58, 150)
            b += arrow(cx - 56, yc - 92, cx - 56, yc - 50)
        elif i == 2:
            b += _stick(cx + 14, yc - 38, -50, 140)
            for k, (dx, dy) in enumerate([(-16, -54), (-6, -62), (20, -58)]):
                b += '<path d="M%d,%d l5,-2 l2,4 z" fill="#fff" stroke="#e2cfd4"/>' % (cx + dx, yc + dy)
        elif i == 3:
            b += _file(cx + 34, yc - 84, -72, 150, 20, label='180', lsize=14)
            b += arrow(cx + 92, yc - 150, cx + 72, yc - 88, MUTED, 1.5, True)
        elif i == 4:
            b += _brush(cx + 18, yc - 92, -35, 120, '#efe4d6', 'dust', handle='#c2577a')
            for k in range(10):
                b += '<circle cx="%d" cy="%d" r="%.1f" fill="#c3ad9f"/>' % (cx - 34 + (k * 23) % 70, yc - 150 + (k * 17) % 46, 1.5 + (k % 3) * .6)
        elif i == 5:
            b += _bottle(x + 238, y + 170, '#f6eebe', 50, 34)
            b += text(x + 238, y + 157, '1', 15, weight=800, fill=INK)
            b += _bottle(x + 238, y + 262, '#fbe7a6', 50, 34)
            b += text(x + 238, y + 249, '2', 15, weight=800, fill=INK)
            b += _brush(cx + 2, yc - 64, -52, 90, '#f6e7a6', 'oval', load='#f6e7a6')
    return svg(920, 620, arrow_defs() + b, 'Preparazione dell\'unghia naturale in sei passaggi')


@fig('tip-applicazione.svg')
def tip_app():
    b = ''
    T = ['Scegli la misura', 'Incolla a ~45°', 'Taglia la lunghezza', 'Fondi il contatto']
    for i, t in enumerate(T):
        x = 20 + i * 230
        b += panel(x, 20, 215, 300, t, i + 1)
    # 1 misura: il tip copre la lamina da solco a solco
    cx = 20 + 107
    f, p = finger_nail(cx, 275, hw=34, nail_len=95, free_len=8, shape='tonda', finger_len=25)
    b += f
    for sx in (-1, 1):
        b += '<line x1="%d" y1="140" x2="%d" y2="186" stroke="%s" stroke-dasharray="3 3"/>' % (cx + sx * 38, cx + sx * 38, ACC2)
    b += arrow(cx - 36, 132, cx + 36, 132, ACC2, 1.8, True)
    b += text(cx, 118, 'da solco a solco', 15, weight=700, fill=ACC2)
    b += text(cx, 74, 'nel dubbio, la misura', 15, fill=MUTED) + text(cx, 93, 'più grande, poi limala', 15, fill=MUTED)
    # 2 angolo: vista laterale, il tip si appoggia e si abbassa
    x = 250
    s, q = _finger_side(x + 10, 250, x + 70, x + 150, free=0)
    b += s
    px, py = x + 100, 247
    tip = ('<g transform="translate(%d,%d) rotate(-45)"><rect x="0" y="-6" width="118" height="7" rx="3" fill="#f6f1ea" stroke="#b9ab98"/>'
           '<rect x="0" y="-6" width="32" height="7" rx="3" fill="#f3cbd6" stroke="#b9ab98"/></g>' % (px, py))
    b += '<g filter="url(#nxShS)">%s</g>' % tip
    b += drop(px + 6, py - 6, '#e9f4fb')
    b += '<path d="M%d,%d A44,44 0 0 0 %.1f,%.1f" fill="none" stroke="%s" stroke-width="1.8" stroke-dasharray="3 3"/>' % (
        px + 44, py, px + 31.1, py - 31.1, ACC2)
    b += text(px + 50, py - 14, '45°', 15, 'start', 800, ACC2)
    b += ('<path d="M%d,%d A80,80 0 0 1 %d,%d" fill="none" stroke="%s" stroke-width="2" marker-end="url(#ar)"/>'
          % (px + 74, py - 104, px + 108, py - 40, ACC2))
    b += text(x + 107, 74, 'colla sull\'incavo (well)', 15, fill=MUTED)
    b += text(x + 107, 93, 'abbassa e premi 5–10 s', 15, fill=MUTED)
    # 3 taglio con il tagliatip
    cx = 480 + 107
    f, p = finger_nail(cx, 285, hw=32, nail_len=70, free_len=110, shape='quadrata', smile=4, free='#f6f1ea', finger_len=15)
    b += f
    b += '<line x1="%d" y1="150" x2="%d" y2="150" stroke="%s" stroke-width="2" stroke-dasharray="6 4"/>' % (cx - 52, cx + 52, ERR)
    b += text(cx, 74, 'linea di taglio', 15, weight=700, fill=ERR)
    b += text(cx, 93, 'lascia 1–2 mm per limare', 15, fill=MUTED)
    cut = ('<path d="M0,-12 L30,-12 Q38,-12 38,-4 L38,4 Q38,12 30,12 L0,12 Z" fill="#9aa3ad" stroke="#5f6973"/>'
           '<rect x="4" y="-3" width="30" height="6" rx="2" fill="#4b3a40"/>'
           '<path d="M36,-8 L96,-30 L100,-20 L40,0 Z" fill="#c2577a"/><path d="M36,8 L96,30 L100,20 L40,0 Z" fill="#8e3b5a"/>')
    b += _rot(cx + 38, 150, 0, '<g transform="scale(.62)">%s</g>' % cut)
    # 4 fusione dell'incavo
    cx = 710 + 107
    extra = '<rect x="%d" y="%d" width="80" height="22" fill="url(#hatch)" clip-path="url(#CLIP)"/>' % (cx - 40, 285 - 95 - 10)
    f, p = finger_nail(cx, 285, hw=32, nail_len=95, free_len=55, shape='squoval', smile=4, free='#f6f1ea', finger_len=15, extra=extra)
    b += f
    b += _file(cx + 52, 160, -24, 80, 13)
    b += _callout(cx - 18, 186, cx - 70, 164, ['zona da', 'fondere'], 15)
    b += text(cx, 74, 'lima solo il tip,', 15, weight=700, fill=ERR)
    b += text(cx, 93, 'non l\'unghia naturale', 15, weight=700, fill=ERR)
    defs = ('<defs><pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
            '<line x1="0" y1="0" x2="0" y2="6" stroke="%s" stroke-width="2.5"/></pattern></defs>' % ACC)
    return svg(950, 340, arrow_defs() + defs + b, 'Applicazione del tip in quattro passaggi')


def _form_sheet(cx, ys, hole=50):
    """Cartina adesiva vista dall'alto: foglio dorato con griglia stampata, asse centrale, alette laterali e foro ovale."""
    gid, gd = _lgrad([(0, '#fbf0c4'), (1, '#efdc92')], 0, 1)
    w, top, bot = 92, ys - 150, ys + 40
    sheet = ('M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f A%.1f,%.1f 0 0 0 %.1f,%.1f Z'
             % (cx - w, bot, cx - w, top + 12, cx - w, top, cx - w + 12, top, cx + w - 12, top, cx + w, top, cx + w, top + 12,
                cx + w, bot, cx + 52, bot, 52, hole, cx - 52, bot))
    s = gd + '<path d="%s" fill="url(#%s)" stroke="#cdb45a" stroke-width="1.3"/>' % (sheet, gid)
    # alette adesive (più scure) ai lati del foro
    for sx in (-1, 1):
        s += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="#e6cf7a" opacity=".7"/>' % (
            cx + sx * w, bot, cx + sx * w, ys - 22, cx + sx * 66, ys - 22, cx + sx * 54, bot)
    # griglia graduata
    for k in range(1, 6):
        yy = ys - 6 - k * 22
        s += _ln(cx - w + 12, yy, cx + w - 12, yy, '#d8c26a', 1 if k % 2 else 1.6)
    for k in range(-3, 4):
        if k:
            s += _ln(cx + k * 24, top + 10, cx + k * 24, ys - 30, '#e3d07f', .8)
    s += _ln(cx, top + 6, cx, ys - 10, ACC2, 1.6, ' stroke-dasharray="5 4"')
    return s


def _form_lens(lx, ly, gap):
    """Vista laterale ingrandita del bordo libero appoggiato sulla cartina."""
    s = '<rect x="%.1f" y="%.1f" width="120" height="100" fill="#fbf6f4"/>' % (lx - 60, ly - 50)
    fy = ly - 4 + gap
    s += '<rect x="%.1f" y="%.1f" width="70" height="8" rx="1.5" fill="#f1df98" stroke="#cdb45a" stroke-width="1.2"/>' % (lx - 4 + (16 if gap else 0), fy)
    s += _ln(lx + 22, fy + 4, lx + 60, fy + 4, '#d8c26a', 1)
    s += _P('M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z' % (
        lx - 70, ly - 4, lx - 16, ly - 4, lx + 4, ly - 2, lx + 6, ly + 16, lx + 4, ly + 38, lx - 20, ly + 44, lx - 70, ly + 44),
        SKIN, SKIN_D, 1.4)
    s += _P('M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z' % (
        lx - 70, ly - 13, lx + 8, ly - 13, lx + 13, ly - 9, lx + 8, ly - 4, lx - 70, ly - 4), '#f6c9d4', NAIL_S, 1.4)
    if gap:
        s += '<rect x="%.1f" y="%.1f" width="12" height="%.1f" fill="%s" opacity=".22"/>' % (lx + 6, ly - 4, gap, ERR)
        s += _P('M%.1f,%.1f h-7 M%.1f,%.1f v%.1f M%.1f,%.1f h-7' % (lx + 34, ly - 4, lx + 30.5, ly - 4, gap, lx + 34, fy), 'none', ERR, 2.2)
        s += '<path d="M%.1f,%.1f q5,7 0,11 q-5,-4 0,-11 z" fill="#cfe6f4" stroke="#5e9cc0" stroke-width="1.2"/>' % (lx + 11, fy + 13)
    else:
        s += '<circle cx="%.1f" cy="%.1f" r="9" fill="none" stroke="%s" stroke-width="2"/>' % (lx + 10, ly - 4, OK)
    return s


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
        pc = uid()
        b += '<defs><clipPath id="%s"><rect x="%d" y="62" width="280" height="262"/></clipPath></defs>' % (pc, x)
        b += '<g clip-path="url(#%s)"><g transform="rotate(%d %d %d)" filter="url(#nxShS)">%s</g></g>' % (pc, ang, cx, ys, _form_sheet(cx, ys, 50 + gap))
        f, p = finger_nail(cx, yc, hw=34, nail_len=95, free_len=8, shape='tonda', smile=6, finger_len=30)
        b += '<g clip-path="url(#%s)">%s</g>' % (pc, f)
        if ang:
            # asse dell'unghia (verde) e asse della cartina (rosso)
            b += _ln(cx, ys - 150, cx, yc + 16, OK, 2, ' stroke-dasharray="6 4"')
            a = math.radians(ang)
            b += _ln(cx + 150 * math.sin(a), ys - 150 * math.cos(a), cx - 26 * math.sin(a), ys + 26 * math.cos(a), ERR, 2, ' stroke-dasharray="6 4"')
            b += _P('M%.1f,%.1f A70,70 0 0 1 %.1f,%.1f' % (cx, ys - 70, cx + 70 * math.sin(a), ys - 70 * math.cos(a)), 'none', ERR, 2)
            b += _tag(cx - 50, ys - 96, 'asse unghia', OK, 14)
            b += _tag(cx + 78, ys - 118, 'asse cartina', ERR, 14)
        else:
            b += _lens(x + 222, 138, 40, _form_lens(x + 222, 138, gap), cx + 26, ys - 6, OK if ok else ERR)
        b += text(cx, 347, sub, 15, weight=700, fill=OK if ok else ERR)
    return svg(920, 380, b, 'Posizionamento della cartina: corretta, con spazio sotto il bordo libero, fuori asse')


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
        cx, base = x + 150, 228
        # superficie di lavoro (cartina vista di lato)
        b += '<rect x="%d" y="%d" width="210" height="9" rx="4.5" fill="#efe1a8" stroke="#d8c26a"/>' % (cx - 105, base)
        tipx, tipy = cx - 40, base - 52
        if i == 0:
            b += ('<path d="M%d,%d C%d,%d %d,%d %d,%d C%d,%d %d,%d %d,%d Z" fill="#fbeef2" stroke="%s" stroke-width="1.3"/>'
                  % (cx - 92, base, cx - 70, base - 8, cx - 30, base - 20, cx + 5, base - 18, cx + 40, base - 16, cx + 80, base - 7, cx + 104, base, NAIL_S))
            b += '<path d="M%d,%d q10,2 9,16 q-1,10 -5,14 q-5,-6 -5,-14 z" fill="#fbeef2" stroke="%s" stroke-width="1.2"/>' % (cx + 96, base + 2, NAIL_S)
            b += '<ellipse cx="%d" cy="%d" rx="26" ry="3" fill="#fff" opacity=".9"/>' % (cx - 20, base - 13)
            tipy = base - 46
        elif i == 1:
            b += ('<path d="M%d,%d C%d,%d %d,%d %d,%d C%d,%d %d,%d %d,%d Z" fill="#fbeef2" stroke="%s" stroke-width="1.3"/>'
                  % (cx - 44, base, cx - 46, base - 30, cx - 26, base - 50, cx, base - 50, cx + 26, base - 50, cx + 46, base - 30, cx + 44, base, NAIL_S))
            b += '<ellipse cx="%d" cy="%d" rx="13" ry="7" fill="#fff" transform="rotate(-25 %d %d)"/>' % (cx - 16, base - 34, cx - 16, base - 34)
            b += '<ellipse cx="%d" cy="%d" rx="34" ry="4" fill="#e9d5dc" opacity=".8"/>' % (cx, base - 2)
            tipy = base - 64
        else:
            rng = random.Random(4)
            pts = []
            for k in range(25):
                a = math.pi * k / 24
                rr = 38 + rng.uniform(-6, 6)
                pts.append('%.1f,%.1f' % (cx - math.cos(a) * rr, base - math.sin(a) * rr * .85))
            b += '<polygon points="%s" fill="#f4ecee" stroke="%s" stroke-width="1.2" stroke-linejoin="round"/>' % (' '.join(pts), NAIL_S)
            for k in range(30):
                gx, gy = cx + rng.uniform(-30, 30), base - rng.uniform(4, 28)
                b += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#d9c8ce"/>' % (gx, gy, rng.uniform(1, 2.2))
            for k in range(8):
                b += '<circle cx="%.1f" cy="%.1f" r="1.6" fill="#e6dade"/>' % (cx + rng.choice([-1, 1]) * rng.uniform(44, 70), base - 2)
            tipy = base - 60
        b += _brush(tipx, tipy, -145, 110, '#f3eee6', 'acrylic')
        b += text(cx - 10, 278, r, 18, weight=800, fill=ACC2)
        b += mtext(x + 140, 305, [l1, l2], 15, fill=MUTED)
    return svg(920, 370, b, 'Perla di acrilico bagnata, media e asciutta')


@fig('smile-line.svg')
def smile():
    b = text(30, 40, 'French: la linea del sorriso (smile line)', 20, 'start', 800, ACC2)
    cases = [('Simmetrica', True, 0, 22, ['punti laterali', 'alla stessa altezza']),
             ('Asimmetrica', False, 16, 18, ['un lato più alto', 'dell\'altro']),
             ('Piatta', False, 0, 2, ['dritta: il dito', 'sembra più largo']),
             ('A "V"', True, 0, -1, ['variante decorativa,', 'simmetrica'])]
    for i, (t, ok, skew, d, cap) in enumerate(cases):
        x = 20 + i * 225
        b += panel(x, 60, 210, 368, t)
        b += mark(x + 182, 88, ok)
        cx, yc = x + 105, 330
        hw, ys = 38, yc - 110
        if d >= 0:
            yl, yr, ym = ys + d, ys + d - skew, ys - d - 2 + skew
            fp = 'M%d,%d Q%d,%d %d,%d L%d,%d L%d,%d Z' % (cx - hw - 4, yl, cx + skew, ym, cx + hw + 4, yr, cx + hw + 4, 60, cx - hw - 4, 60)
            edge = 'M%d,%d Q%d,%d %d,%d' % (cx - hw - 4, yl, cx + skew, ym, cx + hw + 4, yr)
        else:
            yl = yr = ys - 12
            fp = 'M%d,%d L%d,%d L%d,%d L%d,%d L%d,%d Z' % (cx - hw - 4, ys - 12, cx, ys + 26, cx + hw + 4, ys - 12, cx + hw + 4, 60, cx - hw - 4, 60)
            edge = 'M%d,%d L%d,%d L%d,%d' % (cx - hw - 4, ys - 12, cx, ys + 26, cx + hw + 4, ys - 12)
        gw, gwd = _lgrad([(0, '#ffffff'), (1, '#f7f1ee')], 0, 1)
        extra = gwd + '<path d="%s" fill="url(#%s)" clip-path="url(#CLIP)"/>' % (fp, gw)
        extra += '<path d="%s" fill="none" stroke="#e7d9d4" stroke-width="1.5" clip-path="url(#CLIP)"/>' % edge
        f, p = finger_nail(cx, yc, hw=hw, nail_len=110, free_len=70, shape='squoval', smile=0, plate='#f6c9d4', free='#f6c9d4',
                           finger_len=20, extra=extra, lunula=False)
        b += f
        # asse dell'unghia (leggero)
        b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1" stroke-dasharray="3 4" opacity=".7"/>' % (cx, ys - 84, cx, yc - 14, MUTED)
        # guide sui punti laterali
        col = OK if ok else ERR
        xl, xr = cx - hw, cx + hw
        if skew:
            # due quote diverse: mostra lo scarto
            for yy in (yl - 1, yr + 1):
                b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.5" stroke-dasharray="5 4"/>' % (xl - 16, yy, xr + 16, yy, col)
            b += _P('M%d,%d h8 M%d,%d v%d M%d,%d h8' % (xr + 20, yr + 1, xr + 24, yr + 1, yl - yr - 2, xr + 20, yl - 1), 'none', ERR, 2)
            b += text(xr + 30, (yl + yr) / 2 + 4.5, '≠', 16, 'start', 800, ERR)
        else:
            b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.5" stroke-dasharray="5 4"/>' % (xl - 16, yl - 1, xr + 16, yr - 1, col)
        for (px, py) in ((xl, yl - 1), (xr, yr + (1 if skew else -1))):
            b += '<circle cx="%d" cy="%d" r="4.5" fill="%s" stroke="#fff" stroke-width="1.5"/>' % (px, py, col)
        b += mtext(cx, 392, cap, 15, weight=600, fill=col)
    b += text(470, 453, 'Controlla la simmetria guardando l\'unghia dal davanti e capovolgendo la mano della cliente.', 15, fill=MUTED)
    return svg(940, 468, arrow_defs() + b, 'Smile line del french: simmetrica e a V corrette; asimmetrica e piatta errate')


@fig('baby-boomer.svg')
def bboom():
    b = text(40, 40, 'Baby boomer: sfumatura dal nude al bianco', 20, 'start', 800, ACC2)
    defs = ('<defs><linearGradient id="bb" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#f6c9d4"/>'
            '<stop offset=".45" stop-color="#f6c9d4"/><stop offset=".85" stop-color="#ffffff"/></linearGradient>'
            '<linearGradient id="bb2" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#f6c9d4"/>'
            '<stop offset=".62" stop-color="#f6c9d4"/><stop offset=".75" stop-color="#fbe9ee"/><stop offset="1" stop-color="#ffffff"/></linearGradient></defs>')
    steps = [('Base nude/rosa', None, 'colore uniforme, poi lampada'), ('Bianco sulla punta', 'url(#bb2)', 'solo sul bordo libero'),
             ('Sfuma verso la cuticola', 'url(#bb)', 'picchietta: spugnetta o pennello')]
    for i, (t, g, note) in enumerate(steps):
        x = 20 + i * 300
        b += panel(x, 60, 280, 330, t, i + 1)
        b += text(x + 140, 120, note, 15, fill=MUTED)
        cx, yc = x + 130, 350
        f, p = finger_nail(cx, yc, hw=42, nail_len=120, free_len=70, shape='mandorla', smile=0, plate='#f6c9d4', free='#f6c9d4',
                           free_grad=g, finger_len=25, lunula=False)
        b += f
        if i == 0:
            b += _bottle(x + 236, 300, '#f6c9d4', 58, 36)
        elif i == 1:
            b += _brush(cx + 14, yc - 176, -25, 110, '#ffffff', 'flat', load='#ffffff')
            b += _bottle(x + 236, 300, '#ffffff', 58, 36)
        else:
            sp = ('<path d="M0,-16 L34,-16 Q40,-16 40,-10 L40,16 L-6,16 Q-10,16 -8,10 Z" fill="#f3e3d0" stroke="#d6bf9f" stroke-width="1.4"/>'
                  + ''.join('<circle cx="%d" cy="%d" r="1.6" fill="#d6bf9f"/>' % (4 + (k * 11) % 32, -10 + (k * 7) % 22) for k in range(12)))
            b += _rot(cx + 30, yc - 150, -25, sp)
            b += arrow(cx + 76, yc - 186, cx + 52, yc - 160, MUTED, 1.5, True)
    return svg(920, 410, defs + arrow_defs() + b, 'Baby boomer in tre passaggi')


@fig('refill.svg')
def refill():
    b = text(40, 40, 'Perché serve il refill (ogni 3–4 settimane)', 20, 'start', 800, ACC2)
    cases = [('Appena fatta', 0, 0.45, True, 'apex sopra il punto di stress'),
             ('Dopo 3–4 settimane', 42, 0.62, False, 'ricrescita, apex spostato avanti'),
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
            b += leader(x + 100, 210, x + 80, 140, 'ricrescita', 'middle', 15)
        b += text(x + 140, 306, sub, 15, weight=600, fill=OK if ok else ERR)
    b += text(470, 351, 'L\'unghia cresce ≈ 3 mm al mese: il peso si sposta in avanti e aumenta il rischio di rottura e sollevamento.', 14.5, fill=MUTED)
    return svg(940, 370, b, 'Ricrescita e refill: profilo prima e dopo')


@fig('rimozione.svg')
def removal():
    b = ''
    T = ['Opacizza il top', 'Cotone con acetone', 'Avvolgi: 10–15 min', 'Spingi via e nutri']
    notes = [['togli la lucidità,', 'non limare a fondo'], ['cotone imbevuto', 'sulla lamina'], ['stagnola o clip', 'ben chiuse'],
             ['senza grattare', 'né fare leva']]
    for i, t in enumerate(T):
        x = 20 + i * 230
        b += panel(x, 20, 215, 332, t, i + 1)
        cx, yc = x + 100, 280
        extra = ''
        if i == 0:
            pid = uid('mt')
            extra = ('<defs><pattern id="%s" width="4" height="4" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".9" fill="#fff" opacity=".55"/>'
                     '</pattern></defs><rect x="%d" y="%d" width="40" height="160" fill="url(#%s)" clip-path="url(#CLIP)"/>' % (pid, cx - 40, yc - 160, pid))
        if i == 3:
            extra = ('<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="%s" clip-path="url(#CLIP)"/>'
                     % (cx - 40, yc - 165, cx + 40, yc - 165, cx + 40, yc - 92, cx - 40, yc - 72, '#e46f8f'))
        plate = '#e46f8f' if i < 3 else '#f6cbd6'
        f, p = finger_nail(cx, yc, hw=34, nail_len=110, free_len=40, shape='squoval', plate=plate, free=plate, finger_len=20,
                           lunula=False, extra=extra)
        b += f
        b += mtext(x + 107, 320, notes[i], 15, fill=ERR if i == 3 else MUTED, weight=600 if i == 3 else 400)
        if i == 0:
            b += _file(cx + 40, yc - 104, -72, 140, 18, label='180', lsize=14.5)
        elif i == 1:
            rng = random.Random(2)
            pts = []
            for k in range(28):
                a = 2 * math.pi * k / 28
                rr = 38 + rng.uniform(-3, 3)
                pts.append('%.1f,%.1f' % (cx + math.cos(a) * rr, yc - 105 + math.sin(a) * rr * .85))
            b += '<polygon points="%s" fill="#ffffff" stroke="#d8d0cc" stroke-width="1.5" stroke-linejoin="round" filter="url(#nxShS)"/>' % ' '.join(pts)
            for k in range(12):
                b += '<path d="M%.1f,%.1f q4,-3 8,0" stroke="#e7e1de" stroke-width="1.2" fill="none"/>' % (
                    cx - 26 + rng.uniform(0, 44), yc - 128 + rng.uniform(0, 44))
            b += '<ellipse cx="%d" cy="%d" rx="22" ry="12" fill="#d9ecf8" opacity=".75"/>' % (cx + 4, yc - 100)
            b += _bottle(x + 186, 200, '#e6f3fb', 56, 34, cap='#9aa3ad')
        elif i == 2:
            gid = uid('fo')
            b += ('<defs><linearGradient id="%s" x1="0" x2="1"><stop offset="0" stop-color="#b9c0c8"/><stop offset=".35" stop-color="#f4f6f8"/>'
                  '<stop offset=".6" stop-color="#c9cfd6"/><stop offset="1" stop-color="#9aa2ab"/></linearGradient></defs>' % gid)
            b += ('<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d L%d,%d Q%d,%d %d,%d Z" fill="url(#%s)" stroke="#8b939c" stroke-width="1.5" filter="url(#nxShS)"/>'
                  % (cx - 54, yc + 2, cx - 50, yc - 160, cx, yc - 196, cx + 50, yc - 160, cx + 54, yc + 2, cx + 30, yc - 6, cx, yc + 8, cx - 30, yc - 6, gid))
            for (x1, y1, x2, y2) in [(-40, -150, -10, -132), (-12, -120, 30, -140), (10, -96, 42, -80), (-44, -70, -12, -86), (-30, -36, 8, -50), (20, -40, 44, -20)]:
                b += '<path d="M%d,%d L%d,%d" stroke="#ffffff" stroke-width="2" opacity=".85"/><path d="M%d,%d L%d,%d" stroke="#8b939c" stroke-width="1" opacity=".6"/>' % (
                    cx + x1, yc + y1, cx + x2, yc + y2, cx + x1, yc + y1 + 3, cx + x2, yc + y2 + 3)
            b += '<circle cx="%d" cy="78" r="18" fill="#fff" stroke="%s" stroke-width="2.5"/><path d="M%d,78 l0,-11 M%d,78 l8,5" stroke="%s" stroke-width="2.5" stroke-linecap="round"/>' % (
                x + 180, ACC2, x + 180, x + 180, ACC2)
        elif i == 3:
            for k, (dx, dy) in enumerate([(-30, -86), (18, -92), (-6, -80)]):
                b += '<path d="M%d,%d l12,-3 l3,8 l-11,4 z" fill="#e46f8f" stroke="%s" stroke-width=".8"/>' % (cx + dx, yc + dy, NAIL_S)
            b += _stick(cx - 4, yc - 70, -68, 130)
            b += arrow(cx - 52, yc - 70, cx - 52, yc - 130)
            b += drop(cx + 70, yc - 52) + text(cx + 70, yc - 27, 'olio', 15, weight=600, fill=MUTED)
    return svg(950, 372, arrow_defs() + b, 'Rimozione soak-off in quattro passaggi')


@fig('lifting.svg')
def lifting():
    b = text(40, 40, 'Sollevamento (lifting): dove nasce e perché', 20, 'start', 800, ACC2)
    # A: vista dall'alto
    b += panel(20, 60, 250, 400, 'Vista dall\'alto')
    cx, yc = 145, 380
    extra = ('<path d="M%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="#fff" opacity=".85" clip-path="url(#CLIP)"/>'
             % (cx - 40, yc - 14, cx, yc - 50, cx + 40, yc - 14, cx + 40, yc - 34, cx, yc - 70, cx - 40, yc - 34))
    extra += '<path d="M%d,%d L%d,%d L%d,%d Z" fill="#fff" opacity=".85" clip-path="url(#CLIP)"/>' % (cx + 44, yc - 100, cx + 26, yc - 70, cx + 44, yc - 40)
    f, p = finger_nail(cx, yc, hw=44, nail_len=150, free_len=50, shape='squoval', plate='#e9a7bd', free='#e9a7bd', finger_len=40,
                       extra=extra, lunula=False)
    b += f
    b += _num(cx, yc - 44, 'A', r=13, size=14) + _num(cx + 64, yc - 70, 'B', r=13, size=14)
    b += text(40, 446, 'A  cuticola', 15, 'start', 700) + text(152, 446, 'B  laterale', 15, 'start', 700)
    # B: di profilo, il prodotto si stacca e si infiltra umidità
    b += panel(285, 60, 250, 400, 'Di profilo (ingrandito)')
    pc = uid('pc')
    b += '<defs><clipPath id="%s"><rect x="285" y="96" width="250" height="364" rx="16"/></clipPath></defs>' % pc
    gid, sk = _skinv(250, 420)
    z = sk + '<g clip-path="url(#%s)">' % pc
    # polpastrello sotto la lamina e piega prossimale
    z += '<rect x="280" y="300" width="260" height="130" fill="url(#%s)"/>' % gid
    z += '<path d="M330,300 L540,300" stroke="#ee8ea7" stroke-width="8"/>'
    z += '<path d="M280,288 L540,288 L540,302 L280,302 Z" fill="#f7d4dd" stroke="%s" stroke-width="1.6"/>' % NAIL_S
    z += ('<path d="M280,232 L322,232 C346,232 358,252 362,288 L280,302 Z" fill="url(#%s)" stroke="%s" stroke-width="1.6"/>' % (gid, SKIN_D))
    # prodotto: aderisce in avanti, staccato vicino alla cuticola
    z += ('<path d="M374,274 Q380,254 420,250 L540,246 L540,288 L452,288 Q410,284 374,274 Z" fill="#e9a7bd" stroke="%s" stroke-width="1.6"/>' % NAIL_S)
    z += '<path d="M392,262 Q440,254 530,252" stroke="#fff" stroke-width="3" opacity=".6" fill="none" stroke-linecap="round"/>'
    z += '<path d="M374,274 Q410,284 452,288 L374,288 Z" fill="#fff"/>'
    for (dx, dy, r) in [(384, 282, 3.2), (400, 284, 2.6), (418, 285, 2.2)]:
        z += '<circle cx="%d" cy="%d" r="%.1f" fill="#7fb0cc"/>' % (dx, dy, r)
    for (dx, dy) in [(392, 279), (409, 281)]:
        z += '<rect x="%d" y="%d" width="7" height="3" rx="1.5" fill="%s"/>' % (dx, dy, OK)
    z += '</g>'
    b += z
    b += _callout(395, 283, 362, 196, ['fessura: entrano', 'umidità e batteri'], 15)
    b += leader(480, 262, 470, 140, 'prodotto', 'middle', 15)
    b += leader(460, 296, 455, 350, 'lamina naturale', 'middle', 15)
    b += text(410, 406, 'più si aspetta,', 15, fill=MUTED) + text(410, 426, 'più la fessura si allarga', 15, fill=MUTED)
    causes = ['Cuticola non rimossa', 'Olio o umidità sulla lamina', 'Disidratante o primer saltati',
              'Prodotto a contatto con la pelle', 'Bordo libero non sigillato', 'Perla troppo bagnata o asciutta',
              'Refill fatto in ritardo', 'Polimerizzazione incompleta']
    b += text(560, 92, 'Cause più frequenti', 16, 'start', 800)
    for i, c in enumerate(causes):
        y = 125 + i * 33
        b += '<circle cx="572" cy="%d" r="12" fill="%s"/>' % (y - 5, ACC)
        b += text(572, y, str(i + 1), 14, weight=800, fill='#fff')
        b += text(592, y, c, 14.5, 'start')
    b += '<rect x="555" y="380" width="325" height="80" rx="10" fill="#fbe7e4"/>'
    b += mtext(570, 403, ['Mai incollare sopra un sollevamento:', 'si infiltrano umidità e batteri', '(Pseudomonas).'], 15, 'start', 600, ERR)
    return svg(900, 480, b, 'Sollevamento della ricostruzione e sue cause')


@fig('igiene.svg')
def hygiene():
    b = text(30, 40, 'I tre livelli di trattamento igienico', 20, 'start', 800, ACC2)
    levels = [('Detersione / sanificazione', 'Riduce sporco e carica microbica', 'mani, superfici, lime monouso', '#f9e6ec', '#e7bfcc', _ic_soap()),
              ('Disinfezione', 'Elimina la maggior parte dei patogeni', 'strumenti non sterilizzabili, superfici', '#f1bccc', '#d98ea8', _ic_tray()),
              ('Sterilizzazione', 'Elimina ogni forma di vita, spore incluse', 'autoclave classe B (EN 13060), con tracciabilità', ACC, ACC2, _ic_autoclave())]
    for i, (t, d, u, c, st, ic) in enumerate(levels):
        w = 780 - i * 150
        x = 440 - w / 2
        y = 282 - i * 100
        b += '<rect x="%.1f" y="%d" width="%d" height="88" rx="14" fill="%s" stroke="%s" stroke-width="1.2" filter="url(#nxSh)"/>' % (x, y, w, c, st)
        # gradino: numero di livello
        b += '<circle cx="%.1f" cy="%d" r="34" fill="#fff" stroke="%s" stroke-width="1.5"/>' % (x + 52, y + 44, st)
        b += '<g transform="translate(%.1f,%d) scale(.78)">%s</g>' % (x + 52, y + 44, ic)
        fc = '#fff' if i == 2 else INK
        tx = x + 98 + (w - 118) / 2
        b += text(tx, y + 30, t, 17, weight=800, fill=fc)
        b += text(tx, y + 53, d, 15, fill=fc)
        b += text(tx, y + 75, 'Per: ' + u, 14.5, fill='#fde8ef' if i == 2 else MUTED, style='italic')
    # scala di efficacia
    gid, gd = _lgrad([(0, ACC2), (1, '#f3d3dd')], 0, 1)
    b += gd
    b += '<rect x="862" y="104" width="10" height="266" rx="5" fill="url(#%s)"/>' % gid
    b += '<path d="M856,108 L867,88 L878,108 Z" fill="%s"/>' % ACC2
    b += text(880, 76, 'più efficace', 15, 'end', 700, ACC2)
    b += text(30, 396, 'Si procede sempre dal basso: prima si pulisce, poi si disinfetta o si sterilizza.', 15, 'start', fill=MUTED)
    return svg(900, 405, b, 'Detersione, disinfezione e sterilizzazione: tre livelli di efficacia crescente')


@fig('lampade.svg')
def lamps():
    b = text(40, 40, 'Lampade: lunghezze d\'onda di emissione', 20, 'start', 800, ACC2)
    x0, x1, base = 80, 820, 300

    def X(nm):
        return x0 + (nm - 290) / (460 - 290) * (x1 - x0)
    defs = '<defs><linearGradient id="vis" x1="0" x2="1"><stop offset="0" stop-color="#7b4bd6"/><stop offset=".5" stop-color="#3f6fe0"/><stop offset="1" stop-color="#2bb0c9"/></linearGradient></defs>'
    b += '<rect x="%.1f" y="150" width="%.1f" height="150" fill="#f5f1fb"/>' % (X(400), X(460) - X(400))
    b += text(X(430), 170, 'luce visibile →', 15, fill=MUTED)

    for i, (col, lab) in enumerate([('#7b4bd6', 'UV classica: ~300–410 nm, picco ~365 nm'), ('#3f6fe0', 'LED: ~375–425 nm, picco ~385–405 nm'),
                                    (ACC, 'Dual UV/LED: due picchi, es. 365 + 405 nm')]):
        b += '<rect x="90" y="%d" width="22" height="6" rx="3" fill="%s"/>' % (78 + i * 24, col)
        b += text(120, 86 + i * 24, lab, 15, 'start', 600)

    def curve(peak, sd, h, col, lab):
        pts = []
        for nm in range(290, 461, 2):
            y = base - h * math.exp(-((nm - peak) ** 2) / (2 * sd * sd))
            pts.append('%.1f,%.1f' % (X(nm), y))
        return ('<polyline points="%s" fill="none" stroke="%s" stroke-width="3"/>' % (' '.join(pts), col)
                + text(X(peak), base - h - 10, lab, 14, weight=700, fill=col))
    b += curve(366, 20, 130, '#7b4bd6', 'UV')
    b += curve(395, 9, 110, '#3f6fe0', 'LED')
    b += curve(366, 6, 80, ACC, '')
    b += curve(405, 6, 80, ACC, '')
    b += text(X(366) - 34, base - 60, 'Dual', 14, 'end', 700, ACC)
    b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s"/>' % (x0, base, x1, base, INK)
    for nm in range(300, 461, 20):
        b += '<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s"/>' % (X(nm), base, X(nm), base + 6, INK)
        b += text(X(nm), base + 23, str(nm), 15, fill=MUTED)
    b += text((x0 + x1) / 2, base + 47, 'nm', 15, fill=MUTED)
    b += text(450, 380, 'Conta l\'abbinamento lampada ↔ fotoiniziatori del gel, non i watt: usa la lampada del tuo sistema.', 15, weight=600)
    return svg(900, 400, defs + b, 'Spettri di emissione delle lampade UV e LED')


@fig('limatura-direzioni.svg')
def file_dir():
    b = ''
    T = ['Lati: lima parallela al solco', 'Punta: dai lati verso il centro', 'Superficie: segui la curva']
    for i, t in enumerate(T):
        x = 20 + i * 300
        b += panel(x, 20, 280, 332, t, i + 1)
        cx, yc = x + 140, 290
        f, p = finger_nail(cx, yc, hw=38, nail_len=110, free_len=60, shape='squoval', finger_len=20)
        b += f
        ys, yt = p['y_s'], p['y_t']
        if i == 0:
            b += _file(cx + 46, ys + 5, -90, 120, 16)
            b += arrow(cx + 75, ys + 40, cx + 75, ys - 40, ACC2, 2)
        elif i == 1:
            b += _file(cx, yt - 12, 0, 130, 16)
            b += arrow(cx - 70, yt - 34, cx - 10, yt - 34)
            b += arrow(cx + 70, yt - 34, cx + 10, yt - 34)
        else:
            for k in (-20, 0, 20):
                b += ('<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="%s" stroke-width="2" marker-end="url(#ar)"/>'
                      % (cx + k, yc - 30, cx + k * 1.2, (yc + yt) / 2, cx + k, yt + 10, ACC2))
        b += text(cx, 341, ['evita di limare dentro il solco', 'una direzione, no "sega"', 'dalla cuticola verso la punta'][i], 15, fill=MUTED)
    return svg(920, 372, arrow_defs() + b, 'Direzioni corrette di limatura')


@fig('sistemi.svg')
def systems():
    b = text(40, 40, 'I sistemi di ricostruzione a confronto', 20, 'start', 800, ACC2)
    items = [('Gel UV/LED', ['flacone o vasetto', '+ lampada'], ['nessun odore', 'autolivellante', 'rischio picco di calore']),
             ('Acrilico', ['liquido (monomero)', '+ polvere'], ['il più resistente', 'ottimo per lunghezze', 'odore e vapori']),
             ('Polygel', ['pasta + slip solution', '+ lampada'], ['tempo di lavoro libero', 'leggero', 'curva di apprendimento']),
             ('Fibra / seta', ['tessuto + resina', '+ attivatore'], ['sottile e naturale', 'riparazioni', 'meno strutturale'])]
    for i, (t, comp, pts) in enumerate(items):
        x = 20 + i * 225
        b += panel(x, 60, 210, 318, t)
        cx = x + 105
        base = 196
        if i == 0:
            b += _jar(cx - 22, base, '#e9a7bd', 76, 40, label='GEL', lsize=14.5)
            b += _brush(cx + 52, base - 4, -70, 90, GEL, 'oval', load=GEL)
        elif i == 1:
            b += _dappen(cx - 40, base, '#dff0fa', 56)
            b += _jar(cx + 36, base, '#ffffff', 64, 36, lid='#c2577a', label='')
            b += '<ellipse cx="%d" cy="%d" rx="22" ry="5" fill="#f4eef0"/>' % (cx + 36, base - 18)
            b += text(cx - 42, base - 56, 'liquido', 14.5, fill=MUTED) + text(cx + 38, base - 60, 'polvere', 14.5, fill=MUTED)
        elif i == 2:
            tube = ('<path d="M-16,-70 L16,-70 L14,-6 L-14,-6 Z" fill="%s" stroke="#00000022"/>'
                    '<rect x="-17" y="-76" width="34" height="8" rx="1" fill="%s"/>'
                    '<path d="M-17,-74 L17,-74" stroke="#fff" stroke-width="1" opacity=".5"/>'
                    '<rect x="-10" y="-6" width="20" height="18" rx="3" fill="#4b3a40"/>'
                    '<rect x="-10" y="-62" width="5" height="50" rx="2.5" fill="#fff" opacity=".35"/>' % (GEL, '#d98ca5'))
            b += _rot(cx - 22, base - 10, 0, tube)
            b += _bottle(cx + 36, base, '#eef6fb', 52, 32, cap='#9aa3ad')
        else:
            pid = uid('fb')
            b += ('<defs><pattern id="%s" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="6" height="6" fill="#f8f2e6"/>'
                  '<path d="M0,3 L6,3 M3,0 L3,6" stroke="#cdbb9c" stroke-width="1"/></pattern></defs>' % pid)
            b += '<g filter="url(#nxShS)"><path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="url(#%s)" stroke="#cdbb9c"/>' % (
                cx - 70, base - 8, cx - 6, base - 8, cx - 18, base - 36, cx - 82, base - 36, pid)
            b += '<ellipse cx="%d" cy="%d" rx="14" ry="30" fill="url(#%s)" stroke="#b9a37d" stroke-width="1.5"/>' % (cx - 4, base - 46, pid)
            b += '<ellipse cx="%d" cy="%d" rx="5" ry="11" fill="#e6dccb" stroke="#b9a37d"/></g>' % (cx - 4, base - 46)
            b += _bottle(cx + 46, base, '#fdf2c4', 52, 30)
        b += mtext(cx, 224, comp, 15, fill=MUTED)
        for k, pt in enumerate(pts):
            col = ERR if k == 2 else OK
            b += text(cx, 284 + k * 25, ('− ' if k == 2 else '+ ') + pt, 15, weight=600, fill=col)
    return svg(940, 396, b, 'Confronto tra gel, acrilico, polygel e fibra')


def _crack(pts, w=2.4):
    d = 'M' + ' L'.join('%.1f,%.1f' % p for p in pts)
    dl = 'M' + ' L'.join('%.1f,%.1f' % (x + 1.4, y + 1.2) for x, y in pts)
    return (_P(dl, 'none', '#fff', w * .7, ' opacity=".8"') + _P(d, 'none', '#5a2a3a', w))


def _bubbles(spec, stroke='#c97c95'):
    s = ''
    for (x, y, r) in spec:
        s += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#fff" fill-opacity=".55" stroke="%s" stroke-width="1"/>' % (x, y, r, stroke)
        s += '<path d="M%.1f,%.1f A%.1f,%.1f 0 0 1 %.1f,%.1f" stroke="#fff" stroke-width="%.1f" fill="none" stroke-linecap="round"/>' % (
            x - r * .6, y - r * .1, r * .6, r * .6, x - r * .05, y - r * .62, max(1, r * .25))
        s += '<path d="M%.1f,%.1f A%.1f,%.1f 0 0 0 %.1f,%.1f" stroke="%s" stroke-width="%.1f" fill="none" opacity=".45"/>' % (
            x - r * .7, y + r * .35, r, r, x + r * .55, y + r * .6, stroke, max(.8, r * .18))
    return s


def _wrinkles(x0, y0, n, w, dy, amp=4, k=1.0):
    s = ''
    for j in range(n):
        y = y0 + j * dy
        d = 'M%.1f,%.1f' % (x0, y)
        seg = w / 4
        for q in range(4):
            d += ' q%.1f,%.1f %.1f,0' % (seg / 2, -amp if q % 2 == 0 else amp, seg)
        s += _P(d, 'none', '#fff', 2.2 * k, ' opacity=".75"')
        s += '<path d="%s" fill="none" stroke="#b5587a" stroke-width="%.1f" opacity=".75" transform="translate(0,%.1f)"/>' % (d, 1.6 * k, 2.2 * k)
    return s


@fig('problemi.svg')
def problems():
    b = text(30, 40, 'Riconosci il difetto', 20, 'start', 800, ACC2)
    names = [('Crepa / rottura', ['apex assente o', 'mal posizionato']), ('Bolle', ['gel agitato,', 'perla asciutta']),
             ('Grinze', ['strato troppo', 'spesso']), ('Ingiallimento', ['top non', 'polimerizzato, UV'])]
    for i, (n, sub) in enumerate(names):
        x = 20 + i * 225
        b += panel(x, 60, 210, 356, n)
        cx, yc = x + 95, 338
        y_s = yc - 130
        extra = ''
        plate = '#f3bccb'
        lx, ly = x + 166, 168
        if i == 0:
            pts = [(cx - 41, y_s - 2), (cx - 30, y_s + 8), (cx - 23, y_s + 2), (cx - 12, y_s + 18), (cx - 3, y_s + 12), (cx + 8, y_s + 28), (cx + 16, y_s + 24)]
            extra = _crack(pts, 3)
            px, py = cx - 12, y_s + 20
            zoom = '<rect x="%.1f" y="%.1f" width="80" height="80" fill="#f3bccb"/>' % (lx - 40, ly - 40)
            zoom += _crack([(lx - 40, ly - 14), (lx - 22, ly + 2), (lx - 12, ly - 8), (lx + 6, ly + 12), (lx + 16, ly + 4), (lx + 40, ly + 26)], 4)
            zoom += _P('M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f' % (lx - 12, ly - 8, lx - 6, ly - 22, lx + 2, ly - 26), 'none', '#5a2a3a', 1.6)
        elif i == 1:
            spec = [(cx - 18, y_s - 30, 4), (cx - 8, y_s - 22, 6), (cx + 10, y_s - 4, 3), (cx - 14, y_s + 6, 7), (cx + 4, y_s + 22, 4),
                    (cx + 18, y_s - 40, 5), (cx - 22, y_s + 40, 3.5), (cx + 14, y_s + 52, 6), (cx - 4, y_s + 70, 3), (cx + 22, y_s + 26, 2.6)]
            extra = _bubbles(spec)
            px, py = cx - 14, y_s + 6
            zoom = '<rect x="%.1f" y="%.1f" width="80" height="80" fill="#f3bccb"/>' % (lx - 40, ly - 40)
            zoom += _bubbles([(lx - 8, ly - 6, 15), (lx + 16, ly + 16, 8), (lx + 18, ly - 20, 6), (lx - 22, ly + 22, 5)])
        elif i == 2:
            extra = '<g clip-path="url(#CLIP)">%s</g>' % _wrinkles(cx - 44, y_s + 6, 6, 88, 15, 4)
            px, py = cx + 10, y_s + 36
            zoom = '<rect x="%.1f" y="%.1f" width="80" height="80" fill="#f3bccb"/>' % (lx - 40, ly - 40)
            zoom += _wrinkles(lx - 44, ly - 22, 4, 88, 15, 6, 1.6)
        else:
            plate = '#f0d98f'
            gy, gyd = _lgrad([(0, '#e9c45a'), (.55, '#f2dc93'), (1, '#f6e6b4')], 0, 1)
            extra = gyd + '<rect x="%.1f" y="%.1f" width="100" height="190" fill="url(#%s)" clip-path="url(#CLIP)"/>' % (cx - 50, y_s - 55, gy)
            px, py = cx + 18, y_s - 20
            zoom = '<rect x="%.1f" y="%.1f" width="40" height="80" fill="#f6c9d4"/>' % (lx - 40, ly - 40)
            zoom += '<rect x="%.1f" y="%.1f" width="40" height="80" fill="#e9c45a"/>' % (lx, ly - 40)
            zoom += _ln(lx, ly - 40, lx, ly + 40, '#fff', 2)
            zoom += mark(lx - 18, ly, True, 10) + mark(lx + 20, ly, False, 10)
        f, p = finger_nail(cx, yc, hw=40, nail_len=130, free_len=50, shape='squoval', plate=plate, free=plate, finger_len=20, extra=extra, lunula=False)
        b += f
        b += _lens(lx, ly, 36, zoom, px, py, ACC2)
        b += mtext(x + 105, 380, sub, 15, weight=600, fill=MUTED)
    return svg(940, 432, b, 'Difetti comuni: crepa, bolle, grinze, ingiallimento, con ingrandimento del dettaglio')


@fig('nail-art.svg')
def nailart():
    b = text(40, 40, 'Tecniche base di nail art', 20, 'start', 800, ACC2)
    T = [('Dotting', 'puntini con il dotter'), ('Striping', 'linee con pennello fine'), ('Incapsulato', 'glitter tra due strati'), ('Stamping', 'disegno da piastra')]
    for i, (t, sub) in enumerate(T):
        x = 20 + i * 225
        b += panel(x, 60, 210, 320, t)
        cx, yc = x + 105, 314
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
        b += text(cx, 365, sub, 15, fill=MUTED)
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


def _timer(x, y, label, size=15):
    """Come timer(), ma con l'etichetta più grande (solo per le figure di questo file)."""
    return ('<circle cx="%.1f" cy="%.1f" r="15" fill="#fff" stroke="%s" stroke-width="2"/>'
            '<path d="M%.1f,%.1f l0,-9 M%.1f,%.1f l6,4" stroke="%s" stroke-width="2"/>' % (x, y, ACC2, x, y, x, y, ACC2)
            + text(x + 22, y + 5.5, label, size, 'start', 700, ACC2))


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
    notes = ['primer solo sulla lamina', 'aderente sotto il bordo', '', 'disegna la lunghezza', 'il gel più spesso al centro',
             'il gel scende verso l\'apex', 'controlla forma e spessori', 'via la dispersione, poi top']

    def d(i, x, y):
        cx, yb = x + 110, y + 255
        s = ''
        if notes[i]:
            s += text(cx, y + 66, notes[i], 15, fill=MUTED)
        if i in (0, 2):
            f, p = finger_nail(cx, yb, hw=30, nail_len=90, free_len=10, shape='tonda', finger_len=18,
                               plate=NAIL if i == 0 else '#f3b3c6')
            s += f
            if i == 0:
                s += _brush(cx + 8, yb - 70, -50, 80, '#f6e7a6', 'oval', load='#f6e7a6')
            else:
                s += _timer(x + 40, y + 92, 'LED 30–60 s')
        elif i in (1, 3):
            ys = yb - 90
            s += _form(cx, ys, 80, 92)
            if i == 3:
                s += ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5" opacity=".95"/>'
                      % (cx - 30, ys + 4, cx - 30, ys - 74, cx, ys - 80, cx + 30, ys - 74, cx + 30, ys + 4, GELC, NAIL_S))
                s += _brush(cx + 30, ys - 30, -35, 90, GEL, 'flat', load=GEL)
            f, p = finger_nail(cx, yb, hw=30, nail_len=90, free_len=8, shape='tonda', finger_len=18)
            s += f
        elif i == 4:
            sp, p = side_profile(x + 75, y + 180, w=130, stress=0.55, apex=0.45, apex_h=18, tip_h=5, root_h=2, gap=6)
            s += sp + bead(p['ax'], p['ah'] - 10, 13, GEL)
            s += _brush(p['ax'] + 14, p['ah'] - 20, -28, 80, GEL, 'oval')
        elif i == 5:
            sp, p = side_profile(x + 75, y + 165, w=130, stress=0.55, apex=0.45, apex_h=24, tip_h=5, root_h=2, gap=6)
            s += '<g transform="rotate(180 %.1f %.1f)">%s</g>' % (cx, y + 165, sp)
            s += ('<path d="M%.1f,%.1f A54,34 0 0 1 %.1f,%.1f" fill="none" stroke="%s" stroke-width="2.2" marker-end="url(#ar)"/>'
                  % (cx - 54, y + 112, cx + 54, y + 112, ACC2))
            s += mtext(cx, y + 226, ['mano capovolta,', 'poi lampada'], 15, weight=700, fill=ACC2)
        elif i == 6:
            f, p = finger_nail(cx, yb, hw=30, nail_len=90, free_len=70, shape='squoval', finger_len=18, plate='#f3b3c6', free=GELC)
            s += f + _file(cx + 40, yb - 120, -78, 104, 16)
        else:
            f, p = finger_nail(cx, yb, hw=30, nail_len=90, free_len=70, shape='squoval', finger_len=18, plate='#f3b3c6', free=GELC)
            s += f + '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round"/>' % (
                cx - 14, yb - 60, cx - 18, yb - 110, cx - 10, yb - 150)
            s += sparkle(cx + 18, yb - 140) + sparkle(cx + 50, yb - 165, 6)
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
            s += _form(cx, ys, 84, 96)
            if i >= 1:
                s += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="#fffdfd" stroke="%s" stroke-width="1.4"/>'
                      % (cx - 32, ys + 10, cx, ys - 6, cx + 32, ys + 10, cx + 32, ys - 70, cx, ys - 78, cx - 32, ys - 70, NAIL_S))
            f, p = finger_nail(cx, yb, hw=30, nail_len=90, free_len=6, shape='tonda', finger_len=18)
            s += f
            if i == 0:
                s += bead(cx, ys - 40, 20, '#ffffff')
                s += _brush(cx + 24, ys - 56, -40, 100, '#f3eee6', 'acrylic')
            elif i == 1:
                s += _brush(cx + 34, ys - 44, -35, 100, '#f3eee6', 'acrylic')
                s += arrow(cx - 64, ys - 40, cx - 38, ys - 40, MUTED, 1.5) + arrow(cx + 84, ys - 6, cx + 40, ys - 6, MUTED, 1.5)
            elif i == 2:
                s += bead(cx, ys + 30, 18, '#f9dbe4')
                s += _brush(cx + 20, ys + 14, -40, 100, '#f3eee6', 'acrylic')
            else:
                s += bead(cx, yb - 22, 11, '#f9dbe4')
                s += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="%s" stroke-width="1.6" stroke-dasharray="3 3" fill="none"/>' % (
                    cx - 30, yb - 30, cx, yb - 48, cx + 30, yb - 30, ERR)
                s += text(cx, y + 64, '≈1 mm dalla pelle', 15, weight=700, fill=ERR)
        elif i == 4:
            s += _ctip(cx, y + 140, 30, hw=56, col='#f6eef0', thick=9)
            s += arrow(cx - 110, y + 130, cx - 72, y + 138) + arrow(cx + 110, y + 130, cx + 72, y + 138)
            s += text(cx, y + 66, 'vista dal bordo libero', 15, fill=MUTED)
            s += text(cx, y + 254, 'quando il prodotto è ancora morbido', 15, fill=MUTED)
        else:
            sp, p = side_profile(x + 90, y + 180, w=170, stress=0.6, apex=0.47, apex_h=22, tip_h=5, root_h=2, gap=6, product='#f9dbe4')
            s += sp + _file(cx + 10, y + 126, -8, 140, 16)
            s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-dasharray="3 3"/>' % (p['ax'], p['ah'], p['ax'], p['oy'], ACC2)
            s += text(cx, y + 66, 'controlla l\'apex di profilo', 15, fill=MUTED)
        return s
    return steps_fig('Tutorial: ricostruzione in acrilico su cartina', labels, 3, 280, 270, d, 'Ricostruzione in acrilico in sei passaggi')


@fig('tut-semipermanente.svg')
def tut_semi():
    labels = ['Preparazione', 'Base + lampada', 'Colore: 1° strato', 'Colore: 2° strato', 'Top e sigilla il bordo', 'Cleaner e olio']
    COL = '#c2577a'
    notes = ['opacizza e togli la polvere', '', 'strato sottile, non colorare la pelle', '', '', ['via la dispersione,', 'olio sulla cuticola']]

    def d(i, x, y):
        cx, yb = x + 120, y + 255
        plate = [NAIL, '#f3b3c6', '#d98aa3', COL, COL, COL][i]
        f, p = finger_nail(cx, yb, hw=32, nail_len=110, free_len=14, shape='tonda', finger_len=18, plate=plate, free=plate if i else FREE, lunula=i == 0)
        s = f
        if notes[i]:
            s += mtext(x + 140, y + 66, notes[i] if isinstance(notes[i], list) else [notes[i]], 15, fill=MUTED)
        if i == 0:
            s += _file(cx + 40, yb - 96, -70, 120, 16, label='180', lsize=14)
        elif i == 1:
            s += _timer(x + 40, y + 70, 'LED 30–60 s')
            s += _bottle(x + 236, y + 252, '#f6e3ea', 56, 34)
        elif i == 2:
            s += _brush(cx + 18, yb - 100, -40, 100, COL, 'oval', load=COL)
            s += _bottle(x + 236, y + 252, COL, 56, 34)
        elif i == 3:
            s += _timer(x + 40, y + 70, 'secondo strato, lampada')
        elif i == 4:
            s += _brush(cx + 6, p['y_t'] - 2, -25, 100, '#fff', 'oval')
            s += _callout(cx - 6, p['y_t'] + 4, cx - 64, y + 104, ['passa', 'sul bordo'], 15)
            s += sparkle(cx - 12, yb - 80)
        else:
            dr = ('<rect x="-5" y="0" width="10" height="34" rx="2" fill="#f7f2f4" stroke="#bfb1b6"/>'
                  '<rect x="-9" y="-26" width="18" height="28" rx="8" fill="#4b3a40"/>'
                  '<path d="M-3,34 L0,44 L3,34 Z" fill="#bfb1b6"/>')
            s += _rot(cx + 30, yb - 118, 20, dr)
            s += drop(cx + 12, yb - 52) + sparkle(cx - 12, yb - 80)
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
            s += f + arrow(cx - 30, y + 90, cx + 30, y + 90, ACC2, 1.8, True) + text(cx, y + 76, 'da solco a solco', 15, weight=700, fill=ACC2)
        elif i == 1:
            tg = uid('tg')
            s += ('<defs><linearGradient id="%s" x1="0" x2="1"><stop offset="0" stop-color="#f1d3dc"/><stop offset=".3" stop-color="#fdf3f6"/>'
                  '<stop offset="1" stop-color="#efc9d4"/></linearGradient></defs>' % tg)
            tip = nail_outline(cx, y + 240, y + 160, y + 80, 34, 'mandorla')
            s += '<path d="%s" fill="url(#%s)" stroke="%s" stroke-width="1.6" filter="url(#nxShS)"/>' % (tip, tg, NAIL_S)
            s += '<ellipse cx="%.1f" cy="%.1f" rx="22" ry="30" fill="%s" opacity=".8"/>' % (cx, y + 205, GEL)
            s += '<ellipse cx="%.1f" cy="%.1f" rx="7" ry="10" fill="#fff" opacity=".6"/>' % (cx - 8, y + 196)
            s += _brush(cx + 26, y + 194, -40, 80, GEL, 'oval', load=GEL)
            s += text(cx, y + 66, 'strato sottile nell\'incavo', 15, fill=MUTED)
        elif i == 2:
            sx, sy = x + 6, y + 214
            fs, q = _finger_side(sx, sy, x + 66, x + 156, free=0, thick=56)
            s += fs
            px, py = x + 70, sy - 3
            s += ('<g filter="url(#nxShS)"><g transform="translate(%d,%d) rotate(-38)"><rect x="0" y="-6" width="128" height="8" rx="3" fill="#fbeaf0" stroke="%s"/>'
                  '<rect x="0" y="-6" width="40" height="8" rx="3" fill="%s" opacity=".8"/></g></g>' % (px, py, NAIL_S, GEL))
            s += ('<path d="M%d,%d A70,70 0 0 1 %d,%d" fill="none" stroke="%s" stroke-width="2" marker-end="url(#ar)"/>'
                  % (px + 110, py - 92, px + 136, py - 26, ACC2))
            s += text(cx, y + 66, 'parti dalla zona cuticolare', 15, fill=MUTED)
            s += text(cx, y + 85, 'poi abbassa: flash 5–10 s', 15, fill=MUTED)
        else:
            s += _lamp_side(cx, y + 248, 188, 100, opening=56)
            s += _hand_side(x + 4, y + 222, 170)
            s += mtext(cx, y + 66, ['LED 60 s', '(o come da scheda)'], 15, weight=700, fill='#6b4fa0')
            s += text(cx, y + 280, 'poi lima, cleaner e top', 15, fill=MUTED)
        return s
    return steps_fig('Tutorial: soft gel tips', labels, 4, 220, 290, d, 'Applicazione dei soft gel tips in quattro passaggi')


@fig('tut-french.svg')
def tut_french():
    labels = ['Segna i punti laterali', 'Traccia la curva', 'Riempi la punta', 'Sigilla con il top']
    notes = [['stessa altezza sui due lati'], ['pennello liner, mano ferma'], ['bianco pieno,', 'senza striature'], ['top su tutta l\'unghia', 'e sul bordo']]

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
        s += mtext(cx - (16 if i >= 2 else 0), y + 66, notes[i], 15, fill=MUTED)
        if i == 0:
            s += '<circle cx="%d" cy="%d" r="4" fill="#fff" stroke="%s"/><circle cx="%d" cy="%d" r="4" fill="#fff" stroke="%s"/>' % (cx - hw + 3, ys + 16, NAIL_S, cx + hw - 3, ys + 16, NAIL_S)
            s += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-dasharray="3 3"/>' % (cx - hw - 20, ys + 16, cx + hw + 20, ys + 16, ACC2)
        elif i == 1:
            s += _brush(cx + 22, ys - 6, -60, 100, '#fff', 'liner')
        elif i == 2:
            s += _brush(cx + 18, ys - 12, -60, 95, '#fff', 'flat', load='#fff')
        else:
            s += _brush(cx + 24, ys - 18, -60, 90, '#fdf6f8', 'oval')
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
            pid = uid('fb')
            s += ('<defs><pattern id="%s" width="7" height="7" patternUnits="userSpaceOnUse"><rect width="7" height="7" fill="#f8f2e6"/>'
                  '<path d="M0,3.5 L7,3.5 M3.5,0 L3.5,7" stroke="#cdbb9c" stroke-width="1"/></pattern></defs>' % pid)
            s += '<rect x="%d" y="%d" width="96" height="124" rx="3" fill="url(#%s)" stroke="#cdbb9c" filter="url(#nxShS)"/>' % (cx - 58, y + 80, pid)
            s += '<path d="M%d,%d Q%d,%d %d,%d" stroke="%s" stroke-width="2" stroke-dasharray="5 4" fill="none"/>' % (cx - 40, y + 196, cx - 10, y + 70, cx + 20, y + 196, ERR)
            sc = ('<path d="M0,0 L58,-5 L60,-1 Z" fill="#9aa3ad" stroke="#5f6973"/><path d="M0,0 L58,5 L60,1 Z" fill="#9aa3ad" stroke="#5f6973"/>'
                  '<circle cx="2" cy="0" r="3" fill="#5f6973"/>'
                  '<ellipse cx="-14" cy="-10" rx="11" ry="8" fill="none" stroke="#c2577a" stroke-width="4"/>'
                  '<ellipse cx="-14" cy="10" rx="11" ry="8" fill="none" stroke="#c2577a" stroke-width="4"/>')
            s += _rot(cx + 52, y + 196, -110, sc)
            s += text(cx, y + 244, 'a forma dell\'unghia,', 15, fill=MUTED) + text(cx, y + 263, '≈1 mm dalla pelle', 15, fill=MUTED)
            return s
        plate = '#f7d3dd'
        f, p = finger_nail(cx, yb, hw=32, nail_len=110, free_len=40, shape='squoval', finger_len=10, plate=plate, free=plate, extra=mesh if i < 3 else '', lunula=False)
        s += f
        if i == 1:
            s += _brush(cx + 24, yb - 120, -50, 100, '#fdf2c4', 'oval', load='#fdf2c4')
            s += text(cx, y + 66, 'la resina impregna la fibra', 15, fill=MUTED)
        elif i == 2:
            s += _brush(cx + 24, yb - 120, -50, 100, '#cfe9f7', 'oval')
            s += mtext(cx, y + 66, ['poco prodotto:', 'evita il calore'], 15, fill=ERR, weight=600)
        else:
            s += _file(cx + 44, yb - 110, -80, 120, 15) + sparkle(cx - 12, yb - 90)
            s += text(cx, y + 66, 'bordo libero sigillato', 15, fill=MUTED)
        return s
    return steps_fig('Tutorial: rinforzo in fibra di vetro o seta', labels, 4, 220, 290, d, 'Applicazione della fibra in quattro passaggi')


@fig('refill-step.svg')
def refill_steps():
    labels = ['Ricrescita visibile', 'Accorcia e assottiglia', 'Prepara la ricrescita', 'Ricostruisci e sigilla']

    def d(i, x, y):
        cx, yb = x + (80 if i == 0 else 110), y + 280
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
            s += _callout(cx + 22, yb - 24, x + 172, y + 196, ['ricrescita', '≈3 mm', 'al mese'], 15)
        elif i == 1:
            s += _file(cx + 44, yb - 120, -80, 120, 15)
            s += text(cx, y + 66, 'via ogni parte sollevata', 15, fill=ERR, weight=600)
        elif i == 2:
            s += _pusher(cx + 6, yb - 34, -60, 120)
            s += text(cx, y + 66, 'cuticola, opacizza, primer', 15, fill=MUTED)
        else:
            s += sparkle(cx - 10, yb - 100)
            s += text(cx, y + 66, 'apex di nuovo al suo posto', 15, fill=OK, weight=600)
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
            s += _file(cx + 30, yb - 150, -70, 110, 14)
        if i == 3:
            s += _file(cx, yb - 192, 0, 90, 14)
        s += text(cx, y + 66, ['tratteggio = forma finale', 'controlla la simmetria', 'stesso angolo per i 2 lati', 'punta centrata sull\'asse'][i], 15, fill=MUTED)
        return s
    return steps_fig('Come limare una mandorla partendo da una quadrata', labels, 4, 220, 300, d, 'Limatura della forma a mandorla in quattro passaggi')


@fig('cuticola.svg')
def cuticle():
    b = text(20, 38, 'Zona cuticolare: cosa si tocca e cosa no', 20, 'start', 800, ACC2)
    notes = [['spingicuticole quasi piatto,', 'senza forza'], ['solo pelle morta,', 'a lama piatta'], ['eponichio e pieghe sono vivi:', 'rischio infezioni']]
    for k, (t, ok) in enumerate([('Arretra l\'eponichio con delicatezza', True), ('Rimuovi la cuticola dalla lamina', True),
                                 ('Non tagliare la pelle viva', False)]):
        x = 20 + k * 300
        b += panel(x, 60, 285, 284, t)
        b += mark(x + 258, 122, ok)
        y = 222
        s, q = _finger_side(x + 12, y, x + 112, x + 212, free=12, thick=60, cuticle=False)
        b += s
        xf = q['xf']
        if k == 0:
            b += '<path d="M%d,%d Q%d,%d %d,%d" stroke="#fff" stroke-width="3.5" opacity=".9" fill="none" stroke-linecap="round"/>' % (
                xf + 6, y - 1.5, xf + 16, y - 3, xf + 28, y - 3)
            b += _pusher(xf + 10, y - 6, -14, 150)
            b += arrow(xf + 60, y - 62, xf + 20, y - 62)
            b += text(xf + 40, y - 72, 'spingi indietro', 15, weight=700, fill=ACC2)
        elif k == 1:
            for j in range(4):
                b += '<path d="M%d,%d l6,-3 l3,5 z" fill="#fff" stroke="#e2cfd4"/>' % (xf + 22 + j * 9, y - 6 - (j % 2) * 5)
            b += _stick(xf + 8, y - 4, -16, 140)
            b += _callout(xf + 26, y - 4, xf + 10, y - 58, 'pellicina sulla lamina', 15)
        else:
            nip = ('<path d="M0,-1.5 L30,-7 L32,0 Z" fill="#9aa3ad" stroke="#5f6973"/><path d="M0,1.5 L30,7 L32,0 Z" fill="#9aa3ad" stroke="#5f6973"/>'
                   '<path d="M32,-3 C60,-8 90,-20 120,-26" stroke="#7c8691" stroke-width="7" fill="none" stroke-linecap="round"/>'
                   '<path d="M32,3 C60,8 90,20 120,26" stroke="#7c8691" stroke-width="7" fill="none" stroke-linecap="round"/>'
                   '<path d="M48,-6 Q56,0 48,6" stroke="#5f6973" stroke-width="2" fill="none"/>'
                   '<circle cx="32" cy="0" r="5" fill="#c9d0d7" stroke="#5f6973"/>')
            b += _rot(xf - 6, y - 14, -28, nip)
            b += '<circle cx="%d" cy="%d" r="22" fill="none" stroke="%s" stroke-width="3"/>' % (xf - 6, y - 10, ERR)
            b += _callout(xf - 20, y - 12, xf - 48, y - 58, 'pelle viva', 15, fill=ERR)
        b += mtext(x + 142, 308, notes[k], 15, fill=MUTED)
    return svg(925, 360, arrow_defs() + b, 'Gestione corretta della zona cuticolare')


@fig('lampada-posizione.svg')
def lamp_pos():
    b = text(20, 38, 'In lampada: posizione e picco di calore', 20, 'start', 800, ACC2)
    b += panel(20, 60, 285, 292, 'Mano piatta, dita dentro')
    b += mark(278, 112, True)
    b += _lamp_side(170, 270, 220, 110, opening=62)
    b += _hand_side(28, 238, 210)
    b += text(162, 322, 'il pollice si polimerizza a parte', 15, fill=MUTED)
    b += panel(320, 60, 285, 292, 'Dita fuori o inclinate')
    b += mark(578, 112, False)
    b += _lamp_side(470, 270, 220, 110, opening=62)
    b += _hand_side(330, 254, 142, -16)
    b += '<path d="M440,268 L520,268 L470,232 Z" fill="#3b2a30" opacity=".12"/>'
    b += _callout(486, 258, 520, 196, 'zona in ombra', 15, fill=ERR)
    b += mtext(462, 314, ['zone in ombra =', 'gel non polimerizzato'], 15, fill=ERR, weight=600)
    # grafico flash and pull
    b += panel(620, 60, 300, 292, '"Flash and pull"')
    ox, oy = 650, 290
    b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s"/><line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s"/>' % (ox, oy, ox + 250, oy, INK, ox, oy, ox, 110, INK)
    b += text(ox + 125, oy + 21, 'tempo', 14.5, fill=MUTED)
    b += '<text x="%d" y="%d" font-size="14.5" fill="%s" transform="rotate(-90 %d %d)" text-anchor="middle">calore</text>' % (ox - 9, 200, MUTED, ox - 9, 200)
    b += '<line x1="%d" y1="150" x2="%d" y2="150" stroke="%s" stroke-dasharray="5 4"/>' % (ox, ox + 250, ERR)
    b += text(ox + 248, 143, 'soglia di bruciore', 14.5, 'end', 600, ERR)
    b += '<polyline points="%d,%d %d,%d %d,%d" fill="none" stroke="%s" stroke-width="2.5"/>' % (ox, oy - 10, ox + 60, 125, ox + 240, 200, ERR)
    b += '<polyline points="%d,%d %d,%d %d,%d %d,%d %d,%d %d,%d %d,%d" fill="none" stroke="%s" stroke-width="3"/>' % (
        ox, oy - 10, ox + 30, 175, ox + 45, 230, ox + 80, 180, ox + 95, 225, ox + 150, 200, ox + 240, 215, OK)
    b += text(ox + 125, 336, 'verde: togli la mano 5 s e rientra', 15, weight=700, fill=OK)
    return svg(940, 368, arrow_defs() + b, 'Posizione della mano in lampada e tecnica flash and pull')


@fig('dpi.svg')
def ppe():
    b = text(20, 38, 'Dispositivi di protezione individuale (DPI)', 20, 'start', 800, ACC2)
    items = ['Guanti in nitrile', 'Mascherina FFP2', 'Occhiali protettivi', 'Aspiratore da tavolo']
    subs = [['il lattice non ferma', 'i monomeri'], ['durante la limatura'], ['polveri e schizzi'], ['polveri e vapori', 'alla fonte']]
    gl = uid('gl')
    b += ('<defs><linearGradient id="%s" x1="0" x2="1"><stop offset="0" stop-color="#6f8fd8"/><stop offset=".5" stop-color="#9ab2ec"/>'
          '<stop offset="1" stop-color="#6683cf"/></linearGradient></defs>' % gl)
    for k, t in enumerate(items):
        x = 20 + k * 225
        b += panel(x, 60, 210, 262, t)
        cx, cy = x + 105, 190
        if k == 0:
            g = '<g fill="url(#%s)" stroke="#4f6fbf" stroke-width="1.8" filter="url(#nxShS)">' % gl
            for j, (dx, hgt) in enumerate([(-27, 50), (-9, 62), (9, 58), (26, 44)]):
                g += '<rect x="%d" y="%d" width="17" height="%d" rx="8.5"/>' % (cx + dx - 8, cy - 18 - hgt, hgt + 30)
            g += '<path d="M%d,%d C%d,%d %d,%d %d,%d L%d,%d L%d,%d Z"/>' % (
                cx - 36, cy - 26, cx - 38, cy + 20, cx - 30, cy + 46, cx - 26, cy + 52, cx + 30, cy + 52, cx + 36, cy - 26)
            g += '<rect x="%d" y="%d" width="18" height="52" rx="9" transform="rotate(-38 %d %d)"/>' % (cx - 58, cy - 20, cx - 49, cy + 6)
            g += '</g>'
            g += '<rect x="%d" y="%d" width="64" height="16" rx="6" fill="#5876c4" stroke="#4f6fbf" stroke-width="1.8"/>' % (cx - 32, cy + 48)
            for j in (-18, 0, 18):
                g += '<path d="M%d,%d q2,10 0,22" stroke="#4f6fbf" stroke-width="1" fill="none" opacity=".6"/>' % (cx + j, cy - 10)
            g += '<path d="M%d,%d L%d,%d" stroke="#fff" stroke-width="3" opacity=".45" stroke-linecap="round"/>' % (cx - 9, cy - 70, cx - 9, cy - 30)
            b += g
        elif k == 1:
            b += '<path d="M%d,%d C%d,%d %d,%d %d,%d" fill="none" stroke="#9aa3ad" stroke-width="2.5"/>' % (cx - 66, cy - 26, cx - 92, cy - 26, cx - 92, cy + 20, cx - 62, cy + 14)
            b += '<path d="M%d,%d C%d,%d %d,%d %d,%d" fill="none" stroke="#9aa3ad" stroke-width="2.5"/>' % (cx + 66, cy - 26, cx + 92, cy - 26, cx + 92, cy + 20, cx + 62, cy + 14)
            b += ('<path d="M%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="#f7f7f7" stroke="#aab1b8" stroke-width="2" filter="url(#nxShS)"/>'
                  % (cx - 70, cy - 34, cx, cy - 50, cx + 70, cy - 34, cx + 62, cy + 14, cx, cy + 70, cx - 62, cy + 14))
            b += '<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="#c8cdd2" stroke-width="2"/>' % (cx - 68, cy - 6, cx, cy + 8, cx + 68, cy - 6)
            b += '<rect x="%d" y="%d" width="44" height="6" rx="3" fill="#9aa3ad"/>' % (cx - 22, cy - 46)
            b += text(cx - 30, cy + 35, 'FFP2', 14.5, weight=800, fill='#8b939c')
        elif k == 2:
            b += '<path d="M%d,%d L%d,%d M%d,%d L%d,%d" stroke="#4b3a40" stroke-width="5" stroke-linecap="round"/>' % (
                cx - 80, cy - 18, cx - 92, cy - 30, cx + 80, cy - 18, cx + 92, cy - 30)
            b += ('<path d="M%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Q%d,%d %d,%d Q%d,%d %d,%d Z" fill="#dff0fa" fill-opacity=".85" '
                  'stroke="#4b3a40" stroke-width="3.5" filter="url(#nxShS)"/>'
                  % (cx - 82, cy - 22, cx, cy - 34, cx + 82, cy - 22, cx + 76, cy + 14, cx + 50, cy + 34, cx + 14, cy + 20,
                     cx, cy + 6, cx - 14, cy + 20, cx - 50, cy + 34, cx - 76, cy + 14))
            b += '<path d="M%d,%d Q%d,%d %d,%d" stroke="#4b3a40" stroke-width="5" fill="none"/>' % (cx - 82, cy - 22, cx, cy - 34, cx + 82, cy - 22)
            b += '<path d="M%d,%d L%d,%d M%d,%d L%d,%d" stroke="#fff" stroke-width="4" opacity=".8" stroke-linecap="round"/>' % (
                cx - 56, cy - 14, cx - 40, cy + 8, cx + 36, cy - 14, cx + 46, cy - 2)
        else:
            # aspiratore: piano forato in prospettiva, ventola, mano appoggiata
            b += '<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="#d8dde3" stroke="#8b939c" stroke-width="2"/>' % (
                cx - 80, cy + 40, cx + 80, cy + 40, cx + 80, cy + 64, cx - 80, cy + 64)
            b += '<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="#eef1f4" stroke="#8b939c" stroke-width="2"/>' % (
                cx - 60, cy - 10, cx + 60, cy - 10, cx + 80, cy + 40, cx - 80, cy + 40)
            for j in range(9):
                fx = -48 + j * 12
                b += '<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="#8b939c" stroke-width="2.5" stroke-linecap="round"/>' % (
                    cx + fx, cy - 2, cx + fx * 1.3, cy + 32)
            for j in range(3):
                b += arrow(cx - 40 + j * 40, cy - 58, cx - 40 + j * 40 * 1.05, cy - 18, ACC2, 2)
            for (dx, dy) in [(-52, -64), (-20, -72), (16, -66), (50, -74), (-4, -44), (34, -40)]:
                b += '<circle cx="%d" cy="%d" r="2.2" fill="#bfae9f"/>' % (cx + dx, cy + dy)
        b += mtext(cx, 286 + (9 if len(subs[k]) == 1 else 0), subs[k], 15, fill=MUTED)
    return svg(940, 338, arrow_defs() + b, 'Guanti, mascherina, occhiali e aspiratore')


@fig('ciclo-sterilizzazione.svg')
def steril_cycle():
    b = text(20, 38, 'Il ciclo degli strumenti dopo ogni cliente', 20, 'start', 800, ACC2)
    steps = [('Detergi', ['acqua e', 'detergente'], _ic_brushwash()), ('Disinfetta', ['per immersione'], _ic_tray()),
             ('Risciacqua', ['e asciuga bene'], _ic_tap()), ('Imbusta', ['buste sigillate'], _ic_pouch()),
             ('Autoclave', ['classe B', '(EN 13060)'], _ic_autoclave()), ('Registra', ['conserva', 'la stampa'], _ic_register())]
    cols = ['#f3c4d3', '#eeaabf', '#e48fa9', '#d6708f', ACC, ACC2]
    cw, gap, x0, y0, ch = 134, 22, 13, 62, 200
    for k, (t, sub, ic) in enumerate(steps):
        x = x0 + k * (cw + gap)
        cx = x + cw / 2
        b += '<rect x="%d" y="%d" width="%d" height="%d" rx="14" fill="%s"/>' % (x, y0, cw, ch, PANEL)
        b += '<circle cx="%.1f" cy="%d" r="44" fill="#fff" stroke="#efdcd6" stroke-width="1.2"/>' % (cx, y0 + 70)
        b += '<g transform="translate(%.1f,%d)">%s</g>' % (cx, y0 + 70, ic)
        b += '<circle cx="%d" cy="%d" r="13" fill="%s" stroke="#fff" stroke-width="2" filter="url(#nxShS)"/>' % (x + 20, y0 + 22, cols[k])
        b += text(x + 20, y0 + 27.5, str(k + 1), 15, weight=800, fill='#fff' if k > 1 else ACC2)
        b += text(cx, y0 + 142, t, 15, weight=800)
        b += mtext(cx, y0 + 165, sub, 15, fill=MUTED, lh=1.2)
        if k < 5:
            ax = x + cw + gap / 2
            b += '<circle cx="%.1f" cy="%d" r="12" fill="%s" stroke="#fff" stroke-width="2" filter="url(#nxShS)"/>' % (ax, y0 + 70, ACC2)
            b += '<path d="M%.1f,%d l7,6 l-7,6" stroke="#fff" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' % (ax - 3, y0 + 64)
    # avvertenza: monouso
    y1 = y0 + ch + 18
    b += '<rect x="13" y="%d" width="914" height="50" rx="12" fill="#fbe7e4" stroke="#f0c4bd" stroke-width="1"/>' % y1
    lime = ('<g transform="translate(52,%d) rotate(-20)"><rect x="-26" y="-6" width="52" height="12" rx="6" fill="#efe7df" stroke="#cbbdb0"/>'
            '<rect x="-24" y="-4" width="48" height="8" rx="4" fill="#8f8178"/></g>' % (y1 + 25))
    b += lime + ('<circle cx="52" cy="%d" r="17" fill="none" stroke="%s" stroke-width="3"/>'
                 '<line x1="40" y1="%d" x2="64" y2="%d" stroke="%s" stroke-width="3"/>' % (y1 + 25, ERR, y1 + 37, y1 + 13, ERR))
    b += text(84, y1 + 30, 'Lime in carta e buffer non si sterilizzano: sono monouso o si regalano alla cliente.', 14.5, 'start', 700, ERR)
    return svg(940, y1 + 66, b, 'Ciclo di ricondizionamento degli strumenti: detersione, disinfezione, risciacquo, imbustamento, autoclave, registrazione')


@fig('pennelli.svg')
def brushes():
    b = text(20, 38, 'I pennelli e gli strumenti di stesura', 20, 'start', 800, ACC2)
    items = [('Piatto per gel', 'base e costruttore', 'flat', GEL), ('Ovale / tondo', 'gel, zona cuticolare', 'oval', GEL),
             ('Acrilico 8–12', 'raccoglie la perla', 'acrylic', '#f3eee6'), ('Liner / striper', 'linee e dettagli', 'liner', '#3b2a30'),
             ('Ventaglio', 'polveri e glitter', 'fan', '#f3eee6'), ('Dotter', 'puntini', 'dot', None)]
    for k, (t, sub, kind, col) in enumerate(items):
        cx = 82 + k * 155
        if kind in ('flat', 'oval', 'acrylic', 'liner'):
            inner = _brush(0, 0, 90, 130, col, kind, shadow=False)
            b += '<g transform="translate(%d,62) scale(1.6)" filter="url(#nxShS)">%s</g>' % (cx, inner)
        elif kind == 'fan':
            s = ''
            for j in range(-6, 7):
                s += '<line x1="0" y1="62" x2="%.1f" y2="%.1f" stroke="#d9cdb9" stroke-width="2"/>' % (j * 6.2, 14 + abs(j) * 1.2)
            s += '<path d="M0,62 L-38,22 Q0,2 38,22 Z" fill="#f3eee6" opacity=".7" stroke="#cbbfae"/>'
            s += '<rect x="-9" y="58" width="18" height="26" rx="2" fill="#9aa3ad" stroke="#6f7983"/>'
            s += '<path d="M-9,64 L9,64 M-9,78 L9,78" stroke="#6f7983"/>'
            s += '<path d="M-6,84 L-4,240 Q0,246 4,240 L6,84 Z" fill="#4b3a40"/>'
            b += '<g transform="translate(%d,30)" filter="url(#nxShS)">%s</g>' % (cx, s)
        else:
            s = '<path d="M-5,90 L-4,250 Q0,256 4,250 L5,90 Z" fill="#c2577a"/>'
            s += '<rect x="-2" y="56" width="4" height="36" fill="#9aa3ad" stroke="#6f7983" stroke-width=".6"/>'
            s += '<circle cx="0" cy="54" r="7" fill="#9aa3ad" stroke="#6f7983"/><circle cx="-2" cy="52" r="2" fill="#fff" opacity=".8"/>'
            s += '<rect x="-2" y="250" width="4" height="20" fill="#9aa3ad" stroke="#6f7983" stroke-width=".6"/>'
            s += '<circle cx="0" cy="272" r="4" fill="#9aa3ad" stroke="#6f7983"/>'
            b += '<g transform="translate(%d,0)" filter="url(#nxShS)">%s</g>' % (cx, s)
        b += text(cx, 306, t, 16, weight=700)
        b += text(cx, 327, sub, 15, fill=MUTED)
    b += text(470, 366, 'Pulisci i pennelli per gel con il cleaner e quelli per acrilico con il monomero; conservali al riparo dalla luce.', 15, fill=MUTED)
    return svg(940, 382, b, 'Tipi di pennelli per la ricostruzione')


@fig('tip-tipi.svg')
def tip_types():
    b = text(20, 38, 'Tip: tipi e misure', 20, 'start', 800, ACC2)
    tg = uid('tg')
    b += ('<defs><linearGradient id="%s" x1="0" x2="1"><stop offset="0" stop-color="#e6ddd0"/><stop offset=".22" stop-color="#fbf8f3"/>'
          '<stop offset=".7" stop-color="#f6f1ea"/><stop offset="1" stop-color="#ded4c6"/></linearGradient>'
          '<pattern id="hatch2" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
          '<line x1="0" y1="0" x2="0" y2="6" stroke="%s" stroke-width="2"/></pattern></defs>' % (tg, GEL))
    b += panel(20, 60, 300, 290, 'Con incavo (well)')
    b += panel(335, 60, 300, 290, 'A contatto (contact)')
    for k, x in enumerate((170, 485)):
        tip = nail_outline(x, 236, 176, 104, 40, 'squoval')
        b += '<path d="%s" fill="url(#%s)" stroke="#b9ab98" stroke-width="1.6" filter="url(#nxShS)"/>' % (tip, tg)
        b += '<rect x="%d" y="112" width="6" height="110" rx="3" fill="#fff" opacity=".7"/>' % (x - 26)
        if k == 0:
            b += '<path d="M%d,%d Q%d,%d %d,%d L%d,%d L%d,%d Z" fill="url(#hatch2)" stroke="%s"/>' % (x - 40, 212, x, 192, x + 40, 212, x + 40, 242, x - 40, 242, ACC)
            b += '<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="%s" stroke-width="2.5"/>' % (x - 40, 212, x, 192, x + 40, 212, ACC2)
            b += _callout(x + 30, 206, x + 92, 150, ['linea di', 'arresto'], 15)
            # profilo: gradino dell'incavo
            b += '<path d="M%d,282 L%d,282 L%d,276 L%d,276 Q%d,276 %d,280 L%d,282 Z" fill="#f6f1ea" stroke="#b9ab98"/>' % (
                x - 80, x - 40, x - 36, x + 70, x + 78, x + 80, x + 76)
            b += '<rect x="%d" y="282" width="44" height="5" fill="%s" opacity=".5"/>' % (x - 80, GEL)
            b += text(x, 314, 'profilo: l\'incavo crea un gradino', 15, fill=MUTED)
            b += text(x, 334, 'da fondere dopo l\'applicazione', 15, fill=MUTED)
        else:
            b += '<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="#cbbfae" stroke-width="1.5" stroke-dasharray="4 3"/>' % (x - 40, 226, x, 210, x + 40, 226)
            b += '<path d="M%d,282 L%d,276 Q%d,276 %d,280 L%d,282 Z" fill="#f6f1ea" stroke="#b9ab98"/>' % (x - 80, x + 70, x + 78, x + 80, x + 76)
            b += text(x, 314, 'profilo: bordo sottile, nessun incavo', 15, fill=MUTED)
            b += text(x, 334, 'meno da fondere, presa minore', 15, fill=MUTED)
    b += panel(650, 60, 270, 290, 'Misure (0 = la più larga)')
    for k in range(10):
        w = 46 - k * 3.2
        x = 690 + (k % 5) * 48
        y = 160 + (k // 5) * 100
        b += '<path d="%s" fill="url(#%s)" stroke="#b9ab98"/>' % (nail_outline(x, y + 4, y - 20, y - 50, w / 2, 'squoval'), tg)
        b += text(x, y + 31, str(k), 15, weight=800)
    b += text(785, 334, 'una misura per ogni dito', 15, fill=MUTED)
    return svg(940, 366, b, 'Tip con incavo, tip a contatto e scala delle misure')


@fig('scheda-cliente.svg')
def client_card():
    b = '<rect x="30" y="20" width="620" height="520" rx="14" fill="#fff" stroke="#e5d6d2" stroke-width="2"/>'
    b += '<rect x="30" y="20" width="620" height="60" rx="14" fill="%s"/><rect x="30" y="60" width="620" height="20" fill="%s"/>' % (ACC, ACC)
    b += text(60, 58, 'Scheda cliente', 22, 'start', 800, '#fff')
    b += text(620, 58, 'n. ____', 15, 'end', 600, '#fff')
    rows = [('Nome e cognome', 'line'), ('Telefono / e-mail', 'line'), ('Informativa privacy consegnata', 'check'), ('Consenso dati di salute (firmato)', 'check'),
            ('Allergie (acrilati, lattice…)', 'line'), ('Farmaci, diabete, gravidanza, terapie', 'line'),
            ('Abitudini (onicofagia, acqua…)', 'line'), ('Stato della lamina / controindicazioni', 'line'),
            ('Servizio e prodotti (lotti)', 'line'), ('Consenso foto (facoltativo, a parte)', 'box'), ('Prossimo refill', 'line')]
    for k, (lab, kind) in enumerate(rows):
        y = 112 + k * 38
        b += text(60, y, lab, 14, 'start', 600)
        if kind == 'line':
            b += '<line x1="340" y1="%d" x2="620" y2="%d" stroke="#d8c8c4" stroke-width="1.5"/>' % (y + 3, y + 3)
        else:
            b += '<rect x="340" y="%d" width="16" height="16" rx="3" fill="none" stroke="%s" stroke-width="2"/>' % (y - 12, ACC2)
            if kind == 'check':
                b += '<path d="M343,%d l4,5 l8,-10" stroke="%s" stroke-width="2.5" fill="none"/>' % (y - 4, OK)
            else:
                b += text(366, y, 'sì / no: decide la cliente', 14, 'start', fill=MUTED)
    b += text(60, 530, 'Firma della cliente ______________________     Data ___/___/______', 14, 'start', fill=MUTED)
    return svg(680, 560, b, 'Esempio di scheda cliente')


# ================================================================= MODULI 13-16
@fig('onicofagia.svg')
def nail_biting():
    labels = ['Valuta l\'unghia', 'Adatta e tira la cartina', 'Letto artificiale (cover)', 'Bordo corto e tondo']

    def d(i, x, y):
        cx, yb = x + 110, y + 280
        s = ''
        if i == 1:
            s += form_top(cx, yb - 70, 80, 140)
            s += arrow(cx + 62, yb - 120, cx + 62, yb - 80) + arrow(cx - 62, yb - 120, cx - 62, yb - 80)
        ext = ''
        if i >= 2:
            ext = '<rect x="%d" y="%d" width="80" height="60" fill="%s" clip-path="url(#CLIP)"/>' % (cx - 40, yb - 118, '#f2b3c3')
        free = 0 if i < 2 else (26 if i == 2 else 22)
        f, p = finger_nail(cx, yb, hw=32, nail_len=55, free_len=free, shape='tonda', smile=6, finger_len=10,
                           plate='#f4c4cf', free='#ffffff' if i == 3 else '#f2b3c3', lunula=i < 2, extra=ext)
        s += f
        if i == 0:
            s += '<path d="M%d,%d Q%d,%d %d,%d" stroke="%s" stroke-width="5" fill="none" stroke-linecap="round"/>' % (cx - 34, yb - 58, cx, yb - 74, cx + 34, yb - 58, '#e9a98e')
            s += _callout(cx + 20, yb - 64, cx + 4, y + 136, ['pelle rialzata', 'davanti all\'unghia'], 15)
            s += mtext(cx, y + 66, ['ferite o infiammazione?', 'STOP'], 15, weight=700, fill=ERR)
        elif i == 2:
            s += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-dasharray="4 4"/>' % (cx - 50, yb - 55, cx + 50, yb - 55, ACC2)
            s += text(cx, y + 66, 'tratteggio = letto naturale', 15, fill=MUTED)
        elif i == 3:
            s += mtext(cx, y + 66, ['corta: più difficile', 'da mordere'], 15, fill=MUTED)
        return s
    return steps_fig('Onicofagia: ricostruzione su unghie rosicchiate', labels, 4, 220, 300, d, 'Ricostruzione su unghie rosicchiate in quattro passaggi')


@fig('unghie-difficili.svg')
def difficult():
    b = text(20, 38, 'Unghie difficili: riconoscerle e adattare la costruzione', 20, 'start', 800, ACC2)
    items = [('A cucchiaio (coilonichia)', ['livella la conca,', 'poi l\'apex']),
             ('Ski-jump (punta in su)', ['accorcia, cartina', 'inclinata in giù']),
             ('A pinza / a tegola', ['curva C moderata,', 'niente pinching']),
             ('Piatta e larga', ['crea la curva C,', 'lati non svasati'])]
    for k, (t, sub) in enumerate(items):
        x = 20 + k * 225
        b += panel(x, 60, 210, 288, t)
        cx = x + 105
        if k < 2:
            y = 190
            s, q = _finger_side(x + 8, y, x + 70, x + 150, plate=False, thick=56)
            b += s
            if k == 0:
                b += ('<path d="M%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="#f6d3dc" stroke="%s" stroke-width="1.6"/>'
                      % (x + 54, y, x + 120, y + 16, x + 176, y - 12, x + 176, y - 6, x + 120, y + 22, x + 54, y + 5, NAIL_S))
                b += '<path d="M%d,%d q6,10 0,15 q-6,-5 0,-15 z" fill="#7fc3e8" stroke="#4f9cc7"/>' % (x + 116, y - 2)
                b += _callout(x + 116, y + 4, x + 105, 140, 'la goccia resta ferma', 15, weight=400, fill=MUTED)
            else:
                b += ('<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d L%d,%d Z" fill="#f6d3dc" stroke="%s" stroke-width="1.6"/>'
                      % (x + 54, y, x + 140, y, x + 166, y - 2, x + 184, y - 30, x + 189, y - 27, x + 170, y + 4, x + 140, y + 5, x + 54, y + 5, NAIL_S))
                b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2.5" stroke-dasharray="6 4"/>' % (x + 146, y + 4, x + 200, y + 12, OK)
                b += mtext(cx, 124, ['tratteggio =', 'nuova direzione'], 15, fill=MUTED)
        elif k == 2:
            b += _ctip(cx, 204, 34, hw=44, col='#eaa0b6', thick=8)
            for sx in (-1, 1):
                b += arrow(cx + sx * 74, 208, cx + sx * 52, 206, ERR, 2)
            b += mtext(cx, 124, ['vista dalla punta:', 'stringe i lati'], 15, fill=MUTED)
        else:
            b += _ctip(cx, 204, 4, hw=80, col='#eaa0b6', thick=8)
            b += '<path d="M%d,%d Q%d,%d %d,%d" stroke="%s" stroke-width="2.5" fill="none" stroke-dasharray="6 4"/>' % (cx - 76, 192, cx, 152, cx + 76, 192, OK)
            b += text(cx, 132, 'vista dalla punta', 15, fill=MUTED)
        b += mtext(cx, 316, sub, 15, weight=700)
    b += text(470, 372, 'Forma insolita, comparsa da poco o dolorosa? Consiglia il medico (es. la coilonichia è spesso legata a carenza di ferro).', 14.5, fill=ERR, weight=600)
    return svg(940, 386, arrow_defs() + b, 'Unghia a cucchiaio, ski-jump, a pinza e piatta')


@fig('cover-letto.svg')
def cover_bed():
    labels = ['Letto naturale corto', 'Allunga (cartina o tip)', 'Cover oltre il letto', 'Smile line più avanti']

    def d(i, x, y):
        cx, yb = x + 110, y + 290
        ext = ''
        if i >= 2:
            ext = '<rect x="%d" y="%d" width="80" height="%d" fill="#f0b9c4" clip-path="url(#CLIP)"/>' % (cx - 40, yb - 150, 120)
        if i == 3:
            ext += '<path d="M%d,%d Q%d,%d %d,%d L%d,%d L%d,%d Z" fill="#fff" clip-path="url(#CLIP)"/>' % (
                cx - 40, yb - 128, cx, yb - 156, cx + 40, yb - 128, cx + 40, yb - 260, cx - 40, yb - 260)
        f, p = finger_nail(cx, yb, hw=32, nail_len=70, free_len=0 if i == 0 else 90, shape='squoval', smile=8, finger_len=6,
                           plate='#f4c4cf', free='#f7f1ec', lunula=False, extra=ext)
        s = f
        s += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-dasharray="4 4"/>' % (cx - 52, yb - 70, cx + 52, yb - 70, ACC2)
        if i == 0:
            s += text(cx, y + 66, 'tratteggio = fine del letto', 15, fill=MUTED)
        elif i == 2:
            s += mtext(cx, y + 66, ['cover coprente,', 'senza "finestre"'], 15, fill=MUTED)
        elif i == 3:
            s += text(cx, y + 66, 'il letto sembra più lungo', 15, fill=OK, weight=600)
        return s
    return steps_fig('Cover / camouflage: allungare otticamente il letto ungueale', labels, 4, 220, 300, d, 'Allungamento ottico del letto ungueale con gel cover')


@fig('colori-sottotono.svg')
def colors():
    b = text(20, 38, 'Colore: cerchio cromatico e scelta del cover', 20, 'start', 800, ACC2)
    cx, cy, r = 190, 210, 120
    hues = ['#e53935', '#fb8c00', '#fdd835', '#7cb342', '#1e88e5', '#8e24aa']
    names = ['rosso', 'arancio', 'giallo', 'verde', 'blu', 'viola']
    for k, c in enumerate(hues):
        a0, a1 = math.radians(-90 + k * 60 - 30), math.radians(-90 + k * 60 + 30)
        b += '<path d="M%d,%d L%.1f,%.1f A%d,%d 0 0 1 %.1f,%.1f Z" fill="%s" stroke="#fff" stroke-width="3"/>' % (
            cx, cy, cx + r * math.cos(a0), cy + r * math.sin(a0), r, r, cx + r * math.cos(a1), cy + r * math.sin(a1), c)
        am = math.radians(-90 + k * 60)
        b += text(cx + (r + 24) * math.cos(am), cy + (r + 24) * math.sin(am) + 5.5, names[k], 15, weight=600)
    b += '<circle cx="%d" cy="%d" r="67" fill="#fff"/>' % (cx, cy)
    b += mtext(cx, cy - 4, ['colori opposti', '= complementari'], 14.5, weight=700)
    b += mtext(cx, 380, ['viola ↔ giallo: un tocco violaceo', 'attenua il giallo'], 15, fill=MUTED)
    b += text(420, 90, 'Sottotono della pelle → cover consigliato (indicazione pratica)', 15, 'start', 700)
    rows = [('Freddo', 'riflessi rosati, vene bluastre', '#f3c6cf', 'rosa / rosa-beige'),
            ('Caldo', 'riflessi dorati, vene verdastre', '#f5c9a8', 'pesca / nude caldo'),
            ('Neutro', 'via di mezzo', '#ecc9b6', 'nude beige')]
    for k, (t, desc, sw, cov) in enumerate(rows):
        y = 120 + k * 75
        b += '<rect x="420" y="%d" width="490" height="62" rx="12" fill="%s"/>' % (y, PANEL)
        b += '<circle cx="452" cy="%d" r="20" fill="%s" stroke="%s"/>' % (y + 31, sw, SKIN_D)
        b += text(484, y + 27, t, 15, 'start', 800)
        b += text(484, y + 48, desc, 15, 'start', fill=MUTED)
        b += '<rect x="712" y="%d" width="40" height="40" rx="8" fill="%s"/>' % (y + 11, ['#f2b3c3', '#f6c3a6', '#e9c5b1'][k])
        b += text(762, y + 36.5, cov, 15, 'start', 600)
    b += mtext(665, 380, ['Prova sempre un campione con luce naturale:', 'il colore giusto "sparisce".'], 15, fill=MUTED)
    return svg(940, 414, b, 'Cerchio cromatico e scelta del cover in base al sottotono')


@fig('piede-taglio.svg')
def toenail():
    b = text(20, 38, 'Unghie dei piedi: taglio e crescita', 20, 'start', 800, ACC2)
    cases = [('Dritto, angoli smussati', True, 'squoval'), ('Tondo e troppo corto', False, 'tonda'), ('Lati scavati', False, 'quadrata')]
    for k, (t, ok, sh) in enumerate(cases):
        x = 20 + k * 225
        b += panel(x, 60, 210, 290, t)
        b += mark(x + 185, 112, ok)
        cx, yb = x + 105, 316
        hw, nl = 50, 86 if k != 1 else 76
        extra = ''
        if k == 2:
            # angoli scavati a "V" nei solchi laterali
            for sx in (-1, 1):
                extra += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" clip-path="url(#CLIP)"/>' % (
                    cx + sx * (hw + 2), yb - nl - 8, cx + sx * (hw - 20), yb - nl - 8, cx + sx * (hw + 2), yb - nl + 34, '#e9b9a6')
                extra += _P('M%.1f,%.1f L%.1f,%.1f' % (cx + sx * (hw - 20), yb - nl - 4, cx + sx * (hw + 1), yb - nl + 32), 'none', '#b5776a', 1.6)
        f, p = _toe_top(cx, yb, hw=hw, nail_len=nl, free=8 if ok else (0 if k == 1 else 4), shape=sh, finger_len=20, extra=extra)
        pc = uid('p')
        b += '<defs><clipPath id="%s"><rect x="%d" y="60" width="210" height="290" rx="16"/></clipPath></defs>' % (pc, x)
        b += '<g clip-path="url(#%s)">%s</g>' % (pc, f)
        if ok:
            b += _ln(cx - hw - 18, p['y_t'], cx + hw + 18, p['y_t'], OK, 2, ' stroke-dasharray="6 4"')
            b += text(cx, 160, 'dritto, a filo del dito', 15, weight=600, fill=OK)
        else:
            ry = p['y_s'] + (hw * 0.42 if k == 1 else 10)
            b += '<circle cx="%.1f" cy="%.1f" r="15" fill="none" stroke="%s" stroke-width="3"/>' % (cx + hw, ry, ERR)
            b += '<path d="M%.1f,%.1f l10,0 M%.1f,%.1f l7,-7 M%.1f,%.1f l7,7" stroke="%s" stroke-width="2" stroke-linecap="round"/>' % (
                cx + hw + 18, ry, cx + hw + 18, ry - 5, cx + hw + 18, ry + 5, ERR)
            b += text(cx, 160, 'rischio unghia incarnita', 15, weight=600, fill=ERR)
    x0 = 700
    b += panel(x0, 60, 220, 290, 'Crescita media')
    for k, (lab, v, col) in enumerate([('Mani', 3.47, ACC), ('Piedi', 1.62, '#8a7d9e')]):
        h = v / 3.47 * 170
        bx = x0 + 50 + k * 80
        b += '<rect x="%d" y="%.1f" width="50" height="%.1f" rx="6" fill="%s"/>' % (bx, 300 - h, h, col)
        b += text(bx + 25, 291 - h, ('%.2f' % v).replace('.', ','), 16, weight=800)
        b += text(bx + 25, 321, lab, 15, weight=700)
    b += text(x0 + 110, 341, 'mm al mese (Yaemsiri 2010)', 14.5, fill=MUTED)
    return svg(940, 365, b, 'Taglio corretto delle unghie dei piedi e velocità di crescita')


@fig('pedicure-protocollo.svg')
def pedicure():
    labels = ['Anamnesi', 'Ispeziona: dubbi? STOP', 'Pediluvio igienico', 'Taglio dritto', 'Cuticola senza tagli', 'Semipermanente sottile']

    def d(i, x, y):
        cx, yb = x + 140, y + 236
        s = ''
        if i == 0:
            s += '<rect x="%d" y="%d" width="130" height="160" rx="10" fill="#fff" stroke="#e5d6d2" stroke-width="2" filter="url(#nxShS)"/>' % (cx - 65, y + 70)
            s += '<rect x="%d" y="%d" width="50" height="12" rx="4" fill="#9aa3ad"/>' % (cx - 25, y + 64)
            for k, t in enumerate(['diabete', 'circolazione', 'farmaci', 'micosi?']):
                s += '<rect x="%d" y="%d" width="12" height="12" rx="2" fill="none" stroke="%s" stroke-width="2"/>' % (cx - 48, y + 96 + k * 30, ACC2)
                s += text(cx - 28, y + 107.5 + k * 30, t, 15, 'start')
            return s
        if i == 2:
            s += text(cx, y + 66, 'vaschetta disinfettata o monouso', 15, fill=MUTED)
            s += text(cx, y + 85, 'acqua tiepida, non calda', 15, fill=MUTED)
            s += ('<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="#e8f3fb" stroke="#7fb0cc" stroke-width="2" filter="url(#nxShS)"/>'
                  % (cx - 100, y + 140, cx + 100, y + 140, cx + 92, y + 236, cx + 70, y + 240, cx - 70, y + 240, cx - 92, y + 236, cx - 100, y + 140))
            s += '<ellipse cx="%d" cy="%d" rx="100" ry="12" fill="#cfe6f4" stroke="#7fb0cc" stroke-width="2"/>' % (cx, y + 140)
            s += '<ellipse cx="%d" cy="%d" rx="86" ry="8" fill="#b9dcf0"/>' % (cx, y + 150)
            for k in range(3):
                s += '<path d="M%d,%d q12,-6 24,0 q12,6 24,0" stroke="#7fb4d6" stroke-width="2" fill="none"/>' % (cx - 70 + k * 40, y + 182 + (k % 2) * 16)
            for (dx, dy, r) in [(-40, 168, 4), (30, 200, 3), (60, 172, 3.5)]:
                s += '<circle cx="%d" cy="%d" r="%.1f" fill="#fff" stroke="#9cc3dc"/>' % (cx + dx, y + dy, r)
            return s
        plate = '#c2577a' if i == 5 else '#f3cbc6'
        f, p = _toe_top(cx, yb, hw=52, nail_len=84, free=6 if i != 5 else 0, shape='squoval', finger_len=30, plate=plate)
        s += f
        if i == 1:
            s += text(cx, y + 66, 'gialla, spessa, friabile → medico', 15, weight=700, fill=ERR)
            s += text(cx, y + 85, 'diabete con ferite → podologo', 15, weight=700, fill=ERR)
        elif i == 3:
            s += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2" stroke-dasharray="6 4"/>' % (cx - 96, p['y_t'], cx + 96, p['y_t'], OK)
            s += text(cx, y + 66, 'angoli appena smussati', 15, fill=MUTED)
        elif i == 4:
            s += _pusher(cx + 4, yb - 8, -58, 120)
            s += text(cx, y + 66, 'arretra e togli la pellicina', 15, fill=MUTED)
        else:
            s += sparkle(cx - 14, yb - 70)
            s += text(cx, y + 66, 'strati sottili, sigilla il bordo', 15, fill=MUTED)
        return s
    return steps_fig('Protocollo pedicure estetica con semipermanente', labels, 3, 280, 270, d, 'Protocollo di pedicure estetica in sei passaggi')


@fig('nail-art-effetti.svg')
def art_fx():
    labels = ['Chrome: top no-wipe', 'Strofina la polvere', 'Cat-eye: magnete', 'One-stroke']

    def d(i, x, y):
        cx, yb = x + 110, y + 290
        s = ''
        if i == 3:
            pg = uid('pg')
            s += ('<defs><linearGradient id="%s" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#c2577a"/>'
                  '<stop offset=".55" stop-color="#ec9ab4"/><stop offset="1" stop-color="#ffffff"/></linearGradient></defs>' % pg)
            petals = ''
            fx, fy = cx - 4, yb - 128
            for a in (-60, -20, 20, 60, 180):
                petals += ('<path d="M0,0 C-16,-12 -16,-36 0,-44 C16,-36 16,-12 0,0 Z" fill="url(#%s)" stroke="#fff" stroke-width="1" '
                           'transform="translate(%d,%d) rotate(%d)"/>' % (pg, fx, fy, a))
            petals += '<path d="M%d,%d q20,26 4,60" stroke="#5c8f5a" stroke-width="2.5" fill="none"/>' % (fx, fy)
            petals += '<path d="M%d,%d c14,-4 22,4 22,14 c-12,2 -20,-4 -22,-14 z" fill="#7fae6f"/>' % (fx + 10, fy + 30)
            f, p = finger_nail(cx, yb, hw=34, nail_len=110, free_len=50, shape='mandorla', smile=0, finger_len=8, lunula=False,
                               plate='#fbeef2', free='#fbeef2', extra='<g clip-path="url(#CLIP)">%s</g>' % petals)
            s += f
            br = ('<rect x="18" y="-6" width="64" height="12" rx="6" fill="#4b3a40"/><rect x="4" y="-7" width="16" height="14" rx="2" fill="#9aa3ad" stroke="#6f7983"/>'
                  '<path d="M4,-7 L-24,-6 L-28,0 L4,0 Z" fill="#c2577a"/><path d="M4,0 L-28,0 L-24,6 L4,7 Z" fill="#ffffff" stroke="#e2cfd4"/>')
            s += _rot(cx + 40, y + 140, -45, br)
            s += mtext(cx, y + 66, ['metà e metà, poi ruota', 'il pennello'], 15, fill=MUTED)
            return s
        plate = '#2b1f22' if i < 2 else '#3a2a55'
        ext = ''
        if i == 1:
            cg = uid('chr')
            ext = ('<defs><linearGradient id="%s" x1="0" x2="1"><stop offset="0" stop-color="#aab2ba"/><stop offset=".45" stop-color="#ffffff"/>'
                   '<stop offset=".6" stop-color="#dfe3e7"/><stop offset="1" stop-color="#8d96a0"/></linearGradient></defs>' % cg)
            ext += '<rect x="%d" y="%d" width="80" height="120" fill="url(#%s)" clip-path="url(#CLIP)"/>' % (cx - 40, yb - 190, cg)
        if i == 2:
            ext = ('<rect x="%d" y="%d" width="18" height="190" fill="#d8c8ff" opacity=".75" clip-path="url(#CLIP)" transform="rotate(20 %d %d)"/>'
                   '<rect x="%d" y="%d" width="6" height="190" fill="#fff" opacity=".6" clip-path="url(#CLIP)" transform="rotate(20 %d %d)"/>'
                   % (cx - 9, yb - 200, cx, yb - 100, cx - 3, yb - 200, cx, yb - 100))
        f, p = finger_nail(cx, yb, hw=34, nail_len=110, free_len=50, shape='mandorla', smile=0, finger_len=8, lunula=False, plate=plate, free=plate, extra=ext)
        s += f
        if i == 0:
            s += _timer(x + 40, y + 112, 'polimerizza')
            s += mtext(cx, y + 66, ['niente dispersione', 'da togliere'], 15, fill=MUTED)
        elif i == 1:
            ap = ('<rect x="0" y="-4" width="96" height="8" rx="4" fill="#4b3a40"/>'
                  '<ellipse cx="-8" cy="0" rx="14" ry="9" fill="#d5d9de" stroke="#9aa3ad"/>'
                  '<ellipse cx="-12" cy="-3" rx="5" ry="3" fill="#fff" opacity=".8"/>')
            s += _rot(cx + 22, yb - 120, -35, ap)
            s += _jar(x + 180, y + 270, '#d5d9de', 46, 26, lid='#9aa3ad')
            s += mtext(cx, y + 66, ['velo sottile,', 'poi sigilla i bordi'], 15, fill=MUTED)
        elif i == 2:
            mg = ('<rect x="0" y="-9" width="62" height="18" rx="9" fill="#4b3a40"/>'
                  '<rect x="-16" y="-9" width="20" height="18" rx="3" fill="#9aa3ad" stroke="#6f7983"/>'
                  '<rect x="-20" y="-9" width="6" height="18" rx="2" fill="%s"/>' % ERR)
            s += _rot(cx + 60, yb - 150, -70, mg)
            for r in (14, 24):
                s += '<path d="M%.1f,%.1f a%d,%d 0 0 0 %d,%d" stroke="#b9a7f0" stroke-width="1.6" fill="none" stroke-dasharray="3 3"/>' % (
                    cx + 52 - r, yb - 128, r, r, 2 * r, 0)
            s += mtext(cx, y + 66, ['orienta le particelle,', 'poi lampada'], 15, fill=MUTED)
        return s
    return steps_fig('Nail art avanzata: chrome, cat-eye e one-stroke', labels, 4, 220, 300, d, 'Effetti chrome, cat-eye e one-stroke')


@fig('gara-scheda.svg')
def score_sheet():
    b = text(20, 38, 'Gare: cosa guardano i giudici', 20, 'start', 800, ACC2)
    b += '<rect x="20" y="60" width="520" height="342" rx="14" fill="#fff" stroke="#e5d6d2" stroke-width="2" filter="url(#nxSh)"/>'
    b += '<rect x="20" y="60" width="520" height="46" rx="14" fill="%s"/><rect x="20" y="90" width="520" height="16" fill="%s"/>' % (ACC, ACC)
    b += text(40, 90, 'Scheda di autovalutazione (modello gara)', 16, 'start', 800, '#fff')
    b += text(464, 129, 'punti 1–5', 14.5, fill=MUTED)
    rows = ['Curva C uniforme (vista a tunnel)', 'Apex nella stessa posizione', 'Bordo libero sottile e uniforme', 'Smile line simmetrica',
            'Zona cuticolare pulita', 'Superficie lucida, senza graffi']
    for k, r in enumerate(rows):
        y = 158 + k * 36
        if k % 2 == 0:
            b += '<rect x="30" y="%d" width="500" height="34" rx="6" fill="#fbf4f2"/>' % (y - 23)
        b += text(40, y, r, 15, 'start', 600)
        for j in range(5):
            b += '<circle cx="%d" cy="%d" r="8" fill="%s" stroke="%s"/>' % (420 + j * 22, y - 5, ACC if j < 4 - k % 3 else '#fff', ACC)
    b += mtext(40, 368, ['Leggi sempre il regolamento dell\'edizione:', 'tempi, divieti e punteggi cambiano.'], 15, 'start', fill=MUTED)
    b += panel(560, 60, 360, 342, 'Vista "a tunnel"')
    for k, (ok, kk) in enumerate([(True, 30), (False, 8)]):
        cx, y = 652 + k * 176, 236
        b += '<g transform="translate(%d,%d) scale(.8) translate(%d,%d)">%s</g>' % (cx, y, -cx, -y, _ctip(cx, y, kk, hw=66, col='#eaa0b6', thick=8))
        b += mark(cx, 140, ok)
        b += mtext(cx, 336, ['arco regolare,', 'spessore uniforme'] if ok else ['piatta o', 'irregolare'], 15, fill=OK if ok else ERR, weight=600)
    b += text(740, 388, 'guarda dalla punta verso la cuticola', 15, fill=MUTED)
    return svg(940, 418, b, 'Scheda di valutazione stile gara e vista a tunnel')


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, f in FIGS.items():
        with open(os.path.join(OUT, name), 'w', encoding='utf-8') as fh:
            fh.write(f())
    print('Generate %d illustrazioni in %s' % (len(FIGS), os.path.normpath(OUT)))


if __name__ == '__main__':
    main()
