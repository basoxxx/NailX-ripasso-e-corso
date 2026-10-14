#!/usr/bin/env python3
"""Illustrazioni del gruppo A (moduli anatomia, igiene, sistemi, attrezzatura). Uso: python3 tools/svg_a.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_svg import *  # palette, svg(), text(), mtext(), leader(), arrow(), panel(), mark(), finger_nail(), side_profile(), tool_*(), lamp(), timer(), steps_fig(), ...
import gen_svg
import math
import random

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
            + text(x, y + r * 0.62, '!', max(12, r * 1.15), weight=900, fill='#fff'))


def excl(x, y, col=AMBER, r=13):
    return '<circle cx="%.1f" cy="%.1f" r="%s" fill="%s"/>' % (x, y, r, col) + text(x, y + r * 0.45, '!', max(12, r * 1.25), weight=900, fill='#fff')


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
    b += mark(538, 384, False, 10) + text(552, 389, 'Non assottigliare la lamina', 13, 'start', 600)
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


def _matrix_section(x, y, w, ml, th):
    """Sezione longitudinale del dito (punta a destra). y = fondo della lamina (letto ungueale);
    ml = lunghezza della matrice, th = spessore della lamina. Restituisce (svg, punti utili)."""
    xf = x + 96                  # bordo della piega prossimale
    xm0 = xf - 8 - ml            # inizio della matrice (sotto la piega)
    xt = x + w - 34              # fine del letto (iponichio)
    xe = x + w - 6               # bordo libero
    top = y - th - 26            # dorso del dito
    gid = uid('ms')
    s = ('<defs><linearGradient id="%s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f8dccb"/>'
         '<stop offset=".5" stop-color="#f3cdb6"/><stop offset="1" stop-color="#dcab92"/></linearGradient></defs>' % gid)
    body = ('M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z'
            % (x, top, xf - 22, top, xf + 2, top + 2, xf + 4, y - th, xt, y,
               xt + 22, y + 4, xt + 26, y + 34, xt + 10, y + 56, xt - 6, y + 74, xt - 40, y + 80, x, y + 80))
    s += '<path d="%s" fill="url(#%s)" stroke="%s" stroke-width="1.5"/>' % (body, gid, SKIN_D)
    # falange (osso) e letto ungueale
    s += ('<path d="M%.1f,%.1f L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="#f6efe2" stroke="#d9cbb3" stroke-width="1.2"/>'
          % (x, y + 22, xt - 40, y + 20, xt - 14, y + 20, xt - 14, y + 52, xt - 40, y + 54, x, y + 56))
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="6" fill="#f2a3b6"/>' % (xm0 + ml, y, xt - xm0 - ml)
    # matrice (germinativa) a mezzaluna sotto la piega
    s += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="%s" stroke="#8f2a22" stroke-width="1"/>'
          % (xm0, y - 2, xm0 + ml / 2, y + 14, xm0 + ml, y + 2, xm0 + ml, y + 9, xm0 + ml / 2, y + 22, xm0, y + 7, ERR))
    # lamina: dalla radice al bordo libero, con strati
    pl = ('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z'
          % (xm0, y - 1, xm0 + 2, y - th, xm0 + 12, y - th, xt, y - th, xe - 2, y - th, xe, y - th / 2 + 1,
             xe - 2, y, xt, y, xm0 + ml, y, xm0 + 4, y + 1, xm0, y - 1))
    s += '<path d="%s" fill="%s" stroke="%s" stroke-width="1.5"/>' % (pl, NAIL, NAIL_S)
    if th > 10:
        for k in (1, 2):
            yy = y - th * k / 3
            s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1" opacity=".45"/>' % (xm0 + 12, yy, xe - 6, yy, NAIL_S)
    # piega prossimale sopra la radice
    s += ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="url(#%s)"/>'
          % (x, top, xf - 22, top, xf + 2, top + 2, xf + 4, y - th, xf - 14, y - th - 2, x, y - th - 2, gid))
    s += '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="%s" stroke-width="1.5" fill="none"/>' % (
        x, top, xf - 22, top, xf + 2, top + 2, xf + 4, y - th, SKIN_D)
    s += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="#fff" stroke-width="2.5" opacity=".8" fill="none" stroke-linecap="round"/>' % (
        xf + 6, y - th - 1, xf + 14, y - th - 2.5, xf + 22, y - th - 2)
    return s, dict(xm0=xm0, xm1=xm0 + ml, xe=xe, xt=xt, top=top)


@figx('matrice-forma.svg')
def matrice_forma():
    b = title('La matrice decide spessore e forma della lamina')
    pw = 232
    for i, (t, ml, th, lab) in enumerate((('Matrice lunga', 60, 18, 'Lamina spessa'), ('Matrice corta', 24, 6, 'Lamina sottile'))):
        x = 20 + i * (pw + 12)
        b += frame(x, 56, pw, 244, t, i + 1)
        y = 168
        s, p = _matrix_section(x + 8, y, pw - 16, ml, th)
        b += s
        # misura della matrice
        b += '<path d="M%.1f,%.1f v6 H%.1f v-6" stroke="%s" stroke-width="1.6" fill="none"/>' % (p['xm0'], y + 26, p['xm1'], ERR)
        b += callout((p['xm0'] + p['xm1']) / 2, y + 32, x + 70, 280, 'matrice', 13.5, 700, ERR)
        b += callout(p['xe'] - 30, y - th / 2, x + 150, 112, lab, 15, 800, ACC2)
        # spessore
        b += '<path d="M%.1f,%.1f h6 M%.1f,%.1f v%.1f M%.1f,%.1f h6" stroke="%s" stroke-width="1.6"/>' % (
            p['xe'] + 2, y - th, p['xe'] + 5, y - th, th, p['xe'] + 2, y, ACC2)
    x = 20 + 2 * (pw + 12)
    b += frame(x, 56, pw, 244, 'Vista dalla punta', 3)
    b += gen_svg._ctip(x + 62, 132, 3, 44, NAIL, 7)
    b += gen_svg._ctip(x + 172, 140, 22, 40, NAIL, 7)
    b += mtext(x + 62, 248, ['Matrice piatta', '→ unghia piatta'], 13, weight=600)
    b += mtext(x + 172, 248, ['Matrice curva', '→ curva a C', 'profonda'], 13, weight=600)
    b += '<rect x="20" y="314" width="720" height="50" rx="12" fill="#f1ecee"/>'
    b += calendar(40, 321, 38, 34)
    b += text(94, 345, 'Dalla matrice al bordo libero: circa 4–6 mesi', 16, 'start', 700)
    b += text(730, 345, 'non puoi cambiarle: le compensi', 13, 'end', fill=MUTED, style='italic')
    return svg(760, 380, b, 'Matrice lunga o corta, piatta o curva: spessore e forma della lamina')


@figx('anatomia-sigilli.svg')
def sigilli():
    b = title('I 4 sigilli proteggono letto e matrice')
    f, p = finger_nail(270, 300, hw=64, nail_len=180, free_len=26, shape='squoval', smile=10, finger_len=70)
    b += f
    cx, yc, ys, hw = p['cx'], p['y_c'], p['y_s'], p['hw']
    # cuticola (bianca) sulla piega
    b += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="#fff" stroke-width="5" opacity=".85"/>' % (
        cx - hw + 4, yc - 32, cx, yc + 8, cx + hw - 4, yc - 32)
    pts = {1: (cx, yc + 22), 2: (cx - hw - 18, (yc + ys) / 2 + 10), 3: (cx + hw + 18, (yc + ys) / 2 + 10)}
    # germi fermati
    for (gx, gy), (tx, ty) in (((cx + 70, yc + 82), pts[1]), ((70, 290), pts[2]), ((470, 290), pts[3])):
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
    b += scissors(92, 330, 1.0, -20) + no_sign(98, 328, 22)
    b += mark(40, 384, False, 11) + text(56, 389, 'Non tagliare la pelle viva', 14, 'start', 700, ERR)
    # inserto: sezione con iponichio
    ix, iy = 540, 196
    b += frame(ix, iy, 200, 190, 'Di lato: iponichio')
    b += nail_side(ix + 6, iy + 104, 176)
    hx = ix + 6 + 176 * 0.84
    b += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="#e4a48a" stroke="%s" stroke-width="1"/>' % (
        hx - 20, iy + 110, hx - 2, iy + 104, hx + 14, iy + 108, hx + 6, iy + 124, hx - 20, iy + 110, SKIN_D)
    b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.3"/>' % (hx, iy + 112, ix + 160, iy + 146, MUTED)
    b += badge(ix + 160, iy + 150, 4, OK, 14)
    b += germ(ix + 186, iy + 104, 6)
    b += text(ix + 100, iy + 184, 'sotto il bordo libero', 12.5, fill=MUTED)
    return svg(760, 410, arrow_defs() + b, 'I quattro sigilli dell\'unghia: cuticola con piega prossimale, due pieghe laterali e iponichio')


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


def _finger_path(x1, y1, x2, y2, r1, r2):
    """Dito affusolato: base larga r1 in (x1,y1), punta arrotondata di raggio r2 in (x2,y2)."""
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    mx, my = x1 + dx * .55, y1 + dy * .55
    rm = (r1 + r2) / 2 + .6
    return ('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f A%.1f,%.1f 0 0 0 %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z' % (
        x1 + nx * r1, y1 + ny * r1, mx + nx * rm, my + ny * rm, x2 + nx * r2, y2 + ny * r2,
        r2, r2, x2 - nx * r2, y2 - ny * r2, mx - nx * rm, my - ny * rm, x1 - nx * r1, y1 - ny * r1))


def hand_back(cx, cy, s=1.0, palm=False):
    """Dorso della mano destra, dita verso l'alto (palm=True: palmo, senza unghie). (cx, cy) = centro del palmo."""
    o = ''
    segs = [(fx, -40, fx + a * 2.2, -46 - L, r) for fx, L, r, a in HAND_FINGERS]
    PALM = ('M-68,-44 C-66,-66 -40,-74 -6,-74 C30,-74 70,-70 78,-50 C82,-20 80,30 72,62 C64,88 50,100 40,104 '
            'L-36,104 C-52,98 -60,88 -66,70 C-74,40 -70,0 -68,-44 Z')
    # palmo/dorso, poi pollice e dita, poi copertura delle basi per un attacco senza cuciture
    o += '<path d="%s" fill="%s" stroke="%s" stroke-width="1.6"/>' % (PALM, SKIN, SKIN_D)
    o += '<path d="%s" fill="%s" stroke="%s" stroke-width="1.6"/>' % (_finger_path(-40, 66, -120, -20, 25, 15.5), SKIN, SKIN_D)
    for x1, y1, x2, y2, r in segs:
        o += '<path d="%s" fill="%s" stroke="%s" stroke-width="1.6"/>' % (_finger_path(x1, y1 + 10, x2, y2, r * 1.12, r * 0.9), SKIN, SKIN_D)
    cid = uid('hb')
    o += '<defs><clipPath id="%s"><path d="M-90,-40 C-60,-58 -20,-62 10,-60 C40,-60 70,-56 100,-44 L100,116 L-90,116 Z"/></clipPath></defs>' % cid
    o += '<path d="%s" fill="%s" clip-path="url(#%s)"/>' % (PALM, SKIN, cid)
    o += ('<path d="M-68,-44 C-70,0 -74,40 -66,70 C-60,88 -52,98 -36,104 M40,104 C50,100 64,88 72,62 C80,30 82,-20 78,-50" '
          'fill="none" stroke="%s" stroke-width="1.6"/>') % SKIN_D
    # polso
    o += '<path d="M-38,100 L-40,172 L40,172 L40,100 Z" fill="%s"/>' % SKIN
    o += '<path d="M-38,100 L-40,172 M40,100 L40,172" stroke="%s" stroke-width="1.6"/>' % SKIN_D
    o += '<path d="M-36,104 C-12,110 16,110 40,104" stroke="%s" stroke-width="1.1" fill="none" opacity=".45"/>' % SKIN_D
    for x1, y1, x2, y2, r in segs + [(-40, 66, -120, -20, 15.5)]:
        ux, uy = x2 - x1, y2 - y1
        Ln = math.hypot(ux, uy)
        ux, uy = ux / Ln, uy / Ln
        ang = math.degrees(math.atan2(uy, ux)) + 90
        # pieghe delle articolazioni
        for f in (0.45, 0.72):
            px, py = x1 + (x2 - x1) * f, y1 + (y2 - y1) * f
            o += '<path d="M%.1f,%.1f q%.1f,%.1f %.1f,0" stroke="%s" stroke-width="1.1" fill="none" opacity=".55" transform="rotate(%.1f %.1f %.1f)"/>' % (
                px - r * .5, py, r * .5, -r * .25 if not palm else r * .25, r, SKIN_D, ang, px, py)
        if palm:
            continue
        nx, ny = x2 - ux * r * 0.95, y2 - uy * r * 0.95
        o += ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s" stroke="%s" stroke-width="1.3" transform="rotate(%.1f %.1f %.1f)"/>'
              % (nx - r * 0.62, ny - r * 0.98, r * 1.24, r * 1.9, r * 0.58, NAIL, NAIL_S, ang, nx, ny))
        o += ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="#fff" opacity=".45" transform="rotate(%.1f %.1f %.1f)"/>'
              % (nx - r * 0.42, ny - r * 0.8, r * 0.22, r * 1.4, r * 0.11, ang, nx, ny))
    if palm:
        o += ('<path d="M-60,-30 Q-10,-46 72,-38 M-62,-2 Q0,-16 66,-6 M-30,92 Q-52,40 -46,-14" stroke="%s" stroke-width="1.8" fill="none" opacity=".6"/>' % SKIN_D)
    else:
        for k in range(4):
            fx = HAND_FINGERS[k][0]
            o += '<path d="M%.1f,-64 q5,8 0,16" stroke="%s" stroke-width="1.2" fill="none" opacity=".5"/>' % (fx, SKIN_D)
        o += '<path d="M-30,30 Q-6,10 0,-40 M10,30 Q16,0 18,-40" stroke="%s" stroke-width="1" fill="none" opacity=".25"/>' % SKIN_D
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
# ----------------------------------------------------------------- strumenti realistici (vista dall'alto / di lato)
STEEL, STEEL_D, STEEL_E = '#9aa3ad', '#6f7983', '#56606a'   # i primi due diventano sfumature metalliche


def _g(x, y, ang, s, inner):
    return '<g transform="translate(%.1f,%.1f) rotate(%.1f) scale(%.3f)">%s</g>' % (x, y, ang, s, inner)


def _knurl(x0, x1, y0, y1):
    """Zigrinatura dell'impugnatura (righe incrociate ritagliate sul manico)."""
    cid = uid('kn')
    o = '<defs><clipPath id="%s"><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f"/></clipPath></defs><g clip-path="url(#%s)" stroke="%s" stroke-width=".8" opacity=".55">' % (
        cid, x0, y0, x1 - x0, y1 - y0, cid, STEEL_E)
    h = y1 - y0
    xx = x0 - h
    while xx < x1 + h:
        o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/><line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (
            xx, y0, xx + h, y1, xx + h, y0, xx, y1)
        xx += 3.6
    return o + '</g>'


def _handle(x0=-46, x1=46, r=7):
    """Manico metallico zigrinato con anelli e riflesso."""
    o = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s" stroke="%s" stroke-width="1"/>' % (
        x0, -r, x1 - x0, 2 * r, r, STEEL, STEEL_E)
    o += _knurl(x0 + 12, x1 - 12, -r, r)
    for xx in (x0 + 9, x1 - 12):
        o += '<rect x="%.1f" y="%.1f" width="3" height="%.1f" fill="%s"/>' % (xx, -r, 2 * r, STEEL_D)
    o += '<rect x="%.1f" y="%.1f" width="%.1f" height="2.2" rx="1.1" fill="#fff" opacity=".6"/>' % (x0 + 4, -r + 2, x1 - x0 - 8)
    return o


def _neck(x0, x1, w0, w1):
    return '<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1"/>' % (
        x0, -w0, x0 + (x1 - x0) * .4, -w0 * .9, x0 + (x1 - x0) * .7, -w1, x1, -w1, x1, w1, x0 + (x1 - x0) * .7, w1, x0 + (x1 - x0) * .4, w0 * .9, x0, w0, STEEL, STEEL_E)


def double_pusher(x, y, s=1.0, ang=0):
    """Spingicuticole doppio: paletta arrotondata a destra, punta a scalpello a sinistra. Lungo ~150*s."""
    o = _neck(44, 78, 5, 2.2) + _neck(-44, -78, 5, 2.2)
    o += ('<path d="M76,-2.6 C82,-3 85,-8.5 94,-8.5 Q104,-8.5 104,0 Q104,8.5 94,8.5 C85,8.5 82,3 76,2.6 Z" fill="%s" stroke="%s" stroke-width="1"/>'
          '<path d="M88,-5.2 Q99,-5.6 100.5,0" fill="none" stroke="#fff" stroke-width="1.5" opacity=".75"/>'
          '<path d="M86,0 Q94,6 101,2" fill="none" stroke="%s" stroke-width=".9" opacity=".7"/>') % (STEEL, STEEL_E, STEEL_E)
    o += ('<path d="M-77,-2.6 L-91,-6.5 L-104,-4.5 L-104,4.5 L-91,6.5 L-77,2.6 Z" fill="%s" stroke="%s" stroke-width="1"/>'
          '<path d="M-100,-4 L-100,4" stroke="#fff" stroke-width="1.6" opacity=".8"/>') % (STEEL, STEEL_E)
    o += _handle()
    return _g(x, y, ang, s * 0.72, o)


def curette(x, y, s=1.0, ang=0):
    """Curetta doppia: due cucchiaini di misura diversa."""
    o = _neck(44, 82, 5, 1.8) + _neck(-44, -82, 5, 1.8)
    for cx, rx, ry in ((88, 7, 5.5), (-87, 5.5, 4.2)):
        o += ('<ellipse cx="%.1f" cy="0" rx="%.1f" ry="%.1f" fill="%s" stroke="%s" stroke-width="1.2"/>'
              '<ellipse cx="%.1f" cy=".6" rx="%.1f" ry="%.1f" fill="%s"/>'
              '<path d="M%.1f,%.1f q%.1f,-2 %.1f,0" stroke="#fff" stroke-width="1" fill="none" opacity=".8"/>') % (
            cx, rx, ry, STEEL, STEEL_E, cx, rx * .6, ry * .55, STEEL_E, cx - rx * .5, -ry * .55, rx * .5, rx)
    o += _handle()
    return _g(x, y, ang, s * 0.58, o)


def nipper(x, y, s=1.0, ang=0):
    """Tronchesine per pellicine viste di lato: becchi a destra, manici curvi con doppia molla a sinistra."""
    o = ''
    for sy in (-1, 1):
        # manico (leggermente bombato)
        o += ('<path d="M-6,%.1f C-34,%.1f -72,%.1f -110,%.1f Q-118,%.1f -117,%.1f Q-116,%.1f -108,%.1f C-72,%.1f -36,%.1f -6,%.1f Z" '
              'fill="%s" stroke="%s" stroke-width="1"/>') % (
            sy * 9, sy * 14, sy * 24, sy * 28, sy * 28, sy * 22, sy * 16.5, sy * 17, sy * 13, sy * 4, sy * 1.5, STEEL, STEEL_E)
        o += '<path d="M-16,%.1f C-44,%.1f -80,%.1f -106,%.1f" stroke="#fff" stroke-width="1.5" fill="none" opacity=".6"/>' % (
            sy * 8.5, sy * 13, sy * 20.5, sy * 23.5)
        # molla doppia (due lamine che si toccano al centro)
        o += '<path d="M-24,%.1f C-40,%.1f -56,%.1f -66,0" fill="none" stroke="%s" stroke-width="4" stroke-linecap="round"/>' % (
            sy * 6, sy * 10, sy * 8, STEEL_E)
        o += '<path d="M-24,%.1f C-40,%.1f -56,%.1f -66,0" fill="none" stroke="#c3cad1" stroke-width="2.2" stroke-linecap="round"/>' % (
            sy * 6, sy * 10, sy * 8)
        # becco
        o += ('<path d="M6,%.1f C20,%.1f 34,%.1f 44,%.1f L44,%.1f L6,%.1f Z" fill="%s" stroke="%s" stroke-width="1"/>') % (
            sy * 11, sy * 11, sy * 6.5, sy * 1.4, sy * .4, sy * .4, STEEL, STEEL_E)
        o += '<path d="M12,%.1f C22,%.1f 32,%.1f 40,%.1f" stroke="%s" stroke-width=".9" fill="none" opacity=".8"/>' % (
            sy * 4.5, sy * 4.5, sy * 3, sy * 1, STEEL_E)
    o += '<line x1="8" y1="0" x2="44" y2="0" stroke="#fff" stroke-width="1.2" opacity=".9"/>'
    o += '<circle cx="-66" cy="0" r="2.6" fill="%s"/>' % STEEL_E
    # snodo a scatola
    o += ('<rect x="-12" y="-12" width="22" height="24" rx="5" fill="%s" stroke="%s" stroke-width="1"/>'
          '<circle cx="-1" cy="0" r="4.6" fill="#d6dbe0" stroke="%s" stroke-width="1"/><line x1="-4" y1="-3" x2="2" y2="3" stroke="%s" stroke-width="1.3"/>') % (
        STEEL_D, STEEL_E, STEEL_E, STEEL_E)
    return _g(x, y, ang, s * 0.55, o)


def tip_cutter(x, y, s=1.0, ang=0, tip=True):
    """Tagliatip a ghigliottina visto di lato: testa con fessura e lama, raccoglitore trasparente, manici gommati."""
    o = ''
    for sy, y0, y1 in ((-1, 6, 24), (1, 6, 20)):
        o += '<path d="M-46,%.1f L70,%.1f Q78,%.1f 78,%.1f Q78,%.1f 70,%.1f L-46,%.1f Z" fill="%s" stroke="%s" stroke-width="1"/>' % (
            sy * y0, sy * y1, sy * y1, sy * (y1 + 6), sy * (y1 + 12), sy * (y1 + 12), sy * (y0 + 9), STEEL, STEEL_E)
        o += '<path d="M2,%.1f L70,%.1f Q80,%.1f 80,%.1f Q80,%.1f 70,%.1f L2,%.1f Q-3,%.1f 2,%.1f Z" fill="#d9799a" stroke="%s" stroke-width="1"/>' % (
            sy * (y0 + 4), sy * (y1 - 2), sy * (y1 - 2), sy * (y1 + 6), sy * (y1 + 14), sy * (y1 + 14), sy * (y0 + 14), sy * (y0 + 9), sy * (y0 + 4), NAIL_S)
        o += '<path d="M8,%.1f L70,%.1f" stroke="#fff" stroke-width="1.8" opacity=".5" stroke-linecap="round"/>' % (sy * (y0 + 6.5), sy * (y1 + 1))
    o += '<path d="M-40,-8 Q-16,-8 -16,0 Q-16,8 -40,8" fill="none" stroke="%s" stroke-width="2.6"/>' % STEEL_D
    o += '<rect x="-100" y="-20" width="58" height="40" rx="6" fill="%s" stroke="%s" stroke-width="1.1"/>' % (STEEL, STEEL_E)
    o += '<rect x="-96" y="-17" width="50" height="5" rx="2" fill="#fff" opacity=".45"/>'
    o += '<rect x="-101" y="-4" width="44" height="8" rx="1.5" fill="#3b4148"/>'
    o += '<path d="M-74,-20 L-64,-20 L-64,1 L-70,5 L-74,1 Z" fill="#e9edf1" stroke="%s" stroke-width="1"/>' % STEEL_E
    o += '<circle cx="-48" cy="0" r="3.4" fill="#d6dbe0" stroke="%s"/>' % STEEL_E
    o += '<path d="M-98,20 L-98,32 Q-98,38 -92,38 L-52,38 Q-46,38 -46,32 L-46,20 Z" fill="#dff0f7" fill-opacity=".7" stroke="#7fb0cc" stroke-width="1.2"/>'
    if tip:
        o += '<path d="M-128,-3 L-90,-3 L-90,3 L-128,3 Q-133,0 -128,-3 Z" fill="#fff" stroke="#c9a3b1" stroke-width="1.2"/>'
    return _g(x, y, ang, s * 0.68, o)


def tweezers(x, y, s=1.0, ang=0):
    """Pinzette a punta obliqua: molla a destra, punte a sinistra."""
    o = ''
    for sy in (-1, 1):
        o += ('<path d="M100,%.1f L-24,%.1f L-88,%.1f L-100,%.1f L-96,%.1f L-86,%.1f L-24,%.1f L98,%.1f Z" fill="%s" stroke="%s" stroke-width="1"/>') % (
            sy * 6, sy * 15, sy * 6.5, sy * (2.4 if sy < 0 else 5.5), sy * .5, sy * 1, sy * 6, sy * .6, STEEL, STEEL_E)
        o += '<path d="M90,%.1f L-22,%.1f" stroke="#fff" stroke-width="1.4" opacity=".6"/>' % (sy * 4, sy * 12.4)
        for k in range(7):
            xx = -4 - k * 5
            o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width=".9" opacity=".7"/>' % (
                xx, sy * (6.6 - k * .1), xx, sy * (14.4 - k * .9), STEEL_E)
    o += '<path d="M96,-6.5 Q107,-6.5 107,0 Q107,6.5 96,6.5 Z" fill="%s" stroke="%s"/>' % (STEEL_D, STEEL_E)
    return _g(x, y, ang, s * 0.7, o)


def cuticle_scissors(x, y, s=1.0, ang=0):
    """Forbicine con lame curve (punte a sinistra) e anelli a destra."""
    o = ''
    for sy in (-1, 1):
        # gambo e anello
        o += '<path d="M2,%.1f C20,%.1f 32,%.1f 44,%.1f" fill="none" stroke="%s" stroke-width="5.5" stroke-linecap="round"/>' % (
            sy * 2, sy * 4, sy * 9, sy * 13, STEEL_E)
        o += '<path d="M2,%.1f C20,%.1f 32,%.1f 44,%.1f" fill="none" stroke="#b8c0c8" stroke-width="3.6" stroke-linecap="round"/>' % (
            sy * 2, sy * 4, sy * 9, sy * 13)
        o += '<ellipse cx="60" cy="%.1f" rx="16" ry="11" fill="none" stroke="%s" stroke-width="5.6"/>' % (sy * 16, STEEL_E)
        o += '<ellipse cx="60" cy="%.1f" rx="16" ry="11" fill="none" stroke="#b8c0c8" stroke-width="3.6"/>' % (sy * 16)
    # lame curve
    o += ('<path d="M6,-4.5 C-24,-6 -62,-6 -96,-16 Q-100,-16 -98,-12 C-64,-1 -26,3 6,2 Z" fill="%s" stroke="%s" stroke-width="1"/>'
          '<path d="M6,4.5 C-24,5 -60,2 -94,-12 Q-97,-10 -95,-8 C-62,8 -24,10 6,9 Z" fill="%s" stroke="%s" stroke-width="1" opacity=".95"/>'
          '<path d="M0,-2.4 C-30,-3 -62,-4 -92,-13" stroke="#fff" stroke-width="1.2" fill="none" opacity=".7"/>') % (STEEL, STEEL_E, STEEL_D, STEEL_E)
    o += '<circle cx="2" cy="0" r="4.6" fill="#d6dbe0" stroke="%s" stroke-width="1.1"/><line x1="-.8" y1="-2.4" x2="4.8" y2="2.4" stroke="%s"/>' % (STEEL_E, STEEL_E)
    return _g(x, y, ang, s * 0.7, o)


def orange_stick(x, y, s=1.0, ang=0):
    """Bastoncino d'arancio: estremità a scalpello (sinistra) e a punta (destra), venatura del legno."""
    o = ('<path d="M-92,-3 L-80,-5.5 L84,-5.5 L102,0 L84,5.5 L-80,5.5 L-100,4.5 Z" fill="#e7c796" stroke="#b08a5a" stroke-width="1.1"/>'
         '<path d="M-92,-3 L-80,-5.5 L-80,5.5 L-100,4.5 Z" fill="#d4ad75"/>'
         '<path d="M84,-5.5 L102,0 L84,0 Z" fill="#f1d9b2"/>')
    for k, (yy, a, b2) in enumerate(((-2.5, -70, 40), (0.5, -40, 76), (3, -76, 10), (-1, 20, 70))):
        o += '<path d="M%d,%.1f Q%d,%.1f %d,%.1f" stroke="#b08a5a" stroke-width=".8" fill="none" opacity=".6"/>' % (a, yy, (a + b2) / 2, yy + (1 if k % 2 else -1), b2, yy)
    return _g(x, y, ang, s * 0.72, o)


def cleaning_brush(x, y, s=1.0, ang=0):
    """Spazzolino per unghie di lato: impugnatura sagomata e ciuffi di setole."""
    o = ''
    for k in range(12):
        cx = -64 + k * 11.6
        for j in range(5):
            dx = (j - 2) * 1.5
            o += '<line x1="%.1f" y1="3" x2="%.1f" y2="23" stroke="%s" stroke-width="1.1" stroke-linecap="round"/>' % (
                cx + dx, cx + dx * 1.8, '#e6dcc4' if j % 2 else '#fbf7ec')
    o += '<path d="M-74,-6 Q-74,-20 -56,-20 L56,-20 Q76,-20 76,-6 L76,0 L-74,0 Z" fill="#3f86b8" stroke="#2c6690" stroke-width="1.2"/>'
    o += '<path d="M-30,-20 Q0,-29 30,-20" fill="#3f86b8" stroke="#2c6690" stroke-width="1.2"/>'
    o += '<path d="M-62,-14 L58,-14" stroke="#fff" stroke-width="2.4" opacity=".45" stroke-linecap="round"/>'
    o += '<rect x="-74" y="0" width="150" height="4" rx="1" fill="#2c6690"/>'
    return _g(x, y, ang, s * 0.66, o)


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


# ----------------------------------------------------------------- fresa: punte e manipolo realistici
BIT_MAT = {'carburo': ('#a7afb8', '#56606a'), 'diamantata': ('#d9b453', '#8a6d1f'), 'ceramica': ('#f3eee9', '#a99f96')}
GRIT_COL = {'XF': '#f1d27a', 'F': '#d9534f', 'M': '#3f6fe0', 'G': '#3d9a5c', 'XG': '#2b2b2b'}


def _bit_outline(shape):
    """Contorno della testa (lavoro verso x negativo, attacco al gambo in x=0)."""
    return {
        'cil': 'M0,-8 L-34,-8 Q-36,-8 -36,-6 L-36,6 Q-36,8 -34,8 L0,8 Z',
        'sic': 'M0,-8 L-28,-8 Q-36,-8 -36,0 Q-36,8 -28,8 L0,8 Z',
        'cono': 'M0,-8.5 L-36,-2.6 Q-38,0 -36,2.6 L0,8.5 Z',
        'fiamma': 'M0,-4 C-6,-9 -18,-10 -26,-5 C-31,-2 -36,-.6 -42,0 C-36,.6 -31,2 -26,5 C-18,10 -6,9 0,4 Z',
        'palla': 'M0,-2.6 L-6,-2.6 A8,8 0 1 0 -6,2.6 L0,2.6 Z',
        'ago': 'M0,-4.2 L-40,-.8 Q-43,0 -40,.8 L0,4.2 Z',
    }[shape]


def bit_r(x, y, s=1.0, ang=0, shape='cil', mat='carburo', grit='M', shank=46):
    """Punta per fresa realistica: testa a sinistra (x negativo), gambo da 2,35 mm verso destra, anello colorato della grana."""
    col, dk = BIT_MAT[mat]
    out = _bit_outline(shape)
    cid = uid('bt')
    o = '<defs><clipPath id="%s"><path d="%s"/></clipPath></defs>' % (cid, out)
    # gambo
    o += '<rect x="-1" y="-2.7" width="%.1f" height="5.4" rx="1" fill="%s" stroke="%s" stroke-width=".8"/>' % (shank, STEEL, STEEL_E)
    o += '<rect x="0" y="-1.8" width="%.1f" height="1.2" fill="#fff" opacity=".6"/>' % (shank - 2)
    o += '<rect x="5" y="-3.4" width="7" height="6.8" rx="1" fill="%s" stroke="%s" stroke-width=".6"/>' % (GRIT_COL.get(grit, grit), STEEL_E)
    # testa
    o += '<path d="%s" fill="%s" stroke="%s" stroke-width="1"/>' % (out, col, dk)
    tex = ''
    if mat == 'carburo' or mat == 'ceramica':
        step = 3.6 if mat == 'carburo' else 5
        xx = -50
        while xx < 12:
            tex += '<line x1="%.1f" y1="-12" x2="%.1f" y2="12" stroke="%s" stroke-width="%.1f"/>' % (xx, xx + 7, dk, 1.1 if mat == 'carburo' else .8)
            xx += step
        if mat == 'carburo':
            xx = -50
            while xx < 12:
                tex += '<line x1="%.1f" y1="-12" x2="%.1f" y2="12" stroke="%s" stroke-width=".5" opacity=".6"/>' % (xx + 7, xx, dk)
                xx += step
    else:
        rnd = random.Random(7 + len(shape))
        for _ in range(70):
            px, py = rnd.uniform(-44, 0), rnd.uniform(-9, 9)
            tex += '<circle cx="%.1f" cy="%.1f" r="%.2f" fill="%s" opacity=".8"/>' % (px, py, rnd.uniform(.5, 1.1), dk if rnd.random() < .6 else '#fff6d5')
    if shape == 'sic':
        tex += '<path d="M-28,-8 Q-36,-8 -36,0 Q-36,8 -28,8 L-27,8 L-27,-8 Z" fill="%s"/>' % col   # punta liscia
    o += '<g clip-path="url(#%s)">%s<rect x="-50" y="-7" width="60" height="3.4" fill="#fff" opacity=".45"/></g>' % (cid, tex)
    o += '<path d="%s" fill="none" stroke="%s" stroke-width="1"/>' % (out, dk)
    return _g(x, y, ang, s, o)


def handpiece_r(x, y, ang=0, s=1.0, shape='cil', mat='carburo', grit='M', cord=True, body='#e7e3ec'):
    """Manipolo della fresa con punta; (x, y) = attacco testa-gambo della punta, il manipolo va verso x positivo."""
    g = uid('hp')
    o = ('<defs><linearGradient id="%s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset=".35" stop-color="%s"/>'
         '<stop offset="1" stop-color="#a59cb3"/></linearGradient></defs>') % (g, body)
    if cord:
        o += '<path d="M232,0 C262,0 276,10 292,30" fill="none" stroke="#4b3a40" stroke-width="5" stroke-linecap="round"/>'
        o += '<rect x="210" y="-5" width="26" height="10" rx="4" fill="#4b3a40"/>'
        for k in range(4):
            o += '<line x1="%d" y1="-5" x2="%d" y2="5" stroke="#6d5a62" stroke-width="1.2"/>' % (214 + k * 6, 214 + k * 6)
    # corpo
    o += '<path d="M58,-12 L190,-12 C202,-12 212,-8 214,0 C212,8 202,12 190,12 L58,12 Z" fill="url(#%s)" stroke="#7d7290" stroke-width="1.2"/>' % g
    for k in range(7):
        o += '<rect x="%d" y="-12" width="2.4" height="24" rx="1" fill="#7d7290" opacity=".35"/>' % (66 + k * 6)
    o += '<rect x="120" y="-12" width="3" height="24" fill="#7d7290" opacity=".5"/>'
    o += '<rect x="62" y="-8.5" width="146" height="3" rx="1.5" fill="#fff" opacity=".7"/>'
    # mandrino (naso) e ghiera
    o += '<path d="M30,-4.5 L48,-9 L58,-10.5 L58,10.5 L48,9 L30,4.5 Z" fill="%s" stroke="%s" stroke-width="1"/>' % (STEEL, STEEL_E)
    o += '<rect x="46" y="-10" width="4" height="20" fill="%s"/>' % STEEL_D
    o += '<rect x="32" y="-3" width="20" height="1.6" fill="#fff" opacity=".6"/>'
    o += bit_r(0, 0, 1.0, 0, shape, mat, grit, shank=34)
    return _g(x, y, ang, s, o)


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
        o += nipper(x + w * 0.46, y + h * 0.34, 0.95 * w / 150, 0) + double_pusher(x + w * 0.42, y + h * 0.7, 0.85 * w / 150, 0)
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
            b += file_r('dritta', x + 52, iy - 2, '#8f8379', '#2f2a28', ('', ''), -20, 0.55, seed=11)
            b += file_r('buffer', x + 112, iy + 2, '', '', ('', ''), 0, 0.42)
            b += orange_stick(x + 162, iy + 4, 0.42, -35)
            b += bin_pedal(x + 220, iy + 24, 32, 36)
        elif k == 1:
            b += glass_file(x + 58, iy, -20, 0.6)
            b += bowl(x + 132, iy - 8, 54)
            b += glasses(x + 202, iy, 0.75)
        else:
            b += nipper(x + 66, iy - 10, 0.8, -12) + double_pusher(x + 68, iy + 22, 0.58, -12)
            b += bit_r(x + 150, iy, 0.9, -30, 'cil', 'carburo', 'M', shank=40)
            b += autoclave_icon(x + 214, iy, 0.5)
        for j, it in enumerate(items[k]):
            yy = 210 + j * 24
            b += '<circle cx="%d" cy="%d" r="4" fill="%s"/>' % (x + 20, yy - 4, c)
            b += text(x + 32, yy, it, 13, 'start', 600)
    b += '<rect x="20" y="366" width="760" height="46" rx="12" fill="#fbe9e7"/>'
    b += file_r('dritta', 62, 388, '#8f8379', '#2f2a28', ('', ''), 0, 0.4, seed=12) + magnifier(70, 384, 13)
    b += text(110, 395, 'Poroso = monouso:', 16, 'start', 900, ERR)
    b += text(270, 395, 'lime in carta e buffer non si disinfettano, anche se "lavabili".', 14, 'start', 600)
    return svg(800, 420, b, 'Classificazione degli strumenti: monouso, da disinfettare, da sterilizzare')


@figx('autoclave-busta.svg')
def autoclave_busta():
    b = title('Busta sterile e autoclave: cosa controllare')
    px, py, pw, ph = 24, 70, 300, 170
    b += pouch(px, py, pw, ph, False)
    b += nipper(px + 150, py + 60, 1.3, 0) + double_pusher(px + 128, py + 116, 1.3, 0)
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
    # icone ai lati, in medaglioni
    for i in range(4):
        b += '<circle cx="52" cy="%d" r="34" fill="#fff" stroke="%s" stroke-width="2" filter="url(#nxShS)"/>' % (103 + i * 86, cols[i])
    ic = ''
    ic += '<g transform="translate(66,128) scale(.42)">%s</g>' % gel_bottle(0, 0, 70, 90)
    ic += mark(88, 84, True, 10)
    # aspiratore da tavolo che aspira la polvere
    ic += '<rect x="38" y="196" width="56" height="18" rx="4" fill="#dfe3e8" stroke="%s" stroke-width="1.6"/>' % GREY_D
    ic += ''.join('<rect x="%d" y="199" width="3.5" height="12" rx="1.5" fill="%s"/>' % (43 + j * 7, GREY) for j in range(7))
    ic += ''.join('<path d="M%d,172 L%d,190" stroke="%s" stroke-width="2" marker-end="url(#ar)"/>' % (50 + j * 16, 50 + j * 16, ACC2) for j in range(3))
    ic += dust(66, 170, 7, 22, '#a9b2ba', 4)
    # finestra aperta con aria
    ic += '<rect x="44" y="254" width="40" height="44" fill="#e6f1f8" stroke="%s" stroke-width="2.2"/>' % GREY_D
    ic += '<path d="M64,254 L64,298 M44,276 L84,276" stroke="%s" stroke-width="1.8"/>' % GREY_D
    ic += '<path d="M84,254 L96,260 L96,304 L84,298 Z" fill="#cfe3f0" stroke="%s" stroke-width="1.6"/>' % GREY_D
    ic += '<path d="M40,262 q-6,6 0,12 M38,282 q-6,6 0,12" stroke="#7fb0cc" stroke-width="2" fill="none" stroke-linecap="round"/>'
    # DPI
    ic += glove(52, 368, 0.42, -10) + glasses(80, 348, 0.48)
    ic += '<path d="M64,372 Q82,362 100,372 L96,386 Q82,392 68,386 Z" fill="#f7f7f7" stroke="%s" stroke-width="1.4"/>' % GREY
    b += '<g transform="translate(-14,0)">%s</g>' % ic
    # freccia di efficacia
    b += '<defs><linearGradient id="eff" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="#f3c4d3"/></linearGradient></defs>' % OK
    b += '<rect x="690" y="70" width="14" height="306" rx="7" fill="url(#eff)"/>'
    b += text(697, 56, 'Più efficace', 13, weight=800, fill=OK)
    b += text(697, 400, 'Ultima barriera', 13, weight=800, fill=ACC2)
    return svg(760, 420, arrow_defs() + b, 'Gerarchia della protezione: prodotti, aspirazione, ventilazione, DPI')


def client_hand_side(x, y, s=1.0, col=SKIN, stroke=SKIN_D):
    """Mano della cliente vista di lato, appoggiata, dita verso destra (y = piano d'appoggio)."""
    o = ('<path d="M-70,0 L-70,-27 C-56,-35 -36,-39 -16,-37 C4,-35 20,-31 36,-27 C50,-24 60,-21 66,-15 C71,-10 68,-3 60,-2 L-70,0 Z" '
         'fill="%s" stroke="%s" stroke-width="1.6" stroke-linejoin="round"/>') % (col, stroke)
    o += '<path d="M48,-25 C54,-25 62,-22 66,-17 L60,-15 C56,-18 52,-19 47,-20 Z" fill="%s" stroke="%s" stroke-width="1.2"/>' % (NAIL, NAIL_S)
    o += ('<path d="M-34,-18 C-14,-24 6,-22 20,-14 C25,-10 21,-6 15,-7 C0,-9 -16,-8 -30,-6 Z" fill="%s" stroke="%s" stroke-width="1.3" opacity=".95"/>' % (col, stroke))
    o += '<path d="M14,-13 C18,-14 22,-12 22,-9 L16,-8 Z" fill="%s" stroke="%s" stroke-width="1"/>' % (NAIL, NAIL_S)
    o += '<path d="M-6,-36 Q0,-30 -4,-24 M22,-31 Q27,-26 24,-21" stroke="%s" stroke-width="1.2" fill="none" opacity=".7"/>' % stroke
    return '<g transform="translate(%.1f,%.1f) scale(%.2f)">%s</g>' % (x, y, s, o)


def operator(x, y, s=1.0, bent=False, mask=True, specs=True):
    """Busto dell'operatrice di profilo, rivolta a destra. (x, y) = base del busto."""
    hx, hy = (30, -128) if bent else (0, -140)
    o = '<g transform="translate(%.1f,%.1f) scale(%.2f)">' % (x, y, s)
    # collo
    o += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.4"/>' % (
        hx - 12, hy + 14, hx + 10, hy + 14, hx + 12 - (6 if bent else 0), -100, hx - 14, -100, SKIN, SKIN_D)
    # busto con casacca
    o += ('<path d="M-42,0 L-40,-78 C-38,-102 -20,-112 %.1f,-114 C%.1f,-112 %.1f,-100 %.1f,-84 L40,0 Z" fill="#9fc3dc" stroke="#5f8fb0" stroke-width="1.6"/>'
          % (hx - 2, hx + 20, hx + 34, hx + 34 if bent else 36))
    o += '<path d="M%.1f,-112 L%.1f,-92 L%.1f,-110" fill="none" stroke="#5f8fb0" stroke-width="1.6"/>' % (hx - 8, hx + 2, hx + 12)
    # testa e capelli raccolti
    o += '<circle cx="%.1f" cy="%.1f" r="12" fill="#5a3a2e"/>' % (hx - 26, hy - 14)
    o += '<circle cx="%.1f" cy="%.1f" r="26" fill="%s" stroke="%s" stroke-width="1.6"/>' % (hx, hy, SKIN, SKIN_D)
    o += '<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z" fill="#5a3a2e"/>' % (
        hx - 27, hy + 6, hx - 30, hy - 30, hx + 8, hy - 36, hx + 24, hy - 14, hx + 10, hy - 20, hx - 6, hy - 14, hx - 12, hy + 8)
    o += '<path d="M%.1f,%.1f q5,-6 4,4" fill="%s" stroke="%s" stroke-width="1.2"/>' % (hx - 6, hy - 2, SKIN, SKIN_D)
    if specs:
        o += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="2"/>' % (hx - 4, hy - 6, hx + 14, hy - 6, INK)
        o += '<rect x="%.1f" y="%.1f" width="13" height="12" rx="4" fill="#e8f3fb" fill-opacity=".8" stroke="%s" stroke-width="2"/>' % (hx + 14, hy - 11, INK)
    if mask:
        o += ('<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z" fill="#f7f7f7" stroke="%s" stroke-width="1.4"/>'
              % (hx + 6, hy + 2, hx + 20, hy - 2, hx + 34, hy + 2, hx + 32, hy + 12, hx + 30, hy + 20, hx + 20, hy + 26, hx + 8, hy + 22,
                 hx + 2, hy + 16, hx + 2, hy + 8, hx + 6, hy + 2, GREY))
        o += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="1.4"/>' % (hx + 6, hy + 6, hx - 18, hy - 2, GREY)
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
    if not fist:
        fingers = [(-15, -48, 7.2), (-5, -57, 7.6), (5, -54, 7.6), (15, -43, 6.8)]
    else:
        fingers = [(-15, -27, 7.4), (-5, -30, 7.8), (5, -29, 7.8), (15, -25, 7)]
    PALM = 'M-24,-12 C-25,-24 -18,-28 0,-28 C18,-28 25,-24 25,-12 L24,14 C23,24 16,28 0,28 C-16,28 -23,24 -24,14 Z'
    o += '<path d="%s" fill="%s" stroke="%s" stroke-width="1.6"/>' % (PALM, col, stroke)
    o += '<path d="%s" fill="%s" stroke="%s" stroke-width="1.6"/>' % (_finger_path(-14, 10, -35, -16, 9.5, 7), col, stroke)
    for fx, ty, r in fingers:
        o += '<path d="%s" fill="%s" stroke="%s" stroke-width="1.6"/>' % (_finger_path(fx, -16, fx + fx * .06, ty, r * 1.05, r * .92), col, stroke)
    cid = uid('gv')
    o += '<defs><clipPath id="%s"><path d="M-30,-20 Q0,-30 30,-20 L30,40 L-30,40 Z"/></clipPath></defs>' % cid
    o += '<path d="%s" fill="%s" clip-path="url(#%s)"/>' % (PALM, col, cid)
    o += '<path d="M-24,-12 L-24,14 C-23,24 -16,28 0,28 C16,28 23,24 24,14 L25,-12" fill="none" stroke="%s" stroke-width="1.6"/>' % stroke
    if fist:
        for fx, ty, r in fingers:
            o += '<path d="M%.1f,%.1f q%.1f,%.1f %.1f,0" stroke="%s" stroke-width="1.2" fill="none" opacity=".7"/>' % (fx - r * .7, ty + r * 1.4, r * .7, r * .6, r * 1.4, stroke)
    o += '<path d="M-14,-2 Q0,-8 14,-2" stroke="#fff" stroke-width="1.6" fill="none" opacity=".35"/>'
    if col == NITR:
        o += '<path d="M-10,-24 L-10,10" stroke="#fff" stroke-width="3" opacity=".25" stroke-linecap="round"/>'
    if cuff:
        o += '<path d="M-21,24 L-23,46 L23,46 L21,24 Z" fill="%s" stroke="%s" stroke-width="1.6"/>' % (col, stroke)
        o += '<rect x="-24" y="42" width="48" height="6" rx="3" fill="%s" stroke="%s" stroke-width="1.4"/>' % (col, stroke)
    else:
        o += '<path d="M-18,24 L-18,46 L18,46 L18,24 Z" fill="%s"/>' % col
        o += '<path d="M-18,24 L-18,46 M18,46 L18,24" stroke="%s" stroke-width="1.6"/>' % stroke
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
    hair = '#6b4434'
    o += '<circle cx="64" cy="-70" r="17" fill="%s"/>' % hair
    o += ('<path d="M-30,-90 C-40,-80 -44,-66 -42,-54 C-42,-48 -44,-45 -46,-42 C-50,-34 -56,-24 -62,-14 Q-65,-9 -60,-7 '
          'C-56,-5 -53,-6 -50,-4 Q-54,0 -52,3 Q-49,5 -51,8 Q-54,12 -50,15 C-47,20 -50,24 -46,28 C-42,34 -32,36 -22,34 '
          'C-12,33 -6,36 -2,44 L2,80 L58,80 L54,30 C70,10 74,-20 70,-44 C66,-80 40,-104 6,-102 C-10,-102 -22,-98 -30,-90 Z" '
          'fill="%s" stroke="%s" stroke-width="1.8" stroke-linejoin="round"/>') % (SKIN, SKIN_D)
    o += ('<path d="M-30,-92 C-10,-108 42,-108 62,-80 C76,-60 76,-28 62,-8 C58,-2 54,4 48,8 L42,-22 C38,-48 20,-62 -2,-64 '
          'C-16,-64 -30,-60 -41,-54 C-42,-70 -38,-84 -30,-92 Z" fill="%s"/>') % hair
    o += ('<path d="M20,-34 C30,-40 38,-30 36,-18 C35,-8 28,-4 22,-8 C26,-14 28,-24 20,-34 Z" fill="%s" stroke="%s" stroke-width="1.5"/>' % (SKIN, SKIN_D))
    o += '<path d="M-38,-50 Q-30,-56 -20,-52" stroke="#5a3a2e" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
    o += '<path d="M-36,-40 Q-29,-46 -21,-41 Q-28,-36 -36,-40 Z" fill="#fff" stroke="%s" stroke-width="1.3"/><circle cx="-31" cy="-41" r="2.6" fill="%s"/>' % (INK, INK)
    o += '<path d="M-37,-41 Q-29,-47 -20,-42" stroke="%s" stroke-width="1.8" fill="none"/>' % INK
    o += '<path d="M-52,3 Q-49,5 -51,8 Q-54,12 -50,15 Q-47,10 -48,4 Z" fill="#d97a8f"/>'
    o += '<path d="M-56,-10 Q-52,-8 -50,-12" stroke="%s" stroke-width="1.2" fill="none"/>' % SKIN_D
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
    b += gel_bottle(113, 350, 112, 196)
    b += text(113, 200, 'BUILDER', 13, weight=900, fill=ACC2) + text(113, 220, 'GEL', 13, weight=900, fill=ACC2)
    b += '<line x1="80" y1="232" x2="146" y2="232" stroke="#ead7dd"/>'
    b += lines_block(82, 248, 62, 4, 9)
    b += text(113, 316, '15 ml', 12, weight=700, fill=MUTED)
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
            b += mini(None, cx - 10, 196, 0.95)
            b += '<path d="M%.1f,%.1f q4,8 0,16" stroke="#c62828" stroke-width="2.4" fill="none"/>' % (cx + 22, 174)
            b += drop_icon(cx + 34, 214, 0.5, '#c62828')
            b += ('<g transform="rotate(-12 %.1f %.1f)"><rect x="%.1f" y="%.1f" width="40" height="36" rx="3" fill="#fff" stroke="%s" stroke-width="1.4"/>'
                  % (cx + 26, 180, cx + 6, 162, GREY))
            for k in range(5):
                b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#e3e7eb" stroke-width="1.2"/>' % (cx + 8, 168 + k * 6, cx + 44, 168 + k * 6)
                b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#e3e7eb" stroke-width="1.2"/>' % (cx + 12 + k * 7, 164, cx + 12 + k * 7, 196)
            b += '</g>'
            b += glove(cx + 46, 132, 0.78, -150)
            b += carrow(cx + 70, 150, cx + 54, 170, ACC2, 2)
        elif i == 1:
            b += bottle(cx - 30, 222, 54, 88, '#eaf3f9', '', 12)
            b += first_aid(cx - 30, 180, 13)
            b += mtext(cx - 30, 242, ['disinfettante', 'per cute lesa'], 12, weight=600, fill=MUTED)
            b += ('<g transform="rotate(-30 %.1f %.1f)"><rect x="%.1f" y="%.1f" width="78" height="26" rx="13" fill="#f0c9a6" stroke="#c99a74" stroke-width="1.5"/>'
                  '<rect x="%.1f" y="%.1f" width="28" height="20" rx="4" fill="#fbe9dc" stroke="#e2c3a8"/>' % (cx + 40, 170, cx + 2, 157, cx + 27, 160))
            for k in range(4):
                b += '<circle cx="%.1f" cy="%.1f" r="1.3" fill="#c99a74"/><circle cx="%.1f" cy="%.1f" r="1.3" fill="#c99a74"/>' % (cx + 10 + k * 4, 166 + (k % 2) * 6, cx + 62 + k * 4, 166 + (k % 2) * 6)
            b += '</g>'
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


def foil_finger(cx, cy, s=1.0):
    """Dito avvolto nella stagnola con cotone imbevuto (vista dall'alto, punta in alto)."""
    o = '<path d="M-20,60 L-20,-10 A20,20 0 0 1 20,-10 L20,60 Z" fill="%s" stroke="%s" stroke-width="1.5"/>' % (SKIN, SKIN_D)
    o += ('<path d="M-25,22 L-24,-14 C-24,-34 -10,-40 0,-40 C12,-40 25,-32 24,-14 L26,22 L16,26 L8,20 L-2,27 L-12,21 Z" '
          'fill="#d9dee3" stroke="%s" stroke-width="1.5" stroke-linejoin="round"/>') % GREY_D
    o += '<path d="M-14,-26 L-4,-14 L-12,0 M6,-32 L2,-16 L12,-6 M-18,8 L-6,12 M10,8 L18,14" stroke="#fff" stroke-width="1.6" fill="none"/>'
    o += '<path d="M-14,-24 L-6,-12 M4,-30 L1,-18" stroke="#a9b2ba" stroke-width="1" fill="none"/>'
    return '<g transform="translate(%.1f,%.1f) scale(%.2f)">%s</g>' % (cx, cy, s, o)


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
    b += bowl(262, 166, 54) + foil_finger(334, 178, 0.8)
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
    b += file_r('dritta', 650, 172, '#8f8379', '#2f2a28', ('', ''), -16, 0.72, seed=41)
    b += handpiece_r(610, 216, -8, 0.5, 'cil', 'carburo', 'M', cord=True)
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
            b += gel_pot(jx, 140, 46, 30, c)
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
    """Dappen dish in vetro: pareti spesse, liquido con menisco, riflessi."""
    o = '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="#eef6fb" stroke="%s" stroke-width="1.8" stroke-linejoin="round"/>' % (
        cx - w / 2, base - h, cx + w / 2, base - h, cx + w / 2 - 6, base, cx - w / 2 + 6, base, GREY_D)
    lh = h * liquid
    o += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="#bcdcf1" opacity=".9"/>' % (
        cx - w / 2 + 5 + 6 * (1 - liquid), base - lh, cx, base - lh + 4, cx + w / 2 - 5 - 6 * (1 - liquid), base - lh, cx + w / 2 - 10, base - 6, cx - w / 2 + 10, base - 6)
    o += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f" fill="none" stroke="#a9c3d6" stroke-width="1.2"/>' % (
        cx - w / 2 + 5, base - h + 2, cx - w / 2 + 10, base - 6, cx + w / 2 - 10, base - 6, cx + w / 2 - 5, base - h + 2)
    o += '<rect x="%.1f" y="%.1f" width="%.1f" height="4" rx="2" fill="#fff" opacity=".9"/>' % (cx - w / 2 + 2, base - h, w - 4)
    o += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>' % (cx - w / 2 + 9, base - h + 8, cx - w / 2 + 12, base - 10)
    if lid:
        o += '<rect x="%.1f" y="%.1f" width="%.1f" height="10" rx="4" fill="%s"/>' % (cx - w / 2 - 4, base - h - 12, w + 8, ACC2)
        o += '<rect x="%.1f" y="%.1f" width="%.1f" height="3" rx="1.5" fill="#fff" opacity=".35"/>' % (cx - w / 2, base - h - 10, w)
    return o


def powder_jar(cx, base, w=70, h=44, col='#f6d6df', label='', lid=False):
    """Barattolo di polvere in vetro con cumulo di polvere (lid=True: con coperchio)."""
    o = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="8" fill="#fbfdff" stroke="%s" stroke-width="1.8"/>' % (cx - w / 2, base - h, w, h, GREY_D)
    o += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="%s"/>' % (
        cx - w / 2 + 3, base - h * 0.5, cx, base - h * 0.78, cx + w / 2 - 3, base - h * 0.5, cx + w / 2 - 3, base - 8, cx + w / 2 - 3, base - 3, cx - w / 2 + 8, base - 3, col)
    o += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="#fff" stroke-width="2" fill="none" opacity=".7"/>' % (
        cx - w * 0.3, base - h * 0.55, cx - w * 0.1, base - h * 0.68, cx + w * 0.1, base - h * 0.66)
    o += '<rect x="%.1f" y="%.1f" width="5" height="%.1f" rx="2.5" fill="#fff" opacity=".8"/>' % (cx - w / 2 + 5, base - h + 5, h - 12)
    if lid:
        o += '<rect x="%.1f" y="%.1f" width="%.1f" height="12" rx="4" fill="#3b2a30"/>' % (cx - w / 2 - 2, base - h - 11, w + 4)
        o += '<rect x="%.1f" y="%.1f" width="%.1f" height="3" rx="1.5" fill="#fff" opacity=".25"/>' % (cx - w / 2 + 2, base - h - 9, w - 4)
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
    b += powder_jar(546, 250, 76, 56, '#f6d6df', lid=True)
    items_p = ['Perline di PMMA', 'Iniziatore BPO', 'Pigmenti']
    for k, t in enumerate(items_p):
        b += '<circle cx="600" cy="%d" r="4" fill="%s"/>' % (130 + k * 30, ACC)
        b += text(610, 135 + k * 30, t, 13.5, 'start', 700)
    b += ''.join('<circle cx="%d" cy="%d" r="4" fill="#fff" stroke="%s"/>' % (530 + (k % 4) * 10, 222 + (k // 4) * 9, ACC) for k in range(8))
    # centro
    b += tool_brush(396, 168, -28, 76, '#e9d6c0')
    b += bead(370, 184, 20, '#f9e3ea')
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
            b += bottle(cx + 54, 200, 36, 58, '#e6f1f8', 'EMA', 12)
        elif i == 1:
            b += dappen(cx, 210, 70, 46, 0.5)
            b += tool_brush(cx + 2, 188, -100, 64, '#e9d6c0')
        elif i == 2:
            b += dappen(cx, 210, 70, 46, 0.5)
            b += tool_brush(cx + 30, 160, -125, 64, '#e9d6c0')
            b += drop_icon(cx + 31, 184, 0.45, '#9cc7e0')
            b += text(cx - 40, 152, 'sul bordo', 12, weight=700, fill=ACC2)
        else:
            b += powder_jar(cx, 214, 96, 50, '#f6d6df')
            b += tool_brush(cx + 30, 160, -150, 64, '#e9d6c0')
            b += bead(cx + 2, 174, 12, '#fbeef2')
        b += mtext(cx, 256, wrap(lab, W - 20, 13.5, True), 13.5, weight=800)
    return svg(760, 300, arrow_defs() + b, 'Dappen dish, pennello e polvere: immergi, scarica, raccogli la perla')


def pg_tube(cx, cy, s=1.0, col='#f3c1cf'):
    """Tubetto di polygel orizzontale: fondo pinzato a sinistra, tappo a destra."""
    o = ('<path d="M-46,-12 L22,-15 Q30,-15 30,-8 L30,8 Q30,15 22,15 L-46,12 Z" fill="#fbf3f5" stroke="%s" stroke-width="1.5"/>' % NAIL_S)
    o += '<rect x="-52" y="-14" width="8" height="28" rx="2" fill="#efe1e5" stroke="%s" stroke-width="1.3"/>' % NAIL_S
    for k in range(4):
        o += '<line x1="%d" y1="-13" x2="%d" y2="13" stroke="%s" stroke-width=".8" opacity=".6"/>' % (-50 + k * 2, -50 + k * 2, NAIL_S)
    o += '<rect x="-34" y="-8" width="46" height="16" rx="3" fill="%s"/>' % col
    o += text(-11, 4.5, 'POLY', 10, weight=900, fill=ACC2).replace('font-size="10"', 'font-size="12"')
    o += '<rect x="30" y="-6" width="8" height="12" fill="#e9e4e6" stroke="%s"/>' % NAIL_S
    o += '<rect x="38" y="-8" width="10" height="16" rx="2" fill="%s"/>' % ACC2
    o += '<rect x="-40" y="-12" width="60" height="3" rx="1.5" fill="#fff" opacity=".8"/>'
    return '<g transform="translate(%.1f,%.1f) scale(%.2f)">%s</g>' % (cx, cy, s, o)


def pg_spatula(x, y, ang=0, s=1.0):
    """Strumento doppio per polygel: spatola a un lato, pennello piatto all'altro (qui la spatola a sinistra)."""
    o = '<rect x="-30" y="-4" width="70" height="8" rx="4" fill="%s" stroke="%s" stroke-width=".9"/>' % (STEEL, STEEL_E)
    o += '<path d="M-30,-4 L-50,-7 Q-56,-6 -56,0 Q-56,6 -50,7 L-30,4 Z" fill="%s" stroke="%s" stroke-width=".9"/>' % (STEEL, STEEL_E)
    o += '<rect x="-28" y="-2.5" width="64" height="1.6" fill="#fff" opacity=".6"/>'
    return _g(x, y, ang, s, o)


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
            b += pg_tube(cx - 4, 130, 1.1)
            b += pg_spatula(cx + 2, 184, 168, 1.0)
            b += '<path d="M%.1f,%.1f c-2,-8 6,-14 14,-10 c8,4 6,14 -2,14 c-6,0 -10,0 -12,-4 z" fill="%s" stroke="%s" stroke-width="1.2"/>' % (cx + 50, 170, PG, NAIL_S)
            b += carrow(cx + 58, 146, cx + 58, 158, ACC2, 1.8)
        elif i == 1:
            b += '<rect x="%.1f" y="186" width="104" height="12" rx="3" fill="#e9ecef" stroke="%s"/>' % (cx - 52, GREY)
            b += '<rect x="%.1f" y="166" width="66" height="20" rx="10" fill="%s" stroke="%s"/>' % (cx - 40, PG, NAIL_S)
            b += '<rect x="%.1f" y="166" width="4" height="20" fill="#fff" opacity=".5"/>' % (cx - 30)
            b += pg_spatula(cx + 8, 136, -80, 1.0)
            b += '<line x1="%.1f" y1="160" x2="%.1f" y2="194" stroke="%s" stroke-width="2" stroke-dasharray="3 3"/>' % (cx + 4, cx + 4, ACC2)
            b += text(cx, 220, 'una perla per zona', 12, weight=600, fill=MUTED)
        elif i in (2, 3):
            f, p = finger_nail(cx, 200, hw=27, nail_len=72, free_len=8, shape='squoval', finger_len=26, lunula=False)
            b += f
            if i == 2:
                b += '<ellipse cx="%.1f" cy="%.1f" rx="16" ry="10" fill="%s" stroke="%s"/>' % (cx, 156, PG, NAIL_S)
                b += '<ellipse cx="%.1f" cy="%.1f" rx="6" ry="3" fill="#fff" opacity=".7"/>' % (cx - 5, 152)
                b += text(cx, 104, 'al centro', 12, weight=700, fill=ACC2)
            else:
                b += '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s" opacity=".9" stroke="%s"/>' % (
                    cx - 22, 180, cx - 22, 126, cx, 116, cx + 22, 126, cx + 22, 180, PG, NAIL_S)
                b += tool_brush(cx + 14, 134, -40, 50, '#f1e3a0', 'flat')
                b += drop_icon(cx + 46, 110, 0.4, '#9cc7e0')
        else:
            b += lamp_r(cx, 214, 116, 'UV/LED')
            b += '<path d="M%.1f,214 L%.1f,200 Q%.1f,192 %.1f,196 L%.1f,206 Z" fill="%s" stroke="%s" stroke-width="1.2"/>' % (cx - 30, cx - 30, cx + 10, cx + 26, cx + 30, SKIN, SKIN_D)
            b += '<rect x="%.1f" y="196" width="10" height="5" rx="2.5" fill="%s"/>' % (cx + 16, PG)
        b += mtext(cx, 256, wrap(lab, W - 16, 13.5, True), 13.5, weight=800)
    return svg(800, 296, arrow_defs() + b, 'Polygel: preleva dal tubetto, taglia, appoggia, modella con poca slip solution, polimerizza')


@figx('fibra-riparazione.svg')
def fibra_rip():
    b = title('Riparare una crepa con la fibra')
    labs = ['Trova la crepa', 'Toppa 2–3 mm oltre la crepa', 'Resina + attivatore, poi lima']
    W = 196
    for i, lab in enumerate(labs):
        x = 20 + i * (W + 10)
        b += frame(x, 56, W, 250, None)
        b += badge(x + 24, 80, i + 1, ACC, 13)
        cx = x + W / 2 + 4
        ex = ''
        if i == 1:
            ex = '<g clip-path="url(#CLIP)"><rect x="%.1f" y="70" width="64" height="62" fill="url(#mesh)" stroke="#9a8f7a" stroke-width="1.2" stroke-dasharray="4 3"/></g>' % (cx - 26)
        elif i == 2:
            ex = '<g clip-path="url(#CLIP)"><rect x="%.1f" y="70" width="64" height="62" fill="#ffffff" opacity=".5"/></g>' % (cx - 26)
        f, p = finger_nail(cx, 214, hw=38, nail_len=104, free_len=26, shape='squoval', finger_len=26, lunula=False, extra=ex)
        b += f
        b += '<path d="M%.1f,%.1f l7,7 l-7,7 l7,7 l-5,7" fill="none" stroke="%s" stroke-width="2.6" stroke-linejoin="round"/>' % (cx + 20, 92, ERR if i < 2 else '#d99aa5')
        if i == 0:
            b += magnifier(cx + 50, 84, 13)
        if i == 1:
            b += carrow(cx + 26, 130, cx + 38, 130, ACC2, 1.6)
            b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.2" stroke-dasharray="2 2"/>' % (cx + 25, 122, cx + 25, 136, ACC2)
        if i == 2:
            b += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" opacity=".9"/>' % (cx - 16, 176, cx - 20, 130, cx - 12, 96)
            b += file_r('dritta', cx + 58, 150, '#8f8379', '#2f2a28', ('', ''), -70, 0.6, seed=21)
        b += mtext(cx - 4, 268, wrap(lab, W - 20, 13.5, True), 13.5, weight=800)
    b += '<defs><pattern id="mesh" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="6" height="6" fill="#fffaf0"/><path d="M0,0 L6,0 M0,0 L0,6" stroke="#cbbf9f" stroke-width="1"/></pattern></defs>'
    b += '<rect x="638" y="56" width="102" height="250" rx="16" fill="%s"/>' % WARN_BG
    b += excl(689, 96, AMBER, 14)
    b += mtext(689, 140, ['Attivatore:', 'poco', 'e da', 'lontano'], 14, weight=800, fill=WARN)
    b += mtext(689, 240, ['a 1 mm da', 'cuticola', 'e lati'], 13, weight=700)
    return svg(760, 320, arrow_defs() + b, 'Riparazione di una crepa con la fibra: la toppa supera la crepa di 2–3 millimetri, poi resina, attivatore e lima')


# ----------------------------------------------------------------- lampade e documenti (completamento modulo 3)
def spectrum(x0, x1, base, curves, band=(350, 415), h=70):
    """Mini grafico spettro 300–450 nm con zona del fotoiniziatore evidenziata."""
    def X(nm):
        return x0 + (nm - 300) / 150.0 * (x1 - x0)
    o = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#f8dfe7"/>' % (X(band[0]), base - h - 6, X(band[1]) - X(band[0]), h + 6)
    o += text((X(band[0]) + X(band[1])) / 2, base - h + 8, 'zona del gel', 12, weight=700, fill=ACC2)
    for peak, sd, hh, col in curves:
        pts = ['%.1f,%.1f' % (X(nm), base - hh * math.exp(-((nm - peak) ** 2) / (2 * sd * sd))) for nm in range(300, 451, 2)]
        o += '<polygon points="%.1f,%.1f %s %.1f,%.1f" fill="%s" opacity=".18"/>' % (X(300), base, ' '.join(pts), X(450), base, col)
        o += '<polyline points="%s" fill="none" stroke="%s" stroke-width="3" stroke-linejoin="round"/>' % (' '.join(pts), col)
    o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.5"/>' % (x0, base, x1, base, INK)
    for nm in (300, 350, 400, 450):
        o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s"/>' % (X(nm), base, X(nm), base + 5, INK)
        o += text(X(nm), base + 19, str(nm) + (' nm' if nm == 450 else ''), 12, 'middle' if nm < 450 else 'end', 400, MUTED)
    return o


@figx('lampada-watt-vs-nm.svg')
def lampada_watt():
    b = title('Watt o lunghezza d\'onda?')
    data = [(20, 'Lampada potente, luce sbagliata', 116, '36 W', [(432, 7, 62, '#3f6fe0')], False, 'Gel sotto-polimerizzato'),
            (390, 'Lampada piccola, luce giusta', 84, '9 W', [(365, 6, 58, UV), (405, 6, 58, UV)], True, 'Polimerizza bene')]
    for x, ttl, lw, watt, curves, ok, res in data:
        b += frame(x, 56, 350, 270, ttl, ok=ok, bw=2.5, border=OK if ok else ERR)
        cx = x + 120
        b += lamp_r(cx, 172, lw, display=False, glow=('#d9c6ff', '#8a63d8', '#43306e') if ok else ('#cfe0ff', '#3f6fe0', '#1f3270'))
        b += text(x + 256, 138, watt, 30, weight=900, fill=INK)
        b += text(x + 256, 158, 'potenza', 12.5, weight=600, fill=MUTED)
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
        mx, my = fx + (tx - fx) * 0.4, -40 + (ty + 40) * 0.4
        g += '<path d="%s" fill="%s" stroke="%s" stroke-width="1.6"/>' % (_finger_path(fx, -30, mx, my, r * 1.2, r * 1.12), col, st)
        g += '<path d="M%.1f,%.1f l%.1f,0" stroke="#6b5a60" stroke-width="2"/>' % (mx - r * 1.05, my + 3, r * 2.1)
    g += '<path d="%s" fill="%s" stroke="%s" stroke-width="1.6"/>' % (_finger_path(-40, 66, -96, 4, 26, 17.5), col, st)
    g += ('<path d="M-72,-46 C-70,-70 -42,-78 -6,-78 C32,-78 74,-74 82,-52 C86,-20 84,30 76,64 C68,92 52,104 42,108 '
          'L-38,108 C-56,102 -64,90 -70,72 C-78,40 -74,0 -72,-46 Z" fill="%s" stroke="%s" stroke-width="1.6"/>') % (col, st)
    g += '<rect x="-42" y="104" width="84" height="38" fill="%s" stroke="%s" stroke-width="1.4"/><rect x="-42" y="128" width="84" height="14" fill="#6b5a60"/>' % (col, st)
    g += '<path d="M-40,-30 Q10,-46 64,-34" stroke="#6b5a60" stroke-width="2.4" fill="none" stroke-dasharray="5 3"/>'
    g += '<path d="M-54,60 Q8,40 66,52" stroke="#6b5a60" stroke-width="2" fill="none" opacity=".7"/>'
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


GHS_SYM = {
    # GHS02 – fiamma su base
    'fire': ('<path d="M-6,34 C-30,30 -40,12 -34,-8 C-31,-18 -26,-24 -22,-30 C-21,-18 -16,-10 -9,-6 C-14,-26 -6,-46 10,-60 '
             'C8,-42 16,-30 24,-20 C27,-26 28,-32 27,-38 C40,-24 44,-4 38,12 C34,24 24,32 10,34 Z" fill="#111"/>'
             '<path d="M2,34 C-12,30 -16,18 -12,8 C-10,2 -6,-2 -4,-6 C-2,4 4,10 10,12 C8,2 10,-6 14,-12 C22,-2 24,10 20,20 C17,28 10,33 2,34 Z" fill="#fff"/>'
             '<rect x="-36" y="40" width="72" height="9" rx="1.5" fill="#111"/>'),
    # GHS07 – punto esclamativo
    'excl': ('<path d="M-10,-50 Q-10,-56 0,-56 Q10,-56 10,-50 L6,18 Q5,22 0,22 Q-5,22 -6,18 Z" fill="#111"/>'
             '<circle cx="0" cy="38" r="9.5" fill="#111"/>'),
    # GHS08 – pericolo per la salute
    'health': ('<circle cx="0" cy="-40" r="13" fill="#111"/>'
               '<path d="M-40,46 C-42,6 -26,-22 0,-22 C26,-22 42,6 40,46 Z" fill="#111"/>'
               '<path d="M0,-12 L5,2 L18,-4 L11,9 L24,14 L11,18 L17,32 L4,25 L0,38 L-4,25 L-17,32 L-11,18 L-24,14 L-11,9 L-18,-4 L-5,2 Z" fill="#fff"/>'),
    # GHS05 – corrosivo (stilizzato: gocce su mano e superficie)
    'corr': ('<path d="M-40,40 L40,40 L40,48 L-40,48 Z" fill="#111"/>'
             '<path d="M-30,-30 L-14,-30 L-14,-8 L-30,-8 Z M14,-30 L30,-30 L30,-8 L14,-8 Z" fill="#111"/>'
             '<path d="M-22,0 q5,8 0,14 q-5,-6 0,-14 Z M22,0 q5,8 0,14 q-5,-6 0,-14 Z" fill="#111"/>'),
}


def ghs(cx, cy, r=14, kind='excl'):
    """Pittogramma GHS/CLP: quadrato ruotato a rombo, fondo bianco, bordo rosso spesso, simbolo nero. r = semidiagonale."""
    if kind == 'flame':
        kind = 'fire'
    return ('<g transform="translate(%.1f,%.1f) scale(%.4f)">'
            '<path d="M0,-92 L92,0 L0,92 L-92,0 Z" fill="#fff" stroke="#e3001b" stroke-width="13" stroke-linejoin="round"/>'
            '<g transform="scale(.86)">%s</g></g>') % (cx, cy, r / 100.0, GHS_SYM[kind])


def lamp_r(cx, y, w=120, label='', display=True, glow=('#d9c6ff', '#8a63d8', '#43306e')):
    """Lampada UV/LED realistica vista di fronte: cupola, apertura illuminata, LED, base. y = piano d'appoggio."""
    g1, g2 = uid('lp'), uid('lp')
    h1, h2 = w * 0.62, w * 0.42
    o = ('<defs><linearGradient id="%s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#e2dcea"/></linearGradient>'
         '<radialGradient id="%s" cx=".5" cy=".95" r=".8"><stop offset="0" stop-color="%s"/><stop offset=".55" stop-color="%s"/>'
         '<stop offset="1" stop-color="%s"/></radialGradient></defs>') % (g1, g2, glow[0], glow[1], glow[2])
    o += '<rect x="%.1f" y="%.1f" width="%.1f" height="7" rx="3.5" fill="#8a7d9e"/>' % (cx - w / 2 - 6, y - 1, w + 12)
    o += ('<path d="M%.1f,%.1f L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="url(#%s)" stroke="#8a7d9e" stroke-width="1.6" filter="url(#nxShS)"/>'
          % (cx - w / 2, y, cx - w / 2, y - h1 * 0.5, cx - w / 2, y - h1 * 1.18, cx + w / 2, y - h1 * 1.18, cx + w / 2, y - h1 * 0.5, cx + w / 2, y, g1))
    o += ('<path d="M%.1f,%.1f L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="url(#%s)" stroke="#6b5a8a" stroke-width="1.2"/>'
          % (cx - w * 0.36, y, cx - w * 0.36, y - h2 * 0.45, cx - w * 0.36, y - h2 * 1.2, cx + w * 0.36, y - h2 * 1.2, cx + w * 0.36, y - h2 * 0.45, cx + w * 0.36, y, g2))
    for k in range(5):
        t = (k - 2) / 2.0
        lx = cx + t * w * 0.24
        ly = y - h2 * (0.82 - 0.16 * t * t)
        o += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#f4eeff"/>' % (lx, ly, max(1.6, w * 0.018))
    o += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="#fff" stroke-width="%.1f" fill="none" opacity=".8" stroke-linecap="round"/>' % (
        cx - w * 0.4, y - h1 * 0.55, cx - w * 0.36, y - h1 * 0.95, cx - w * 0.12, y - h1 * 1.02, max(1.5, w * 0.025))
    if display and w >= 90:
        o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="#2f2840"/>' % (cx - w * 0.12, y - h1 * 1.02, w * 0.24, w * 0.1)
        o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1" fill="#b9f5cf" opacity=".85"/>' % (cx - w * 0.07, y - h1 * 1.02 + w * 0.035, w * 0.14, w * 0.03)
    if label:
        o += text(cx, y - h1 * 1.12 - 8, label, 13, weight=800, fill='#6b4fa0')
    return o


def doc_sheet(x, y, w, h, head, head_col, sub=''):
    """Foglio con intestazione colorata e angolo piegato."""
    o = ('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="#fff" stroke="#c9ced4" stroke-width="1.4" filter="url(#nxShS)"/>'
         % (x, y, x + w - 16, y, x + w, y + 16, x + w, y + h, x, y + h))
    o += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="#e9ecef" stroke="#c9ced4" stroke-width="1.2"/>' % (x + w - 16, y, x + w - 16, y + 16, x + w, y + 16)
    o += '<rect x="%.1f" y="%.1f" width="%.1f" height="20" fill="%s"/>' % (x + 8, y + 10, w - 34, head_col)
    o += text(x + 14, y + 25, head, 12, 'start', 800, '#fff')
    if sub:
        o += text(x + 10, y + 46, sub, 12, 'start', 800, INK)
    return o


def lines_block(x, y, w, n, gap=8, col='#d3d8dd', seed=0):
    o = ''
    for k in range(n):
        ww = w * (0.55 + 0.45 * (((k + seed) * 37) % 10) / 10.0)
        o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="3" stroke-linecap="round"/>' % (x, y + k * gap, x + ww, y + k * gap, col)
    return o


def gel_bottle(cx, base, w=86, h=130, col='#f6d6df', name='BUILDER GEL', inci=True):
    """Flacone di gel con tappo zigrinato ed etichetta."""
    g = uid('bt')
    o = ('<defs><linearGradient id="%s" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9b4c4"/><stop offset=".25" stop-color="%s"/>'
         '<stop offset=".6" stop-color="#fbe8ee"/><stop offset="1" stop-color="#e5a9bc"/></linearGradient></defs>') % (g, col)
    o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="16" fill="url(#%s)" stroke="%s" stroke-width="1.8" filter="url(#nxShS)"/>' % (
        cx - w / 2, base - h, w, h, g, NAIL_S)
    o += '<rect x="%.1f" y="%.1f" width="%.1f" height="12" rx="3" fill="#d8b4c0" stroke="%s" stroke-width="1.4"/>' % (cx - w * 0.3, base - h - 10, w * 0.6, NAIL_S)
    o += '<rect x="%.1f" y="%.1f" width="%.1f" height="34" rx="6" fill="#3b2a30"/>' % (cx - w * 0.28, base - h - 42, w * 0.56)
    for k in range(7):
        xx = cx - w * 0.22 + k * w * 0.44 / 6
        o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#5a4650" stroke-width="2"/>' % (xx, base - h - 38, xx, base - h - 12)
    o += '<rect x="%.1f" y="%.1f" width="5" height="26" rx="2.5" fill="#fff" opacity=".35"/>' % (cx - w * 0.2, base - h - 38)
    o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="6" fill="#fff" stroke="#ead7dd"/>' % (cx - w / 2 + 9, base - h + 18, w - 18, h - 32)
    o += '<rect x="%.1f" y="%.1f" width="7" height="%.1f" rx="3.5" fill="#fff" opacity=".55"/>' % (cx - w / 2 + 3, base - h + 14, h - 30)
    return o


@figx('tre-documenti.svg')
def tre_documenti():
    b = title('Tre documenti per ogni prodotto')
    cols = [('ETICHETTA', 'INCI, avvertenze, lotto, PAO', ACC),
            ('SCHEDA TECNICA', 'lampada, tempi, ordine', '#3f86b8'),
            ('SDS', 'rischi, DPI, conservazione, smaltimento', '#c62828')]
    W = 236
    for k, (t, sub, c) in enumerate(cols):
        x = 20 + k * (W + 6)
        cx = x + W / 2
        b += '<rect x="%d" y="56" width="%d" height="276" rx="14" fill="%s"/>' % (x, W, PANEL)
        b += badge(x + 24, 80, k + 1, c)
        if k == 0:
            b += gel_bottle(cx, 250, 96, 136)
            b += text(cx, 150, 'BUILDER GEL', 12, weight=900, fill=ACC2)
            b += '<line x1="%.1f" y1="157" x2="%.1f" y2="157" stroke="%s" stroke-width="1"/>' % (cx - 34, cx + 34, '#ead7dd')
            b += text(cx - 34, 172, 'INCI:', 12, 'start', 800, INK)
            b += lines_block(cx - 34, 181, 66, 2, 7)
            b += warn_tri(cx - 20, 209, 10.5) + pao(cx + 16, 204, '12M', 1.0)
            b += text(cx, 234, 'LOT 2409A', 12, weight=800, fill=MUTED)
        elif k == 1:
            b += doc_sheet(cx - 74, 72, 148, 186, 'SCHEDA TECNICA', '#3f86b8', 'Builder Gel')
            for r, (l1, l2) in enumerate((('LED', '60 s'), ('UV', '120 s'))):
                for c2, tt in enumerate((l1, l2)):
                    b += '<rect x="%.1f" y="%.1f" width="58" height="20" fill="%s" stroke="#c8ced4"/>' % (cx - 64 + c2 * 58, 128 + r * 20, '#eef5fa' if c2 == 0 else '#fff')
                    b += text(cx - 35 + c2 * 58, 142.5 + r * 20, tt, 12, weight=800 if c2 == 0 else 700)
            b += lamp_r(cx + 36, 238, 56, display=False)
            for j, st in enumerate(['base', 'gel', 'top']):
                b += badge(cx - 56, 188 + j * 21, j + 1, '#3f86b8', 9, 12)
                b += text(cx - 43, 192 + j * 21, st, 12.5, 'start', 700)
        else:
            b += doc_sheet(cx - 74, 72, 148, 186, 'SDS · 16 SEZIONI', '#c62828')
            b += text(cx - 64, 120, '2 · Pericoli', 12, 'start', 800, '#c62828')
            for j, kd in enumerate(('fire', 'excl', 'health')):
                b += ghs(cx - 40 + j * 40, 150, 19, kd)
            for j in range(4):
                yy = 188 + j * 16
                b += text(cx - 64, yy + 4, str(j * 3 + 4), 10, 'start', 800, MUTED).replace('font-size="10"', 'font-size="12"')
                b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#d3d8dd" stroke-width="3" stroke-linecap="round"/>' % (cx - 44, yy, cx + 50 - (j % 2) * 18, yy)
        b += text(cx, 284, t, 16, weight=900, fill=c)
        b += mtext(cx, 305, wrap(sub, W - 30, 13, True), 13, weight=700)
    return svg(760, 340, b, 'Etichetta, scheda tecnica e scheda di sicurezza (SDS) con i pittogrammi di pericolo: che cosa contiene ciascuna')


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
        ix = 424
        if n == 2:
            for q, kd in enumerate(('fire', 'excl', 'health')):
                b += ghs(402 + q * 26, y - 1, 14.5, kd)
        elif n == 4:
            b += first_aid(ix, y - 1, 16)
        elif n == 7:
            b += cabinet(ix, y - 3, 0.95)
        elif n == 8:
            b += glove(ix - 6, y + 2, 0.5) + glasses(ix + 10, y + 8, 0.36)
        else:
            b += trash(ix, y + 20, 30, 34)
        b += text(472, y - 6, 'Sez. %d – %s' % (n, t), 15, 'start', 800, ACC2)
        b += text(472, y + 14, sub, 13, 'start', 600)
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
                o += '<path d="M%.1f,178 L%.1f,134 Q%.1f,116 %.1f,116 Q%.1f,116 %.1f,134 L%.1f,178 Z" fill="#d65d86" stroke="%s" stroke-width="1.5"/>' % (
                    px, px, px, px + w / 2, px + w, px + w, px + w, NAIL_S)
                o += '<rect x="%.1f" y="124" width="%.1f" height="44" rx="%.1f" fill="#fff" opacity=".35"/>' % (px + 4, w * 0.18, w * 0.09)
                o += text(px + w / 2, 198, n, 13, weight=800, fill=ACC2)
            o += text(cx, 240, 'una misura per dito', 12.5, weight=600, fill=MUTED)
        else:
            f, p = finger_nail(cx, 196, hw=28, nail_len=64, free_len=6 if i < 3 else 24, shape='squoval', finger_len=26, lunula=False,
                               plate=NAIL if i < 3 else '#d65d86', free=FREE if i < 3 else '#d65d86')
            o += f
            if i == 1:
                o += file_r('dritta', cx + 26, 128, '#ece4dc', '#bba', ('', ''), -24, 0.66, seed=31)
                o += text(cx, 248, 'lima fine, poi sgrassa', 12.5, weight=600, fill=MUTED)
            elif i == 2:
                o += drop_icon(cx, 150, 0.8, '#f1d27a')
                o += ('<g transform="translate(%.1f,150) rotate(-35)"><rect x="-9" y="-40" width="18" height="46" rx="5" fill="#fff" stroke="%s" stroke-width="1.6"/>'
                      '<rect x="-9" y="-26" width="18" height="14" fill="%s"/><path d="M-4,-40 L0,-56 L4,-40 Z" fill="%s"/></g>' % (cx + 48, GREY_D, ACC, GREY_D))
                o += text(cx, 248, 'colla o linguetta', 12.5, weight=600, fill=MUTED)
            else:
                o += '<ellipse cx="%.1f" cy="118" rx="30" ry="18" fill="%s" stroke="%s" stroke-width="1.6"/>' % (cx, SKIN, SKIN_D)
                o += arrow(cx - 48, 104, cx - 48, 132)
                o += stopwatch(cx + 60, 196, 15)
                o += text(cx, 248, 'qualche secondo', 12.5, weight=600, fill=MUTED)
        return o
    return steps_fig('Press-on in 4 passaggi', labels, 4, 179, 214, draw,
                     'Applicazione delle press-on: scegliere la misura, preparare la lamina, incollare, premere')


FILE_PATHS = {
    'dritta': 'M-58,-12 L58,-12 A12,12 0 0 1 58,12 L-58,12 A12,12 0 0 1 -58,-12 Z',
    'banana': 'M-66,-6 Q0,-36 66,-6 A10,10 0 0 1 66,14 Q0,-14 -66,14 A10,10 0 0 1 -66,-6 Z',
    'mezzaluna': 'M-66,10 Q0,-38 66,10 Q71,14 66,16 L-66,16 Q-71,14 -66,10 Z',
    'ovale': 'M-70,0 C-62,-15 62,-15 70,0 C62,15 -62,15 -70,0 Z',
}


def file_r(kind, cx, cy, col, core='#3b2a30', grits=('', ''), ang=0, s=1.0, seed=3, fg='#fff'):
    """Lima vista dall'alto: spessore con l'anima colorata, grana puntinata, numeri di grana stampati."""
    if kind == 'buffer':
        o = ('<path d="M-52,-6 l12,-12 h96 l-12,12 Z" fill="#fbeef2" stroke="#c9a3b1" stroke-width="1.2"/>'
             '<path d="M44,-6 l12,-12 v28 l-12,12 Z" fill="#e8c6d1" stroke="#c9a3b1" stroke-width="1.2"/>'
             '<rect x="-52" y="-6" width="96" height="28" fill="#f6dce4" stroke="#c9a3b1" stroke-width="1.2"/>')
        rnd = random.Random(seed)
        for _ in range(60):
            o += '<circle cx="%.1f" cy="%.1f" r=".9" fill="#c98aa0" opacity=".6"/>' % (rnd.uniform(-50, 42), rnd.uniform(-4, 20))
        o += text(-4, 13, grits[0], 12, weight=800, fill=ACC2) if grits[0] else ''
        return _g(cx, cy, ang, s, o)
    d = FILE_PATHS[kind]
    cid = uid('fl')
    o = '<defs><clipPath id="%s"><path d="%s"/></clipPath></defs>' % (cid, d)
    o += '<path d="%s" transform="translate(0,3.2)" fill="%s"/>' % (d, core)
    o += '<path d="%s" fill="%s" stroke="rgba(0,0,0,.28)" stroke-width="1"/>' % (d, col)
    rnd = random.Random(seed)
    t = ''
    for _ in range(170):
        t += '<circle cx="%.1f" cy="%.1f" r="%.2f" fill="%s" opacity=".55"/>' % (
            rnd.uniform(-72, 72), rnd.uniform(-36, 18), rnd.uniform(.5, 1.1), '#000' if rnd.random() < .5 else '#fff')
    t += '<rect x="-72" y="-40" width="144" height="8" fill="#fff" opacity=".0"/>'
    o += '<g clip-path="url(#%s)">%s</g>' % (cid, t)
    gy = {'dritta': 4.5, 'banana': -4, 'mezzaluna': 6, 'ovale': 4.5}[kind]
    if grits[0]:
        o += text(-34, gy, grits[0], 12, weight=800, fill=fg)
    if grits[1]:
        o += text(34, gy, grits[1], 12, weight=800, fill=fg)
    return _g(cx, cy, ang, s, o)


def file_shape(kind, cx, cy, col='#b9aa9c', col2='#e6dbd0'):
    """Compatibilità: lima semplice (usa file_r)."""
    return file_r(kind, cx, cy, col, '#5d4a3d')


@figx('lime-forme-anime.svg')
def lime_forme():
    b = title('Lime: forme e anima')
    items = [('dritta', 'Dritta', '100/180', 'lati paralleli', '#8f8379', '#2f2a28', ('100', '180')),
             ('banana', 'Banana', '180/240', 'zona cuticolare', '#d98aa5', '#ffffff', ('180', '240')),
             ('mezzaluna', 'Mezzaluna', '240', 'curve e punta', '#7fa9c7', '#ffffff', ('240', '240')),
             ('ovale', 'Ovale', '180/240', 'uso generale', '#9c93c4', '#ffffff', ('180', '240')),
             ('buffer', 'Buffer a blocco', '180/400', 'leviga e lucida', '', '', ('', ''))]
    for k, (kd, name, g, use, col, core, grits) in enumerate(items):
        cx = 92 + k * 154
        b += '<ellipse cx="%d" cy="104" rx="70" ry="30" fill="%s" opacity=".55"/>' % (cx, PANEL)
        b += file_r(kd, cx, 102 if kd != 'buffer' else 96, col, core, grits, seed=k + 2)
        b += text(cx, 160, name, 15, weight=800)
        b += chip(cx, 184, g, ACC2, '#fff', 12.5)
        b += text(cx, 212, use, 13, weight=600, fill=MUTED)
    # sezioni dell'anima
    def layer_tex(x0, y0, w, h, col, dot, seed):
        rnd = random.Random(seed)
        o = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (x0, y0, w, h, col)
        for _ in range(int(w * h / 14)):
            o += '<circle cx="%.1f" cy="%.1f" r="%.2f" fill="%s" opacity=".7"/>' % (rnd.uniform(x0, x0 + w), rnd.uniform(y0, y0 + h), rnd.uniform(.5, 1.1), dot)
        return o
    b += frame(20, 230, 370, 138, 'Anima rigida (legno o plastica)')
    X0, Y0 = 60, 282
    b += layer_tex(X0, Y0, 230, 6, '#8f8379', '#2f2a28', 1)
    b += '<rect x="%d" y="%d" width="230" height="18" fill="#d8b98a"/>' % (X0, Y0 + 6)
    for k in range(5):
        b += '<path d="M%d,%d q60,-3 120,0 t110,0" stroke="#b39466" stroke-width="1" fill="none"/>' % (X0, Y0 + 9 + k * 3)
    b += layer_tex(X0, Y0 + 24, 230, 6, '#8f8379', '#2f2a28', 2)
    b += '<rect x="%d" y="%d" width="230" height="30" fill="none" stroke="#6d5f55" stroke-width="1.2"/>' % (X0, Y0)
    b += leader(X0 + 230, Y0 + 3, 304, 270, 'abrasivo', 'start', 12.5, 700)
    b += leader(X0 + 230, Y0 + 15, 304, 300, 'anima', 'start', 12.5, 700)
    b += text(205, 352, 'Non si piega: lati dritti e forma', 13, weight=700, fill=MUTED)
    b += frame(410, 230, 370, 138, 'Anima morbida (spugna)')
    # lima morbida che si adatta alla curva dell'unghia
    b += '<path d="M480,334 Q595,290 710,334" fill="none" stroke="%s" stroke-width="8" stroke-linecap="round"/>' % NAIL_S
    b += '<path d="M480,334 Q595,290 710,334 L710,340 Q595,296 480,340 Z" fill="%s"/>' % NAIL
    cid = uid('sp')
    sp = 'M478,326 Q595,282 712,326 L712,300 Q595,254 478,300 Z'
    b += '<defs><clipPath id="%s"><path d="%s"/></clipPath></defs>' % (cid, sp)
    rnd = random.Random(9)
    t = '<path d="%s" fill="#f6e7a6"/>' % sp
    for _ in range(90):
        t += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#e2c86a" opacity=".8"/>' % (rnd.uniform(478, 712), rnd.uniform(256, 330), rnd.uniform(1.2, 2.6))
    b += '<g clip-path="url(#%s)">%s</g>' % (cid, t)
    b += '<path d="M478,329 Q595,285 712,329" fill="none" stroke="#9c93c4" stroke-width="5"/>'
    b += '<path d="M478,297 Q595,251 712,297" fill="none" stroke="#9c93c4" stroke-width="5"/>'
    b += leader(700, 296, 724, 268, 'abrasivo', 'start', 12.5, 700)
    b += leader(650, 302, 724, 296, 'spugna', 'start', 12.5, 700)
    b += text(595, 360, 'Segue la curva: superficie e buffer', 13, weight=700, fill=MUTED)
    return svg(800, 380, b, 'Forme delle lime (dritta, banana, mezzaluna, ovale, buffer) con grana stampata, e differenza tra anima rigida e anima morbida')


def spray(cx, base, s=1.0, col='#dfe9f2', label='DISINF.'):
    """Flacone spray con grilletto, etichetta e nebulizzazione verso destra. base = fondo del flacone."""
    g = uid('sp')
    o = ('<defs><linearGradient id="%s" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#c9dbe8"/><stop offset=".35" stop-color="%s"/>'
         '<stop offset=".7" stop-color="#ffffff"/><stop offset="1" stop-color="#bcd0de"/></linearGradient></defs>') % (g, col)
    o += '<path d="M-16,-58 L16,-58 Q20,-58 20,-50 L20,-6 Q20,0 14,0 L-14,0 Q-20,0 -20,-6 L-20,-50 Q-20,-58 -16,-58 Z" fill="url(#%s)" stroke="%s" stroke-width="1.6"/>' % (g, GREY_D)
    o += '<rect x="-15" y="-42" width="30" height="24" rx="3" fill="#fff" stroke="#c9ced4"/>'
    o += '<rect x="-15" y="-42" width="30" height="7" rx="2" fill="%s"/>' % OK
    o += '<line x1="-10" y1="-29" x2="10" y2="-29" stroke="#c9ced4" stroke-width="2.4"/><line x1="-10" y1="-23" x2="6" y2="-23" stroke="#c9ced4" stroke-width="2.4"/>'
    o += '<rect x="-8" y="-66" width="16" height="9" rx="2" fill="#4b3a40"/>'
    o += '<path d="M-10,-66 L-10,-80 Q-10,-84 -4,-84 L18,-84 L22,-79 L18,-74 L6,-74 L6,-66 Z" fill="#4b3a40"/>'
    o += '<path d="M2,-74 Q4,-62 -2,-54 L-6,-56 Q-1,-62 -2,-72 Z" fill="#6d5a62"/>'
    for k, (dx, dy) in enumerate(((30, -86), (34, -80), (31, -74), (38, -84), (40, -77), (36, -71), (44, -80))):
        o += '<circle cx="%d" cy="%d" r="%.1f" fill="%s" opacity=".8"/>' % (dx, dy, 1.6 if k % 2 else 2.1, PROD_S)
    return '<g transform="translate(%.1f,%.1f) scale(%.2f)">%s</g>' % (cx, base, s, o)


def glass_file(cx, cy, ang=0, s=1.0):
    """Lima in vetro: trasparente, con zona incisa e riflessi."""
    o = ('<path d="M-66,-11 L56,-11 Q70,-11 70,0 Q70,11 56,11 L-66,11 Q-72,0 -66,-11 Z" fill="#cfe8f6" fill-opacity=".85" stroke="#6fa7c9" stroke-width="1.4"/>')
    for k in range(26):
        xx = -56 + k * 4.4
        o += '<line x1="%.1f" y1="-8" x2="%.1f" y2="8" stroke="#8fbfdc" stroke-width=".8"/>' % (xx, xx + 3)
    o += '<rect x="-64" y="-8" width="122" height="3" rx="1.5" fill="#fff" opacity=".8"/>'
    o += '<rect x="20" y="-11" width="18" height="22" fill="#fff" opacity=".35"/>'
    return _g(cx, cy, ang, s, o)


def metal_file(cx, cy, ang=0, s=1.0, strip=False):
    """Lima in metallo con impugnatura; strip=True: supporto per ricambi adesivi."""
    o = '<rect x="-80" y="-6" width="30" height="12" rx="6" fill="#4b3a40"/>'
    o += '<rect x="-52" y="-10" width="126" height="20" rx="8" fill="%s" stroke="%s" stroke-width="1.2"/>' % (STEEL, STEEL_E)
    if not strip:
        for k in range(24):
            xx = -46 + k * 4.8
            o += '<line x1="%.1f" y1="-7" x2="%.1f" y2="7" stroke="%s" stroke-width=".8" opacity=".8"/>' % (xx, xx + 3, STEEL_E)
            o += '<line x1="%.1f" y1="-7" x2="%.1f" y2="7" stroke="%s" stroke-width=".6" opacity=".5"/>' % (xx + 3, xx, STEEL_E)
    o += '<rect x="-48" y="-8" width="118" height="2.4" rx="1.2" fill="#fff" opacity=".6"/>'
    return _g(cx, cy, ang, s, o)


def bin_pedal(cx, base, w=44, h=52):
    """Cestino con coperchio e pedale."""
    g = uid('bn')
    o = ('<defs><linearGradient id="%s" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#aab3bc"/><stop offset=".4" stop-color="#e6eaee"/>'
         '<stop offset="1" stop-color="#9aa3ad"/></linearGradient></defs>') % g
    o += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="url(#%s)" stroke="%s" stroke-width="1.5"/>' % (
        cx - w / 2, base - h, cx + w / 2, base - h, cx + w / 2 - 4, base, cx - w / 2 + 4, base, g, GREY_D)
    o += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="#c9d0d7" stroke="%s" stroke-width="1.5"/>' % (cx - w / 2 - 3, base - h, cx, base - h - 14, cx + w / 2 + 3, base - h, GREY_D)
    o += '<rect x="%.1f" y="%.1f" width="14" height="5" rx="2" fill="%s"/>' % (cx - 7, base - 2, GREY_D)
    return o


@figx('lime-igiene.svg')
def lime_igiene():
    b = title('Lime e igiene: dipende dal materiale')
    cols = [('Porosa → monouso', 'carta, spugna, buffer: nel cestino o regalala alla cliente', ERR, ERR_BG),
            ('Non porosa → pulisci e disinfetta', 'vetro e metallo', '#3f86b8', BLUE_BG),
            ('Ricambio monouso + supporto disinfettato', 'il supporto metallico resta', OK, OK_BG)]
    W = 236
    for k, (t, sub, c, bg) in enumerate(cols):
        x = 20 + k * (W + 6)
        cx = x + W / 2
        b += '<rect x="%d" y="56" width="%d" height="270" rx="14" fill="%s"/>' % (x, W, bg)
        b += badge(x + 24, 80, k + 1, c)
        if k == 0:
            b += file_r('dritta', cx - 26, 112, '#8f8379', '#2f2a28', ('', ''), -14, 0.82)
            b += file_r('buffer', cx - 50, 160, '', '', ('', ''), 0, 0.62)
            # lente sui pori con polvere e germi intrappolati
            mx, my = cx + 56, 170
            b += '<circle cx="%.1f" cy="%.1f" r="32" fill="#efe4d9" stroke="%s" stroke-width="3.5"/>' % (mx, my, ACC2)
            rnd = random.Random(5)
            for j in range(18):
                a, rr = rnd.uniform(0, 6.28), rnd.uniform(0, 24)
                b += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#b7a596"/>' % (mx + math.cos(a) * rr, my + math.sin(a) * rr, rnd.uniform(2, 3.6))
            b += germ(mx - 8, my - 6, 4, '#6f7983') + germ(mx + 10, my + 8, 3.5, '#6f7983')
            b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="6" stroke-linecap="round"/>' % (mx + 23, my + 23, mx + 38, my + 38, ACC2)
            b += bin_pedal(cx - 56, 238, 40, 46)
        elif k == 1:
            b += glass_file(cx - 6, 112, -12, 0.95)
            b += metal_file(cx - 6, 148, -12, 0.95)
            b += cleaning_brush(cx - 50, 210, 0.62, -12)
            b += spray(cx + 62, 240, 0.95)
        else:
            b += metal_file(cx - 6, 126, 0, 1.0, strip=True)
            # ricambio adesivo che si stacca
            b += ('<path d="M%.1f,117 L%.1f,117 Q%.1f,104 %.1f,86 L%.1f,92 Q%.1f,108 %.1f,124 L%.1f,124 Z" fill="#cfc2b4" stroke="#8f8379" stroke-width="1.2"/>'
                  % (cx - 54, cx + 18, cx + 44, cx + 60, cx + 70, cx + 52, cx + 22, cx - 54))
            rnd = random.Random(8)
            for j in range(40):
                b += '<circle cx="%.1f" cy="%.1f" r=".9" fill="#6d5f55" opacity=".6"/>' % (rnd.uniform(cx - 52, cx + 14), rnd.uniform(118, 123))
            b += curved(cx + 70, 96, cx + 78, 168, -26)
            b += bin_pedal(cx + 78, 226, 36, 40)
            b += spray(cx - 50, 240, 0.85)
        lines = wrap(t, W - 24, 14, True)
        b += mtext(cx, 266, lines, 14, weight=800, fill=c)
        b += mtext(cx, 266 + len(lines) * 17.5 + 2, wrap(sub, W - 24, 12.5), 12.5, weight=600, fill=MUTED)
    return svg(760, 336, arrow_defs() + b, 'Igiene delle lime: carta e buffer monouso, vetro e metallo si disinfettano, supporto metallico con ricambi monouso')


# ================================================================= MODULO 4 – ATTREZZATURA
def control_unit(x, y, w=270, h=170, rpm='15.000'):
    """Centralina della fresa: display, manopola della velocità, selettore avanti/indietro, accensione, presa del manipolo."""
    g, gk = uid('cu'), uid('cu')
    o = ('<defs><linearGradient id="%s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#dfe3e8"/></linearGradient>'
         '<radialGradient id="%s" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#ffffff"/><stop offset=".6" stop-color="#c9d0d7"/><stop offset="1" stop-color="#8d969f"/></radialGradient></defs>') % (g, gk)
    o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="16" fill="url(#%s)" stroke="%s" stroke-width="1.6" filter="url(#nxShS)"/>' % (x, y, w, h, g, GREY_D)
    o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="10" fill="#f6f7f9" stroke="#c9ced4"/>' % (x + 12, y + 34, w - 24, h - 46)
    o += text(x + 16, y + 24, 'Centralina', 16, 'start', 800, ACC2)
    # display
    o += '<rect x="%.1f" y="%.1f" width="104" height="34" rx="6" fill="#26303a"/>' % (x + 24, y + 48)
    o += text(x + 66, y + 72, rpm, 17, weight=800, fill='#8fe3b0')
    o += text(x + 113, y + 72, 'RPM', 9.5, 'end', 700, '#8fe3b0').replace('font-size="9.5"', 'font-size="12"').replace('x="%.1f"' % (x + 113), 'x="%.1f"' % (x + 124))
    # manopola
    kx, ky, kr = x + 76, y + 122, 22
    for k in range(11):
        a = math.radians(135 + k * 27)
        o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2" stroke-linecap="round"/>' % (
            kx + math.cos(a) * (kr + 5), ky + math.sin(a) * (kr + 5), kx + math.cos(a) * (kr + 10), ky + math.sin(a) * (kr + 10), ERR if k >= 8 else GREY_D)
    o += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="url(#%s)" stroke="%s" stroke-width="1.5"/>' % (kx, ky, kr, gk, GREY_D)
    for k in range(16):
        a = k * math.pi / 8
        o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1" opacity=".5"/>' % (
            kx + math.cos(a) * (kr - 4), ky + math.sin(a) * (kr - 4), kx + math.cos(a) * kr, ky + math.sin(a) * kr, GREY_D)
    a = math.radians(250)
    o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="4" stroke-linecap="round"/>' % (
        kx + math.cos(a) * 4, ky + math.sin(a) * 4, kx + math.cos(a) * (kr - 6), ky + math.sin(a) * (kr - 6), ACC2)
    # selettore F/R
    sx, sy = x + 172, y + 62
    o += '<rect x="%.1f" y="%.1f" width="26" height="48" rx="8" fill="#e9ecef" stroke="%s" stroke-width="1.5"/>' % (sx, sy, GREY_D)
    o += '<rect x="%.1f" y="%.1f" width="18" height="20" rx="5" fill="%s"/>' % (sx + 4, sy + 4, ACC2)
    o += text(sx + 36, sy + 18, 'F', 13, 'start', 800) + text(sx + 36, sy + 42, 'R', 13, 'start', 800)
    # accensione e presa
    o += '<circle cx="%.1f" cy="%.1f" r="11" fill="#fff" stroke="%s" stroke-width="1.6"/>' % (x + 236, y + 76, GREY_D)
    o += '<path d="M%.1f,%.1f a6,6 0 1 0 6,0 M%.1f,%.1f v7" stroke="%s" stroke-width="1.8" fill="none" stroke-linecap="round"/>' % (
        x + 233, y + 72, x + 236, y + 68, OK)
    o += '<circle cx="%.1f" cy="%.1f" r="9" fill="#3b4148" stroke="%s" stroke-width="2"/>' % (x + w - 28, y + h - 30, GREY_D)
    return o


@figx('fresa-anatomia.svg')
def fresa_anatomia():
    b = title('La fresa: le parti')
    b += control_unit(30, 62, 280, 186)
    b += text(106, 272, 'Velocità (RPM)', 13, weight=700) + text(106, 288, '0–35.000', 12.5, weight=600, fill=MUTED)
    b += '<line x1="106" y1="224" x2="106" y2="258" stroke="%s" stroke-width="1.3"/>' % MUTED
    b += text(222, 272, 'Avanti / Indietro', 13, weight=700)
    b += '<line x1="215" y1="172" x2="222" y2="258" stroke="%s" stroke-width="1.3"/>' % MUTED
    # cavo
    b += '<path d="M282,220 C320,240 300,318 330,318 L346,318" fill="none" stroke="#4b3a40" stroke-width="5" stroke-linecap="round"/>'
    # manipolo (punta verso destra)
    hx, hy, hs = 566, 318, 1.22
    b += '<g transform="translate(%.1f,%.1f) scale(-1,1)">%s</g>' % (hx, hy, handpiece_r(0, 0, 0, hs, 'cil', 'carburo', 'M', cord=False))
    b += text(hx - 120 * hs, hy + 36, 'Manipolo', 15, weight=800, fill=ACC2)
    b += text(hx - 120 * hs, hy + 54, 'motore + mandrino', 12.5, weight=600, fill=MUTED)
    # ingrandimento
    zx, zy, zr = 724, 150, 96
    cid = uid('zm')
    b += '<circle cx="%.1f" cy="%.1f" r="24" fill="none" stroke="%s" stroke-width="1.5" stroke-dasharray="4 3"/>' % (hx - 12, hy, GREY)
    b += '<path d="M%.1f,%.1f L%.1f,%.1f M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="1.3" stroke-dasharray="4 4"/>' % (
        hx - 30, hy - 16, zx - 88, zy + 40, hx + 8, hy - 22, zx - 20, zy + zr - 2, GREY)
    b += '<defs><clipPath id="%s"><circle cx="%.1f" cy="%.1f" r="%.1f"/></clipPath></defs>' % (cid, zx, zy, zr)
    b += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#fff" stroke="%s" stroke-width="2" filter="url(#nxSh)"/>' % (zx, zy, zr, GREY)
    b += '<g clip-path="url(#%s)"><g transform="translate(%.1f,%.1f) scale(-2.05,2.05)">%s</g></g>' % (
        cid, zx + 22, zy + 6, handpiece_r(0, 0, 0, 1.0, 'cil', 'carburo', 'M', cord=False).replace('scale(2.500)', ''))
    b += leader(zx - 70, zy + 2, 600, 96, 'Mandrino', 'end', 13)
    b += text(594, 116, 'stringe la punta', 12, 'end', 600, MUTED)
    b += callout(zx - 20, zy + 8, zx - 30, zy + zr + 26, 'Gambo 3/32" = 2,35 mm', 13, 700)
    b += callout(zx + 60, zy - 10, zx + 60, zy - zr - 6, 'Testa della punta', 13, 700)
    # punta storta
    x0, y0 = 650, 300
    b += '<rect x="%d" y="%d" width="190" height="88" rx="12" fill="%s"/>' % (x0, y0, ERR_BG)
    b += mark(x0 + 22, y0 + 22, False, 12)
    b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.2" stroke-dasharray="4 3"/>' % (x0 + 50, y0 + 30, x0 + 150, y0 + 30, GREY_D)
    b += bit_r(x0 + 80, y0 + 30, 0.9, -12, 'cil', 'carburo', 'M', shank=56)
    for k in range(3):
        b += '<path d="M%d,%d q4,-5 0,-10 q-4,-5 0,-10" fill="none" stroke="%s" stroke-width="1.8"/>' % (x0 + 152 + k * 9, y0 + 36, ERR)
    b += text(x0 + 95, y0 + 62, 'Punta storta o caduta:', 12.5, weight=700)
    b += text(x0 + 95, y0 + 79, 'vibra = buttala', 13.5, weight=800, fill=ERR)
    # coppia
    b += '<rect x="30" y="318" width="210" height="64" rx="12" fill="%s"/>' % BLUE_BG
    b += mtext(135, 344, ['Coppia: tiene la velocità', 'quando appoggi la punta'], 13, weight=700, fill='#2c6690')
    return svg(860, 400, b, 'Le parti della fresa: centralina con velocità e senso di rotazione, manipolo, mandrino, gambo da 2,35 mm e testa della punta')


@figx('punte-forme.svg')
def punte_forme():
    b = title('Le punte e dove si usano')
    ZF, ZS = 'fill="%s" fill-opacity=".38" stroke="%s" stroke-width="1.6" stroke-dasharray="4 3"' % (ACC, ACC2), ''
    tiles = [('Cilindro', 'cil', 'carburo', 'Superficie del prodotto, accorciare', 'Carburo/ceramica'),
             ('Cilindro di sicurezza', 'sic', 'diamantata', 'Superficie vicino alle pieghe', 'Punta liscia'),
             ('Cono', 'cono', 'ceramica', 'Sotto il bordo libero, angoli', 'Carburo/ceramica'),
             ('Fiamma', 'fiamma', 'diamantata', 'Solleva la cuticola, pieghe laterali', 'Diamantata'),
             ('Pallina', 'palla', 'diamantata', 'Pelle morta della zona cuticolare', 'Diamantata'),
             ('Ago', 'ago', 'diamantata', 'Dettagli, solchi laterali', 'Diamantata')]
    W, H = 300, 200
    for i, (name, sh, mat, use, chipt) in enumerate(tiles):
        x = 20 + (i % 3) * (W + 10)
        y = 56 + (i // 3) * (H + 10)
        b += '<rect x="%d" y="%d" width="%d" height="%d" rx="14" fill="%s"/>' % (x, y, W, H, PANEL)
        b += text(x + 16, y + 28, name, 15, 'start', 800)
        b += '<ellipse cx="%d" cy="%d" rx="74" ry="24" fill="#fff" opacity=".75"/>' % (x + 92, y + 72)
        b += bit_r(x + 72, y + 72, 1.55, 0, sh, mat, 'M' if mat != 'ceramica' else 'F', shank=48)
        b += mtext(x + 16, y + 122, wrap(use, 160, 13, True), 13, 'start', 700, MUTED)
        mc = {'carburo': '#7d8792', 'diamantata': '#b8902a', 'ceramica': '#9a8f86'}[mat]
        b += chip(x + 16 + (tw(chipt, 12, True) + 18) / 2, y + 176, chipt, mc, '#fff', 12)
        # dito intero con la zona d'uso
        cx, yc = x + 244, y + 126
        hw, nl, fl = 23, 56, 15
        ys, yt = yc - nl, yc - nl - fl
        zone, post, bt = '', '', ''
        if sh == 'cil':
            zone = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" %s clip-path="url(#CLIP)"/>' % (cx - hw + 5, yt + 3, 2 * hw - 10, (yc - 34) - (yt + 3), ZF)
            bt = bit_r(cx + 12, ys + 6, 0.62, 0, sh, mat, 'M', shank=40)
        elif sh == 'sic':
            zone = '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" %s clip-path="url(#CLIP)"/>' % (
                cx - hw, yc - 50, cx, yc - 6, cx + hw, yc - 50, cx + hw, yc - 22, cx, yc + 26, cx - hw, yc - 22, ZF)
            bt = bit_r(cx + 6, yc - 34, 0.62, 0, sh, mat, 'M', shank=40)
        elif sh == 'cono':
            zone = '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" %s clip-path="url(#CLIP)"/>' % (
                cx - hw - 4, ys + 8, cx, ys - 10, cx + hw + 4, ys + 8, cx + hw + 4, yt - 6, cx - hw - 4, yt - 6, ZF)
            bt = bit_r(cx + hw - 2, ys - 6, 0.62, -30, sh, mat, 'F', shank=40)
        elif sh == 'fiamma':
            post = '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f" fill="none" stroke="%s" stroke-opacity=".55" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>' % (
                cx - hw - 4, ys + 12, cx - hw - 4, yc - 28, cx, yc + 22, cx + hw + 4, yc - 28, cx + hw + 4, ys + 12, ACC)
            bt = bit_r(cx - 2, yc - 22, 0.62, -40, sh, mat, 'M', shank=40)
        elif sh == 'palla':
            post = '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" %s/>' % (
                cx - hw - 6, yc - 30, cx, yc + 18, cx + hw + 6, yc - 30, cx + hw + 10, yc - 18, cx + hw + 4, yc - 16,
                cx, yc + 32, cx - hw - 4, yc - 16, ZF)
            bt = bit_r(cx + hw - 4, yc - 10, 0.62, -25, sh, mat, 'M', shank=40)
        else:
            for sx in (-1, 1):
                post += '<rect x="%.1f" y="%.1f" width="7" height="%.1f" rx="3.5" %s/>' % (cx + sx * (hw + 4) - 3.5, ys - 4, yc - 26 - (ys - 4), ZF)
            bt = bit_r(cx + hw + 6, ys + 4, 0.62, -80, sh, mat, 'M', shank=40)
        f, p = finger_nail(cx, yc, hw=hw, nail_len=nl, free_len=fl, shape='squoval', smile=6, finger_len=90, lunula=False, extra=zone)
        cid = uid('pt')
        b += '<defs><clipPath id="%s"><rect x="%d" y="%d" width="%d" height="%d" rx="14"/></clipPath></defs>' % (cid, x, y, W, H)
        b += '<g clip-path="url(#%s)">%s%s%s</g>' % (cid, f, post, bt)
    # legenda
    yy = 492
    b += '<rect x="20" y="%d" width="18" height="14" rx="3" %s/>' % (yy - 11, ZF)
    b += text(44, yy, 'zona d\'uso', 13, 'start', 700)
    b += text(150, yy, 'Anello sul gambo = grana:', 13.5, 'start', 700)
    for k, (c, l) in enumerate([('#f1d27a', 'XF'), ('#d9534f', 'F'), ('#3f6fe0', 'M'), ('#3d9a5c', 'G'), ('#2b2b2b', 'XG')]):
        bx = 330 + k * 62
        b += '<rect x="%d" y="%d" width="18" height="14" rx="3" fill="%s"/>' % (bx, yy - 11, c)
        b += text(bx + 24, yy + 1, l, 13, 'start', 800)
    b += text(640, yy, 'fine → grossa, varia tra marchi', 13, 'start', 600, MUTED)
    return svg(960, 510, b, 'Forme delle punte per fresa (cilindro, cilindro di sicurezza, cono, fiamma, pallina, ago) con la zona d\'uso indicata su un dito intero e il materiale')


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


def client_finger_left(x, y, w=330, prod=True):
    """Dito della cliente di profilo con la punta a SINISTRA. (x, y) = punta del bordo libero; y = superficie dell'unghia."""
    o = ('<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
         % (x + 24, y + 6, x + 4, y + 8, x - 2, y + 30, x + 12, y + 58, x + 40, y + 70, x + w, y + 70, x + w, y + 4,
            x + 150, y + 4, x + 60, y + 4, x + 24, y + 6, SKIN, SKIN_D))
    # lamina + prodotto
    o += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="4" stroke-linecap="round"/>' % (x + 22, y + 6, x + 150, y + 5, NAIL_S)
    if prod:
        o += ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.2"/>'
              % (x, y + 1, x + 60, y - 2, x + 120, y - 3, x + 146, y + 1, x + 146, y + 4, x, y + 4, PROD, PROD_S))
    # piega prossimale
    o += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.3"/>'
          % (x + 144, y + 5, x + 150, y - 6, x + 170, y - 7, x + w, y - 7, x + w, y + 6, SKIN, SKIN_D))
    return o


def efile_grip(x, y, ang=0, s=1.0, rest=True):
    """Mano dell'operatrice che impugna il manipolo come una penna, mignolo appoggiato (rest=True).
    (x, y) = attacco testa-gambo della punta; il manipolo va verso destra, la mano sta sopra.
    Dita affusolate con nocche e unghie (gen_svg._digit)."""
    D, B = gen_svg._digit, gen_svg._blob
    HC, HD, HS = gen_svg._HAND, gen_svg._HAND_D, gen_svg._HAND_S
    o = ''
    # anulare ripiegato e mignolo (disteso fino al dito della cliente oppure raccolto)
    o += D([(196, -12), (176, 6), (164, 20), (168, 32)], [11.5, 10.5, 9.5, 8.5], nail=0, fill=HD, creases=(1, 2))
    if rest:
        o += D([(222, -24), (236, -6), (248, 8), (258, 16)], [10.5, 9.5, 8.5, 7.5], nail=-1, fill=HD, creases=(1, 2))
    else:
        o += D([(220, -20), (212, 0), (204, 14), (198, 22)], [10, 9, 8, 7.5], nail=0, fill=HD, creases=(1,))
    # medio sotto il manipolo
    o += D([(176, 6), (140, 20), (110, 25), (86, 25)], [12.5, 11.5, 10.5, 9.5], nail=-1, fill=HD, creases=(1, 2))
    # dorso della mano e polso (in alto a destra)
    o += B([(98, -32), (126, -66), (180, -86), (260, -96), (400, -110), (404, -30), (300, -16), (250, -10), (200, 2), (150, 4), (116, -8)], HC, HS)
    o += '<path d="M150,-70 Q178,-82 214,-84" stroke="%s" stroke-width="1.1" fill="none" opacity=".45"/>' % HS
    # manipolo
    o += handpiece_r(0, 0, 0, 1.0, 'cil', 'carburo', 'M', cord=False)
    # indice arcuato sopra il manipolo
    o += D([(172, -58), (134, -60), (104, -46), (84, -30), (70, -21)], [14, 12.5, 11, 10, 9], nail=1, creases=(2, 3))
    # pollice davanti
    o += D([(186, -10), (146, -8), (114, -2), (88, 3)], [18, 15.5, 13, 11], nail=1, creases=(2,))
    return _g(x, y, ang, s, o)


@figx('fresa-angolo.svg')
def fresa_angolo():
    b = title('Come tenere la punta')
    b += frame(20, 56, 410, 300, 'Parallela alla lamina', ok=True, border=OK)
    b += frame(450, 56, 410, 300, 'Inclinata', ok=False, border=ERR)
    S = 0.78
    # ✓ parallela: punta appoggiata di piatto, mignolo sul dito della cliente
    cid = uid('fa')
    b += '<defs><clipPath id="%s"><rect x="22" y="58" width="406" height="296" rx="15"/></clipPath></defs>' % cid
    fx, fy = 70, 242
    g = client_finger_left(fx, fy, 380)
    g += efile_grip(fx + 74, fy - 8 * S - 2, 0, S, True)
    b += '<g clip-path="url(#%s)">%s</g>' % (cid, g)
    b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2" stroke-dasharray="6 4"/>' % (fx - 6, fy - 1, fx + 120, fy - 1, OK)
    b += carrow(fx + 50, fy - 34, fx + 10, fy - 34, ACC2, 2.2) + carrow(fx + 50, fy - 34, fx + 90, fy - 34, ACC2, 2.2)
    b += mtext(fx + 50, fy - 96, ['punta di piatto,', 'tutta a contatto'], 13, weight=700, fill=OK)
    b += '<circle cx="%.1f" cy="%.1f" r="11" fill="none" stroke="%s" stroke-width="2"/>' % (fx + 74 + 254 * S, fy - 8 * S - 2 + 18 * S, ACC2)
    b += callout(fx + 74 + 254 * S, fy - 8 * S - 2 + 30 * S, 330, 296, 'Punto d\'appoggio', 13, 800, ACC2)
    b += text(330, 312, 'mignolo sulla cliente', 12.5, weight=600, fill=INK)
    b += text(225, 340, 'Pressione leggera, sempre in movimento', 14, weight=800, fill=OK)
    # ✗ inclinata: il bordo della punta scava
    cid2 = uid('fa')
    b += '<defs><clipPath id="%s"><rect x="452" y="58" width="406" height="296" rx="15"/></clipPath></defs>' % cid2
    fx2, fy2 = 500, 242
    g = client_finger_left(fx2, fy2, 380)
    px, py = fx2 + 52, fy2 - 1          # punto in cui il bordo della punta tocca
    g += ('<g transform="rotate(-30 %.1f %.1f)">%s</g>' % (px, py, efile_grip(px + 36 * S, py - 8 * S, 0, S, False)))
    b += '<g clip-path="url(#%s)">%s</g>' % (cid2, g)
    b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6" stroke-dasharray="5 4"/>' % (px, py, px + 120, py, GREY_D)
    b += '<path d="M%.1f,%.1f A86,86 0 0 0 %.1f,%.1f" fill="none" stroke="%s" stroke-width="2.2"/>' % (
        px + 86, py, px + 86 * math.cos(math.radians(30)), py - 86 * math.sin(math.radians(30)), ERR)
    b += text(px + 96, py - 18, '30°', 14, 'start', 800, ERR)
    b += '<circle cx="%.1f" cy="%.1f" r="9" fill="none" stroke="%s" stroke-width="2.5"/>' % (px, py, ERR)
    b += thermometer(px - 26, py - 118, 0.7)
    b += mtext(px - 12, py - 128, ['calore', 'da attrito'], 12.5, 'start', 700, ERR)
    # inserto vista dall'alto con anelli di fuoco
    ex = ''.join('<path d="M%.1f,%.1f a10,10 0 0 1 20,0" fill="none" stroke="%s" stroke-width="2.5"/>' % (qx, qy, ERR)
                 for qx, qy in ((-20, -30), (2, -46), (-10, -60), (8, -24)))
    ix, iy = 800, 270
    b += '<circle cx="%d" cy="%d" r="50" fill="#fff" stroke="%s" stroke-width="1.6" stroke-dasharray="4 3"/>' % (ix, iy, GREY)
    b += mini('', ix, iy - 4, 0.6)
    b += '<g transform="translate(%d,%.1f) scale(0.6)">%s</g>' % (ix, iy - 4 + 34 * 0.6, ex)
    b += text(ix, iy - 60, 'Anelli di fuoco', 13, weight=800, fill=ERR)
    b += text(610, 340, 'Il bordo scava solchi e scalda', 14, weight=800, fill=ERR)
    return svg(880, 370, b, 'Fresa: punta parallela alla lamina, impugnatura a penna e mignolo appoggiato sulla cliente; punta inclinata che scava anelli di fuoco e scalda')


def tool_brush(x, y, ang=0, l=140, bristle=ACC, kind='round'):
    """Pennello realistico (sostituisce quello base in questo file): setole a sinistra, ghiera metallica, manico affusolato."""
    if kind == 'flat':
        bd = 'M10,-6 L-16,-6.5 Q-19,-6 -19,-3 L-19,3 Q-19,6 -16,6.5 L10,6 Z'
    else:
        bd = 'M10,-5.5 C2,-7.5 -10,-7 -16,-3.2 Q-23,0 -16,3.2 C-10,7 2,7.5 10,5.5 Z'
    cid = uid('br')
    o = '<defs><clipPath id="%s"><path d="%s"/></clipPath></defs>' % (cid, bd)
    o += '<path d="%s" fill="%s" stroke="rgba(60,40,40,.45)" stroke-width=".9"/>' % (bd, bristle)
    st = ''.join('<line x1="12" y1="%.1f" x2="-24" y2="%.1f" stroke="#000" stroke-width=".5" opacity=".18"/>' % (yy, yy * .4) for yy in (-4, -2, 0, 2, 4))
    st += '<rect x="-24" y="-7" width="36" height="3" fill="#fff" opacity=".35"/>'
    st += '<rect x="2" y="-8" width="10" height="16" fill="#000" opacity=".12"/>'
    o += '<g clip-path="url(#%s)">%s</g>' % (cid, st)
    # manico affusolato
    o += '<path d="M24,-5.2 L%.1f,-3.6 Q%.1f,-3.6 %.1f,0 Q%.1f,3.6 %.1f,3.6 L24,5.2 Z" fill="#4b3a40"/>' % (22 + l, 26 + l, 26 + l, 26 + l, 22 + l)
    o += '<path d="M26,-3.2 L%.1f,-2.2" stroke="#fff" stroke-width="1.3" opacity=".35" stroke-linecap="round"/>' % (18 + l)
    # ghiera
    o += '<path d="M8,-6.2 L26,-5.4 L26,5.4 L8,6.2 Z" fill="%s" stroke="%s" stroke-width=".8"/>' % (STEEL, STEEL_E)
    o += '<line x1="18" y1="-5.8" x2="18" y2="5.8" stroke="%s" stroke-width="1"/><line x1="21" y1="-5.7" x2="21" y2="5.7" stroke="%s" stroke-width="1"/>' % (STEEL_E, STEEL_E)
    o += '<rect x="9" y="-4.6" width="16" height="1.6" fill="#fff" opacity=".6"/>'
    return '<g transform="translate(%.1f,%.1f) rotate(%.1f)">%s</g>' % (x, y, ang, o)


def gel_pot(cx, base, w=36, h=24, col='#f6c1d0', lid='#3b2a30', label=''):
    """Vasetto di gel: vetro smerigliato col prodotto, coperchio zigrinato."""
    o = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="5" fill="%s" stroke="rgba(0,0,0,.25)" stroke-width="1.2"/>' % (cx - w / 2, base - h, w, h, col)
    o += '<rect x="%.1f" y="%.1f" width="4" height="%.1f" rx="2" fill="#fff" opacity=".55"/>' % (cx - w / 2 + 4, base - h + 3, h - 6)
    o += '<rect x="%.1f" y="%.1f" width="%.1f" height="13" rx="3" fill="%s"/>' % (cx - w / 2 - 2, base - h - 12, w + 4, lid)
    for k in range(int(w / 4)):
        o += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#fff" stroke-width=".8" opacity=".25"/>' % (cx - w / 2 + 2 + k * 4, base - h - 10, cx - w / 2 + 2 + k * 4, base - h - 1)
    if label:
        o += text(cx, base - h / 2 + 4.5, label, 12, weight=800, fill=INK)
    return o


def polish_bottle(cx, base, s=1.0, col='#d65d86'):
    """Boccetta di smalto/semipermanente: vetro con prodotto colorato e tappo alto."""
    o = '<rect x="-15" y="-30" width="30" height="30" rx="9" fill="%s" stroke="rgba(0,0,0,.3)" stroke-width="1.2"/>' % col
    o += '<rect x="-11" y="-26" width="4" height="20" rx="2" fill="#fff" opacity=".55"/>'
    o += '<rect x="-6" y="-35" width="12" height="6" fill="#e9e4e6" stroke="rgba(0,0,0,.25)"/>'
    o += '<rect x="-7.5" y="-62" width="15" height="28" rx="3" fill="#2f2428"/>'
    o += '<rect x="-4.5" y="-59" width="3" height="22" rx="1.5" fill="#fff" opacity=".3"/>'
    return '<g transform="translate(%.1f,%.1f) scale(%.2f)">%s</g>' % (cx, base, s, o)


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
            b += lamp_r(x + 58, 160, 84, display=False)
            for j, (cl, lb) in enumerate((('#fbe3ea', 'B'), ('#f3a9bf', 'G'), ('#eef6fb', 'T'))):
                b += gel_pot(x + 132 + j * 40, 160, 32, 26, cl, label=lb)
            b += text(x + 172, 180, 'Base · Builder · Top', 12, weight=700, fill=MUTED)
        elif k == 1:
            b += handpiece_r(x + 54, 110, 0, 0.55, 'cil', 'carburo', 'M', cord=True)
            for j, cc in enumerate(['#d65d86', '#8e3b5a', '#e9a7bd', '#b39ddb']):
                b += polish_bottle(x + 72 + j * 36, 180, 0.8, cc)
        else:
            b += dappen(x + 50, 160, 50, 32, 0.5, lid=False) + powder_jar(x + 118, 160, 50, 32)
            b += tool_brush(x + 176, 156, -35, 48, '#f3eee6')
        yy = 202
        for it in items:
            lines = wrap(it, W - 40, 13, True)
            b += '<circle cx="%d" cy="%d" r="4" fill="%s"/>' % (x + 20, yy - 4, c)
            b += mtext(x + 32, yy, lines, 13, 'start', 700)
            yy += (18 if k == 0 else 26) + 16 * (len(lines) - 1)
    b += '<rect x="20" y="376" width="760" height="36" rx="12" fill="%s"/>' % ACC2
    b += text(400, 400, 'Un solo sistema completo all\'inizio', 16, weight=800, fill='#fff')
    return svg(800, 420, b, 'Priorità di acquisto del kit: subito il necessario per un sistema, dopo qualche mese fresa e colori, più avanti acrilico e effetti')


def chair_top(cx, cy, flip=False):
    """Sedia vista dall'alto: seduta e schienale (flip=True: schienale in basso)."""
    sy = 1 if not flip else -1
    o = '<rect x="%.1f" y="%.1f" width="70" height="40" rx="14" fill="#d8cfd3" stroke="%s" stroke-width="1.5"/>' % (cx - 35, cy - 20, GREY_D)
    o += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="9" stroke-linecap="round"/>' % (
        cx - 34, cy - sy * 24, cx, cy - sy * 40, cx + 34, cy - sy * 24, '#b8aab0')
    return o


@figx('kit-postazione.svg')
def kit_postazione():
    b = title('La postazione: tre zone')
    b += chair_top(400, 66) + text(450, 72, 'cliente', 13, 'start', 700, MUTED)
    b += chair_top(400, 380, True) + text(450, 386, 'operatrice', 13, 'start', 700, MUTED)
    g = uid('tb')
    b += ('<defs><linearGradient id="%s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6efe8"/><stop offset="1" stop-color="#eadfd4"/></linearGradient></defs>' % g)
    b += '<rect x="40" y="96" width="720" height="254" rx="14" fill="url(#%s)" stroke="#c7b9ad" stroke-width="2" filter="url(#nxShS)"/>' % g
    for k in range(6):
        b += '<path d="M50,%d q180,-6 360,0 t350,0" stroke="#e0d2c4" stroke-width="1.2" fill="none"/>' % (112 + k * 42)
    zones = [(54, 'Zona pulita', OK_BG, OK), (292, 'Zona di lavoro', '#ffffff', ACC2), (530, 'Zona sporco', ERR_BG, ERR)]
    for zx, t, bg, c in zones:
        b += '<rect x="%d" y="108" width="216" height="230" rx="10" fill="%s" fill-opacity=".9" stroke="%s" stroke-width="2" stroke-dasharray="7 5"/>' % (zx, bg, c)
        b += text(zx + 108, 132, t, 15, weight=800, fill=c)
    # pulita: buste sterili, lime nuove, flaconi chiusi
    b += pouch(66, 146, 104, 58, True) + pouch(66, 212, 104, 58, True)
    b += text(118, 290, 'buste sterili', 12.5, weight=700)
    b += file_r('dritta', 214, 196, '#8f8379', '#2f2a28', ('', ''), 90, 0.62, seed=4) + file_r('dritta', 240, 196, '#d98aa5', '#fff', ('', ''), 90, 0.62, seed=5)
    b += text(227, 252, 'lime nuove', 12.5, weight=700)
    for k, cc in enumerate(('#f6c1d0', '#eef6fb', '#fbe3ea')):
        px = 196 + k * 28
        b += '<circle cx="%d" cy="290" r="12" fill="%s" stroke="%s" stroke-width="1.4"/><circle cx="%d" cy="290" r="7" fill="#3b2a30"/><circle cx="%d" cy="287" r="2" fill="#fff" opacity=".4"/>' % (px, cc, GREY_D, px, px - 2)
    b += text(224, 322, 'flaconi chiusi', 12.5, weight=700)
    # lavoro: aspiratore con griglia, poggiamano, mano della cliente, lampada UV/LED e luce
    b += '<rect x="330" y="208" width="140" height="84" rx="8" fill="#dfe3e8" stroke="%s" stroke-width="1.6"/>' % GREY_D
    for k in range(12):
        b += '<rect x="%d" y="216" width="5" height="68" rx="2.5" fill="#9aa3ad" opacity=".75"/>' % (338 + k * 11)
    b += '<rect x="362" y="206" width="76" height="44" rx="20" fill="%s" stroke="%s" stroke-width="1.6"/>' % ('#e9a7bd', ACC2)
    b += '<rect x="368" y="212" width="64" height="32" rx="15" fill="none" stroke="#fff" stroke-width="1.2" stroke-dasharray="3 3"/>'
    b += '<g transform="translate(400,232) rotate(180)">%s</g>' % hand_back(0, 0, 0.3)
    b += text(400, 312, 'poggiamano', 12.5, weight=700) + text(400, 327, 'sull\'aspiratore', 12.5, weight=700)
    # lampada UV/LED vista dall'alto
    b += '<rect x="304" y="146" width="60" height="46" rx="16" fill="#f4f1f8" stroke="#8a7d9e" stroke-width="1.8"/>'
    b += '<path d="M314,192 L314,176 Q334,158 354,176 L354,192 Z" fill="#7b5bc4" opacity=".8"/>'
    b += '<rect x="322" y="152" width="24" height="8" rx="2" fill="#2f2840"/>'
    b += text(334, 208, 'UV/LED', 12, weight=800, fill='#6b4fa0').replace('y="208.0"', 'y="142.0"')
    # lampada da tavolo
    b += '<circle cx="484" cy="168" r="13" fill="%s" stroke="%s" stroke-width="1.5"/>' % ('#c9d0d7', GREY_D)
    b += '<path d="M484,168 L470,182 L460,198" stroke="%s" stroke-width="5" stroke-linecap="round" fill="none"/>' % GREY_D
    b += '<ellipse cx="456" cy="202" rx="15" ry="10" fill="#fff3c4" stroke="%s" stroke-width="2" transform="rotate(-50 456 202)"/>' % GREY_D
    b += text(470, 148, 'luce', 12, weight=700, fill=MUTED)
    # sporco: vaschetta con strumenti usati, cestino con coperchio, salviette usate
    b += '<rect x="546" y="150" width="118" height="70" rx="10" fill="#fff" stroke="%s" stroke-width="2"/>' % GREY_D
    b += '<rect x="552" y="156" width="106" height="58" rx="7" fill="#eef1f4"/>'
    b += nipper(618, 174, 0.75, 4) + double_pusher(604, 200, 0.62, -6)
    b += text(605, 238, 'strumenti usati', 12.5, weight=700)
    b += '<circle cx="712" cy="184" r="26" fill="#cfd6dd" stroke="%s" stroke-width="2"/>' % GREY_D
    b += '<path d="M688,184 L736,184" stroke="%s" stroke-width="1.6"/><rect x="704" y="176" width="16" height="6" rx="3" fill="%s"/>' % (GREY_D, GREY_D)
    b += '<rect x="704" y="210" width="16" height="7" rx="2" fill="%s"/>' % GREY_D
    b += text(712, 238, 'cestino', 12.5, weight=700) + text(712, 253, 'a pedale', 12.5, weight=700)
    for px, py, r in ((572, 290, 13), (600, 300, 12), (588, 276, 11)):
        b += '<circle cx="%d" cy="%d" r="%d" fill="#fff" stroke="#c7b9ad" stroke-width="1.4"/>' % (px, py, r)
        b += '<ellipse cx="%d" cy="%d" rx="%d" ry="%d" fill="%s" opacity=".5"/>' % (px + 2, py + 1, r * 0.45, r * 0.3, '#d65d86')
    b += text(676, 300, 'salviette usate', 12.5, weight=700)
    return svg(800, 410, arrow_defs() + b, 'Postazione vista dall\'alto: zona pulita, zona di lavoro con poggiamano e aspiratore, zona sporco con strumenti usati e cestino')


@figx('pennelli-cura.svg')
def pennelli_cura():
    b = title('Cura dei pennelli')
    rows = [('Acrilico', ['Pulisci nel monomero', 'Asciuga su carta', 'Rimodella la punta', 'Mai in acetone']),
            ('Gel', ['Togli il gel', 'Chiudi il cappuccio', 'Lontano dalla luce', 'Uno per prodotto'])]
    W, H = 176, 136
    AC, GB = '#f3eee6', '#f2b8c9'
    for r, (lab, items) in enumerate(rows):
        y = 56 + r * (H + 10)
        b += '<rect x="20" y="%d" width="92" height="%d" rx="12" fill="%s"/>' % (y, H, ACC2)
        b += text(66, y + H / 2 + 6, lab, 16, weight=800, fill='#fff')
        for k, t in enumerate(items):
            x = 122 + k * (W + 8)
            cx = x + W / 2
            iy = y + 66
            b += '<rect x="%d" y="%d" width="%d" height="%d" rx="12" fill="%s"/>' % (x, y, W, H, PANEL)
            b += badge(x + 20, y + 20, k + 1, ACC, 11, 13)
            if r == 0 and k == 0:
                b += dappen(cx - 18, iy + 34, 58, 36, 0.6)
                b += tool_brush(cx - 22, iy + 18, -62, 44, AC)
                b += '<path d="M%.1f,%.1f q8,-8 16,0" stroke="%s" stroke-width="1.6" fill="none"/>' % (cx - 30, iy + 2, PROD_S)
                b += mark(cx + 54, iy - 22, True, 11)
            elif r == 0 and k == 1:
                b += '<path d="M%.1f,%.1f l116,0 l-8,26 l-116,0 Z" fill="#fff" stroke="#c7b9ad" stroke-width="1.4"/>' % (cx - 54, iy + 6)
                b += tool_brush(cx - 40, iy + 16, 0, 72, AC)
                b += carrow(cx - 50, iy - 12, cx - 20, iy - 12, ACC2, 2) + text(cx + 16, iy - 8, 'tampona', 12, weight=700, fill=ACC2)
                b += drop_icon(cx - 58, iy + 36, 0.32, '#9cc7e0')
            elif r == 0 and k == 2:
                b += tool_brush(cx - 28, iy + 8, 0, 72, AC)
                b += carrow(cx - 52, iy - 14, cx - 46, iy + 2, ACC2, 2) + carrow(cx - 52, iy + 30, cx - 46, iy + 14, ACC2, 2)
                b += text(cx + 22, iy - 12, 'a punta', 12, weight=700, fill=ACC2)
            elif r == 0 and k == 3:
                b += bottle(cx + 30, iy + 32, 34, 50, '#e6f1f8', 'ACE', 12)
                b += tool_brush(cx - 34, iy + 10, -30, 40, AC)
                b += no_sign(cx - 26, iy + 4, 26, 3.5)
            elif r == 1 and k == 0:
                b += tool_brush(cx - 30, iy + 8, 0, 72, GB, 'flat')
                b += '<path d="M%.1f,%.1f l22,-8 l8,20 l-22,8 Z" fill="#fff" stroke="%s" stroke-width="1.4"/>' % (cx - 62, iy, GREY)
                b += text(cx + 18, iy - 14, 'salvietta', 12, weight=700, fill=ACC2)
            elif r == 1 and k == 1:
                b += tool_brush(cx - 10, iy + 8, 0, 64, GB, 'flat')
                b += '<rect x="%.1f" y="%.1f" width="34" height="18" rx="6" fill="%s"/>' % (cx - 84, iy - 1, INK)
                b += '<rect x="%.1f" y="%.1f" width="28" height="3" rx="1.5" fill="#fff" opacity=".3"/>' % (cx - 81, iy + 2)
                b += carrow(cx - 46, iy + 8, cx - 32, iy + 8, ACC2, 2)
            elif r == 1 and k == 3:
                for j, (bc, kd) in enumerate((('#f2b8c9', 'flat'), ('#d65d86', 'flat'), (AC, 'round'))):
                    b += tool_brush(cx - 40, iy - 14 + j * 20, 0, 64, bc, kd)
            else:
                b += '<rect x="%.1f" y="%.1f" width="104" height="34" rx="6" fill="#efe6dd" stroke="#b9a99a" stroke-width="1.4"/>' % (cx - 58, iy - 6)
                b += tool_brush(cx - 40, iy + 11, 0, 60, GB, 'flat')
                b += '<circle cx="%.1f" cy="%.1f" r="9" fill="%s"/>' % (cx + 62, iy - 30, AMBER)
                for a in range(8):
                    an = a * math.pi / 4
                    b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>' % (
                        cx + 62 + math.cos(an) * 12, iy - 30 + math.sin(an) * 12, cx + 62 + math.cos(an) * 16, iy - 30 + math.sin(an) * 16, AMBER)
                b += no_sign(cx + 62, iy - 30, 20, 3)
            b += text(cx, y + H - 12, t, 13, weight=700)
    return svg(860, 348, arrow_defs() + b, 'Cura dei pennelli: per l\'acrilico monomero, asciugatura e rimodellatura senza acetone; per il gel pulizia, cappuccio e riparo dalla luce')


def pen_grip(x, y, ang, s, tool):
    """Mano destra dell'operatrice che impugna uno strumento come una penna (vista dal lato del pollice).
    tool = svg dello strumento disegnato lungo l'asse x positivo con la punta in (0,0).
    (x, y) = punta dello strumento, ang = inclinazione (negativa = sale verso destra)."""
    D, B = gen_svg._digit, gen_svg._blob
    HC, HD, HS = gen_svg._HAND, gen_svg._HAND_D, gen_svg._HAND_S
    o = ''
    # anulare e mignolo ripiegati, medio sotto lo strumento (in secondo piano, più scuri)
    o += D([(172, 22), (142, 34), (128, 46), (134, 56)], [9.5, 9, 8, 7.5], nail=0, fill=HD)
    o += D([(160, 6), (128, 20), (110, 32), (114, 44)], [11, 10.5, 9.5, 8.5], nail=0, fill=HD, creases=(1, 2))
    o += D([(160, -4), (122, 6), (92, 12), (66, 13)], [12, 11, 10, 9], nail=-1, fill=HD, creases=(1, 2))
    # dorso della mano e polso
    o += B([(104, -24), (130, -50), (176, -58), (220, -52), (268, -46), (270, 44), (220, 52), (176, 46), (140, 30), (110, 6)], HC, HS)
    o += '<path d="M150,-48 Q176,-56 204,-52" stroke="%s" stroke-width="1.1" fill="none" opacity=".45"/>' % HS
    o += tool
    # indice arcuato sopra lo strumento
    o += D([(176, -44), (136, -48), (104, -36), (76, -20), (52, -10)], [13.5, 12, 11, 10, 9], nail=1, creases=(2, 3))
    # pollice in primo piano
    o += D([(170, 12), (130, 6), (98, 4), (70, 6)], [17, 14.5, 12.5, 10.5], nail=1, creases=(2,))
    return _g(x, y, ang, s, o)


def _tool_axis_pusher():
    """Spingicuticole lungo l'asse x con la paletta in (0,0) (per la vignetta della presa)."""
    return '<g transform="translate(104,0) rotate(180) scale(1,-1)">%s</g>' % double_pusher(0, 0, 1 / 0.72)


@figx('strumenti-manuali.svg')
def strumenti_manuali():
    b = title('Gli strumenti manuali')
    items = [('Spingicuticole', 'arretra l\'eponichio', 'Sterilizzare', lambda cx, cy: double_pusher(cx, cy, 1.0)),
             ('Curetta', 'cuticola aderente', 'Sterilizzare', lambda cx, cy: curette(cx, cy, 1.2)),
             ('Tronchesine', 'solo pelle morta', 'Sterilizzare', lambda cx, cy: nipper(cx + 22, cy, 1.0)),
             ('Forbicine', 'fibra e decorazioni', 'Sterilizzare', lambda cx, cy: cuticle_scissors(cx - 8, cy, 0.95)),
             ('Tagliatip', 'accorcia i tip', 'Disinfettare', lambda cx, cy: tip_cutter(cx + 18, cy - 4, 0.95)),
             ('Pinzette', 'strass e fibra', 'Disinfettare', lambda cx, cy: tweezers(cx, cy, 1.0)),
             ('Bastoncino d\'arancio', 'pulisce i bordi', 'Monouso', lambda cx, cy: orange_stick(cx, cy, 1.0, -8)),
             ('Spazzolino', 'unghie e strumenti', 'Disinfettare', lambda cx, cy: cleaning_brush(cx, cy + 4, 1.0))]
    bc = {'Sterilizzare': OK, 'Disinfettare': '#3f86b8', 'Monouso': '#8a8f96'}
    W, H = 166, 180
    for i, (name, use, bd, draw) in enumerate(items):
        x = 20 + (i % 4) * (W + 10)
        y = 56 + (i // 4) * (H + 10)
        cx = x + W / 2
        b += '<rect x="%d" y="%d" width="%d" height="%d" rx="14" fill="%s"/>' % (x, y, W, H, PANEL)
        b += '<ellipse cx="%.1f" cy="%d" rx="64" ry="34" fill="#fff" opacity=".7"/>' % (cx, y + 62)
        b += draw(cx, y + 62)
        b += text(cx, y + 122, name, 15, weight=800)
        b += text(cx, y + 141, use, 12.5, weight=600, fill=MUTED)
        b += chip(cx, y + 164, bd, bc[bd], '#fff', 12)
    # vignetta: come si tiene lo spingicuticole
    x, y, w, h = 734, 56, 206, 384
    b += '<rect x="%d" y="%d" width="%d" height="%d" rx="14" fill="#fff" stroke="%s" stroke-width="1.6"/>' % (x, y, w, h, '#e3d3d8')
    b += text(x + w / 2, y + 28, 'Come si tiene', 15, weight=800, fill=ACC2)
    cid = uid('vg')
    b += '<defs><clipPath id="%s"><rect x="%d" y="%d" width="%d" height="176" rx="12"/></clipPath></defs>' % (cid, x + 8, y + 40, w - 16)
    # ✓ a penna, inclinato basso, sulla lamina, verso la cuticola
    g = '<rect x="%d" y="%d" width="%d" height="176" rx="12" fill="%s"/>' % (x + 8, y + 40, w - 16, OK_BG)
    g += nail_side(x + 4, y + 176, 230)
    g += pen_grip(x + 70, y + 170, -32, 0.5, _tool_axis_pusher())
    b += '<g clip-path="url(#%s)">%s</g>' % (cid, g)
    b += mark(x + 28, y + 62, True, 12)
    b += mtext(x + w / 2, y + 238, ['A penna, inclinato basso', '(30–45°), verso la cuticola'], 12.5, weight=700, fill=OK)
    # ✗ verticale, sotto la piega
    y2 = y + 272
    cid2 = uid('vg')
    b += '<defs><clipPath id="%s"><rect x="%d" y="%d" width="%d" height="68" rx="12"/></clipPath></defs>' % (cid2, x + 8, y2, w - 16)
    g2 = '<rect x="%d" y="%d" width="%d" height="68" rx="12" fill="%s"/>' % (x + 8, y2, w - 16, ERR_BG)
    g2 += nail_side(x + 4, y2 + 50, 200)
    g2 += double_pusher(x + 64, y2 + 8, 0.62, -98)
    b += '<g clip-path="url(#%s)">%s</g>' % (cid2, g2)
    b += mark(x + 28, y2 + 22, False, 12)
    b += mtext(x + w / 2, y2 + 88, ['Mai in verticale', 'o sotto la piega'], 12.5, weight=700, fill=ERR)
    return svg(960, 450, b, 'Strumenti manuali (spingicuticole, curetta, tronchesine, forbicine, tagliatip, pinzette, bastoncino d\'arancio, spazzolino), destinazione igienica e impugnatura corretta a penna')


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
    TOP, TOP_D = '#9fc3dc', '#5f8fb0'
    PANTS, PANTS_D = '#56637a', '#3a4456'
    HAIR = '#5a3a2e'

    def part(p1, p2, r1, r2, col, st):
        return '<path d="%s" fill="%s" stroke="%s" stroke-width="1.5" stroke-linejoin="round"/>' % (_finger_path(p1[0], p1[1], p2[0], p2[1], r1, r2), col, st)

    for k, good in enumerate((True, False)):
        px = 20 + k * 370
        fl = 356
        # pavimento
        b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2"/>' % (px + 24, fl, px + 340, fl, GREY)
        # tavolo
        b += '<rect x="%d" y="%d" width="156" height="9" rx="3" fill="#cdbba9" stroke="#a8927d"/>' % (px + 184, fl - 141)
        b += '<rect x="%d" y="%d" width="8" height="132" fill="#b9a693"/>' % (px + 318, fl - 132)
        # sedia: seduta, schienale, pistone, base a razze con ruote
        b += '<rect x="%d" y="%d" width="76" height="12" rx="6" fill="#6f7983"/>' % (px + 46, fl - 114)
        b += '<rect x="%d" y="%d" width="8" height="70" fill="#9aa3ad"/>' % (px + 80, fl - 102)
        b += '<path d="M%d,%d L%d,%d M%d,%d L%d,%d" stroke="#6f7983" stroke-width="5" stroke-linecap="round"/>' % (
            px + 84, fl - 30, px + 52, fl - 12, px + 84, fl - 30, px + 116, fl - 12)
        for wx in (52, 116):
            b += '<circle cx="%d" cy="%d" r="6" fill="#3b4148"/>' % (px + wx, fl - 6)
        if good:
            b += '<rect x="%d" y="%d" width="12" height="78" rx="6" fill="#6f7983"/>' % (px + 40, fl - 196)
            b += '<path d="M%d,%d L%d,%d" stroke="#6f7983" stroke-width="4"/>' % (px + 46, fl - 118, px + 50, fl - 112)
            hip, sh, head = (px + 78, fl - 128), (px + 82, fl - 208), (px + 90, fl - 240)
            knee, ank, toe = (px + 150, fl - 124), (px + 152, fl - 18), (px + 178, fl - 8)
            elb, hand = (px + 120, fl - 150), (px + 202, fl - 150)
            ch = px + 248
        else:
            hip, sh, head = (px + 78, fl - 128), (px + 136, fl - 204), (px + 172, fl - 210)
            knee, ank, toe = (px + 150, fl - 124), (px + 118, fl - 24), (px + 134, fl - 8)
            elb, hand = (px + 176, fl - 166), (px + 240, fl - 162)
            ch = px + 296
        # aspiratore + poggiamano + mano della cliente
        b += '<rect x="%d" y="%d" width="64" height="8" rx="2" fill="#c9d0d7" stroke="%s"/>' % (ch - 32, fl - 149, GREY_D)
        b += client_hand_side(ch + 10, fl - 149, 0.42)
        if good:
            b += '<rect x="%d" y="%d" width="44" height="46" rx="5" fill="#dfe3e8" stroke="%s"/>' % (ch - 22, fl - 132, GREY_D)
            for j in range(4):
                b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.5"/>' % (ch - 14, fl - 122 + j * 9, ch + 14, fl - 122 + j * 9, GREY)
            b += text(ch, fl - 70, 'aspiratore', 12.5, weight=700, fill=MUTED)
            # lampada da tavolo
            b += '<path d="M%d,%d L%d,%d L%d,%d" fill="none" stroke="%s" stroke-width="4" stroke-linecap="round"/>' % (
                px + 330, fl - 150, px + 304, fl - 254, ch + 24, fl - 252, GREY_D)
            b += '<path d="M%d,%d l-24,22 l26,8 Z" fill="%s"/>' % (ch + 28, fl - 260, GREY_D)
            b += '<path d="M%d,%d L%d,%d L%d,%d Z" fill="#fff3c4" opacity=".75"/>' % (ch + 16, fl - 238, ch - 12, fl - 152, ch + 44, fl - 152)
        # gambe (dietro), busto, braccio, testa
        b += part(hip, knee, 15, 12, PANTS, PANTS_D) + part(knee, ank, 11, 8.5, PANTS, PANTS_D)
        b += '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="#3b2a30"/>' % (
            ank[0] - 9, ank[1] - 2, ank[0] + 7, ank[1] - 2, toe[0] + 12, toe[1] - 4, toe[0] + 10, toe[1] + 6, ank[0] - 9, toe[1] + 6)
        neck = (sh[0] + (head[0] - sh[0]) * .45, sh[1] + (head[1] - sh[1]) * .45)
        b += part(sh, neck, 7, 6.5, SKIN, SKIN_D)
        b += part(hip, sh, 19, 20, TOP, TOP_D)
        b += part(sh, elb, 9, 8, TOP, TOP_D) + part(elb, hand, 6.5, 5.5, SKIN, SKIN_D)
        b += '<ellipse cx="%.1f" cy="%.1f" rx="8" ry="5.5" fill="%s" stroke="%s" stroke-width="1.2"/>' % (hand[0] + 4, hand[1], SKIN, SKIN_D)
        b += '<circle cx="%.1f" cy="%.1f" r="19" fill="%s" stroke="%s" stroke-width="1.5"/>' % (head[0], head[1], SKIN, SKIN_D)
        if good:
            b += '<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z" fill="%s"/>' % (
                head[0] - 20, head[1] + 4, head[0] - 22, head[1] - 22, head[0] + 4, head[1] - 28, head[0] + 18, head[1] - 10,
                head[0] + 6, head[1] - 14, head[0] - 8, head[1] - 10, head[0] - 10, head[1] + 6, HAIR)
            b += '<circle cx="%.1f" cy="%.1f" r="8" fill="%s"/>' % (head[0] - 20, head[1] - 10, HAIR)
            b += '<circle cx="%.1f" cy="%.1f" r="2" fill="%s"/>' % (head[0] + 9, head[1] - 2, INK)
        else:
            b += '<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z" fill="%s"/>' % (
                head[0] - 18, head[1] - 10, head[0] - 10, head[1] - 26, head[0] + 16, head[1] - 22, head[0] + 18, head[1] - 4,
                head[0] + 8, head[1] - 10, head[0] - 4, head[1] - 12, head[0] - 12, head[1] + 2, HAIR)
            b += '<circle cx="%.1f" cy="%.1f" r="8" fill="%s"/>' % (head[0] - 18, head[1] - 16, HAIR)
            b += '<circle cx="%.1f" cy="%.1f" r="2" fill="%s"/>' % (head[0] + 8, head[1] + 8, INK)
        if good:
            b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2" stroke-dasharray="5 4"/>' % (px + 62, fl - 226, px + 62, fl - 126, OK)
            b += text(px + 104, 146, 'schiena dritta', 12.5, 'start', 700, OK)
            b += mtext(px + 126, 174, ['avambracci', 'appoggiati'], 12.5, 'start', 700, OK)
            b += text(px + 186, 338, 'piedi a terra', 12.5, 'start', 700, OK)
        else:
            b += pain(sh[0] + 20, sh[1] - 12) + pain(hip[0] + 4, hip[1] - 30) + pain(elb[0], elb[1] + 2, 9)
            b += '<path d="M%.1f,%.1f q8,-14 20,-14" fill="none" stroke="%s" stroke-width="2.2"/>' % (sh[0] - 4, sh[1] - 18, ERR)
            for t, (lx, ly) in (('collo piegato', (px + 214, 112)), ('gomiti sospesi', (px + 192, 172)), ('mano lontana', (px + 244, 236))):
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
