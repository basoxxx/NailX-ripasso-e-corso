#!/usr/bin/env python3
"""Illustrazioni del gruppo B (moduli preparazione, tip, cartina, limatura). Uso: python3 tools/svg_b.py"""
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
PROD = '#d6ebf6'      # prodotto (gel/acrilico trasparente) in sezione
PROD_S = '#7fb0cc'
TIPC, TIP_S = '#f3eee6', '#b9ab98'   # plastica del tip
FORM, FORM_S = '#f6e7a8', '#d8c26a'  # cartina
YEL = '#f1d27a'
SKIN_RED = '#f2a7a0'
LIGHT = '#f5c542'
GREY = '#9aa3ad'
GREY_D = '#6f7983'


# ================================================================= primitive di supporto
def frame(x, y, w, h, title, num=None, ok=None, sub=None, sub2=None, body='', subcol=None, tsize=None):
    """Pannello con titolo, contenuto ritagliato, segno ✓/✗ e didascalia in basso."""
    pc = uid('k')
    s = '<defs><clipPath id="%s"><rect x="%d" y="%d" width="%d" height="%d" rx="16"/></clipPath></defs>' % (pc, x, y, w, h)
    s += '<rect x="%d" y="%d" width="%d" height="%d" rx="16" fill="%s"/>' % (x, y, w, h, PANEL)
    s += '<g clip-path="url(#%s)">%s</g>' % (pc, body)
    if num is not None:
        avail = w - 47 - (34 if ok is not None else 10)
        ts = max(12.5, min(tsize or 15, avail / (0.58 * max(1, len(title)))))
        s += '<circle cx="%d" cy="%d" r="14" fill="%s"/>' % (x + 25, y + 25, ACC2)
        s += text(x + 25, y + 30.5, str(num), 15, weight=800, fill='#fff')
        s += text(x + 47, y + 30, title, '%.1f' % ts, 'start', 700)
    elif title:
        avail = w - (64 if ok is not None else 20)
        ts = max(12.5, min(tsize or 15.5, avail / (0.58 * max(1, len(title)))))
        s += text(x + w / 2 - (14 if ok is not None else 0), y + 30, title, '%.1f' % ts, weight=700)
    if ok is not None:
        s += mark(x + w - 24, y + 25, ok, 13)
    if sub:
        yy = y + h - (34 if sub2 else 16)
        s += text(x + w / 2, yy, sub, 13, weight=700, fill=subcol or (OK if ok else ERR if ok is False else INK))
    if sub2:
        s += text(x + w / 2, y + h - 15, sub2, 12.5, fill=MUTED, style='italic')
    return s


def stop_sign(x, y, r=14):
    return ('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#fff" stroke="%s" stroke-width="%.1f"/>'
            '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.1f"/>'
            % (x, y, r, ERR, r * 0.28, x - r * 0.68, y - r * 0.68, x + r * 0.68, y + r * 0.68, ERR, r * 0.28))


def warn_tri(x, y, s=1.0, col=WARN):
    return ('<g transform="translate(%.1f,%.1f) scale(%.2f)"><path d="M0,-13 L13,10 L-13,10 Z" fill="%s" stroke="%s" stroke-width="1.5" stroke-linejoin="round"/>'
            '<rect x="-1.6" y="-5" width="3.2" height="8" rx="1.4" fill="#fff"/><circle cx="0" cy="6.3" r="1.7" fill="#fff"/></g>'
            % (x, y, s, col, col))


def excl(x, y, r=13, col=WARN):
    return ('<circle cx="%.1f" cy="%.1f" r="%d" fill="%s"/>' % (x, y, r, col)
            + text(x, y + 5.5, '!', 16, weight=900, fill='#fff'))


def sign(x, y, w, s, h=34):
    return ('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" rx="8" fill="#fff3c4" stroke="%s" stroke-width="1.5"/>'
            % (x, y, w, h, '#d9b44a') + text(x + w / 2, y + h / 2 + 5, s, 14, weight=800, fill='#7a5a12'))


def eye(x, y, ang=0, s=1.0):
    """Occhio stilizzato che guarda nella direzione ang (gradi, 0 = verso destra)."""
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f) scale(%.2f)">'
            '<path d="M-14,0 Q0,-11 14,0 Q0,11 -14,0 Z" fill="#fff" stroke="%s" stroke-width="2"/>'
            '<circle cx="2" cy="0" r="4.6" fill="%s"/><circle cx="3.4" cy="-1.4" r="1.4" fill="#fff"/></g>'
            % (x, y, ang, s, INK, ACC2))


def dim(x1, y1, x2, y2, label, side='above', col=ACC2, size=13, off=0):
    """Quota con frecce alle due estremità."""
    s = arrow(x1, y1, x2, y2, col if col == ACC2 else MUTED, 1.5, True)
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    if side == 'above':
        s += text(mx, my - 7 - off, label, size, weight=700, fill=col)
    elif side == 'below':
        s += text(mx, my + 17 + off, label, size, weight=700, fill=col)
    elif side == 'right':
        s += text(mx + 8 + off, my + 5, label, size, 'start', 700, col)
    else:
        s += text(mx - 8 - off, my + 5, label, size, 'end', 700, col)
    return s


def scaled(x, y, s, body):
    return '<g transform="translate(%.1f,%.1f) scale(%.3f)">%s</g>' % (x, y, s, body)


def rot(ang, cx, cy, body):
    return '<g transform="rotate(%.1f %.1f %.1f)">%s</g>' % (ang, cx, cy, body)


def dashed(x1, y1, x2, y2, col=ACC2, w=1.6, dash='6 5'):
    return '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s" stroke-dasharray="%s"/>' % (
        x1, y1, x2, y2, col, w, dash)


def arc_angle(cx, cy, r, a0, a1, label, col=ACC2, lx=None, ly=None, size=13):
    """Archetto d'angolo tra a0 e a1 (gradi, 0 = destra, positivi verso il basso come in SVG)."""
    p0 = (cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0)))
    p1 = (cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1)))
    sweep = 1 if a1 > a0 else 0
    s = '<path d="M%.1f,%.1f A%.1f,%.1f 0 0 %d %.1f,%.1f" fill="none" stroke="%s" stroke-width="1.8" stroke-dasharray="3 3"/>' % (
        p0[0], p0[1], r, r, sweep, p1[0], p1[1], col)
    if label:
        am = math.radians((a0 + a1) / 2)
        tx = lx if lx is not None else cx + (r + 16) * math.cos(am)
        ty = ly if ly is not None else cy + (r + 16) * math.sin(am) + 5
        s += text(tx, ty, label, size, weight=800, fill=col)
    return s


# ---------------------------------------------------------------- dita e sezioni
def top_finger(cx, yc, **kw):
    """finger_nail con valori di default comodi per i pannelli."""
    d = dict(hw=36, nail_len=120, free_len=14, shape='tonda', smile=8, finger_len=40)
    d.update(kw)
    return finger_nail(cx, yc, **d)


def finger_side(x, y, L=170, free=0, plate=True, free_col=FREE, tip_down=0):
    """Dito di profilo, punta verso destra. x = eponichio, y = superficie della lamina, L = lunghezza del letto."""
    xe = x + L
    s = ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f '
         'C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
         % (x - 110, y - 14, x - 8, y - 14, x + 6, y - 14, x + 10, y - 2, xe, y + 5,
            xe + 26, y + 10, xe + 30, y + 52, xe + 2, y + 70, xe - 20, y + 80, x - 60, y + 80, x - 110, y + 80, SKIN, SKIN_D))
    if plate:
        s += ('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.4"/>'
              % (x + 4, y, xe, y + 1, xe, y + 6, x + 6, y + 5, NAIL, NAIL_S))
        if free:
            s += ('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.4"/>'
                  % (xe, y + 1, xe + free, y + 1 + tip_down, xe + free, y + 6 + tip_down, xe, y + 6, free_col, NAIL_S))
        # piega dell'eponichio sopra l'inizio della lamina
        s += ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.3"/>'
              % (x - 40, y - 14, x - 8, y - 14, x + 8, y - 14, x + 12, y - 1, x - 40, y - 1, SKIN, SKIN_D))
    return s


def cuticle_section(x, y, w, cut=True, flap=False):
    """Sezione ingrandita della zona cuticolare (eponichio a sinistra, punta a destra). y = superficie lamina."""
    ex = x + 40
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (x - 10, y + 12, w + 20, 90, '#f0c3ad')
    s += ('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
          % (ex - 40, y, x + w + 10, y, x + w + 10, y + 12, ex - 40, y + 12, NAIL, NAIL_S))
    s += ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
          % (x - 10, y - 46, ex, y - 46, ex + 34, y - 44, ex + 38, y - 1, x - 10, y - 1, SKIN, SKIN_D))
    if cut:
        s += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="#fffaf6" stroke="#cdb7ad" stroke-width="1.2" opacity=".95"/>'
              % (ex + 30, y - 1, ex + 60, y - 6, ex + 92, y - 1.5, ex + 92, y, ex + 60, y - 1, ex + 30, y))
    if flap:
        s += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="#fff4ee" stroke="#cdb7ad" stroke-width="1.2"/>'
              % (ex + 30, y - 22, ex + 50, y - 40, ex + 62, y - 30, ex + 50, y - 30, ex + 34, y - 16))
    return s, dict(ex=ex, fold_x=ex + 38)


# ---------------------------------------------------------------- strumenti aggiuntivi
def tool_curette(x, y, ang=0, l=130):
    """Curette: punta (cucchiaino) in (x, y), manico verso +x prima della rotazione."""
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f)"><rect x="14" y="-4" width="%d" height="8" rx="4" fill="%s"/>'
            '<path d="M16,-3 L4,-2 Q-6,-6 -10,0 Q-6,6 4,2 L16,3 Z" fill="%s" stroke="#5d666f" stroke-width="1"/></g>'
            % (x, y, ang, l, GREY, GREY_D))


def tool_nipper(x, y, ang=0, s=1.0):
    """Tronchesina: becco in (x, y), manici verso +x."""
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f) scale(%.2f)">'
            '<path d="M0,0 L22,-7 L30,-3 L8,2 Z" fill="%s"/><path d="M0,1 L22,9 L30,5 L8,0 Z" fill="%s"/>'
            '<circle cx="30" cy="1" r="5" fill="%s"/>'
            '<path d="M32,-3 Q70,-26 110,-24 L112,-17 Q74,-16 34,3 Z" fill="%s"/>'
            '<path d="M32,5 Q70,28 110,26 L112,19 Q74,18 34,0 Z" fill="%s"/></g>'
            % (x, y, ang, s, GREY, GREY_D, GREY_D, GREY, GREY_D))


def tool_tipcutter(x, y, ang=0, s=1.0):
    """Tagliatip: lama dritta in (x, y)."""
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f) scale(%.2f)">'
            '<rect x="-6" y="-30" width="12" height="60" rx="3" fill="%s"/>'
            '<rect x="-2" y="-30" width="3" height="60" fill="#e8edf2"/>'
            '<path d="M6,-26 L60,-34 L64,-24 L10,-12 Z" fill="%s"/>'
            '<path d="M6,26 L60,34 L64,24 L10,12 Z" fill="%s"/>'
            '<path d="M58,-26 q10,26 0,52" stroke="%s" stroke-width="3" fill="none"/></g>'
            % (x, y, ang, s, GREY_D, GREY, GREY, MUTED))


def tool_scissors(x, y, ang=0, s=1.0):
    """Forbicine: punte in (x, y), anelli verso +x."""
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f) scale(%.2f)">'
            '<path d="M0,-2 L36,-6 L38,0 Z" fill="%s"/><path d="M0,2 L36,6 L38,0 Z" fill="%s"/>'
            '<circle cx="37" cy="0" r="3" fill="%s"/>'
            '<path d="M38,-4 L52,-12" stroke="%s" stroke-width="4"/><path d="M38,4 L52,12" stroke="%s" stroke-width="4"/>'
            '<circle cx="60" cy="-15" r="9" fill="none" stroke="%s" stroke-width="4"/>'
            '<circle cx="60" cy="15" r="9" fill="none" stroke="%s" stroke-width="4"/></g>'
            % (x, y, ang, s, GREY, GREY_D, INK, ACC2, ACC2, ACC2, ACC2))


def tool_pencil(x, y, ang=0, l=110):
    """Matita: punta in (x, y)."""
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f)"><path d="M0,0 L16,-6 L16,6 Z" fill="#e8c9a0"/>'
            '<path d="M0,0 L6,-2.3 L6,2.3 Z" fill="%s"/><rect x="16" y="-6" width="%d" height="12" fill="#f0b43c"/>'
            '<rect x="%d" y="-6" width="12" height="12" rx="2" fill="#e88a9c"/></g>' % (x, y, ang, INK, l, 16 + l))


def bottle(cx, yb, liquid='#cfe6f7', label='', w=40, h=56):
    """Flaconcino con tappo-pennello; yb = base."""
    s = ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="9" fill="#fff" stroke="%s" stroke-width="1.6"/>'
         % (cx - w / 2, yb - h, w, h, MUTED))
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="6" fill="%s"/>' % (cx - w / 2 + 4, yb - h * 0.62, w - 8, h * 0.62 - 4, liquid)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="%s"/>' % (cx - w * 0.22, yb - h - 26, w * 0.44, 26, INK)
    if label:
        s += text(cx, yb - h * 0.25, label, 12, weight=800, fill=INK)
    return s


def drop_c(cx, cy, col, stroke=None, s=1.0):
    return ('<path d="M%.1f,%.1f q%.1f,%.1f 0,%.1f q%.1f,%.1f 0,%.1f z" fill="%s" stroke="%s"/>'
            % (cx, cy - 10 * s, 8 * s, 12 * s, 19 * s, -8 * s, -7 * s, -19 * s, col, stroke or col))


def desk_lamp(x, y, s=1.0):
    """Lampada da tavolo; (x, y) = centro della testa (luce verso destra/basso)."""
    return ('<g transform="translate(%.1f,%.1f) scale(%.2f)">'
            '<rect x="-48" y="96" width="44" height="8" rx="4" fill="%s"/>'
            '<path d="M-26,96 L-36,40 L0,0" stroke="%s" stroke-width="5" fill="none" stroke-linecap="round"/>'
            '<path d="M-10,-14 L24,-6 L16,24 Z" fill="%s"/><circle cx="16" cy="10" r="5" fill="%s"/></g>'
            % (x, y, s, INK, MUTED, ACC2, LIGHT))


def rays(x0, y0, x1, y1, n=4, dx=0, dy=22, col=LIGHT):
    s = ''
    for k in range(n):
        s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2.5" stroke-linecap="round" opacity=".85"/>' % (
            x0 + k * dx, y0 + k * dy, x1 + k * dx, y1 + k * dy, col)
    return s


def thumb(x, y, ang=0, s=1.0):
    """Pollice stilizzato: polpastrello in (x, y), dito verso +y prima della rotazione."""
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f) scale(%.2f)">'
            '<path d="M-18,70 L-18,0 Q-18,-20 0,-20 Q18,-20 18,0 L18,70 Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
            '<path d="M-10,-8 Q0,-16 10,-8 L10,8 Q0,12 -10,8 Z" fill="%s" stroke="%s" stroke-width="1" opacity=".8"/></g>'
            % (x, y, ang, s, SKIN, SKIN_D, NAIL, NAIL_S))


def mini_hand(cx, cy, s=1.0):
    """Mano aperta stilizzata (palmo verso l'osservatore)."""
    b = '<rect x="-22" y="-6" width="44" height="46" rx="14" fill="%s" stroke="%s" stroke-width="1.5"/>' % (SKIN, SKIN_D)
    for k, (fx, fh) in enumerate([(-17, 30), (-6, 38), (5, 36), (16, 28)]):
        b += '<rect x="%d" y="%d" width="10" height="%d" rx="5" fill="%s" stroke="%s" stroke-width="1.5"/>' % (fx - 4, -fh + 4, fh, SKIN, SKIN_D)
    b += '<rect x="-36" y="6" width="22" height="10" rx="5" transform="rotate(-35 -20 12)" fill="%s" stroke="%s" stroke-width="1.5"/>' % (SKIN, SKIN_D)
    b += '<rect x="-21" y="-2" width="42" height="40" rx="13" fill="%s"/>' % SKIN
    return '<g transform="translate(%.1f,%.1f) scale(%.2f)">%s</g>' % (cx, cy, s, b)


def magnifier(cx, cy, r=18):
    return ('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#ffffff" fill-opacity=".35" stroke="%s" stroke-width="4"/>'
            '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="6" stroke-linecap="round"/>'
            % (cx, cy, r, INK, cx + r * 0.7, cy + r * 0.7, cx + r * 1.6, cy + r * 1.6, INK))


def dust(cx, cy, n=8, spread=18, col='#a99a92', seed=1):
    s = ''
    for k in range(n):
        a = (k * 2.39996 + seed) % (2 * math.pi)
        rr = spread * ((k * 37 + seed * 13) % 100) / 100
        s += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>' % (cx + rr * math.cos(a), cy + rr * math.sin(a), 1.6 + (k % 3) * 0.6, col)
    return s


def nail_center_line(p, col=ACC2, top=None, bottom=None):
    return dashed(p['cx'], top if top is not None else p['y_t'] - 18, p['cx'], bottom if bottom is not None else p['y_c'] + 20, col, 1.5, '5 4')


def epo_curve(p, dy=0):
    """Curva dell'eponichio (stessa di finger_nail) spostata di dy."""
    cx, yc, hw = p['cx'], p['y_c'], p['hw']
    return 'M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - hw - 4, yc - 28 + dy, cx, yc + 22 + dy, cx + hw + 4, yc - 28 + dy)


# ================================================================= MODULO PREPARAZIONE
@figx('prep-sequenza-perche.svg')
def prep_seq():
    W, H = 940, 420
    b = text(20, 38, 'La preparazione: ogni passaggio ha un perché', 20, 'start', 800, ACC2)
    b += sign(W - 230, 16, 210, 'Stesso ordine, ogni volta')
    steps = [(['Igiene'], 'niente infezioni'), (['Controllo'], 'unghia sana?'), (['Accorcia'], 'bordo pulito'),
             (['Arretra'], 'libera la lamina'), (['Togli', 'cuticola'], 'niente pelle morta'),
             (['Opacizza', '180–240'], 'più presa'), (['Via la', 'polvere'], 'niente bolle'),
             (['Disidratante', '+ primer'], 'niente sebo')]
    xs = [72 + i * 114 for i in range(8)]
    yl = 92
    b += arrow(xs[0], yl, xs[-1] + 40, yl, ACC2, 3)
    for i, (act, why) in enumerate(steps):
        x = xs[i]
        b += '<circle cx="%d" cy="%d" r="17" fill="%s" stroke="#fff" stroke-width="3"/>' % (x, yl, ACC2)
        b += text(x, yl + 6, str(i + 1), 16, weight=800, fill='#fff')
        b += '<rect x="%d" y="128" width="104" height="128" rx="14" fill="%s"/>' % (x - 52, PANEL)
        b += step_icon(i, x, 192)
        b += mtext(x, 284, act, 14, weight=800)
        b += text(x, 284 + 18 * len(act) + 4, why, 12.5, fill=MUTED, style='italic')
    b += text(W / 2, 385, 'Saltare un passaggio rovina quelli dopo: la maggior parte dei sollevamenti nasce qui.', 14, weight=600, fill=MUTED)
    return svg(W, H, arrow_defs() + b, 'Sequenza della preparazione in otto tappe, ognuna con il suo perché')


def mini_nail(cx, cy, s=0.42, extra='', **kw):
    d = dict(hw=34, nail_len=110, free_len=12, shape='tonda', smile=6, finger_len=40)
    d.update(kw)
    f, p = finger_nail(0, 0, extra=extra, **d)
    return scaled(cx, cy, s, f), p


def step_icon(i, x, y):
    s = ''
    if i == 0:
        s += mini_hand(x - 14, y + 18, 0.85)
        s += drop_c(x + 26, y - 30, '#86bfe0') + drop_c(x + 36, y - 2, '#86bfe0', s=0.7) + drop_c(x + 22, y + 22, '#86bfe0', s=0.8)
    elif i == 1:
        f, _ = mini_nail(x - 6, y + 40, 0.45)
        s += f + magnifier(x - 4, y - 6, 20)
    elif i == 2:
        f, _ = mini_nail(x, y + 46, 0.45, free_len=26)
        s += f + tool_file(x, y - 30, 0, 80, 12)
    elif i == 3:
        f, _ = mini_nail(x, y + 46, 0.45)
        s += f + tool_pusher(x - 2, y + 30, -60, 60)
    elif i == 4:
        f, _ = mini_nail(x, y + 46, 0.45)
        s += f
        s += '<path d="M%.1f,%.1f q8,-10 16,-4 q-6,2 -4,8" fill="#fff" stroke="#cdb7ad" stroke-width="1.2"/>' % (x - 6, y + 28)
        s += tool_curette(x + 8, y + 22, -55, 60)
    elif i == 5:
        hatch = ''.join('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#fff" stroke-width="2" opacity=".9" clip-path="url(#CLIP)"/>'
                        % (-40 + k * 10, -120, -60 + k * 10, 0) for k in range(10))
        f, _ = mini_nail(x, y + 46, 0.45, extra=hatch)
        s += f + tool_file(x + 10, y - 2, -65, 72, 12)
    elif i == 6:
        f, _ = mini_nail(x - 4, y + 46, 0.45)
        s += f + tool_brush(x + 16, y - 20, -40, 50, '#c9b8a0') + dust(x - 10, y - 4, 9, 14)
    else:
        s += bottle(x - 20, y + 42, '#9fd0ee', '', 30, 44) + bottle(x + 22, y + 42, '#f4c27c', '', 30, 44)
        s += drop_c(x - 20, y + 20, '#3d8fc6', s=0.8) + drop_c(x + 22, y + 20, '#e08a2c', s=0.8)
    return s


@figx('prep-errori.svg')
def prep_err():
    W, H = 940, 320
    b = ''
    data = [('Pellicina residua', 'si solleva alla base'), ('Lamina assottigliata', 'calore e dolore in lampada'),
            ('Polvere nei solchi', 'bolle ai lati'), ('Dita sulla lamina', 'il sebo blocca l\'adesione')]
    for i, (t, sub) in enumerate(data):
        x = 20 + i * 228
        cx, yc = x + 106, 248
        body = ''
        extra = ''
        if i == 1:
            extra = ('<ellipse cx="%d" cy="%d" rx="20" ry="44" fill="#ec8aa5" opacity=".75" clip-path="url(#CLIP)"/>'
                     '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#c9627f" stroke-width="3" opacity=".8" stroke-linecap="round"/>'
                     '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#c9627f" stroke-width="3" opacity=".8" stroke-linecap="round"/>'
                     % (cx, yc - 72, cx - 9, yc - 110, cx - 11, yc - 40, cx + 9, yc - 108, cx + 11, yc - 38))
        f, p = top_finger(cx, yc, hw=38, nail_len=125, free_len=12, extra=extra)
        body += f
        if i == 0:
            body += '<path d="%s" fill="none" stroke="#fffaf6" stroke-width="10" opacity=".95" clip-path="url(#%s)"/>' % (epo_curve(p, -9), p['clip'])
            body += '<path d="%s" fill="none" stroke="#cdb7ad" stroke-width="1.2" stroke-dasharray="3 3" clip-path="url(#%s)"/>' % (epo_curve(p, -14), p['clip'])
            body += arrow(cx + 62, yc - 74, cx + 16, yc - 17)
            body += text(cx + 64, yc - 80, 'velo', 13, 'start', 700, ACC2)
        elif i == 1:
            body += arrow(x + 176, yc - 140, cx + 14, yc - 84)
            body += text(x + 204, yc - 148, 'zona sottile', 13, 'end', 700, ACC2)
        elif i == 2:
            for sx in (-1, 1):
                for k in range(6):
                    body += dust(cx + sx * 40, yc - 40 - k * 16, 3, 4, '#8f817a', k + (3 if sx > 0 else 0))
            body += arrow(cx + 70, yc - 120, cx + 44, yc - 92)
            body += text(cx + 54, yc - 128, 'polvere', 13, 'start', 700, ACC2)
        else:
            body += ('<ellipse cx="%d" cy="%d" rx="34" ry="40" fill="%s" stroke="%s" stroke-width="1.5"/>'
                     % (cx + 18, yc - 112, SKIN, SKIN_D))
            body += '<rect x="%d" y="%d" width="68" height="60" fill="%s"/>' % (cx - 16, yc - 220, SKIN)
            body += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.5"/>' % (cx - 16, yc - 220, cx - 16, yc - 114, SKIN_D)
            body += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.5"/>' % (cx + 52, yc - 220, cx + 52, yc - 114, SKIN_D)
            body += drop(cx - 22, yc - 66) + drop(cx + 2, yc - 56) + drop(cx + 22, yc - 70)
            body += text(cx + 62, yc - 52, 'sebo', 13, 'start', 700, WARN)
        b += frame(x, 20, 216, 285, t, ok=False, sub=sub, body=body, subcol=ERR)
    return svg(W, H, arrow_defs() + b, 'Quattro errori di preparazione che causano sollevamenti')


@figx('cuticola-step.svg')
def cut_steps():
    W, H = 940, 340
    b = ''
    T = [('Arretra', 'quasi piatto, senza forza'), ('Solleva la pellicina', 'lama piatta sulla lamina'),
         ('Taglia ciò che pende', 'mai la pelle viva'), ('Luce radente', 'controlla: nessun velo opaco')]
    for i, (t, sub) in enumerate(T):
        x = 20 + i * 228
        body = ''
        y0 = 200
        if i < 3:
            sec, q = cuticle_section(x, y0, 216, cut=(i != 2), flap=(i == 2))
            body += sec
            fx = q['fold_x']
            if i == 0:
                # spingicuticole a ~35° con la punta contro l'eponichio
                body += tool_pusher(fx + 4, y0 - 6, -35, 120)
                body += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.2" stroke-dasharray="4 4"/>' % (fx + 4, y0 - 6, fx + 120, y0 - 6, MUTED)
                body += arc_angle(fx + 4, y0 - 6, 62, -35, 0, '30–45°', lx=fx + 92, ly=y0 - 22)
                body += arrow(fx + 10, y0 - 90, fx - 30, y0 - 90)
                body += text(fx - 14, y0 - 100, 'verso la pelle', 12.5, 'middle', 600, ACC2)
            elif i == 1:
                body += '<path d="M%d,%d q10,-18 22,-10 q-8,3 -6,10" fill="#fffaf6" stroke="#cdb7ad" stroke-width="1.2"/>' % (fx + 44, y0 - 2)
                body += tool_curette(fx + 66, y0 - 6, -22, 110)
                body += arrow(fx + 20, y0 + 40, fx + 120, y0 + 40)
                body += text(fx + 70, y0 + 62, 'verso la punta', 12.5, 'middle', 600, ACC2)
            else:
                body += tool_nipper(fx + 22, y0 - 28, -20, 0.95)
                body += mark(x + 34, y0 - 76, False, 12)
                body += text(x + 52, y0 - 72, 'non tagliare qui', 12.5, 'start', 700, ERR)
                body += '<path d="M%d,%d L%d,%d" stroke="%s" stroke-width="1.4" stroke-dasharray="3 3"/>' % (x + 34, y0 - 63, x + 40, y0 - 30, ERR)
                body += text(fx + 60, y0 + 52, 'pellicina morta', 12.5, 'middle', 600, ACC2)
                body += arrow(fx + 60, y0 + 36, fx + 30, y0 - 18)
        else:
            f, p = top_finger(x + 130, 262, hw=34, nail_len=120, free_len=12)
            body += f + desk_lamp(x + 50, 92, 0.9)
            body += rays(x + 70, 110, x + 112, 150, 4, 8, 20)
            body += mark(x + 130, 190, True, 14)
        b += frame(x, 20, 216, 300, t, i + 1, sub=sub, body=body, subcol=INK)
    return svg(W, H, arrow_defs() + b, 'Zona cuticolare in quattro passaggi: arretra, solleva, taglia solo ciò che pende, controlla')


# ================================================================= MAIN
def main():
    only = sys.argv[1:]
    for name, f in MINE.items():
        if only and name not in only:
            continue
        with open(os.path.join(OUT, name), 'w', encoding='utf-8') as fh:
            fh.write(f())
    print('Gruppo B: %d illustrazioni' % len(MINE))


if __name__ == '__main__':
    main()
