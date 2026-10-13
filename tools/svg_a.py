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


def hand_back(cx, cy, s=1.0, palm=False):
    """Dorso della mano destra, dita verso l'alto (palm=True: palmo, senza unghie). (cx, cy) = centro del palmo."""
    o = ''
    segs = [(fx, -46, fx + a * 2.2, -46 - L, r) for fx, L, r, a in HAND_FINGERS] + [(-62, 40, -122, -22, 17)]
    for x1, y1, x2, y2, r in segs:
        o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.1f" stroke-linecap="round"/>' % (x1, y1, x2, y2, SKIN_D, 2 * r + 3)
        o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.1f" stroke-linecap="round"/>' % (x1, y1, x2, y2, SKIN, 2 * r)
        ang = math.degrees(math.atan2(y2 - y1, x2 - x1)) + 90
        ux, uy = (x2 - x1), (y2 - y1)
        Ln = math.hypot(ux, uy)
        nx, ny = x2 - ux / Ln * r * 0.9, y2 - uy / Ln * r * 0.9
        if palm:
            continue
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
    if palm:
        o += '<path d="M-60,-30 Q-10,-44 70,-40 M-60,0 Q0,-14 60,-6 M-30,90 Q-50,40 -46,-10" stroke="%s" stroke-width="1.8" fill="none" opacity=".7"/>' % SKIN_D
    else:
        for k in range(4):
            o += '<path d="M%.1f,-66 q4,8 0,16" stroke="%s" stroke-width="1.2" fill="none" opacity=".6"/>' % (-50 + k * 33, SKIN_D)
    return '<g transform="translate(%.1f,%.1f) scale(%.2f,%.2f)">%s</g>' % (cx, cy, -s if palm else s, s, o)


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


# ================================================================= MODULO 2 – IGIENE
def nipper(x, y, s=1.0, ang=0):
    """Tronchesine viste dall'alto."""
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f) scale(%.2f)" stroke="%s" stroke-width="1.5" fill="%s">'
            '<path d="M-4,0 C-20,-10 -50,-14 -62,-10 L-62,-4 C-48,-6 -22,-2 -4,6 Z"/>'
            '<path d="M-4,0 C-20,10 -50,14 -62,10 L-62,4 C-48,6 -22,2 -4,-6 Z"/>'
            '<circle cx="0" cy="0" r="6"/><path d="M4,-4 L22,-3 L24,0 L22,3 L4,4 Z"/>'
            '<line x1="6" y1="0" x2="23" y2="0" stroke="%s" stroke-width="1.4"/></g>' % (x, y, ang, s, METAL_D, METAL, METAL_D))


def curette(x, y, s=1.0, ang=0):
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f) scale(%.2f)">'
            '<rect x="-50" y="-4" width="78" height="8" rx="4" fill="%s" stroke="%s"/>'
            '<path d="M28,-2 L40,-2" stroke="%s" stroke-width="3"/><ellipse cx="45" cy="0" rx="6" ry="4.5" fill="none" stroke="%s" stroke-width="2.4"/></g>'
            % (x, y, ang, s, METAL, METAL_D, METAL_D, METAL_D))


def bit(x, y, s=1.0, ang=0, head='#9aa3ad', shape='cil'):
    """Punta per fresa: gambo + testa (shape: cil, cono, fiamma, palla, ago, sic)."""
    hd = {'cil': '<rect x="0" y="-8" width="30" height="16" rx="2" fill="%s" stroke="%s"/>',
          'sic': '<path d="M0,-8 L24,-8 Q32,-8 32,0 Q32,8 24,8 L0,8 Z" fill="%s" stroke="%s"/>',
          'cono': '<path d="M0,-9 L30,-3 L30,3 L0,9 Z" fill="%s" stroke="%s"/>',
          'fiamma': '<path d="M0,-6 Q14,-10 22,-4 Q30,0 34,0 Q30,0 22,4 Q14,10 0,6 Z" fill="%s" stroke="%s"/>',
          'palla': '<circle cx="9" cy="0" r="9" fill="%s" stroke="%s"/>',
          'ago': '<path d="M0,-4 L30,-1 L34,0 L30,1 L0,4 Z" fill="%s" stroke="%s"/>'}[shape] % (head, METAL_D)
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f) scale(%.2f)"><rect x="-46" y="-3.5" width="48" height="7" rx="2" fill="%s" stroke="%s"/>%s</g>'
            % (x, y, ang, s, METAL, METAL_D, hd))


def glasses(cx, cy, s=1.0):
    return ('<g transform="translate(%.1f,%.1f) scale(%.2f)"><ellipse cx="-22" cy="0" rx="18" ry="13" fill="#e8f3fb" stroke="%s" stroke-width="3"/>'
            '<ellipse cx="22" cy="0" rx="18" ry="13" fill="#e8f3fb" stroke="%s" stroke-width="3"/><path d="M-5,-2 q5,-5 10,0" stroke="%s" stroke-width="3" fill="none"/></g>'
            % (cx, cy, s, INK, INK, INK))


def bowl(cx, cy, w=60):
    return ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="#e6f1f8" stroke="%s" stroke-width="2"/>'
            % (cx - w / 2, cy, cx, cy + w * 0.7, cx + w / 2, cy, PROD_S))


def pouch(x, y, w=150, h=90, tools=True, ind_col='#8a5a2b', s_rot=0):
    """Busta di sterilizzazione: metà carta, metà plastica trasparente."""
    o = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="4" fill="#fbfbf8" stroke="%s" stroke-width="1.8"/>' % (x, y, w, h, GREY_D)
    o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#dff0f7" opacity=".75"/>' % (x + 4, y + 4, w * 0.55, h - 8)
    o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="none" stroke="#7fb0cc" stroke-width="1.2" stroke-dasharray="3 2"/>' % (x + 4, y + 4, w - 8, h - 8)
    if tools:
        o += nipper(x + w * 0.42, y + h * 0.36, 0.8 * w / 150, 0) + tool_pusher(x + w * 0.16, y + h * 0.7, 0, int(w * 0.5))
    return o


def autoclave(x, y, w=170, h=120):
    o = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="12" fill="#eef1f4" stroke="%s" stroke-width="2"/>' % (x, y, w, h, GREY_D)
    o += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#dfe4e9" stroke="%s" stroke-width="3"/>' % (x + w * 0.36, y + h * 0.52, h * 0.32, GREY_D)
    o += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#c9d0d6"/>' % (x + w * 0.36, y + h * 0.52, h * 0.2)
    o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="#2f3e46"/>' % (x + w * 0.7, y + h * 0.22, w * 0.22, h * 0.16)
    o += text(x + w * 0.81, y + h * 0.22 + h * 0.13, '134°', 12, weight=700, fill='#8fe3b0') if w >= 140 else ''
    for k in range(3):
        o += '<circle cx="%.1f" cy="%.1f" r="4" fill="%s"/>' % (x + w * 0.73 + k * w * 0.08, y + h * 0.58, [OK, AMBER, GREY_D][k])
    return o


def autoclave_icon(cx, cy, s=1.0):
    return '<g transform="translate(%.1f,%.1f) scale(%.2f)">%s</g>' % (cx - 34 * s, cy - 24 * s, s, autoclave(0, 0, 68, 48))


def biohazard(cx, cy, r=10, col=INK):
    o = ''
    for k in range(3):
        a = -math.pi / 2 + k * 2 * math.pi / 3
        o += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" stroke-width="%.1f"/>' % (
            cx + math.cos(a) * r * 0.55, cy + math.sin(a) * r * 0.55, r * 0.62, col, r * 0.2)
    return o + '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" stroke-width="%.1f"/>' % (cx, cy, r * 0.32, col, r * 0.16)


@figx('livelli-disinfezione.svg')
def livelli_disinf():
    b = title('Livelli: dalla pulizia alla sterilizzazione')
    levels = [('Detersione', '#f6eef0', INK), ('Disinfezione bassa', '#f8dfe7', INK), ('Disinfezione intermedia', '#f1bfcf', INK),
              ('Disinfezione alta', '#e48fa9', '#fff'), ('Sterilizzazione', ACC, '#fff')]
    killed = [(), (0,), (0, 1, 2), (0, 1, 2), (0, 1, 2, 3)]
    icons = [bacterium, virus, fungus, spore]
    names = ['batteri', 'virus', 'funghi', 'spore']
    for j, nm in enumerate(names):
        x = 34 + j * 48
        b += text(x, 76, nm, 12, weight=700, fill=MUTED)
    for i, (lab, col, fc) in enumerate(levels):
        y = 344 - i * 62
        wbot = 400 - i * 50
        wtop = wbot - 50
        cx = 404
        b += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s"/>' % (
            cx - wbot / 2, y + 56, cx + wbot / 2, y + 56, cx + wtop / 2, y, cx - wtop / 2, y, col)
        b += text(cx, y + 34, lab, 15 if i < 4 else 16, weight=800, fill=fc)
        for j, ic in enumerate(icons):
            x = 34 + j * 48
            yy = y + 28
            g = ic(x, yy, 0.8)
            if j in killed[i]:
                b += '<g opacity=".45">%s</g>' % g
                b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="3" stroke-linecap="round"/>' % (x - 13, yy + 13, x + 13, yy - 13, ERR)
            else:
                b += g
        # icone a destra
        rx = 632
        if i == 0:
            b += '<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="#dfe9f2" stroke="%s" stroke-width="1.8"/>' % (rx - 18, y + 16, rx + 18, y + 16, rx + 13, y + 48, rx - 13, y + 48, PROD_S)
            b += '<rect x="%d" y="%d" width="6" height="26" fill="#c9a06a" transform="rotate(25 %d %d)"/>' % (rx + 4, y + 2, rx + 7, y + 15)
            b += mtext(rx + 26, y + 28, ['acqua e', 'detergente'], 12.5, 'start', 600)
        elif i < 4:
            b += bottle(rx, y + 50, 22, 30, ['#f8dfe7', '#dfe9f2', '#e8e0f5'][i - 1])
            b += text(rx + 22, y + 37, ['QAC', 'Alcol 70–90%', 'Alto livello'][i - 1], 12.5, 'start', 600)
        else:
            b += autoclave_icon(rx, y + 30, 0.62)
            b += text(rx + 30, y + 37, 'Autoclave', 12.5, 'start', 700)
    b += '<rect x="200" y="406" width="408" height="28" rx="10" fill="#f1ecee"/>'
    b += text(404, 425, 'Prima si pulisce, poi si disinfetta', 14, weight=700, fill=ACC2)
    b += text(30, 425, 'barrato = eliminato', 12, 'start', 600, MUTED)
    return svg(760, 440, arrow_defs() + b, 'Livelli di disinfezione e sterilizzazione e microrganismi eliminati')


@figx('classificazione-strumenti.svg')
def classif_strumenti():
    b = title('Dove va ogni strumento dopo la cliente')
    cols = [('MONOUSO', '→ nel cestino', '#8a8f96', '#f3f4f5'), ('DISINFETTARE', 'pulisci + disinfettante', '#3f86b8', '#eaf3f9'),
            ('STERILIZZARE', 'busta + autoclave', OK, '#e9f5ee')]
    items = [['Lima in carta / spugna', 'Buffer', 'Bastoncino d\'arancio', 'Banda abrasiva', 'Cartina, tip', 'Guanti, cotone'],
             ['Lima in vetro o metallo', 'Ciotola per manicure', 'Poggiamano lavabile', 'Occhiali', 'Lampada'],
             ['Tronchesine, forbicine', 'Spingicuticole', 'Curetta', 'Punte per fresa in metallo', 'Pinzette (se toccano pelle lesa)']]
    W = 248
    for k, (t, sub, c, bg) in enumerate(cols):
        x = 20 + k * (W + 8)
        b += '<rect x="%d" y="56" width="%d" height="300" rx="14" fill="%s"/>' % (x, W, bg)
        b += '<path d="M%d,70 Q%d,56 %d,56 L%d,56 Q%d,56 %d,70 L%d,100 L%d,100 Z" fill="%s"/>' % (x, x, x + 14, x + W - 14, x + W, x + W, x + W, x, c)
        b += text(x + W / 2, 84, t, 16, weight=900, fill='#fff')
        b += text(x + W / 2, 122, sub, 13, weight=700, fill=c)
        # icone
        iy = 160
        if k == 0:
            b += tool_file(x + 60, iy, -20, 80, 16, '#b9aa9c', '#e6dbd0')
            b += '<rect x="%d" y="%d" width="40" height="22" rx="4" fill="#f1e3c8" stroke="#c9b08a" transform="rotate(10 %d %d)"/>' % (x + 110, iy - 14, x + 130, iy)
            b += tool_stick(x + 168, iy + 8, -25, 56)
            b += trash(x + 220, iy + 22, 30, 36)
        elif k == 1:
            b += tool_file(x + 58, iy, -20, 80, 14, '#9cc7e0', '#d8edf8')
            b += bowl(x + 130, iy - 8, 54)
            b += glasses(x + 200, iy, 0.75)
        else:
            b += nipper(x + 80, iy, 0.9, -15) + curette(x + 150, iy + 4, 0.7, -30)
            b += autoclave_icon(x + 214, iy, 0.5)
        for j, it in enumerate(items[k]):
            yy = 210 + j * 24
            b += '<circle cx="%d" cy="%d" r="4" fill="%s"/>' % (x + 20, yy - 4, c)
            b += text(x + 32, yy, it, 13, 'start', 600)
    b += '<rect x="20" y="366" width="760" height="46" rx="12" fill="#fbe9e7"/>'
    b += tool_file(66, 389, 0, 56, 14, '#b9aa9c', '#e6dbd0') + magnifier(72, 384, 13)
    b += text(110, 395, 'Poroso = monouso:', 16, 'start', 900, ERR)
    b += text(270, 395, 'lime in carta e buffer non si disinfettano davvero, anche se "lavabili".', 14, 'start', 600)
    return svg(800, 420, b, 'Classificazione degli strumenti: monouso, da disinfettare, da sterilizzare')


@figx('autoclave-busta.svg')
def autoclave_busta():
    b = title('Busta sterile e autoclave: cosa controllare')
    px, py, pw, ph = 24, 70, 300, 170
    b += pouch(px, py, pw, ph, False)
    b += nipper(px + 150, py + 60, 1.3, 0) + tool_pusher(px + 50, py + 116, 0, 150)
    b += '<rect x="%d" y="%d" width="%d" height="24" fill="#f4f0e6" stroke="%s"/>' % (px, py + ph - 24, pw, GREY_D)
    b += text(px + 12, py + ph - 7, 'Data: 13/10 – Ciclo n. 128', 13.5, 'start', 700, '#2b4a8a')
    b += '<rect x="%d" y="%d" width="54" height="12" rx="2" fill="#8a5a2b"/>' % (px + pw - 70, py + 14)
    # etichette (colonna centrale)
    lx = 352
    b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.3"/><circle cx="%d" cy="%d" r="3.5" fill="%s"/>' % (px + pw - 16, py + 20, lx - 6, 92, MUTED, px + pw - 16, py + 20, ACC2)
    b += text(lx, 97, 'Indicatore virato', 14, 'start', 700)
    b += '<rect x="%d" y="106" width="30" height="10" rx="2" fill="#f2b3c3"/>' % lx + text(lx + 36, 116, '→', 13, 'start', 700)
    b += '<rect x="%d" y="106" width="30" height="10" rx="2" fill="#8a5a2b"/>' % (lx + 56)
    b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.3"/><circle cx="%d" cy="%d" r="3.5" fill="%s"/>' % (px + 250, py + ph - 12, lx - 6, 210, MUTED, px + 250, py + ph - 12, ACC2)
    b += mtext(lx, 206, ['Data e n. ciclo', 'sul bordo'], 14, 'start', 700)
    b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.3"/><circle cx="%d" cy="%d" r="3.5" fill="%s"/>' % (px + pw, py + 70, lx - 6, 152, MUTED, px + pw, py + 70, ACC2)
    b += mtext(lx, 150, ['Busta sigillata,', 'senza fori'], 14, 'start', 700)
    b += mark(40, 276, True, 12) + text(60, 281, 'Asciutta', 15, 'start', 800, OK)
    b += mark(170, 276, False, 12) + text(190, 281, 'Umida = ripeti il ciclo', 15, 'start', 800, ERR)
    b += text(24, 320, 'Strumenti puliti e asciutti prima di imbustare;', 13, 'start', 600, MUTED)
    b += text(24, 340, 'buste conservate chiuse, fino alla scadenza.', 13, 'start', 600, MUTED)
    # autoclave con stampante
    ax, ay = 560, 104
    b += text(ax + 90, ay - 14, 'Classe B – UNI EN 13060', 14, weight=800, fill=ACC2)
    b += autoclave(ax, ay, 180, 124)
    b += '<rect x="%d" y="%d" width="50" height="7" fill="%s"/>' % (ax + 118, ay + 102, INK)
    b += '<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="#fff" stroke="%s"/>' % (ax + 122, ay + 106, ax + 164, ay + 106, ax + 164, ay + 166, ax + 122, ay + 166, GREY_D)
    for k in range(5):
        b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#aab2ba" stroke-width="2"/>' % (ax + 127, ay + 132 + k * 7, ax + 159 - (k % 2) * 8, ay + 132 + k * 7)
    b += '<rect x="%d" y="%d" width="196" height="84" rx="12" fill="%s"/>' % (ax - 8, ay + 180, PANEL)
    b += text(ax + 4, ay + 204, 'Registro di ogni ciclo:', 14, 'start', 800)
    b += text(ax + 4, ay + 226, 'n. ciclo, data, T, P,', 14, 'start', 600)
    b += text(ax + 4, ay + 246, 'tempo, test, firma', 14, 'start', 600)
    return svg(760, 380, b, 'Busta di sterilizzazione pronta e autoclave di classe B con registro')


@figx('protezione-piramide.svg')
def protezione():
    b = title('L\'ordine della protezione')
    lv = [('Prodotti conformi e poche scorte', 'etichetta in italiano, flaconi chiusi'), ('Aspirazione alla fonte', 'tavolo aspirante o cappa vicino alle mani'),
          ('Ventilazione e ordine', 'aria pulita, rifiuti con coperchio'), ('DPI', 'guanti, occhiali, mascherina')]
    cols = [ACC2, ACC, '#e48fa9', '#f3c4d3']
    for i, (t, sub) in enumerate(lv):
        y = 64 + i * 86
        wt = 560 - i * 100
        wb = wt - 100
        cx = 372
        b += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s"/>' % (cx - wt / 2, y, cx + wt / 2, y, cx + wb / 2, y + 78, cx - wb / 2, y + 78, cols[i])
        fc = '#fff' if i < 3 else INK
        bx = cx - (wt - 100 * 30 / 78) / 2 + 28
        b += '<circle cx="%.1f" cy="%d" r="14" fill="%s"/>' % (bx, y + 30, '#fff' if i < 3 else ACC2)
        b += text(bx, y + 35, str(i + 1), 15, weight=900, fill=cols[i] if i < 3 else '#fff')
        b += text(cx + 14, y + 34, t, 17 if i < 3 else 18, weight=800, fill=fc)
        b += text(cx + 14, y + 56, sub, 13, weight=600, fill=fc)
    # icone ai lati
    b += bottle(56, 136, 30, 54, '#dfe9f2', '') + mark(76, 92, True, 10)
    b += '<rect x="30" y="196" width="72" height="34" rx="6" fill="#d8dde3" stroke="%s" stroke-width="2"/>' % GREY
    b += ''.join('<line x1="%d" y1="200" x2="%d" y2="226" stroke="%s" stroke-width="2"/>' % (38 + j * 8, 38 + j * 8, GREY) for j in range(8))
    b += ''.join('<path d="M%d,186 q4,6 0,12" stroke="%s" stroke-width="1.6" fill="none" marker-end="url(#ar)"/>' % (46 + j * 20, ACC2) for j in range(3))
    b += '<rect x="34" y="262" width="56" height="50" fill="#e6f1f8" stroke="%s" stroke-width="2.5"/><line x1="62" y1="262" x2="62" y2="312" stroke="%s" stroke-width="2"/><line x1="34" y1="287" x2="90" y2="287" stroke="%s" stroke-width="2"/>' % (GREY_D, GREY_D, GREY_D)
    b += glasses(66, 346, 0.8)
    b += '<path d="M44,366 Q66,356 88,366 L84,380 Q66,386 48,380 Z" fill="#f3f3f3" stroke="%s" stroke-width="1.5"/>' % GREY
    # freccia di efficacia
    b += '<defs><linearGradient id="eff" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="#f3c4d3"/></linearGradient></defs>' % OK
    b += '<rect x="690" y="70" width="14" height="306" rx="7" fill="url(#eff)"/>'
    b += text(697, 56, 'Più efficace', 13, weight=800, fill=OK)
    b += text(697, 400, 'Ultima barriera', 13, weight=800, fill=ACC2)
    return svg(760, 420, arrow_defs() + b, 'Gerarchia della protezione: prodotti, aspirazione, ventilazione, DPI')


def client_hand_side(x, y, s=1.0, col=SKIN, stroke=SKIN_D):
    """Mano della cliente vista di lato, appoggiata, dita verso destra (y = piano d'appoggio)."""
    return ('<g transform="translate(%.1f,%.1f) scale(%.2f)"><path d="M-70,0 L-70,-30 Q-50,-40 -16,-36 L38,-24 Q64,-21 68,-12 Q70,-3 56,-2 L-70,0 Z" fill="%s" stroke="%s" stroke-width="1.6"/>'
            '<path d="M44,-21 L64,-15" stroke="%s" stroke-width="4" stroke-linecap="round"/><path d="M-6,-34 Q2,-24 -4,-14" stroke="%s" stroke-width="1.3" fill="none"/></g>' % (x, y, s, col, stroke, NAIL_S, stroke))


def operator(x, y, s=1.0, bent=False, mask=True, specs=True):
    """Busto dell'operatrice di profilo, rivolta a destra. (x, y) = base del busto."""
    hx, hy = (30, -128) if bent else (0, -140)
    o = '<g transform="translate(%.1f,%.1f) scale(%.2f)">' % (x, y, s)
    o += '<path d="M-40,0 L-36,-86 Q-30,-112 %.1f,-116 Q%.1f,-112 %.1f,-80 L38,0 Z" fill="#cfe0ec" stroke="%s" stroke-width="1.6"/>' % (
        hx - 4, hx + 28, hx + 30 if bent else 34, GREY_D)
    o += '<circle cx="%.1f" cy="%.1f" r="26" fill="%s" stroke="%s" stroke-width="1.6"/>' % (hx, hy, SKIN, SKIN_D)
    o += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="#5a3a2e"/>' % (hx - 26, hy - 2, hx - 22, hy - 32, hx + 4, hy - 28, hx + 20, hy - 26, hx + 24, hy - 12)
    if specs:
        o += '<rect x="%.1f" y="%.1f" width="16" height="10" rx="4" fill="#e8f3fb" stroke="%s" stroke-width="2"/>' % (hx + 12, hy - 8, INK)
    if mask:
        o += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="#f3f3f3" stroke="%s" stroke-width="1.4"/>' % (
            hx + 6, hy + 2, hx + 34, hy + 4, hx + 28, hy + 16, hx + 22, hy + 22, hx + 10, hy + 24, hx + 2, hy + 16, GREY)
    return o + '</g>'


def dust(x, y, n=6, spread=20, col='#a9b2ba', seed=1):
    import random as _r
    rnd = _r.Random(seed)
    return ''.join('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>' % (x + rnd.uniform(-spread, spread), y + rnd.uniform(-spread / 2, spread / 2), rnd.uniform(1.5, 3), col) for _ in range(n))


@figx('aspirazione-tavolo.svg')
def aspirazione():
    b = title('Aspirazione: le mani sopra la bocchetta')
    for k in range(2):
        x0 = 20 + k * 366
        b += frame(x0, 56, 354, 300, 'Corretto' if k == 0 else 'Errato', ok=(k == 0))
        ty = 260
        b += '<rect x="%d" y="%d" width="300" height="14" rx="3" fill="#d9c7b8" stroke="#b39a86"/>' % (x0 + 30, ty)
        b += '<rect x="%d" y="%d" width="10" height="70" fill="#b39a86"/>' % (x0 + 300, ty + 14)
        if k == 0:
            gx = x0 + 200
            b += '<rect x="%d" y="%d" width="96" height="10" fill="#9aa3ad"/>' % (gx - 48, ty - 1)
            b += ''.join('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#6f7983" stroke-width="2"/>' % (gx - 44 + j * 10, ty - 1, gx - 44 + j * 10, ty + 9) for j in range(10))
            b += '<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="#c5ccd3" stroke="%s"/>' % (gx - 40, ty + 14, gx + 40, ty + 14, gx + 20, ty + 40, gx - 20, ty + 40, GREY_D)
            b += '<path d="M%d,%d L%d,%d L%d,%d" fill="none" stroke="%s" stroke-width="12" stroke-linejoin="round"/>' % (gx, ty + 40, gx, ty + 60, x0 + 60, ty + 60, GREY)
            b += client_hand_side(gx + 10, ty - 8, 0.95)
            b += operator(x0 + 70, ty, 0.8)
            for j in range(3):
                b += carrow(gx + 30 - j * 26, ty - 40, gx + 24 - j * 22, ty - 6, '#3f86b8', 2)
            b += dust(gx, ty - 44, 8, 30, seed=3)
            b += carrow(gx - 20, ty + 60, x0 + 64, ty + 60, '#3f86b8', 2.2)
            b += mtext(x0 + 232, 304, ['aria all\'esterno', 'o filtrata'], 13, 'start', 700, '#3f86b8')
        else:
            b += '<rect x="%d" y="%d" width="56" height="34" rx="6" fill="#d8dde3" stroke="%s" stroke-width="2"/>' % (x0 + 262, ty - 34, GREY)
            b += text(x0 + 290, ty - 42, 'lontano', 12.5, weight=700, fill=MUTED)
            b += client_hand_side(x0 + 170, ty - 8, 0.95)
            b += operator(x0 + 70, ty, 0.8, bent=True, mask=False)
            for j in range(3):
                b += carrow(x0 + 190 - j * 16, ty - 40, x0 + 120 - j * 4, 140 + j * 12, GREY_D, 2)
            b += dust(x0 + 170, ty - 44, 10, 30, seed=5)
            b += '<path d="M%d,%d q6,-6 12,-4 M%d,%d q8,-4 14,0" stroke="%s" stroke-width="2" fill="none"/>' % (x0 + 112, 150, x0 + 114, 158, GREY_D)
            b += '<path d="M%d,%d q10,-12 22,-4 q12,-8 20,4 q10,8 -2,14 q-10,10 -22,2 q-14,6 -18,-16 z" fill="#eef1f4" stroke="%s"/>' % (x0 + 132, 128, GREY)
            b += mark(x0 + 200, 100, False, 11) + text(x0 + 216, 105, 'Non soffiare', 14, 'start', 800, ERR)
            b += text(x0 + 177, 338, 'la polvere sale verso il viso', 13, weight=700, fill=ERR)
    b += '<rect x="20" y="366" width="720" height="28" rx="10" fill="#f1ecee"/>'
    b += text(380, 385, 'Mani il più vicino possibile alla bocchetta; poi occhiali e mascherina', 14, weight=700)
    return svg(760, 400, arrow_defs() + b, 'Aspirazione corretta ed errata al tavolo di lavoro')


def mask_surgical(cx, cy, s=1.0):
    o = '<g transform="translate(%.1f,%.1f) scale(%.2f)">' % (cx, cy, s)
    o += '<rect x="-46" y="-26" width="92" height="52" rx="8" fill="#cfe7f2" stroke="#7fb0cc" stroke-width="2"/>'
    o += ''.join('<line x1="-44" y1="%d" x2="44" y2="%d" stroke="#9cc7dc" stroke-width="2"/>' % (y, y) for y in (-12, 0, 12))
    o += '<path d="M-46,-18 Q-70,-16 -66,0 Q-64,16 -46,18 M46,-18 Q70,-16 66,0 Q64,16 46,18" fill="none" stroke="#7fb0cc" stroke-width="2"/>'
    return o + '</g>'


def mask_ffp2(cx, cy, s=1.0):
    o = '<g transform="translate(%.1f,%.1f) scale(%.2f)">' % (cx, cy, s)
    o += '<path d="M-50,-4 Q-46,-38 0,-40 Q46,-38 50,-4 Q42,34 0,40 Q-42,34 -50,-4 Z" fill="#f4f4f4" stroke="#9aa3ad" stroke-width="2"/>'
    o += '<path d="M-44,-8 Q0,6 44,-8" fill="none" stroke="#c8ced4" stroke-width="2"/><path d="M-20,-34 Q0,-40 20,-34" stroke="%s" stroke-width="3" fill="none"/>' % GREY_D
    o += '<path d="M-50,-4 L-70,-20 M50,-4 L70,-20 M-46,14 L-68,24 M46,14 L68,24" stroke="#d6a63a" stroke-width="2"/>'
    o += text(0, 24, 'FFP2', 12, weight=800, fill=GREY_D)
    return o + '</g>'


def mask_half(cx, cy, s=1.0):
    o = '<g transform="translate(%.1f,%.1f) scale(%.2f)">' % (cx, cy, s)
    o += '<path d="M-30,-30 Q0,-46 30,-30 L36,16 Q0,44 -36,16 Z" fill="#6b7480" stroke="#3e454d" stroke-width="2"/>'
    for sx in (-1, 1):
        o += '<circle cx="%d" cy="12" r="20" fill="#5a6d3a" stroke="#3e454d" stroke-width="2"/>' % (sx * 46)
        o += '<circle cx="%d" cy="12" r="11" fill="#7e9550"/>' % (sx * 46)
    o += text(-46, 17, 'A', 13, weight=900, fill='#fff') + text(46, 17, 'A', 13, weight=900, fill='#fff')
    return o + '</g>'


@figx('mascherine-confronto.svg')
def mascherine():
    b = title('Mascherine: cosa fermano davvero')
    data = [('Mascherina chirurgica', mask_surgical, [('Polvere', 'poco', 'mid'), ('Vapori', 'no', 'no')]),
            ('FFP2 (EN 149)', mask_ffp2, [('Polvere', 'sì, se aderente', 'ok'), ('Vapori', 'no', 'no')]),
            ('Semimaschera a carboni', mask_half, [('Polvere', 'con filtro P', 'ok'), ('Vapori', 'sì (filtro A)', 'ok')])]
    W = 232
    for k, (t, fn, rows) in enumerate(data):
        x = 20 + k * (W + 12)
        b += frame(x, 56, W, 240, t)
        b += fn(x + W / 2, 140, 1.0)
        for j, (a, v, st) in enumerate(rows):
            yy = 220 + j * 34
            if st == 'mid':
                b += excl(x + 28, yy - 5, AMBER, 11)
            else:
                b += mark(x + 28, yy - 5, st == 'ok', 11)
            b += text(x + 46, yy, a + ':', 14, 'start', 800)
            b += text(x + 46 + tw(a + ':', 14, True) + 6, yy, v, 14, 'start', 600)
    b += '<rect x="20" y="308" width="720" height="40" rx="12" fill="#fbe9e7"/>'
    b += text(380, 334, 'Nessuna mascherina sostituisce l\'aspirazione alla fonte', 16, weight=800, fill=ERR)
    return svg(760, 360, b, 'Mascherina chirurgica, FFP2 e semimaschera a carboni attivi a confronto')


def glove(cx, cy, s=1.0, ang=0, col=NITR, stroke=NITR_D, cuff=True, fist=False):
    """Mano (guantata o nuda) vista dal dorso, dita in alto. (cx, cy) = centro del palmo."""
    o = '<g transform="translate(%.1f,%.1f) rotate(%.1f) scale(%.2f)">' % (cx, cy, ang, s)
    segs = ([(-15, -16, -15, -48, 7.5), (-5, -18, -5, -56, 8), (5, -18, 5, -52, 8), (15, -16, 15, -42, 7)] if not fist else
            [(-15, -18, -15, -26, 7.5), (-5, -20, -5, -28, 8), (5, -20, 5, -28, 8), (15, -18, 15, -24, 7)])
    segs.append((-20, 6, -36, -16, 7.5))
    for x1, y1, x2, y2, r in segs:
        o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.1f" stroke-linecap="round"/>' % (x1, y1, x2, y2, stroke, 2 * r + 3)
        o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.1f" stroke-linecap="round"/>' % (x1, y1, x2, y2, col, 2 * r)
    o += '<rect x="-24" y="-24" width="48" height="50" rx="14" fill="%s" stroke="%s" stroke-width="1.6"/>' % (col, stroke)
    if cuff:
        o += '<rect x="-20" y="22" width="40" height="22" rx="4" fill="%s" stroke="%s" stroke-width="1.6"/>' % (col, stroke)
    else:
        o += '<rect x="-18" y="22" width="36" height="22" fill="%s" stroke="%s" stroke-width="1.6"/>' % (col, stroke)
    return o + '</g>'


@figx('guanti-togliere.svg')
def guanti():
    b = title('Togliere i guanti senza sporcarsi')
    labs = ['Pizzica all\'esterno', 'Tieni nel pugno', 'Dita dentro', 'Fai un sacchetto', 'Butta e igienizza']
    W = 148
    for i, lab in enumerate(labs):
        x = 20 + i * (W + 8)
        b += frame(x, 56, W, 192, None)
        b += badge(x + 22, 78, i + 1, ACC, 13)
        b += text(x + W / 2, 236, lab, 13, weight=700)
        cx = x + W / 2
        if i == 0:
            b += glove(cx - 26, 146, 0.95, 0) + glove(cx + 40, 186, 0.8, -90)
            b += '<circle cx="%.1f" cy="%.1f" r="9" fill="none" stroke="%s" stroke-width="2.5"/>' % (cx - 12, 184, ERR)
        elif i == 1:
            b += glove(cx - 4, 160, 0.95, 0, fist=True)
            b += '<path d="M%.1f,%.1f q-12,-18 6,-26 q20,-6 22,14 q2,16 -16,18 z" fill="%s" stroke="%s" stroke-width="1.6" opacity=".9"/>' % (cx - 18, 140, '#aab5e6', NITR_D)
            b += glove(cx + 40, 150, 0.7, 20, SKIN, SKIN_D, cuff=False)
        elif i == 2:
            b += glove(cx - 24, 156, 0.9, 0, fist=True)
            b += glove(cx + 26, 150, 0.8, -25, SKIN, SKIN_D, cuff=False)
            b += arrow(cx + 4, 196, cx - 14, 182, ACC2, 2)
        elif i == 3:
            b += '<path d="M%.1f,%.1f q-26,-30 4,-44 q34,-10 40,22 q4,30 -24,30 z" fill="%s" stroke="%s" stroke-width="1.8"/>' % (cx - 18, 186, '#9aa6e0', NITR_D)
            b += '<path d="M%.1f,%.1f q-6,-14 8,-18" stroke="%s" stroke-width="1.6" fill="none"/>' % (cx - 4, 166, NITR_D)
            b += glove(cx + 40, 132, 0.62, 30, SKIN, SKIN_D, cuff=False)
        else:
            b += trash(cx - 22, 206, 46, 60, pedal=True)
            b += bottle(cx + 38, 206, 30, 50, '#e6f1f8', '') 
            b += drop_icon(cx + 38, 126, 0.6, '#7fb0cc')
            b += glove(cx + 22, 104, 0.45, 0, SKIN, SKIN_D, cuff=False)
    return svg(800, 260, arrow_defs() + b, 'Come togliere i guanti in cinque passaggi')




def face_profile(cx, cy, s=1.0, zones=True):
    """Volto di profilo rivolto a sinistra. (cx, cy) ~ centro del viso."""
    o = '<g transform="translate(%.1f,%.1f) scale(%.2f)">' % (cx, cy, s)
    o += ('<path d="M40,-100 C0,-110 -38,-92 -42,-58 L-46,-42 Q-46,-36 -50,-30 L-62,-14 Q-62,-8 -50,-8 Q-46,-6 -50,0 Q-46,4 -50,8 Q-48,18 -38,26 '
          'Q-20,34 0,30 L6,80 L58,80 L52,24 Q76,0 70,-44 Q66,-94 40,-100 Z" fill="%s" stroke="%s" stroke-width="1.8"/>' % (SKIN, SKIN_D))
    o += '<path d="M40,-100 C0,-110 -38,-92 -42,-62 Q-10,-80 20,-70 Q40,-60 52,-30 Q72,-20 70,-44 Q66,-94 40,-100 Z" fill="#6b4434"/>'
    o += '<path d="M-36,-40 Q-28,-46 -20,-40 Q-28,-36 -36,-40 Z" fill="#fff" stroke="%s" stroke-width="1.5"/><circle cx="-29" cy="-40" r="2.4" fill="%s"/>' % (INK, INK)
    o += '<path d="M24,-30 q10,-6 12,8 q-2,12 -12,8" fill="none" stroke="%s" stroke-width="1.6"/>' % SKIN_D
    if zones:
        o += '<ellipse cx="-28" cy="-44" rx="13" ry="7" fill="%s" opacity=".55"/>' % ERR
        o += '<ellipse cx="-20" cy="-8" rx="13" ry="10" fill="%s" opacity=".4"/>' % ERR
        o += '<ellipse cx="28" cy="52" rx="16" ry="20" fill="%s" opacity=".4"/>' % ERR
        o += ''.join('<circle cx="%d" cy="%d" r="1.6" fill="%s"/>' % (px, py, ERR) for px, py in ((-24, -10), (-16, -4), (-22, -2), (22, 46), (30, 58), (34, 44), (26, 62)))
    return o + '</g>'


@figx('allergia-zone.svg')
def allergia_zone():
    b = title('Dove compare l\'allergia agli acrilati')
    cx, cy, sc = 260, 296, 0.9
    b += hand_back(cx, cy, sc)
    ft = finger_tips(cx, cy, sc)
    for k, (tip, mid, base) in enumerate(ft):
        b += '<ellipse cx="%.1f" cy="%.1f" rx="16" ry="9" fill="%s" opacity=".45"/>' % (base[0], base[1] + 6, ERR)
        b += ''.join('<circle cx="%.1f" cy="%.1f" r="1.8" fill="%s"/>' % (base[0] + dx, base[1] + 6 + dy, ERR) for dx, dy in ((-8, 0), (0, 3), (7, -1), (3, -4)))
        b += '<ellipse cx="%.1f" cy="%.1f" rx="12" ry="7" fill="%s" opacity=".35"/>' % (tip[0], tip[1] - 2, ERR)
    t1 = ft[2]
    b += '<path d="M%.1f,%.1f q-6,-14 2,-20 q10,-2 12,8 z" fill="#fff" stroke="%s" stroke-width="1.5"/>' % (t1[0][0] - 4, t1[0][1] + 14, NAIL_S)
    b += callout(ft[0][2][0] - 8, ft[0][2][1] + 6, 88, 214, 'Intorno all\'unghia', 14, 700)
    b += '<line x1="%.1f" y1="%.1f" x2="100" y2="116" stroke="%s" stroke-width="1.3"/><circle cx="%.1f" cy="%.1f" r="3.5" fill="%s"/>' % (
        ft[0][0][0] - 4, ft[0][0][1] + 2, MUTED, ft[0][0][0] - 4, ft[0][0][1] + 2, ACC2)
    b += mtext(100, 92, ['Polpastrelli secchi', 'e spaccati'], 14, weight=700)
    b += callout(t1[0][0] + 4, t1[0][1] + 4, 370, 84, 'Unghia che si stacca', 14, 700)
    # volto
    fx, fy = 610, 210
    b += face_profile(fx, fy, 1.15)
    b += callout(fx - 32, fy - 52, 560, 84, 'Palpebre', 14, 700)
    b += callout(fx + 34, fy + 64, 680, 340, 'Viso e collo', 14, 700)
    b += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="6 5"/>' % (
        ft[3][0][0] + 12, ft[3][0][1] + 4, 440, 110, fx - 70, fy - 18, ACC2)
    b += text(450, 204, 'Le dita toccano il viso', 13.5, weight=700, fill=ACC2)
    # fasi
    b += '<rect x="20" y="380" width="720" height="46" rx="12" fill="%s"/>' % PANEL
    b += badge(46, 403, 1, ACC, 13) + text(66, 408, 'Sensibilizzazione (nessun segno)', 15, 'start', 700)
    b += arrow(330, 403, 380, 403)
    b += badge(404, 403, 2, ERR, 13) + text(424, 408, 'Reazione: l\'allergia resta per sempre', 15, 'start', 700, ERR)
    return svg(760, 440, arrow_defs() + b, 'Zone in cui compare la dermatite allergica da acrilati: dita, unghie, palpebre, viso e collo')


@figx('contatto-pelle.svg')
def contatto_pelle():
    b = title('Il prodotto non deve toccare la pelle')
    for k in range(2):
        x0 = 20 + k * 300
        b += frame(x0, 56, 288, 270, 'Prodotto sulla pelle' if k == 0 else 'Margine pulito', ok=(k == 1))
        cx, yc = x0 + 110, 260
        hw = 52
        if k == 0:
            f, p = finger_nail(cx, yc, hw=hw, nail_len=140, free_len=20, shape='squoval', smile=8, finger_len=40, lunula=False)
            b += f
            ys = p['y_t']
            r = 18
            prod = ('M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z' % (
                cx - hw - 9, yc - 20, cx - hw - 9, ys + r, cx - hw - 9, ys, cx - hw + r, ys, cx + hw - r, ys, cx + hw + 9, ys, cx + hw + 9, ys + r,
                cx + hw + 9, yc - 20, cx, yc + 34, cx - hw - 9, yc - 20))
            b += '<path d="%s" fill="%s" opacity=".8" stroke="%s" stroke-width="1.5"/>' % (prod, PROD, PROD_S)
            b += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="4" opacity=".75"/>' % (cx - hw - 6, yc - 12, cx, yc + 32, cx + hw + 6, yc - 12, ERR)
            for sx in (-1, 1):
                b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="4" opacity=".75"/>' % (cx + sx * (hw + 8), ys + 30, cx + sx * (hw + 8), yc - 20, ERR)
            b += callout(cx + hw + 8, yc - 70, x0 + 220, 120, 'pieghe', 13, 700, ERR)
            b += callout(cx + 20, yc + 12, x0 + 226, 300, 'cuticola', 13, 700, ERR)
            b += mtext(x0 + 144, 344, ['Rischio allergia e sollevamento'], 13.5, weight=800, fill=ERR)
        else:
            m = 7
            ex = ('<path d="M%.1f,-200 L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,-200 Z" fill="%s" opacity=".85" stroke="%s" stroke-width="1.5" clip-path="url(#CLIP)"/>' % (
                cx - hw + m, cx - hw + m, yc - 34, cx, yc + 10, cx + hw - m, yc - 34, cx + hw - m, PROD, PROD_S))
            f, p = finger_nail(cx, yc, hw=hw, nail_len=140, free_len=20, shape='squoval', smile=8, finger_len=40, lunula=False, extra=ex)
            b += f
            b += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="2.5" stroke-dasharray="5 4"/>' % (cx - hw + m, yc - 30, cx, yc + 12, cx + hw - m, yc - 30, OK)
            b += callout(cx + hw - m, yc - 60, x0 + 224, 120, 'margine', 13, 700, OK)
            b += text(x0 + 224, 136, '≈ 1 mm', 13, weight=700, fill=OK)
            b += callout(cx, yc - 10, x0 + 228, 300, 'cuticola libera', 13, 700, OK)
            b += mtext(x0 + 144, 344, ['Sbavature tolte prima della lampada'], 13.5, weight=800, fill=OK)
    # lampada
    b += frame(620, 56, 120, 270, None)
    b += lamp(680, 230, 96, 'UV/LED')
    b += mtext(680, 262, ['Polimerizza', 'tutto,', 'pollice a parte'], 13, weight=700)
    return svg(760, 360, b, 'Prodotto che tocca cuticola e pieghe (errato) e margine pulito di circa 1 mm (corretto)')


def pao(cx, cy, label='12M', s=1.0):
    return ('<g transform="translate(%.1f,%.1f) scale(%.2f)"><path d="M-14,-6 L14,-6 L12,16 L-12,16 Z" fill="#fff" stroke="%s" stroke-width="2"/>'
            '<path d="M-15,-8 L13,-18 L15,-13 L-13,-3 Z" fill="#fff" stroke="%s" stroke-width="2"/></g>' % (cx, cy, s, INK, INK)
            + text(cx, cy + 9 * s, label, 10.5 * s + 1.5, weight=800))


@figx('etichetta-inci.svg')
def etichetta_inci():
    b = title('Cosa cercare in etichetta')
    # flacone di gel
    b += '<rect x="58" y="150" width="110" height="200" rx="18" fill="#f6d6df" stroke="%s" stroke-width="2"/>' % NAIL_S
    b += '<rect x="80" y="86" width="66" height="70" rx="8" fill="%s"/>' % INK
    b += '<rect x="72" y="200" width="82" height="96" rx="6" fill="#fff"/>'
    b += text(113, 228, 'BUILDER', 13, weight=900, fill=ACC2) + text(113, 248, 'GEL', 13, weight=900, fill=ACC2)
    b += text(113, 276, '15 ml', 12, weight=600, fill=MUTED)
    b += '<path d="M176,240 L214,200 M176,240 L214,330" stroke="%s" stroke-width="1.5" stroke-dasharray="4 4"/>' % GREY
    # etichetta ingrandita
    X, Y, Wd = 220, 60, 520
    b += '<rect x="%d" y="%d" width="%d" height="346" rx="10" fill="#fffdf8" stroke="%s" stroke-width="1.8"/>' % (X, Y, Wd, GREY_D)
    rows = [
        ('ok', 'Solo per uso professionale'),
        ('ok', 'Può provocare una reazione allergica'),
    ]
    yy = Y + 32
    for st, t in rows:
        b += '<rect x="%d" y="%d" width="%d" height="26" rx="5" fill="#d9f0e2"/>' % (X + 14, yy - 18, Wd - 28)
        b += mark(X + 30, yy - 5, True, 9) + text(X + 46, yy, t, 14.5, 'start', 700)
        yy += 34
    b += text(X + 14, yy + 4, 'INGREDIENTS: Urethane Dimethacrylate,', 13.5, 'start', 600)
    b += text(X + 14, yy + 24, 'HEMA, Silica, Hydroxycyclohexyl Phenyl Ketone...', 13.5, 'start', 600)
    b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2.5"/>' % (X + 14, yy + 29, X + 56, yy + 29, ACC2)
    b += magnifier(X + Wd - 64, yy + 2, 20)
    yy += 52
    b += text(X + 14, yy, 'Se nell\'INCI trovi questi nomi: non usare', 13.5, 'start', 800, ERR)
    for t, badge_t in (('Trimethylbenzoyl Diphenylphosphine Oxide (TPO)', 'VIETATO dal 1/9/2025'), ('Dimethyltolylamine (DMTA)', 'VIETATO')):
        yy += 30
        b += '<rect x="%d" y="%d" width="%d" height="26" rx="5" fill="#fbe1de"/>' % (X + 14, yy - 18, Wd - 28)
        b += text(X + 22, yy, t, 13, 'start', 600).replace('<text ', '<text text-decoration="line-through" ')
        b += chip(X + Wd - 22 - (tw(badge_t, 11.5, True) + 18) / 2, yy - 5, badge_t, ERR, '#fff', 12)
    yy += 44
    b += text(X + 14, yy, 'Lotto: 2409A', 14, 'start', 700)
    b += pao(X + 190, yy - 8, '12M', 1.15)
    b += text(X + 214, yy, 'dopo l\'apertura', 13, 'start', 600, MUTED)
    yy += 30
    b += text(X + 14, yy, 'Responsabile: nome e indirizzo UE', 14, 'start', 700)
    yy += 24
    b += text(X + 14, yy, 'Etichetta e avvertenze in italiano', 13, 'start', 600, MUTED)
    return svg(760, 420, b, 'Etichetta di un gel: avvertenze HEMA, assenza di TPO e DMTA, lotto e PAO')


def box(x, y, w, h, lines, fill='#fff', stroke=ACC, size=13, weight=700, fg=INK):
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="10" fill="%s" stroke="%s" stroke-width="1.8"/>' % (x, y, w, h, fill, stroke)
    n = len(lines)
    y0 = y + h / 2 - (n - 1) * size * 1.25 / 2 + size * 0.36
    return s + mtext(x + w / 2, y0, lines, size, 'middle', weight, fg)


@figx('percorsi-estetista.svg')
def percorsi():
    b = title('Tre strade per diventare estetista abilitata')
    lanes = [('Corso', [(0, 1, ['Corso biennale', '(≈1.800 h)']), (1, 1, ['Qualifica']), (2, 1, ['Specializzazione', '600 h o 1 anno', 'di lavoro']), (3, 1, ['Esame'])]),
             ('Apprendistato', [(0, 1, ['Apprendistato']), (1, 1, ['1 anno di lavoro', 'qualificato']), (2, 1, ['Corso teorico', '300 h']), (3, 1, ['Esame'])]),
             ('Esperienza', [(0, 2, ['3 anni di lavoro qualificato']), (2, 1, ['Corso teorico', '300 h']), (3, 1, ['Esame'])])]
    X0, CW, G = 150, 114, 16
    for i, (ln, items) in enumerate(lanes):
        y = 66 + i * 98
        b += '<rect x="20" y="%d" width="644" height="82" rx="14" fill="%s"/>' % (y, PANEL)
        b += text(30, y + 46, ln, 14, 'start', 800, ACC2)
        for col, span, lines in items:
            x = X0 + col * (CW + G)
            w = CW * span + G * (span - 1)
            b += box(x, y + 10, w, 62, lines, '#fff', ACC if lines != ['Esame'] else ACC2, 12.5)
            if col + span < 4:
                b += arrow(x + w + 2, y + 41, x + w + G - 2, y + 41)
        ex = X0 + 3 * (CW + G) + CW
        b += '<path d="M%d,%d C%d,%d %d,%d %d,%d" fill="none" stroke="%s" stroke-width="2.2" marker-end="url(#ar)"/>' % (
            ex + 2, y + 41, ex + 30, y + 41, 670, 214, 686, 214, ACC2)
    b += '<rect x="690" y="150" width="96" height="128" rx="16" fill="%s"/>' % OK
    b += mtext(738, 196, ['Estetista', 'abilitata'], 15, weight=900, fill='#fff')
    b += mark(738, 248, True, 13).replace('fill="%s"' % OK, 'fill="#ffffff"').replace('stroke="#fff"', 'stroke="%s"' % OK)
    b += text(20, 382, 'Esempio Emilia-Romagna: ore e percorsi li decide ogni Regione.', 13, 'start', 600, MUTED)
    b += text(20, 402, 'Verifica sempre le regole della tua Regione e del tuo Comune.', 13, 'start', 600, MUTED)
    b += doc(574, 360, 34, 44, 3) + no_sign(591, 382, 22)
    b += mtext(624, 380, ['Attestato privato', 'da solo: non abilita'], 13, 'start', 700, ERR)
    return svg(800, 420, arrow_defs() + b, 'Percorsi per la qualifica di estetista: corso, apprendistato, esperienza')


@figx('apertura-attivita.svg')
def apertura():
    b = title('Aprire l\'attività: le tappe')
    b += '<path d="M10,262 C160,222 240,296 400,258 C560,220 620,292 750,252" fill="none" stroke="#d9d2cf" stroke-width="40" stroke-linecap="round"/>'
    b += '<path d="M10,262 C160,222 240,296 400,258 C560,220 620,292 750,252" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="14 12"/>'
    steps = [('Locale a norma', ['regolamento comunale', 'e ASL']), ('SCIA al SUAP', ['del Comune']), ('Responsabile', ['tecnico qualificato']),
             ('ComUnica', ['Registro Imprese,', 'INPS, INAIL, Fisco']), ('Documenti pronti', ['protocollo, registro,', 'SDS, schede clienti'])]
    xs = [84, 232, 380, 528, 676]
    ys = [246, 262, 258, 240, 262]
    for k, (t, sub) in enumerate(steps):
        x, y = xs[k], ys[k]
        b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3"/>' % (x, y, x, y - 62, INK)
        b += '<path d="M%d,%d L%d,%d L%d,%d L%d,%d L%d,%d Z" fill="%s"/>' % (x, y - 62, x + 40, y - 62, x + 32, y - 49, x + 40, y - 36, x, y - 36, ACC)
        b += text(x + 16, y - 43, str(k + 1), 16, 'middle', 900, '#fff')
        iy = 130
        if k == 0:
            b += '<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="#f6d6df" stroke="%s" stroke-width="2"/>' % (x - 34, iy + 30, x - 34, iy - 6, x + 34, iy - 6, x + 34, iy + 30, ACC2)
            b += '<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="%s"/>' % (x - 40, iy - 6, x - 32, iy - 26, x + 32, iy - 26, x + 40, iy - 6, ACC)
            b += '<rect x="%d" y="%d" width="18" height="24" fill="#fff" stroke="%s"/>' % (x - 9, iy + 6, ACC2)
            b += chip(x + 44, iy + 24, 'ASL', '#3f86b8', '#fff', 12)
        elif k == 1:
            b += doc(x - 46, iy - 34, 40, 54, 4)
            b += '<path d="M%d,%d L%d,%d L%d,%d Z" fill="%s"/>' % (x + 2, iy - 8, x + 26, iy - 26, x + 50, iy - 8, GREY_D)
            b += ''.join('<rect x="%d" y="%d" width="6" height="26" fill="%s"/>' % (x + 6 + j * 14, iy - 6, GREY) for j in range(4))
            b += '<rect x="%d" y="%d" width="48" height="6" fill="%s"/>' % (x + 2, iy + 20, GREY_D)
        elif k == 2:
            b += '<circle cx="%d" cy="%d" r="13" fill="%s"/>' % (x, iy - 18, SKIN)
            b += '<path d="M%d,%d Q%d,%d %d,%d Z" fill="#cfe0ec" stroke="%s"/>' % (x - 24, iy + 26, x, iy - 18, x + 24, iy + 26, GREY_D)
            b += '<rect x="%d" y="%d" width="16" height="11" rx="2" fill="%s"/>' % (x + 2, iy + 6, ACC)
        elif k == 3:
            b += '<rect x="%d" y="%d" width="54" height="36" rx="4" fill="#e6f1f8" stroke="%s" stroke-width="2"/>' % (x - 40, iy - 22, GREY_D)
            b += '<rect x="%d" y="%d" width="66" height="6" rx="2" fill="%s"/>' % (x - 46, iy + 14, GREY_D)
            b += '<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="%s"/>' % (x + 14, iy - 4, x + 44, iy - 22, x + 34, iy + 6, x + 28, iy - 2, ACC)
        else:
            b += '<path d="M%d,%d L%d,%d L%d,%d L%d,%d L%d,%d L%d,%d Z" fill="#f1d27a" stroke="#c9a54a" stroke-width="2"/>' % (
                x - 34, iy + 26, x - 34, iy - 24, x - 12, iy - 24, x - 6, iy - 16, x + 34, iy - 16, x + 34, iy + 26)
            b += ''.join('<rect x="%d" y="%d" width="10" height="16" fill="%s"/>' % (x - 26 + j * 15, iy - 30, c) for j, c in enumerate((ACC, OK, '#3f86b8', AMBER)))
        b += text(x, 310, t, 14.5, weight=800)
        b += mtext(x, 330, sub, 12.5, weight=600, fill=MUTED)
    return svg(760, 380, b, 'Tappe per aprire l\'attività: locale, SCIA, responsabile tecnico, ComUnica, documenti')




def hpt(cx, cy, s, lx, ly, palm=False):
    return (cx - s * lx if palm else cx + s * lx, cy + s * ly)


def foam(x, y, r=12, seed=1):
    import random as _r
    rnd = _r.Random(seed)
    o = ''
    for _ in range(6):
        o += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#dff1fb" stroke="#7fb0cc" stroke-width="1.2" opacity=".95"/>' % (
            x + rnd.uniform(-r, r), y + rnd.uniform(-r * 0.6, r * 0.6), rnd.uniform(r * 0.35, r * 0.6))
    return o


def circ_arrow(x, y, r=14, col=ACC2):
    return cpath('M%.1f,%.1f A%.1f,%.1f 0 1 1 %.1f,%.1f' % (x - r, y, r, r, x - r * 0.7, y + r * 0.7), col, 2.2)


@figx('lavaggio-mani.svg')
def lavaggio():
    b = title('Igiene delle mani: tutti i punti')
    b += '<circle cx="580" cy="32" r="10" fill="none" stroke="#d6a63a" stroke-width="3.5"/><rect x="604" y="22" width="22" height="20" rx="5" fill="none" stroke="%s" stroke-width="3"/>' % GREY_D
    b += no_sign(580, 32, 15, 3) + no_sign(615, 32, 15, 3)
    b += text(640, 38, 'Niente gioielli', 14, 'start', 800, ERR)
    labs = ['Palmo contro palmo', 'Dorso con dita intrecciate', 'Palmo con dita intrecciate', 'Dorso delle dita',
            'Pollici', 'Punte delle dita sul palmo', 'Risciacqua e asciuga con carta monouso', None]
    W, H = 182, 178
    for i, lab in enumerate(labs):
        x = 20 + (i % 4) * (W + 10)
        y = 56 + (i // 4) * (H + 10)
        pc = uid('lv')
        b += '<defs><clipPath id="%s"><rect x="%d" y="%d" width="%d" height="%d" rx="16"/></clipPath></defs>' % (pc, x, y, W, H)
        b += '<rect x="%d" y="%d" width="%d" height="%d" rx="16" fill="%s"/>' % (x, y, W, H, PANEL)
        g = ''
        cx, cy, sc = x + 92, y + 98, 0.42
        if i < 6:
            palm = i in (0, 2, 4, 5)
            g += hand_back(cx, cy, sc, palm=palm)
            if i in (0, 1):
                px, py = hpt(cx, cy, sc, 5, 15, palm)
                g += foam(px, py, 18, i)
                g += circ_arrow(px + 30, py - 30, 11)
            if i in (1, 2):
                for k, lx in enumerate((-33, 1, 34)):
                    px, py = hpt(cx, cy, sc, lx, -58, palm)
                    g += foam(px, py, 7, 10 + k)
            if i == 3:
                for k, (fx, L, r, a) in enumerate(HAND_FINGERS):
                    px, py = hpt(cx, cy, sc, fx + a * 1.1, -46 - L * 0.45, palm)
                    g += foam(px, py, 7, 20 + k)
            if i == 4:
                px, py = hpt(cx, cy, sc, -96, 6, palm)
                g += foam(px, py, 12, 30)
                g += circ_arrow(px + 4, py - 4, 22)
            if i == 5:
                for k, (fx, L, r, a) in enumerate(HAND_FINGERS):
                    px, py = hpt(cx, cy, sc, fx + a * 2.2, -46 - L + 4, palm)
                    g += foam(px, py, 6, 40 + k)
                g += circ_arrow(x + 150, y + 54, 10)
        elif i == 6:
            g += '<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d" fill="none" stroke="%s" stroke-width="10" stroke-linecap="round"/>' % (
                x + 20, y + 52, x + 70, y + 52, x + 86, y + 52, x + 86, y + 66, x + 86, y + 70, GREY)
            g += ''.join(drop_icon(x + 80 + dx, y + 86 + dy, 0.45, '#7fb0cc') for dx, dy in ((0, 0), (10, 14), (-6, 20)))
            g += hand_back(x + 80, y + 170, 0.36, palm=True)
            g += '<rect x="%d" y="%d" width="46" height="60" rx="4" fill="#fff" stroke="%s" stroke-width="1.6" transform="rotate(8 %d %d)"/>' % (x + 122, y + 64, GREY, x + 145, y + 94)
            g += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#d8dde3" stroke-width="2"/>' % (x + 128, y + 80, x + 160, y + 84)
        else:
            g += stopwatch(x + 44, y + 64, 22)
            g += text(x + 76, y + 58, 'Gel alcolico', 13.5, 'start', 800)
            g += text(x + 76, y + 76, '20–30 s', 13.5, 'start', 700, ACC2)
            g += text(x + 20, y + 120, 'Acqua e sapone', 13.5, 'start', 800)
            g += text(x + 20, y + 138, '40–60 s', 13.5, 'start', 700, ACC2)
            g += text(x + 20, y + 162, 'se le mani sono sporche', 12.5, 'start', 600, MUTED)
        b += '<g clip-path="url(#%s)">%s</g>' % (pc, g)
        b += badge(x + 22, y + 22, i + 1, ACC, 13)
        if lab:
            lines = wrap(lab, W - 20, 13, True)
            yy = y + H - 10 - (len(lines) - 1) * 16
            b += '<rect x="%d" y="%.1f" width="%d" height="%.1f" fill="%s" opacity=".9"/>' % (x + 4, yy - 16, W - 8, H - (yy - 16 - y) - 4, PANEL)
            b += mtext(x + W / 2, yy, lines, 13, weight=700, lh=1.23)
    return svg(800, 434, arrow_defs() + b, 'Lavaggio e frizione delle mani: palmi, dorsi, spazi tra le dita, pollici e punte')


@figx('incidente-taglio.svg')
def incidente():
    b = title('Piccolo taglio durante il servizio')
    labs = [['Premi con', 'garza sterile'], ['Disinfetta', 'e copri'], ['Strumento', 'da parte'], ['Garze nel contenitore', 'a rischio infettivo']]
    W = 176
    for i, lab in enumerate(labs):
        x = 20 + i * (W + 12)
        b += frame(x, 56, W, 270, None)
        b += badge(x + 24, 80, i + 1, ACC, 13)
        cx = x + W / 2
        if i == 0:
            b += mini(None, cx - 28, 200, 0.85)
            b += drop_icon(cx - 74, 172, 0.6, '#c62828') + drop_icon(cx - 66, 196, 0.45, '#c62828')
            b += '<rect x="%.1f" y="%.1f" width="40" height="34" rx="3" fill="#fff" stroke="%s" stroke-width="1.5" transform="rotate(-10 %.1f %.1f)"/>' % (cx - 50, 128, GREY, cx - 30, 145)
            b += '<path d="M%.1f,%.1f l26,-4 M%.1f,%.1f l26,-4" stroke="#e0e4e8" stroke-width="2"/>' % (cx - 44, 142, cx - 42, 152)
            b += glove(cx + 26, 114, 0.75, -125)
        elif i == 1:
            b += bottle(cx - 34, 230, 54, 90, '#eaf3f9', 'cute lesa', 12)
            b += text(cx - 34, 252, 'disinfettante', 12, weight=600, fill=MUTED)
            b += ('<g transform="rotate(-30 %.1f %.1f)"><rect x="%.1f" y="%.1f" width="74" height="24" rx="12" fill="#f3d2b5" stroke="#c99a74" stroke-width="1.5"/>'
                  '<rect x="%.1f" y="%.1f" width="26" height="18" rx="3" fill="#fbe9dc"/></g>' % (cx + 40, 170, cx + 4, 158, cx + 28, 161))
        elif i == 2:
            b += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="#e6eaee" stroke="%s" stroke-width="2"/>' % (cx - 62, 170, cx + 62, 170, cx + 52, 214, cx - 52, 214, GREY_D)
            b += nipper(cx + 14, 186, 0.8, 0)
            b += chip(cx, 246, 'da sterilizzare', OK, '#fff', 12.5)
        else:
            b += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="#f2c94c" stroke="#b8901c" stroke-width="2"/>' % (cx - 40, 140, cx + 40, 140, cx + 34, 250, cx - 34, 250)
            b += '<rect x="%.1f" y="%.1f" width="92" height="14" rx="4" fill="#e0b53a" stroke="#b8901c" stroke-width="2"/>' % (cx - 46, 128)
            b += biohazard(cx, 194, 20, INK)
        b += mtext(cx, 290, lab, 14, weight=700)
    b += '<rect x="20" y="334" width="740" height="0"/>'
    return svg(780, 340, b, 'Cosa fare se una cliente sanguina: pressione, disinfezione, strumenti da parte, rifiuti a rischio infettivo')


@figx('rifiuti-contenitori.svg')
def rifiuti():
    b = title('Dove vanno i rifiuti')
    W = 168
    data = [('Taglienti', ['lame, aghi,', 'strumenti rotti']), ('Rischio infettivo', ['garze, cotone,', 'guanti con sangue']),
            ('Salviette con solventi', ['acetone, monomero,', 'cleaner'])]
    for i, (t, sub) in enumerate(data):
        x = 20 + i * (W + 10)
        b += frame(x, 56, W, 256, None)
        cx = x + W / 2
        if i == 0:
            b += '<rect x="%.1f" y="110" width="80" height="110" rx="6" fill="#f2c94c" stroke="#b8901c" stroke-width="2"/>' % (cx - 40)
            b += '<path d="M%.1f,110 L%.1f,96 L%.1f,96 L%.1f,110 Z" fill="#e0b53a" stroke="#b8901c" stroke-width="2"/>' % (cx - 40, cx - 30, cx + 30, cx + 40)
            b += '<rect x="%.1f" y="99" width="24" height="5" fill="%s"/>' % (cx - 12, INK)
            b += biohazard(cx, 160, 16)
            b += '<path d="M%.1f,86 l26,-20 l4,4 l-26,20 z" fill="%s"/>' % (cx + 12, METAL)
        elif i == 1:
            b += '<path d="M%.1f,110 L%.1f,110 L%.1f,222 L%.1f,222 Z" fill="#fff4cf" stroke="#b8901c" stroke-width="2"/>' % (cx - 44, cx + 44, cx + 38, cx - 38)
            b += '<path d="M%.1f,110 Q%.1f,96 %.1f,110" fill="#f2c94c" stroke="#b8901c" stroke-width="2"/>' % (cx - 44, cx, cx + 44)
            b += biohazard(cx, 166, 18)
        else:
            b += trash(cx, 222, 84, 106, col='#d7dce1', pedal=True)
            b += '<path d="M%.1f,%.1f q8,-14 20,-6 q10,-10 18,4" fill="#fff" stroke="%s"/>' % (cx - 20, 104, GREY)
        b += mtext(cx, 256, [t], 15, weight=800)
        b += mtext(cx, 278, sub, 12.5, weight=600, fill=MUTED)
    # scaffale prodotti scaduti
    x = 20 + 3 * (W + 10)
    b += frame(x, 56, 206, 256, None)
    b += '<rect x="%d" y="78" width="178" height="58" rx="6" fill="%s"/>' % (x + 14, ERR)
    b += mtext(x + 103, 100, ['PRODOTTI SCADUTI', 'E NON UTILIZZABILI'], 13, weight=900, fill='#fff')
    for k in range(2):
        yy = 190 + k * 56
        b += '<rect x="%d" y="%d" width="178" height="6" fill="#b39a86"/>' % (x + 14, yy)
        for j in range(4):
            b += bottle(x + 38 + j * 42, yy, 22, 34 - (j % 2) * 6, ['#f6d6df', '#dfe9f2', '#e8e0f5', '#fff4cf'][j])
    b += text(x + 103, 274, 'ritiro dal fornitore', 12.5, weight=600, fill=MUTED)
    b += text(x + 103, 292, 'o smaltimento (vedi SDS)', 12.5, weight=600, fill=MUTED)
    # lavandino
    b += '<rect x="20" y="322" width="740" height="56" rx="12" fill="#fbe9e7"/>'
    b += '<path d="M60,346 L120,346 Q118,370 90,370 Q62,370 60,346 Z" fill="#e6eaee" stroke="%s" stroke-width="2"/>' % GREY_D
    b += '<path d="M90,346 L90,334 L104,334" fill="none" stroke="%s" stroke-width="4"/>' % GREY_D
    b += bottle(140, 370, 22, 30, '#e8e0f5') + no_sign(100, 352, 24)
    b += text(176, 346, 'Mai nello scarico monomero, acetone e gel.', 15.5, 'start', 900, ERR)
    b += text(176, 368, 'Piccole quantità: falle indurire o evaporare, poi smaltisci come indica la SDS.', 13.5, 'start', 600)
    return svg(780, 390, b, 'Contenitori per taglienti, rifiuti a rischio infettivo e salviette con solventi; prodotti scaduti separati')


# ================================================================= MODULO 3 – SISTEMI
def network(x, y, w, h, step, col=ACC2, node='#e9a7bd', seed=2, jitter=0.25):
    """Rete di polimero: nodi su griglia irregolare collegati ai vicini."""
    import random as _r
    rnd = _r.Random(seed)
    nx, ny = int(w // step) + 1, int(h // step) + 1
    P = {}
    for i in range(nx):
        for j in range(ny):
            P[i, j] = (x + i * step + rnd.uniform(-jitter, jitter) * step, y + j * step + rnd.uniform(-jitter, jitter) * step)
    o = ''
    for (i, j), (px, py) in P.items():
        for di, dj in ((1, 0), (0, 1), (1, 1)):
            q = P.get((i + di, j + dj))
            if q and (di + dj == 1 or (i + j) % 2 == 0):
                o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>' % (px, py, q[0], q[1], col)
    for (px, py) in P.values():
        o += '<circle cx="%.1f" cy="%.1f" r="4" fill="%s" stroke="%s" stroke-width="1.2"/>' % (px, py, node, col)
    return o


def acetone_drop(x, y, s=0.7):
    return drop_icon(x, y, s, '#6fb6e0')


def foil(cx, cy, s=1.0):
    return ('<path d="M%.1f,%.1f l%.1f,%.1f l%.1f,%.1f l%.1f,%.1f l%.1f,%.1f z" fill="#d9dee3" stroke="%s" stroke-width="1.5"/>'
            % (cx - 22 * s, cy - 10 * s, 18 * s, -14 * s, 26 * s, 6 * s, -4 * s, 22 * s, -34 * s, 4 * s, GREY_D)
            + '<path d="M%.1f,%.1f l%.1f,%.1f" stroke="#fff" stroke-width="2"/>' % (cx - 10 * s, cy - 14 * s, 14 * s, 4 * s))


def efile_hand(cx, cy, s=1.0, ang=0):
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f) scale(%.2f)"><rect x="-10" y="-9" width="70" height="18" rx="9" fill="#e6e1ec" stroke="%s" stroke-width="1.6"/>'
            '<rect x="-18" y="-5" width="10" height="10" fill="%s"/><rect x="-34" y="-6" width="16" height="12" rx="2" fill="%s"/>'
            '<path d="M60,0 q20,0 30,14" stroke="%s" stroke-width="3" fill="none"/></g>' % (cx, cy, ang, s, GREY_D, METAL, GREY, GREY_D))


@figx('sistemi-rimozione.svg')
def sistemi_rim():
    b = title('Acetone o lima? Dipende dalla rete di polimero')
    b += frame(20, 56, 354, 270, 'Si scioglie in acetone')
    b += network(50, 126, 160, 84, 40, '#3f86b8', '#cfe6f7', 4)
    for (dx, dy) in ((72, 148), (112, 186), (152, 146), (190, 190), (94, 112)):
        b += acetone_drop(dx, dy, 0.55)
    b += mark(222, 112, True, 10)
    b += text(290, 112, 'maglia larga:', 13, weight=700, fill=MUTED)
    b += text(290, 130, 'l\'acetone entra', 13, weight=700, fill=MUTED)
    b += bowl(266, 170, 54) + foil(334, 180, 0.8)
    b += clock(270, 220, 13) + text(290, 225, '10–20 min', 13, 'start', 800, ACC2)
    b += para(40, 266, 'Soft gel, semipermanente, acrilico, dip, fibra', 320, 14, weight=700)[0]
    b += frame(386, 56, 354, 270, 'Si toglie limando')
    b += network(416, 134, 150, 80, 18, ACC2, '#f6d6df', 7, 0.2)
    for dx in (450, 520):
        b += acetone_drop(dx, 112, 0.55)
        b += '<path d="M%.1f,%.1f q10,-16 22,-10" fill="none" stroke="#6fb6e0" stroke-width="2" marker-end="url(#arw)"/>' % (dx + 6, 110)
    b += mark(588, 112, False, 10)
    b += text(660, 112, 'maglia fitta:', 13, weight=700, fill=MUTED)
    b += text(660, 130, 'l\'acetone non entra', 13, weight=700, fill=MUTED)
    b += tool_file(650, 176, -20, 90, 16) + efile_hand(630, 218, 0.8, -10)
    b += para(406, 266, 'Hard gel (e alcuni polygel): si lima lasciando un velo', 320, 14, weight=700)[0]
    return svg(760, 340, arrow_defs() + b, 'Rete di polimero aperta (si scioglie in acetone) e fitta (si toglie limando)')


def dnode(cx, cy, w, h, lines, col=ACC2, fill='#fff', size=13.5):
    s = '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="2"/>' % (
        cx, cy - h / 2, cx + w / 2, cy, cx, cy + h / 2, cx - w / 2, cy, fill, col)
    return s + mtext(cx, cy - (len(lines) - 1) * size * 0.62 + size * 0.36, lines, size, weight=800, lh=1.25)


@figx('sistemi-scelta.svg')
def sistemi_scelta():
    b = title('Quale sistema? 4 domande')
    G = OK
    b += dnode(400, 100, 260, 70, ['Allergia o', 'controindicazioni?'])
    b += box(600, 74, 180, 52, ['Niente acrilati –', 'medico'], ERR_BG, ERR, 13.5, 800, ERR)
    b += arrow(530, 100, 596, 100) + text(562, 92, 'Sì', 13, weight=800, fill=ERR)
    b += arrow(400, 136, 400, 168) + text(412, 158, 'No', 13, 'start', 800, G)
    b += dnode(400, 204, 230, 66, ['Vuole', 'lunghezza?'])
    # ramo NO lunghezza
    b += arrow(285, 204, 230, 204) + text(258, 196, 'No', 13, weight=800, fill=G)
    b += dnode(150, 204, 150, 62, ['Solo colore?'])
    b += arrow(150, 236, 150, 286) + text(162, 266, 'Sì', 13, 'start', 800, G)
    b += box(70, 290, 160, 46, ['Semipermanente'], OK_BG, G, 14)
    b += arrow(75, 204, 46, 204, ACC2, 2) 
    b += '<path d="M46,204 L36,204 L36,380 L60,380" fill="none" stroke="%s" stroke-width="2.2" marker-end="url(#ar)"/>' % ACC2
    b += text(30, 300, 'No', 13, 'end', 800, ERR) if False else text(44, 298, 'No', 13, 'start', 800, ERR)
    b += box(64, 356, 200, 50, ['Soft gel / BIAB', '(rinforzo)'], OK_BG, G, 13.5)
    # ramo SI lunghezza
    b += arrow(400, 238, 400, 266) + text(412, 258, 'Sì', 13, 'start', 800, G)
    b += dnode(400, 302, 230, 66, ['Unghia sottile', 'o difficile?'])
    b += arrow(515, 302, 576, 302) + text(546, 294, 'Sì', 13, weight=800, fill=G)
    b += box(580, 272, 200, 62, ['Cartina + gel flessibile,', 'strati sottili'], OK_BG, G, 13)
    b += arrow(400, 336, 400, 366) + text(412, 358, 'No', 13, 'start', 800, G)
    for k, t in enumerate((['Hard gel'], ['Acrilico'], ['Polygel /', 'soft gel tips'])):
        bx = 296 + k * 130
        b += box(bx, 370, 118, 50, t, OK_BG, G, 13.5)
    b += '<rect x="20" y="436" width="760" height="34" rx="10" fill="#f1ecee"/>'
    b += text(400, 458, 'Poi: stesso sistema (stesso produttore) dalla base al top', 14.5, weight=800, fill=ACC2)
    return svg(800, 480, arrow_defs() + b, 'Albero decisionale per scegliere il sistema')


def chain(x, y, n=4, ang=0, col='#c2577a', seg=14):
    pts = []
    for k in range(n):
        a = math.radians(ang + (25 if k % 2 else -25))
        pts.append((x, y))
        x += math.cos(a) * seg
        y += math.sin(a) * seg
    pts.append((x, y))
    o = '<polyline points="%s" fill="none" stroke="%s" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>' % (
        ' '.join('%.1f,%.1f' % p for p in pts), col)
    o += ''.join('<circle cx="%.1f" cy="%.1f" r="3.2" fill="%s"/>' % (px, py, col) for px, py in pts)
    return o, pts


def star(cx, cy, r=7, col='#b9bec4', stroke='#8a9097'):
    pts = []
    for k in range(10):
        a = -math.pi / 2 + k * math.pi / 5
        rr = r if k % 2 == 0 else r * 0.45
        pts.append('%.1f,%.1f' % (cx + math.cos(a) * rr, cy + math.sin(a) * rr))
    return '<polygon points="%s" fill="%s" stroke="%s" stroke-width="1.2"/>' % (' '.join(pts), col, stroke)


def thermometer(x, y, s=1.0, col=ERR):
    return ('<g transform="translate(%.1f,%.1f) scale(%.2f)"><rect x="-5" y="-34" width="10" height="38" rx="5" fill="#fff" stroke="%s" stroke-width="1.8"/>'
            '<circle cy="8" r="9" fill="%s" stroke="%s" stroke-width="1.8"/><rect x="-2.5" y="-20" width="5" height="26" fill="%s"/></g>' % (x, y, s, GREY_D, col, GREY_D, col))


def flame(x, y, s=1.0):
    return ('<path d="M%.1f,%.1f q%.1f,%.1f %.1f,%.1f q%.1f,%.1f %.1f,%.1f q%.1f,%.1f %.1f,%.1f z" fill="#f28c38"/>' % (
        x, y, -10 * s, -12 * s, 0, -30 * s, 4 * s, 10 * s, 10 * s, 12 * s, 6 * s, 10 * s, -10 * s, 18 * s)
        + '<path d="M%.1f,%.1f q%.1f,%.1f 0,%.1f q%.1f,%.1f 0,%.1f z" fill="#f9d14a"/>' % (x, y - 2 * s, -5 * s, -6 * s, -14 * s, 6 * s, 7 * s, 14 * s))


@figx('gel-chimica.svg')
def gel_chimica():
    b = title('Come indurisce il gel')
    W = 232
    specs = [(20, 'Gel nel vasetto'), (264, 'In lampada'), (508, 'Gel indurito')]
    for i, (x, t) in enumerate(specs):
        b += frame(x, 56, W, 276, t, i + 1)
        if i < 2:
            starts = [(x + 34, 152, 10), (x + 120, 146, -15), (x + 40, 222, 5), (x + 130, 216, -8), (x + 80, 182, 20)]
            for k, (sx, sy, a) in enumerate(starts):
                o, _ = chain(sx, sy, 4, a, ['#c2577a', '#8e3b5a', '#d97a9a'][k % 3])
                b += o
            for k, (px, py) in enumerate(((x + 100, 168), (x + 186, 176), (x + 70, 256), (x + 184, 248), (x + 124, 268))):
                b += star(px, py, 8, '#f9d14a' if i == 1 else '#c8ccd1', '#c9a52a' if i == 1 else '#8a9097')
            if i == 1:
                b += chip(x + W / 2, 112, 'Luce 365–405 nm', UV, '#fff', 12)
                for k in range(5):
                    b += '<line x1="%d" y1="126" x2="%d" y2="142" stroke="%s" stroke-width="3" stroke-dasharray="5 4"/>' % (x + 30 + k * 44, x + 26 + k * 44, UV)
                for (ax, ay, bx2, by2) in ((x + 100, 168, x + 112, 152), (x + 186, 176, x + 170, 200), (x + 70, 256, x + 60, 234), (x + 184, 248, x + 172, 228)):
                    b += lightning((ax + bx2) / 2, (ay + by2) / 2, 0.8, '#f2a33a')
        else:
            b += network(x + 26, 116, 150, 140, 30, ACC2, '#f6d6df', 9, 0.18)
            b += thermometer(x + 196, 286, 0.9) + flame(x + 214, 296, 0.8)
        b += text(x + W / 2, 300, ['Catene corte separate', 'Le catene si collegano', 'Una rete solida'][i], 13.5, weight=700)
        b += text(x + W / 2, 320, ['interruttori spenti', 'i fotoiniziatori si accendono', 'la reazione scalda'][i], 12.5, weight=600, fill=MUTED)
        if i < 2:
            b += arrow(x + W + 1, 190, x + W + 11, 190)
    # legenda
    o, _ = chain(28, 356, 3, 0)
    b += o + text(80, 361, 'Oligomeri', 13, 'start', 700)
    b += star(188, 356, 8) + text(202, 361, 'Fotoiniziatori', 13, 'start', 700)
    b += '<line x1="330" y1="348" x2="326" y2="364" stroke="%s" stroke-width="3" stroke-dasharray="5 4"/>' % UV + text(340, 361, 'Luce UV/LED', 13, 'start', 700)
    b += '<circle cx="470" cy="356" r="4" fill="#f6d6df" stroke="%s"/><line x1="474" y1="356" x2="490" y2="356" stroke="%s" stroke-width="2"/>' % (ACC2, ACC2)
    b += text(498, 361, 'Rete solida', 13, 'start', 700)
    return svg(760, 380, arrow_defs() + b, 'Oligomeri e fotoiniziatori: la luce fa partire la reazione e si forma una rete')


def layered_side(x, y, w, layers):
    """Unghia di profilo (piatta) con strati di prodotto colorati, dal basso."""
    o = '<rect x="%.1f" y="%.1f" width="%.1f" height="30" rx="10" fill="%s" stroke="%s" stroke-width="1.5"/>' % (x - 10, y, w + 30, SKIN, SKIN_D)
    o += '<rect x="%.1f" y="%.1f" width="%.1f" height="5" fill="%s"/>' % (x, y - 5, w, NAIL_S)
    yy = y - 5
    for col, h in layers:
        o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="%s" stroke="%s" stroke-width="1"/>' % (x + 4, yy - h, w - 8, h, col, NAIL_S)
        yy -= h
    return o


@figx('gel-fasi.svg')
def gel_fasi():
    b = title('Trifasico, bifasico, monofasico')
    C1, C2, C3 = '#f9e0a8', '#f3b3c6', '#cfe6f7'
    cols = [('Trifasico', [('Base', C1), ('Costruttore', C2), ('Sigillante', C3)], [(C1, 8), (C2, 26), (C3, 8)]),
            ('Bifasico', [('Base + costruttore', C2), ('Sigillante', C3)], [(C2, 32), (C3, 8)]),
            ('Monofasico', [('Tutto in uno', '#e7b6e0')], [('#e7b6e0', 40)])]
    W = 232
    for i, (t, jars, layers) in enumerate(cols):
        x = 20 + i * (W + 12)
        b += frame(x, 56, W, 210, t)
        n = len(jars)
        for j, (lab, c) in enumerate(jars):
            jx = x + W / 2 + (j - (n - 1) / 2) * 72
            b += jar(jx, 140, 48, 32, c)
            for k, ln in enumerate(wrap(lab, 70, 12, True)):
                b += text(jx, 158 + k * 15, ln, 12, weight=700)
        b += layered_side(x + 46, 232, 140, layers)
    b += '<defs><linearGradient id="ctrl" x1="0" x2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>' % (OK, '#3f86b8')
    b += '<rect x="20" y="282" width="720" height="14" rx="7" fill="url(#ctrl)"/>'
    b += text(20, 318, '← Più controllo (consigliato per imparare)', 14, 'start', 800, OK)
    b += text(740, 318, 'Più velocità →', 14, 'end', 800, '#3f86b8')
    return svg(760, 334, b, 'Gel trifasico, bifasico e monofasico: prodotti e strati')


@figx('strato-dispersione.svg')
def strato_disp():
    b = title('Lo strato di dispersione')
    b += frame(20, 56, 420, 250, None)
    b += '<rect x="40" y="226" width="380" height="40" fill="%s"/>' % SKIN
    b += '<rect x="40" y="214" width="380" height="12" fill="%s" stroke="%s"/>' % (NAIL, NAIL_S)
    b += '<rect x="40" y="164" width="380" height="50" fill="%s" stroke="%s"/>' % (GEL, NAIL_S)
    b += '<rect x="40" y="150" width="380" height="14" fill="#f9d7e2"/>'
    b += ''.join('<circle cx="%d" cy="%d" r="2" fill="#fff"/>' % (48 + k * 12, 154 + (k % 3) * 4) for k in range(31))
    for k in range(6):
        ox = 70 + k * 60
        b += '<circle cx="%d" cy="102" r="9" fill="#e6f1f8" stroke="#3f86b8" stroke-width="1.8"/><circle cx="%d" cy="102" r="9" fill="#e6f1f8" stroke="#3f86b8" stroke-width="1.8"/>' % (ox, ox + 13)
        b += text(ox + 6, 104, 'O₂', 10.5 + 1.5, weight=800, fill='#3f86b8') if False else ''
        b += carrow(ox + 6, 113, ox + 6, 128, '#3f86b8', 1.6)
    b += text(420, 80, 'Ossigeno dell\'aria (O₂)', 13.5, 'end', 800, '#3f86b8')
    b += callout(300, 156, 300, 136, '', 1) if False else ''
    b += text(56, 146, 'Strato di dispersione (appiccicoso)', 13.5, 'start', 800, ACC2)
    b += text(230, 195, 'Gel polimerizzato', 14, weight=800, fill='#fff')
    b += text(230, 252, 'Unghia', 13, weight=700, fill=SKIN_D)
    b += text(230, 292, 'L\'ossigeno blocca la reazione solo in superficie', 13, weight=600, fill=MUTED)
    # vignette
    items = [(True, 'Tra uno strato e l\'altro:', 'lascialo (aiuta l\'aggancio)'), (True, 'Alla fine: cleaner,', 'una salvietta per ogni dito'),
             (False, 'Stessa salvietta su', 'tutte le dita')]
    for k, (ok, t1, t2) in enumerate(items):
        y = 56 + k * 86
        b += '<rect x="452" y="%d" width="288" height="78" rx="14" fill="%s"/>' % (y, OK_BG if ok else ERR_BG)
        b += mark(476, y + 26, ok, 12)
        b += text(496, y + 31, t1, 13.5, 'start', 800)
        b += text(496, y + 51, t2, 13.5, 'start', 600)
        if k == 1:
            b += ''.join('<rect x="%d" y="%d" width="16" height="12" rx="2" fill="#fff" stroke="%s"/>' % (640 + j * 20, y + 58, GREY) for j in range(5))
        if k == 2:
            b += '<rect x="680" y="%d" width="26" height="18" rx="3" fill="#f9d7e2" stroke="%s"/>' % (y + 50, ERR)
    return svg(760, 320, arrow_defs() + b, 'Strato di dispersione: patina appiccicosa dovuta all\'ossigeno; si toglie alla fine con una salvietta per dito')




def dappen(cx, base, w=60, h=40, liquid=0.5, lid=False):
    o = '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="#eef6fb" stroke="%s" stroke-width="2"/>' % (
        cx - w / 2, base - h, cx + w / 2, base - h, cx + w / 2 - 6, base, cx - w / 2 + 6, base, GREY_D)
    lh = h * liquid
    o += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="#cfe6f7" opacity=".9"/>' % (
        cx - w / 2 + 2 + 6 * (1 - liquid), base - lh, cx + w / 2 - 2 - 6 * (1 - liquid), base - lh, cx + w / 2 - 7, base - 2, cx - w / 2 + 7, base - 2)
    if lid:
        o += '<rect x="%.1f" y="%.1f" width="%.1f" height="10" rx="4" fill="%s"/>' % (cx - w / 2 - 4, base - h - 12, w + 8, ACC2)
    return o


def powder_jar(cx, base, w=70, h=44, col='#f6d6df', label=''):
    o = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="8" fill="#fff" stroke="%s" stroke-width="2"/>' % (cx - w / 2, base - h, w, h, GREY_D)
    o += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s"/>' % (
        cx - w / 2 + 3, base - h * 0.55, cx, base - h * 0.75, cx + w / 2 - 3, base - h * 0.55, cx + w / 2 - 3, base - 3, cx - w / 2 + 3, base - 3, col)
    if label:
        o += text(cx, base + 18, label, 12.5, weight=700)
    return o


@figx('acrilico-chimica.svg')
def acrilico_chimica():
    b = title('Acrilico: cosa c\'è nel liquido e nella polvere')
    # liquido
    b += frame(20, 56, 250, 262, 'Liquido – EMA')
    b += bottle(70, 250, 56, 120, '#e6f1f8', 'EMA', 13)
    items_l = ['Monomero EMA', 'Accelerante', 'Inibitore (tracce)', 'Reticolante']
    for k, t in enumerate(items_l):
        b += '<circle cx="118" cy="%d" r="4" fill="#3f86b8"/>' % (130 + k * 30)
        b += text(128, 135 + k * 30, t, 13.5, 'start', 700)
    # polvere
    b += frame(490, 56, 250, 262, 'Polvere – PMMA')
    b += powder_jar(546, 250, 76, 56, '#f6d6df')
    items_p = ['Perline di PMMA', 'Iniziatore BPO', 'Pigmenti']
    for k, t in enumerate(items_p):
        b += '<circle cx="600" cy="%d" r="4" fill="%s"/>' % (130 + k * 30, ACC)
        b += text(610, 135 + k * 30, t, 13.5, 'start', 700)
    b += ''.join('<circle cx="%d" cy="%d" r="4" fill="#fff" stroke="%s"/>' % (530 + (k % 4) * 10, 222 + (k // 4) * 9, ACC) for k in range(8))
    # centro
    b += tool_brush(400, 164, -28, 90, '#e9d6c0')
    b += bead(370, 182, 20, '#f9e3ea')
    b += carrow(290, 170, 340, 182, '#3f86b8', 2) + carrow(486, 200, 398, 190, ACC, 2)
    b += mtext(380, 236, ['Reazione all\'aria:', 'indurisce in pochi minuti'], 14, weight=800, fill=ACC2)
    b += text(380, 284, 'senza lampada', 13, weight=600, fill=MUTED)
    b += '<rect x="20" y="330" width="355" height="40" rx="12" fill="%s"/>' % ERR_BG
    b += mark(44, 350, False, 11) + text(62, 355, 'Non mescolare marche diverse', 14.5, 'start', 800, ERR)
    b += '<rect x="385" y="330" width="355" height="40" rx="12" fill="%s"/>' % ERR_BG
    b += mark(409, 350, False, 11) + text(427, 355, 'Mai liquido MMA; niente DMTA', 14.5, 'start', 800, ERR)
    return svg(760, 384, arrow_defs() + b, 'Composizione del liquido (EMA) e della polvere (PMMA con BPO) dell\'acrilico')


@figx('acrilico-dappen.svg')
def acrilico_dappen():
    labs = ['Poco liquido, coperchio', 'Immergi', 'Scarica l\'eccesso', 'Raccogli la perla (1–2 s)']
    b = title('La perla di acrilico in 4 gesti')
    W = 172
    for i, lab in enumerate(labs):
        x = 20 + i * (W + 10)
        b += frame(x, 56, W, 230, None)
        b += badge(x + 24, 80, i + 1, ACC, 13)
        cx = x + W / 2
        if i == 0:
            b += dappen(cx, 200, 70, 46, 0.45, lid=True)
            b += bottle(cx + 52, 200, 26, 54, '#e6f1f8') + '<rect x="%.1f" y="%.1f" width="20" height="8" rx="3" fill="%s"/>' % (cx + 42, 128, ACC2)
        elif i == 1:
            b += dappen(cx, 210, 70, 46, 0.5)
            b += tool_brush(cx + 4, 182, -100, 90, '#e9d6c0')
        elif i == 2:
            b += dappen(cx, 210, 70, 46, 0.5)
            b += tool_brush(cx + 30, 160, -125, 90, '#e9d6c0')
            b += drop_icon(cx + 28, 186, 0.45, '#9cc7e0')
            b += carrow(cx + 40, 150, cx + 40, 172, ACC2, 1.8) if False else ''
        else:
            b += powder_jar(cx, 214, 96, 50, '#f6d6df')
            b += tool_brush(cx + 34, 152, -150, 90, '#e9d6c0')
            b += bead(cx + 2, 172, 12, '#fbeef2')
        b += mtext(cx, 256, wrap(lab, W - 20, 13.5, True), 13.5, weight=800)
    return svg(760, 300, arrow_defs() + b, 'Dappen dish, pennello e polvere: immergi, scarica, raccogli la perla')


@figx('polygel-step.svg')
def polygel_step():
    labs = ['Preleva', 'Taglia', 'Appoggia', 'Modella (poca slip)', 'Polimerizza']
    b = title('Polygel in 5 passi')
    W = 144
    PG = '#f3c1cf'
    for i, lab in enumerate(labs):
        x = 20 + i * (W + 10)
        b += frame(x, 56, W, 228, None)
        b += badge(x + 22, 78, i + 1, ACC, 13)
        cx = x + W / 2
        if i == 0:
            b += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="#f6d6df" stroke="%s" stroke-width="2"/>' % (cx - 40, 130, cx + 30, 130, cx + 40, 170, cx - 50, 170, NAIL_S)
            b += '<rect x="%.1f" y="%.1f" width="16" height="22" rx="3" fill="%s"/>' % (cx + 38, 139, ACC2)
            b += '<path d="M%.1f,%.1f q-14,4 -22,18 q16,4 22,-6 z" fill="%s" stroke="%s"/>' % (cx - 50, 154, PG, NAIL_S)
            b += '<rect x="%.1f" y="196" width="80" height="10" rx="5" fill="%s" transform="rotate(-15 %.1f 201)"/>' % (cx - 40, METAL, cx)
        elif i == 1:
            b += '<rect x="%.1f" y="166" width="70" height="20" rx="10" fill="%s" stroke="%s"/>' % (cx - 40, PG, NAIL_S)
            b += '<rect x="%.1f" y="130" width="8" height="70" rx="3" fill="%s" transform="rotate(10 %.1f 165)"/>' % (cx + 4, METAL, cx + 8)
            b += '<line x1="%.1f" y1="160" x2="%.1f" y2="192" stroke="%s" stroke-width="2" stroke-dasharray="3 3"/>' % (cx + 8, cx + 8, ACC2)
        elif i in (2, 3):
            ex = ''
            f, p = finger_nail(cx, 222, hw=30, nail_len=80, free_len=8, shape='squoval', finger_len=30, lunula=False)
            b += f
            if i == 2:
                b += '<ellipse cx="%.1f" cy="%.1f" rx="16" ry="10" fill="%s" stroke="%s"/>' % (cx, 170, PG, NAIL_S)
            else:
                b += '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s" opacity=".9" stroke="%s"/>' % (
                    cx - 24, 200, cx - 24, 140, cx, 128, cx + 24, 140, cx + 24, 200, PG, NAIL_S)
                b += tool_brush(cx + 34, 130, -40, 60, '#f1e3a0')
                b += drop_icon(cx + 44, 112, 0.4, '#9cc7e0')
        else:
            b += lamp(cx, 210, 110, 'UV/LED')
            b += '<rect x="%.1f" y="186" width="54" height="22" rx="10" fill="%s" stroke="%s"/>' % (cx - 27, SKIN, SKIN_D)
        b += mtext(cx, 256, wrap(lab, W - 16, 13.5, True), 13.5, weight=800)
    return svg(800, 296, b, 'Polygel: preleva, taglia, appoggia, modella con poca slip solution, polimerizza')


@figx('fibra-riparazione.svg')
def fibra_rip():
    b = title('Riparare una crepa con la fibra')
    labs = ['Crepa', 'Toppa più grande della crepa', 'Resina + attivatore, poi lima']
    W = 196
    for i, lab in enumerate(labs):
        x = 20 + i * (W + 10)
        b += frame(x, 56, W, 250, lab if len(lab) < 8 else None, i + 1 if len(lab) < 8 else None)
        if len(lab) >= 8:
            b += badge(x + 24, 80, i + 1, ACC, 13)
        cx = x + W / 2
        ex = ''
        if i >= 1:
            ex = ('<g clip-path="url(#CLIP)"><rect x="%.1f" y="60" width="%.1f" height="70" fill="url(#mesh)" stroke="%s" stroke-width="1.2" stroke-dasharray="4 3"/></g>' % (
                cx - 30, 60, '#9a8f7a')) if i == 1 else ('<g clip-path="url(#CLIP)"><rect x="%.1f" y="60" width="%.1f" height="70" fill="#ffffff" opacity=".55"/></g>' % (cx - 30, 60))
        f, p = finger_nail(cx, 260, hw=44, nail_len=130, free_len=30, shape='squoval', finger_len=40, lunula=False, extra=ex)
        b += f
        b += '<path d="M%.1f,%.1f l8,8 l-8,8 l8,8 l-6,8" fill="none" stroke="%s" stroke-width="2.6" stroke-linejoin="round"/>' % (cx + 26, 104, ERR if i < 2 else '#d99aa5')
        if i == 1:
            b += callout(cx + 30, 96, cx + 56, 230, '2–3 mm oltre', 12.5, 700, ACC2)
        if i == 2:
            b += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" opacity=".9"/>' % (cx - 20, 200, cx - 24, 140, cx - 14, 96)
            b += tool_file(cx + 56, 160, -70, 90, 14)
        b += mtext(cx, 290, [lab] if len(lab) < 8 else wrap(lab, W - 20, 13, True), 13, weight=700) if len(lab) >= 8 else ''
    b += '<defs><pattern id="mesh" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="6" height="6" fill="#fffaf0"/><path d="M0,0 L6,0 M0,0 L0,6" stroke="#cbbf9f" stroke-width="1"/></pattern></defs>'
    b += '<rect x="638" y="56" width="102" height="250" rx="16" fill="%s"/>' % WARN_BG
    b += mtext(689, 120, ['Attivatore:', 'poco', 'e da', 'lontano'], 14, weight=800, fill=WARN)
    b += mtext(689, 220, ['a 1 mm da', 'cuticola', 'e lati'], 13, weight=700)
    return svg(760, 320, b, 'Riparazione di una crepa con la fibra: la toppa supera la crepa di qualche millimetro')


# ----------------------------------------------------------------- lampade e documenti (completamento modulo 3)
def spectrum(x0, x1, base, curves, band=(350, 415), h=70):
    """Mini grafico spettro 300–450 nm con zona del fotoiniziatore evidenziata."""
    def X(nm):
        return x0 + (nm - 300) / 150.0 * (x1 - x0)
    o = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#f8dfe7"/>' % (X(band[0]), base - h - 6, X(band[1]) - X(band[0]), h + 6)
    o += text((X(band[0]) + X(band[1])) / 2, base - h + 8, 'zona del gel', 12, weight=700, fill=ACC2)
    for peak, sd, hh, col in curves:
        pts = ['%.1f,%.1f' % (X(nm), base - hh * math.exp(-((nm - peak) ** 2) / (2 * sd * sd))) for nm in range(300, 451, 2)]
        o += '<polyline points="%s" fill="none" stroke="%s" stroke-width="3"/>' % (' '.join(pts), col)
    o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.5"/>' % (x0, base, x1, base, INK)
    for nm in (300, 350, 400, 450):
        o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s"/>' % (X(nm), base, X(nm), base + 5, INK)
        o += text(X(nm), base + 19, str(nm) + (' nm' if nm == 450 else ''), 12, 'middle' if nm < 450 else 'end', 400, MUTED)
    return o


@figx('lampada-watt-vs-nm.svg')
def lampada_watt():
    b = title('Watt o lunghezza d\'onda?')
    data = [(20, 'Lampada potente, luce sbagliata', 150, '36 W', [(432, 7, 62, '#3f6fe0')], False, 'Gel sotto-polimerizzato'),
            (390, 'Lampada piccola, luce giusta', 96, '9 W', [(365, 6, 58, UV), (405, 6, 58, UV)], True, 'Polimerizza bene')]
    for x, ttl, lw, watt, curves, ok, res in data:
        b += frame(x, 56, 350, 270, ttl, ok=ok, bw=2.5, border=OK if ok else ERR)
        cx = x + 120
        b += lamp(cx, 158, lw)
        b += text(x + 250, 128, watt, 30, weight=900, fill=INK)
        b += text(x + 250, 148, 'potenza', 12, weight=600, fill=MUTED)
        b += spectrum(x + 34, x + 316, 260, curves)
        b += mark(x + 92, 300, ok, 11) + text(x + 110, 305, res, 15, 'start', 800, OK if ok else ERR)
    b += '<rect x="20" y="336" width="720" height="34" rx="10" fill="%s"/>' % BLUE_BG
    b += text(380, 358, 'Conta la luce giusta che arriva sull\'unghia, non i watt', 15, weight=800, fill=ACC2)
    return svg(760, 380, b, 'Una lampada da 36 W con spettro che non coincide con il gel polimerizza male; una da 9 W con lo spettro giusto polimerizza bene')


def fingerless(cx, cy, s=1.0):
    """Mano (dorso) con guanto senza dita: copre dorso e base delle dita, unghie scoperte."""
    col, st = '#4b3a40', '#2c2024'
    o = hand_back(cx, cy, s)
    g = ''
    for fx, L, r, a in HAND_FINGERS:
        tx, ty = fx + a * 2.2, -46 - L
        mx, my = fx + (tx - fx) * 0.38, -46 + (ty + 46) * 0.38
        g += '<line x1="%.1f" y1="-40" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.1f"/>' % (fx, mx, my, st, 2 * r + 5)
        g += '<line x1="%.1f" y1="-40" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.1f"/>' % (fx, mx, my, col, 2 * r + 2)
    g += '<line x1="-62" y1="40" x2="-92" y2="9" stroke="%s" stroke-width="38"/><line x1="-62" y1="40" x2="-92" y2="9" stroke="%s" stroke-width="35"/>' % (st, col)
    g += ('<path d="M-72,-60 Q-72,-76 -50,-76 L62,-76 Q82,-76 82,-56 L78,64 Q74,104 36,106 L-34,106 Q-68,102 -72,66 Z" fill="%s" stroke="%s" stroke-width="1.6"/>' % (col, st))
    g += '<rect x="-42" y="100" width="84" height="40" fill="%s"/><rect x="-42" y="128" width="84" height="12" fill="#6b5a60"/>' % col
    g += '<path d="M-30,-20 Q10,-34 50,-22" stroke="#6b5a60" stroke-width="3" fill="none"/>'
    return o + '<g transform="translate(%.1f,%.1f) scale(%.2f)">%s</g>' % (cx, cy, s, g)


@figx('lampada-protezione.svg')
def lampada_prot():
    b = title('Proteggere la pelle dalla lampada (facoltativo)')
    for i, (x, ttl) in enumerate([(20, 'Crema solare sul dorso'), (390, 'Guanti senza dita')]):
        b += frame(x, 56, 350, 200, ttl, num=i + 1)
    # 1 crema
    b += hand_back(150, 172, 0.45)
    for (px, py, rx) in ((140, 165, 16), (160, 180, 12), (132, 185, 9)):
        b += '<ellipse cx="%d" cy="%d" rx="%d" ry="%d" fill="#ffffff" opacity=".9" stroke="#e8dcd4"/>' % (px, py, rx, rx * 0.6)
    b += ('<g transform="translate(280,170) rotate(-25)"><rect x="-20" y="-50" width="40" height="86" rx="8" fill="#f6c84a" stroke="%s" stroke-width="1.8"/>'
          '<rect x="-12" y="36" width="24" height="14" rx="3" fill="%s"/></g>' % (WARN, INK))
    b += text(276, 172, 'SPF', 14, weight=900, fill=INK).replace('<text ', '<text transform="rotate(-25 276 168)" ')
    b += text(276, 192, '50', 14, weight=800, fill=INK).replace('<text ', '<text transform="rotate(-25 276 168)" ')
    # 2 guanto
    b += fingerless(520, 172, 0.45)
    b += callout(560, 108, 650, 130, 'unghie scoperte', 13, 700, ACC2)
    b += callout(540, 190, 650, 200, 'anti-UV', 13, 700, ACC2)
    b += '<rect x="20" y="266" width="720" height="26" rx="10" fill="%s"/>' % OK_BG
    b += text(380, 284, 'Rischio basso: protezione facoltativa per chi la desidera', 14, weight=700, fill=OK)
    return svg(760, 300, b, 'Protezione facoltativa dalla lampada: crema solare sul dorso della mano o guanti senza dita anti-UV')


def ghs(cx, cy, r=14, kind='excl'):
    """Pittogramma di pericolo: rombo bianco bordato di rosso."""
    o = '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="#fff" stroke="#d42a2a" stroke-width="%.1f" stroke-linejoin="round"/>' % (
        cx, cy - r, cx + r, cy, cx, cy + r, cx - r, cy, max(2, r * 0.16))
    if kind == 'excl':
        o += text(cx, cy + r * 0.42, '!', r * 1.15, weight=900, fill=INK)
    else:
        o += ('<path d="M%.1f,%.1f q%.1f,%.1f 0,%.1f q%.1f,%.1f 0,%.1f z" fill="%s"/>'
              % (cx, cy + r * 0.5, -r * 0.45, -r * 0.35, -r * 0.95, r * 0.45, r * 0.4, r * 0.95, INK))
        o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6"/>' % (cx - r * 0.4, cy + r * 0.56, cx + r * 0.4, cy + r * 0.56, INK)
    return o


@figx('tre-documenti.svg')
def tre_documenti():
    b = title('Tre documenti per ogni prodotto')
    cols = [('ETICHETTA', 'INCI, avvertenze, lotto, PAO', ACC),
            ('SCHEDA TECNICA', 'lampada, tempi, ordine', '#3f86b8'),
            ('SDS', 'rischi, DPI, conservazione, smaltimento', ERR)]
    W = 236
    for k, (t, sub, c) in enumerate(cols):
        x = 20 + k * (W + 6)
        cx = x + W / 2
        b += '<rect x="%d" y="56" width="%d" height="276" rx="14" fill="%s"/>' % (x, W, PANEL)
        b += badge(x + 24, 80, k + 1, c)
        if k == 0:
            b += '<rect x="%.1f" y="104" width="96" height="150" rx="16" fill="#f6d6df" stroke="%s" stroke-width="2"/>' % (cx - 48, NAIL_S)
            b += '<rect x="%.1f" y="74" width="50" height="34" rx="6" fill="%s"/>' % (cx - 25, INK)
            b += '<rect x="%.1f" y="130" width="76" height="104" rx="5" fill="#fff"/>' % (cx - 38)
            b += text(cx, 148, 'INCI', 12, weight=800, fill=ACC2)
            for j in range(3):
                b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#c8ced4" stroke-width="2.5" stroke-linecap="round"/>' % (cx - 30, 160 + j * 9, cx + 28 - j * 8, 160 + j * 9)
            b += warn_tri(cx - 20, 204, 11) + pao(cx + 18, 200, '12M', 1.0)
            b += text(cx, 228, 'LOT 24A', 12, weight=700, fill=MUTED)
        elif k == 1:
            b += doc(cx - 62, 76, 124, 170, lines=0)
            b += text(cx - 50, 100, 'Gel Builder', 12, 'start', 800, ACC2)
            for r in range(2):
                for c2 in range(2):
                    b += '<rect x="%.1f" y="%.1f" width="%d" height="20" fill="%s" stroke="#c8ced4"/>' % (cx - 50 + c2 * 52, 112 + r * 22, 52, '#fff')
            b += text(cx - 24, 126, 'LED', 12, weight=700) + text(cx + 28, 126, '60 s', 12, weight=700)
            b += text(cx - 24, 148, 'UV', 12, weight=700) + text(cx + 28, 148, '120 s', 12, weight=700)
            b += ('<path d="M%.1f,232 L%.1f,206 Q%.1f,186 %.1f,206 L%.1f,232 Z" fill="#f4f1f8" stroke="#8a7d9e" stroke-width="2"/>'
                  '<rect x="%.1f" y="232" width="58" height="6" rx="3" fill="#8a7d9e"/>' % (cx - 50, cx - 50, cx - 24, cx + 2, cx + 2, cx - 53))
            for j, st in enumerate(['1 base', '2 colore', '3 top']):
                b += text(cx + 12, 182 + j * 20, st, 12, 'start', 700, ACC2)
        else:
            b += doc(cx - 62, 76, 124, 170, lines=0)
            for j in range(16):
                yy = 92 + j * 9.4
                b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#c8ced4" stroke-width="3" stroke-linecap="round"/>' % (cx - 34, yy, cx + 6 - (j % 3) * 8, yy)
                b += '<circle cx="%.1f" cy="%.1f" r="3" fill="%s"/>' % (cx - 46, yy, ERR if j in (1, 3, 6, 7, 12) else GREY)
            b += ghs(cx + 36, 120, 15, 'excl') + ghs(cx + 36, 160, 15, 'fire')
        b += text(cx, 278, t, 16, weight=900, fill=c)
        b += mtext(cx, 300, wrap(sub, W - 30, 13, True), 13, weight=700)
    return svg(760, 340, b, 'Etichetta, scheda tecnica e scheda di sicurezza (SDS): che cosa contiene ciascuna')


def cabinet(cx, cy, s=1.0):
    return ('<g transform="translate(%.1f,%.1f) scale(%.2f)"><rect x="-16" y="-20" width="32" height="40" rx="3" fill="#eef1f4" stroke="%s" stroke-width="2"/>'
            '<line x1="0" y1="-20" x2="0" y2="20" stroke="%s" stroke-width="2"/><circle cx="-4" cy="0" r="1.8" fill="%s"/><circle cx="4" cy="0" r="1.8" fill="%s"/>'
            '<line x1="-16" y1="20" x2="-16" y2="24" stroke="%s" stroke-width="2"/><line x1="16" y1="20" x2="16" y2="24" stroke="%s" stroke-width="2"/></g>'
            % (cx, cy, s, GREY_D, GREY_D, GREY_D, GREY_D, GREY_D, GREY_D))


def first_aid(cx, cy, r=16):
    return ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="5" fill="%s"/>' % (cx - r, cy - r, 2 * r, 2 * r, OK)
            + '<path d="M%.1f,%.1f h%.1f M%.1f,%.1f v%.1f" stroke="#fff" stroke-width="%.1f"/>' % (cx - r * 0.6, cy, r * 1.2, cx, cy - r * 0.6, r * 1.2, r * 0.38))


@figx('sds-sezioni.svg')
def sds_sezioni():
    b = title('La scheda di sicurezza (SDS): le 5 sezioni da leggere')
    X, Y, Wd, rh = 40, 66, 270, 20.5
    b += doc(X, Y, Wd, 16 * rh + 22, lines=0)
    hi = {2: ('Pericoli', 'pittogrammi e frasi di rischio'), 4: ('Primo soccorso', 'cosa fare se tocca occhi o pelle'),
          7: ('Conservazione', 'dove e come tenerlo'), 8: ('Protezione (DPI)', 'guanti, occhiali, mascherina'),
          13: ('Smaltimento', 'residui, salviette e flaconi')}
    ly = {2: 92, 4: 168, 7: 244, 8: 320, 13: 396}
    for n in range(1, 17):
        yy = Y + 14 + (n - 1) * rh
        on = n in hi
        if on:
            b += '<rect x="%d" y="%.1f" width="%d" height="%.1f" rx="4" fill="%s" opacity=".9"/>' % (X + 6, yy - 1, Wd - 12, rh - 2, '#f6d6df')
        b += text(X + 22, yy + 14, str(n), 12, weight=800, fill=ACC2 if on else MUTED)
        b += '<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="3" stroke-linecap="round"/>' % (
            X + 40, yy + 9, X + Wd - 30 - (n % 4) * 18, yy + 9, ACC if on else '#d5dadf')
        if on:
            b += '<path d="M%d,%.1f C%d,%.1f %d,%d %d,%d" fill="none" stroke="%s" stroke-width="1.8"/>' % (
                X + Wd - 8, yy + 9, X + Wd + 40, yy + 9, X + Wd + 40, ly[n] - 6, 382, ly[n] - 6, ACC)
            b += '<circle cx="%d" cy="%.1f" r="3.5" fill="%s"/>' % (X + Wd - 8, yy + 9, ACC2)
    for n, (t, sub) in hi.items():
        y = ly[n]
        b += '<rect x="384" y="%d" width="356" height="62" rx="12" fill="%s"/>' % (y - 32, PANEL)
        ix = 420
        if n == 2:
            b += ghs(ix, y - 1, 18)
        elif n == 4:
            b += first_aid(ix, y - 1, 16)
        elif n == 7:
            b += cabinet(ix, y - 3, 0.95)
        elif n == 8:
            b += glove(ix - 6, y + 2, 0.5) + glasses(ix + 10, y + 8, 0.36)
        else:
            b += trash(ix, y + 20, 30, 34)
        b += text(452, y - 6, 'Sez. %d – %s' % (n, t), 15, 'start', 800, ACC2)
        b += text(452, y + 14, sub, 13, 'start', 600)
    return svg(760, 440, b, 'Scheda di dati di sicurezza a 16 sezioni: evidenziate pericoli, primo soccorso, conservazione, DPI e smaltimento')


def finger_down(cx, tip_y, s=1.0, flen=90, free_len=12):
    f, p = finger_nail(0, 0, hw=30, nail_len=70, free_len=free_len, shape='squoval', smile=6, finger_len=flen, lunula=False)
    return '<g transform="translate(%.1f,%.1f) scale(%.2f) rotate(180) translate(0,%d)">%s</g>' % (cx, tip_y, s, 70 + free_len, f)


def spoon(x, y, ang=0, s=1.0, powder=True):
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f) scale(%.2f)"><rect x="12" y="-3" width="80" height="6" rx="3" fill="%s" stroke="%s"/>'
            '<ellipse cx="0" cy="0" rx="16" ry="11" fill="%s" stroke="%s" stroke-width="1.6"/>%s</g>'
            % (x, y, ang, s, METAL, METAL_D, METAL, METAL_D, '<ellipse cx="0" cy="-2" rx="11" ry="6" fill="#f6d6df"/>' if powder else ''))


@figx('dip-versare.svg')
def dip_versare():
    b = title('Polveri dip: come si usano in modo igienico')
    b += frame(20, 56, 350, 270, 'Corretto', ok=True, border=OK)
    b += frame(390, 56, 350, 270, 'Errato', ok=False, border=ERR)
    # corretto: ciotolina monouso sotto il dito, cucchiaino che versa
    b += '<path d="M120,230 L220,230 L208,262 L132,262 Z" fill="#fff" stroke="%s" stroke-width="2"/>' % GREY_D
    b += '<path d="M126,236 Q170,226 214,236 L208,258 L132,258 Z" fill="#f6d6df"/>'
    b += finger_down(170, 222, 0.62, 80)
    b += spoon(258, 150, 150, 1.0)
    import random as _r
    rnd = _r.Random(3)
    for k in range(16):
        px = 244 - k * 2.6 + rnd.uniform(-5, 5)
        py = 164 + k * 3.8 + rnd.uniform(-3, 3)
        b += '<circle cx="%.1f" cy="%.1f" r="2" fill="#e48fa9"/>' % (px, py)
    b += text(286, 236, 'monouso', 12, 'start', 700, MUTED)
    b += mtext(195, 290, ['Versa con cucchiaino pulito,', 'l\'avanzo va nel cestino'], 14, weight=700, fill=OK)
    # errato: dito nel barattolo comune
    b += '<rect x="505" y="170" width="120" height="96" rx="10" fill="#fff" stroke="%s" stroke-width="2"/>' % GREY_D
    b += '<rect x="508" y="200" width="114" height="63" rx="8" fill="#f6d6df"/>'
    b += finger_down(565, 222, 0.62, 80)
    b += '<rect x="505" y="170" width="120" height="96" rx="10" fill="#ffffff" opacity=".35"/>'
    b += '<rect x="500" y="160" width="130" height="12" rx="4" fill="#d9dee3" stroke="%s"/>' % GREY_D
    for (gx, gy) in ((610, 214), (520, 224), (598, 244), (532, 252)):
        b += germ(gx, gy, 4.5, '#6f7983')
    b += text(640, 228, 'comune', 12, 'start', 700, MUTED)
    b += no_sign(470, 120, 20)
    b += text(565, 290, 'Mai il dito nel barattolo comune', 14, weight=700, fill=ERR)
    return svg(760, 340, b, 'Polveri dip: versare con un cucchiaino pulito in una ciotolina monouso, mai immergere il dito nel barattolo comune')


@figx('press-on-step.svg')
def press_on():
    labels = ['Misura', 'Prepara', 'Incolla', 'Premi']

    def draw(i, x, y):
        cx = x + 89
        o = ''
        if i == 0:
            for k, (w, n) in enumerate(((30, '2'), (26, '4'), (23, '6'), (20, '8'), (17, '9'))):
                px = x + 22 + k * 33
                o += '<path d="M%.1f,170 L%.1f,128 Q%.1f,112 %.1f,112 Q%.1f,112 %.1f,128 L%.1f,170 Z" fill="%s" stroke="%s" stroke-width="1.5"/>' % (
                    px, px, px, px + w / 2, px + w, px + w, px + w, NAIL, NAIL_S)
                o += text(px + w / 2, 190, n, 13, weight=800, fill=ACC2)
            o += text(cx, 222, 'una misura per dito', 12.5, weight=600, fill=MUTED)
        else:
            f, p = finger_nail(cx, 210, hw=28, nail_len=64, free_len=6 if i < 3 else 22, shape='squoval', finger_len=40, lunula=False,
                               plate=NAIL if i < 3 else '#d65d86', free=FREE if i < 3 else '#d65d86')
            o += f
            if i == 1:
                o += tool_file(cx + 18, 150, -20, 110, 14, '#b9aa9c', '#e6dbd0')
                o += text(cx, 252, 'lima fine, poi sgrassa', 12.5, weight=600, fill=MUTED)
            elif i == 2:
                o += drop_icon(cx, 154, 0.9, '#f1d27a')
                o += ('<g transform="translate(%.1f,178) rotate(-35)"><rect x="-8" y="-40" width="16" height="44" rx="4" fill="#fff" stroke="%s" stroke-width="1.6"/>'
                      '<path d="M-4,-40 L0,-54 L4,-40 Z" fill="%s"/></g>' % (cx + 54, GREY_D, GREY_D))
                o += text(cx, 252, 'colla o linguetta', 12.5, weight=600, fill=MUTED)
            else:
                o += '<ellipse cx="%.1f" cy="132" rx="32" ry="20" fill="%s" stroke="%s" stroke-width="1.6"/>' % (cx, SKIN, SKIN_D)
                o += arrow(cx - 50, 116, cx - 50, 146)
                o += stopwatch(cx + 58, 200, 16)
                o += text(cx, 252, 'qualche secondo', 12.5, weight=600, fill=MUTED)
        return o
    return steps_fig('Press-on in 4 passaggi', labels, 4, 179, 200, draw,
                     'Applicazione delle press-on: scegliere la misura, preparare la lamina, incollare, premere')


def file_shape(kind, cx, cy, col='#b9aa9c', col2='#e6dbd0'):
    if kind == 'dritta':
        return '<rect x="%.1f" y="%.1f" width="130" height="20" rx="10" fill="%s"/><rect x="%.1f" y="%.1f" width="130" height="10" rx="5" fill="%s"/>' % (
            cx - 65, cy - 10, col, cx - 65, cy, col2)
    if kind == 'banana':
        return ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.2"/>'
                % (cx - 64, cy - 4, cx, cy - 34, cx + 64, cy - 4, cx + 62, cy + 14, cx, cy - 14, cx - 62, cy + 14, col, '#8a7d74'))
    if kind == 'mezzaluna':
        return ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.2"/>'
                % (cx - 64, cy + 8, cx, cy - 40, cx + 64, cy + 8, cx, cy - 4, cx - 64, cy + 8, col, '#8a7d74'))
    if kind == 'ovale':
        return '<ellipse cx="%.1f" cy="%.1f" rx="64" ry="14" fill="%s" stroke="%s" stroke-width="1.2"/>' % (cx, cy, col, '#8a7d74')
    return ('<path d="M%.1f,%.1f l10,-10 h96 l-10,10 Z" fill="%s" stroke="#bfa9b1"/><rect x="%.1f" y="%.1f" width="96" height="26" fill="%s" stroke="#bfa9b1"/>'
            '<path d="M%.1f,%.1f l10,-10 v26 l-10,10 Z" fill="#e2cfd6" stroke="#bfa9b1"/>' % (cx - 53, cy - 8, '#f4e6ea', cx - 53, cy - 8, '#f9eef1', cx + 43, cy - 8))


@figx('lime-forme-anime.svg')
def lime_forme():
    b = title('Lime: forme e anima')
    items = [('dritta', 'Dritta', '100/180', 'lati paralleli'), ('banana', 'Banana', '180/240', 'zona cuticolare'),
             ('mezzaluna', 'Mezzaluna', '240', 'curve e punta'), ('ovale', 'Ovale', '180/240', 'uso generale'),
             ('buffer', 'Buffer a blocco', '180/400', 'leviga e lucida')]
    cols = [('#b9aa9c', '#e6dbd0'), ('#d98aa5', '#f3c9d6'), ('#8fb5cf', '#d1e5f2'), ('#a7a0c9', '#ddd8f0'), ('', '')]
    for k, (kd, name, g, use) in enumerate(items):
        cx = 92 + k * 154
        b += file_shape(kd, cx, 104, cols[k][0] or '#b9aa9c', cols[k][1] or '#e6dbd0')
        b += text(cx, 154, name, 15, weight=800)
        b += chip(cx, 178, g, ACC2, '#fff', 12.5)
        b += text(cx, 206, use, 13, weight=600, fill=MUTED)
    # sezioni
    b += frame(20, 222, 360, 128, 'Anima rigida (legno/plastica)', border=None)
    b += '<rect x="70" y="290" width="260" height="22" rx="3" fill="#c9a87a" stroke="#8a6a3f" stroke-width="1.5"/>'
    for yy in (286, 312):
        b += '<rect x="70" y="%d" width="260" height="4" fill="#5d4a3d"/>' % yy
    b += text(200, 340, 'non si piega: lati dritti e forma', 13, weight=600, fill=MUTED)
    b += frame(400, 222, 340, 128, 'Anima morbida (spugna)', border=None)
    # unghia curva sotto e lima che si piega
    b += '<path d="M450,322 Q570,280 690,322" fill="none" stroke="%s" stroke-width="7" stroke-linecap="round"/>' % NAIL_S
    b += '<path d="M450,310 Q570,268 690,310 L690,294 Q570,250 450,294 Z" fill="#f2e6a8" stroke="#c9b45a" stroke-width="1.5"/>'
    b += '<path d="M450,313 Q570,271 690,313" fill="none" stroke="#5d4a3d" stroke-width="4"/>'
    b += '<path d="M450,292 Q570,248 690,292" fill="none" stroke="#5d4a3d" stroke-width="4"/>'
    b += text(570, 344, 'segue la curva: superficie e buffer', 13, weight=600, fill=MUTED)
    return svg(800, 360, b, 'Forme delle lime (dritta, banana, mezzaluna, ovale, buffer) e differenza tra anima rigida e anima morbida')


def spray(cx, base, s=1.0, col='#dfe9f2'):
    return ('<g transform="translate(%.1f,%.1f) scale(%.2f)"><rect x="-14" y="-50" width="28" height="50" rx="6" fill="%s" stroke="%s" stroke-width="1.8"/>'
            '<rect x="-7" y="-62" width="14" height="13" fill="%s"/><path d="M-7,-62 L12,-62 L12,-56 L-7,-56 Z" fill="%s"/><path d="M-4,-56 L-10,-44" stroke="%s" stroke-width="3"/>'
            '<path d="M16,-60 l10,-6 M16,-58 l12,0 M16,-56 l10,6" stroke="%s" stroke-width="1.6"/></g>'
            % (cx, base, s, col, GREY_D, INK, INK, INK, PROD_S))


@figx('lime-igiene.svg')
def lime_igiene():
    b = title('Lime e igiene: dipende dal materiale')
    cols = [('Porosa → monouso', 'nel cestino o regalala alla cliente', ERR, ERR_BG),
            ('Non porosa → pulisci e disinfetta', 'vetro e metallo', '#3f86b8', BLUE_BG),
            ('Ricambio monouso + supporto disinfettato', 'il supporto metallico resta', OK, OK_BG)]
    W = 236
    for k, (t, sub, c, bg) in enumerate(cols):
        x = 20 + k * (W + 6)
        cx = x + W / 2
        b += '<rect x="%d" y="56" width="%d" height="250" rx="14" fill="%s"/>' % (x, W, bg)
        b += badge(x + 24, 80, k + 1, c)
        if k == 0:
            b += tool_file(cx - 30, 108, -15, 120, 18, '#b9aa9c', '#e6dbd0')
            b += '<rect x="%.1f" y="140" width="60" height="26" rx="4" fill="#f9eef1" stroke="#bfa9b1"/>' % (cx - 70)
            b += '<circle cx="%.1f" cy="170" r="30" fill="#efe4d9" stroke="%s" stroke-width="3.5"/>' % (cx + 50, ACC2)
            import random as _r
            rnd = _r.Random(5)
            for j in range(16):
                a, rr = rnd.uniform(0, 6.28), rnd.uniform(0, 22)
                b += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#8a7d74"/>' % (cx + 50 + math.cos(a) * rr, 170 + math.sin(a) * rr, rnd.uniform(1.4, 3))
            b += '<line x1="%.1f" y1="191" x2="%.1f" y2="212" stroke="%s" stroke-width="6" stroke-linecap="round"/>' % (cx + 71, cx + 88, ACC2)
            b += trash(cx - 52, 234, 30, 32)
        elif k == 1:
            b += tool_file(cx - 20, 116, -15, 120, 14, '#9cc7e0', '#d8edf8')
            b += tool_file(cx - 20, 148, -15, 120, 14, '#7d8792', '#c5ccd3')
            b += ('<g transform="translate(%.1f,200) rotate(-20)"><rect x="-30" y="-5" width="50" height="10" rx="4" fill="#c9a06a"/>'
                  '<rect x="-30" y="5" width="34" height="10" fill="#f0ead8"/>%s</g>' % (cx - 40, ''.join(
                      '<line x1="%d" y1="5" x2="%d" y2="15" stroke="#9a8f7a"/>' % (xx, xx) for xx in range(-28, 4, 4))))
            b += spray(cx + 60, 230, 1.0)
        else:
            b += '<rect x="%.1f" y="120" width="150" height="16" rx="6" fill="%s" stroke="%s" stroke-width="1.6"/>' % (cx - 80, METAL, METAL_D)
            b += '<rect x="%.1f" y="124" width="24" height="8" rx="3" fill="%s"/>' % (cx - 104, METAL_D)
            b += '<path d="M%.1f,118 L%.1f,118 Q%.1f,104 %.1f,84 L%.1f,90 Q%.1f,108 %.1f,114 Z" fill="#e6dbd0" stroke="#b9aa9c" stroke-width="1.4"/>' % (
                cx - 76, cx + 10, cx + 40, cx + 60, cx + 66, cx + 46, cx + 10)
            b += '<rect x="%.1f" y="114" width="70" height="6" fill="#e6dbd0" stroke="#b9aa9c"/>' % (cx - 76)
            b += curved(cx + 70, 90, cx + 80, 150, -30)
            b += trash(cx + 76, 222, 30, 34)
            b += spray(cx - 50, 230, 0.85)
        b += mtext(cx, 260, wrap(t, W - 24, 14, True), 14, weight=800, fill=c)
        n = len(wrap(t, W - 24, 14, True))
        b += text(cx, 260 + n * 17.5 + 4, sub, 12.5, weight=600, fill=MUTED)
    return svg(760, 320, arrow_defs() + b, 'Igiene delle lime: carta e buffer monouso, vetro e metallo si disinfettano, supporto metallico con ricambi monouso')


# ================================================================= MODULO 4 – ATTREZZATURA
@figx('fresa-anatomia.svg')
def fresa_anatomia():
    b = title('La fresa: le parti')
    # centralina
    b += '<rect x="30" y="80" width="240" height="140" rx="14" fill="#eef1f4" stroke="%s" stroke-width="2"/>' % GREY_D
    b += text(150, 106, 'Centralina', 16, weight=800, fill=ACC2)
    b += '<circle cx="85" cy="150" r="26" fill="#fff" stroke="%s" stroke-width="3"/>' % GREY_D
    for k in range(9):
        a = math.radians(135 + k * 33.75)
        b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>' % (
            85 + math.cos(a) * 30, 150 + math.sin(a) * 30, 85 + math.cos(a) * 36, 150 + math.sin(a) * 36, ACC if k > 6 else GREY_D)
    b += '<line x1="85" y1="150" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="4" stroke-linecap="round"/>' % (85 + math.cos(math.radians(250)) * 20, 150 + math.sin(math.radians(250)) * 20, ACC2)
    b += text(85, 200, 'Velocità (RPM)', 12.5, weight=700)
    b += text(85, 214, '0–35.000', 12, weight=600, fill=MUTED)
    b += '<rect x="186" y="128" width="28" height="44" rx="6" fill="#fff" stroke="%s" stroke-width="2"/>' % GREY_D
    b += '<rect x="191" y="133" width="18" height="18" rx="4" fill="%s"/>' % ACC2
    b += text(226, 146, 'F', 13, 'start', 800) + text(226, 168, 'R', 13, 'start', 800)
    b += text(205, 200, 'Avanti / Indietro', 12.5, weight=700)
    # cavo e manipolo
    b += '<path d="M270,190 C320,200 250,300 300,300" fill="none" stroke="%s" stroke-width="5"/>' % INK
    b += '<rect x="298" y="282" width="170" height="36" rx="18" fill="#e6e1ec" stroke="%s" stroke-width="2"/>' % GREY_D
    for k in range(5):
        b += '<line x1="%d" y1="286" x2="%d" y2="314" stroke="%s" stroke-width="2" opacity=".5"/>' % (330 + k * 10, 330 + k * 10, GREY_D)
    b += '<path d="M468,288 L500,294 L500,306 L468,312 Z" fill="%s" stroke="%s" stroke-width="1.5"/>' % (METAL, METAL_D)
    b += '<rect x="500" y="297" width="30" height="6" fill="%s" stroke="%s"/>' % (METAL, METAL_D)
    b += '<rect x="530" y="292" width="20" height="16" rx="2" fill="#9aa3ad" stroke="%s"/>' % METAL_D
    b += text(383, 342, 'Manipolo', 15, weight=800, fill=ACC2)
    b += '<rect x="30" y="246" width="230" height="60" rx="12" fill="%s"/>' % BLUE_BG
    b += mtext(145, 270, ['Coppia: mantiene la velocità', 'sotto carico'], 13.5, weight=700, fill=ACC2)
    # ingrandimento
    b += '<rect x="540" y="62" width="200" height="188" rx="14" fill="%s" stroke="%s" stroke-width="1.6" stroke-dasharray="5 4"/>' % (PANEL, GREY)
    b += '<path d="M530,290 L560,250 M550,290 L720,250" stroke="%s" stroke-width="1.3" stroke-dasharray="4 4"/>' % GREY
    b += '<path d="M556,92 L606,104 L606,132 L556,144 Z" fill="%s" stroke="%s" stroke-width="2"/>' % (METAL, METAL_D)
    b += '<rect x="606" y="112" width="58" height="12" fill="%s" stroke="%s" stroke-width="1.5"/>' % (METAL, METAL_D)
    b += '<rect x="664" y="100" width="56" height="36" rx="3" fill="#9aa3ad" stroke="%s" stroke-width="1.6"/>' % METAL_D
    for k in range(6):
        b += '<line x1="%d" y1="100" x2="%d" y2="136" stroke="%s" stroke-width="1.5"/>' % (670 + k * 9, 664 + k * 9, METAL_D)
    b += callout(580, 144, 580, 170, 'Mandrino', 13, 700)
    b += callout(636, 124, 636, 214, 'Gambo 3/32"', 13, 700)
    b += text(636, 232, '= 2,35 mm', 13, weight=700)
    b += callout(700, 136, 700, 166, 'Testa', 13, 700)
    b += text(700, 182, 'della punta', 13, weight=700)
    # inserto punta storta
    b += '<rect x="560" y="262" width="180" height="90" rx="12" fill="%s"/>' % ERR_BG
    b += '<path d="M584,300 L634,300 L656,288" fill="none" stroke="%s" stroke-width="6" stroke-linecap="round"/>' % METAL_D
    b += '<rect x="652" y="276" width="22" height="14" rx="2" fill="#9aa3ad" stroke="%s" transform="rotate(-28 663 283)"/>' % METAL_D
    for k in range(3):
        b += '<path d="M%d,%d q4,-6 0,-12 q-4,-6 0,-12" fill="none" stroke="%s" stroke-width="1.8"/>' % (690 + k * 8, 300 - k * 2, ERR)
    b += mark(586, 284, False, 11)
    b += text(650, 336, 'Vibra = buttala', 14, weight=800, fill=ERR)
    return svg(760, 360, b, 'Le parti della fresa: centralina con velocità e senso di rotazione, manipolo, mandrino, gambo da 2,35 mm e testa della punta')


@figx('punte-forme.svg')
def punte_forme():
    b = title('Le punte e dove si usano')
    tiles = [('Cilindro', 'cil', 'sulla superficie', 'Carburo/ceramica', (0, -50, 22, 26)),
             ('Cilindro di sicurezza', 'sic', 'vicino alla piega', 'Diamantata', (0, -10, 22, 9)),
             ('Cono', 'cono', 'sotto il bordo libero', 'Carburo/ceramica', (0, -88, 26, 7)),
             ('Fiamma', 'fiamma', 'solleva la cuticola', 'Diamantata', (0, 0, 24, 8)),
             ('Pallina', 'palla', 'zona cuticolare', 'Diamantata', (-20, -6, 10, 10)),
             ('Ago', 'ago', 'dettagli e solchi', 'Diamantata', (31, -40, 5, 26))]
    W, H = 248, 140
    for i, (name, sh, use, mat, (zx, zy, zrx, zry)) in enumerate(tiles):
        x = 20 + (i % 3) * (W + 8)
        y = 54 + (i // 3) * (H + 8)
        b += '<rect x="%d" y="%d" width="%d" height="%d" rx="14" fill="%s"/>' % (x, y, W, H, PANEL)
        b += text(x + 16, y + 28, name, 15, 'start', 800)
        hc = '#c8ccd2' if mat.startswith('Carburo') else '#e2bf5a'
        b += bit(x + 82, y + 66, 1.4, 0, hc, sh)
        b += text(x + 16, y + 102, use, 13, 'start', 600, MUTED)
        b += chip(x + 16 + (tw(mat, 12, True) + 18) / 2, y + 122, mat, '#8a8f96' if mat.startswith('Carburo') else '#b8902a', '#fff', 12)
        cx, cy, s = x + 204, y + 70, 0.62
        b += mini(None, cx, cy, s)
        b += '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s" opacity=".55" stroke="%s" stroke-width="1.5"/>' % (
            cx + zx * s, cy + 34 * s + zy * s, zrx * s, zry * s, ACC, ACC2)
    # legenda grane
    yy = 362
    b += text(20, yy + 5, 'Colore sul gambo = grana:', 13.5, 'start', 700)
    for k, (c, l) in enumerate([('#f1d27a', 'XF'), ('#d9534f', 'F'), ('#3f6fe0', 'M'), ('#3d9a5c', 'G'), ('#2b2b2b', 'XG')]):
        bx = 210 + k * 62
        b += '<rect x="%d" y="%d" width="18" height="14" rx="3" fill="%s"/>' % (bx, yy - 6, c)
        b += text(bx + 24, yy + 6, l, 13, 'start', 800)
    b += text(520, yy + 5, 'fine → grossa, varia tra marchi', 13, 'start', 600, MUTED)
    return svg(800, 390, b, 'Forme delle punte per fresa (cilindro, cilindro di sicurezza, cono, fiamma, pallina, ago), dove si usano e materiale')


@figx('fresa-rpm-scala.svg')
def fresa_rpm():
    b = title('Quanti giri? La velocità giusta per ogni zona')
    x0, x1 = 50, 710

    def X(r):
        return x0 + r / 35000.0 * (x1 - x0)
    b += '<defs><linearGradient id="rpmg" x1="0" x2="1"><stop offset="0" stop-color="#3d9a5c"/><stop offset=".45" stop-color="#f2b632"/><stop offset="1" stop-color="#c0392b"/></linearGradient>'
    b += '<pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="8" height="8" fill="#fbe9e7"/><line x1="0" y1="0" x2="0" y2="8" stroke="#e7a39b" stroke-width="3"/></pattern></defs>'
    b += '<rect x="%.1f" y="58" width="%.1f" height="148" rx="6" fill="url(#hatch)"/>' % (X(25000), X(35000) - X(25000))
    b += mtext((X(25000) + X(35000)) / 2, 112, ['Mai durante', 'il servizio'], 14, weight=800, fill=ERR)
    bands = [(2000, 10000, 'Zona cuticolare 2.000–10.000', '#3d9a5c'), (8000, 15000, 'Levigare 8.000–15.000', '#7fae4a'),
             (10000, 20000, 'Forma e refill 10.000–20.000', '#d9a12a'), (15000, 25000, 'Rimozione (esperte) 15.000–25.000', '#d9792a')]
    for k, (a, c2, lab, col) in enumerate(bands):
        y = 66 + k * 34
        b += '<rect x="%.1f" y="%d" width="%.1f" height="12" rx="6" fill="%s"/>' % (X(a), y + 8, X(c2) - X(a), col)
        if k < 3:
            b += text(X(a), y + 3, lab, 13, 'start', 700)
        else:
            b += text(X(c2), y + 3, lab, 13, 'end', 700)
    b += '<rect x="%d" y="208" width="%d" height="22" rx="11" fill="url(#rpmg)"/>' % (x0, x1 - x0)
    for r in range(0, 35001, 5000):
        b += '<line x1="%.1f" y1="230" x2="%.1f" y2="236" stroke="%s"/>' % (X(r), X(r), INK)
        b += text(X(r), 250, '{:,}'.format(r).replace(',', '.') + (' RPM' if r == 35000 else ''), 12, 'middle' if 0 < r < 35000 else ('start' if r == 0 else 'end'), 600, MUTED)
    # pelle → prodotto
    b += mini(None, 80, 290, 0.38)
    b += mini(None, 680, 290, 0.38, plate='#d6ebf6', free='#d6ebf6', free_len=30)
    b += carrow(120, 290, 640, 290, GREY, 2)
    b += '<rect x="230" y="274" width="300" height="32" rx="10" fill="#fff"/>'
    b += text(380, 296, 'Più vicino alla pelle = più lento', 15, weight=800, fill=ACC2)
    b += text(80, 328, 'pelle', 12.5, weight=700, fill=MUTED) + text(680, 328, 'prodotto', 12.5, weight=700, fill=MUTED)
    return svg(760, 340, b, 'Scala delle velocità della fresa da 0 a 35.000 giri: più si è vicini alla pelle più si va piano; oltre 25.000 mai durante il servizio')


def side_nail_scene(x, y, w=300):
    """Dito di profilo con prodotto sulla lamina (punta a destra). y = superficie del prodotto."""
    o = ('<path d="M%.1f,%.1f L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
         % (x, y + 10, x + w * 0.8, y + 10, x + w * 0.95, y + 12, x + w * 0.95, y + 70, x + w * 0.7, y + 72, x, y + 72, SKIN, SKIN_D))
    o += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.4"/>' % (
        x + w * 0.22, y + 10, x + w * 0.22, y + 2, x + w * 1.0, y, x + w * 1.0, y + 10, PROD, PROD_S)
    o += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="4"/>' % (x + w * 0.22, y + 11, x + w * 0.9, y + 11, NAIL_S)
    o += '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.3"/>' % (
        x, y - 2, x + w * 0.16, y - 2, x + w * 0.24, y, x + w * 0.24, y + 10, x, y + 10, SKIN, SKIN_D)
    return o


def handpiece(x, y, ang, s=1.0, shape='cil'):
    """Manipolo con punta; (x, y) = centro della testa della punta."""
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f) scale(%.2f)">'
            '<rect x="-15" y="-8" width="30" height="16" rx="2" fill="#c8ccd2" stroke="%s" stroke-width="1.4"/>'
            '<rect x="15" y="-3" width="20" height="6" fill="%s" stroke="%s"/>'
            '<path d="M35,-7 L55,-14 L55,14 L35,7 Z" fill="%s" stroke="%s"/>'
            '<rect x="55" y="-16" width="150" height="32" rx="16" fill="#e6e1ec" stroke="%s" stroke-width="1.8"/></g>'
            % (x, y, ang, s, METAL_D, METAL, METAL_D, METAL, METAL_D, GREY_D))


@figx('fresa-angolo.svg')
def fresa_angolo():
    b = title('Come tenere la punta')
    b += frame(20, 56, 350, 276, 'Parallela', ok=True, border=OK)
    b += frame(390, 56, 350, 276, 'Inclinata', ok=False, border=ERR)
    # 1 parallela
    b += side_nail_scene(40, 200, 250)
    b += handpiece(150, 191, 0, 0.85)
    b += arrow(110, 160, 190, 160, ACC2, 2.4, both=True)
    b += '<ellipse cx="290" cy="226" rx="26" ry="14" fill="%s" stroke="%s" stroke-width="1.5"/>' % (SKIN, SKIN_D)
    b += callout(296, 240, 296, 296, 'Punto d\'appoggio', 13, 700, ACC2)
    b += text(160, 296, 'mignolo sulla mano', 12.5, weight=600, fill=MUTED).replace('x="160.0"', 'x="130.0"')
    b += text(195, 318, 'Pressione leggera, sempre in movimento', 14, weight=800, fill=OK)
    # 2 inclinata
    b += side_nail_scene(410, 200, 200)
    b += handpiece(510, 186, -28, 0.85)
    b += '<circle cx="497" cy="199" r="9" fill="none" stroke="%s" stroke-width="2.5"/>' % ERR
    b += thermometer(436, 124, 0.8)
    b += mtext(454, 112, ['Calore da', 'attrito'], 13, 'start', 700, ERR)
    # inserto vista dall'alto con anelli di fuoco
    ex = ''.join('<path d="M%.1f,%.1f a10,10 0 0 1 20,0" fill="none" stroke="%s" stroke-width="2.5" clip-path="url(#CLIP)"/>' % (px, py, ERR)
                 for px, py in ((-20, -30), (2, -46), (-10, -60), (8, -24)))
    b += '<circle cx="680" cy="226" r="52" fill="#fff" stroke="%s" stroke-width="1.6" stroke-dasharray="4 3"/>' % GREY
    b += mini('', 680, 222, 0.62)
    b += '<g transform="translate(680,%.1f) scale(0.62)">%s</g>' % (222 + 34 * 0.62, ex.replace('clip-path="url(#CLIP)"', ''))
    b += text(565, 296, 'Anelli di fuoco:', 14, weight=800, fill=ERR)
    b += text(565, 318, 'solchi sulla lamina', 13, weight=600)
    return svg(760, 340, arrow_defs() + b, 'Punta della fresa parallela alla superficie con punto d\'appoggio, oppure inclinata: crea anelli di fuoco e calore')


@figx('kit-priorita.svg')
def kit_priorita():
    b = title('Il kit: cosa comprare e quando')
    cols = [('SUBITO', OK, OK_BG, ['Lampada UV/LED', 'Aspiratore', 'Guanti, occhiali, FFP2', 'Gel: Base, Builder, Top', 'Disidratante, primer, cleaner',
                                    'Lime 100/180 e 240', 'Spingicuticole, tronchesine', 'Tip e cartine', 'Mano da allenamento']),
            ('DOPO QUALCHE MESE', '#b7791f', WARN_BG, ['Fresa con 3 punte', 'Gel cover', '4 semipermanenti', 'Dotter']),
            ('PIÙ AVANTI', '#3f86b8', BLUE_BG, ['Kit acrilico: liquido, polveri, pennello, dappen', 'Polygel', 'Polveri chrome', 'Magnete cat-eye'])]
    W = 248
    for k, (t, c, bg, items) in enumerate(cols):
        x = 20 + k * (W + 8)
        cx = x + W / 2
        b += '<rect x="%d" y="56" width="%d" height="310" rx="14" fill="%s"/>' % (x, W, bg)
        b += '<path d="M%d,70 Q%d,56 %d,56 L%d,56 Q%d,56 %d,70 L%d,94 L%d,94 Z" fill="%s"/>' % (x, x, x + 14, x + W - 14, x + W, x + W, x + W, x, c)
        b += text(cx, 82, t, 15, weight=900, fill='#fff')
        if k == 0:
            b += ('<path d="M%.1f,150 L%.1f,124 Q%.1f,98 %.1f,124 L%.1f,150 Z" fill="#f4f1f8" stroke="#8a7d9e" stroke-width="2"/>'
                  '<rect x="%.1f" y="150" width="70" height="6" rx="3" fill="#8a7d9e"/>' % (x + 24, x + 24, x + 54, x + 84, x + 84, x + 19)) + jar(x + 118, 150, 30, 22, '#f6d6df', '') + jar(x + 156, 150, 30, 22, '#f8bbd0', '') + jar(x + 194, 150, 30, 22, '#fdf3dc', '')
            b += text(x + 156, 174, 'Base · Builder · Top', 12, weight=700, fill=MUTED)
        elif k == 1:
            b += efile_hand(cx - 30, 128, 0.9, 0)
            for j, cc in enumerate(['#d65d86', '#8e3b5a', '#e9a7bd', '#b39ddb']):
                b += bottle(x + 60 + j * 40, 172, 22, 30, cc, cap=INK)
        else:
            b += dappen(x + 60, 150, 50, 32, 0.5) + powder_jar(x + 130, 150, 50, 32) + tool_brush(x + 190, 132, -30, 50, '#f3eee6')
        yy = 200
        for it in items:
            lines = wrap(it, W - 40, 13, True)
            b += '<circle cx="%d" cy="%d" r="4" fill="%s"/>' % (x + 20, yy - 4, c)
            b += mtext(x + 32, yy, lines, 13, 'start', 700)
            yy += (19 if k == 0 else 26) + 16 * (len(lines) - 1)
    b += '<rect x="20" y="376" width="760" height="36" rx="12" fill="%s"/>' % ACC2
    b += text(400, 400, 'Un solo sistema completo all\'inizio', 16, weight=800, fill='#fff')
    return svg(800, 420, b, 'Priorità di acquisto del kit: subito il necessario per un sistema, dopo qualche mese fresa e colori, più avanti acrilico e effetti')


@figx('kit-postazione.svg')
def kit_postazione():
    b = title('La postazione: tre zone')
    # sedie
    b += '<path d="M360,84 Q400,58 440,84 L440,92 L360,92 Z" fill="#d8cfd3" stroke="%s" stroke-width="1.6"/>' % GREY_D
    b += text(470, 82, 'cliente', 13, 'start', 700, MUTED)
    b += '<path d="M360,352 L440,352 L440,360 Q400,386 360,360 Z" fill="#d8cfd3" stroke="%s" stroke-width="1.6"/>' % GREY_D
    b += text(470, 370, 'operatrice', 13, 'start', 700, MUTED)
    b += '<rect x="40" y="96" width="720" height="250" rx="14" fill="#f3ece6" stroke="#c7b9ad" stroke-width="2"/>'
    zones = [(54, 'Zona pulita', OK_BG, OK), (292, 'Zona di lavoro', '#fff', ACC2), (530, 'Zona sporco', ERR_BG, ERR)]
    for zx, t, bg, c in zones:
        b += '<rect x="%d" y="108" width="216" height="226" rx="10" fill="%s" stroke="%s" stroke-width="2" stroke-dasharray="7 5"/>' % (zx, bg, c)
        b += text(zx + 108, 132, t, 15, weight=800, fill=c)
    # pulita
    b += pouch(70, 150, 90, 54, False) + nipper(118, 172, 0.6) + pouch(70, 214, 90, 54, False) + curette(110, 240, 0.7)
    b += text(115, 286, 'buste sterili', 12.5, weight=600)
    b += tool_file(220, 168, 90, 70, 12, '#b9aa9c', '#e6dbd0') + tool_file(238, 168, 90, 70, 12, '#b9aa9c', '#e6dbd0')
    b += text(229, 220, 'lime nuove', 12.5, weight=600)
    for k in range(3):
        b += '<circle cx="%d" cy="258" r="11" fill="#dfe9f2" stroke="%s" stroke-width="1.6"/><circle cx="%d" cy="258" r="5" fill="%s"/>' % (190 + k * 26, GREY_D, 190 + k * 26, INK)
    b += text(216, 290, 'flaconi chiusi', 12.5, weight=600)
    # lavoro
    b += '<rect x="330" y="210" width="140" height="70" rx="6" fill="#d5dadf" stroke="%s" stroke-width="1.6"/>' % GREY_D
    for k in range(9):
        b += '<line x1="%d" y1="216" x2="%d" y2="274" stroke="%s" stroke-width="2"/>' % (340 + k * 15, 340 + k * 15, GREY)
    b += '<rect x="368" y="226" width="64" height="38" rx="18" fill="%s" stroke="%s" stroke-width="1.6"/>' % (ACC, ACC2)
    b += text(400, 300, 'poggiamano su aspiratore', 12.5, weight=600)
    b += '<rect x="304" y="148" width="64" height="44" rx="12" fill="#f4f1f8" stroke="#8a7d9e" stroke-width="2"/>'
    b += '<path d="M314,192 Q336,166 358,192" fill="#e6dcf5" stroke="#8a7d9e" stroke-width="1.6"/>'
    b += text(336, 210, 'UV/LED', 12, weight=700, fill='#6b4fa0').replace('y="210.0"', 'y="145.0"')
    b += '<circle cx="470" cy="170" r="12" fill="%s"/>' % GREY_D
    b += '<path d="M470,170 L440,190 L420,214" stroke="%s" stroke-width="5" stroke-linecap="round" fill="none"/>' % GREY_D
    b += '<ellipse cx="418" cy="216" rx="14" ry="9" fill="#fff3c4" stroke="%s" stroke-width="2"/>' % GREY_D
    b += text(470, 150, 'lampada', 12, weight=700, fill=MUTED)
    # sporco
    b += '<rect x="548" y="150" width="110" height="70" rx="8" fill="#fff" stroke="%s" stroke-width="2"/>' % GREY_D
    b += nipper(612, 176, 0.65, 10) + tool_pusher(584, 200, 0, 60)
    b += text(603, 240, 'strumenti usati', 12.5, weight=600)
    b += '<circle cx="700" cy="186" r="24" fill="#cfd6dd" stroke="%s" stroke-width="2"/><circle cx="700" cy="186" r="8" fill="%s"/>' % (GREY_D, GREY_D)
    b += text(696, 230, 'cestino', 12.5, weight=600)
    b += text(696, 246, 'con coperchio', 12.5, weight=600)
    for px, py in ((580, 286), (610, 296), (596, 274)):
        b += '<path d="M%d,%d l12,-6 l10,4 l6,10 l-8,8 l-14,0 l-8,-8 Z" fill="#fff" stroke="#c7b9ad" stroke-width="1.4"/>' % (px, py)
    b += text(670, 300, 'salviette usate', 12.5, weight=600)
    return svg(800, 400, arrow_defs() + b, 'Postazione vista dall\'alto: zona pulita, zona di lavoro con poggiamano e aspiratore, zona sporco con strumenti usati e cestino')


@figx('pennelli-cura.svg')
def pennelli_cura():
    b = title('Cura dei pennelli')
    rows = [('Acrilico', ['Pulisci nel monomero', 'Asciuga su carta', 'Rimodella', 'No acetone']),
            ('Gel', ['Togli il gel', 'Chiudi il cappuccio', 'Lontano dalla luce'])]
    W, H = 150, 120
    for r, (lab, items) in enumerate(rows):
        y = 56 + r * (H + 10)
        b += '<rect x="20" y="%d" width="90" height="%d" rx="12" fill="%s"/>' % (y, H, ACC2)
        b += text(65, y + H / 2 + 6, lab, 16, weight=800, fill='#fff')
        for k, t in enumerate(items):
            x = 120 + k * (W + 6)
            cx = x + W / 2
            b += '<rect x="%d" y="%d" width="%d" height="%d" rx="12" fill="%s"/>' % (x, y, W, H, PANEL)
            b += badge(x + 18, y + 18, k + 1, ACC, 11, 13)
            iy = y + 56
            if r == 0 and k == 0:
                b += dappen(cx - 6, iy + 26, 54, 32, 0.6) + tool_brush(cx + 4, iy + 12, -60, 34, '#f3eee6')
            elif r == 0 and k == 1:
                b += '<rect x="%.1f" y="%d" width="100" height="34" rx="3" fill="#fff" stroke="#c7b9ad"/>' % (cx - 50, iy + 2)
                b += tool_brush(cx - 30, iy + 16, 0, 70, '#f3eee6')
                b += drop_icon(cx - 46, iy + 28, 0.35, '#9cc7e0')
            elif r == 0 and k == 2:
                b += tool_brush(cx - 10, iy + 18, 0, 70, '#f3eee6')
                b += glove(cx - 22, iy + 4, 0.42, 90, fist=True)
            elif r == 0 and k == 3:
                b += bottle(cx, iy + 36, 30, 44, '#e6f1f8', 'ACE', 12)
                b += no_sign(cx, iy + 8, 30, 4)
            elif r == 1 and k == 0:
                b += tool_brush(cx - 10, iy + 12, 0, 70, GEL)
                b += '<path d="M%.1f,%d l20,-4 l6,18 l-20,6 Z" fill="#fff" stroke="%s" stroke-width="1.4"/>' % (cx - 40, iy + 2, GREY)
            elif r == 1 and k == 1:
                b += tool_brush(cx - 20, iy + 12, 0, 70, GEL)
                b += '<rect x="%.1f" y="%d" width="34" height="16" rx="5" fill="%s" opacity=".9"/>' % (cx - 50, iy + 4, INK)
                b += carrow(cx - 70, iy + 30, cx - 44, iy + 22, ACC2, 2)
            else:
                b += tool_brush(cx - 30, iy + 22, 0, 60, GEL)
                b += '<circle cx="%.1f" cy="%d" r="10" fill="%s"/>' % (cx + 44, iy - 4, AMBER)
                for a in range(8):
                    an = a * math.pi / 4
                    b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>' % (
                        cx + 44 + math.cos(an) * 13, iy - 4 + math.sin(an) * 13, cx + 44 + math.cos(an) * 18, iy - 4 + math.sin(an) * 18, AMBER)
                b += no_sign(cx + 44, iy - 4, 22, 3)
            b += text(cx, y + H - 12, t, 13, weight=700)
    return svg(760, 320, b, 'Cura dei pennelli: per l\'acrilico monomero, asciugatura e rimodellatura senza acetone; per il gel pulizia, cappuccio e riparo dalla luce')


def double_pusher(x, y, s=1.0, ang=0):
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f) scale(%.2f)"><rect x="-50" y="-4" width="100" height="8" rx="4" fill="%s" stroke="%s"/>'
            '<path d="M-50,-4 L-72,-11 L-74,11 L-50,4 Z" fill="%s"/><path d="M50,-3 L72,-2 L76,0 L72,2 L50,3 Z" fill="%s"/>'
            '<path d="M-20,-4 L-20,4 M-14,-4 L-14,4 M-8,-4 L-8,4" stroke="%s"/></g>' % (x, y, ang, s, METAL, METAL_D, METAL_D, METAL_D, METAL_D))


def tweezers(x, y, s=1.0, ang=0):
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f) scale(%.2f)" fill="none" stroke="%s" stroke-width="5" stroke-linecap="round">'
            '<path d="M-50,0 L40,-9"/><path d="M-50,0 L40,9"/></g>' % (x, y, ang, s, METAL_D))


def tip_cutter(x, y, s=1.0):
    return ('<g transform="translate(%.1f,%.1f) scale(%.2f)"><path d="M-60,-6 L30,-10 L40,-4 L40,4 L-60,2 Z" fill="%s" stroke="%s" stroke-width="1.4"/>'
            '<path d="M-60,6 L30,4 L40,12 L-60,14 Z" fill="%s" stroke="%s" stroke-width="1.4"/>'
            '<path d="M20,-4 L46,-4 L46,6 L20,6" fill="none" stroke="%s" stroke-width="2"/><circle cx="-4" cy="2" r="3" fill="%s"/></g>'
            % (x, y, s, METAL, METAL_D, '#b5bcc4', METAL_D, METAL_D, METAL_D))


def cleaning_brush(x, y, s=1.0):
    return ('<g transform="translate(%.1f,%.1f) scale(%.2f)"><rect x="-60" y="-6" width="90" height="12" rx="6" fill="%s"/>'
            '<rect x="20" y="-14" width="44" height="12" rx="3" fill="#6fa8c9"/>%s</g>'
            % (x, y, s, '#3f86b8', ''.join('<line x1="%d" y1="-2" x2="%d" y2="12" stroke="#f0ead8" stroke-width="2"/>' % (xx, xx) for xx in range(23, 63, 5))))


@figx('strumenti-manuali.svg')
def strumenti_manuali():
    b = title('Gli strumenti manuali')
    items = [('Spingicuticole', 'Sterilizzare', lambda cx, cy: double_pusher(cx, cy, 1.0)),
             ('Curetta', 'Sterilizzare', lambda cx, cy: curette(cx, cy, 1.4)),
             ('Tronchesine', 'Sterilizzare', lambda cx, cy: nipper(cx + 16, cy, 1.4)),
             ('Tagliatip', 'Disinfettare', lambda cx, cy: tip_cutter(cx, cy, 1.0)),
             ('Pinzette', 'Disinfettare', lambda cx, cy: tweezers(cx, cy, 1.0)),
             ('Bastoncino d\'arancio', 'Monouso', lambda cx, cy: tool_stick(cx - 50, cy, 0, 100)),
             ('Spazzolino', 'Disinfettare', lambda cx, cy: cleaning_brush(cx, cy, 1.0))]
    bc = {'Sterilizzare': OK, 'Disinfettare': '#3f86b8', 'Monouso': '#8a8f96'}
    W, H = 184, 156
    for i, (name, bd, draw) in enumerate(items):
        x = 20 + (i % 4) * (W + 8)
        y = 56 + (i // 4) * (H + 8)
        cx = x + W / 2
        b += '<rect x="%d" y="%d" width="%d" height="%d" rx="14" fill="%s"/>' % (x, y, W, H, PANEL)
        b += draw(cx, y + 60)
        b += text(cx, y + 112, name, 14.5, weight=800)
        b += chip(cx, y + 138, bd, bc[bd], '#fff', 12.5)
    # inserto
    x, y = 20 + 3 * (W + 8), 56 + H + 8
    b += '<rect x="%d" y="%d" width="%d" height="%d" rx="14" fill="#fff" stroke="%s" stroke-width="1.6"/>' % (x, y, W, H, GREY)
    b += text(x + W / 2, y + 22, 'Come si tiene', 13.5, weight=800, fill=ACC2)
    for j, ok in enumerate((True, False)):
        yy = y + 62 + j * 56
        x0 = x + 12
        b += nail_side(x0, yy, 110)
        if ok:
            b += tool_pusher(x0 + 54, yy - 7, -12, 64)
        else:
            b += tool_pusher(x0 + 42, yy - 12, -40, 56)
        b += mark(x + W - 18, yy - 18, ok, 11)
    return svg(800, 400, b, 'Strumenti manuali (spingicuticole, curetta, tronchesine, tagliatip, pinzette, bastoncino, spazzolino) e come trattarli dopo l\'uso')


def limb(x1, y1, x2, y2, w=16, col='#cfe0ec', st=GREY_D):
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.1f" stroke-linecap="round"/>'
            '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.1f" stroke-linecap="round"/>'
            % (x1, y1, x2, y2, st, w + 3, x1, y1, x2, y2, col, w))


def pain(x, y, r=11):
    o = ''
    for k in range(8):
        a = k * math.pi / 4
        rr = r if k % 2 == 0 else r * 0.55
        o += '%.1f,%.1f ' % (x + math.cos(a) * rr, y + math.sin(a) * rr)
    return '<polygon points="%s" fill="%s" stroke="#fff" stroke-width="1.5"/>' % (o, ERR)


@figx('postura-tavolo.svg')
def postura():
    b = title('La postura al tavolo')
    b += frame(20, 56, 350, 316, 'Postura corretta', ok=True, border=OK)
    b += frame(390, 56, 350, 316, 'Postura scorretta', ok=False, border=ERR)
    for k, good in enumerate((True, False)):
        px = 20 + k * 370
        fl = 356
        # tavolo
        b += '<rect x="%d" y="%d" width="150" height="10" rx="3" fill="#c7b9ad"/>' % (px + 186, fl - 140)
        b += '<rect x="%d" y="%d" width="8" height="130" fill="#c7b9ad"/>' % (px + 320, fl - 130)
        b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2"/>' % (px + 30, fl, px + 340, fl, GREY)
        # sedia
        b += '<rect x="%d" y="%d" width="70" height="10" rx="4" fill="%s"/>' % (px + 50, fl - 110, GREY_D)
        b += '<rect x="%d" y="%d" width="6" height="100" fill="%s"/>' % (px + 82, fl - 100, GREY_D)
        b += '<rect x="%d" y="%d" width="50" height="5" rx="2" fill="%s"/>' % (px + 60, fl - 5, GREY_D)
        if good:
            b += '<rect x="%d" y="%d" width="8" height="80" rx="4" fill="%s"/>' % (px + 46, fl - 190, GREY_D)
            hip, sh, head = (px + 80, fl - 122), (px + 84, fl - 222), (px + 92, fl - 252)
            knee, ank, toe = (px + 150, fl - 122), (px + 150, fl - 12), (px + 176, fl - 6)
            elb, hand = (px + 106, fl - 160), (px + 205, fl - 152)
            ch = px + 236
        else:
            hip, sh, head = (px + 80, fl - 122), (px + 140, fl - 206), (px + 176, fl - 214)
            knee, ank, toe = (px + 150, fl - 122), (px + 118, fl - 22), (px + 132, fl - 6)
            elb, hand = (px + 168, fl - 168), (px + 238, fl - 160)
            ch = px + 290
        # aspiratore + poggiamano + mano cliente
        b += '<rect x="%d" y="%d" width="60" height="8" fill="%s"/>' % (ch - 30, fl - 141, GREY)
        b += client_hand_side(ch + 12, fl - 140, 0.42)
        if good:
            b += '<rect x="%d" y="%d" width="40" height="44" rx="4" fill="#d5dadf" stroke="%s"/>' % (ch - 20, fl - 130, GREY_D)
            b += text(ch, fl - 70, 'aspiratore', 12, weight=600, fill=MUTED)
            # lampada da tavolo
            b += '<path d="M%d,%d L%d,%d L%d,%d" fill="none" stroke="%s" stroke-width="4" stroke-linecap="round"/>' % (px + 330, fl - 150, px + 316, fl - 270, ch + 20, fl - 250, GREY_D)
            b += '<path d="M%d,%d l-22,22 l24,8 Z" fill="%s"/>' % (ch + 26, fl - 258, GREY_D)
            b += '<path d="M%d,%d L%d,%d L%d,%d Z" fill="#fff3c4" opacity=".7"/>' % (ch + 14, fl - 238, ch - 10, fl - 150, ch + 40, fl - 150)
        # corpo
        b += limb(hip[0], hip[1], knee[0], knee[1], 20) + limb(knee[0], knee[1], ank[0], ank[1], 16) + limb(ank[0], ank[1], toe[0], toe[1], 10)
        b += limb(hip[0], hip[1], sh[0], sh[1], 36, '#cfe0ec')
        b += limb(sh[0], sh[1], elb[0], elb[1], 14) + limb(elb[0], elb[1], hand[0], hand[1], 12)
        b += '<circle cx="%.1f" cy="%.1f" r="7" fill="%s" stroke="%s"/>' % (hand[0], hand[1], SKIN, SKIN_D)
        b += '<circle cx="%.1f" cy="%.1f" r="20" fill="%s" stroke="%s" stroke-width="1.6"/>' % (head[0], head[1], SKIN, SKIN_D)
        b += '<path d="M%.1f,%.1f a20,20 0 0 1 %.1f,%.1f" fill="#5a3a2e"/>' % (head[0] - 20, head[1], 34, -14) if good else \
            '<path d="M%.1f,%.1f a20,20 0 0 1 %.1f,%.1f" fill="#5a3a2e"/>' % (head[0] - 18, head[1] - 10, 30, -10)
        if good:
            b += text(px + 112, 150, 'schiena dritta', 12.5, 'start', 700, OK)
            b += mtext(px + 124, 168, ['avambracci', 'appoggiati'], 12.5, 'start', 700, OK)
            b += text(px + 190, 338, 'piedi a terra', 12.5, 'start', 700, OK)
        else:
            b += pain(sh[0] + 22, sh[1] - 6) + pain(hip[0] + 4, hip[1] - 26) + pain(hand[0] - 12, hand[1] + 4, 9)
            b += '<path d="M%.1f,%.1f q6,-12 14,-14" fill="none" stroke="%s" stroke-width="2"/>' % (sh[0] - 14, sh[1] - 14, ERR)
            for t, (lx, ly) in (('collo piegato', (px + 210, 106)), ('gomiti sospesi', (px + 196, 172)), ('mano lontana', (px + 250, 238))):
                b += text(lx, ly, t, 12.5, 'start', 700, ERR)
    return svg(760, 380, arrow_defs() + b, 'Postura al tavolo: corretta con schiena dritta, piedi a terra e avambracci appoggiati; scorretta con collo piegato e gomiti sospesi')


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
