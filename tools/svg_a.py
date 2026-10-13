#!/usr/bin/env python3
"""Illustrazioni del gruppo A (moduli anatomia, igiene, sistemi, attrezzatura). Uso: python3 tools/svg_a.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_svg import *  # palette, svg(), text(), mtext(), leader(), arrow(), panel(), mark(), finger_nail(), side_profile(), tool_*(), lamp(), timer(), steps_fig(), ...
import gen_svg
import math

MINE = {}


def figx(name):
    def deco(f):
        MINE[name] = f; gen_svg.FIGS[name] = f
        return f
    return deco


# ================================================================= colori aggiuntivi (coerenti con la palette)
PROD, PROD_S = '#d6ebf6', '#7fb0cc'     # prodotto artificiale
L_TOP, L_MID, L_BOT = '#b39ddb', '#d1c4e9', '#f8bbd0'   # strati della lamina
YEL = '#f1d27a'
AMBER = '#f2b632'
GREY, GREY_D = '#9aa3ad', '#6f7983'
METAL, METAL_D = '#c5ccd3', '#7d8792'
NITR, NITR_D = '#7f8fd6', '#4f5fae'      # guanti in nitrile
OK_BG, ERR_BG, WARN_BG = '#e7f3ec', '#fbe9e7', '#fdf3dc'
BLUE_BG = '#e6f1f8'
UV = '#7b4bd6'


# ================================================================= testo
def tw(s, size, bold=False):
    """Larghezza stimata di un testo (font Inter/system-ui)."""
    return len(s) * size * (0.56 if bold else 0.51)


def wrap(s, maxw, size, bold=False):
    words, lines, cur = s.split(' '), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if cur and tw(t, size, bold) > maxw:
            lines.append(cur)
            cur = w
        else:
            cur = t
    if cur:
        lines.append(cur)
    return lines


def para(x, y, s, maxw, size=13.5, anchor='start', weight=400, fill=INK, lh=1.3):
    """Paragrafo a capo automatico. Restituisce (svg, altezza)."""
    lines = wrap(s, maxw, size, weight >= 600)
    return mtext(x, y, lines, size, anchor, weight, fill, lh), len(lines) * size * lh


def title(s, x=20, y=38):
    return text(x, y, s, 20, 'start', 800, ACC2)


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


# ================================================================= cornici, badge, segni
def frame(x, y, w, h, ttl=None, num=None, ok=None, color=ACC, border=None, fill=PANEL, tsize=15, bw=2.5):
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="16" fill="%s"%s/>' % (
        x, y, w, h, fill, (' stroke="%s" stroke-width="%s"' % (border, bw)) if border else '')
    if ttl:
        if num is not None:
            s += '<circle cx="%.1f" cy="%.1f" r="15" fill="%s"/>' % (x + 26, y + 26, color)
            s += text(x + 26, y + 31.5, str(num), 15, weight=800, fill='#fff')
            s += text(x + 50, y + 31, ttl, tsize, 'start', 700)
        elif ok is not None:
            s += text(x + 18, y + 31, ttl, tsize, 'start', 700)
        else:
            s += text(x + w / 2, y + 31, ttl, tsize, weight=700)
    if ok is not None:
        s += mark(x + w - 26, y + 26, ok)
    return s


def badge(x, y, n, color=ACC, r=13, size=14):
    return ('<circle cx="%.1f" cy="%.1f" r="%s" fill="%s" stroke="#fff" stroke-width="2"/>' % (x, y, r, color)
            + text(x, y + size * 0.36, str(n), size, weight=800, fill='#fff'))


def chip(cx, cy, s, fill, fg='#fff', size=12.5, pad=9, bold=True):
    w = tw(s, size, bold) + 2 * pad
    return ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s"/>' % (cx - w / 2, cy - size * 0.95, w, size * 1.75, size * 0.87, fill)
            + text(cx, cy + size * 0.38, s, size, weight=700 if bold else 400, fill=fg))


def no_sign(x, y, r=16, w=3.5):
    return ('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" stroke-width="%s"/>'
            '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s"/>'
            % (x, y, r, ERR, w, x - r * 0.7, y - r * 0.7, x + r * 0.7, y + r * 0.7, ERR, w))


def warn_tri(x, y, r=13, col=AMBER):
    return ('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="#fff" stroke-width="1.5" stroke-linejoin="round"/>'
            % (x, y - r, x + r * 1.1, y + r * 0.8, x - r * 1.1, y + r * 0.8, col)
            + text(x, y + r * 0.62, '!', r * 1.15, weight=900, fill='#fff'))


def excl(x, y, col=AMBER, r=13):
    return '<circle cx="%.1f" cy="%.1f" r="%s" fill="%s"/>' % (x, y, r, col) + text(x, y + r * 0.45, '!', r * 1.25, weight=900, fill='#fff')


def curved(x1, y1, x2, y2, bend=30, color=ACC2, w=2, dash=''):
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1
    cx, cy = mx - dy / L * bend, my + dx / L * bend
    m = 'ar' if color == ACC2 else 'arw'
    return ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="%s"%s marker-end="url(#%s)"/>'
            % (x1, y1, cx, cy, x2, y2, color, w, (' stroke-dasharray="%s"' % dash) if dash else '', m))


def carrow(x1, y1, x2, y2, color, w=2.2, dash=''):
    """Freccia colorata qualsiasi (marker dedicato)."""
    mid = uid('mk')
    return ('<defs><marker id="%s" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            '<path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>'
            '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s" marker-end="url(#%s)"%s/>'
            % (mid, color, x1, y1, x2, y2, color, w, mid, (' stroke-dasharray="%s"' % dash) if dash else ''))


def cpath(d, color, w=2.2, dash=''):
    mid = uid('mk')
    return ('<defs><marker id="%s" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            '<path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>'
            '<path d="%s" fill="none" stroke="%s" stroke-width="%s" marker-end="url(#%s)"%s/>'
            % (mid, color, d, color, w, mid, (' stroke-dasharray="%s"' % dash) if dash else ''))


def callout(px, py, lx, ly, label, size=14, weight=700, fill=INK, anchor='middle'):
    """Etichetta centrata in (lx, ly) con linea che parte da sotto (o sopra) il testo verso il punto (px, py)."""
    ey = ly + 6 if py > ly else ly - size - 2
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.3"/><circle cx="%.1f" cy="%.1f" r="3.5" fill="%s"/>'
            % (px, py, lx, ey, MUTED, px, py, ACC2) + text(lx, ly, label, size, anchor, weight, fill))


# ================================================================= icone
def germ(x, y, r=7, col='#8e9aa6'):
    s = ''
    for k in range(6):
        a = k * math.pi / 3 + 0.3
        s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6"/>' % (
            x, y, x + math.cos(a) * r * 1.6, y + math.sin(a) * r * 1.6, col)
        s += '<circle cx="%.1f" cy="%.1f" r="1.8" fill="%s"/>' % (x + math.cos(a) * r * 1.6, y + math.sin(a) * r * 1.6, col)
    return s + '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#cfd6dd" stroke="%s" stroke-width="1.6"/>' % (x, y, r, col)


def bacterium(x, y, s=1.0, col='#7cb87c'):
    return ('<g transform="translate(%.1f,%.1f) scale(%.2f)"><rect x="-16" y="-7" width="32" height="14" rx="7" fill="%s" stroke="#4d8a4d" stroke-width="1.5"/>'
            '<path d="M16,0 q8,-6 14,2" fill="none" stroke="#4d8a4d" stroke-width="1.5"/></g>' % (x, y, s, col))


def virus(x, y, s=1.0, col='#e59a8f'):
    sp = ''.join('<line x1="0" y1="0" x2="%.1f" y2="%.1f" stroke="#b45f55" stroke-width="1.6"/><circle cx="%.1f" cy="%.1f" r="2.4" fill="#b45f55"/>'
                 % (math.cos(k * math.pi / 4) * 14, math.sin(k * math.pi / 4) * 14, math.cos(k * math.pi / 4) * 14, math.sin(k * math.pi / 4) * 14) for k in range(8))
    return '<g transform="translate(%.1f,%.1f) scale(%.2f)">%s<circle r="9" fill="%s" stroke="#b45f55" stroke-width="1.5"/></g>' % (x, y, s, sp, col)


def fungus(x, y, s=1.0, col='#c9a3d9'):
    return ('<g transform="translate(%.1f,%.1f) scale(%.2f)" fill="none" stroke="#8a62a0" stroke-width="2.2" stroke-linecap="round">'
            '<path d="M-14,10 Q-6,0 -2,-12"/><path d="M-6,4 Q2,2 8,-6"/><path d="M-2,-12 Q4,-16 10,-14"/><path d="M-10,6 Q-16,-2 -14,-10"/>'
            '<circle cx="10" cy="-14" r="3" fill="%s"/><circle cx="8" cy="-6" r="3" fill="%s"/><circle cx="-14" cy="-10" r="3" fill="%s"/></g>'
            % (x, y, s, col, col, col))


def spore(x, y, s=1.0):
    return ('<g transform="translate(%.1f,%.1f) scale(%.2f)"><ellipse rx="13" ry="9" fill="#e8d3a6" stroke="#8b6b2e" stroke-width="3"/>'
            '<ellipse rx="6" ry="4" fill="#b98f43"/></g>' % (x, y, s))


def bottle(cx, base, w=36, h=70, col='#dfe9f2', label='', lab_size=11.5, cap='#4b3a40', stroke='#7d8792', lab_col=INK):
    s = ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="8" fill="%s" stroke="%s" stroke-width="1.8"/>'
         % (cx - w / 2, base - h, w, h, col, stroke))
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="%s"/>' % (cx - w * 0.22, base - h - 16, w * 0.44, 18, cap)
    if label:
        s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#fff" opacity=".85"/>' % (cx - w / 2 + 3, base - h * 0.62, w - 6, h * 0.36)
        s += text(cx, base - h * 0.62 + h * 0.18 + lab_size * 0.38, label, lab_size, weight=800, fill=lab_col)
    return s


def jar(cx, base, w=50, h=34, col='#f6d6df', label='', lid=ACC2, lab_size=11.5):
    s = ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="7" fill="%s" stroke="%s" stroke-width="1.6"/>'
         % (cx - w / 2, base - h, w, h, col, NAIL_S))
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="12" rx="4" fill="%s"/>' % (cx - w / 2 - 3, base - h - 10, w + 6, lid)
    if label:
        s += text(cx, base - h / 2 + lab_size * 0.38, label, lab_size, weight=800, fill=INK)
    return s


def trash(cx, base, w=50, h=58, col='#cfd6dd', lid=True, stroke=GREY_D, pedal=False):
    s = ('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.8"/>'
         % (cx - w / 2, base - h, cx + w / 2, base - h, cx + w / 2 - 5, base, cx - w / 2 + 5, base, col, stroke))
    for k in (-1, 0, 1):
        s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.4" opacity=".6"/>' % (
            cx + k * w * 0.22, base - h + 10, cx + k * w * 0.2, base - 8, stroke)
    if lid:
        s += '<rect x="%.1f" y="%.1f" width="%.1f" height="9" rx="3" fill="%s" stroke="%s" stroke-width="1.6"/>' % (cx - w / 2 - 4, base - h - 9, w + 8, col, stroke)
        s += '<rect x="%.1f" y="%.1f" width="14" height="5" rx="2" fill="%s"/>' % (cx - 7, base - h - 14, stroke)
    if pedal:
        s += '<rect x="%.1f" y="%.1f" width="16" height="5" rx="2" fill="%s"/>' % (cx - 8, base - 2, stroke)
    return s


def magnifier(x, y, r=18, col=ACC2):
    return ('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#ffffff" fill-opacity=".35" stroke="%s" stroke-width="3.5"/>'
            '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="6" stroke-linecap="round"/>'
            % (x, y, r, col, x + r * 0.72, y + r * 0.72, x + r * 1.6, y + r * 1.6, col))


def stopwatch(x, y, r=20, col=ACC2):
    return ('<rect x="%.1f" y="%.1f" width="10" height="7" rx="2" fill="%s"/>' % (x - 5, y - r - 8, col)
            + '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#fff" stroke="%s" stroke-width="2.5"/>' % (x, y, r, col)
            + '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="2.5" fill="none" stroke-linecap="round"/>' % (
                x, y - r * 0.65, x, y, x + r * 0.45, y + r * 0.25, col))


def eye(x, y, s=1.0, col=ACC2):
    return ('<g transform="translate(%.1f,%.1f) scale(%.2f)"><path d="M-20,0 Q0,-16 20,0 Q0,16 -20,0 Z" fill="#fff" stroke="%s" stroke-width="2.4"/>'
            '<circle r="6.5" fill="%s"/><circle cx="-2" cy="-2" r="2" fill="#fff"/></g>' % (x, y, s, col, col))


def camera(x, y, s=1.0, col=ACC2):
    return ('<g transform="translate(%.1f,%.1f) scale(%.2f)"><rect x="-20" y="-12" width="40" height="27" rx="5" fill="%s"/>'
            '<rect x="-8" y="-17" width="14" height="7" rx="2" fill="%s"/><circle cy="2" r="8" fill="#fff"/><circle cy="2" r="4.5" fill="%s"/></g>'
            % (x, y, s, col, col, col))


def doc(x, y, w, h, lines=6, col='#ffffff', stroke=GREY_D, fold=True):
    s = ('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.8"/>'
         % (x, y, x + w - 14, y, x + w, y + 14, x + w, y + h, x, y + h, col, stroke))
    if fold:
        s += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f" fill="none" stroke="%s" stroke-width="1.5"/>' % (x + w - 14, y, x + w - 14, y + 14, x + w, y + 14, stroke)
    for k in range(lines):
        yy = y + 22 + k * (h - 30) / max(1, lines)
        s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#c8ced4" stroke-width="2.5" stroke-linecap="round"/>' % (x + 9, yy, x + w - 10 - (k % 3) * 6, yy)
    return s


def scissors(x, y, s=1.0, ang=0, col=GREY_D):
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f) scale(%.2f)" stroke="%s" stroke-width="2.4" fill="none">'
            '<line x1="-4" y1="-4" x2="26" y2="8"/><line x1="-4" y1="4" x2="26" y2="-8"/>'
            '<circle cx="-11" cy="-7" r="6.5" fill="#fff"/><circle cx="-11" cy="7" r="6.5" fill="#fff"/></g>' % (x, y, ang, s, col))


def drop_icon(x, y, s=1.0, col='#d24b4b'):
    return '<path d="M%.1f,%.1f q%.1f,%.1f 0,%.1f q%.1f,%.1f 0,%.1f z" fill="%s"/>' % (
        x, y - 14 * s, 11 * s, 15 * s, 25 * s, -11 * s, -10 * s, -25 * s, col)


def lightning(x, y, s=1.0, col=ERR):
    pts = [(2, -12), (-6, 1), (0, 1), (-3, 12), (7, -3), (1, -3), (5, -12)]
    return '<path d="M%s Z" fill="%s"/>' % (' L'.join('%.1f,%.1f' % (x + px * s, y + py * s) for px, py in pts), col)


def clock(x, y, r=16, col=ACC2):
    return ('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#fff" stroke="%s" stroke-width="2.4"/>'
            '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
            % (x, y, r, col, x, y - r * 0.6, x, y, x + r * 0.5, y + r * 0.2, col))


def calendar(x, y, w=40, h=36, col=ACC2):
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="5" fill="#fff" stroke="%s" stroke-width="2"/>' % (x, y, w, h, col)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="10" rx="4" fill="%s"/>' % (x, y, w, col)
    for r in range(2):
        for c in range(3):
            s += '<rect x="%.1f" y="%.1f" width="6" height="5" fill="%s" opacity=".55"/>' % (x + 7 + c * 11, y + 16 + r * 9, col)
    return s


# ================================================================= dito in miniatura (vista dall'alto) con segni
def mini(kind, cx, cy, s=1.0, shape='squoval', plate=None, free=None, free_len=14, extra_kw=None):
    """Dito con unghia, centrato in (cx, cy). kind = segno da disegnare sopra."""
    kind = kind or ''
    pl, fr, ex, post = plate or NAIL, free or FREE, '', ''
    if kind == 'micosi':
        pl, fr = '#e5cf8a', '#d8bf75'
        ex = ('<g clip-path="url(#CLIP)">'
              '<path d="M-34,-80 L-22,-86 L-14,-79 L-4,-88 L6,-80 L16,-87 L26,-79 L34,-84 L34,-100 L-34,-100 Z" fill="#ffffff"/>'
              + ''.join('<circle cx="%d" cy="%d" r="2.2" fill="#8a6a3a"/>' % (px, py) for px, py in ((-18, -76), (-6, -78), (10, -75), (22, -77), (2, -72)))
              + ''.join('<line x1="%d" y1="-70" x2="%d" y2="-20" stroke="#c9a85a" stroke-width="3" opacity=".7"/>' % (xx, xx + 2) for xx in (-16, 4, 18))
              + '</g>')
    elif kind == 'paronichia':
        post = ('<ellipse cx="38" cy="-36" rx="12" ry="30" fill="#e8705f" opacity=".9"/>'
                '<ellipse cx="38" cy="-36" rx="7" ry="20" fill="#f08f7f"/><circle cx="36" cy="-30" r="4.5" fill="#f2d24a" stroke="#c9a52a"/>')
    elif kind in ('banda', 'banda_chiara'):
        col = '#7a4a2a' if kind == 'banda' else '#b88a64'
        ex = '<rect x="-4" y="-110" width="7" height="125" fill="%s" opacity=".9" clip-path="url(#CLIP)"/>' % col
    elif kind == 'banda_larga':
        ex = ('<g clip-path="url(#CLIP)"><rect x="-6" y="-110" width="17" height="125" fill="#6b3f25"/>'
              '<rect x="-3" y="-110" width="4" height="125" fill="#2b1810"/><rect x="5" y="-110" width="3" height="125" fill="#3a2215"/>'
              '<rect x="-6" y="-60" width="17" height="14" fill="#9a6440" opacity=".7"/></g>')
    elif kind == 'hutchinson':
        ex = '<rect x="-5" y="-110" width="11" height="125" fill="#5a3320" clip-path="url(#CLIP)"/>'
        post = ('<path d="M-12,-4 Q-2,-14 12,-6 Q18,6 6,12 Q-8,14 -14,6 Z" fill="#5a3320" opacity=".85"/>'
                '<circle cx="0" cy="2" r="20" fill="none" stroke="%s" stroke-width="2.5" stroke-dasharray="5 3"/>' % ERR)
    elif kind == 'onicolisi':
        ex = ('<path d="M-36,-100 L36,-100 L36,-62 Q24,-48 12,-56 Q0,-44 -12,-54 Q-24,-46 -36,-58 Z" fill="#f4ecd4" clip-path="url(#CLIP)"/>'
              '<path d="M36,-62 Q24,-48 12,-56 Q0,-44 -12,-54 Q-24,-46 -36,-58" fill="none" stroke="#d9c79b" stroke-width="1.5" clip-path="url(#CLIP)"/>')
    elif kind == 'ematoma':
        ex = '<ellipse cx="0" cy="-16" rx="24" ry="30" fill="#7b2c4a" opacity=".9" clip-path="url(#CLIP)"/><ellipse cx="0" cy="-16" rx="30" ry="36" fill="#a23d5f" opacity=".35" clip-path="url(#CLIP)"/>'
    elif kind.startswith('ematoma@'):
        yy = float(kind.split('@')[1])
        ex = '<ellipse cx="2" cy="%.1f" rx="20" ry="13" fill="#5e2340" opacity=".9" clip-path="url(#CLIP)"/>' % yy
    elif kind == 'verde':
        ex = ('<g clip-path="url(#CLIP)"><rect x="-40" y="-110" width="80" height="112" fill="%s" opacity=".75"/>'
              '<ellipse cx="6" cy="-60" rx="20" ry="16" fill="#5f8f4f"/><ellipse cx="8" cy="-62" rx="12" ry="10" fill="#2b4a2e"/></g>' % PROD)
    elif kind == 'verruche':
        post = ''.join('<circle cx="%d" cy="%d" r="%d" fill="#dcbc98" stroke="#a7825c" stroke-width="1.4"/>' % (px, py, r)
                       for px, py, r in ((-40, -50, 8), (-36, -36, 9), (-44, -62, 6), (-32, -24, 6)))
        post += ''.join('<circle cx="%d" cy="%d" r="1.3" fill="#8a6a45"/>' % (px, py) for px, py in ((-42, -52), (-38, -48), (-35, -38), (-38, -34), (-44, -62), (-32, -25)))
    elif kind == 'granuloma':
        post = ('<ellipse cx="34" cy="-34" rx="14" ry="13" fill="#c62f45" stroke="#8f1f30" stroke-width="1.5"/>'
                '<ellipse cx="30" cy="-38" rx="4" ry="3" fill="#fff" opacity=".8"/>')
    elif kind == 'psoriasi':
        ex = ('<g clip-path="url(#CLIP)"><ellipse cx="8" cy="-50" rx="14" ry="11" fill="#f0a27a" opacity=".85"/>'
              + ''.join('<circle cx="%d" cy="%d" r="2" fill="#a9707f"/>' % (px, py) for px, py in ((-18, -30), (-10, -40), (-20, -55), (-6, -24), (14, -26), (20, -36), (-14, -66), (4, -70)))
              + '</g>')
    elif kind == 'beau':
        ex = ''.join('<path d="M-32,%d Q0,%d 32,%d" stroke="#c98097" stroke-width="3" fill="none" clip-path="url(#CLIP)"/>'
                     '<path d="M-32,%d Q0,%d 32,%d" stroke="#fff" stroke-width="1.5" fill="none" opacity=".9" clip-path="url(#CLIP)"/>'
                     % (yy, yy - 6, yy, yy + 3, yy - 3, yy + 3) for yy in (-36, -56))
    elif kind == 'leuconichia':
        ex = ''.join('<ellipse cx="%d" cy="%d" rx="5" ry="3.5" fill="#fff" stroke="#e7b9c6"/>' % (px, py) for px, py in ((-12, -40), (10, -52), (-4, -64), (16, -30), (-16, -58)))
    elif kind == 'striature':
        ex = ''.join('<line x1="%d" y1="-90" x2="%d" y2="0" stroke="#d986a0" stroke-width="1.8" clip-path="url(#CLIP)"/>' % (xx, xx) for xx in (-20, -10, 0, 10, 20))
        ex += '<path d="M8,-92 L4,-76" stroke="%s" stroke-width="2"/>' % ERR
    elif kind == 'sfogliato':
        ex = ('<g clip-path="url(#CLIP)"><path d="M-36,-76 L-24,-80 L-16,-73 L-4,-79 L8,-72 L20,-78 L36,-74 L36,-100 L-36,-100 Z" fill="#ffffff"/>'
              '<path d="M-34,-74 L-24,-77 L-16,-70 L-4,-76 L8,-69 L20,-75 L34,-71" stroke="#c98097" stroke-width="2" fill="none"/>'
              '<path d="M-34,-66 L-22,-69 L-12,-63 L0,-68 L12,-62 L24,-67 L34,-64" stroke="#c98097" stroke-width="1.8" fill="none"/>'
              '<path d="M-30,-58 L-16,-61 L-4,-56 L10,-60 L24,-56" stroke="#d9a3b3" stroke-width="1.5" fill="none"/></g>')
    elif kind == 'pellicine':
        post = '<path d="M-36,-30 L-50,-40 L-38,-22 Z" fill="#f6d9c6" stroke="#c48a6c" stroke-width="1.4"/>'
    pl_final = pl
    f, p = finger_nail(0, 0, hw=30, nail_len=78, free_len=free_len, shape=shape, smile=7, plate=pl_final, free=fr,
                       finger_len=28, extra=ex, lunula=False)
    return '<g transform="translate(%.1f,%.1f) scale(%.3f)">%s%s</g>' % (cx, cy + 34 * s, s, f, post)


def nail_side(x, y, w=170, kind='normale'):
    """Dito di profilo (punta a destra). y = quota della superficie su cui poggia la lamina."""
    H = w * 0.34
    o = ('<path d="M%.1f,%.1f L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
         % (x, y, x + w * 0.78, y, x + w * 0.97, y + 2, x + w * 0.97, y + H, x + w * 0.74, y + H, x, y + H, SKIN, SKIN_D))
    x0, x1 = x + w * 0.24, x + w * 0.8
    if kind == 'cucchiaio':
        o += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="%s" stroke-width="5" fill="none" stroke-linecap="round"/>' % (
            x0, y - 3, x + w * 0.62, y + 10, x + w * 0.98, y - 20, NAIL_S)
    elif kind == 'sottile':
        o += '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="%s" stroke-width="2" fill="none" stroke-linecap="round"/>' % (
            x0, y - 1, x1, y - 1, x + w * 0.92, y, x + w * 1.02, y + 14, NAIL_S)
    else:
        o += '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="%s" stroke-width="5" fill="none" stroke-linecap="round"/>' % (
            x0, y - 3, x1, y - 3, x + w * 0.94, y - 3, x + w * 1.02, y + 3, NAIL_S)
    # piega prossimale
    o += '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.3"/>' % (
        x, y - 9, x + w * 0.18, y - 9, x + w * 0.26, y - 8, x + w * 0.27, y - 1, x, y + 1, SKIN, SKIN_D)
    return o


def nail_front(cx, cy, r=34, curve=0.5, col=NAIL, thick=6):
    """Polpastrello visto dalla punta con l'arco dell'unghia (curve 0 = piatta, 1 = molto curva)."""
    s = '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s" stroke="%s" stroke-width="1.6"/>' % (cx, cy + 6, r, r * 0.86, SKIN, SKIN_D)
    hh = 6 + curve * r * 0.85
    s += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round"/>' % (
        cx - r * 0.82, cy - r * 0.18 + hh * 0.35, cx, cy - r * 0.18 - hh, cx + r * 0.82, cy - r * 0.18 + hh * 0.35, NAIL_S, thick)
    return s


# ================================================================= MODULO 1 – ANATOMIA
@figx('anatomia-strati-lamina.svg')
def strati_lamina():
    b = title('La lamina è fatta a strati')
    # --- sezione longitudinale (sinistra)
    b += frame(20, 56, 440, 344, None)
    b += text(240, 84, 'Sezione del dito (ingrandita)', 15, weight=700)
    b += '<rect x="34" y="168" width="412" height="166" fill="%s"/>' % SKIN          # tessuto del dito
    b += '<rect x="186" y="206" width="260" height="12" fill="#ee8ea7"/>'             # letto ungueale
    # matrice in tre segmenti
    for (x0, x1, c) in ((70, 110, L_TOP), (110, 150, L_MID), (150, 190, L_BOT)):
        b += '<path d="M%d,212 Q%d,224 %d,212 L%d,232 Q%d,244 %d,232 Z" fill="%s" stroke="#8d6fb8" stroke-width="1.2"/>' % (
            x0, (x0 + x1) / 2, x1, x1, (x0 + x1) / 2, x0, c)
    # lamina: tre bande
    b += '<path d="M66,170 Q80,166 96,166 L446,166 L446,176 L70,176 Z" fill="%s"/>' % L_TOP
    b += '<path d="M70,176 L446,176 L446,198 L70,198 Z" fill="%s"/>' % L_MID
    b += '<path d="M70,198 L446,198 L446,206 L70,206 Z" fill="%s"/>' % L_BOT
    b += '<path d="M96,166 L446,166 M70,206 L446,206" stroke="%s" stroke-width="1.6"/>' % NAIL_S
    # piega prossimale (copre la radice)
    b += ('<path d="M34,120 L150,120 Q188,122 194,160 L190,166 Q150,160 96,164 L34,164 Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
          % (SKIN, SKIN_D))
    b += '<rect x="34" y="150" width="36" height="24" fill="%s"/>' % SKIN
    # frecce matrice -> strati
    b += cpath('M90,214 Q120,180 214,171', '#6f53a6', 2)
    b += cpath('M130,214 Q160,192 226,187', '#8a74c0', 2)
    b += cpath('M170,214 Q190,206 238,202', '#c2577a', 2)
    b += leader(120, 140, 70, 104, 'Piega prossimale', 'start', 13.5)
    b += leader(110, 238, 92, 362, 'Matrice', 'middle', 13.5)
    b += leader(176, 236, 200, 304, 'Lunula', 'middle', 13.5)
    b += leader(330, 212, 340, 290, 'Letto ungueale', 'middle', 13.5)
    b += text(240, 386, 'Ogni parte della matrice produce uno strato', 13, fill=MUTED, style='italic')
    # --- blocchetto 3D (destra)
    bx, by, bw = 512, 108, 170
    hs = [(14, L_TOP), (44, L_MID), (14, L_BOT)]
    dx, dy = 36, -26
    yy = by
    for h, c in hs:
        b += '<rect x="%d" y="%d" width="%d" height="%d" fill="%s" stroke="#8d6fb8" stroke-width="1.2"/>' % (bx, yy, bw, h, c)
        b += '<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="%s" stroke="#8d6fb8" stroke-width="1.2" opacity=".9"/>' % (
            bx + bw, yy, bx + bw + dx, yy + dy, bx + bw + dx, yy + dy + h, bx + bw, yy + h, c)
        yy += h
    b += '<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="%s" stroke="#8d6fb8" stroke-width="1.2"/>' % (
        bx, by, bx + dx, by + dy, bx + bw + dx, by + dy, bx + bw, by, '#c9b6e6')
    for k in range(1, 6):     # fibre trasversali
        b += '<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#9c86c9" stroke-width="1.4" stroke-dasharray="10 5"/>' % (
            bx + 6, by + 14 + k * 7.3, bx + bw - 6, by + 14 + k * 7.3)
    b += leader(bx + 60, by + 36, 560, 66, 'Fibre da lato a lato', 'start', 13.5)
    # legenda strati
    items = [(L_TOP, 'Strato superiore', 'duro, resiste all\'acqua'), (L_MID, 'Strato centrale', 'il più spesso, flessibile'),
             (L_BOT, 'Strato inferiore', 'aderisce al letto')]
    for k, (c, t1, t2) in enumerate(items):
        y0 = 200 + k * 42
        b += '<rect x="486" y="%d" width="22" height="22" rx="4" fill="%s" stroke="#8d6fb8"/>' % (y0, c)
        b += text(518, y0 + 10, t1, 14, 'start', 700)
        b += text(518, y0 + 27, t2, 13, 'start', fill=MUTED)
    # riquadro lima
    b += '<rect x="474" y="332" width="272" height="70" rx="12" fill="%s"/>' % PANEL
    b += tool_file(504, 350, 0, 40, 12, '#cfc3b8', '#efe8e1')
    b += mark(538, 350, True, 10) + text(552, 355, 'Opacizza solo la superficie', 13, 'start', 600)
    b += tool_file(504, 384, 0, 40, 16, '#6f6259', '#9a8b80')
    b += mark(538, 384, False, 10) + text(552, 389, 'Non togliere lo strato superiore', 13, 'start', 600)
    return svg(760, 420, b, 'Gli strati della lamina ungueale e la matrice che li produce')


def mini_section(x, y, w, mlen, thick):
    """Sezione laterale semplificata. y = fondo della lamina; matrice (rossa) sotto la piega."""
    xe = x + 78                      # fine della piega prossimale
    xm = xe - mlen                   # inizio della matrice
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="74" fill="%s"/>' % (x, y - thick, w, SKIN)
    s += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
          % (xm, y, xm + 4, y - thick, xm + 14, y - thick, x + w, y - thick, x + w, y, xm, y, NAIL, NAIL_S))
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="10" rx="5" fill="%s"/>' % (xm, y + 2, mlen, ERR)
    s += ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.4"/>'
          % (x, y - thick - 30, xe - 22, y - thick - 30, xe + 2, y - thick - 28, xe + 4, y - thick, x, y - thick, SKIN, SKIN_D))
    return s


@figx('matrice-forma.svg')
def matrice_forma():
    b = title('La matrice decide spessore e forma della lamina')
    pw = 232
    for i, (t, ml, th, lab) in enumerate((('Matrice lunga', 64, 22, 'Lamina spessa'), ('Matrice corta', 26, 7, 'Lamina sottile'))):
        x = 20 + i * (pw + 12)
        b += frame(x, 56, pw, 244, t, i + 1)
        b += mini_section(x + 12, 176, pw - 24, ml, th)
        b += callout(x + 90 - ml / 2, 183, x + 70, 272, 'matrice', 13.5, 700, ERR)
        b += callout(x + 170, 176 - th / 2, x + 150, 112, lab, 15, 800, ACC2)
    x = 20 + 2 * (pw + 12)
    b += frame(x, 56, pw, 244, 'Vista dalla punta', 3)
    b += nail_front(x + 62, 160, 36, 0.05, thick=7)
    b += nail_front(x + 172, 160, 36, 1.0, thick=7)
    b += mtext(x + 62, 228, ['Matrice piatta', '→ unghia piatta'], 13, weight=600)
    b += mtext(x + 172, 228, ['Matrice curva', '→ curva a C', 'profonda'], 13, weight=600)
    b += '<rect x="20" y="314" width="720" height="50" rx="12" fill="#f1ecee"/>'
    b += calendar(40, 321, 38, 34)
    b += text(94, 345, 'Dalla matrice al bordo libero: circa 4–6 mesi', 16, 'start', 700)
    b += text(730, 345, 'non puoi cambiarle: le compensi', 13, 'end', fill=MUTED, style='italic')
    return svg(760, 380, b, 'Matrice lunga o corta, piatta o curva: spessore e forma della lamina')


@figx('anatomia-sigilli.svg')
def sigilli():
    b = title('I 4 sigilli proteggono letto e matrice')
    f, p = finger_nail(270, 330, hw=64, nail_len=180, free_len=26, shape='squoval', smile=10, finger_len=70)
    b += f
    cx, yc, ys, hw = p['cx'], p['y_c'], p['y_s'], p['hw']
    # cuticola (bianca) sulla piega
    b += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="#fff" stroke-width="5" opacity=".85"/>' % (
        cx - hw + 4, yc - 32, cx, yc + 8, cx + hw - 4, yc - 32)
    pts = {1: (cx, yc + 22), 2: (cx - hw - 18, (yc + ys) / 2 + 10), 3: (cx + hw + 18, (yc + ys) / 2 + 10)}
    # germi fermati
    for (gx, gy), (tx, ty) in (((cx + 70, yc + 82), pts[1]), ((70, 320), pts[2]), ((470, 320), pts[3])):
        b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.8" stroke-dasharray="5 4"/>' % (
            gx, gy, (gx + tx) / 2, (gy + ty) / 2, GREY_D)
        ang = math.atan2(ty - gy, tx - gx)
        mx, my = (gx + tx) / 2, (gy + ty) / 2
        b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="4" stroke-linecap="round"/>' % (
            mx - math.sin(ang) * 9, my + math.cos(ang) * 9, mx + math.sin(ang) * 9, my - math.cos(ang) * 9, OK)
        b += germ(gx, gy, 7)
    for n, (x, y) in pts.items():
        b += badge(x, y, n, OK, 14)
    b += text(cx + 22, yc + 27, 'Cuticola + piega prossimale', 14, 'start', 700)
    b += text(pts[2][0] - 20, pts[2][1] - 22, 'Piega laterale', 14, 'end', 700)
    b += text(pts[3][0] + 20, pts[3][1] - 22, 'Piega laterale', 14, 'start', 700)
    b += germ(560, 90, 7) + text(578, 95, 'germi e sostanze', 13, 'start', 600, MUTED)
    b += '<line x1="553" y1="122" x2="567" y2="122" stroke="%s" stroke-width="4" stroke-linecap="round"/>' % OK
    b += text(578, 127, 'fermati dai sigilli', 13, 'start', 600, MUTED)
    # forbice barrata
    b += scissors(92, 360, 1.0, -20) + no_sign(98, 358, 22)
    b += mark(40, 410, False, 11) + text(56, 415, 'Non tagliare la pelle viva', 14, 'start', 700, ERR)
    # inserto: sezione con iponichio
    ix, iy = 540, 236
    b += frame(ix, iy, 200, 190, 'Di lato: iponichio')
    b += nail_side(ix + 6, iy + 104, 176)
    hx = ix + 6 + 176 * 0.84
    b += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="#e4a48a" stroke="%s" stroke-width="1"/>' % (
        hx - 20, iy + 110, hx - 2, iy + 104, hx + 14, iy + 108, hx + 6, iy + 124, hx - 20, iy + 110, SKIN_D)
    b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.3"/>' % (hx, iy + 112, ix + 160, iy + 146, MUTED)
    b += badge(ix + 160, iy + 150, 4, OK, 14)
    b += germ(ix + 186, iy + 104, 6)
    b += text(ix + 100, iy + 184, 'sotto il bordo libero', 12.5, fill=MUTED)
    return svg(760, 440, arrow_defs() + b, 'I quattro sigilli dell\'unghia: cuticola con piega prossimale, due pieghe laterali e iponichio')


@figx('crescita-timeline.svg')
def crescita_timeline():
    b = title('L\'unghia cresce: la ricostruzione si sposta in avanti')
    labels = ['Giorno 0', '1 settimana', '2 settimane', '3 settimane', '4 settimane']
    for i, lab in enumerate(labels):
        cx = 66 + i * 112
        line_y = -12 - i * 9          # bordo del prodotto (coordinate locali)
        ex = ('<rect x="-40" y="-130" width="80" height="%.1f" fill="%s" opacity=".9" clip-path="url(#CLIP)"/>'
              '<line x1="-40" y1="%.1f" x2="40" y2="%.1f" stroke="%s" stroke-width="2.5" clip-path="url(#CLIP)"/>'
              % (130 + line_y, PROD, line_y, line_y, ERR))
        f, p = finger_nail(0, 0, hw=30, nail_len=88, free_len=26, shape='squoval', smile=7, finger_len=24, extra=ex, lunula=False)
        b += '<g transform="translate(%d,206)">%s</g>' % (cx, f)
        b += text(cx, 266, lab, 13.5, weight=700)
        if i:
            b += text(cx - 56, 70, '+0,8 mm', 12.5, weight=700, fill=ACC2)
            b += arrow(cx - 84, 80, cx - 30, 80, ACC2, 1.6)
        if i >= 2:
            b += leader(cx + 12, 206 + line_y + 9, cx + 26, 290, 'ricrescita', 'middle', 12.5, 600, ACC2)
    bx = 584
    b += '<rect x="%d" y="70" width="160" height="150" rx="14" fill="%s"/>' % (bx, PANEL)
    b += text(bx + 80, 98, 'In media', 14, weight=800, fill=ACC2)
    b += text(bx + 80, 128, 'Mani', 13.5, weight=700)
    b += text(bx + 80, 148, '≈ 3–3,5 mm/mese', 13.5)
    b += text(bx + 80, 178, 'Piedi', 13.5, weight=700)
    b += text(bx + 80, 198, '≈ 1,6 mm/mese', 13.5)
    b += '<rect x="%d" y="236" width="14" height="14" fill="%s" stroke="%s"/>' % (bx, PROD, PROD_S) + text(bx + 20, 248, 'prodotto', 12.5, 'start')
    b += '<line x1="%d" y1="268" x2="%d" y2="268" stroke="%s" stroke-width="2.5"/>' % (bx, bx + 14, ERR) + text(bx + 20, 273, 'bordo del prodotto', 12.5, 'start')
    return svg(760, 310, arrow_defs() + b, 'Crescita settimana per settimana: circa 0,8 mm a settimana')


@figx('crescita-refill-calcolo.svg')
def crescita_refill():
    b = title('Quando fare il refill')
    rows = [('Sett. 1', '~0,8 mm', '', OK_BG, OK), ('Sett. 2', '~1,6 mm', '', OK_BG, OK),
            ('Sett. 3', '~2,4 mm', 'refill ideale', WARN_BG, WARN), ('Sett. 4', '~3,2 mm', 'limite', WARN_BG, WARN),
            ('Sett. 5–6', '~4–5 mm', 'rischio rotture', ERR_BG, ERR)]
    for k, (w, mm, note, bg, fg) in enumerate(rows):
        y = 62 + k * 52
        b += '<rect x="20" y="%d" width="330" height="44" rx="10" fill="%s" stroke="%s" stroke-width="1.5"/>' % (y, bg, fg)
        b += text(36, y + 28, w, 15, 'start', 800, fg)
        b += text(130, y + 28, mm, 15, 'start', 700)
        if note:
            b += text(334, y + 28, note, 14, 'end', 700, fg)
        if k == 2:
            b += calendar(212, y + 7, 30, 30, WARN)
    # dito di profilo con ricrescita
    b += frame(370, 56, 370, 290, 'Misura la ricrescita')
    s, p = side_profile(440, 190, w=250, stress=0.62, apex=0.62, apex_h=30, tip_h=6, root_h=3, regrowth=34, product=PROD)
    b += s
    ax = p['ax']
    b += '<path d="M%.1f,%.1f l-8,-14 l16,0 z" fill="%s"/>' % (ax, p['ah'] - 6, ACC)
    b += text(ax + 8, p['ah'] - 26, 'Apex spostato in avanti', 13, 'middle', 700, ACC2)
    # righello
    rx0 = 440
    b += '<rect x="%d" y="226" width="80" height="18" fill="#fff6d6" stroke="#c9a54a"/>' % (rx0 - 10)
    for k in range(0, 9):
        b += '<line x1="%d" y1="226" x2="%d" y2="%d" stroke="#8b6b2e" stroke-width="1.2"/>' % (rx0 - 6 + k * 9, rx0 - 6 + k * 9, 236 if k % 2 else 240)
    b += '<path d="M%d,%d L%d,%d" stroke="%s" stroke-width="2"/>' % (440, 204, 440, 226, ACC2)
    b += '<path d="M%d,%d L%d,%d" stroke="%s" stroke-width="2"/>' % (474, 204, 474, 226, ACC2)
    b += text(457, 268, 'ricrescita', 13, weight=700, fill=ACC2)
    b += callout(560, 176, 640, 252, 'prodotto', 13, 600, MUTED)
    b += '<rect x="386" y="282" width="338" height="50" rx="10" fill="#fff"/>'
    b += text(555, 302, 'mm di ricrescita ÷ settimane', 14, weight=700)
    b += text(555, 322, '= velocità della tua cliente', 14, weight=700, fill=ACC2)
    return svg(760, 360, arrow_defs() + b, 'Settimane e millimetri di ricrescita: refill dopo 3–4 settimane')


@figx('semaforo-unghie.svg')
def semaforo():
    b = title('Il semaforo: lavorare o no?')
    b += '<rect x="34" y="62" width="92" height="340" rx="22" fill="#3b2a30"/>'
    b += '<rect x="72" y="402" width="16" height="38" fill="#3b2a30"/>'
    rows = [(ERR, ERR_BG, ['micosi', 'paronichia', 'banda'], ['Unghia ispessita', 'Dito rosso e gonfio', 'Banda scura'],
             'NON LAVORARE', 'consiglia il medico'),
            (AMBER, WARN_BG, ['onicolisi', 'ematoma', None], ['Unghia staccata', 'Ematoma recente', 'Diabete'],
             'CHIEDI, ADATTA', 'o aspetta il parere del medico'),
            (OK, OK_BG, ['beau', 'leuconichia', 'sfogliato'], ['Solchi trasversali', 'Macchioline bianche', 'Bordo sfogliato'],
             'PUOI LAVORARE', 'con delicatezza')]
    for k, (c, bg, kinds, labs, t1, t2) in enumerate(rows):
        y = 70 + k * 112
        b += '<circle cx="80" cy="%d" r="40" fill="%s"/>' % (y + 50, c)
        b += '<circle cx="67" cy="%d" r="10" fill="#fff" opacity=".35"/>' % (y + 37)
        b += '<rect x="146" y="%d" width="594" height="100" rx="14" fill="%s"/>' % (y, bg)
        for j, kd in enumerate(kinds):
            ix = 200 + j * 124
            if kd:
                b += mini(kd, ix, y + 40, 0.6)
            else:
                b += drop_icon(ix, y + 42, 1.3, '#d24b4b')
            b += text(ix, y + 90, labs[j], 12.5, weight=600, fill=INK)
        b += text(540, y + 46, t1, 17, 'start', 900, c if c != AMBER else WARN)
        b += para(540, y + 68, t2, 190, 13, weight=600)[0]
    b += text(740, 432, 'Nel dubbio = rosso', 16, 'end', 800, ERR)
    return svg(760, 450, b, 'Semaforo delle unghie: rosso non lavorare, giallo chiedi e adatta, verde lavora con delicatezza')


def tile(x, y, w, h, kind_draw, name, desc, col, sym='x', adapt=None):
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="14" fill="#fff" stroke="%s" stroke-width="2.2"/>' % (x, y, w, h, col)
    s += kind_draw
    yy = y + 30
    for ln in wrap(name, w - 128, 15, True):
        s += text(x + 104, yy, ln, 15, 'start', 800)
        yy += 18
    yy += 4
    for ln in wrap(desc, w - 116, 12.5):
        s += text(x + 104, yy, ln, 12.5, 'start', fill=MUTED)
        yy += 16
    if sym == 'x':
        s += mark(x + w - 18, y + 18, False, 11)
    elif sym == '!':
        s += excl(x + w - 18, y + 18, AMBER, 11)
    elif sym == '!r':
        s += excl(x + w - 18, y + 18, ERR, 11)
    elif sym == 'ok':
        s += mark(x + w - 18, y + 18, True, 11)
    if adapt:
        cw = tw(adapt, 12, True) + 18
        s += chip(min(x + 104 + (w - 116) / 2, x + w - 10 - cw / 2), y + h - 22, adapt, col if col == OK else WARN, '#fff', 12)
    return s


@figx('patologie-tavola.svg')
def patologie():
    b = title('Riconosci, non diagnosticare')
    b += text(780, 38, 'niente servizio: consiglia il medico', 13, 'end', 600, MUTED)
    data = [('micosi', 'Onicomicosi', 'Lamina gialla-grigia, spessa, bordo friabile', ERR, 'x'),
            ('tinea', 'Tinea', 'Pelle che si squama e prude, tra le dita', ERR, 'x'),
            ('paronichia', 'Paronichia', 'Piega rossa, gonfia, dolente, a volte pus', ERR, 'x'),
            ('verde', 'Unghia verde', 'Macchia verde-nera sotto un sollevamento', ERR, 'x'),
            ('verruche', 'Verruche', 'Escrescenze ruvide intorno all\'unghia', ERR, 'x'),
            ('granuloma', 'Granuloma', 'Massa rossa lucida che sanguina', ERR, 'x'),
            ('onicolisi', 'Onicolisi', 'Punta bianca staccata dal letto', AMBER, '!'),
            ('psoriasi', 'Psoriasi', 'Puntini "a ditale", macchia color salmone', AMBER, '!'),
            ('banda', 'Banda scura', 'Striscia marrone dalla base alla punta', ERR, '!r')]
    W, H = 246, 140
    for i, (k, n, d, c, sym) in enumerate(data):
        x = 20 + (i % 3) * (W + 11)
        y = 56 + (i // 3) * (H + 12)
        if k == 'tinea':
            dr = mini(None, x + 34, y + 70, 0.55) + mini(None, x + 76, y + 70, 0.55)
            dr += ''.join('<path d="M%.1f,%.1f q4,-5 8,0" stroke="#c0605a" stroke-width="1.6" fill="none"/>' % (x + 46 + (j % 2) * 6, y + 62 + j * 9) for j in range(6))
            dr += '<ellipse cx="%.1f" cy="%.1f" rx="10" ry="30" fill="#e8705f" opacity=".35"/>' % (x + 55, y + 86)
        else:
            dr = mini(k, x + 54, y + 70, 0.68)
        b += tile(x, y, W, H, dr, n, d, c, sym)
    return svg(800, 520, b, 'Tavola delle condizioni in cui non si lavora')


@figx('melanonichia-segnali.svg')
def melanonichia():
    b = title('Banda scura sull\'unghia: quando preoccuparsi')
    b += frame(20, 56, 300, 262, 'Spesso innocua', border=OK, fill='#f4faf6')
    b += mini('banda_chiara', 100, 156, 0.85) + mini('banda_chiara', 196, 156, 0.85)
    for k, t in enumerate(['Sottile e uniforme', 'Su più dita', 'Stabile nel tempo']):
        b += mark(48, 252 + k * 22, True, 8) + text(62, 257 + k * 22, t, 13.5, 'start', 600)
    b += frame(340, 56, 400, 262, 'Dal dermatologo subito', border=ERR, fill='#fdf3f2')
    b += mini('banda_larga', 440, 156, 0.85) + mini('hutchinson', 620, 156, 0.85)
    b += text(440, 224, 'larga, irregolare', 12.5, fill=MUTED)
    b += text(620, 224, 'pigmento sulla pelle', 12.5, fill=MUTED)
    for k, t in enumerate(['Una sola banda in un adulto', 'Larga ≥ 3 mm o irregolare', 'Nuova o si allarga',
                           'Pigmento sulla pelle (segno di Hutchinson)']):
        b += excl(366, 248 + k * 20, ERR, 9.5) + text(382, 253 + k * 20, t, 13, 'start', 600)
    b += '<rect x="20" y="330" width="720" height="40" rx="12" fill="#f1ecee"/>'
    b += camera(50, 349, 0.8)
    b += text(78, 355, 'Fotografa (con consenso) e annota.', 15, 'start', 700)
    b += text(352, 355, 'Non coprire con colore o gel.', 15, 'start', 800, ERR)
    return svg(760, 380, b, 'Melanonichia: bande spesso innocue e segnali da far vedere subito al dermatologo')


@figx('disturbi-tavola.svg')
def disturbi():
    b = title('Disturbi: si lavora con attenzione')
    data = [('beau', 'Linee di Beau', 'Solchi trasversali', OK, 'Grana fine'),
            ('leuconichia', 'Macchioline bianche', 'Piccoli traumi', OK, 'Nessun limite'),
            ('striature', 'Striature', 'Righe per il lungo', OK, 'Lima 240 + olio'),
            ('sfogliato', 'Sfogliamento', 'Bordo libero a strati', OK, 'Accorcia e sigilla'),
            ('sottile', 'Unghia sottile', 'Lamina che si piega', OK, 'Strati sottili, flash'),
            ('pellicine', 'Pellicine', 'Lembi di pelle secca', OK, 'Taglia solo il lembo'),
            ('ematoma@-50', 'Ematoma vecchio', 'Si sposta in avanti, non fa male', AMBER, 'Con delicatezza'),
            ('cucchiaio', 'A cucchiaio', 'Unghia concava (di profilo)', AMBER, 'Se è nuova: medico'),
            ('pinza', 'A pinza', 'Curva molto stretta (dalla punta)', AMBER, 'Niente pinching')]
    W, H = 246, 140
    for i, (k, n, d, c, adapt) in enumerate(data):
        x = 20 + (i % 3) * (W + 11)
        y = 56 + (i // 3) * (H + 12)
        if k == 'sottile':
            dr = nail_side(x + 8, y + 74, 88, 'sottile')
            dr += '<path d="M%.1f,%.1f l0,18" stroke="%s" stroke-width="2.4" marker-end="url(#ar)"/>' % (x + 88, y + 40, ACC2)
        elif k == 'cucchiaio':
            dr = nail_side(x + 6, y + 78, 88, 'cucchiaio')
        elif k == 'pinza':
            dr = nail_front(x + 52, y + 78, 34, 1.6, thick=6)
        else:
            dr = mini(k, x + 52, y + 70, 0.68)
        b += tile(x, y, W, H, dr, n, d, c, 'ok' if c == OK else '!', adapt)
    return svg(800, 520, arrow_defs() + b, 'Disturbi comuni non contagiosi e come adattare il lavoro')


@figx('ematoma-confronto.svg')
def ematoma():
    b = title('Ematoma: recente o vecchio?')
    b += frame(20, 56, 270, 236, 'Recente', 1, ok=False)
    b += mini('ematoma', 155, 168, 1.0)
    b += lightning(92, 130, 1.3) + lightning(220, 150, 1.3) + lightning(100, 200, 1.1)
    b += mtext(155, 262, ['Dolore, macchia alla base', '→ non lavorare'], 13.5, weight=700, fill=ERR)
    b += frame(304, 56, 436, 236, 'Vecchio', 2, ok=True)
    for j, (yy, lab) in enumerate(((-30, '0 sett.'), (-48, '2 sett.'), (-68, '4 sett.'))):
        cx = 380 + j * 140
        b += mini('ematoma@%d' % yy, cx, 156, 0.78)
        b += text(cx, 226, lab, 13, weight=700, fill=ACC2)
        if j:
            b += arrow(cx - 98, 150, cx - 44, 150, ACC2, 1.8)
    b += mtext(522, 256, ['Si sposta con la crescita, non fa male', '→ lavora con delicatezza'], 13.5, weight=700, fill=OK)
    b += '<rect x="20" y="304" width="720" height="30" rx="10" fill="#f1ecee"/>'
    b += text(380, 324, 'Macchia sempre attaccata alla base o che si allarga → dermatologo', 14, weight=700, fill=ERR)
    return svg(760, 340, arrow_defs() + b, 'Ematoma recente e dolente oppure vecchio che si sposta con la crescita')


HAND_FINGERS = [(-50, 112, 15, -5), (-16, 130, 16, -1), (18, 122, 15.5, 3), (50, 96, 13.5, 8)]   # (x base, lunghezza, raggio, inclinazione)


def finger_tips(cx, cy, s=1.0):
    """Punti utili delle dita: per ogni dito (punta, centro unghia, base unghia)."""
    out = []
    for fx, L, r, a in HAND_FINGERS:
        tx, ty = fx + a * 2.2, -46 - L
        ang = math.atan2(ty + 46, tx - fx)
        ux, uy = math.cos(ang), math.sin(ang)
        tip = (tx + ux * r * 0.2, ty + uy * r * 0.2)
        mid = (tx - ux * r * 0.9, ty - uy * r * 0.9)
        base = (tx - ux * r * 2.0, ty - uy * r * 2.0)
        out.append([(cx + s * px, cy + s * py) for px, py in (tip, mid, base)])
    return out


def hand_back(cx, cy, s=1.0):
    """Dorso della mano destra, dita verso l'alto. (cx, cy) = centro del palmo."""
    o = ''
    segs = [(fx, -46, fx + a * 2.2, -46 - L, r) for fx, L, r, a in HAND_FINGERS] + [(-62, 40, -122, -22, 17)]
    for x1, y1, x2, y2, r in segs:
        o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.1f" stroke-linecap="round"/>' % (x1, y1, x2, y2, SKIN_D, 2 * r + 3)
        o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.1f" stroke-linecap="round"/>' % (x1, y1, x2, y2, SKIN, 2 * r)
        ang = math.degrees(math.atan2(y2 - y1, x2 - x1)) + 90
        ux, uy = (x2 - x1), (y2 - y1)
        Ln = math.hypot(ux, uy)
        nx, ny = x2 - ux / Ln * r * 0.9, y2 - uy / Ln * r * 0.9
        o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s" stroke="%s" stroke-width="1.4" transform="rotate(%.1f %.1f %.1f)"/>' % (
            nx - r * 0.66, ny - r * 1.0, r * 1.32, r * 2.0, r * 0.6, NAIL, NAIL_S, ang, nx, ny)
        # piega alla base dell'unghia
        bx, by = x2 - ux / Ln * r * 2.05, y2 - uy / Ln * r * 2.05
        o += '<path d="M%.1f,%.1f q%.1f,%.1f %.1f,0" stroke="%s" stroke-width="1.3" fill="none" transform="rotate(%.1f %.1f %.1f)"/>' % (
            bx - r * 0.7, by - 2, r * 0.7, r * 0.5, r * 1.4, SKIN_D, ang - 180 if False else ang, bx, by)
    o += ('<path d="M-70,-62 Q-70,-74 -50,-74 L62,-74 Q80,-74 80,-56 L76,64 Q72,100 36,104 L-34,104 Q-66,100 -70,66 Z" fill="%s" stroke="%s" stroke-width="1.6"/>'
          % (SKIN, SKIN_D))
    o += '<path d="M-40,100 L-40,170 M40,100 L40,170" stroke="%s" stroke-width="1.6"/>' % SKIN_D
    o += '<rect x="-39" y="96" width="78" height="76" fill="%s"/>' % SKIN
    for k in range(4):
        o += '<path d="M%.1f,-66 q4,8 0,16" stroke="%s" stroke-width="1.2" fill="none" opacity=".6"/>' % (-50 + k * 33, SKIN_D)
    return '<g transform="translate(%.1f,%.1f) scale(%.2f)">%s</g>' % (cx, cy, s, o)


@figx('checkup-6-punti.svg')
def checkup():
    b = title('Il check-up in 6 punti')
    cx, cy, sc = 380, 268, 1.05
    b += hand_back(cx, cy, sc)
    ft = finger_tips(cx, cy, sc)
    pts = {1: (cx + 20, cy + 20), 2: ft[1][2], 3: ft[2][1], 4: ft[0][0], 5: ft[3][1], 6: (cx, cy + 150)}
    labs = {1: ('Pelle della mano', 540, 300), 2: ('Pieghe e cuticole', 220, 160), 3: ('Lamina', 540, 100),
            4: ('Letto e bordo libero', 220, 90), 5: ('Forma', 540, 180), 6: ('Abitudini e salute', 220, 400)}
    for n, (px, py) in pts.items():
        t, lx, ly = labs[n]
        right = lx > cx
        b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.4"/>' % (px, py, lx + (-14 if right else 14), ly, MUTED)
        b += '<circle cx="%.1f" cy="%.1f" r="4" fill="%s"/>' % (px, py, ACC2)
        b += badge(lx, ly, n, ACC, 14)
        b += text(lx + (20 if right else -20), ly + 5, t, 15, 'start' if right else 'end', 700)
    b += eye(625, 180, 0.7)
    b += ('<path d="M120,344 q0,-18 20,-18 l30,0 q20,0 20,18 q0,18 -20,18 l-14,0 l-12,10 l2,-10 q-26,0 -26,-18 z" fill="#fff" stroke="%s" stroke-width="2"/>' % ACC2)
    b += text(155, 350, '?', 16, weight=900, fill=ACC2)
    b += stopwatch(630, 46, 16) + text(654, 52, '2 minuti', 16, 'start', 800, ACC2)
    return svg(760, 440, b, 'Check-up in sei punti prima del servizio')


@figx('viste-dito.svg')
def viste_dito():
    b = title('Guarda ogni dito da tre lati')
    pw = 232
    # 1 dall'alto
    x = 20
    b += frame(x, 56, pw, 230, 'Dall\'alto', 1)
    b += eye(x + pw - 30, 82, 0.6)
    f, p = finger_nail(x + 84, 250, hw=34, nail_len=100, free_len=24, shape='squoval', smile=8, finger_len=30)
    b += f
    b += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="#c9a3ad" stroke-width="3" fill="none" clip-path="url(#%s)"/>' % (
        p['cx'] - 34, p['y_s'] + 8, p['cx'], p['y_s'] - 6, p['cx'] + 34, p['y_s'] + 8, p['clip'])
    b += leader(p['cx'] + 20, p['y_s'] + 2, x + 140, 112, 'Banda', 'start', 13)
    b += text(x + 146, 131, 'onicodermica', 13, 'start', 600)
    b += leader(p['cx'] + 38, p['y_c'] - 50, x + 140, 196, 'Piega laterale', 'start', 13)
    # 2 di profilo
    x = 20 + pw + 12
    b += frame(x, 56, pw, 230, 'Di profilo', 2)
    b += eye(x + pw - 30, 82, 0.6)
    b += nail_side(x + 20, 170, 190)
    b += '<circle cx="%.1f" cy="167" r="7" fill="%s"/>' % (x + 20 + 190 * 0.8, ERR)
    b += callout(x + 20 + 190 * 0.8, 167, x + 120, 262, 'Punto di stress', 14, 700, ERR)
    # 3 dalla punta
    x = 20 + 2 * (pw + 12)
    b += frame(x, 56, pw, 230, 'Dalla punta', 3)
    b += eye(x + pw - 30, 82, 0.6)
    b += nail_front(x + pw / 2, 170, 52, 0.55, thick=8)
    b += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="%s" stroke-width="3" fill="none" stroke-dasharray="6 4"/>' % (
        x + pw / 2 - 62, 160, x + pw / 2, 112, x + pw / 2 + 62, 160, ACC)
    b += text(x + pw / 2, 262, 'Curva a C', 14, weight=700, fill=ACC2)
    return svg(760, 300, b, 'Tre viste dello stesso dito: dall\'alto, di profilo, dalla punta')


# ================================================================= main
def main():
    only = [a for a in sys.argv[1:] if a.endswith('.svg')]
    n = 0
    for name, f in MINE.items():
        if only and name not in only:
            continue
        with open(os.path.join(OUT, name), 'w', encoding='utf-8') as fh:
            fh.write(f())
        n += 1
    print('Gruppo A: %d illustrazioni' % n)


if __name__ == '__main__':
    main()
