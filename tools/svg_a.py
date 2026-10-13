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
