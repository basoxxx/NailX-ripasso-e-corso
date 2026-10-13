#!/usr/bin/env python3
"""Illustrazioni del gruppo D (moduli onicofagia, cover-colori, piedi, arte-gare). Uso: python3 tools/svg_d.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_svg import *  # palette, svg(), text(), mtext(), leader(), arrow(), panel(), mark(), finger_nail(), side_profile(), tool_*(), lamp(), timer(), steps_fig(), ...
import gen_svg
import math
import re

MINE = {}


def figx(name):
    def deco(f):
        MINE[name] = f; gen_svg.FIGS[name] = f
        return f
    return deco


# ================================================================= colori aggiuntivi (coerenti con la palette)
NAT = '#f9dce3'          # lamina naturale (rosa chiaro)
COV, COV_S = '#e8a2b2', '#c97b8f'   # gel cover coprente
CUSH = '#e6b095'         # cuscinetto di pelle rialzato (iponichio)
FORM, FORM_S = '#f6e7a8', '#d8c26a'  # cartina
CLEAR, CLEAR_S = '#d9eef5', '#7fb0cc'  # gel trasparente
WATER, WATER_S = '#d7ecf7', '#7fb4d6'
GREY, GREY_D = '#9aa3ad', '#6f7983'
YEL, YEL_BG = '#e8b83a', '#fdf3d0'
RED_BG, GREEN_BG, BLUE_BG = '#fde6e3', '#e3f3ea', '#e4f0f8'
INFL = '#e57373'         # infiammazione
MYC = '#d9b44a'          # giallo micosi
GOLD = '#d4af37'
CHROME = ('#e8e8ee', '#9da3b0', '#f5f5f7')
UV = '#9a6be0'


def T(s):
    return text(20, 38, s, 20, 'start', 800, ACC2)


def fit(s, size, maxw, mn=12):
    """Riduce il corpo del testo se la stringa non entra in maxw (stima 0,56 em per carattere)."""
    return max(mn, min(size, maxw / (0.56 * max(1, len(s)))))


def ftext(x, y, s, size, maxw, anchor='middle', weight=400, fill=INK, style=''):
    return text(x, y, s, '%.1f' % fit(s, size, maxw), anchor, weight, fill, style)


def rbox(x, y, w, h, fill=PANEL, stroke='none', sw=2, rx=14, extra=''):
    return '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%d" fill="%s" stroke="%s" stroke-width="%s"%s/>' % (
        x, y, w, h, rx, fill, stroke, sw, extra)


def frame(x, y, w, h, title=None, num=None, ok=None, body='', sub=None, sub2=None, subcol=None, fill=PANEL, tsize=15):
    """Pannello con titolo (numerato o centrato), contenuto ritagliato, ✓/✗ e didascalia in basso."""
    pc = uid('dk')
    s = '<defs><clipPath id="%s"><rect x="%d" y="%d" width="%d" height="%d" rx="16"/></clipPath></defs>' % (pc, x, y, w, h)
    s += '<rect x="%d" y="%d" width="%d" height="%d" rx="16" fill="%s"/>' % (x, y, w, h, fill)
    s += '<g clip-path="url(#%s)">%s</g>' % (pc, body)
    if sub:
        # fascia sotto la didascalia: il testo resta leggibile anche sopra il disegno
        bh = 52 if sub2 else 34
        s += '<rect x="%d" y="%d" width="%d" height="%d" fill="#f9ede9" opacity=".93" clip-path="url(#%s)"/>' % (x, y + h - bh, w, bh, pc)
        s += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#efdcd6" stroke-width="1"/>' % (x + 1, y + h - bh, x + w - 1, y + h - bh)
    right = 36 if ok is not None else 10
    if num is not None:
        s += '<circle cx="%d" cy="%d" r="14" fill="%s"/>' % (x + 25, y + 25, ACC)
        s += text(x + 25, y + 30.5, str(num), 15, weight=800, fill='#fff')
        s += ftext(x + 47, y + 30, title, tsize, w - 47 - right, 'start', 700)
    elif title:
        s += ftext(x + w / 2 - (14 if ok is not None else 0), y + 30, title, tsize + 0.5, w - 2 * right, 'middle', 700)
    if ok is not None:
        s += mark(x + w - 24, y + 25, ok, 13)
    if sub:
        yy = y + h - (34 if sub2 else 15)
        s += ftext(x + w / 2, yy, sub, 13, w - 16, weight=700, fill=subcol or (OK if ok else ERR if ok is False else INK))
    if sub2:
        s += ftext(x + w / 2, y + h - 14, sub2, 12.5, w - 16, fill=MUTED)
    return s


def strip(x, y, w, h, s, kind='warn', size=14):
    col = {'warn': (YEL_BG, YEL, '#7a5a12'), 'err': (RED_BG, ERR, ERR), 'ok': (GREEN_BG, OK, OK), 'info': (BLUE_BG, '#7fb4d6', '#2c5a78')}[kind]
    return (rbox(x, y, w, h, col[0], col[1], 1.5, 12)
            + ftext(x + w / 2, y + h / 2 + size * 0.36, s, size, w - 24, weight=700, fill=col[2]))


def dashed(x1, y1, x2, y2, col=ACC2, w=1.6, d='5 4'):
    return '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s" stroke-dasharray="%s"/>' % (x1, y1, x2, y2, col, w, d)


def ln(x1, y1, x2, y2, col=INK, w=2, extra=''):
    return '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s" stroke-linecap="round"%s/>' % (x1, y1, x2, y2, col, w, extra)


def P(d, fill='none', stroke=INK, sw=2, extra=''):
    return '<path d="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round"%s/>' % (d, fill, stroke, sw, extra)


def circ(cx, cy, r, fill='none', stroke=INK, sw=2, extra=''):
    return '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" stroke="%s" stroke-width="%s"%s/>' % (cx, cy, r, fill, stroke, sw, extra)


def g(body, tx=0, ty=0, rot=0, sc=1):
    return '<g transform="translate(%.1f,%.1f) rotate(%.1f) scale(%.3f)">%s</g>' % (tx, ty, rot, sc, body)


def curved_arrow(x1, y1, x2, y2, bend=30, col=ACC2, w=2):
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1
    cx, cy = mx - dy / L * bend, my + dx / L * bend
    m = 'ar' if col == ACC2 else 'arw'
    return '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="%s" marker-end="url(#%s)"/>' % (
        x1, y1, cx, cy, x2, y2, col, w, m)


def pause_mark(x, y, r=14):
    return circ(x, y, r, YEL, 'none', 0) + rbox(x - 6, y - 7, 4, 14, '#fff', rx=1) + rbox(x + 2, y - 7, 4, 14, '#fff', rx=1)


# ================================================================= resa "da manuale": sfumature, effetti, piedi
def _stop(o, c, a=1):
    return '<stop offset="%s" stop-color="%s" stop-opacity="%s"/>' % (o, c, a)


def _lg(i, stops, x2=1, y2=0, x1=0, y1=0):
    return '<linearGradient id="%s" x1="%s" y1="%s" x2="%s" y2="%s">%s</linearGradient>' % (i, x1, y1, x2, y2, ''.join(_stop(*s) for s in stops))


# definizioni condivise: incluse una sola volta per figura (solo se usate) da SV()
DX = {
    'dxShade': _lg('dxShade', [(0, '#000', .34), (.17, '#000', .07), (.5, '#000', 0), (.83, '#000', .08), (1, '#000', .36)]),
    'dxHi': _lg('dxHi', [(0, '#fff', .9), (.6, '#fff', .35), (1, '#fff', 0)], 0, 1),
    'dxTipShade': _lg('dxTipShade', [(0, '#000', .16), (.25, '#000', 0), (.8, '#000', 0), (1, '#000', .14)], 0, 1),
    'dxChrome': _lg('dxChrome', [(0, '#3d434c'), (.1, '#8d949e'), (.2, '#f4f6f9'), (.27, '#ffffff'), (.34, '#a9b0ba'),
                                 (.47, '#5b626c'), (.58, '#7e8691'), (.7, '#dfe3e8'), (.8, '#bfc5cd'), (.92, '#6a717b'), (1, '#353a42')]),
    'dxChromeV': _lg('dxChromeV', [(0, '#fff', .35), (.35, '#fff', 0), (.7, '#000', 0), (1, '#000', .25)], 0, 1),
    'dxGold': _lg('dxGold', [(0, '#9c7417'), (.18, '#e9c75a'), (.32, '#fff2b8'), (.46, '#d6a83a'), (.62, '#a77b1d'),
                             (.78, '#f3d77a'), (.9, '#fff0b0'), (1, '#b58a26')], 1, 1),
    'dxSilverF': _lg('dxSilverF', [(0, '#7d848e'), (.25, '#f2f4f7'), (.5, '#9aa1ab'), (.75, '#e6e9ed'), (1, '#6e757f')], 1, 1),
    'dxSpk': '<pattern id="dxSpk" width="17" height="15" patternUnits="userSpaceOnUse"><circle cx="1.5" cy="2" r=".9" fill="#e9e3ff" opacity=".9"/>'
             '<circle cx="9" cy="4.5" r=".7" fill="#fff" opacity=".7"/><circle cx="4.5" cy="9.5" r=".6" fill="#c7bdf2" opacity=".8"/>'
             '<circle cx="13.5" cy="11" r=".8" fill="#fff" opacity=".6"/><circle cx="12" cy="1" r=".5" fill="#d9cfff" opacity=".8"/>'
             '<circle cx="7" cy="13.5" r=".9" fill="#b8acef" opacity=".7"/><circle cx="16" cy="7" r=".5" fill="#fff" opacity=".5"/></pattern>',
    'dxShim': '<pattern id="dxShim" width="7" height="7" patternUnits="userSpaceOnUse"><circle cx="1.2" cy="1.5" r=".8" fill="#fff" opacity=".85"/>'
              '<circle cx="4.8" cy="4.6" r=".6" fill="#fff" opacity=".55"/><circle cx="2.5" cy="5.8" r=".5" fill="#ffe9f1" opacity=".7"/></pattern>',
    'dxPore': '<pattern id="dxPore" width="8" height="8" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.1" fill="#000" opacity=".13"/>'
              '<circle cx="6" cy="5" r=".8" fill="#000" opacity=".1"/><circle cx="4" cy="7" r=".6" fill="#000" opacity=".08"/></pattern>',
    'dxBlur': '<filter id="dxBlur" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="3.2"/></filter>',
    'dxBlurS': '<filter id="dxBlurS" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="1.4"/></filter>',
    'dxGlowUV': _lg('dxGlowUV', [(0, '#9a6be0', .55), (1, '#9a6be0', 0)], 0, 1),
    'dxWood': _lg('dxWood', [(0, '#efe4d6'), (.5, '#f6eee4'), (1, '#e8dccb')], 0, 1),
}


def svg(w, h, body, title):
    """Come gen_svg.svg, più le definizioni condivise DX usate nella figura."""
    used = [k for k in DX if 'url(#%s)' % k in body]
    return gen_svg.svg(w, h, ('<defs>%s</defs>' % ''.join(DX[k] for k in used) if used else '') + body, title)


def _hex(c):
    c = c.lstrip('#')
    if len(c) == 3:
        c = ''.join(ch * 2 for ch in c)
    return [int(c[i:i + 2], 16) for i in (0, 2, 4)]


def mix(c1, c2, t):
    a, b2 = _hex(c1), _hex(c2)
    return '#%02x%02x%02x' % tuple(int(round(a[i] + (b2[i] - a[i]) * t)) for i in range(3))


def dark(c, t=.35):
    return mix(c, '#000000', t)


def light(c, t=.35):
    return mix(c, '#ffffff', t)


def gel_fx(cx, by, w, h, shade=True, hi=True, k=1.0):
    """Ombreggiatura di curvatura + riflesso, da usare come 'extra' (clip CLIP) di nail_shape."""
    s = ''
    if shade:
        s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#dxShade)" clip-path="url(#CLIP)"/>' % (cx - w / 2, by - h - 2, w, h + 10)
        s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#dxTipShade)" clip-path="url(#CLIP)"/>' % (cx - w / 2, by - h - 2, w, h + 10)
    if hi:
        s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="url(#dxHi)" opacity="%.2f" clip-path="url(#CLIP)"/>' % (
            cx - w * 0.31, by - h * 0.9, w * 0.12, h * 0.62, w * 0.06, 0.8 * k)
    return s


def gel(cx, by, w, h, fill, stroke=None, fx='', shade=True, hi=True, sw=1.3, k=1.0):
    """Unghia in gel con volume: colore + effetto + curvatura + riflesso."""
    return nail_shape(cx, by, w, h, fill, stroke or dark(fill if fill.startswith('#') else '#888888', .4), sw, fx + gel_fx(cx, by, w, h, shade, hi, k))


def chrome_fx(cx, by, w, h):
    return ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#dxChrome)" clip-path="url(#CLIP)"/>'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#dxChromeV)" clip-path="url(#CLIP)"/>') % (
        cx - w / 2, by - h - 2, w, h + 10, cx - w / 2, by - h - 2, w, h + 10)


def cateye_fx(cx, by, w, h, mode='centro', col='#d9cfff'):
    """Banda luminosa morbida (particelle magnetiche) su base scura."""
    gid = uid('ceg')
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#dxSpk)" opacity=".35" clip-path="url(#CLIP)"/>' % (cx - w / 2, by - h - 2, w, h + 10)
    if mode in ('centro', '45'):
        s += '<defs>%s</defs>' % _lg(gid, [(0, col, 0), (.36, col, .15), (.47, col, .85), (.5, '#ffffff', 1), (.53, col, .85), (.64, col, .15), (1, col, 0)])
        band = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#%s)" filter="url(#dxBlurS)"%s/>' % (
            cx - w * 0.6, by - h * 1.3, w * 1.2, h * 1.6, gid, (' transform="rotate(-38 %.1f %.1f)"' % (cx, by - h / 2)) if mode == '45' else '')
        spk = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#dxSpk)"%s/>' % (
            cx - w * 0.14, by - h * 1.3, w * 0.28, h * 1.6, (' transform="rotate(-38 %.1f %.1f)"' % (cx, by - h / 2)) if mode == '45' else '')
        s += '<g clip-path="url(#CLIP)">%s%s</g>' % (band, spk)
    elif mode == 'lato':
        s += '<defs>%s</defs>' % _lg(gid, [(0, col, 0), (.55, col, 0), (.8, col, .45), (.95, '#ffffff', .95), (1, col, .9)])
        s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#%s)" clip-path="url(#CLIP)"/>' % (cx - w / 2, by - h - 2, w, h + 10, gid)
        s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#dxSpk)" clip-path="url(#CLIP)"/>' % (cx + w * 0.22, by - h - 2, w * 0.3, h + 10)
    elif mode == 'galassia':
        s += '<defs><radialGradient id="%s" cx=".5" cy=".45" r=".55">%s</radialGradient></defs>' % (
            gid, ''.join(_stop(*q) for q in [(0, '#ffffff', 1), (.2, col, .9), (.55, '#7d6fc0', .45), (1, '#2b2340', 0)]))
        s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#%s)" clip-path="url(#CLIP)"/>' % (cx - w / 2, by - h - 2, w, h + 10, gid)
        s += '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="url(#dxSpk)" clip-path="url(#CLIP)"/>' % (cx, by - h * 0.55, w * 0.35, h * 0.3)
    else:  # velvet
        s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#dxSpk)" clip-path="url(#CLIP)"/>' % (cx - w / 2, by - h - 2, w, h + 10)
        s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#bfb3f0" opacity=".22" clip-path="url(#CLIP)"/>' % (cx - w / 2, by - h - 2, w, h + 10)
    return s


def foil_fx(path, seed=3, clip=True):
    """Foil oro: riflessi metallici + piccole crepe (path = forma del foil trasferito)."""
    import random as _r
    rnd = _r.Random(seed)
    s = '<path d="%s" fill="url(#dxGold)"%s/>' % (path, ' clip-path="url(#CLIP)"' if clip else '')
    pid = uid('fo')
    s += '<defs><clipPath id="%s"><path d="%s"/></clipPath></defs><g clip-path="url(#%s)">' % (pid, path, pid)
    nums = [float(v) for v in re.findall(r'-?\d+\.?\d*', path)]
    xs, ys = nums[0::2], nums[1::2]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    for j in range(16):
        ax, ay = rnd.uniform(x0, x1), rnd.uniform(y0, y1)
        pts = [(ax, ay)]
        for q in range(3):
            ax += rnd.uniform(-9, 9); ay += rnd.uniform(-9, 9); pts.append((ax, ay))
        s += '<polyline points="%s" fill="none" stroke="%s" stroke-width="%.1f" opacity=".7"/>' % (
            ' '.join('%.1f,%.1f' % p for p in pts), rnd.choice(['#fff6cf', '#8a6512', '#fff']), rnd.choice([0.7, 1, 1.3]))
    s += '</g>'
    return s


def nail_shine(cx, by, w, h, k=1.0):
    """Riflesso libero (fuori da nail_shape)."""
    return P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - w * 0.22, by - h * 0.2, cx - w * 0.3, by - h * 0.55, cx - w * 0.18, by - h * 0.85),
             'none', '#fff', 3.2 * k, ' opacity=".7"')


DX['dxGrit'] = ('<pattern id="dxGrit" width="5" height="5" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".7" fill="#000" opacity=".22"/>'
                '<circle cx="3.5" cy="3" r=".6" fill="#fff" opacity=".35"/><circle cx="2" cy="4.2" r=".5" fill="#000" opacity=".15"/></pattern>')
DX['dxToeNail'] = _lg('dxToeNail', [(0, '#eab0a4'), (.2, '#f7d5cc'), (.5, '#fde6df'), (.8, '#f6d0c6'), (1, '#e6ab9f')])
DX['dxShadeW'] = _lg('dxShadeW', [(0, '#8a3f2e', .3), (.18, '#8a3f2e', .05), (.5, '#8a3f2e', 0), (.82, '#8a3f2e', .06), (1, '#8a3f2e', .32)])
DX['dxSkinR'] = ('<radialGradient id="dxSkinR" cx=".42" cy=".38" r=".7"><stop offset="0" stop-color="#fbe3d4"/><stop offset=".55" stop-color="#f3cdb6"/>'
                 '<stop offset="1" stop-color="#dba68c"/></radialGradient>')


def file_pro(x, y, ang=0, l=120, w=16, c1='#8a7d74', c2='#d9cfc6', s=1.0):
    """Lima con anima centrale, due grane e texture abrasiva."""
    b = rbox(-l / 2, -w / 2, l, w, c1, dark(c1, .3), 1, int(w / 2))
    b += rbox(-l / 2, 0, l, w / 2, c2, 'none', 0, int(w / 4))
    b += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%d" fill="url(#dxGrit)"/>' % (-l / 2, -w / 2, l, w, int(w / 2))
    b += ln(-l / 2 + w / 2, 0, l / 2 - w / 2, 0, '#fff', 1.2, ' opacity=".7"')
    return g(b, x, y, ang, s)


def nipper(x, y, ang=0, s=1.0):
    """Tronchesino per unghie dei piedi: ganasce dritte in alto, snodo, manici e molla."""
    b = ''
    # manici (sotto)
    for sx in (-1, 1):
        b += P('M%d,14 C%d,40 %d,70 %d,96 L%d,98 C%d,70 %d,40 %d,16 Z' % (sx * 4, sx * 12, sx * 22, sx * 24, sx * 15, sx * 13, sx * 5, sx * -2),
               '#9aa3ad', '#5d6670', 1.4)
        b += P('M%d,30 C%d,52 %d,74 %d,92' % (sx * 9, sx * 14, sx * 19, sx * 20), 'none', '#e8ecf0', 1.3, ' opacity=".8"')
    # molla a doppia lamina
    b += P('M-6,46 Q0,58 -4,72 M6,46 Q0,58 4,72', 'none', '#b9c1ca', 2)
    b += P('M-11,64 Q0,56 11,64', 'none', '#7c8691', 2)
    # snodo
    b += P('M-12,6 L12,6 L10,22 L-10,22 Z', '#6f7983', '#4a525b', 1.3)
    b += circ(0, 14, 4, '#d6dbe0', '#4a525b', 1.2)
    # ganasce con taglio dritto
    b += P('M-12,6 L-13,-14 L-1,-14 L-1,6 Z', '#9aa3ad', '#4a525b', 1.3) + P('M12,6 L13,-14 L1,-14 L1,6 Z', '#9aa3ad', '#4a525b', 1.3)
    b += ln(-13, -14, 13, -14, '#3b434b', 2.2) + ln(-9, -10, -9, 2, '#fff', 1, ' opacity=".7"')
    return g(b, x, y, ang, s)


def toe_top(cx, by, hw=46, nail_len=78, free=6, plate='#f3cbc6', free_col=None, finger_len=40, extra='', shape='squoval', deep=True):
    """Alluce visto dall'alto, anatomico: polpastrello largo e bombato che sporge oltre l'unghia,
    lamina larga quasi quadrata, pieghe laterali morbide che coprono i bordi (solchi profondi), piega prossimale bassa."""
    y_c = by
    y_s = y_c - nail_len
    y_t = y_s - free
    tw = hw * 1.5          # semi-larghezza massima (polpastrello)
    bw = hw * 1.3          # semi-larghezza alla base
    yp = min(y_s, y_t) - hw * 0.52   # punta del dito
    yb = by + finger_len
    toe = ('M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f '
           'C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z') % (
        cx - bw, yb + 30,
        cx - bw, y_c, cx - tw, y_s + hw * 1.0, cx - tw, y_s + hw * 0.45,
        cx - tw * 0.97, yp + hw * 0.3, cx - tw * 0.58, yp, cx, yp,
        cx + tw * 0.58, yp, cx + tw * 0.97, yp + hw * 0.3, cx + tw, y_s + hw * 0.45,
        cx + tw, y_s + hw * 1.0, cx + bw, y_c, cx + bw, yb + 30,
        cx + bw * 0.4, yb + 40, cx - bw * 0.4, yb + 40, cx - bw, yb + 30)
    tc = uid('toe')
    o = '<defs><clipPath id="%s"><path d="%s"/></clipPath></defs>' % (tc, toe)
    o += '<path d="%s" fill="%s"/>' % (toe, SKIN)
    # volume: ombra sui fianchi e luce sul polpastrello
    o += '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="#fff" opacity=".28" clip-path="url(#%s)"/>' % (cx - hw * 0.15, yp + hw * 0.32, tw * 0.62, hw * 0.24, tc)
    # lamina
    outline = nail_outline(cx, y_c, y_s, y_t, hw, shape)
    clip = uid()
    o += '<defs><clipPath id="%s"><path d="%s"/></clipPath></defs>' % (clip, outline)
    o += '<path d="%s" fill="%s"/>' % (outline, 'url(#dxToeNail)' if plate == '#f3cbc6' else plate)
    if free > 0:
        fc = free_col or (light(plate, .55) if plate == '#f3cbc6' else plate)
        o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" clip-path="url(#%s)"/>' % (cx - hw - 4, y_t - 10, 2 * hw + 8, free + 10, fc, clip)
        o += ln(cx - hw, y_s, cx + hw, y_s, dark(plate, .12), 1, ' opacity=".6"')
    o += extra.replace('CLIP', clip)
    # curvatura trasversale + riflesso
    o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#dxShadeW)" clip-path="url(#%s)"/>' % (cx - hw, y_t - 4, 2 * hw, nail_len + free + 12, clip)
    o += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="url(#dxHi)" opacity=".6" clip-path="url(#%s)"/>' % (
        cx - hw * 0.55, y_t + 8, hw * 0.2, nail_len * 0.62, hw * 0.1, clip)
    o += '<path d="%s" fill="none" stroke="%s" stroke-width="1.5"/>' % (outline, dark(plate, .35) if plate != '#f3cbc6' else '#c98f88')
    # pieghe laterali (coprono i bordi della lamina) e solco
    for sx in (-1, 1):
        x_in = cx + sx * (hw - 3)
        x_out = cx + sx * (tw + 2)
        fold = 'M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (
            x_in, y_c - 6, x_in - sx * 3, y_c - nail_len * 0.45, x_in + sx * 1, y_s + 18, cx + sx * (hw + 3), y_s + 4,
            x_out, y_s, x_out, y_c + 10)
        o += '<path d="%s" fill="%s" clip-path="url(#%s)"/>' % (fold, SKIN, tc)
        o += P('M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f' % (x_in, y_c - 6, x_in - sx * 3, y_c - nail_len * 0.45, x_in + sx * 1, y_s + 18, cx + sx * (hw + 3), y_s + 4),
               'none', SKIN_D, 1.6)
        if deep:
            o += P('M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f' % (x_in + sx * 3, y_c - 10, x_in + sx * 1, y_c - nail_len * 0.45, x_in + sx * 4, y_s + 20, cx + sx * (hw + 5), y_s + 8),
                   'none', '#b07a62', 1.4, ' opacity=".7"')
        # rotondità della piega
        o += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (x_in + sx * 8, y_c - 14, x_in + sx * 9, y_c - nail_len * 0.5, x_in + sx * 8, y_s + 16), 'none', '#fff', 3, ' opacity=".25"')
    # piega prossimale (bassa, larga) + cuticola
    pf = 'M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (cx - tw - 2, y_c - 12, cx, y_c + 16, cx + tw + 2, y_c - 12, cx + tw + 2, yb + 50, cx - tw - 2, yb + 50)
    o += '<path d="%s" fill="%s" clip-path="url(#%s)"/>' % (pf, SKIN, tc)
    o += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - hw - 2, y_c - 8, cx, y_c + 12, cx + hw + 2, y_c - 8), 'none', '#f7e3da', 2.4)
    o += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - hw - 4, y_c - 6, cx, y_c + 15, cx + hw + 4, y_c - 6), 'none', SKIN_D, 1.6)
    # pieghe dell'articolazione
    if finger_len >= 22:
        for j, dy in enumerate((0.55, 0.75)):
            yy = y_c + finger_len * dy + 6
            o += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - hw * (0.7 - j * 0.15), yy, cx, yy + 5, cx + hw * (0.7 - j * 0.15), yy), 'none', SKIN_D, 1.1, ' opacity=".6"')
    o += '<path d="%s" fill="none" stroke="%s" stroke-width="1.6"/>' % (toe, SKIN_D)
    pts = dict(cx=cx, y_c=y_c, y_s=y_s, y_t=y_t, hw=hw, fw=tw, clip=clip, yp=yp, tw=tw)
    return o, pts


def foot_top(cx, by, s=1.0, squeeze=0.0, nail='#f3cbc6', sx=1.0, nails=None):
    """Piede destro visto dall'alto (dita in alto, alluce a sinistra). by = tallone.
    squeeze 0..1 = dita compresse da una punta stretta."""
    nails = nails or [nail] * 5
    # dita: (x base, lunghezza, semi-larghezza, angolo)
    toes = [(-30, 74, 19, -4), (-1, 64, 12, 3), (19, 56, 11, 9), (36, 48, 10, 16), (51, 38, 9, 26)]
    sq = squeeze
    toes = [(x * (1 - 0.18 * sq) + (5 * sq if k == 0 else -3 * sq * k), L * (1 - 0.06 * sq * (k > 0)), r, a * (1 - sq) + (14 * sq if k == 0 else -6 * sq * k))
            for k, (x, L, r, a) in enumerate(toes)]
    base_y = [-206, -214, -206, -196, -182]
    outl = ''
    fills = ''
    det = ''
    for k, (x, L, r, a) in enumerate(toes):
        y0 = base_y[k] + (6 * sq if k else 0)
        cap = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f"/>' % (-r, -L, 2 * r, L + 20, r * 0.95)
        outl += '<g transform="translate(%.1f,%.1f) rotate(%.1f)">%s</g>' % (x, y0, a, cap.replace('/>', ' fill="%s" stroke="%s" stroke-width="3"/>' % (SKIN, SKIN_D)))
        fills += '<g transform="translate(%.1f,%.1f) rotate(%.1f)">%s</g>' % (x, y0, a, cap.replace('/>', ' fill="url(#nxSkin)"/>'))
        nw, nl = r * 1.3, r * 1.25 if k else r * 1.15
        nb = ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1"/>'
              % (-nw / 2, -L + r * 0.35 + nl, -nw / 2, -L + r * 0.55, -nw / 2, -L + r * 0.3, 0, -L + r * 0.3, nw / 2, -L + r * 0.3, nw / 2, -L + r * 0.55,
                 nw / 2, -L + r * 0.35 + nl, 0, -L + r * 0.35 + nl + r * 0.35, -nw / 2, -L + r * 0.35 + nl, nails[k], '#c98f88'))
        nb += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1" fill="#fff" opacity=".5"/>' % (-nw * 0.3, -L + r * 0.45, nw * 0.14, nl * 0.7)
        nb += P('M%.1f,%.1f Q0,%.1f %.1f,%.1f' % (-r * 0.6, -L + r * 0.5 + L * 0.42, -L + r * 0.5 + L * 0.42 + 3, r * 0.6, -L + r * 0.5 + L * 0.42), 'none', SKIN_D, 1, ' opacity=".55"')
        det += '<g transform="translate(%.1f,%.1f) rotate(%.1f)">%s</g>' % (x, y0, a, nb)
    body = ('M-34,0 C-46,-6 -48,-50 -44,-96 C-42,-140 -52,-176 -50,-204 C-48,-222 -12,-228 6,-224 '
            'C30,-220 54,-206 64,-186 C72,-168 62,-130 54,-96 C46,-60 46,-20 30,-2 C14,10 -18,10 -34,0 Z')
    out = '<path d="%s" fill="%s" stroke="%s" stroke-width="3"/>' % (body, SKIN, SKIN_D) + outl
    out += '<path d="%s" fill="url(#nxSkin)"/>' % body + fills
    # pieghe tra le dita e arco
    for k in range(4):
        xa = (toes[k][0] + toes[k + 1][0]) / 2
        out += P('M%.1f,%.1f q2,10 0,18' % (xa, base_y[k] - 4 + (3 if k else 6)), 'none', SKIN_D, 1.3, ' opacity=".7"')
    out += P('M-40,-120 C-36,-80 -36,-50 -30,-20', 'none', '#fff', 6, ' opacity=".25"')
    out += P('M20,-150 C36,-120 40,-80 34,-40', 'none', SKIN_D, 1.2, ' opacity=".35"')
    out += det
    return '<g transform="translate(%.1f,%.1f) scale(%.3f,%.3f)">%s</g>' % (cx, by, s * sx, s, out)


def foot_side(ox, oy, s=1.0):
    """Piede di profilo (punta a destra), oy = pianta: caviglia, tallone, arco, dita."""
    leg = ('M8,-170 L10,-80 C8,-56 -10,-40 -14,-20 C-16,-4 -6,2 12,2 C40,2 52,-6 82,-6 C112,-6 124,2 150,2 L176,2 '
           'C188,2 192,-6 190,-13 C188,-21 180,-24 170,-24 C152,-26 132,-34 112,-46 C88,-60 68,-78 56,-104 L52,-170 Z')
    b = '<path d="%s" fill="%s" stroke="%s" stroke-width="1.6"/>' % (leg, SKIN, SKIN_D)
    b += P('M44,-112 Q36,-96 44,-84', 'none', SKIN_D, 1.2, ' opacity=".55"')  # malleolo
    b += circ(40, -96, 9, '#fff', 'none', 0, ' opacity=".2"')
    b += P('M168,-24 C174,-28 186,-26 190,-16', 'none', '#c98f88', 4)  # unghia dell'alluce
    b += P('M150,-26 Q154,-14 150,-2', 'none', SKIN_D, 1, ' opacity=".5"')
    b += P('M20,-8 C40,-12 60,-14 80,-12', 'none', '#fff', 3, ' opacity=".3"')
    return g(b, ox, oy, 0, s)


def toe_section(cx, cy, s=1.0, nail_col='#f3cbc6', pinch=1.0, press=False):
    """Sezione trasversale dell'alluce vista dalla punta: lamina molto curva, pieghe laterali che la abbracciano."""
    b = ''
    body = 'M-150,-20 C-160,30 -110,86 0,90 C110,86 160,30 150,-20 C140,-48 110,-58 96,-52 C70,-64 -70,-64 -96,-52 C-110,-58 -140,-48 -150,-20 Z'
    b += '<path d="%s" fill="url(#dxSkinR)" stroke="%s" stroke-width="1.6"/>' % (body, SKIN_D)
    b += '<ellipse cx="0" cy="22" rx="58" ry="30" fill="#f7e6d6" stroke="#e1c3ad" stroke-width="1.2" opacity=".9"/>'
    b += text(0, 27, 'osso', 12, weight=600, fill='#b08b73')
    # letto + lamina curva (spessa)
    arc_top = 'M-100,%.1f Q0,%.1f 100,%.1f' % (-36 + 22 * pinch, -100 - 10 * pinch, -36 + 22 * pinch)
    b += P(arc_top, 'none', '#e7a9a1', 14)
    b += P(arc_top, 'none', nail_col, 10)
    b += P('M-60,%.1f Q0,%.1f 60,%.1f' % (-58 - 4 * pinch, -84 - 6 * pinch, -58 - 4 * pinch), 'none', '#fff', 2.5, ' opacity=".7"')
    # pieghe laterali che salgono sopra gli angoli
    for sx in (-1, 1):
        b += P('M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z' % (
            sx * 150, -20, sx * 146, -50, sx * 124, -62, sx * 106, -50, sx * 92, -40, sx * 90, -18, sx * 110, -6), '#f3cdb6', SKIN_D, 1.4)
    return g(b, cx, cy, 0, s)


# ----------------------------------------------------------------- dito di profilo (punta verso destra)
def finger_side(ox, oy, L=260, th=64, nx0=None, nx1=None, nail_th=5, plate=NAT, bone=True, fold=True, nail_path=None):
    """Dito di profilo con la punta a destra. oy = livello del letto (superficie su cui poggia la lamina).
    nx0/nx1 = inizio/fine della lamina. nail_path = percorso alternativo della lamina (riempito)."""
    xr = ox + L
    s = P('M%.1f,%.1f L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f Z' % (
        ox, oy, xr - 0.55 * th, oy, xr - 0.1 * th, oy, xr + 0.06 * th, oy + 0.3 * th, xr + 0.02 * th, oy + 0.58 * th,
        xr - 0.02 * th, oy + 0.92 * th, xr - 0.4 * th, oy + th, xr - 0.75 * th, oy + th, ox, oy + th), SKIN, SKIN_D, 1.5)
    if bone:
        s += rbox(ox + 10, oy + th * 0.34, L * 0.62, th * 0.36, '#efe3d0', '#cdb894', 1.2, 10)
    if nx0 is None:
        nx0 = ox + L * 0.38
    if nx1 is None:
        nx1 = xr - 0.3 * th
    if nail_path:
        s += P(nail_path, plate, NAIL_S, 1.8)
    else:
        s += P('M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z' % (
            nx0, oy - nail_th, nx1 - 3, oy - nail_th, nx1 + 2, oy - nail_th, nx1 + 2, oy - nail_th / 2, nx1, oy), plate, NAIL_S, 1.8)
    if fold:
        s += P('M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (
            ox, oy - 11, nx0 - 10, oy - 11, nx0 + 8, oy - 11, nx0 + 12, oy - nail_th + 1, nx0 + 12, oy + 3, ox, oy + 3), SKIN, 'none', 0)
        s += P('M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (ox, oy - 11, nx0 - 10, oy - 11, nx0 + 8, oy - 11, nx0 + 12, oy - nail_th + 1),
               'none', SKIN_D, 1.5)
    return s


def tip_view(cx, cy, w=70, curve=22, th=6, col=NAIL_S, fill=NAT, finger=True):
    """Unghia vista dalla punta: arco a C sopra il polpastrello."""
    s = ''
    if finger:
        s += P('M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z' % (
            cx - w * 0.6, cy + 4, cx - w * 0.62, cy + w * 0.75, cx + w * 0.62, cy + w * 0.75, cx + w * 0.6, cy + 4,
            cx + w * 0.4, cy - curve * 0.4, cx - w * 0.4, cy - curve * 0.4, cx - w * 0.6, cy + 4), SKIN, SKIN_D, 1.5)
    s += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z' % (
        cx - w / 2, cy, cx, cy - 2 * curve, cx + w / 2, cy, cx + w / 2 - 2, cy + th * 0.4, cx, cy - 2 * curve + 2 * th, cx - w / 2 + 2, cy + th * 0.4),
        fill, col, 1.8)
    return s


# ----------------------------------------------------------------- icone
def eye(x, y, s=1.0, col=INK):
    return g(P('M-18,0 Q0,-14 18,0 Q0,14 -18,0 Z', '#fff', col, 2) + circ(0, 0, 6, ACC2, 'none', 0) + circ(-2, -2, 2, '#fff', 'none', 0), x, y, 0, s)


def magnifier(x, y, r=16, ang=45):
    return (circ(x, y, r, '#eef6fb', GREY_D, 3)
            + ln(x + r * 0.72, y + r * 0.72, x + r * 1.7, y + r * 1.7, GREY_D, 6))


def scissors(x, y, ang=0, s=1.0, col=GREY_D):
    b = (circ(-14, 10, 7, '#fff', col, 3) + circ(-14, -10, 7, '#fff', col, 3)
         + P('M-8,6 L26,-4', 'none', col, 3.5) + P('M-8,-6 L26,4', 'none', col, 3.5) + circ(4, 0, 1.8, col, 'none', 0))
    return g(b, x, y, ang, s)


def oil_bottle(x, y, s=1.0):
    b = (rbox(-16, -10, 32, 40, '#f6d58a', '#c9a54a', 2, 6) + rbox(-8, -22, 16, 13, '#8e3b5a', 'none', 0, 3)
         + P('M-4,-22 Q0,-38 4,-22 Z', '#4b3a40', '#4b3a40', 1) + rbox(-10, 2, 20, 14, '#fff', 'none', 0, 3)
         + P('M-5,9 h10', 'none', '#c9a54a', 2))
    return g(b, x, y, 0, s)


def glove(x, y, s=1.0, col='#f2c94c'):
    b = P('M-18,30 L-18,-2 Q-24,-12 -22,-20 Q-16,-22 -12,-12 L-12,-30 Q-6,-34 -2,-30 L-2,-34 Q4,-38 8,-34 L8,-30 Q14,-34 18,-28 L18,30 Z',
          col, '#b38a1f', 2) + rbox(-20, 28, 40, 10, '#e0b33d', '#b38a1f', 2, 3)
    return g(b, x, y, 0, s)


def phone_cal(x, y, s=1.0):
    b = rbox(-20, -34, 40, 68, '#4b3a40', 'none', 0, 8) + rbox(-16, -26, 32, 50, '#fff', 'none', 0, 3)
    b += rbox(-16, -26, 32, 10, ACC, 'none', 0, 2)
    for r in range(3):
        for c in range(4):
            b += rbox(-13 + c * 7.5, -12 + r * 9, 5, 5, ACC if (r, c) == (1, 2) else '#e5d6d2', 'none', 0, 1)
    return g(b, x, y, 0, s)


def bulb(x, y, s=1.0):
    b = circ(0, -6, 14, '#fff3b0', '#d9b44a', 2) + rbox(-7, 7, 14, 10, GREY, 'none', 0, 2)
    for a in range(-150, -20, 30):
        r = math.radians(a)
        b += ln(20 * math.cos(r), -6 + 20 * math.sin(r), 27 * math.cos(r), -6 + 27 * math.sin(r), '#d9b44a', 2.5)
    return g(b, x, y, 0, s)


def sun(x, y, r=14):
    b = circ(x, y, r, '#ffd54f', '#e0a800', 2)
    for k in range(8):
        a = math.radians(k * 45)
        b += ln(x + (r + 4) * math.cos(a), y + (r + 4) * math.sin(a), x + (r + 10) * math.cos(a), y + (r + 10) * math.sin(a), '#e0a800', 2.5)
    return b


def window_icon(x, y, w, h):
    return (rbox(x, y, w, h, '#dff0fb', '#8fb7d0', 3, 4) + ln(x + w / 2, y, x + w / 2, y + h, '#8fb7d0', 3)
            + ln(x, y + h / 2, x + w, y + h / 2, '#8fb7d0', 3))


def bars_lamp(cx, y, w=70, label=''):
    """Lampada piccola (cupola) – riusa lamp() in scala."""
    return lamp(cx, y, w, label)


def mini_lamp(cx, cy, s=0.45):
    return g(lamp(0, 0, 90), cx, cy, 0, s)


def pen_brush(x, y, ang=0, l=90, bristle=ACC):
    return tool_brush(x, y, ang, l, bristle)


# ================================================================= MODULO 13 – ONICOFAGIA
def bitten_top(cx, yb, hw=46, bed=62, plate=NAT, cushion=True, hangnails=True, dots=True, finger_len=60):
    """Dito visto dall'alto con unghia rosicchiata: lamina corta, bordo seghettato, cuscinetto di pelle."""
    fw = hw * 1.42
    y_e = yb - bed               # bordo (seghettato) della lamina
    f_top = y_e - 0.9 * hw       # punta del dito molto oltre la lamina
    s = P('M%.1f,%.1f L%.1f,%.1f A%.1f,%.1f 0 0 1 %.1f,%.1f L%.1f,%.1f Z' % (
        cx - fw, yb + finger_len, cx - fw, f_top + fw, fw, fw, cx + fw, f_top + fw, cx + fw, yb + finger_len), SKIN, SKIN_D, 1.5)
    if cushion:
        s += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z' % (
            cx - hw - 2, y_e + 4, cx - hw, y_e - 26, cx, y_e - 30, cx + hw, y_e - 26, cx + hw + 2, y_e + 4, cx, y_e - 6, cx - hw - 2, y_e + 4),
            CUSH, '#c98f72', 1.5)
    # lamina con bordo a zig-zag
    zz = ''
    n = 9
    for k in range(n + 1):
        xx = cx + hw - k * 2 * hw / n
        yy = y_e - (5 if k % 2 == 0 else -2) - (3 if k in (3, 4) else 0)
        zz += ' L%.1f,%.1f' % (xx, yy)
    s += P('M%.1f,%.1f L%.1f,%.1f%s L%.1f,%.1f Z' % (cx - hw, yb + 6, cx + hw, yb + 6, zz, cx - hw, yb + 6), plate, NAIL_S, 1.8)
    if dots:
        for (dx, dy) in [(-14, 22), (8, 34), (18, 16)]:
            s += circ(cx + dx, y_e + dy, 3, '#8b2b3a', 'none', 0)
    # piega prossimale e pieghe laterali
    s += ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s"/>'
          % (cx - fw + 1, yb - 28, cx - hw - 4, yb - 28, cx, yb + 22, cx + hw + 4, yb - 28, cx + fw - 1, yb - 28,
             cx + fw - 1, yb + 30, cx - fw + 1, yb + 30, SKIN))
    s += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - hw - 4, yb - 28, cx, yb + 22, cx + hw + 4, yb - 28), 'none', SKIN_D, 1.8)
    for sx in (-1, 1):
        s += ln(cx + sx * (hw + 4), yb - 28, cx + sx * (hw + 4), y_e + 2, SKIN_D, 1.6)
    if hangnails:
        for sx in (-1, 1):
            bx = cx + sx * (hw + 5)
            s += P('M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (bx, yb - 40, bx + sx * 14, yb - 52, bx, yb - 48), '#fbe3d6', '#c98f72', 1.3)
    return s, dict(y_e=y_e, f_top=f_top, fw=fw)


@figx('onicofagia-segni.svg')
def oni_segni():
    W, H = 820, 400
    b = T('Come si riconosce un\'unghia rosicchiata')
    # ---- vista dall'alto
    cx = 112
    f, p = bitten_top(cx, 292, hw=46, bed=76, finger_len=60)
    b += frame(20, 58, 390, 278, body=f)
    b += text(36, 84, 'Vista dall\'alto', 15, 'start', 700)
    ye = p['y_e']
    lx = 214
    b += leader(cx + 4, ye - 20, lx, 112, 'pelle rialzata (iponichio)', size=13)
    b += leader(cx + 30, ye - 3, lx, 146, 'bordo seghettato', size=13)
    b += leader(cx + 18, ye + 16, lx, 180, 'puntini scuri = piccole', size=13)
    b += text(lx + 6, 199, 'emorragie', 13, 'start', 600)
    b += leader(cx + 8, ye + 48, lx, 232, 'letto accorciato', size=13)
    b += leader(cx + 60, 246, lx, 268, 'pellicine strappate', size=13)
    # ---- profilo
    b += rbox(420, 58, 380, 278)
    b += text(436, 84, 'Di profilo', 15, 'start', 700)
    ox, oy = 440, 214
    b += finger_side(ox, oy, L=270, th=70, nx0=ox + 95, nx1=ox + 172, nail_th=6)
    xr = ox + 270
    b += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z' % (
        ox + 174, oy, ox + 182, oy - 18, ox + 206, oy - 19, xr - 26, oy - 18, xr - 4, oy + 12, ox + 174, oy + 12), CUSH, '#c98f72', 1.5)
    b += dashed(ox + 150, oy - 6, xr + 14, oy - 6, MUTED, 1.2, '3 3')
    b += leader(ox + 212, oy - 18, ox + 196, 146, 'più alto della lamina', 'end', 13)
    b += dashed(ox + 240, 108, ox + 240, oy - 22, OK, 1.8)
    b += text(ox + 240, 102, 'qui finirebbe un letto normale', 13, 'end', 700, OK)
    b += leader(ox + 130, oy - 4, ox + 100, 300, 'lamina corta', 'middle', 13)
    b += leader(ox + 230, oy + 4, ox + 236, 300, 'cuscinetto di pelle', 'middle', 13)
    b += strip(20, 348, 780, 38, 'Banda scura nuova sulla lamina? → consiglia il medico (non spetta a te dire da cosa dipende)', 'warn', 14)
    return svg(W, H, arrow_defs() + b, 'Come si riconosce un\'unghia rosicchiata: vista dall\'alto e di profilo')


def mini_finger(cx, yb, hw=24, plate=NAT, extra_top='', free=0, nail_len=40, finger_len=30, shape='tonda'):
    f, p = finger_nail(cx, yb, hw=hw, nail_len=nail_len, free_len=free, shape=shape, smile=4, finger_len=finger_len, lunula=False,
                       plate=plate, free='#ffffff')
    return f + extra_top, p


@figx('onicofagia-semaforo.svg')
def oni_semaforo():
    W, H = 860, 400
    b = T('Valutazione: lavoro, rimando o invio?')
    cols = [('#3fae6b', 'VERDE', 'Pelle chiusa, niente dolore', 'Lavora: allungamento corto', OK, 'ok'),
            (YEL, 'GIALLO', 'Pellicine, taglietti recenti', 'Rimanda: olio e guanti', '#9a6a00', 'pause'),
            ('#d64545', 'ROSSO', 'Gonfiore, pus, ferite aperte', 'Niente servizio → medico', ERR, 'err')]
    for k, (c, name, l1, l2, tc, kind) in enumerate(cols):
        x = 20 + k * 276
        cx = x + 130
        body = circ(cx, 104, 32, c, '#4b3a40', 3) + text(cx, 109, name, 13, weight=800, fill='#fff')
        f, p = finger_nail(cx, 252, hw=38, nail_len=50, free_len=0, shape='tonda', smile=4, finger_len=18, lunula=False, plate=NAT)
        body += f
        if k == 1:
            for sx in (-1, 1):
                bx = cx + sx * 43
                body += P('M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (bx, 232, bx + sx * 20, 214, bx + sx * 2, 222), '#fde9de', '#b5735a', 1.5)
            body += P('M%.1f,%.1f l14,-9' % (cx - 62, 262), 'none', '#d9534f', 3)
            body += P('M%.1f,%.1f l12,-7' % (cx + 50, 274), 'none', '#d9534f', 3)
        if k == 2:
            body += '<ellipse cx="%.1f" cy="%.1f" rx="20" ry="40" fill="%s" opacity=".7"/>' % (cx - 50, 236, INFL)
            body += '<ellipse cx="%.1f" cy="%.1f" rx="56" ry="16" fill="%s" opacity=".55"/>' % (cx, 268, INFL)
            body += circ(cx - 50, 222, 6, '#f2d64b', '#c9a54a', 1.2)
            body += leader(cx - 50, 222, cx - 90, 160, 'pus', 'middle', 12.5)
        b += frame(x, 58, 260, 280, body=body)
        b += ftext(cx, 304, l1, 14, 240, weight=600)
        if kind == 'ok':
            b += mark(x + 24, 324, True, 11)
        elif kind == 'pause':
            b += pause_mark(x + 24, 324, 11)
        else:
            b += mark(x + 24, 324, False, 11)
        b += ftext(cx + 12, 329, l2, 14, 212, weight=800, fill=tc)
    b += arrow(60, 370, 800, 370, MUTED, 2)
    b += '<rect x="370" y="358" width="120" height="24" fill="#fff"/>'
    b += text(430, 375, 'più rischio', 14, weight=700, fill=MUTED)
    return svg(W, H, arrow_defs() + b, 'Semaforo della valutazione: verde si lavora, giallo si rimanda, rosso si invia al medico')


def form_flat(cx, cy, w=150, h=120, tab=True, notch=False, cut45=False, grid=True):
    """Cartina (form) vista piatta: corpo con ali laterali, apertura a semicerchio in alto, linguetta."""
    hw = w / 2
    r = 30
    d = ('M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f A%.1f,%.1f 0 0 0 %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z'
         % (cx - hw, cy + h / 2, cx - hw, cy - h / 2 + 18, cx - hw, cy - h / 2, cx - hw + 18, cy - h / 2, cx - r, cy - h / 2,
            r, r, cx + r, cy - h / 2, cx + hw - 18, cy - h / 2, cx + hw, cy - h / 2, cx + hw, cy - h / 2 + 18, cx + hw, cy + h / 2))
    s = ''
    if cut45:
        # lati superiori rifilati a 45°
        d = ('M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f A%.1f,%.1f 0 0 0 %.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z'
             % (cx - hw, cy + h / 2, cx - hw, cy - h / 2 + 46, cx - hw + 46, cy - h / 2, cx - r, cy - h / 2,
                r, r, cx + r, cy - h / 2, cx + hw - 46, cy - h / 2, cx + hw, cy - h / 2 + 46, cx + hw, cy + h / 2))
    clip = uid('fm')
    s += '<defs><clipPath id="%s"><path d="%s"/></clipPath></defs>' % (clip, d)
    s += P(d, FORM, FORM_S, 1.8)
    if grid:
        for k in range(1, 6):
            yy = cy - h / 2 + k * h / 6 + 6
            s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" clip-path="url(#%s)"/>' % (cx - hw, yy, cx + hw, yy, FORM_S, clip)
        s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-dasharray="4 4"/>' % (cx, cy - h / 2 + r + 2, cx, cy + h / 2, ACC2)
    if tab:
        s += P('M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f' % (cx - 18, cy - h / 2 + r - 2, cx - 18, cy - h / 2 - 2, cx + 18, cy - h / 2 - 2, cx + 18, cy - h / 2 + r - 2),
               '#fbf3cf', ERR, 1.6, ' stroke-dasharray="4 3"')
    if notch:
        s += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - 10, cy - h / 2 + r - 1, cx, cy - h / 2 + r + 22, cx + 10, cy - h / 2 + r - 1), '#fff', ERR, 2.5)
    return s


@figx('onicofagia-cartina-adattata.svg')
def oni_cartina():
    W, H = 900, 420
    b = T('Adattare la cartina su unghie rosicchiate')
    ws = [184, 184, 184, 292]
    xs = [20]
    for w in ws[:-1]:
        xs.append(xs[-1] + w + 12)
    y0, h = 58, 344
    # 1 linguetta
    x, w = xs[0], ws[0]
    body = form_flat(x + w / 2, y0 + 200, 150, 140, tab=True)
    body += scissors(x + w / 2 + 50, y0 + 110, 200, 0.9, ERR)
    b += frame(x, y0, w, h, 'Linguetta', 1, body=body, sub='taglia la linguetta', sub2='se ostacola l\'appoggio')
    # 2 U
    x, w = xs[1], ws[1]
    body = g(form_flat(0, 0, 150, 140, tab=False, notch=True), x + w / 2, y0 + 214, 0, 1.1)
    body += circ(x + w / 2, y0 + 156, 26, 'none', ERR, 2, ' stroke-dasharray="4 3"')
    body += text(x + w / 2, y0 + 108, 'piccola "U"', 14, weight=800, fill=ERR)
    b += frame(x, y0, w, h, 'Taglio a U', 2, body=body, sub='per l\'iponichio rialzato', sub2='non preme sulla pelle')
    # 3 lati 45
    x, w = xs[2], ws[2]
    cx, cy = x + w / 2, y0 + 210
    body = form_flat(cx, cy, 150, 150, tab=False, notch=True, cut45=True)
    for sx in (-1, 1):
        body += P('M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f' % (cx + sx * 75, cy - 75 + 46, cx + sx * 75, cy - 75, cx + sx * (75 - 46), cy - 75),
                  'none', MUTED, 1.4, ' stroke-dasharray="3 3"')
        body += text(cx + sx * 52, cy - 86, '45°', 15, weight=800, fill=ACC2)
    b += frame(x, y0, w, h, 'Lati a 45°', 3, body=body, sub='seguono i solchi laterali', sub2='curva a C più regolare')
    # 4 profilo + vista dalla punta
    x, w = xs[3], ws[3]
    ox, oy = x + 6, y0 + 120
    body = finger_side(ox, oy, L=170, th=60, nx0=ox + 70, nx1=ox + 122, nail_th=5, bone=False)
    # cuscinetto abbassato
    body += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z' % (ox + 124, oy + 1, ox + 140, oy - 3, ox + 158, oy + 2, ox + 124, oy + 6), CUSH, '#c98f72', 1.2)
    # cartina: prosegue dritta dal bordo e avvolge il polpastrello
    body += P('M%.1f,%.1f L%.1f,%.1f' % (ox + 121, oy + 1, ox + 270, oy + 1), 'none', FORM_S, 5)
    body += P('M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f' % (ox + 150, oy + 3, ox + 182, oy + 6, ox + 186, oy + 40, ox + 160, oy + 62), 'none', FORM_S, 5)
    body += arrow(ox + 214, oy + 14, ox + 214, oy + 52, ACC2, 2.4)
    body += text(x + w - 14, oy - 46, 'tira giù:', 13, 'end', 700, ACC2)
    body += text(x + w - 14, oy - 30, 'la pelle scende', 13, 'end', 700, ACC2)
    # riquadri dalla punta
    by = y0 + 226
    body += text(x + w / 2, by - 10, 'controlla dalla punta', 13, weight=700, fill=MUTED)
    for k, okk in enumerate([True, False]):
        bx0 = x + 10 + k * 141
        body += rbox(bx0, by, 131, 106, '#fff', OK if okk else ERR, 1.5, 10)
        bx = bx0 + 60
        body += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (bx - 42, by + 60, bx, by + 42, bx + 42, by + 60), 'none', FORM_S, 5)
        yy = by + 47 - (0 if okk else 14)
        body += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (bx - 28, yy + 6, bx, yy - 14, bx + 28, yy + 6), 'none', NAIL_S, 5)
        if not okk:
            body += P('M%.1f,%.1f q5,7 0,11 q-5,-4 0,-11 z' % (bx, by + 44), CLEAR, CLEAR_S, 1.2)
        body += mark(bx0 + 112, by + 18, okk, 10)
        body += text(bx, by + 82, 'a filo:' if okk else 'spazio:', 12.5, weight=800, fill=OK if okk else ERR)
        body += text(bx, by + 98, 'nessuno spazio' if okk else 'il prodotto cola', 12.5, weight=700, fill=OK if okk else ERR)
    b += frame(x, y0, w, h, 'Tira verso il basso', 4, body=body)
    return svg(W, H, arrow_defs() + b, 'Adattare la cartina su unghie rosicchiate: linguetta, taglio a U, lati a 45 gradi, cartina tirata verso il basso')


def ext_nail(cx, yb, hw=26, nat=34, cov=0, free=0, free_col='#ffffff', shape='tonda', finger_len=26, show_nat=True, smile=6, plate=NAT):
    """Unghia vista dall'alto con letto naturale (nat), cover oltre il letto (cov) e bordo libero (free)."""
    ext = ''
    if cov:
        ext += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" clip-path="url(#CLIP)"/>' % (cx - hw - 8, yb - nat - cov - 4, 2 * hw + 16, cov + 8, COV)
    f, p = finger_nail(cx, yb, hw=hw, nail_len=nat + cov, free_len=free, shape=shape, smile=smile, finger_len=finger_len, lunula=False,
                       plate=plate, free=free_col, extra=ext)
    if show_nat:
        f += dashed(cx - hw - 10, yb - nat, cx + hw + 10, yb - nat, ACC2, 1.5)
    return f, p


@figx('onicofagia-step.svg')
def oni_step():
    labels = ['Prepara', 'Cartina a filo', 'Cover oltre il letto', 'Bordo corto', 'Apex in zona 2', 'Lima tondo']
    subs = ['opacizza leggero, niente tagli', 'in asse con il dito', 'il letto sembra più lungo', 'bianco o trasparente, corto',
            'apex basso, niente gobba', 'tonda, nessuno spigolo']
    NB, CV, FR = 50, 30, 22

    def d(i):
        cx, yb = 150, 222
        s = ''
        if i == 0:
            f, p = ext_nail(cx, yb, hw=32, nat=NB, show_nat=True)
            s += f
            for k in range(16):
                s += circ(cx - 18 + (k * 7) % 36, yb - 10 - (k * 11) % 36, 1.2, '#c98f9e', 'none', 0)
            s += tool_pusher(cx + 26, yb - 22, -55, 80)
        elif i in (1, 2, 3):
            s += form_top(cx, yb - NB, 70, 110)
            f, p = ext_nail(cx, yb, hw=32, nat=NB, cov=CV if i >= 2 else 0, free=FR if i == 3 else 0, smile=7)
            s += f
            if i == 2:
                s += arrow(cx + 92, yb - NB, cx + 92, yb - NB - CV, ACC2, 2)
                s += text(cx + 92, yb - NB - CV - 10, '+2–3 mm', 13, 'middle', 800, ACC2)
            if i == 3:
                s += leader(cx + 10, yb - NB - CV - 10, cx + 94, yb - NB - CV - 40, 'corto', 'start', 13)
        elif i == 4:
            sp, pp = side_profile(60, 150, w=180, stress=0.6, apex=0.45, apex_h=16, tip_h=5, root_h=2, gap=6, product='#f2c6d2')
            s += sp + circ(pp['ax'], pp['ah'], 4.5, ACC2, 'none', 0)
            s += leader(pp['ax'], pp['ah'], pp['ax'] + 30, 86, 'apex basso', 'start', 13)
        else:
            f, p = ext_nail(cx, yb, hw=32, nat=NB, cov=CV, free=FR, smile=7, show_nat=False)
            s += f
            s += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - 12, yb - 22, cx - 15, yb - 60, cx - 8, yb - 86), 'none', '#fff', 4, ' opacity=".8"')
            s += mark(cx + 80, yb - 90, True, 13)
        return s
    pw, ph = 300, 262
    W = 3 * pw + 2 * 14 + 40
    b = T('Costruzione su unghia rosicchiata: 6 passaggi')
    b += text(W - 20, 38, '- - -  fine del letto naturale', 13, 'end', 700, ACC2)
    for i, lab in enumerate(labels):
        x = 20 + (i % 3) * (pw + 14)
        y = 60 + (i // 3) * (ph + 14)
        b += frame(x, y, pw, ph, lab, i + 1, body=g(d(i), x, y), sub=subs[i], subcol=OK if i == 5 else MUTED)
    return svg(W, 60 + 2 * (ph + 14) + 6, arrow_defs() + b, 'Costruzione su unghia rosicchiata in sei passaggi: preparazione, cartina, cover, bordo, apex, limatura')


def nail_right(x0, cy, bed, free, hw=30, cov_from=None, free_col='#ffffff', fl=70):
    """Dito con unghia vista dall'alto, ruotato con la punta verso destra. x0 = cuticola."""
    ext = ''
    if cov_from is not None:
        ext = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" clip-path="url(#CLIP)"/>' % (-hw - 8, -bed - 4, 2 * hw + 16, bed - cov_from + 4, COV)
    f, p = finger_nail(0, 0, hw=hw, nail_len=bed, free_len=free, shape='tonda', smile=6, finger_len=fl, lunula=False,
                       plate=NAT, free=free_col, extra=ext)
    return '<g transform="translate(%.1f,%.1f) rotate(90)">%s</g>' % (x0, cy, f)


@figx('onicofagia-proporzioni.svg')
def oni_prop():
    W, H = 780, 360
    b = T('Quanto allungare? Circa 1/3')
    b += rbox(20, 58, 470, 250)
    x0, cy, bed = 116, 206, 204
    b += nail_right(x0, cy, bed, bed / 3, hw=38, cov_from=120, fl=80)
    ry = 128
    b += ln(x0, ry, x0 + bed + bed / 3, ry, INK, 1.5)
    for k in range(5):
        xx = x0 + k * bed / 3
        b += ln(xx, ry - 7, xx, ry + 7, INK, 1.5)
    for k in range(3):
        b += text(x0 + (k + 0.5) * bed / 3, ry - 10, str(k + 1), 15, weight=800)
    b += rbox(x0 + bed + 3, ry - 5, bed / 3 - 6, 10, '#f6c6d6', rx=3)
    b += text(x0 + bed + bed / 6, ry - 10, '≈ 1/3', 15, weight=800, fill=ACC2)
    b += mark(44, 84, True, 12) + text(64, 89, 'allungamento ≈ 1/3 della lamina', 15, 'start', 800, OK)
    # graffe sotto
    yb = 262
    b += P('M%.1f,%.1f v8 H%.1f v-8' % (x0 + 2, yb, x0 + bed - 2), 'none', MUTED, 1.5)
    b += P('M%.1f,%.1f v8 H%.1f v-8' % (x0 + bed + 2, yb, x0 + bed + bed / 3 - 2), 'none', ACC2, 1.5)
    b += text(x0 + bed / 2, yb + 28, 'lamina (letto + cover)', 13, weight=700, fill=MUTED)
    b += text(x0 + bed + bed / 6, yb + 28, 'allungamento', 13, weight=700, fill=ACC2)
    # esempio sbagliato
    b += rbox(504, 58, 256, 250)
    x1, bed2 = 552, 110
    b += nail_right(x1, 196, bed2, bed2 * 2 / 3 + 10, hw=24, cov_from=62, fl=40)
    b += mark(738, 84, False, 12)
    b += text(622, 89, 'bordo lungo il doppio', 14, weight=800, fill=ERR)
    b += text(632, 262, 'leva troppo lunga:', 14, weight=700, fill=ERR)
    b += text(632, 282, 'si rompe e si solleva', 14, weight=700, fill=ERR)
    b += strip(20, 318, 740, 34, 'Allunga poco alla volta, refill dopo refill', 'ok', 14)
    return svg(W, H, arrow_defs() + b, 'Proporzioni su unghia rosicchiata: allungamento al massimo circa un terzo della lamina')


@figx('unghie-difficili-viste.svg')
def diff_viste():
    W, H = 900, 400
    b = T('Osserva da tre lati')
    pw = 280
    titles = ['Dall\'alto', 'Di profilo', 'Dalla punta']
    for k in range(3):
        x = 20 + k * (pw + 10)
        b += rbox(x, 58, pw, 200)
        b += eye(x + 30, 84, 0.9) + arrow(x + 50, 84, x + 74, 84, MUTED, 2)
        b += text(x + 84, 89, titles[k], 15, 'start', 700)
        cx = x + pw / 2
        if k == 0:
            f, p = finger_nail(cx - 40, 232, hw=30, nail_len=70, free_len=18, shape='squoval', smile=6, finger_len=20, lunula=False, plate=NAT)
            b += f
            b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6" marker-start="url(#ar)" marker-end="url(#ar)"/>' % (cx - 70, 126, cx - 10, 126, ACC2)
            b += text(cx + 4, 131, 'larghezza', 13, 'start', 700)
            b += dashed(cx - 74, 140, cx - 74, 232, OK) + dashed(cx - 6, 140, cx - 6, 232, OK)
            b += text(cx + 4, 190, 'lati paralleli?', 13, 'start', 700)
        elif k == 1:
            ox = x + 18
            b += finger_side(ox, 180, L=180, th=56, nx0=ox + 80, nx1=ox + 196, nail_th=5)
            b += text(cx, 130, 'dritta? sale? scende?', 13, weight=700)
            b += curved_arrow(ox + 210, 168, ox + 236, 150, -10) + curved_arrow(ox + 210, 178, ox + 236, 196, 10)
        else:
            b += tip_view(cx - 30, 190, w=110, curve=26, th=8)
            b += text(cx + 46, 150, 'curva C', 13, 'start', 700)
            b += text(cx + 46, 186, 'pinza', 13, 'start', 700)
            b += text(cx + 46, 204, 'o piatta?', 13, 'start', 700)
    # mini icone
    b += text(20, 290, 'Le forme da riconoscere', 15, 'start', 700, ACC2)
    names = [('cucchiaio', 'profilo concavo'), ('ski-jump', 'profilo che sale'), ('pinza', 'C quasi chiusa'), ('piatta', 'quasi dritta')]
    for k, (n, sub) in enumerate(names):
        x = 20 + k * 217
        b += rbox(x, 300, 207, 88, '#fff', '#e5d6d2', 1.5, 12)
        cx, cy = x + 56, 350
        if k == 0:
            b += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - 36, cy - 14, cx, cy + 12, cx + 36, cy - 14), 'none', NAIL_S, 5)
            b += P('M%.1f,%.1f q4,6 0,9 q-4,-3 0,-9 z' % (cx, cy - 10), '#7fc3e8', 'none', 0)
        elif k == 1:
            b += P('M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - 40, cy, cx + 10, cy, cx + 30, cy, cx + 40, cy - 22), 'none', NAIL_S, 5)
        elif k == 2:
            b += P('M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f' % (cx - 24, cy + 16, cx - 34, cy - 34, cx + 34, cy - 34, cx + 24, cy + 16), 'none', NAIL_S, 5)
        else:
            b += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - 40, cy + 4, cx, cy - 6, cx + 40, cy + 4), 'none', NAIL_S, 5)
        b += text(x + 104, 340, n, 15, 'start', 800)
        b += text(x + 104, 360, sub, 12.5, 'start', 400, MUTED)
    return svg(W, H, arrow_defs() + b, 'Le tre viste per riconoscere la forma dell\'unghia: dall\'alto, di profilo, dalla punta')


@figx('ski-jump-correzione.svg')
def ski_jump():
    W, H = 860, 360
    b = T('Ski-jump: accorcia e inclina')
    b += rbox(20, 58, 300, 250)
    b += mark(296, 82, False, 13)
    ox, oy = 30, 190
    nail = 'M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z' % (
        ox + 70, oy - 5, ox + 150, oy - 5, ox + 172, oy - 6, ox + 186, oy - 22, ox + 188, oy - 17, ox + 172, oy, ox + 70, oy)
    b += finger_side(ox, oy, L=180, th=60, nx0=ox + 70, nail_path=nail)
    b += P('M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (ox + 186, oy - 22, ox + 270, oy - 62, ox + 272, oy - 54, ox + 188, oy - 15), '#f2c6d2', NAIL_S, 1.6)
    b += text(160, 108, 'segue la salita: "a paletta"', 14, weight=700, fill=ERR)
    b += text(170, 290, 'allungamento storto', 13, fill=MUTED, weight=600)
    b += rbox(330, 58, 200, 250)
    ox2 = 340
    b += finger_side(ox2, oy, L=150, th=60, nx0=ox2 + 50, nail_path='M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z' % (
        ox2 + 50, oy - 5, ox2 + 125, oy - 5, ox2 + 145, oy - 6, ox2 + 158, oy - 22, ox2 + 160, oy - 17, ox2 + 145, oy, ox2 + 50, oy))
    b += dashed(ox2 + 132, 100, ox2 + 132, oy + 20, ERR, 2)
    b += scissors(ox2 + 132, 112, 90, 0.9, ERR)
    b += text(430, 280, 'accorcia qui:', 14, weight=800, fill=ERR)
    b += text(430, 298, 'dove inizia la salita', 13, fill=MUTED, weight=600)
    b += rbox(540, 58, 300, 250)
    b += mark(816, 82, True, 13)
    ox3 = 552
    b += finger_side(ox3, oy, L=170, th=60, nx0=ox3 + 70, nx1=ox3 + 146, nail_th=5)
    b += P('M%.1f,%.1f L%.1f,%.1f' % (ox3 + 146, oy + 1, ox3 + 282, oy + 12), 'none', FORM_S, 5)
    b += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (
        ox3 + 80, oy - 6, ox3 + 120, oy - 24, ox3 + 170, oy - 22, ox3 + 280, oy - 2, ox3 + 282, oy + 6, ox3 + 146, oy - 1, ox3 + 80, oy - 1),
        '#f2c6d2', NAIL_S, 1.6)
    b += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z' % (
        ox3 + 110, oy - 6, ox3 + 130, oy - 20, ox3 + 165, oy - 20, ox3 + 175, oy - 4, ox3 + 140, oy - 3, ox3 + 110, oy - 6), '#e46f8f', 'none', 0, ' opacity=".55"')
    b += leader(ox3 + 145, oy - 14, ox3 + 120, 112, 'più prodotto in zona 2', 'middle', 13)
    b += arrow(ox3 + 266, oy + 22, ox3 + 266, oy + 46, ACC2, 2)
    b += text(690, 262, 'cartina un po\' in giù', 13.5, weight=700, fill=OK)
    b += text(690, 284, 'linea superiore dritta', 13.5, weight=700, fill=OK)
    b += strip(20, 318, 820, 32, 'A ogni refill controlla di profilo: l\'unghia tende a tornare a salire', 'info', 13.5)
    return svg(W, H, arrow_defs() + b, 'Ski-jump di profilo: a sinistra l\'errore, al centro dove accorciare, a destra la correzione')


@figx('cucchiaio-livellamento.svg')
def spoon():
    W, H = 760, 330
    b = T('Unghia a cucchiaio: prima livella')
    subs = [('trattiene una goccia', MUTED), ('velo di builder nella conca', MUTED), ('poi curva C e apex', OK)]
    for k in range(3):
        x = 20 + k * 245
        b += rbox(x, 58, 230, 210)
        b += circ(x + 26, 84, 14, ACC, 'none', 0) + text(x + 26, 89.5, str(k + 1), 15, weight=800, fill='#fff')
        cx, cy = x + 115, 170
        # polpastrello (vista dalla punta) + lamina concava
        b += P('M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z' % (cx - 70, cy + 6, cx - 70, cy + 80, cx + 70, cy + 80, cx + 70, cy + 6), SKIN, SKIN_D, 1.5)
        lam = 'M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - 66, cy - 20, cx, cy + 24, cx + 66, cy - 20)
        if k >= 1:
            b += P(lam + ' L%.1f,%.1f L%.1f,%.1f Z' % (cx + 66, cy - 20, cx - 66, cy - 20), CLEAR, CLEAR_S, 1.5)
        if k == 2:
            b += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z' % (
                cx - 68, cy - 18, cx, cy - 70, cx + 68, cy - 18, cx + 66, cy - 20, cx, cy - 20, cx - 66, cy - 20), '#f2c6d2', NAIL_S, 1.6)
        b += P(lam, 'none', NAIL_S, 6)
        if k == 0:
            b += P('M%.1f,%.1f q9,14 0,20 q-9,-6 0,-20 z' % (cx, cy - 14), '#7fc3e8', '#4f9ac4', 1.2)
        if k == 1:
            b += dashed(cx - 66, cy - 20, cx + 66, cy - 20, ACC2, 1.5)
            b += text(cx, cy - 30, 'ora è piatta', 12.5, weight=700, fill=ACC2)
        b += ftext(cx, 252, subs[k][0], 14, 210, weight=700, fill=subs[k][1])
        if k == 2:
            b += mark(x + 204, 84, True, 12)
        if k < 2:
            b += arrow(x + 232, 170, x + 243, 170, MUTED, 2)
    b += text(20, 296, 'Vista dalla punta (sezione trasversale).', 13, 'start', 600, MUTED)
    b += strip(380, 280, 360, 34, 'Comparsa da poco? Consiglia il medico', 'warn', 14)
    return svg(W, H, arrow_defs() + b, 'Unghia a cucchiaio in sezione: prima si livella la conca, poi si costruisce')


@figx('onicofagia-timeline.svg')
def oni_timeline():
    W, H = 920, 340
    b = T('Il recupero richiede mesi')
    b += rbox(730, 18, 170, 32, GREEN_BG, OK, 1.5, 16) + text(815, 39, '≈ 3,5 mm al mese', 14, weight=800, fill=OK)
    stops = [('Seduta 1', 'cover lungo, bordo corto'), ('2 settimane', 'controllo e ritocco'), ('1 mese', '+3–4 mm di unghia'),
             ('3 mesi', 'letto più lungo'), ('≈ 6 mesi', 'unghia rinnovata')]
    b += ln(110, 92, 810, 92, ACC, 4)
    nat_l = [30, 32, 42, 56, 76]
    for k, (t, sub) in enumerate(stops):
        cx = 110 + k * 175
        b += circ(cx, 92, 12, '#fff', ACC, 4)
        b += text(cx, 72, t, 14, weight=800)
        nat = nat_l[k]
        f, p = ext_nail(cx, 262, hw=28, nat=nat, cov=max(0, 76 - nat), free=16, smile=6, finger_len=30, show_nat=k < 4)
        b += f
        b += ftext(cx, 322, sub, 13.5, 168, weight=700 if k == 4 else 600, fill=OK if k == 4 else INK)
    b += rbox(20, 116, 14, 14, NAT, NAIL_S, 1, 3) + text(40, 128, 'unghia naturale', 12.5, 'start', 600)
    b += rbox(20, 138, 14, 14, COV, NAIL_S, 1, 3) + text(40, 150, 'cover', 12.5, 'start', 600)
    return svg(W, H, arrow_defs() + b, 'Linea del tempo indicativa del recupero da onicofagia: dalla prima seduta a circa 6 mesi')


@figx('onicofagia-aftercare.svg')
def oni_aftercare():
    W, H = 820, 330
    b = T('A casa: cosa aiuta')
    items = [('Olio ogni giorno', 'meno pellicine'), ('Limetta in borsa', 'limare, non mordere'),
             ('Guanti per pulizie', 'pelle protetta'), ('Refill puntuale', 'ogni 2 settimane all\'inizio')]
    for k, (t1, t2) in enumerate(items):
        x = 20 + k * 197
        cx = x + 93
        b += rbox(x, 58, 186, 196)
        if k == 0:
            b += oil_bottle(cx, 130, 1.5)
        elif k == 1:
            b += tool_file(cx, 130, -35, 130, 20)
        elif k == 2:
            b += glove(cx, 130, 1.4)
        else:
            b += phone_cal(cx, 128, 1.25)
        b += ftext(cx, 210, t1, 15, 176, weight=800)
        b += ftext(cx, 232, t2, 13, 176, weight=600, fill=MUTED)
    b += rbox(20, 268, 780, 46, RED_BG, ERR, 1.5, 12)
    b += mark(48, 291, False, 13)
    b += text(72, 297, 'Non tirare ciò che si stacca: porta via strati di lamina. Chiama e fissa un ritocco.', 15, 'start', 700, ERR)
    return svg(W, H, b, 'Consigli a casa dopo la ricostruzione su unghie rosicchiate: olio, limetta, guanti, refill puntuale')


def nail_shape(cx, by, w=40, h=64, fill=NAT, stroke=NAIL_S, sw=1.6, extra='', clip_id=None):
    """Unghia/tip isolato visto dall'alto (punta in alto). by = base (cuticola)."""
    hw = w / 2
    d = ('M%.1f,%.1f L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z'
         % (cx - hw, by - 6, cx - hw, by - h + hw * 0.9, cx - hw, by - h + 2, cx - hw * 0.4, by - h, cx, by - h,
            cx + hw * 0.4, by - h, cx + hw, by - h + 2, cx + hw, by - h + hw * 0.9, cx + hw, by - 6, cx, by + 8, cx - hw, by - 6))
    d = ('M%.1f,%.1f L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z'
         % (cx - hw, by - 6, cx - hw, by - h + hw, cx - hw, by - h + hw * 0.2, cx - hw * 0.55, by - h, cx, by - h,
            cx + hw * 0.55, by - h, cx + hw, by - h + hw * 0.2, cx + hw, by - h + hw, cx + hw, by - 6, cx, by + 6, cx - hw, by - 6))
    s = ''
    cid = clip_id or uid('ns')
    s += '<defs><clipPath id="%s"><path d="%s"/></clipPath></defs>' % (cid, d)
    s += '<path d="%s" fill="%s"/>' % (d, fill)
    s += extra.replace('CLIP', cid)
    s += '<path d="%s" fill="none" stroke="%s" stroke-width="%s"/>' % (d, stroke, sw)
    return s


def gloss(cx, by, h, k=1.0):
    return P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - 8 * k, by - h * 0.25, cx - 11 * k, by - h * 0.55, cx - 5 * k, by - h * 0.8),
             'none', '#fff', 3.5 * k, ' opacity=".75"')


def color_wheel(cx, cy, r, hl=(), n=12, inner=0.45):
    hues = ['#e53935', '#f4511e', '#fb8c00', '#fbc02d', '#c0ca33', '#7cb342', '#43a047', '#26a69a', '#1e88e5', '#3949ab', '#8e24aa', '#d81b60']
    s = ''
    for k, c in enumerate(hues):
        a0, a1 = math.radians(-90 + k * 30 - 15), math.radians(-90 + k * 30 + 15)
        ri = r * inner
        d = 'M%.1f,%.1f L%.1f,%.1f A%.1f,%.1f 0 0 1 %.1f,%.1f L%.1f,%.1f A%.1f,%.1f 0 0 0 %.1f,%.1f Z' % (
            cx + ri * math.cos(a0), cy + ri * math.sin(a0), cx + r * math.cos(a0), cy + r * math.sin(a0), r, r,
            cx + r * math.cos(a1), cy + r * math.sin(a1), cx + ri * math.cos(a1), cy + ri * math.sin(a1), ri, ri,
            cx + ri * math.cos(a0), cy + ri * math.sin(a0))
        on = (k in hl) or not hl
        s += '<path d="%s" fill="%s" opacity="%s" stroke="#fff" stroke-width="1.5"/>' % (d, c, 1 if on else 0.22)
    for k in hl:
        a = math.radians(-90 + k * 30)
        s += circ(cx + r * 1.12 * math.cos(a), cy + r * 1.12 * math.sin(a), 3.2, INK, 'none', 0)
    return s


def hand_back(cx, by, s=1.0, skin=SKIN, nails=None, spread=1.0):
    """Mano vista dal dorso, dita in alto: dita affusolate con nocche, pollice divaricato. by = polso.
    nails = lista di 5 colori (pollice→mignolo) o None."""
    nails = nails or [NAT] * 5
    edge = SKIN_D if skin == SKIN else dark(skin, .22)
    # (x base, y base, lunghezza, largh. base, largh. punta, angolo)
    fingers = [(-44, -52, 60, 25, 21, -50), (-31, -98, 76, 22, 18.5, -9), (-9, -104, 86, 23, 19.5, -2), (14, -100, 78, 22, 18.5, 6), (34, -90, 60, 19, 16, 15)]
    palm = 'M-40,0 C-44,-30 -50,-70 -46,-96 Q-30,-114 -8,-116 Q20,-116 44,-102 C50,-70 46,-30 40,0 Z'
    shapes = []
    for k, (x, y, L, wb, wt, ang) in enumerate(fingers):
        ang *= spread
        d = 'M%.1f,14 L%.1f,%.1f A%.1f,%.1f 0 0 1 %.1f,%.1f L%.1f,14 Z' % (-wb / 2, -wt / 2, -L + wt / 2, wt / 2, wt / 2, wt / 2, -L + wt / 2, wb / 2)
        shapes.append((x, y, ang, d, L, wt))
    out = ''
    for x, y, ang, d, L, wt in shapes:
        out += '<path d="%s" transform="translate(%.1f,%.1f) rotate(%.1f)" fill="%s" stroke="%s" stroke-width="2.8"/>' % (d, x, y, ang, skin, edge)
    out += '<path d="%s" fill="%s" stroke="%s" stroke-width="2.8"/>' % (palm, skin, edge)
    for x, y, ang, d, L, wt in shapes:
        out += '<path d="%s" transform="translate(%.1f,%.1f) rotate(%.1f)" fill="%s"/>' % (d, x, y, ang, skin)
    out += '<path d="%s" fill="%s"/>' % (palm, skin)
    for k, (x, y, ang, d, L, wt) in enumerate(shapes):
        det = ''
        for f in ((0.36, 0.62) if k else (0.45,)):
            det += P('M%.1f,%.1f Q0,%.1f %.1f,%.1f' % (-wt * 0.32, -L * f, -L * f + 2.5, wt * 0.32, -L * f), 'none', edge, 0.9, ' opacity=".55"')
        det += nail_shape(0, -L + wt * 1.2, wt * 0.64, wt * 0.98, nails[k], NAIL_S, 1)
        det += rbox(-wt * 0.2, -L + wt * 0.42, wt * 0.09, wt * 0.55, '#fff', 'none', 0, 1, ' opacity=".55"')
        out += '<g transform="translate(%.1f,%.1f) rotate(%.1f)">%s</g>' % (x, y, ang, det)
    # nocche e tendini
    for x in (-30, -8, 15, 35):
        out += P('M%.1f,%.1f q5,-3 10,0' % (x - 5, -100 + abs(x) * 0.12), 'none', edge, 1, ' opacity=".5"')
    out += P('M-24,-90 L-18,-30 M-4,-96 L-2,-30 M14,-92 L10,-30', 'none', '#fff', 2.2, ' opacity=".22"')
    return g(out, cx, by, 0, s)

@figx('cover-step.svg')
def cover_step():
    labels = ['Allunga', 'Scegli la lunghezza', 'Cover, 2 strati sottili', 'Controlla controluce', 'Smile line', 'Builder e top']
    subs = ['tip o cartina', 'proporzionata al dito', 'fino alla nuova linea', 'nessuna "finestra" chiara', 'centro, poi i due angoli',
            'struttura, lima, top']
    NB, CV, FR = 48, 30, 30

    def d(i):
        cx, yb = 128, 226
        s = ''
        if i in (0, 1, 2, 4):
            s += form_top(cx, yb - NB, 72, 120)
        if i == 0:
            f, p = ext_nail(cx, yb, hw=32, nat=NB, free=0)
            s += f
        elif i == 1:
            f, p = ext_nail(cx, yb, hw=32, nat=NB, free=0)
            s += f
            s += dashed(cx - 64, yb - NB - CV, cx + 64, yb - NB - CV, ERR, 2.2, '6 4')
            s += text(cx + 74, yb - NB - CV - 2, 'nuovo letto', 13, 'start', 800, ERR)
            s += text(cx + 74, yb - NB - CV + 15, '+2–3 mm', 12.5, 'start', 700, MUTED)
            s += arrow(cx + 52, yb - NB - 2, cx + 52, yb - NB - CV + 4, ACC2, 2)
        elif i == 2:
            f, p = ext_nail(cx, yb, hw=32, nat=NB, cov=CV)
            s += f
            s += circ(cx + 92, yb - NB - 12, 17, ACC, 'none', 0) + text(cx + 92, yb - NB - 7, '×2', 14, weight=800, fill='#fff')
        elif i == 3:
            for a in range(-60, 241, 30):
                r = math.radians(a)
                s += ln(cx + 60 * math.cos(r), yb - 110 + 60 * math.sin(r), cx + 92 * math.cos(r), yb - 110 + 92 * math.sin(r), '#f5c542', 3, ' opacity=".7"')
            s += circ(cx, yb - 110, 52, '#fff7cf', 'none', 0)
            f, p = ext_nail(cx, yb, hw=32, nat=NB, cov=CV, free=FR, show_nat=False)
            s += f
            s += mark(cx + 92, yb - 150, True, 13)
        elif i == 4:
            f, p = ext_nail(cx, yb, hw=32, nat=NB, cov=CV, free=FR, smile=10, show_nat=False)
            s += f
            ys = yb - NB - CV
            for (dx, dy) in [(0, 0), (-30, 10), (30, 10)]:
                s += circ(cx + dx, ys + dy, 4.5, ACC2, '#fff', 1.5)
            s += text(cx + 84, ys + 4, '1° centro,', 12.5, 'start', 700, ACC2)
            s += text(cx + 84, ys + 22, 'poi angoli', 12.5, 'start', 700, ACC2)
        else:
            f, p = ext_nail(cx - 20, yb, hw=32, nat=NB, cov=CV, free=FR, smile=10, show_nat=False)
            s += f + gloss(cx - 20, yb - 10, 90)
            sp, pp = side_profile(cx + 50, yb - 70, w=100, stress=0.6, apex=0.45, apex_h=14, tip_h=4, root_h=2, gap=4, product='#f2c6d2', finger=False)
            s += sp + circ(pp['ax'], pp['ah'], 3.5, ACC2, 'none', 0)
            s += text(cx + 100, yb - 104, 'apex', 12.5, 'middle', 700, ACC2)
        return s
    pw, ph = 300, 262
    W = 3 * pw + 2 * 14 + 40
    b = T('French con letto allungato: 6 passaggi')
    b += text(W - 20, 38, '- - -  fine del letto naturale', 13, 'end', 700, ACC2)
    for i, lab in enumerate(labels):
        x = 20 + (i % 3) * (pw + 14)
        y = 60 + (i // 3) * (ph + 14)
        b += frame(x, y, pw, ph, lab, i + 1, body=g(d(i), x, y), sub=subs[i], subcol=MUTED)
    return svg(W, 60 + 2 * (ph + 14) + 6, arrow_defs() + b, 'French con letto allungato in cover: sei passaggi')


def french_nail(cx, by, w=70, h=150, cov_top=0.62, sc=10, sw=10, win=False, ears=False, cov_col=COV):
    """Unghia allungata con cover e bianco. cov_top = frazione di h dove finisce il cover (al centro).
    sc / sw = profondità della curva del cover e del bianco ai lati."""
    ys = by - h * cov_top
    hw = w / 2
    ext = ''
    if cov_col:
        ext += '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s" clip-path="url(#CLIP)"/>' % (
            cx - hw - 4, by + 10, cx - hw - 4, ys + sc, cx, ys - sc, cx + hw + 4, ys + sc, cx + hw + 4, by + 10, cov_col)
    if sw is not None:
        ext += '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="#ffffff" clip-path="url(#CLIP)"/>' % (
            cx - hw - 4, by - h - 10, cx - hw - 4, ys + sw, cx, ys - sw, cx + hw + 4, ys + sw, cx + hw + 4, by - h - 10)
    if win:
        for (dx, dy, rx, ry) in [(-12, -0.35, 9, 13), (10, -0.5, 7, 10)]:
            ext += '<ellipse cx="%.1f" cy="%.1f" rx="%d" ry="%d" fill="#fff3b8" clip-path="url(#CLIP)"/>' % (cx + dx, by + h * dy, rx, ry)
    if sw is not None:
        ext += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="#d9c9cd" stroke-width="1.2" clip-path="url(#CLIP)"/>' % (
            cx - hw - 4, ys + sw, cx, ys - sw, cx + hw + 4, ys + sw)
    s = nail_shape(cx, by, w, h, '#fff3b8', NAIL_S, 1.8, ext)
    return s, ys


@figx('cover-controluce.svg')
def cover_controluce():
    W, H = 820, 380
    b = T('Prova controluce')

    def rays(cx, cy):
        s = ''
        for a in range(0, 360, 24):
            r = math.radians(a)
            s += ln(cx + 54 * math.cos(r), cy + 54 * math.sin(r), cx + 84 * math.cos(r), cy + 84 * math.sin(r), '#f5c542', 3, ' opacity=".75"')
        return s + circ(cx, cy, 60, '#fff7cf', 'none', 0)
    items = [(True, 'coprente, uniforme', OK), (False, 'finestre: aggiungi un velo', ERR), (False, '"orecchie" trasparenti', ERR)]
    for k, (ok, lab, col) in enumerate(items):
        x = 20 + k * 266
        body = ''
        cx, by = x + 125, 290
        if k < 2:
            body += rays(cx, 205)
            n, ys = french_nail(cx, by, 74, 170, cov_top=1.1, sc=6, sw=None, win=(k == 1))
            body += n
            if k == 1:
                body += circ(cx - 12, by - 170 * 0.35, 18, 'none', ERR, 2.2) + circ(cx + 10, by - 85, 14, 'none', ERR, 2.2)
            b += frame(x, 58, 250, 270, None, None, ok, body, sub=lab, subcol=col)
        else:
            by = 258
            n, ys = french_nail(cx - 40, by, 64, 150, cov_top=0.6, sc=14, sw=2)
            body += n
            for sx in (-1, 1):
                body += circ(cx - 40 + sx * 26, ys + 9, 11, 'none', ERR, 2.2)
            body += mark(cx - 40, 92, False, 12)
            n2, ys2 = french_nail(cx + 62, by, 64, 150, cov_top=0.6, sc=14, sw=14)
            body += n2 + mark(cx + 62, 92, True, 12)
            body += text(cx + 62, by + 24, 'angoli un po\'', 12.5, weight=700, fill=OK)
            body += text(cx + 62, by + 38, 'più bassi', 12.5, weight=700, fill=OK)
            body += text(cx - 40, by + 24, 'angoli', 12.5, weight=700, fill=ERR)
            body += text(cx - 40, by + 38, 'troppo alti', 12.5, weight=700, fill=ERR)
            b += frame(x, 58, 250, 270, None, None, None, body)
    b += strip(20, 338, 780, 32, 'Davanti a una luce, le zone dove il cover manca diventano chiare (in giallo): lì aggiungi un velo.', 'info', 13.5)
    return svg(W, H, b, 'Prova controluce del cover: uniforme, con finestre trasparenti, con orecchie trasparenti ai lati della smile line')


@figx('cover-sezione.svg')
def cover_sezione():
    W, H = 780, 340
    b = T('L\'unghia in sezione')
    x0, x1, oy = 70, 470, 200      # x0 = cuticola, x1 = punta
    xn = 230                      # fine del letto naturale
    xsm = 360                     # smile line
    TB, TC = 5, 12                # spessore base e cover

    def tb(x):
        t = (x - x0) / (x1 - x0)
        if t < 0.9:
            return 5 + 40 * math.sin(math.pi * t / 0.9) ** 1.3
        return 5 + (1 - t) * 30

    b += P('M20,%.1f L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L20,%.1f Z' % (oy - 14, xn - 30, oy + 2, xn + 26, oy + 2, xn + 34, oy + 70, xn - 30, oy + 74, oy + 74),
           SKIN, SKIN_D, 1.5)
    b += rbox(x0 - 4, oy, xn - x0 + 8, 9, NAT, NAIL_S, 1.2, 3)
    b += P('M20,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L20,%.1f Z' % (oy - 14, x0 - 14, oy - 14, x0 - 2, oy - 14, x0 + 2, oy - 2, x0 + 2, oy + 4, oy + 4), SKIN, 'none', 0)
    b += ln(xn + 4, oy + 9, x1 + 24, oy + 9, FORM_S, 5)
    yb = oy
    b += rbox(x0 + 6, yb - TB, x1 - x0 - 6, TB, '#bcd3de', '#8fb0c2', 0.8, 1)
    yc = yb - TB
    b += rbox(x0 + 8, yc - TC, xsm - x0 - 8, TC, COV, COV_S, 1, 2)
    b += P('M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (xsm, yc - TC, x1, yc - TC + 2, x1, yc, xsm, yc), '#ffffff', '#b9a8ad', 1)
    yt = yc - TC
    pts = ['%.1f,%.1f' % (x, yt - tb(x)) for x in range(x0 + 10, x1 + 1, 5)]
    b += P('M%.1f,%.1f L%s L%.1f,%.1f Z' % (x0 + 10, yt, ' L'.join(pts), x1, yt + 2), CLEAR, CLEAR_S, 1.2)
    pts2 = ['%.1f,%.1f' % (x, yt - tb(x) - 2) for x in range(x0 + 10, x1 + 1, 5)]
    b += P('M' + ' L'.join(pts2), 'none', '#4a98c9', 3.5)
    ax = x0 + (x1 - x0) * 0.45
    b += circ(ax, yt - tb(ax) - 2, 4, ACC2, 'none', 0) + text(ax, yt - tb(ax) - 12, 'apex', 13, weight=800, fill=ACC2)
    lx = 548
    lab = [(450, yt - tb(450) - 2, 'top (sottile, lucido)', 92),
           (430, yt - tb(430) / 2, 'builder trasparente + apex', 124),
           (440, yc - TC / 2, 'bianco (smile line)', 156),
           (340, yc - TC / 2, 'cover (fino alla smile line)', 188),
           (455, yb - TB / 2, 'base (sottile)', 220),
           (200, yb + 5, 'lamina naturale', 252),
           (480, yb + 9, 'cartina (si toglie)', 284)]
    for (px, py, t, ly) in lab:
        b += leader(px, py, lx, ly, t, 'start', 13.5)
    b += dashed(xn, oy + 12, xn, 300, MUTED, 1.2, '3 3') + dashed(xsm, yc, xsm, 326, ACC2, 1.2, '3 3')
    b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2" marker-start="url(#arw)" marker-end="url(#arw)"/>' % (x0, 296, xn, 296, MUTED)
    b += text((x0 + xn) / 2, 290, 'letto naturale', 13, weight=700, fill=MUTED)
    b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2" marker-start="url(#ar)" marker-end="url(#ar)"/>' % (x0, 324, xsm, 324, ACC2)
    b += text((x0 + xsm) / 2, 318, 'letto ottico (con il cover)', 13, weight=800, fill=ACC2)
    return svg(W, H, arrow_defs() + b, 'L\'unghia con letto allungato in sezione: lamina, base, cover, bianco, builder trasparente con apex, top')


@figx('colori-proprieta.svg')
def col_prop():
    W, H = 860, 330
    b = T('Tinta, luminosità, saturazione')
    rows = [('Tinta', 'il "nome" del colore', ['#e53935', '#fb8c00', '#fdd835', '#43a047', '#1e88e5', '#8e24aa'], None),
            ('Luminosità', 'chiaro o scuro', ['#fbe4ea', '#f4b6c8', '#e57b9b', '#c2406a', '#8e1f45', '#561127'], 'chiaro → scuro'),
            ('Saturazione', 'spento o intenso', ['#b9a9ad', '#c39aa6', '#cc8aa0', '#d8709a', '#e45493', '#f0258c'], 'spento → intenso')]
    for k, (t, sub, cols, arr) in enumerate(rows):
        y = 64 + k * 88
        b += rbox(20, y, 820, 76)
        b += text(40, y + 34, t, 17, 'start', 800)
        b += text(40, y + 56, sub, 13, 'start', 600, MUTED)
        for j, c in enumerate(cols):
            b += rbox(220 + j * 72, y + 12, 58, 52, c, '#fff', 2, 10)
        if arr:
            b += arrow(670, y + 40, 820, y + 40, ACC2, 2)
            b += text(745, y + 30, arr, 13, weight=700, fill=ACC2)
        else:
            b += text(745, y + 44, 'cambia il colore', 13, weight=700, fill=ACC2)
    return svg(W, H, arrow_defs() + b, 'Le tre proprietà del colore: tinta, luminosità e saturazione')


def wrist(cx, cy, vein, s=1.0, skin=SKIN):
    """Interno del polso e avambraccio con vene. vein: colore (o tupla per vene miste)."""
    arm = 'M-38,72 C-42,30 -44,-20 -38,-60 Q-36,-74 -26,-78 Q0,-84 26,-78 Q36,-74 38,-60 C44,-20 42,30 38,72 Z'
    b = '<path d="%s" fill="%s" stroke="%s" stroke-width="1.4"/>' % (arm, skin, SKIN_D)
    b += P('M-34,-52 Q0,-60 34,-52', 'none', SKIN_D, 1.1, ' opacity=".6"') + P('M-32,-42 Q0,-48 32,-42', 'none', SKIN_D, 1, ' opacity=".45"')
    vs = vein if isinstance(vein, tuple) else (vein, vein, vein)
    paths = ['M-18,70 Q-24,24 -14,-6 Q-6,-30 -12,-38', 'M4,70 Q10,26 2,-4 Q-4,-26 6,-36', 'M22,66 Q16,30 22,0', 'M-14,20 Q-4,8 2,-2']
    for k, d in enumerate(paths):
        c = vs[min(k, 2)] if k < 3 else vs[0]
        b += P(d, 'none', c, 4.2, ' opacity=".35"') + P(d, 'none', c, 2.2, ' opacity=".9"')
    b += P('M-26,60 C-30,20 -30,-20 -24,-50', 'none', '#fff', 5, ' opacity=".22"')
    return g(b, cx, cy, 0, s)

@figx('sottotono-test.svg')
def sottotono():
    W, H = 900, 380
    b = T('Capire il sottotono: tre test')
    b += sun(860, 30, 11) + text(834, 36, 'luce naturale', 14, 'end', 700, '#9a6a00')
    pw = 280
    # 1 vene
    x = 20
    body = wrist(x + 80, 168, '#5b7fc7', 0.62)
    body += text(x + 150, 140, 'guarda l\'interno', 13, 'start', 600, MUTED)
    body += text(x + 150, 158, 'del polso', 13, 'start', 600, MUTED)
    for k, (v, t) in enumerate([('#4f6fcf', 'freddo'), ('#4f9a5a', 'caldo'), (('#4f6fcf', '#4f9a5a', '#6f7fa0'), 'neutro')]):
        cx = x + 60 + k * 82
        body += wrist(cx, 262, v, 0.38)
        body += text(cx, 306, t, 13, weight=700)
    b += frame(x, 58, pw, 270, 'Vene del polso', 1, body=body)
    # 2 foglio bianco
    x = 20 + pw + 10
    body = ''
    for k, (halo, t, sk) in enumerate([('#f6b8c6', 'freddo: rosata', '#f1c4c0'), ('#f3d27a', 'caldo: dorata', '#efcda0')]):
        cx = x + 72 + k * 136
        body += rbox(cx - 58, 112, 116, 168, '#ffffff', '#d9d0cd', 1.5, 4)
        body += '<ellipse cx="%.1f" cy="%.1f" rx="52" ry="70" fill="%s" opacity=".45"/>' % (cx, 200, halo)
        body += hand_back(cx, 270, 0.62, sk)
        body += text(cx, 302, t, 13, weight=700)
    b += frame(x, 58, pw, 270, 'Foglio bianco', 2, body=body)
    # 3 gioielli
    x = 20 + 2 * (pw + 10)
    body = ''
    for k, (c1, c2, t, t2) in enumerate([('#d9dde3', '#8c96a3', 'argento', 'freddo'), ('#f3d27a', '#b88a1b', 'oro', 'caldo')]):
        cx = x + 76 + k * 128
        body += '<ellipse cx="%.1f" cy="%.1f" rx="38" ry="38" fill="none" stroke="%s" stroke-width="12"/>' % (cx, 190, c2)
        body += '<ellipse cx="%.1f" cy="%.1f" rx="38" ry="38" fill="none" stroke="%s" stroke-width="8"/>' % (cx, 190, c1)
        body += P('M%.1f,%.1f q8,-6 16,-2' % (cx - 22, 162), 'none', '#fff', 3)
        body += text(cx, 256, t, 14, weight=800)
        body += text(cx, 276, 'sta bene? → ' + t2, 12.5, weight=600, fill=MUTED)
    body += text(x + pw / 2, 306, 'entrambi? → neutro', 13, weight=700)
    b += frame(x, 58, pw, 270, 'Gioielli', 3, body=body)
    b += strip(20, 338, 860, 32, 'Indicazioni, non misure: conferma sempre con la prova del tip', 'warn', 14)
    return svg(W, H, b, 'Tre test pratici per capire il sottotono: vene del polso, foglio bianco, gioielli')


@figx('nude-prova-tip.svg')
def nude_tip():
    W, H = 840, 360
    b = T('La prova del tip')
    tips = [('#f3b8c8', 'troppo rosa'), ('#efcf9c', 'troppo giallo'), ('#e9b9b0', 'sparisce: è lui')]
    bed = '#ecbcb3'
    body = window_icon(36, 76, 90, 110) + text(81, 206, 'finestra', 12.5, weight=600, fill=MUTED)
    body += sun(81, 240, 9)
    body += hand_back(236, 350, 1.0, SKIN, [bed] * 5, 1.0)
    for k, (c, t) in enumerate(tips):
        ang = (k - 1) * 26
        tb = nail_shape(0, 0, 22, 56, c, '#a48c86', 1.3)
        body += g(tb, 236 + (k - 1) * 12, 164, ang)
        lx = 236 + (k - 1) * 62
        body += circ(lx, 92, 11, ACC, 'none', 0) + text(lx, 97, str(k + 1), 13, weight=800, fill='#fff')
        body += dashed(lx, 104, 236 + (k - 1) * 30, 116, MUTED, 1, '2 3')
    b += frame(20, 58, 360, 250, body=body)
    for k, (c, t) in enumerate(tips):
        x = 392 + k * 146
        ok = k == 2
        cx = x + 68
        body = nail_shape(cx, 238, 52, 120, bed, NAIL_S, 1.6,
                          '<rect x="%.1f" y="%.1f" width="70" height="70" fill="%s" clip-path="url(#CLIP)"/>' % (cx - 35, 238 - 120 - 4, c))
        if not ok:
            body += dashed(cx - 30, 238 - 54, cx + 30, 238 - 54, ERR, 2)
        b += frame(x, 58, 136, 250, None, None, None, body)
        b += circ(x + 22, 82, 12, ACC, 'none', 0) + text(x + 22, 87, str(k + 1), 13, weight=800, fill='#fff')
        b += mark(x + 114, 82, ok, 12)
        b += ftext(cx, 278, 'stacca:' if not ok else 'sparisce:', 13, 124, weight=800, fill=OK if ok else ERR)
        b += ftext(cx, 296, t.replace('sparisce: ', ''), 13, 124, weight=700, fill=OK if ok else ERR)
    b += strip(20, 318, 800, 32, 'Confronta con il letto ungueale, non con il dorso della mano', 'info', 14)
    return svg(W, H, b, 'La prova del tip: campioni di cover appoggiati all\'unghia alla luce naturale')


@figx('pigmenti-luce.svg')
def pigmenti():
    W, H = 860, 390
    b = T('Pigmenti e luce: l\'effetto ombrello')
    # lampada vista di fronte con barra LED
    b += '<ellipse cx="430" cy="138" rx="160" ry="8" fill="#000" opacity=".1" filter="url(#dxBlurS)"/>'
    b += P('M270,132 L270,104 C270,70 330,56 430,56 C530,56 590,70 590,104 L590,132 Z', '#f7f5fa', '#8a7d9e', 2)
    b += P('M286,74 C320,64 380,62 430,62', 'none', '#fff', 4, ' opacity=".9"')
    b += rbox(300, 120, 260, 12, '#3a3046', 'none', 0, 4)
    for j in range(12):
        b += circ(312 + j * 21.8, 126, 3.2, '#c9a8ff', 'none', 0) + circ(312 + j * 21.8, 126, 6, '#9a6be0', 'none', 0, ' opacity=".35"')
    b += rbox(262, 132, 336, 8, '#8a7d9e', 'none', 0, 3)
    items = [('Sottile, chiaro', '#f7d3dc', 1.0, 30, False, True, 'indurito fino in fondo'),
             ('Sottile, scuro', '#a3263f', 0.9, 30, False, True, 'ok con tempi da scheda'),
             ('Spesso, scuro', '#a3263f', 0.45, 78, True, False, 'sotto: non polimerizzato')]
    for k, (t, col, pen, th, soft, ok, sub) in enumerate(items):
        x = 40 + k * 270
        cx = x + 110
        base = 306
        # alone di luce che entra
        gid = uid('uvb')
        b += '<defs>%s</defs>' % _lg(gid, [(0, UV, .0), (.5, UV, .16), (1, UV, .3)], 0, 1)
        b += '<rect x="%d" y="150" width="180" height="%d" fill="url(#%s)"/>' % (x + 20, base - th - 150, gid)
        b += rbox(x, base, 220, 12, NAT, NAIL_S, 1.2, 3)
        lid = uid('lay')
        b += '<defs>%s</defs>' % _lg(lid, [(0, light(col, .15)), (1, dark(col, .15))], 0, 1)
        b += rbox(x + 20, base - th, 180, th, 'url(#%s)' % lid, dark(col, .4), 1.2, 4)
        b += rbox(x + 24, base - th + 2, 172, 4, '#fff', 'none', 0, 2, ' opacity=".45"')
        if soft:
            pid = uid('hatch')
            b += ('<defs><pattern id="%s" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
                  '<rect width="10" height="10" fill="#f6c58f"/><line x1="0" y1="0" x2="0" y2="10" stroke="#e08a2c" stroke-width="4"/></pattern></defs>') % pid
            b += '<rect x="%d" y="%d" width="180" height="%d" fill="url(#%s)"/>' % (x + 20, base - th / 2, th / 2, pid)
            b += rbox(x + 20, base - th, 180, th, 'none', dark(col, .4), 1.2, 4)
            b += text(x + 110, base - th / 4 + 5, 'molle', 12.5, weight=800, fill='#8a4a10')
            for j in range(5):
                ux, uy = x + 40 + j * 35, base - th + 12
                b += P('M%.1f,%.1f a9,7 0 0 1 18,0 Z' % (ux - 9, uy), '#2b1d22', 'none', 0) + ln(ux, uy, ux, uy + 9, '#2b1d22', 1.5)
        else:
            for j in range(10):
                b += circ(x + 32 + j * 17, base - th / 2 + (j % 2) * 6 - 3, 2.2, '#fff' if k == 0 else '#5c0f22', 'none', 0, ' opacity=".7"')
        for j in range(4):
            ax = x + 50 + j * 40
            y_end = base - th + th * pen - 4 if k < 2 else base - th + th * pen
            b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="3" stroke-linecap="round" marker-end="url(#uvm)"/>' % (ax, 152, ax, y_end, UV)
        b += mark(x + 200, base - th - 18, ok, 12)
        b += text(cx, base + 38, t, 15, weight=800)
        b += text(cx, base + 58, sub, 13, weight=700, fill=OK if ok else ERR)
    defs = ('<defs><marker id="uvm" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">'
            '<path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>') % UV
    b += rbox(640, 18, 200, 30, YEL_BG, YEL, 1.2, 12) + text(740, 38, 'Rossi e neri assorbono più luce', 12.5, weight=700, fill='#7a5a12')
    return svg(W, H, arrow_defs() + defs + b, 'Effetto ombrello dei pigmenti: in uno strato sottile la luce arriva in fondo, in uno spesso e pigmentato no')

@figx('colore-strati-step.svg')
def colore_strati():
    labels = ['Mescola', 'Base + lampada', '1° strato sottile', 'Sigilla la punta', '2° strato + top']
    subs = ['rotola, non agitare', 'sottile, poi lampada', 'striato? è normale', 'passa sullo spessore', 'colore pieno e lucido']
    pw, ph = 176, 286
    W = 20 + 5 * pw + 4 * 12 + 20
    b = T('Colore in gel: strati sottili')
    RED = '#c62f4a'
    for i, lab in enumerate(labels):
        x = 20 + i * (pw + 12)
        cx, by = x + pw / 2, 58 + 222
        s = ''
        if i == 0:
            s += rbox(cx - 18, 150, 36, 62, RED, '#7a1a2b', 2, 8) + rbox(cx - 9, 132, 18, 20, '#3b2a30', 'none', 0, 3)
            s += curved_arrow(cx - 50, 232, cx + 50, 232, 22) + curved_arrow(cx + 50, 128, cx - 50, 128, 22)
        elif i == 1:
            s += nail_shape(cx - 10, by, 56, 116, '#f6dbe2', NAIL_S, 1.6) + gloss(cx - 10, by, 116, 0.8)
            s += mini_lamp(cx + 50, 138, 0.42)
        elif i == 2:
            ext = ''.join('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#ef8a9d" stroke-width="3" clip-path="url(#CLIP)"/>' % (
                cx - 18 + j * 9, by - 12, cx - 20 + j * 9, by - 104) for j in range(5))
            s += nail_shape(cx, by, 58, 116, NAT, NAIL_S, 1.6)
            s += nail_shape(cx, by - 8, 48, 104, '#d9566d', '#d9566d', 0.1, ext)
            s += leader(cx, by - 4, cx + 52, by - 36, '', 'start', 12)
            s += text(cx + 50, by - 54, 'piccolo', 12, 'middle', 700, ACC2)
            s += text(cx + 50, by - 40, 'margine', 12, 'middle', 700, ACC2)
        elif i == 3:
            yy = 210
            s += P('M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z' % (
                cx - 80, yy, cx + 30, yy, cx + 46, yy, cx + 47, yy + 10, cx + 46, yy + 20, cx + 30, yy + 20, cx - 80, yy + 20), NAT, NAIL_S, 1.6)
            s += P('M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (
                cx - 80, yy - 5, cx + 32, yy - 5, cx + 52, yy - 4, cx + 52, yy + 10, cx + 52, yy + 22, cx + 36, yy + 23), 'none', RED, 6)
            s += tool_brush(cx + 62, yy - 30, -125, 80, RED)
            s += text(cx - 30, yy + 50, 'bordo libero', 12, 'middle', 600, MUTED)
            s += text(cx - 30, yy + 64, 'di profilo', 12, 'middle', 600, MUTED)
        else:
            s += nail_shape(cx - 10, by, 58, 116, NAT, NAIL_S, 1.6)
            s += nail_shape(cx - 10, by - 8, 48, 104, RED, '#7a1a2b', 1) + gloss(cx - 10, by - 6, 104, 0.8)
            s += mini_lamp(cx + 50, 138, 0.42)
        b += frame(x, 58, pw, ph, lab, i + 1, body=s, tsize=14, sub=subs[i], subcol=OK if i == 4 else MUTED)
        if i < 4:
            b += arrow(x + pw + 1, 58 + ph / 2, x + pw + 11, 58 + ph / 2, MUTED, 2)
    return svg(W, 58 + ph + 20, arrow_defs() + b, 'Stendere il colore in gel: mescola, base, primo strato sottile, sigilla la punta, secondo strato e top')


@figx('colori-finiture.svg')
def finiture():
    W, H = 860, 300
    b = T('Le finiture')
    names = ['coprente', 'jelly', 'shimmer', 'glitter', 'magnetico']
    subs = ['copre in 1–2 strati', 'traslucido', 'perlato fine', 'particelle grandi', 'cat-eye']
    nw, nh = 66, 136
    for k, n in enumerate(names):
        x = 20 + k * 166
        cx, by = x + 78, 222
        b += rbox(x, 58, 156, 228)
        s = '<ellipse cx="%.1f" cy="%.1f" rx="32" ry="5" fill="#000" opacity=".12" filter="url(#dxBlurS)"/>' % (cx, by + 6)
        if k == 0:
            s += gel(cx, by, nw, nh, '#c62f4a', '#7a1a2b', k=1.1)
        elif k == 1:
            # lamina naturale con bordo libero visibile attraverso il colore traslucido
            fx = '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="#fff" clip-path="url(#CLIP)"/>' % (
                cx - 40, by - 88, cx, by - 112, cx + 40, by - 88, cx + 40, by - 150, cx - 40, by - 150)
            fx += '<rect x="%.1f" y="%.1f" width="80" height="150" fill="#d42c4c" opacity=".5" clip-path="url(#CLIP)"/>' % (cx - 40, by - 146)
            s += gel(cx, by, nw, nh, '#f3c3cc', '#a8324b', fx=fx, k=1.1)
        elif k == 2:
            s += gel(cx, by, nw, nh, '#e08aa6', '#a8476a', fx=shimmer_fx(cx, by, nw, nh, '#fff0f6'), k=0.8)
        elif k == 3:
            fx = glitter_fx(cx, by, nw, nh, 26, 7) + glitter_fx(cx, by, nw, nh, 30, 11, (1, 2))
            s += gel(cx, by, nw, nh, '#f1f3f6', '#9aa3ad', fx=fx, k=0.9)
        else:
            s += gel(cx, by, nw, nh, '#1f1b29', '#000', fx=cateye_fx(cx, by, nw, nh, '45'), hi=False)
        b += s
        b += text(cx, 250, n, 15, weight=800)
        b += text(cx, 270, subs[k], 12.5, weight=600, fill=MUTED)
    return svg(W, H, b, 'Le finiture dei colori: coprente, jelly traslucido, shimmer, glitter e magnetico (cat-eye)')

@figx('cartella-colori.svg')
def cartella():
    W, H = 860, 400
    b = T('La cartella campioni')
    fam = [('nude/cover', ['#f4ddd2', '#ecc4b4', '#d9a28c', '#a8705a']),
           ('rosa', ['#fbd5df', '#f3a6bd', '#e46f93', '#b8406a']),
           ('rossi', ['#f28b82', '#e53935', '#b71c1c', '#6d1020']),
           ('viola/blu', ['#c9b6e4', '#8e6cc4', '#3f51b5', '#1a237e']),
           ('verdi', ['#c8e6c9', '#81c784', '#388e3c', '#1b4d2a']),
           ('scuri', ['#bdb6b3', '#7d716d', '#4a3f3c', '#1d1717']),
           ('effetti', ['glitter', 'chrome', 'cat', 'shimmer'])]
    b += rbox(20, 58, 700, 324)
    nw, nh = 32, 56
    for c, (name, cols) in enumerate(fam):
        x = 30 + c * 92
        cx = x + 34
        b += ftext(cx, 84, name, 13.5, 88, weight=800)
        for r, col in enumerate(cols):
            by = 156 + r * 66
            b += '<ellipse cx="%.1f" cy="%.1f" rx="14" ry="3" fill="#000" opacity=".12"/>' % (cx, by + 4)
            if col == 'glitter':
                b += gel(cx, by, nw, nh, '#f7f4ef', '#b9ab98', fx=glitter_fx(cx, by, nw, nh, 14, 3, (1.5, 3)), k=0.7)
            elif col == 'chrome':
                b += gel(cx, by, nw, nh, '#9aa1ab', '#5b626c', fx=chrome_fx(cx, by, nw, nh), k=0.8)
            elif col == 'cat':
                b += gel(cx, by, nw, nh, '#1f1b29', '#000', fx=cateye_fx(cx, by, nw, nh, '45'), hi=False)
            elif col == 'shimmer':
                b += gel(cx, by, nw, nh, '#d98aa8', '#a0506c', fx=shimmer_fx(cx, by, nw, nh), k=0.6)
            else:
                b += gel(cx, by, nw, nh, col, dark(col, .3), k=0.8)
            b += circ(cx, by - nh - 6, 2.6, '#fff', '#b9ab98', 1)  # foro dell'anello
    b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2.4" marker-end="url(#ar)"/>' % (692, 112, 692, 346, ACC2)
    b += text(692, 104, 'chiaro', 12.5, 'middle', 700, ACC2)
    b += text(692, 368, 'scuro', 12.5, 'middle', 700, ACC2)
    # retro del tip
    b += rbox(734, 58, 106, 324, '#fff', '#e5d6d2', 1.5, 14)
    b += text(787, 84, 'il retro', 14, weight=800)
    b += gel(787, 266, 72, 152, '#fbf7f2', '#b9ab98', k=0.5)
    b += mtext(787, 176, ['marca', 'nome', 'n° 112'], 14, weight=700, fill='#3a5a9a', lh=1.4)
    b += P('M762,232 q8,-4 16,0 q8,4 16,0 q6,-3 10,0', 'none', '#3a5a9a', 1.6)
    b += text(787, 306, 'scritto a', 12.5, weight=600, fill=MUTED)
    b += text(787, 322, 'pennarello', 12.5, weight=600, fill=MUTED)
    return svg(W, H, arrow_defs() + b, 'Cartella colori ordinata per famiglie, dal chiaro allo scuro, con marca, nome e numero sul retro')

@figx('armonie-colore.svg')
def armonie():
    W, H = 900, 330
    b = T('Abbinamenti facili')
    items = [('Monocromatico', [8], ['#90caf9', '#42a5f5', '#1565c0', '#42a5f5', '#90caf9'], None),
             ('Analoghi', [11, 0, 1], ['#f48fb1', '#ff8a65', '#ffb74d', '#ff8a65', '#f48fb1'], None),
             ('Complementari', [8, 2], ['#1e5bb8', '#1e5bb8', '#1e5bb8', 'acc', '#1e5bb8'], '#fb8c00'),
             ('Neutro + accento', [], ['#e9c7b8', '#e9c7b8', '#e9c7b8', 'chrome', '#e9c7b8'], None)]
    for k, (t, hl, cols, acc) in enumerate(items):
        x = 20 + k * 218
        b += rbox(x, 58, 208, 258)
        b += text(x + 104, 86, t, 15, weight=800)
        if hl:
            b += color_wheel(x + 104, 142, 40, hl)
        else:
            b += circ(x + 76, 142, 26, '#e9c7b8', '#c9a898', 1.5) + circ(x + 70, 134, 8, '#fff', 'none', 0, ' opacity=".35"')
            cid = uid('cc')
            b += '<defs><clipPath id="%s"><circle cx="%d" cy="142" r="18"/></clipPath></defs>' % (cid, x + 142)
            b += '<rect x="%d" y="124" width="36" height="36" fill="url(#dxChrome)" clip-path="url(#%s)"/>' % (x + 124, cid)
            b += circ(x + 142, 142, 18, 'none', '#6a717b', 1.5)
            b += text(x + 111, 149, '+', 20, weight=800)
            b += text(x + 104, 200, 'nude + 1 effetto', 12.5, weight=600, fill=MUTED)
        # mano stilizzata: cinque unghie su dita accennate
        for j, c in enumerate(cols):
            nx = x + 30 + j * 37
            hh = [52, 64, 70, 64, 48][j]
            by = 300 - [8, 0, -4, 0, 10][j]
            b += rbox(nx - 15, by - hh * 0.55, 30, 60, SKIN, SKIN_D, 1.2, 14)
            if c == 'acc':
                fx = '<rect x="%.1f" y="%.1f" width="40" height="22" fill="%s" clip-path="url(#CLIP)"/>' % (nx - 20, by - hh - 2, acc)
                b += gel(nx, by, 26, hh, '#1e5bb8', '#123d7a', fx=fx, k=0.8)
            elif c == 'chrome':
                b += gel(nx, by, 26, hh, '#9aa1ab', '#5b626c', fx=chrome_fx(nx, by, 26, hh), k=0.8)
            else:
                b += gel(nx, by, 26, hh, c, dark(c, .3), k=0.8)
    return svg(W, H, b, 'Abbinamenti facili per nail art: monocromatico, analoghi, complementari, neutro più accento')

def basin(cx, by, w=170, h=80, water=True, liner=False, steam=False, tilt=0, alpha=1.0):
    """Vaschetta vista di lato con bordo in prospettiva (ellisse), acqua trasparente."""
    s = ''
    rx, ry = w / 2, max(6, h * 0.14)
    top = by - h
    if liner:
        s += P('M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f' % (cx - rx - 8, top - 4, cx - rx + 12, by - 8, cx, by + 2, cx + rx - 12, by - 8, cx + rx + 8, top - 4),
               'none', '#9ccbe6', 3)
    op = ' fill-opacity="%.2f"' % (alpha if alpha < 1 else 1)
    # interno (parete posteriore)
    s += '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="#dcecf6" stroke="#7fa9c4" stroke-width="2"%s/>' % (cx, top, rx, ry, op)
    body = 'M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f A%.1f,%.1f 0 0 1 %.1f,%.1f Z' % (
        cx - rx, top, cx - rx + 14, by - 6, cx, by + 4, cx + rx - 14, by - 6, cx + rx, top, rx, ry, cx - rx, top)
    if water:
        wl = top + h * 0.28
        wrx = rx - 4
        s += '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f A%.1f,%.1f 0 0 1 %.1f,%.1f Z" fill="%s"%s/>' % (
            cx - wrx, wl, cx - rx + 16, by - 8, cx, by + 1, cx + rx - 16, by - 8, cx + wrx, wl, wrx, ry * 0.9, cx - wrx, wl, WATER, op)
        s += '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="#eef7fc" stroke="%s" stroke-width="1.4"%s/>' % (cx, wl, wrx, ry * 0.9, WATER_S, op)
        for k in range(2):
            s += P('M%.1f,%.1f q10,-5 20,0 q10,5 20,0 q10,-5 20,0' % (cx - 30, wl + h * 0.3 + k * h * 0.2), 'none', WATER_S, 1.6, ' opacity=".8"')
    s += '<path d="%s" fill="#eef6fb" fill-opacity="%.2f" stroke="#7fa9c4" stroke-width="2.2"/>' % (body, 0.35 if water else 0.9)
    s += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - rx + 10, top + 10, cx - rx + 16, by - 20, cx - rx + 26, by - 10), 'none', '#fff', 3, ' opacity=".7"')
    s += P('M%.1f,%.1f A%.1f,%.1f 0 0 0 %.1f,%.1f' % (cx - rx, top, rx, ry, cx + rx, top), 'none', '#5f8eaa', 2.6)
    if steam:
        for k in range(3):
            s += P('M%.1f,%.1f q-8,-10 0,-20 q8,-10 0,-20' % (cx - 30 + k * 30, top - 8), 'none', '#c0392b', 2.4, ' opacity=".8"')
    return s if not tilt else '<g transform="rotate(%d %.1f %.1f)">%s</g>' % (tilt, cx, by, s)

def thermometer(x, y, s=1.0, col='#e57373'):
    b = rbox(-5, -34, 10, 46, '#fff', GREY_D, 2, 5) + circ(0, 16, 9, col, GREY_D, 2) + rbox(-2, -14, 4, 28, col, 'none', 0, 2)
    for k in range(4):
        b += ln(5, -26 + k * 8, 9, -26 + k * 8, GREY_D, 1.2)
    return g(b, x, y, 0, s)


def clipper(x, y, ang=0, s=1.0):
    """Tronchesino: ganasce dritte in alto, manici sotto."""
    b = (P('M-14,-4 L14,-4 L18,6 L-18,6 Z', '#b9c1ca', GREY_D, 2)
         + P('M-16,6 Q-22,40 -12,70', 'none', GREY_D, 7) + P('M16,6 Q22,40 12,70', 'none', GREY_D, 7)
         + P('M-10,30 Q0,22 10,30', 'none', '#b9c1ca', 2.5) + ln(-14, -4, 14, -4, '#5d6670', 2.5))
    return g(b, x, y, ang, s)


def towel(x, y, s=1.0):
    b = rbox(-30, -18, 60, 36, '#cfe8f6', '#7fb4d6', 2, 6)
    for k in range(4):
        b += ln(-30, -10 + k * 7, 30, -10 + k * 7, '#a9d3ea', 1.5)
    return g(b, x, y, 0, s)


def jar(x, y, s=1.0, col='#ffffff', lid='#c2577a', label=''):
    b = rbox(-22, -18, 44, 34, col, '#b5a8a3', 2, 8) + rbox(-24, -28, 48, 12, lid, 'none', 0, 4)
    if label:
        b += text(0, 6, label, 11, weight=700, fill=MUTED)
    return g(b, x, y, 0, s)


def blade(x, y, ang=-30, s=1.0):
    b = rbox(0, -4, 60, 8, '#8a7d74', 'none', 0, 3) + P('M0,-6 L-34,-2 L-38,4 L0,6 Z', '#dfe5ea', GREY_D, 1.6)
    return g(b, x, y, ang, s)


def hourglass(x, y, s=1.0):
    b = (rbox(-18, -30, 36, 6, '#8a6d4f', 'none', 0, 2) + rbox(-18, 24, 36, 6, '#8a6d4f', 'none', 0, 2)
         + P('M-14,-24 L14,-24 L2,0 L14,24 L-14,24 L-2,0 Z', '#eef6fb', GREY_D, 2)
         + P('M-8,18 L8,18 L12,24 L-12,24 Z', '#e8b83a', 'none', 0) + P('M-9,-20 L9,-20 L2,-8 L-2,-8 Z', '#e8b83a', 'none', 0))
    return g(b, x, y, 0, s)


def stethoscope(x, y, s=1.0, col='#2c5a78'):
    b = (P('M-14,-24 L-14,-6 Q-14,14 0,14 Q14,14 14,-6 L14,-24', 'none', col, 3.5)
         + P('M0,14 L0,26 Q0,38 12,38 L18,38', 'none', col, 3.5) + circ(24, 38, 7, '#fff', col, 3.5)
         + circ(-14, -26, 3, col, 'none', 0) + circ(14, -26, 3, col, 'none', 0))
    return g(b, x, y, 0, s)


def podo_icon(x, y, s=1.0, col='#2c5a78'):
    """Impronta di piede con croce sanitaria = podologo."""
    b = P('M-8,24 C-20,22 -20,0 -14,-12 C-8,-24 8,-26 10,-12 C12,0 8,8 6,16 C4,24 0,26 -8,24 Z', '#fff', col, 2.5)
    for k, (dx, dy, r) in enumerate([(-14, -24, 4.5), (-5, -30, 3.6), (3, -30, 3.2), (10, -27, 2.8), (15, -21, 2.4)]):
        b += circ(dx, dy - 2, r, '#fff', col, 2)
    b += rbox(14, 4, 20, 20, '#d64545', 'none', 0, 4) + rbox(21.5, 7, 5, 14, '#fff', 'none', 0, 1) + rbox(17, 11.5, 14, 5, '#fff', 'none', 0, 1)
    return g(b, x, y, 0, s)


def ban(x, y, r=16):
    return circ(x, y, r, '#fff', ERR, 4) + ln(x - r * 0.7, y + r * 0.7, x + r * 0.7, y - r * 0.7, ERR, 4)


def notebook(x, y, w=80, h=64, cols=('data', 'ora', 'sigla'), rows=3):
    s = rbox(x, y, w, h, '#fff', '#b5a8a3', 2, 6) + rbox(x, y, w, 14, '#e5d6d2', 'none', 0, 6)
    cw = w / len(cols)
    for k, c in enumerate(cols):
        s += text(x + cw * (k + 0.5), y + 11, c, 9.5, weight=700, fill=INK)
        if k:
            s += ln(x + cw * k, y + 14, x + cw * k, y + h, '#d9cfc6', 1)
    for r in range(rows):
        yy = y + 14 + (r + 1) * (h - 14) / (rows + 0.2)
        s += ln(x + 4, yy, x + w - 4, yy, '#e5d6d2', 1)
    return s


@figx('piede-unghia-anatomia.svg')
def piede_anat():
    W, H = 860, 400
    b = T('L\'unghia dell\'alluce')
    # vista dall'alto: alluce + secondo dito accennato
    body = ''
    f, p = toe_top(160, 262, hw=58, nail_len=88, free=8, finger_len=60)
    body += f
    b += frame(20, 58, 400, 270, 'Vista dall\'alto', body=body)
    cx, ys, yc, yt = 160, p['y_s'], 262, p['y_t']
    lx = 262
    b += leader(cx + 62, p['yp'] + 16, lx, 104, 'polpastrello', 'start', 13.5)
    b += leader(cx + 30, yt + 3, lx, 146, 'bordo libero', 'start', 13.5)
    b += leader(cx + 10, ys + 44, lx, 188, 'lamina larga e spessa', 'start', 13.5)
    b += leader(cx + 62, ys + 56, lx, 230, 'solchi laterali profondi', 'start', 13.5)
    b += leader(cx + 34, yc + 2, lx, 272, 'cuticola', 'start', 13.5)
    b += rbox(lx + 2, 292, 150, 24, '#fff', '#ead9d5', 1, 8) + text(lx + 77, 309, 'più larga che lunga', 12.5, weight=700, fill=ACC2)
    # sezione dalla punta
    x2 = 432
    cx2, cy2 = x2 + 204, 240
    body = toe_section(cx2, cy2 - 10, 0.8)
    for sx in (-1, 1):
        body += circ(cx2 + sx * 80, cy2 - 38, 16, 'none', ERR, 2.2, ' stroke-dasharray="4 3"')
        body += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="3" marker-end="url(#arw)"/>' % (
            cx2 + sx * 170, cy2 - 62, cx2 + sx * 136, cy2 - 50, MUTED)
    for k in (-50, 0, 50):
        body += arrow(cx2 + k, 124, cx2 + k * 0.9, 150, MUTED, 2.6)
    body += text(cx2, 112, 'pressione della scarpa', 13.5, weight=700, fill=MUTED)
    body += text(cx2, 318, 'gli angoli scendono nella pelle', 13.5, weight=800, fill=ERR)
    b += frame(x2, 58, 408, 270, 'Vista dalla punta (sezione)', body=body)
    b += leader(cx2 + 40, cy2 - 58, x2 + 318, 128, 'lamina curva', 'start', 12.5)
    b += strip(20, 340, 820, 40, 'Crescita: mani ≈ 3,5 mm/mese · piedi ≈ 1,6 mm/mese (alluce rinnovato in 12–18 mesi)', 'info', 14)
    return svg(W, H, arrow_defs() + b, 'L\'unghia dell\'alluce: larga, spessa, molto curva, con pieghe laterali morbide e solchi profondi')

@figx('piede-taglio-step.svg')
def piede_taglio_step():
    labels = ['Ammorbidisci', 'Taglia dritto a piccoli colpi', 'Lima gli angoli', 'A filo del dito']
    subs = ['pediluvio tiepido, pochi minuti', 'da un lato all\'altro', 'una sola direzione', 'né più lungo né più corto']
    pw, ph = 224, 290
    W = 20 + 4 * pw + 3 * 12 + 20
    b = T('Taglio dell\'unghia del piede: 4 passaggi')
    for i, lab in enumerate(labels):
        x = 20 + i * (pw + 12)
        cx = x + pw / 2
        s = ''
        if i == 0:
            s += basin(cx - 10, 290, 184, 96, water=False)
            s += foot_side(cx - 92, 272, 0.78)
            s += basin(cx - 10, 290, 184, 96, alpha=0.5)
            s += thermometer(cx + 80, 146, 0.85)
            s += text(cx + 80, 106, 'tiepida', 13, weight=800, fill='#c0392b')
        elif i == 1:
            f, p = toe_top(cx - 8, 252, hw=46, nail_len=72, free=14, finger_len=40)
            s += f
            yt = p['y_t']
            s += dashed(cx - 66, yt + 6, cx + 50, yt + 6, OK, 2)
            for k in range(3):
                xx = cx - 44 + k * 36
                s += circ(xx, yt - 30, 10, ACC, 'none', 0) + text(xx, yt - 25.5, str(k + 1), 12, weight=800, fill='#fff')
            s += arrow(cx - 58, yt - 50, cx + 34, yt - 50, ACC2, 2)
            s += nipper(cx + 74, yt + 34, -18, 0.95)
        elif i == 2:
            f, p = toe_top(cx - 6, 252, hw=46, nail_len=72, free=6, finger_len=40)
            s += f
            ax, ay = cx + 34, p['y_t'] + 8
            s += circ(ax, ay, 15, 'none', ACC2, 2, ' stroke-dasharray="3 3"')
            s += file_pro(ax + 26, ay - 20, -52, 120, 15)
            s += arrow(ax - 2, ay + 40, ax + 30, ay + 2, ACC2, 2.4)
        else:
            ox = x - 186
            s += foot_side(ox, 230, 1.75)
            tipx = ox + 191 * 1.75
            s += dashed(tipx, 112, tipx, 262, OK, 2)
            s += text(tipx - 4, 104, 'punta del dito', 12.5, 'end', 700, OK)
            s += leader(tipx - 14, 230 - 24 * 1.75 + 4, tipx - 70, 132, 'bordo', 'end', 12.5)
            s += mark(tipx + 22, 196, True, 13)
        b += frame(x, 58, pw, ph, lab, i + 1, body=s, sub=subs[i], subcol=MUTED, tsize=14)
    return svg(W, 58 + ph + 20, arrow_defs() + b, 'Taglio dell\'unghia del piede in quattro passaggi: ammorbidisci, taglia dritto a piccoli colpi, lima gli angoli, lunghezza a filo')

@figx('scarpa-pressione.svg')
def scarpa():
    W, H = 820, 380
    b = T('La scarpa conta')
    for k, okk in enumerate([False, True]):
        x = 20 + k * 400
        cx, by = x + 190, 350
        s = ''
        if not okk:
            shoe = ('M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z' % (
                cx - 46, by, cx - 58, by - 110, cx - 44, by - 196, cx + 6, by - 238, cx + 46, by - 192, cx + 64, by - 110, cx + 50, by,
                cx + 20, by + 12, cx - 20, by + 12, cx - 46, by))
        else:
            shoe = ('M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z' % (
                cx - 54, by, cx - 66, by - 130, cx - 76, by - 226, cx + 4, by - 232, cx + 92, by - 232, cx + 84, by - 130, cx + 62, by,
                cx + 20, by + 12, cx - 20, by + 12, cx - 54, by))
        s += '<path d="%s" fill="#efe4da" stroke="none"/>' % shoe
        s += foot_top(cx, by - 12, 0.74 if okk else 0.72, 0.0 if okk else 1.0, sx=1.0 if okk else 0.84)
        # tomaia trasparente
        s += '<path d="%s" fill="#8a6d5a" fill-opacity=".08" stroke="#7a5c48" stroke-width="3.2"/>' % shoe
        s += '<path d="%s" fill="none" stroke="#fff" stroke-width="1" stroke-dasharray="3 5" opacity=".9"/>' % shoe
        if not okk:
            for sx, yy in ((-1, by - 150), (1, by - 140)):
                s += '<ellipse cx="%.1f" cy="%.1f" rx="16" ry="22" fill="%s" opacity=".45" filter="url(#dxBlur)"/>' % (cx + sx * 26, yy - 10, INFL)
            s += arrow(cx - 120, by - 166, cx - 56, by - 166, ERR, 3.2) + arrow(cx + 124, by - 156, cx + 60, by - 156, ERR, 3.2)
            s += text(cx, 96, 'punta stretta: preme sugli angoli', 14.5, weight=800, fill=ERR)
        else:
            s += text(cx, 96, 'punta ampia: spazio per le dita', 14.5, weight=800, fill=OK)
        b += frame(x, 58, 380, 310, None, None, okk, s)
    return svg(W, H, '<defs><marker id="arE" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker></defs>' % ERR
               + arrow_defs() + b.replace('stroke="%s" stroke-width="3.2" marker-end="url(#arw)"' % ERR, 'stroke="%s" stroke-width="3.2" marker-end="url(#arE)"' % ERR),
               'La scarpa conta: punta stretta che schiaccia le dita e preme sugli angoli, punta ampia con spazio per le dita')

@figx('piede-segnali-stop.svg')
def segnali_stop():
    W, H = 960, 460
    b = T('Segnali di STOP sui piedi')
    b += rbox(20, 54, 920, 34, RED_BG, ERR, 1.5, 12)
    b += text(480, 76, 'Non coprire, non limare, non diagnosticare: consiglia', 15, weight=800, fill=ERR)
    cards = [('unghia gialla, spessa', 'medico o podologo', 'both'), ('pelle squamata tra le dita', 'medico', 'med'),
             ('angolo rosso e gonfio', 'podologo', 'pod'), ('ferite, vesciche', 'niente servizio', 'ban'),
             ('escrescenza ruvida', 'medico, non limare', 'med'), ('unghia "a corno"', 'podologo', 'pod')]
    for k, (t, dest, ic) in enumerate(cards):
        x = 20 + (k % 3) * 310
        y = 98 + (k // 3) * 176
        cid = uid('sc')
        b += '<defs><clipPath id="%s"><rect x="%d" y="%d" width="300" height="166" rx="14"/></clipPath></defs>' % (cid, x, y)
        b += rbox(x, y, 300, 166, '#fff', 'none', 0, 14)
        cx, cy = x + 76, y + 92
        s = ''
        if k == 0:
            ext = ''.join(P('M%.1f,%.1f l6,-4' % (cx - 30 + j * 11, cy - 30 + (j % 3) * 14), 'none', '#a37d1c', 2) for j in range(6))
            f, p = toe_top(cx, cy + 64, hw=40, nail_len=70, free=8, plate=MYC, finger_len=24, extra=ext, shape='quadrata')
            s += f
            for j in range(5):
                s += P('M%.1f,%.1f l4,-6 l4,6' % (cx - 34 + j * 14, p['y_t']), '#fff', '#a37d1c', 1.5)
        elif k == 1:
            for sx in (-1, 1):
                s += rbox(cx + sx * 26 - 22, cy - 54, 44, 110, SKIN, SKIN_D, 1.5, 22)
            s += rbox(cx - 8, cy - 30, 16, 80, '#f19a90', 'none', 0, 6)
            for j in range(6):
                s += P('M%.1f,%.1f l6,4 l6,-4' % (cx - 9, cy - 24 + j * 12), 'none', '#fff', 1.6)
        elif k == 2:
            f, p = toe_top(cx, cy + 64, hw=40, nail_len=70, free=4, finger_len=24)
            s += f
            s += '<ellipse cx="%.1f" cy="%.1f" rx="16" ry="30" fill="%s" opacity=".75"/>' % (cx + 44, cy + 6, INFL)
            s += circ(cx + 44, cy + 6, 34, 'none', ERR, 2, ' stroke-dasharray="4 3"')
        elif k == 3:
            f, p = toe_top(cx - 6, cy + 40, hw=34, nail_len=52, free=4, finger_len=40)
            s += f
            s += '<ellipse cx="%.1f" cy="%.1f" rx="12" ry="10" fill="#fdeef0" stroke="#e57373" stroke-width="2"/>' % (cx + 18, cy + 62)
            s += '<ellipse cx="%.1f" cy="%.1f" rx="5" ry="3.5" fill="#fff" opacity=".9"/>' % (cx + 14, cy + 58)
            s += P('M%.1f,%.1f l16,-8' % (cx - 38, cy + 66), 'none', '#c0392b', 3)
        elif k == 4:
            sole = 'M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z' % (
                cx - 40, cy + 80, cx - 56, cy - 10, cx - 34, cy - 70, cx + 2, cy - 70, cx + 40, cy - 70, cx + 52, cy, cx + 36, cy + 80)
            s += '<path d="%s" fill="url(#dxSkinR)" stroke="%s" stroke-width="1.5"/>' % (sole, SKIN_D)
            for j in range(4):
                s += P('M%.1f,%.1f q30,-6 60,0' % (cx - 34, cy - 40 + j * 12), 'none', SKIN_D, 1, ' opacity=".35"')
            s += circ(cx, cy + 10, 17, '#e9d2b8', '#a98b6a', 2)
            for j in range(9):
                s += circ(cx - 9 + (j * 7) % 18, cy + 1 + (j * 11) % 18, 1.8, '#5b3b2a', 'none', 0)
            s += text(cx, cy + 62, 'pianta', 12, weight=600, fill='#a0765e')
        else:
            s += foot_side(cx - 236, cy + 40, 1.45)
            tx, ty = cx - 236 + 168 * 1.45, cy + 40 - 24 * 1.45
            s += P('M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z' % (
                tx - 6, ty + 2, tx + 10, ty - 30, tx + 50, ty - 50, tx + 66, ty - 26,
                tx + 72, ty - 14, tx + 64, ty + 6, tx + 54, ty + 4, tx + 50, ty - 18, tx + 24, ty - 18, tx + 10, ty + 6), '#e3c08a', '#a07a3a', 1.6)
            for j in range(4):
                s += P('M%.1f,%.1f q%.1f,-14 %.1f,-22' % (tx + 6 + j * 9, ty - 4 - j * 4, 14, 26), 'none', '#b9915a', 1.2, ' opacity=".7"')
        b += '<g clip-path="url(#%s)">%s</g>' % (cid, s)
        b += rbox(x, y, 300, 166, 'none', ERR, 2, 14)
        b += ftext(x + 222, y + 56, t, 14, 150, weight=800)
        b += arrow(x + 160, y + 82, x + 190, y + 82, ACC2, 2)
        if ic == 'med':
            b += stethoscope(x + 214, y + 94, 0.8)
        elif ic == 'pod':
            b += podo_icon(x + 222, y + 96, 0.9)
        elif ic == 'ban':
            b += ban(x + 222, y + 92, 16)
        else:
            b += stethoscope(x + 206, y + 92, 0.7) + podo_icon(x + 254, y + 96, 0.75)
        b += ftext(x + 222, y + 146, dest, 13.5, 150, weight=800, fill=ERR)
    return svg(W, H, arrow_defs() + b, 'Segnali di STOP sui piedi: quando non si lavora e si consiglia medico o podologo')


@figx('pediluvio-disinfezione.svg')
def pediluvio():
    W, H = 900, 480
    b = T('Vaschetta: dopo ogni cliente')
    cx, cy, R = 450, 246, 128
    steps = [('Svuota', 0), ('Spazzola + sapone', 1), ('Risciacqua', 2), ('Disinfettante', 3), ('Svuota e asciuga', 4), ('Registro', 5)]
    b += circ(cx, cy, R, 'none', '#ead9d5', 18)
    for k in range(6):
        a0 = math.radians(-90 + k * 60 + 14)
        a1 = math.radians(-90 + (k + 1) * 60 - 14)
        b += '<path d="M%.1f,%.1f A%d,%d 0 0 1 %.1f,%.1f" fill="none" stroke="%s" stroke-width="3" marker-end="url(#ar)"/>' % (
            cx + R * math.cos(a0), cy + R * math.sin(a0), R, R, cx + R * math.cos(a1), cy + R * math.sin(a1), ACC2)
    b += circ(cx, cy, 82, GREEN_BG, OK, 1.5)
    b += mtext(cx, cy - 8, ['senza tubature', '= più sicura'], 15, weight=800, fill=OK)
    pos = []
    for k, (t, _) in enumerate(steps):
        a = math.radians(-90 + k * 60)
        px, py = cx + (R + 0) * math.cos(a), cy + (R + 0) * math.sin(a)
        pos.append((px, py))
    for k, (t, _) in enumerate(steps):
        px, py = pos[k]
        # scheda con icona
        side = 'start' if math.cos(math.radians(-90 + k * 60)) > 0.1 else ('end' if math.cos(math.radians(-90 + k * 60)) < -0.1 else 'middle')
        b += circ(px, py, 40, '#fff', ACC, 2.5)
        ic = ''
        if k == 0:
            ic = basin(0, 14, 56, 30, water=False, tilt=-25)
        elif k == 1:
            ic = rbox(-22, -6, 36, 12, '#8a6d4f', 'none', 0, 4) + ''.join(ln(-18 + j * 6, 6, -18 + j * 6, 16, '#6b5a4a', 2) for j in range(6))
            ic += circ(18, -12, 6, '#fff', '#9ccbe6', 1.5) + circ(10, -20, 4, '#fff', '#9ccbe6', 1.5) + circ(24, -2, 4, '#fff', '#9ccbe6', 1.5)
        elif k == 2:
            ic = rbox(-20, -22, 30, 8, GREY, 'none', 0, 3) + rbox(4, -22, 8, 16, GREY, 'none', 0, 2)
            ic += ''.join(P('M%.1f,%.1f q4,6 0,9 q-4,-3 0,-9 z' % (8 + j * 0, -2 + j * 11), '#7fc3e8', 'none', 0) for j in range(3))
        elif k == 3:
            ic = rbox(-16, -16, 26, 40, '#e4f0f8', '#2c5a78', 2, 5) + rbox(-10, -24, 14, 9, '#2c5a78', 'none', 0, 2)
            ic += rbox(-12, -2, 18, 12, '#fff', 'none', 0, 2) + text(-3, 7, '+', 11, weight=800, fill='#2c5a78')
        elif k == 4:
            ic = rbox(-18, -20, 36, 40, '#fff', '#b5a8a3', 2, 3) + ''.join(ln(-14, -12 + j * 9, 14, -12 + j * 9, '#e5d6d2', 1.5) for j in range(4))
        else:
            ic = g(notebook(-26, -20, 52, 40, ('d', 'h', 's')), 0, 0)
        b += g(ic, px, py)
        lab_x = px + (52 if side == 'start' else -52 if side == 'end' else 0)
        lab_y = py + (5 if side != 'middle' else (-50 if k == 0 else 62))
        b += circ(px - 28, py - 28, 12, ACC, 'none', 0) + text(px - 28, py - 23.5, str(k + 1), 13, weight=800, fill='#fff')
        b += text(lab_x, lab_y, t, 15, side, 800)
        if k == 3:
            b += timer(lab_x + 6, lab_y + 26, '10 min (o da etichetta)')
        if k == 5:
            b += text(lab_x, lab_y + 20, 'data · ora · sigla', 13, side, 600, MUTED)
    return svg(W, H, arrow_defs() + b, 'Pulizia e disinfezione della vaschetta da pediluvio dopo ogni cliente, con il registro')


@figx('piede-diabetico-regole.svg')
def diabete():
    W, H = 900, 440
    b = T('Cliente con diabete')
    yes = [('acqua tiepida, misurata', 'therm'), ('asciuga tra le dita', 'towel'), ('taglio dritto', 'clip'),
           ('crema, ma non tra le dita', 'cream'), ('dubbi? podologo', 'pod')]
    no = [('acqua calda', 'hot'), ('pediluvio lungo', 'hour'), ('lame su calli o cuticole', 'blade'),
          ('prodotti callifughi', 'callif'), ('lavorare su ferite', 'wound')]
    for c, (lst, ok) in enumerate([(yes, True), (no, False)]):
        x = 20 + c * 436
        col = OK if ok else ERR
        b += rbox(x, 58, 424, 320, GREEN_BG if ok else RED_BG, col, 1.5, 16)
        b += mark(x + 30, 84, ok, 13) + text(x + 52, 90, 'Sì' if ok else 'No', 18, 'start', 800, col)
        for k, (t, ic) in enumerate(lst):
            y = 128 + k * 52
            b += circ(x + 44, y, 22, '#fff', col, 1.5)
            if ic == 'therm':
                s = thermometer(x + 44, y + 2, 0.5)
            elif ic == 'towel':
                s = towel(x + 44, y, 0.55)
            elif ic == 'clip':
                s = clipper(x + 44, y - 12, 0, 0.42)
            elif ic == 'cream':
                s = jar(x + 44, y + 4, 0.55)
            elif ic == 'pod':
                s = podo_icon(x + 42, y + 2, 0.55)
            elif ic == 'hot':
                s = g(basin(0, 10, 50, 22, water=True, steam=True), x + 44, y + 2, 0, 0.62)
            elif ic == 'hour':
                s = hourglass(x + 44, y, 0.55)
            elif ic == 'blade':
                s = blade(x + 52, y + 6, -30, 0.55)
            elif ic == 'callif':
                s = jar(x + 44, y + 4, 0.55, '#fff', '#8a6d4f') + ln(x + 30, y + 14, x + 58, y - 12, ERR, 3)
            else:
                s = rbox(x + 30, y - 7, 28, 14, '#f4d7b9', '#b88a5a', 1.5, 6) + circ(x + 44, y, 3.5, '#d9534f', 'none', 0)
            b += s
            b += text(x + 80, y + 5, t, 15, 'start', 700)
    b += strip(20, 390, 860, 38, 'Ferite, infezioni, perdita di sensibilità → niente servizio: podologo o medico', 'warn', 14.5)
    return svg(W, H, b, 'Cliente con diabete: cosa fare e cosa evitare durante la pedicure')


@figx('estetista-podologo.svg')
def esteti_podo():
    W, H = 900, 380
    b = T('Estetista e podologo: chi fa cosa')
    cols = [('Estetista', 'piede sano', '#fbe0ea', ACC, ['taglio e lima', 'cuticole (delicatamente)', 'colore', 'idratazione e massaggio']),
            ('Podologo', 'professione sanitaria', BLUE_BG, '#2c5a78', ['unghie incarnite', 'unghie spesse o deformi', 'calli e duroni', 'piede doloroso', 'pazienti a rischio'])]
    for c, (t, sub, bg, col, items) in enumerate(cols):
        x = 20 + c * 540
        b += rbox(x, 58, 320, 270, bg, col, 2, 22)
        b += text(x + 24, 92, t, 19, 'start', 800, col) + text(x + 24, 114, sub, 13.5, 'start', 600, MUTED)
        if c == 1:
            b += podo_icon(x + 280, 92, 0.8, col)
        else:
            b += g(nail_shape(0, 0, 18, 30, '#e46f8f', NAIL_S, 1.2), x + 290, 106)
        for k, it in enumerate(items):
            y = 148 + k * 34
            b += circ(x + 32, y - 5, 5, col, 'none', 0)
            b += text(x + 46, y, it, 15, 'start', 600)
    # frecce centrali
    b += '<line x1="350" y1="160" x2="550" y2="160" stroke="%s" stroke-width="6" marker-end="url(#ar)"/>' % ACC2
    b += mtext(450, 136, ['dolore, infiammazione,', 'deformità → invia'], 13.5, weight=800, fill=ACC2, lh=1.2)
    b += '<line x1="550" y1="240" x2="350" y2="240" stroke="%s" stroke-width="2" marker-end="url(#arw)"/>' % MUTED
    b += mtext(450, 266, ['piede sano → torna', 'per l\'estetica'], 13, weight=700, fill=MUTED, lh=1.2)
    b += stethoscope(372, 352, 0.6) + text(396, 362, 'sospetta malattia (micosi, verruche, ferite) → medico', 14, 'start', 700, '#2c5a78')
    return svg(W, H, arrow_defs() + b, 'Estetista e podologo: chi fa cosa e quando inviare la cliente')


@figx('pedicure-postazione.svg')
def postazione():
    W, H = 900, 430
    b = T('Postazione di pedicure (vista dall\'alto)')
    b += rbox(20, 54, 860, 362, '#fbf7f4', '#ead9d5', 1.5, 16)
    # pavimento a piastrelle leggere
    for k in range(1, 6):
        b += ln(20 + k * 100, 56, 20 + k * 100, 414, '#f2e9e4', 1)
    for k in range(1, 4):
        b += ln(22, 54 + k * 90, 598, 54 + k * 90, '#f2e9e4', 1)
    # poltrona: schienale, braccioli, seduta imbottita
    b += '<g filter="url(#nxShS)">'
    b += rbox(326, 66, 228, 40, '#b9a3d4', '#7d6a9a', 1.8, 18)
    b += rbox(318, 92, 34, 110, '#c8b5df', '#7d6a9a', 1.6, 14) + rbox(528, 92, 34, 110, '#c8b5df', '#7d6a9a', 1.6, 14)
    b += rbox(352, 96, 176, 104, '#e3d8f1', '#8a7d9e', 1.6, 16)
    b += '</g>'
    b += P('M440,100 L440,196', 'none', '#cdbfe0', 1.4) + P('M360,150 Q440,158 520,150', 'none', '#fff', 2, ' opacity=".6"')
    b += text(440, 136, 'poltrona cliente', 13, weight=700, fill='#5d4f78')
    # gambe della cliente e piedi sul poggiapiedi (dita verso l'operatrice)
    for sx in (-1, 1):
        b += rbox(440 + sx * 24 - 15, 168, 30, 66, SKIN, SKIN_D, 1.4, 14)
    b += rbox(378, 214, 124, 92, '#e6dccf', '#a89a88', 1.8, 18) + rbox(388, 222, 104, 76, '#efe7dc', 'none', 0, 14)
    for sx in (-1, 1):
        b += '<g transform="translate(%.1f,208) rotate(180) scale(%.2f,1)">%s</g>' % (440 + sx * 24, -sx, foot_top(0, 0, 0.3))
    b += text(512, 268, 'poggiapiedi', 12.5, 'start', 700, MUTED)
    # sgabello operatrice
    b += circ(440, 360, 32, '#cfd8dc', '#8a9aa3', 2, ' filter="url(#nxShS)"') + circ(440, 360, 22, '#e2e8eb', '#aab7be', 1.2)
    b += text(484, 365, 'sgabello', 12.5, 'start', 700, '#4a5a63')
    # vaschetta vista dall'alto con fodera
    vx, vy = 156, 178
    b += '<ellipse cx="%d" cy="%d" rx="92" ry="60" fill="#e9f3f9" stroke="#7fa9c4" stroke-width="2.4" filter="url(#nxShS)"/>' % (vx, vy)
    b += '<ellipse cx="%d" cy="%d" rx="84" ry="53" fill="none" stroke="#9ccbe6" stroke-width="5" opacity=".8"/>' % (vx, vy)
    b += '<ellipse cx="%d" cy="%d" rx="74" ry="45" fill="%s"/>' % (vx, vy, WATER)
    for k in range(3):
        b += '<ellipse cx="%d" cy="%d" rx="%d" ry="%d" fill="none" stroke="#fff" stroke-width="1.5" opacity=".8"/>' % (vx + 6, vy + 2, 18 + k * 16, 10 + k * 10)
    b += text(vx, 106, 'vaschetta con fodera', 12.5, weight=700, fill=MUTED)
    b += rbox(vx - 62, 250, 124, 26, '#fff', OK, 1.5, 8) + text(vx, 268, 'disinfettata ✓ 10:15', 12, weight=700, fill=OK)
    # lampada e registro
    b += led_lamp(100, 362, 96) + text(100, 392, 'lampada (fondo rimovibile)', 12, weight=600, fill=MUTED)
    b += notebook(204, 310, 92, 64) + text(250, 392, 'registro', 12, weight=600, fill=MUTED)
    # carrello: pulito | usato
    b += rbox(612, 108, 252, 278, '#fff', '#b5a8a3', 2, 12)
    b += ln(738, 118, 738, 376, '#b5a8a3', 1.5, ' stroke-dasharray="5 4"')
    b += rbox(620, 116, 110, 26, GREEN_BG, OK, 1.2, 8) + text(675, 134, 'PULITO', 13, weight=800, fill=OK)
    b += rbox(746, 116, 110, 26, RED_BG, ERR, 1.2, 8) + text(801, 134, 'USATO', 13, weight=800, fill=ERR)
    # busta sterile con strumento dentro
    b += P('M630,154 L720,154 L720,204 L630,204 Z', '#eef6fb', '#7fa9c4', 1.5) + P('M630,154 L645,162 L705,162 L720,154', 'none', '#7fa9c4', 1.2)
    b += tool_pusher(650, 186, -8, 54) + circ(712, 196, 4, '#3aa0d8', 'none', 0)
    b += text(675, 222, 'busta sterile', 12, weight=700, fill='#2c5a78')
    b += file_pro(675, 240, 0, 84, 12)
    b += text(675, 262, 'lima nuova', 12, weight=600, fill=MUTED)
    for j in range(2):
        sep = rbox(-24, -8, 48, 16, '#f6b3c8', '#c2577a', 1.2, 8) + '<rect x="-24" y="-8" width="48" height="16" rx="8" fill="url(#dxPore)"/>'
        sep += ''.join(P('M%d,-8 q6,8 0,16' % (-12 + q * 12), 'none', '#d97a9a', 1.1) for q in range(3))
        b += g(sep, 650 + j * 52, 284)
    b += text(675, 310, 'separadita', 12, weight=600, fill=MUTED)
    b += glove(660, 340, 0.6, '#9fc6e8') + glove(690, 340, 0.6, '#9fc6e8')
    b += text(675, 376, 'guanti', 12, weight=600, fill=MUTED)
    # usato: contenitore chiuso + pattumiera a pedale
    b += rbox(754, 162, 94, 66, '#fde6e3', '#b5a8a3', 1.5, 8) + rbox(750, 154, 102, 14, '#e5a6a0', '#b5a8a3', 1, 5)
    b += mtext(801, 190, ['strumenti da', 'sterilizzare'], 12, weight=700, fill=ERR)
    b += P('M770,268 L832,268 L826,340 L776,340 Z', '#eee8e4', '#8a7d74', 2) + rbox(764, 258, 74, 12, '#8a7d74', 'none', 0, 4)
    b += rbox(790, 340, 22, 6, '#5d534c', 'none', 0, 2)
    b += text(801, 306, 'monouso', 12, weight=700, fill=MUTED) + text(801, 362, 'cestino', 12, weight=600, fill=MUTED)
    b += text(738, 405, 'flusso: pulito → usato, mai al contrario', 13, weight=800, fill=ACC2)
    return svg(W, H, arrow_defs() + b, 'Postazione di pedicure vista dall\'alto: poltrona, poggiapiedi, vaschetta, zona pulito e zona usato')

@figx('tut-semipermanente-piedi.svg')
def tut_semi_piedi():
    labels = ['Ispeziona', 'Taglio dritto', 'Asciuga bene', 'Separadita', 'Opacizza e sgrassa', 'Base', '2 strati sottili', 'Top e olio']
    subs = ['niente colore su unghie sospette', 'angoli limati appena', 'aspetta qualche minuto', 'il colore non tocca il vicino',
            'buffer 180–240, poi disidratante', 'margine dalla pelle', 'lampada dopo ogni strato', 'lampada, poi olio']
    pw, ph = 219, 232
    W = 20 + 4 * pw + 3 * 12 + 20
    b = T('Semipermanente sui piedi: 8 passaggi')
    RED = '#c62f4a'
    for i, lab in enumerate(labels):
        x = 20 + (i % 4) * (pw + 12)
        y = 58 + (i // 4) * (ph + 12)
        cx, by = x + pw / 2 - 10, y + 172
        s = ''
        plate = '#f3cbc6'
        if i >= 5:
            plate = '#f6dbe2'
        ext = ''
        if i == 5:
            ext = ''
        f, p = toe_top(cx, by, hw=38, nail_len=70, free=6, plate=plate, finger_len=12)
        if i >= 6:
            f, p = toe_top(cx, by, hw=38, nail_len=70, free=6, plate=plate, finger_len=12,
                           extra='<rect x="%.1f" y="%.1f" width="80" height="80" fill="%s" clip-path="url(#CLIP)"/>' % (cx - 40, by - 82, RED))
        s += f
        if i == 0:
            s += magnifier(cx + 20, by - 54, 22)
        elif i == 1:
            s += dashed(cx - 56, p['y_t'] + 4, cx + 44, p['y_t'] + 4, OK, 2) + nipper(cx + 70, p['y_t'] + 18, -16, 0.7)
        elif i == 2:
            s += towel(cx + 64, by - 60, 0.8)
            for j in range(3):
                s += P('M%.1f,%.1f q4,6 0,9 q-4,-3 0,-9 z' % (cx - 18 + j * 18, by - 44 - j * 6), '#7fc3e8', 'none', 0, ' opacity="%.2f"' % (0.9 - j * 0.3))
        elif i == 3:
            for sx in (-1, 1):
                sep = rbox(-11, -46, 22, 92, '#f6b3c8', '#c2577a', 1.5, 11)
                sep += '<rect x="-11" y="-46" width="22" height="92" rx="11" fill="url(#dxPore)"/>'
                for j in range(4):
                    sep += P('M-11,%d q11,7 22,0' % (-30 + j * 20), 'none', '#d97a9a', 1.4)
                sep += rbox(-7, -40, 5, 70, '#fff', 'none', 0, 2, ' opacity=".45"')
                s += g(sep, cx + sx * 66, by - 34, sx * 4)
            s += text(cx + 64, by - 88, 'separadita', 12, 'middle', 700, ACC2)
        elif i == 4:
            s += file_pro(cx + 10, by - 40, -30, 76, 20, '#e9e2da', '#f7f3ee')
            s += oil_bottle(cx + 74, by - 70, 0.8)
        elif i == 5:
            s += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - 30, by - 30, cx, by - 6, cx + 30, by - 30), 'none', '#fff', 3)
            s += tool_brush(cx + 34, by - 66, -50, 60, '#f6dbe2')
        elif i == 6:
            s += mini_lamp(cx + 72, by - 92, 0.4) + text(cx + 72, by - 66, '×2', 15, weight=800, fill=ACC2)
        else:
            s += gloss(cx, by - 4, 70, 0.9) + oil_bottle(cx + 70, by - 70, 0.8)
        b += frame(x, y, pw, ph, lab, i + 1, body=s, sub=subs[i], subcol=MUTED, tsize=14)
    return svg(W, 58 + 2 * (ph + 12) + 8, arrow_defs() + b, 'Il semipermanente sui piedi in otto passaggi')


@figx('piedi-errori-colore.svg')
def piedi_errori():
    W, H = 860, 330
    b = T('Errori di colore sui piedi')
    RED = '#c62f4a'
    items = [('colore sulla pelle', False), ('bordo non sigillato', False), ('troppo prodotto nei solchi', False), ('margine pulito, punta sigillata', True)]
    for k, (t, ok) in enumerate(items):
        x = 20 + k * 208
        cx, by = x + 98, 234
        hw, nl = 40, 74
        ext = '<rect x="%.1f" y="%.1f" width="90" height="90" fill="%s" clip-path="url(#CLIP)"/>' % (cx - 45, by - nl - 10, RED)
        f, p = toe_top(cx, by, hw=hw, nail_len=nl, free=6, plate=RED, finger_len=4)
        s = f
        zx, zy = cx + 54, by - 120
        if k == 0:
            s += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z' % (
                cx - 26, by - 8, cx - 18, by + 14, cx + 2, by + 12, cx + 20, by + 16, cx + 24, by - 6, cx, by + 2, cx - 26, by - 8), RED, '#8e1f35', 1)
            s += circ(cx, by + 4, 28, 'none', ERR, 2.2)
        elif k == 1:
            for j in range(3):
                s += P('M%.1f,%.1f l5,8 l5,-8 Z' % (cx - 30 + j * 22, p['y_t'] - 1), '#f3cbc6', 'none', 0)
            s += circ(cx - 10, p['y_t'] + 2, 24, 'none', ERR, 2.2)
        elif k == 2:
            for sx in (-1, 1):
                s += rbox(cx + sx * (hw + 2) - 5, by - nl + 4, 10, nl - 30, '#e0405e', '#8e1f35', 1.5, 5)
                s += ln(cx + sx * (hw + 2) - 1, by - nl + 10, cx + sx * (hw + 2) - 1, by - 40, '#fff', 2)
            s += circ(cx + hw + 2, by - 50, 22, 'none', ERR, 2.2)
        else:
            s += gloss(cx, by - 6, nl, 0.9)
            s += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - 38, by - 30, cx, by + 16, cx + 38, by - 30), 'none', '#f3cbc6', 5)
        b += frame(x, 58, 196, 250, None, None, ok, s, sub=t, subcol=OK if ok else ERR)
    return svg(W, H, arrow_defs() + b, 'Errori tipici del semipermanente sui piedi: colore sulla pelle, bordo non sigillato, prodotto nei solchi')


def chrome_grad(gid, vertical=False):
    return ('<defs><linearGradient id="%s" x1="0" y1="%s" x2="1" y2="%s"><stop offset="0" stop-color="%s"/><stop offset=".5" stop-color="%s"/>'
            '<stop offset="1" stop-color="%s"/></linearGradient></defs>') % (gid, 0, 1 if vertical else 0, CHROME[0], CHROME[1], CHROME[2])


def magnet(x, y, w=44, h=22, ang=0):
    b = rbox(-w / 2, -h / 2, w / 2, h, '#d64545', '#4b3a40', 1.5, 3) + rbox(0, -h / 2, w / 2, h, '#3f6fc4', '#4b3a40', 1.5, 3)
    b += text(-w / 4, h / 4 - 1, 'N', 11, weight=800, fill='#fff') + text(w / 4, h / 4 - 1, 'S', 11, weight=800, fill='#fff')
    return g(b, x, y, ang)


def brush_flat(x, y, ang=0, c1='#ffffff', c2='#e46f8f', load=0.75, s=1.0, ferrule_dirty=False):
    """Pennello piatto visto di fronte, setole verso il basso (prima della rotazione). load = frazione delle setole caricata."""
    bl = 46
    gid = uid('bf')
    b = ('<defs><linearGradient id="%s" x1="0" x2="1"><stop offset="0" stop-color="%s"/><stop offset=".38" stop-color="%s"/>'
         '<stop offset=".62" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>') % (gid, c1, c1, c2, c2)
    b += rbox(-7, -78, 14, 38, '#4b3a40', 'none', 0, 5)
    b += P('M-12,-44 L12,-44 L14,0 L-14,0 Z', '#c9cdd3' if not ferrule_dirty else '#c9cdd3', GREY_D, 1.5)
    if ferrule_dirty:
        b += P('M-13,-16 L13,-16 L14,0 L-14,0 Z', 'url(#%s)' % gid, 'none', 0)
    b += P('M-14,0 L14,0 L16,%.1f L-16,%.1f Z' % (bl, bl), '#f3e6c9', '#b9a77d', 1.2)
    top = bl * (1 - load)
    b += P('M%.1f,%.1f L%.1f,%.1f L16,%.1f L-16,%.1f Z' % (-14 - 2 * top / bl, top, 14 + 2 * top / bl, top, bl, bl), 'url(#%s)' % gid, 'none', 0)
    for k in range(-12, 13, 4):
        b += ln(k, 2, k * 1.1, bl - 1, '#000', 0.6, ' opacity=".15"')
    return g(b, x, y, ang, s)


def petal(cx, cy, ang=0, L=40, W=22, c_out='#ffffff', c_in='#e46f8f'):
    gid = uid('pt')
    b = ('<defs><linearGradient id="%s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>'
         % (gid, c_out, c_in))
    b += P('M0,0 C%.1f,%.1f %.1f,%.1f 0,%.1f C%.1f,%.1f %.1f,%.1f 0,0 Z' % (-W, -L * 0.3, -W * 0.8, -L, -L, W * 0.8, -L, W, -L * 0.3),
           'url(#%s)' % gid, '#c2577a', 1.2)
    # in SVG il gradiente va dalla punta (esterno, chiaro) alla base
    return g(b, cx, cy, ang)


def leaf(cx, cy, ang=0, L=56, W=16):
    gid = uid('lf')
    b = ('<defs><linearGradient id="%s" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#a5d6a7"/><stop offset="1" stop-color="#2e7d32"/></linearGradient></defs>' % gid)
    b += P('M0,0 C%.1f,%.1f %.1f,%.1f 0,%.1f C%.1f,%.1f %.1f,%.1f 0,0 Z' % (-W, -L * 0.3, -W * 0.5, -L * 0.8, -L, W * 0.2, -L * 0.7, W * 0.9, -L * 0.3),
           'url(#%s)' % gid, '#1b5e20', 1.2)
    b += P('M0,-4 Q2,%.1f 0,%.1f' % (-L * 0.5, -L + 8), 'none', '#1b5e20', 1, ' opacity=".6"')
    return g(b, cx, cy, ang)


@figx('chrome-step.svg')
def chrome_step():
    labels = ['Colore liscio', 'Top no-wipe', 'Poca polvere', 'Strofina', 'Pulisci il bordo', 'Top sulla punta']
    subs = ['meglio su nero o scuro', '≈30 s, vedi scheda', 'spugnetta o silicone', 'fino allo specchio', 'buffer + pennello',
            'avvolge il bordo libero']
    pw, ph = 145, 270
    W = 20 + 6 * pw + 5 * 10 + 20
    b = T('Chrome in 6 passaggi')
    BLK = '#1d1a20'
    nw, nh = 58, 124
    for i, lab in enumerate(labels):
        x = 20 + i * (pw + 10)
        cx, by = x + pw / 2 - 4, 58 + 220
        s = '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="6" fill="#000" opacity=".1" filter="url(#dxBlurS)"/>' % (cx, by + 6, nw * 0.5)
        if i <= 2:
            s += gel(cx, by, nw, nh, BLK, '#000', hi=(i < 2), k=1.0 if i < 2 else 0.5)
        elif i == 3:
            cut = 'M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (
                cx - 40, by - 62, cx - 10, by - 72, cx + 10, by - 52, cx + 40, by - 64, cx + 40, by - nh - 10, cx - 40, by - nh - 10)
            cid = uid('cut')
            fx = ('<defs><clipPath id="%s"><path d="%s"/></clipPath></defs><g clip-path="url(#%s)">%s</g>' % (
                cid, cut, cid, chrome_fx(cx, by, nw, nh)))
            fx += '<path d="%s" fill="none" stroke="#c9ced6" stroke-width="2" opacity=".6" clip-path="url(#CLIP)"/>' % cut.split(' L')[0]
            s += gel(cx, by, nw, nh, BLK, '#000', fx=fx, hi=False)
        else:
            s += gel(cx, by, nw, nh, '#9aa1ab', '#4a515b', fx=chrome_fx(cx, by, nw, nh), shade=True, hi=(i == 5), k=1.2)
        if i == 0:
            pass
        elif i == 1:
            s += g(led_lamp(0, 0, 50), cx + 44, 140)
        elif i == 2:
            s += powder_jar(cx + 42, 132) + applicator(cx + 14, by - 80, 28)
            for j in range(7):
                s += circ(cx - 12 + (j * 9) % 30, by - 66 + (j * 13) % 20, 1.3, '#d0d5dc', 'none', 0)
        elif i == 3:
            s += applicator(cx + 4, by - 70, 20, powder=True)
            s += curved_arrow(cx - 30, by - 22, cx + 30, by - 22, 20) + curved_arrow(cx + 30, by - 104, cx - 30, by - 104, 20)
        elif i == 4:
            s += file_pro(cx, by - nh - 8, 0, 74, 13, '#e9e2da', '#f7f3ee')
            s += dust_brush(cx + 44, by - 60, 30, 0.8)
            for j in range(8):
                s += circ(cx - 34 + j * 10, by - nh - 26 - (j % 3) * 7, 1.6, '#9da3b0', 'none', 0)
        else:
            s += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - 34, by - nh + 18, cx, by - nh - 46, cx + 34, by - nh + 18), 'none', ACC2, 2.2, ' marker-end="url(#ar)"')
            s += mark(cx + 50, by - 26, True, 12)
        b += frame(x, 58, pw, ph, lab, i + 1, body=s, sub=subs[i], subcol=OK if i == 5 else MUTED, tsize=13.5)
    return svg(W, 58 + ph + 18, arrow_defs() + b, 'Chrome in sei passaggi: colore, top no-wipe, polvere, strofina fino allo specchio, pulisci il bordo, top finale')

@figx('cat-eye-magnete.svg')
def cat_eye():
    W, H = 900, 480
    b = T('Cat-eye: posizione del magnete')
    body = ''
    ox, oy = 40, 176
    body += finger_side(ox, oy, L=290, th=50, nx0=ox + 130, nx1=ox + 316, nail_th=6, plate='#2b2733', bone=False)
    gel_l = 'M%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z' % (ox + 130, oy - 6, ox + 220, oy - 24, ox + 318, oy - 10, ox + 320, oy - 4, ox + 220, oy - 4, ox + 130, oy - 6)
    body += P(gel_l, '#2a2533', '#000', 1)
    for j in range(16):
        xx = ox + 144 + j * 11
        d = xx - (ox + 225)
        angd = max(-70, min(70, d * 1.4))
        yy = oy - 10 - (8 - abs(d) / 12) * 0.9
        body += g(ln(0, -3.5, 0, 3.5, '#d9cfff', 1.8), xx, yy, -angd)
    body += '<ellipse cx="%d" cy="%d" rx="18" ry="5" fill="#d9cfff" opacity=".6" filter="url(#dxBlurS)"/>' % (ox + 225, oy - 18)
    body += bar_magnet(ox + 225, oy - 68, 72, 24)
    for k in (-1, 0, 1):
        body += P('M%d,%d Q%d,%d %d,%d' % (ox + 225 + k * 26, oy - 54, ox + 225 + k * 14, oy - 40, ox + 225 + k * 5, oy - 26), 'none', '#9a90c8', 1.4, ' stroke-dasharray="3 3"')
    body += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.8" marker-start="url(#ar)" marker-end="url(#ar)"/>' % (ox + 288, oy - 56, ox + 288, oy - 24, ACC2)
    body += text(ox + 300, oy - 36, '1–5 mm: non toccare', 14, 'start', 800, ACC2)
    body += mtext(560, 136, ['Le particelle metalliche si', 'spostano verso il magnete', 'finché il gel è fluido.'], 13.5, 'start', 600, INK, 1.45)
    b += frame(20, 58, 860, 176, 'Di profilo', body=body, tsize=14)
    names = [('centro', 'linea centrale'), ('45°', 'banda diagonale'), ('lato', 'luce su un lato'), ('due magneti', 'effetto galassia'), ('velvet', 'luce diffusa')]
    modes = ['centro', '45', 'lato', 'galassia', 'velvet']
    for k, (n, sub) in enumerate(names):
        x = 20 + k * 174
        cx, by = x + 58, 392
        nw, nh = 54, 124
        b += rbox(x, 246, 162, 220)
        b += '<ellipse cx="%.1f" cy="%.1f" rx="26" ry="5" fill="#000" opacity=".12" filter="url(#dxBlurS)"/>' % (cx, by + 6)
        b += gel(cx, by, nw, nh, '#1f1b29', '#000', fx=cateye_fx(cx, by, nw, nh, modes[k]), hi=False)
        mx = x + 126
        if k == 0:
            b += bar_magnet(mx, 330, 44, 16, 90)
        elif k == 1:
            b += bar_magnet(mx, 330, 44, 16, 45)
        elif k == 2:
            b += bar_magnet(mx, 356, 44, 16, 90)
        elif k == 3:
            b += bar_magnet(mx - 12, 330, 40, 14, 90) + bar_magnet(mx + 12, 330, 40, 14, 90)
        else:
            b += bar_magnet(mx, 300, 40, 16, 0) + curved_arrow(mx - 20, 340, mx + 20, 340, 10) + curved_arrow(mx + 20, 358, mx - 20, 358, 10)
        b += text(x + 81, 424, n, 14.5, weight=800)
        b += ftext(x + 81, 444, sub, 12.5, 150, weight=600, fill=MUTED)
    b += rbox(560, 18, 320, 30, YEL_BG, YEL, 1.2, 12) + text(720, 38, 'Flash ≈ 10 s, un dito alla volta', 13.5, weight=800, fill='#7a5a12')
    return svg(W, H, arrow_defs() + b, 'Cat-eye: dove tieni il magnete decide il disegno della luce')

@figx('foil-ombre-step.svg')
def foil_ombre():
    W = 960
    b = T('Foil e ombré')
    pw, ph = 222, 200
    rows = [('Foil', ['gel per foil sottile', 'foil: disegno in su', 'strofina e solleva', 'top che sigilla']),
            ('Ombré con spugnetta', ['spugna sul nastro', 'due colori vicini', 'picchietta dalla punta', 'lampada, ripeti, top'])]
    BUR = '#7a2b4a'
    PK, VI = '#f48fb1', '#9575cd'
    for r, (rt, labs) in enumerate(rows):
        y = 58 + r * (ph + 42)
        b += text(20, y + 8, rt, 16, 'start', 800, ACC2)
        y += 18
        for i, lab in enumerate(labs):
            x = 20 + i * (pw + 12)
            cx, by = x + pw / 2 - 26, y + 182
            nw, nh = 54, 124
            s = '<ellipse cx="%.1f" cy="%.1f" rx="26" ry="5" fill="#000" opacity=".1" filter="url(#dxBlurS)"/>' % (cx, by + 6)
            patch = 'M%.1f,%.1f l8,-14 l10,-6 l12,4 l6,-8 l12,10 l-2,12 l8,10 l-8,14 l-10,4 l-6,10 l-14,-4 l-10,-10 l-6,-8 Z' % (cx - 16, by - 64)
            if r == 0:
                fx = ''
                if i == 0:
                    fx = ('<path d="%s" fill="#fff" opacity=".28" clip-path="url(#CLIP)"/>' % patch
                          + '<path d="%s" fill="none" stroke="#fff" stroke-width="1.2" opacity=".7" stroke-dasharray="3 2" clip-path="url(#CLIP)"/>' % patch)
                if i >= 2:
                    fx = foil_fx(patch, 5)
                s += gel(cx, by, nw, nh, BUR, '#3b1525', fx=fx, hi=(i == 3), k=1.1)
                if i == 0:
                    s += g(led_lamp(0, 0, 54), cx + 70, y + 92) + text(cx + 70, y + 112, 'appiccicoso', 12, weight=700, fill=MUTED)
                elif i == 1:
                    sheet = 'M-38,-26 L38,-24 L36,26 L-36,24 Z'
                    sb = '<path d="%s" fill="url(#dxGold)" stroke="#a8871f" stroke-width="1.2"/>' % sheet
                    sb += foil_fx(sheet, 9, clip=False)
                    sb += '<path d="%s" fill="#fff" opacity=".12"/>' % sheet
                    s += g(sb, cx + 6, by - 66, -8)
                    s += mtext(cx + 74, y + 60, ['lato opaco', 'verso l\'unghia'], 12, 'middle', 700, MUTED, 1.2)
                    s += P('M%.1f,%.1f q-6,10 -18,14' % (cx + 64, y + 82), 'none', MUTED, 1.4, ' marker-end="url(#arw)"')
                elif i == 2:
                    film = 'M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (cx + 4, by - 50, cx + 30, by - 96, cx + 86, by - 120, cx + 62, by - 70)
                    s += '<path d="%s" fill="#f2f0ea" fill-opacity=".85" stroke="#a8a294" stroke-width="1.2"/>' % film
                    fb = 'M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (cx + 40, by - 96, cx + 86, by - 120, cx + 62, by - 70, cx + 50, by - 74)
                    s += foil_fx(fb, 2, clip=False)
                    s += arrow(cx + 64, by - 112, cx + 88, by - 140, ACC2, 2)
                else:
                    s += nail_shine(cx, by, nw, nh) + mark(cx + 72, y + 50, True, 12)
            else:
                if i == 0:
                    s = rbox(cx - 60, by - 30, 132, 20, '#f3e3a6', '#c9b25a', 1.5, 3)
                    s += rbox(cx - 60, by - 30, 132, 7, '#fff', 'none', 0, 3, ' opacity=".45"')
                    s += sponge(cx + 6, by - 66, 50, 52)
                    for j in range(5):
                        s += P('M%.1f,%.1f q3,-4 6,0 q3,4 6,0' % (cx - 40 + j * 22, by - 22 + (j % 2) * 3), 'none', '#9a8a6a', 1.2)
                    s += arrow(cx + 6, by - 122, cx + 6, by - 98, ACC2, 2) + text(cx + 6, by - 128, 'togli i pelucchi', 12, 'middle', 700, ACC2)
                    s += text(cx + 6, by + 4, 'nastro adesivo', 12, weight=600, fill=MUTED)
                elif i == 1:
                    s = sponge(cx + 6, by - 70, 74, 80, (PK, VI))
                    s += arrow(cx + 6, by - 4, cx + 6, by - 20, ACC2, 1.8)
                    s += text(cx + 6, by + 8, 'si toccano al centro', 12, weight=700, fill=MUTED)
                else:
                    gid = uid('om')
                    if i == 2:
                        fx = ('<defs>%s</defs><rect x="%.1f" y="%.1f" width="70" height="80" fill="url(#%s)" clip-path="url(#CLIP)"/>'
                              % (_lg(gid, [(0, VI, 1), (.6, VI, .85), (1, VI, 0)], 0, 1), cx - 35, by - nh - 4, gid))
                        fx += '<rect x="%.1f" y="%.1f" width="70" height="80" fill="url(#dxPore)" clip-path="url(#CLIP)"/>' % (cx - 35, by - nh - 4)
                        s += gel(cx, by, nw, nh, '#f8d7e3', NAIL_S, fx=fx, hi=False)
                        s += sponge(cx + 58, by - nh + 46, 40, 44, (PK, VI), -20)
                        s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2" marker-start="url(#ar)" marker-end="url(#ar)"/>' % (
                            cx + 96, by - nh + 6, cx + 96, by - nh + 44, ACC2)
                        s += text(cx + 62, by - nh + 96, 'tap tap', 12, 'middle', 700, ACC2)
                    else:
                        fx = ('<defs>%s</defs><rect x="%.1f" y="%.1f" width="70" height="140" fill="url(#%s)" clip-path="url(#CLIP)"/>'
                              % (_lg(gid, [(0, VI), (.3, VI), (.55, mix(VI, PK, .5)), (.8, PK), (1, PK)], 0, 1), cx - 35, by - nh - 4, gid))
                        fx += '<rect x="%.1f" y="%.1f" width="70" height="140" fill="url(#dxPore)" opacity=".5" clip-path="url(#CLIP)"/>' % (cx - 35, by - nh - 4)
                        s += gel(cx, by, nw, nh, PK, '#a8507a', fx=fx, k=1.1) + nail_shine(cx, by, nw, nh)
                        s += g(led_lamp(0, 0, 54), cx + 70, y + 92)
            b += frame(x, y, pw, ph, lab, i + 1, body=s, tsize=13.5)
    H = 58 + 2 * (ph + 42) - 6
    return svg(W, H, arrow_defs() + b, 'Foil e ombré passo per passo: gel per foil, foil, strofina e solleva, top; spugnetta, due colori, picchietta, top')

@figx('one-stroke-carico.svg')
def os_carico():
    W, H = 860, 350
    b = T('Caricare il pennello one-stroke')
    # 1
    body = brush_flat(150, 196, 0, '#ffffff', '#e46f8f', 0.55, 1.2)
    body += circ(108, 296, 14, '#ffffff', '#c9c0b8', 1.5) + circ(192, 296, 14, '#e46f8f', '#c2577a', 1.5)
    body += arrow(114, 280, 132, 260, MUTED, 1.8) + arrow(186, 280, 168, 260, MUTED, 1.8)
    b += frame(20, 58, 260, 270, 'Metà e metà', 1, body=body)
    # 2
    body = rbox(312, 236, 236, 64, '#ffffff', '#c9c0b8', 1.5, 8)
    body += '<ellipse cx="430" cy="268" rx="70" ry="16" fill="url(#tav)"/>'
    body += ('<defs><linearGradient id="tav" x1="0" x2="1"><stop offset="0" stop-color="#ffffff"/><stop offset=".5" stop-color="#f3b3c6"/>'
             '<stop offset="1" stop-color="#e46f8f"/></linearGradient></defs>')
    body += brush_flat(430, 172, 0, '#ffffff', '#e46f8f', 0.6, 1.1)
    body += '<line x1="360" y1="244" x2="500" y2="244" stroke="%s" stroke-width="2.4" marker-start="url(#ar)" marker-end="url(#ar)"/>' % ACC2
    body += text(430, 316, 'sempre nello stesso punto', 13, weight=700, fill=MUTED)
    b += frame(300, 58, 260, 270, 'Sfuma sulla tavolozza', 2, body=body)
    # 3
    body = brush_flat(656, 190, 0, '#ffffff', '#e46f8f', 0.75, 1.2)
    body += '<line x1="692" y1="204" x2="692" y2="245" stroke="%s" stroke-width="1.8" marker-start="url(#ar)" marker-end="url(#ar)"/>' % ACC2
    body += text(700, 230, '3/4', 15, 'start', 800, ACC2)
    body += mark(660, 280, True, 12) + text(660, 310, '3/4 setole', 13, weight=800, fill=OK)
    body += brush_flat(790, 200, 0, '#ffffff', '#e46f8f', 1.0, 1.0, ferrule_dirty=True)
    body += circ(790, 192, 16, 'none', ERR, 2.2)
    body += mark(790, 280, False, 12) + text(790, 310, 'mai nella ghiera', 13, weight=800, fill=ERR)
    b += frame(580, 58, 260, 270, 'Quanto caricare', 3, body=body)
    return svg(W, H, arrow_defs() + b, 'Caricare il pennello piatto per il one-stroke: due colori, sfumati sulla tavolozza, fino a 3/4 delle setole')


@figx('one-stroke-fiore.svg')
def os_fiore():
    W, H = 960, 360
    b = T('Petalo, fiore, foglia')
    # 1 petalo in 3 fasi
    body = ''
    for k, (lab) in enumerate(['appoggia', 'premi', 'ruota']):
        x = 50 + k * 100
        if k == 0:
            body += g(rbox(-18, -3, 36, 6, '#e46f8f', '#c2577a', 1, 2), x, 150)
        elif k == 1:
            body += g(rbox(-22, -10, 44, 20, '#e46f8f', '#c2577a', 1, 4), x, 150)
        else:
            body += petal(x - 16, 160, 50, 46, 24)
            body += circ(x - 16, 160, 4, INK, 'none', 0)
            body += curved_arrow(x + 12, 170, x + 22, 128, 18)
        body += text(x, 200, lab, 13, weight=700)
        if k < 2:
            body += arrow(x + 30, 150, x + 62, 150, MUTED, 1.6)
    body += text(150, 236, 'il puntino = perno fermo', 12.5, weight=600, fill=MUTED)
    body += petal(150, 296, 0, 44, 26)
    b += frame(20, 58, 300, 270, 'Petalo', 1, body=body)
    # 2 fiore
    body = ''
    cx, cy = 480, 210
    for k in range(5):
        a = k * 72
        body += petal(cx, cy, a, 58, 30)
    for k in range(5):
        a = math.radians(-90 + k * 72)
        body += circ(cx + 76 * math.cos(a), cy + 76 * math.sin(a), 11, ACC, 'none', 0) + text(cx + 76 * math.cos(a), cy + 76 * math.sin(a) + 4.5, str(k + 1), 12, weight=800, fill='#fff')
    for k in range(6):
        a = math.radians(k * 60)
        body += circ(cx + 8 * math.cos(a), cy + 8 * math.sin(a), 3.6, '#fbc02d', '#c49000', 1)
    body += circ(cx, cy, 4, '#fbc02d', '#c49000', 1)
    body += text(cx, 316, 'colore chiaro sempre verso l\'esterno', 13, weight=700, fill=MUTED)
    b += frame(330, 58, 300, 270, 'Fiore a 5 petali', 2, body=body)
    # 3 foglia
    body = leaf(760, 280, 50, 120, 30)
    body += P('M720,250 Q780,190 860,150', 'none', ACC2, 2, ' stroke-dasharray="5 4" marker-end="url(#ar)"')
    body += P('M864,146 q12,-6 8,-16 q-6,-8 -14,0', 'none', ACC2, 2.2)
    body += text(800, 118, 'torsione = punta', 13, weight=800, fill=ACC2)
    body += text(780, 316, 'premi, scivola, alleggerisci', 13, weight=700, fill=MUTED)
    b += frame(640, 58, 300, 270, 'Foglia', 3, body=body)
    b += text(480, 348, 'Allenati su carta prima che sul tip.', 14, weight=700, fill=ACC2)
    return svg(W, H, arrow_defs() + b, 'One-stroke: petalo, fiore a cinque petali e foglia, passo per passo')


@figx('incapsulato-zone.svg')
def incaps():
    W, H = 860, 380
    b = T('Incapsulato: dove sì, dove no')
    # vista dall'alto con zone
    body = ''
    cx, by = 150, 344
    zones = ''
    zones += '<rect x="%.1f" y="%.1f" width="120" height="38" fill="#e46f6f" opacity=".75" clip-path="url(#CLIP)"/>' % (cx - 60, by - 30)
    for sx in (-1, 1):
        zones += '<rect x="%.1f" y="%.1f" width="12" height="230" fill="#e46f6f" opacity=".75" clip-path="url(#CLIP)"/>' % (cx + (sx * 46) - 6, by - 236)
    zones += '<rect x="%.1f" y="%.1f" width="120" height="14" fill="#e46f6f" opacity=".75" clip-path="url(#CLIP)"/>' % (cx - 60, by - 236)
    zones += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="#5cb87a" stroke-width="14" fill="none" opacity=".8" clip-path="url(#CLIP)"/>' % (cx - 44, by - 130, cx, by - 160, cx + 44, by - 130)
    zones += '<ellipse cx="%.1f" cy="%.1f" rx="24" ry="28" fill="#5cb87a" opacity=".75" clip-path="url(#CLIP)"/>' % (cx, by - 80)
    zones += '<ellipse cx="%.1f" cy="%.1f" rx="20" ry="22" fill="#5cb87a" opacity=".75" clip-path="url(#CLIP)"/>' % (cx, by - 200)
    body += nail_shape(cx, by, 96, 236, '#f9e7ec', NAIL_S, 1.8, zones)
    lx = 236
    body += leader(cx + 4, by - 200, lx, 106, 'centro della punta: sì', 'start', 13, fill=OK)
    body += leader(cx + 40, by - 136, lx, 152, 'smile line: sì', 'start', 13, fill=OK)
    body += leader(cx + 20, by - 80, lx, 198, 'zona apex: sì', 'start', 13, fill=OK)
    body += leader(cx + 30, by - 230, lx, 244, 'bordo: no', 'start', 13, fill=ERR)
    body += leader(cx + 47, by - 40, lx, 278, 'lati: no', 'start', 13, fill=ERR)
    body += leader(cx + 30, by - 10, lx, 312, 'cuticola: no', 'start', 13, fill=ERR)
    b += frame(20, 58, 400, 300, 'Vista dall\'alto', body=body)
    # sezione
    body = ''
    x0, x1, oy = 450, 820, 180
    body += rbox(x0, oy, x1 - x0, 8, NAT, NAIL_S, 1, 3)
    body += rbox(x0 + 10, oy - 6, x1 - x0 - 20, 6, CLEAR, CLEAR_S, 1, 2)
    body += leader(x0 + 60, oy - 3, x0 + 20, oy + 34, 'piattaforma ≤ spessore di un tip', 'start', 12.5)
    # fiore
    for k in range(5):
        a = math.radians(k * 72)
        body += circ(620 + 10 * math.cos(a), oy - 12 + 4 * math.sin(a), 7, '#ec6f9b', '#a8325c', 1.2)
    body += circ(620, oy - 12, 3.5, '#fbc02d', 'none', 0)
    body += leader(626, oy - 12, 690, 214, 'decorazione', 'start', 12.5)
    # strato sopra con apex
    body += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z' % (x0 + 10, oy - 6, 560, oy - 52, 620, oy - 52, 720, oy - 52, x1 - 10, oy - 10, x1 - 10, oy - 6),
              CLEAR, CLEAR_S, 1.4, ' opacity=".85"')
    body += circ(620, oy - 51, 4, ACC2, 'none', 0)
    body += leader(620, oy - 51, 660, 108, 'apex sopra il decoro', 'start', 13)
    body += mark(820, 90, True, 12)
    # mini ✗
    body += rbox(460, 250, 370, 96, '#fff', ERR, 1.5, 12)
    body += nail_shape(520, 336, 40, 76, '#f9e7ec', NAIL_S, 1.4)
    body += circ(540, 296, 7, '#f48fb1', '#c2577a', 1) + circ(546, 288, 6, '#f48fb1', '#c2577a', 1)
    body += circ(543, 293, 14, 'none', ERR, 2)
    body += mark(810, 272, False, 11)
    body += text(570, 290, 'decorazione che sporge dal lato:', 13, 'start', 700, ERR)
    body += text(570, 310, 'la capsula resta aperta = lifting', 13, 'start', 700, ERR)
    body += text(570, 330, 'rifila prima di coprire', 13, 'start', 600, MUTED)
    b += frame(440, 58, 400, 300, 'In sezione', body=body)
    return svg(W, H, arrow_defs() + b, 'Dove incapsulare: nelle zone spesse (smile line, apex, centro della punta), mai alla cuticola, ai lati o sul bordo')


@figx('gara-postazione.svg')
def gara_post():
    W, H = 900, 440
    b = T('Il tavolo di gara (vista dall\'alto)')
    # piano del tavolo
    b += rbox(30, 64, 560, 262, 'url(#dxWood)', '#a89a88', 2.5, 12, ' filter="url(#nxShS)"')
    b += rbox(40, 74, 540, 242, 'none', '#e0d3c3', 1, 8)
    b += text(310, 92, 'lato tecnico', 12, weight=700, fill='#a08c76')
    # 7 lampada da tavolo (vista dall'alto: paralume tondo)
    b += '<circle cx="86" cy="128" r="36" fill="#fff6cc" opacity=".6"/>' + circ(86, 128, 24, '#fff9e0', '#d9b44a', 2) + circ(86, 128, 8, '#f3d27a', '#d9b44a', 1.5)
    b += num_badge(116, 100, 7)
    # 1 prodotti etichettati (flaconi)
    for k in range(5):
        bx = 150 + k * 40
        c = ['#f2c6d2', '#ffffff', '#d9eef5', '#e46f8f', '#f3d27a'][k]
        b += '<ellipse cx="%.1f" cy="160" rx="15" ry="4" fill="#000" opacity=".12"/>' % (bx + 14)
        b += rbox(bx, 112, 28, 46, c, '#7d6a70', 1.4, 7) + rbox(bx + 7, 100, 14, 14, '#3b2a30', 'none', 0, 3)
        b += rbox(bx + 4, 126, 20, 16, '#fff', '#7d6a70', 0.8, 2) + ln(bx + 7, 132, bx + 21, 132, '#b9aaa5', 1) + ln(bx + 7, 137, bx + 17, 137, '#b9aaa5', 1)
        b += rbox(bx + 4, 116, 3, 36, '#fff', 'none', 0, 1, ' opacity=".5"')
    b += mark(350, 112, True, 10) + num_badge(150, 98, 1)
    # 2 scatola tip a scomparti
    b += rbox(384, 96, 130, 74, '#fff', '#7d6a70', 2, 6, ' filter="url(#nxShS)"')
    for r in range(2):
        for c in range(5):
            tx, ty = 392 + c * 24.5, 104 + r * 32
            b += rbox(tx, ty, 21, 28, '#f6f2ef', '#d8ccc6', 1, 3)
            for q in range(3):
                b += nail_shape(tx + 5 + q * 5.5, ty + 24, 6, 16, '#fbf7f2', '#cbbdb4', 0.6)
    b += num_badge(384, 96, 2)
    # 3 cartine intatte (rotolo)
    b += circ(552, 132, 22, '#f6e7a8', '#c9b25a', 2) + circ(552, 132, 9, '#fff', '#c9b25a', 1.5) + circ(552, 132, 15, 'none', '#e3cf7c', 1)
    b += num_badge(574, 106, 3)
    # 6 timer
    b += timer_icon(86, 258, 1.0) + num_badge(112, 228, 6)
    # 5 asciugamano + poggiabraccio
    b += rbox(196, 200, 240, 116, '#ffffff', '#d8ccc6', 1.5, 6)
    for k in range(5):
        b += ln(200, 212 + k * 4, 432, 212 + k * 4, '#f2b8c9', 1.6)
    b += rbox(246, 246, 140, 52, '#d9c4b0', '#a8907a', 1.5, 24) + P('M262,262 Q316,254 370,262', 'none', '#fff', 2.5, ' opacity=".55"')
    b += num_badge(246, 246, 5)
    # 4 lampada UV/LED vista dall'alto
    b += rbox(462, 214, 106, 92, '#f7f5fa', '#8a7d9e', 2, 26, ' filter="url(#nxShS)"')
    b += rbox(476, 268, 78, 38, '#3a3046', 'none', 0, 10) + rbox(476, 268, 78, 38, 'url(#dxGlowUV)', 'none', 0, 10)
    b += P('M474,228 Q515,218 556,228', 'none', '#fff', 3, ' opacity=".9"') + rbox(500, 236, 30, 6, '#c9b8e6', 'none', 0, 3)
    b += num_badge(462, 214, 4)
    # lato modella
    b += rbox(196, 336, 240, 38, '#e8ddf3', '#8a7d9e', 1.5, 12) + text(316, 360, 'lato modella', 13, weight=700, fill='#5d4f78')
    b += rbox(196, 384, 120, 30, '#fff', ACC, 2, 6) + text(256, 404, 'Modella n. 12', 12.5, weight=800, fill=ACC2)
    # 8 cestino accanto al tavolo
    b += P('M484,344 L540,344 L535,404 L489,404 Z', '#eee8e4', '#8a7d74', 2) + rbox(478, 334, 68, 12, '#8a7d74', 'none', 0, 4)
    for k in range(3):
        b += ln(498 + k * 14, 352, 498 + k * 13, 396, '#d5cbc4', 1.4)
    b += num_badge(478, 334, 8, col=ACC2)
    # legenda numerata
    lx, ly = 612, 64
    b += rbox(lx, ly, 268, 240)
    b += text(lx + 18, ly + 28, 'Sul tavolo', 15, 'start', 800, ACC2)
    leg = [(1, 'prodotti con etichetta originale', OK), (2, 'tip in scatola, ≥ 10 per misura', INK), (3, 'cartine intatte', INK),
           (4, 'lampada UV/LED', INK), (5, 'poggiabraccio su asciugamano', INK), (6, 'timer (se permesso)', INK),
           (7, 'lampada da tavolo', INK), (8, 'cestino! accanto al tavolo', ACC2)]
    for k, (n, t, c) in enumerate(leg):
        yy = ly + 56 + k * 23.5
        b += circ(lx + 28, yy - 4.5, 9.5, ACC if n != 8 else ACC2, 'none', 0) + text(lx + 28, yy, str(n), 11.5, weight=800, fill='#fff')
        b += ftext(lx + 46, yy, t, 13, 212, 'start', 700 if c != INK else 600, c)
    # lontano dal tavolo
    b += rbox(lx, 314, 268, 112, RED_BG, ERR, 1.5, 12)
    b += mark(lx + 24, 338, False, 11) + text(lx + 42, 343, 'lontano dal tavolo', 14, 'start', 800, ERR)
    ix = [lx + 50, lx + 134, lx + 218]
    b += P('M%d,368 L%d,368 L%d,400 L%d,400 Z' % (ix[0] - 18, ix[0] + 18, ix[0] + 22, ix[0] - 22), '#c9a27e', '#8a6d4f', 1.5) + P('M%d,368 Q%d,352 %d,368' % (ix[0] - 9, ix[0], ix[0] + 9), 'none', '#8a6d4f', 2)
    b += P('M%d,358 L%d,358 L%d,366 L%d,404 L%d,404 L%d,366 Z' % (ix[1] - 12, ix[1] + 12, ix[1] + 22, ix[1] + 18, ix[1] - 18, ix[1] - 22), '#7fa9c4', '#4f7a96', 1.5)
    b += P('M%d,358 L%d,372 L%d,358' % (ix[1] - 6, ix[1], ix[1] + 6), 'none', '#4f7a96', 1.5)
    b += rbox(ix[2] - 22, 360, 44, 34, '#ddd', '#888', 1.5, 4) + circ(ix[2] - 14, 400, 4.5, '#555', 'none', 0) + circ(ix[2] + 14, 400, 4.5, '#555', 'none', 0)
    for t, xx in zip(('borsa', 'giacca', 'carrello'), ix):
        b += ln(xx - 22, 356, xx + 22, 404, ERR, 3) + text(xx, 420, t, 12, weight=700)
    return svg(W, H, b, 'Il tavolo di gara visto dall\'alto: prodotti etichettati, scatola tip, lampada, cestino accanto, niente borse sul tavolo')

@figx('gara-piano-allenamento.svg')
def gara_piano():
    W, H = 920, 330
    b = T('12 settimane verso la gara')
    x0, x1 = 40, 820
    wk = (x1 - x0) / 12
    phases = [('Sett. 1–4', 'Base', 'una mano a settimana, foto', 0, 4, '#f2b8c9', INK),
              ('Sett. 5–8', 'Correzione', 'allena i punti deboli', 4, 8, '#e88aa6', INK),
              ('Sett. 9–12', 'Simulazione', 'simulazioni −10 min', 8, 12, ACC2, '#fff')]
    # settimana 1: avvio
    b += rbox(x0, 58, wk * 1 - 4, 40, '#fbe3ea', ACC, 1.2, 10) + text(x0 + (wk - 4) / 2, 83, 'Sett. 1', 13, weight=800, fill=ACC2)
    b += P('M%.1f,78 L%.1f,78' % (x0 + wk, x0 + wk + 14), 'none', ACC, 1.5)
    b += text(x0 + wk + 20, 83, 'regolamento, scheda punteggi e lista del kit', 13.5, 'start', 700, INK)
    # fasi a freccia (chevron)
    for k, (t, ph, sub, a, z, col, tc) in enumerate(phases):
        xa, xz = x0 + a * wk, x0 + z * wk
        tip = 14
        d = 'M%.1f,112 L%.1f,112 L%.1f,148 L%.1f,184 L%.1f,184 %s Z' % (
            xa, xz - tip, xz, xz - tip, xa, ('L%.1f,148' % (xa + tip)) if k else '')
        b += '<path d="%s" fill="%s" filter="url(#nxShS)"/>' % (d, col)
        tx = xa + (24 if k else 14)
        b += text(tx, 136, t, 14, 'start', 800, tc)
        b += text(xz - tip - 8, 136, ph.upper(), 11.5, 'end', 800, tc if k == 2 else ACC2)
        b += ftext(tx, 160, sub, 13, xz - xa - 40, 'start', 600, tc)
    # asse delle settimane
    ay = 222
    b += ln(x0, ay, x1, ay, MUTED, 2)
    for k in range(13):
        b += ln(x0 + k * wk, ay - 6, x0 + k * wk, ay + 6, MUTED, 1.5)
        if k < 12:
            b += text(x0 + (k + 0.5) * wk, ay + 22, str(k + 1), 12.5, weight=600, fill=MUTED)
    b += text(x0, ay + 42, 'settimane', 12.5, 'start', 600, MUTED)
    # traguardo
    fx = x1 + 34
    b += ln(fx, ay + 6, fx, ay - 40, '#4b3a40', 2.5)
    fid = uid('flag')
    b += '<defs><pattern id="%s" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#fff"/><rect width="4" height="4" fill="#3b2a30"/><rect x="4" y="4" width="4" height="4" fill="#3b2a30"/></pattern></defs>' % fid
    b += P('M%.1f,%.1f l26,0 l0,18 l-26,0 Z' % (fx, ay - 40), 'url(#%s)' % fid, '#3b2a30', 1.2)
    b += text(fx + 2, ay + 22, 'Gara', 14, weight=800, fill=ERR)
    b += ln(x1, ay, fx, ay, MUTED, 2, ' stroke-dasharray="3 3"')
    b += strip(40, 276, 780, 36, 'Ultima settimana: niente prodotti nuovi; controlla le unghie della modella', 'info', 13.5)
    return svg(W, H, b, 'Piano di allenamento indicativo di 12 settimane verso una gara: base, correzione dei punti deboli, simulazioni')

@figx('gara-punteggio.svg')
def gara_punti():
    W, H = 900, 476
    b = T('Dove sono i punti (French Twist 3 forme, 240 pt)')
    data = [('G1 Smile line', 15, 'a'), ('G2 Lunghezza', 15, 'a'), ('G3 Curva C + apex', 30, 's'), ('G4 Spessore + convesso/concavo', 30, 's'),
            ('G5 Forma', 15, 'a'), ('G6 Archi e linee laterali', 30, 's'), ('G7 Decoro, colore, creatività', 45, 'a'),
            ('G8 Cuticola + lucentezza', 18, 'e'), ('G9 Aderenza + superficie', 18, 'a'), ('G10 Applicazione + letto', 24, 'a')]
    col = {'a': '#d9c3cb', 's': ACC2, 'e': OK}
    tot = 240
    # barra di sintesi (composizione dei 240 punti)
    sx0, sw = 290, 560
    b += text(sx0 - 12, 84, 'Totale 240 pt', 13.5, 'end', 800, INK)
    xx = sx0
    for key, lab in (('s', 'struttura 90'), ('e', 'facili 18'), ('a', 'altri 132')):
        v = sum(d[1] for d in data if d[2] == key)
        w = v / tot * sw
        b += rbox(xx, 68, w - 2, 24, col[key], 'none', 0, 4)
        if w > 90:
            b += text(xx + (w - 2) / 2, 85, '%s · %d%%' % (lab, round(v * 100 / tot)), 12.5, weight=800, fill='#fff' if key != 'a' else INK)
        else:
            b += ln(xx + (w - 2) / 2, 93, xx + (w - 2) / 2, 99, MUTED, 1) + text(xx + (w - 2) / 2, 111, '%s · %d%%' % (lab, round(v * 100 / tot)), 12, weight=700, fill=INK)
        xx += w
    # barre per giudice
    x0, sc = 290, 8.4
    top = 124
    for v in (0, 15, 30, 45):
        b += ln(x0 + v * sc, top - 6, x0 + v * sc, top + 300, '#ead9d5', 1, ' stroke-dasharray="3 3"')
        b += text(x0 + v * sc, top + 316, str(v), 12, weight=600, fill=MUTED)
    b += text(x0 + 45 * sc + 26, top + 316, 'punti', 12, 'start', 600, MUTED)
    for k, (t, v, c) in enumerate(data):
        y = top + k * 30
        b += text(x0 - 12, y + 16, t, 13.5, 'end', 700 if c != 'a' else 600, INK)
        b += '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s"/>' % (
            x0, y + 4, x0 + v * sc - 4, y + 4, x0 + v * sc, y + 4, x0 + v * sc, y + 8, x0 + v * sc, y + 18, x0 + v * sc, y + 22, x0 + v * sc - 4, y + 22, x0, y + 22, col[c])
        b += text(x0 + v * sc + 8, y + 18, str(v), 13.5, 'start', 800, INK)
    # legenda
    b += rbox(700, 124, 180, 112, PANEL, rx=12)
    b += rbox(714, 140, 16, 16, ACC2, rx=3) + text(738, 153, 'struttura = 90 pt', 13, 'start', 800, INK)
    b += rbox(714, 170, 16, 16, OK, rx=3) + text(738, 183, 'punti "facili"', 13, 'start', 800, INK)
    b += rbox(714, 200, 16, 16, '#d9c3cb', rx=3) + text(738, 213, 'altri criteri', 13, 'start', 600, INK)
    b += text(20, 464, 'Ogni barra = punti assegnati da un giudice (10 giudici). Leggi sempre la scheda della tua categoria.', 13, 'start', 600, INK)
    b += text(880, 464, 'Fonte: scheda Nailympia 2026', 12, 'end', 600, MUTED)
    return svg(W, H, b, 'I punti della scheda French Twist 3-Shape Challenge 2026, giudice per giudice: la struttura vale 90 punti su 240')

@figx('gara-viste-giudice.svg')
def gara_viste():
    labels = ['Dall\'alto', 'Di profilo', 'A tunnel', 'Cuticola (lente)', 'Come la vede la modella']
    subs = ['forma, lati, simmetria', 'apex, archi, niente gobbe', 'curva C, "hair line"', 'nessuno scalino o taglio', 'forma uniforme anche così']
    pw, ph = 176, 262
    W = 20 + 5 * pw + 4 * 12 + 20
    b = T('Le 5 viste del giudice')
    for i, lab in enumerate(labels):
        x = 20 + i * (pw + 12)
        cx = x + pw / 2
        s = ''
        if i == 0:
            f, p = finger_nail(cx, 230, hw=26, nail_len=60, free_len=50, shape='squoval', smile=8, finger_len=40, lunula=False, plate='#f2c6d2')
            s += f
        elif i == 1:
            sp, pp = side_profile(x + 24, 180, w=140, stress=0.55, apex=0.42, apex_h=18, tip_h=4, root_h=2, gap=4, product='#f2c6d2')
            s += sp + circ(pp['ax'], pp['ah'], 4.5, ACC2, 'none', 0)
        elif i == 2:
            s += tip_view(cx, 170, w=120, curve=28, th=6, fill='#f2c6d2')
            s += leader(cx + 48, 158, cx - 6, 116, 'hair line', 'end', 12.5)
        elif i == 3:
            f, p = finger_nail(cx - 10, 250, hw=30, nail_len=80, free_len=20, shape='squoval', smile=8, finger_len=30, lunula=False, plate='#f2c6d2')
            s += f + magnifier(cx - 10, 224, 22)
        else:
            # mano vista dalla modella: dita verso l'osservatore (in basso), unghie di 4 dita
            s += hand_back(cx + 4, 278, 0.7, SKIN, ['#f2c6d2'] * 5)
        b += frame(x, 58, pw, ph, lab, i + 1, body=s, sub=subs[i], subcol=MUTED, tsize=13)
    return svg(W, 58 + ph + 18, arrow_defs() + b, 'Le cinque viste del giudice: dall\'alto, di profilo, a tunnel, la cuticola, il punto di vista della modella')


def led_lamp(cx, y, w=120):
    """Lampada UV/LED a cupola, vista 3/4: base, apertura scura, LED viola."""
    s = '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="#000" opacity=".12" filter="url(#dxBlurS)"/>' % (cx, y + 4, w * 0.56, 6)
    s += P('M%.1f,%.1f L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f Z' % (
        cx - w / 2, y, cx - w / 2, y - w * 0.32, cx - w / 2, y - w * 0.62, cx - w * 0.2, y - w * 0.7, cx, y - w * 0.7,
        cx + w * 0.2, y - w * 0.7, cx + w / 2, y - w * 0.62, cx + w / 2, y - w * 0.32, cx + w / 2, y), '#f7f5fa', '#8a7d9e', 1.8)
    s += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z' % (cx - w * 0.36, y, cx, y - w * 0.5, cx + w * 0.36, y, cx - w * 0.36, y), '#3a3046', 'none', 0)
    s += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z' % (cx - w * 0.36, y, cx, y - w * 0.5, cx + w * 0.36, y, cx - w * 0.36, y), 'url(#dxGlowUV)', 'none', 0)
    for k in range(5):
        s += circ(cx - w * 0.2 + k * w * 0.1, y - w * 0.33 + abs(k - 2) * w * 0.035, w * 0.018, '#c9a8ff', 'none', 0)
    s += P('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - w * 0.4, y - w * 0.4, cx - w * 0.3, y - w * 0.62, cx - w * 0.05, y - w * 0.66), 'none', '#fff', 3, ' opacity=".9"')
    s += rbox(cx + w * 0.3, y - w * 0.55, w * 0.1, w * 0.05, '#c9b8e6', 'none', 0, 2)
    s += rbox(cx - w / 2 - 4, y - 2, w + 8, 7, '#8a7d9e', 'none', 0, 3)
    return s


def applicator(x, y, ang=0, s=1.0, powder=True):
    """Applicatore a spugnetta per polveri: manico + punta ovale porosa (setole verso il basso)."""
    b = rbox(-4, -64, 8, 52, '#4b3a40', 'none', 0, 4) + rbox(-2.5, -60, 2, 44, '#fff', 'none', 0, 1, ' opacity=".25"')
    b += '<ellipse cx="0" cy="-4" rx="11" ry="15" fill="#e7e2dc" stroke="#a49c94" stroke-width="1.2"/>'
    b += '<ellipse cx="0" cy="-4" rx="11" ry="15" fill="url(#dxPore)"/>'
    if powder:
        b += '<ellipse cx="0" cy="4" rx="9" ry="7" fill="url(#dxChrome)" opacity=".9"/>'
    return g(b, x, y, ang, s)

def powder_jar(x, y, s=1.0):
    b = '<ellipse cx="0" cy="14" rx="20" ry="5" fill="#000" opacity=".12"/>'
    b += rbox(-18, -6, 36, 20, '#f4f1f8', '#9a948d', 1.4, 5)
    b += '<ellipse cx="0" cy="-6" rx="18" ry="5" fill="url(#dxChrome)" stroke="#9a948d" stroke-width="1.2"/>'
    return g(b, x, y, 0, s)

def dust_brush(x, y, ang=0, s=1.0):
    """Pennello da polvere (setole morbide a ventaglio)."""
    b = rbox(-4, -70, 8, 46, '#e9dfd4', '#b8a796', 1, 4) + rbox(-6, -26, 12, 12, '#c9cdd3', GREY_D, 1, 2)
    b += P('M-6,-14 C-18,-4 -20,14 -14,22 L14,22 C20,14 18,-4 6,-14 Z', '#f6efe6', '#c9b9a5', 1.2)
    for k in range(-12, 13, 4):
        b += ln(k * 0.4, -12, k, 21, '#d8c8b3', 0.8)
    return g(b, x, y, ang, s)

def bar_magnet(x, y, w=44, h=18, ang=0):
    gid = uid('mg')
    b = '<defs>%s</defs>' % _lg(gid, [(0, '#fff', .45), (.5, '#fff', 0), (1, '#000', .2)], 0, 1)
    b += rbox(-w / 2, -h / 2, w / 2, h, '#d64545', '#4b3a40', 1.3, 3) + rbox(0, -h / 2, w / 2, h, '#3f6fc4', '#4b3a40', 1.3, 3)
    b += rbox(-w / 2, -h / 2, w, h, 'url(#%s)' % gid, 'none', 0, 3)
    b += text(-w / 4, h * 0.27, 'N', 11, weight=800, fill='#fff') + text(w / 4, h * 0.27, 'S', 11, weight=800, fill='#fff')
    return g(b, x, y, ang)

def sponge(x, y, w=44, h=56, cols=None, ang=0, face='#fbf6f0'):
    """Spugnetta da trucco (blocchetto poroso), faccia di lavoro in basso; cols = due colori caricati."""
    b = '<ellipse cx="0" cy="%.1f" rx="%.1f" ry="4" fill="#000" opacity=".1"/>' % (h / 2 + 4, w / 2)
    b += rbox(-w / 2, -h / 2, w, h, face, '#c9c0b8', 1.4, 7)
    b += P('M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (-w / 2, -h / 2 + 6, -w / 2 + 6, -h / 2, w / 2, -h / 2, w / 2 - 6, -h / 2 + 6), '#fff', 'none', 0, ' opacity=".6"')
    if cols:
        b += rbox(-w / 2, h / 2 - 16, w / 2 + 2, 16, cols[0], 'none', 0, 4) + rbox(-1, h / 2 - 16, w / 2 + 1, 16, cols[1], 'none', 0, 4)
        gid = uid('sp')
        b += '<defs>%s</defs>' % _lg(gid, [(0, cols[0], 0), (.42, cols[0], 0), (.5, mix(cols[0], cols[1], .5), 1), (.58, cols[1], 0), (1, cols[1], 0)])
        b += rbox(-w / 2, h / 2 - 16, w, 16, 'url(#%s)' % gid, 'none', 0, 4)
    b += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="7" fill="url(#dxPore)"/>' % (-w / 2, -h / 2, w, h)
    return g(b, x, y, ang)


def glitter_fx(cx, by, w, h, n=18, seed=4, sizes=(2.5, 5.5), cols=('#d4af37', '#8e24aa', '#1e88e5', '#e53935', '#c0c6cc')):
    import random as _r
    rnd = _r.Random(seed)
    s = ''
    for j in range(n):
        hx, hy = cx + rnd.uniform(-w * 0.42, w * 0.42), by - rnd.uniform(h * 0.06, h * 0.94)
        r = rnd.uniform(*sizes)
        c = cols[j % len(cols)]
        rot = rnd.uniform(0, 60)
        pts = ' '.join('%.1f,%.1f' % (hx + r * math.cos(math.radians(60 * q + rot)), hy + r * math.sin(math.radians(60 * q + rot))) for q in range(6))
        s += '<polygon points="%s" fill="%s" stroke="%s" stroke-width=".6" clip-path="url(#CLIP)"/>' % (pts, c, dark(c, .3))
        s += '<polygon points="%s" fill="#fff" opacity=".55" clip-path="url(#CLIP)"/>' % ' '.join(
            '%.1f,%.1f' % (hx + r * 0.55 * math.cos(math.radians(60 * q + rot)) - r * 0.25, hy + r * 0.55 * math.sin(math.radians(60 * q + rot)) - r * 0.25) for q in (3, 4, 5))
    return s


def shimmer_fx(cx, by, w, h, tint='#ffffff'):
    gid = uid('sh')
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#dxShim)" clip-path="url(#CLIP)"/>' % (cx - w / 2, by - h - 2, w, h + 10)
    s += '<defs><radialGradient id="%s" cx=".35" cy=".35" r=".6">%s</radialGradient></defs>' % (gid, _stop(0, tint, .55) + _stop(1, tint, 0))
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#%s)" clip-path="url(#CLIP)"/>' % (cx - w / 2, by - h - 2, w, h + 10, gid)
    return s


def num_badge(x, y, n, r=11, col=ACC):
    return circ(x, y, r, col, '#fff', 2, ' filter="url(#nxShS)"') + text(x, y + 4.3, str(n), 12.5, weight=800, fill='#fff')

def timer_icon(x, y, s=1.0):
    """Timer da cucina/cronometro."""
    b = circ(0, 4, 20, '#fff', '#4b3a40', 2.5) + rbox(-5, -24, 10, 7, '#4b3a40', 'none', 0, 2) + rbox(-2, -18, 4, 4, '#4b3a40', 'none', 0, 1)
    b += P('M0,4 L0,-9', 'none', ACC, 2.5) + P('M0,4 L9,8', 'none', '#4b3a40', 2)
    for k in range(12):
        a = math.radians(k * 30)
        b += ln(15 * math.cos(a), 4 + 15 * math.sin(a), 17.5 * math.cos(a), 4 + 17.5 * math.sin(a), '#8a7d74', 1.2)
    return g(b, x, y, 0, s)

def main():
    for name, f in MINE.items():
        with open(os.path.join(OUT, name), 'w', encoding='utf-8') as fh:
            fh.write(f())
    print('Gruppo D: %d illustrazioni' % len(MINE))


if __name__ == '__main__':
    main()
