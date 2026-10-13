#!/usr/bin/env python3
"""Illustrazioni del gruppo D (moduli onicofagia, cover-colori, piedi, arte-gare). Uso: python3 tools/svg_d.py"""
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
    """Mano vista dal dorso, dita in alto. by = polso. nails = lista di 5 colori (pollice→mignolo) o None."""
    nails = nails or [NAT] * 5
    out = ''
    # dita: (dx, lunghezza, larghezza, angolo)
    fingers = [(-58, 70, 26, -38), (-30, 112, 24, -8), (0, 124, 25, 0), (28, 112, 24, 7), (52, 86, 21, 16)]
    for k, (dx, L, w, ang) in enumerate(fingers):
        ang *= spread
        base_y = -88 if k else -44
        fx = dx if k else -54
        body = rbox(-w / 2, -L, w, L + 20, skin, SKIN_D, 1.4, int(w / 2))
        body += nail_shape(0, -L + w * 0.95, w * 0.62, w * 0.8, nails[k], NAIL_S, 1.2)
        out += g(body, fx, base_y, ang)
    out += P('M-62,0 L-66,-60 Q-64,-104 -20,-108 L40,-106 Q66,-100 68,-70 L62,0 Z', skin, SKIN_D, 1.4)
    out += P('M-40,-96 Q0,-101 44,-94', 'none', SKIN_D, 1, ' opacity=".5"')
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
            s += text(cx + 88, ys + 4, '1 centro', 12.5, 'start', 700, ACC2)
            s += text(cx + 88, ys + 22, '2–3 angoli', 12.5, 'start', 700, ACC2)
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
            n, ys = french_nail(cx, by, 74, 170, cov_top=0.95, sc=6, sw=None, win=(k == 1))
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
    """Interno del polso con vene. vein: colore (o tupla per vene miste)."""
    b = rbox(-40, -70, 80, 140, skin, SKIN_D, 1.4, 30)
    b += P('M-40,-30 Q0,-40 40,-30', 'none', SKIN_D, 1, ' opacity=".6"')
    vs = vein if isinstance(vein, tuple) else (vein, vein, vein)
    paths = ['M-18,60 Q-24,20 -14,-10 Q-6,-40 -12,-66', 'M4,64 Q10,24 2,-8 Q-4,-36 6,-66', 'M22,60 Q16,30 22,0']
    for k, d in enumerate(paths):
        b += P(d, 'none', vs[k], 3.2)
    return g(b, cx, cy, 0, s)


@figx('sottotono-test.svg')
def sottotono():
    W, H = 900, 380
    b = T('Capire il sottotono: tre test')
    b += sun(860, 30, 11) + text(834, 36, 'luce naturale', 14, 'end', 700, '#9a6a00')
    pw = 280
    # 1 vene
    x = 20
    body = wrist(x + 80, 158, '#5b7fc7', 0.72)
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
    W, H = 860, 380
    b = T('Pigmenti e luce: l\'effetto ombrello')
    b += g(lamp(0, 0, 300), 430, 124, 0, 1.0)
    items = [('Sottile, chiaro', '#f7d3dc', 1.0, 30, False, True, 'indurito fino in fondo'),
             ('Sottile, scuro', '#a3263f', 0.9, 30, False, True, 'ok con tempi da scheda'),
             ('Spesso, scuro', '#a3263f', 0.45, 78, True, False, 'sotto: non polimerizzato')]
    for k, (t, col, pen, th, soft, ok, sub) in enumerate(items):
        x = 40 + k * 270
        cx = x + 110
        base = 300
        b += rbox(x, base, 220, 10, NAT, NAIL_S, 1.2, 3)
        b += rbox(x + 20, base - th, 180, th, col, NAIL_S, 1.2, 4)
        if soft:
            pid = uid('hatch')
            b += ('<defs><pattern id="%s" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
                  '<rect width="10" height="10" fill="#f6c58f"/><line x1="0" y1="0" x2="0" y2="10" stroke="#e08a2c" stroke-width="4"/></pattern></defs>') % pid
            b += '<rect x="%d" y="%d" width="180" height="%d" fill="url(#%s)"/>' % (x + 20, base - th / 2, th / 2, pid)
            b += rbox(x + 20, base - th, 180, th, 'none', NAIL_S, 1.2, 4)
            for j in range(5):
                ux, uy = x + 40 + j * 35, base - th + 14
                b += P('M%.1f,%.1f a9,7 0 0 1 18,0 Z' % (ux - 9, uy), '#3b2a30', 'none', 0) + ln(ux, uy, ux, uy + 9, '#3b2a30', 1.5)
        else:
            for j in range(10):
                b += circ(x + 32 + j * 17, base - th / 2 + (j % 2) * 6 - 3, 2.2, '#fff' if k == 0 else '#5c0f22', 'none', 0, ' opacity=".7"')
        for j in range(4):
            ax = x + 50 + j * 40
            y_end = base - th + th * pen - 4 if k < 2 else base - th + th * pen
            b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="3" marker-end="url(#uvm)"/>' % (ax, 150, ax, y_end, UV)
        b += mark(x + 196, base - th - 18, ok, 12)
        b += text(cx, base + 34, t, 15, weight=800)
        b += text(cx, base + 54, sub, 13, weight=700, fill=OK if ok else ERR)
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
    W, H = 860, 290
    b = T('Le finiture')
    names = ['coprente', 'jelly', 'shimmer', 'glitter', 'magnetico']
    subs = ['copre in 1–2 strati', 'traslucido', 'perlato fine', 'particelle grandi', 'cat-eye']
    for k, n in enumerate(names):
        x = 20 + k * 166
        cx, by = x + 78, 220
        b += rbox(x, 58, 156, 216)
        if k == 0:
            s = nail_shape(cx, by, 64, 130, '#c62f4a', '#7a1a2b', 1.6) + gloss(cx, by, 130)
        elif k == 1:
            ext = ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="#3b2a30" stroke-width="3" fill="none" clip-path="url(#CLIP)"/>'
                   % (cx - 30, by - 40, cx, by - 90, cx + 30, by - 50))
            ext += '<rect x="%.1f" y="%.1f" width="70" height="140" fill="#d42c4c" opacity=".45" clip-path="url(#CLIP)"/>' % (cx - 35, by - 136)
            s = nail_shape(cx, by, 64, 130, '#fbeef1', '#b0485d', 1.6, ext) + gloss(cx, by, 130)
        elif k == 2:
            ext = ''.join(circ(cx - 26 + (j * 13) % 54, by - 12 - (j * 23) % 110, 1.3, '#fff', 'none', 0) for j in range(40))
            s = nail_shape(cx, by, 64, 130, '#e79ab2', '#b0485d', 1.6, ext)
        elif k == 3:
            ext = ''
            cols = ['#d4af37', '#8e24aa', '#1e88e5', '#e53935', '#c0c6cc']
            for j in range(16):
                hx, hy = cx - 24 + (j * 17) % 50, by - 16 - (j * 29) % 108
                r = 4.5
                pts = ' '.join('%.1f,%.1f' % (hx + r * math.cos(math.radians(60 * q)), hy + r * math.sin(math.radians(60 * q))) for q in range(6))
                ext += '<polygon points="%s" fill="%s" clip-path="url(#CLIP)"/>' % (pts, cols[j % 5])
            s = nail_shape(cx, by, 64, 130, '#f4f7fa', '#9aa3ad', 1.6, ext)
        else:
            gid = uid('mg')
            ext = ('<defs><linearGradient id="%s" x1="0" y1="1" x2="1" y2="0"><stop offset=".3" stop-color="#1b1b22"/>'
                   '<stop offset=".5" stop-color="#d9d6ff"/><stop offset=".7" stop-color="#1b1b22"/></linearGradient></defs>'
                   '<rect x="%.1f" y="%.1f" width="70" height="140" fill="url(#%s)" clip-path="url(#CLIP)"/>') % (gid, cx - 35, by - 136, gid)
            s = nail_shape(cx, by, 64, 130, '#1b1b22', '#000', 1.6, ext)
        b += s
        b += text(cx, 244, n, 15, weight=800)
        b += text(cx, 262, subs[k], 12.5, weight=600, fill=MUTED)
    return svg(W, H, b, 'Le finiture dei colori: coprente, jelly, shimmer, glitter e magnetico')


@figx('cartella-colori.svg')
def cartella():
    W, H = 860, 390
    b = T('La cartella campioni')
    fam = [('nude/cover', ['#f4ddd2', '#ecc4b4', '#d9a28c', '#a8705a']),
           ('rosa', ['#fbd5df', '#f3a6bd', '#e46f93', '#b8406a']),
           ('rossi', ['#f28b82', '#e53935', '#b71c1c', '#6d1020']),
           ('viola/blu', ['#c9b6e4', '#8e6cc4', '#3f51b5', '#1a237e']),
           ('verdi', ['#c8e6c9', '#81c784', '#388e3c', '#1b4d2a']),
           ('scuri', ['#bdb6b3', '#7d716d', '#4a3f3c', '#1d1717']),
           ('effetti', ['glitter', 'chrome', 'cat', 'shimmer'])]
    b += rbox(20, 58, 700, 314)
    for c, (name, cols) in enumerate(fam):
        x = 30 + c * 92
        b += ftext(x + 34, 84, name, 13.5, 88, weight=800)
        for r, col in enumerate(cols):
            by = 150 + r * 64
            if col == 'glitter':
                ext = ''.join(circ(x + 22 + (j * 7) % 26, by - 8 - (j * 13) % 40, 2, ['#d4af37', '#e53935', '#1e88e5'][j % 3], 'none', 0) for j in range(10))
                b += nail_shape(x + 34, by, 30, 54, '#f7f4ef', '#b9ab98', 1.2, ext)
            elif col == 'chrome':
                gid = uid('cr')
                ext = ('<defs><linearGradient id="%s" x1="0" x2="1"><stop offset="0" stop-color="%s"/><stop offset=".5" stop-color="%s"/>'
                       '<stop offset="1" stop-color="%s"/></linearGradient></defs><rect x="%.1f" y="%.1f" width="40" height="60" fill="url(#%s)" clip-path="url(#CLIP)"/>'
                       % (gid, CHROME[0], CHROME[1], CHROME[2], x + 14, by - 58, gid))
                b += nail_shape(x + 34, by, 30, 54, '#ccc', '#8a8f99', 1.2, ext)
            elif col == 'cat':
                ext = '<rect x="%.1f" y="%.1f" width="6" height="70" fill="#d9d6ff" opacity=".85" transform="rotate(25 %.1f %.1f)" clip-path="url(#CLIP)"/>' % (x + 31, by - 62, x + 34, by - 27)
                b += nail_shape(x + 34, by, 30, 54, '#1b1b22', '#000', 1.2, ext)
            elif col == 'shimmer':
                ext = ''.join(circ(x + 22 + (j * 7) % 26, by - 8 - (j * 13) % 40, 1, '#fff', 'none', 0) for j in range(18))
                b += nail_shape(x + 34, by, 30, 54, '#d98aa8', '#a0506c', 1.2, ext)
            else:
                b += nail_shape(x + 34, by, 30, 54, col, '#9b8a86', 1.2)
    b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2.4" marker-end="url(#ar)"/>' % (692, 112, 692, 338, ACC2)
    b += text(692, 104, 'chiaro', 12.5, 'middle', 700, ACC2)
    b += text(692, 360, 'scuro', 12.5, 'middle', 700, ACC2)
    # retro del tip
    b += rbox(734, 58, 106, 314, '#fff', '#e5d6d2', 1.5, 14)
    b += text(787, 84, 'il retro', 14, weight=800)
    b += nail_shape(787, 260, 70, 150, '#fbf7f2', '#b9ab98', 1.6)
    b += mtext(787, 172, ['marca', 'nome', 'n° 112'], 14, weight=600, fill='#3a5a9a', lh=1.4)
    b += text(787, 300, 'scritto a', 12.5, weight=600, fill=MUTED)
    b += text(787, 316, 'pennarello', 12.5, weight=600, fill=MUTED)
    return svg(W, H, arrow_defs() + b, 'Cartella colori ordinata per famiglie, dal chiaro allo scuro, con marca, nome e numero sul retro')


@figx('armonie-colore.svg')
def armonie():
    W, H = 900, 320
    b = T('Abbinamenti facili')
    items = [('Monocromatico', [8], ['#90caf9', '#42a5f5', '#1565c0', '#42a5f5', '#90caf9'], None),
             ('Analoghi', [11, 0, 1], ['#f48fb1', '#ff8a65', '#ffb74d', '#ff8a65', '#f48fb1'], None),
             ('Complementari', [8, 2], ['#1e5bb8', '#1e5bb8', '#1e5bb8', 'acc', '#1e5bb8'], '#fb8c00'),
             ('Neutro + accento', [], ['#e9c7b8', '#e9c7b8', '#e9c7b8', 'chrome', '#e9c7b8'], None)]
    for k, (t, hl, cols, acc) in enumerate(items):
        x = 20 + k * 218
        b += rbox(x, 58, 208, 248)
        b += text(x + 104, 86, t, 15, weight=800)
        if hl:
            b += color_wheel(x + 104, 140, 40, hl)
        else:
            b += circ(x + 82, 140, 30, '#e9c7b8', '#c9a898', 1.5)
            gid = uid('cr')
            b += ('<defs><linearGradient id="%s" x1="0" x2="1"><stop offset="0" stop-color="%s"/><stop offset=".5" stop-color="%s"/>'
                  '<stop offset="1" stop-color="%s"/></linearGradient></defs>') % (gid, CHROME[0], CHROME[1], CHROME[2])
            b += circ(x + 138, 140, 18, 'url(#%s)' % gid, '#8a8f99', 1.5)
            b += text(x + 113, 146, '+', 18, weight=800)
            b += text(x + 104, 196, 'nude + 1 effetto', 12.5, weight=600, fill=MUTED)
        for j, c in enumerate(cols):
            nx = x + 30 + j * 37
            hh = [52, 64, 70, 64, 48][j]
            by = 290 - [8, 0, -4, 0, 10][j]
            if c == 'acc':
                ext = '<rect x="%.1f" y="%.1f" width="40" height="22" fill="%s" clip-path="url(#CLIP)"/>' % (nx - 20, by - hh - 2, acc)
                b += nail_shape(nx, by, 28, hh, '#1e5bb8', '#123d7a', 1.2, ext)
            elif c == 'chrome':
                gid = uid('cr')
                ext = ('<defs><linearGradient id="%s" x1="0" x2="1"><stop offset="0" stop-color="%s"/><stop offset=".5" stop-color="%s"/>'
                       '<stop offset="1" stop-color="%s"/></linearGradient></defs><rect x="%.1f" y="%.1f" width="40" height="80" fill="url(#%s)" clip-path="url(#CLIP)"/>'
                       % (gid, CHROME[0], CHROME[1], CHROME[2], nx - 20, by - hh - 4, gid))
                b += nail_shape(nx, by, 28, hh, '#ccc', '#8a8f99', 1.2, ext)
            else:
                b += nail_shape(nx, by, 28, hh, c, '#7d6a70', 1.2)
    return svg(W, H, b, 'Abbinamenti facili per nail art: monocromatico, analoghi, complementari, neutro più accento')


def main():
    for name, f in MINE.items():
        with open(os.path.join(OUT, name), 'w', encoding='utf-8') as fh:
            fh.write(f())
    print('Gruppo D: %d illustrazioni' % len(MINE))


if __name__ == '__main__':
    main()
