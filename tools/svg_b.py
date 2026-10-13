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
         'C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
         % (x - 110, y - 14, x - 8, y - 14, x + 6, y - 14, x + 10, y - 2, xe, y + 5,
            xe + 16, y + 8, xe + 20, y + 44, xe - 2, y + 62, xe - 24, y + 80, x - 60, y + 80, x - 110, y + 80, SKIN, SKIN_D))
    if plate:
        s += ('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.4"/>'
              % (x + 4, y, xe, y + 1, xe, y + 6, x + 6, y + 5, NAIL, NAIL_S))
        if free:
            s += ('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.4"/>'
                  % (xe, y + 1, xe + free, y + 1 + tip_down, xe + free, y + 6 + tip_down, xe, y + 6, free_col, NAIL_S))
        # piega dell'eponichio sopra l'inizio della lamina
        s += ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s"/>'
              % (x - 40, y - 13, x - 8, y - 13, x + 8, y - 13, x + 12, y - 1, x - 40, y - 1, SKIN))
        s += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="1.5"/>'
              % (x - 8, y - 14, x + 8, y - 14, x + 12, y - 1, SKIN_D))
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



@figx('pterigio-vero.svg')
def pterygium():
    W, H = 760, 350
    b = ''
    # sinistra: cuticola normale
    body = ''
    f, p = top_finger(140, 262, hw=46, nail_len=140, free_len=16)
    body += f
    body += '<path d="%s" fill="none" stroke="#fffaf6" stroke-width="11" opacity=".95" clip-path="url(#%s)"/>' % (epo_curve(p, -10), p['clip'])
    body += leader(152, 250, 236, 196, 'pelle morta', 'start', 13)
    body += text(242, 219, 'sulla lamina', 13, 'start', 600)
    body += text(242, 244, 'si rimuove', 13.5, 'start', 800, OK)
    b += frame(20, 20, 350, 300, 'Cuticola', ok=True, body=body)
    # destra: vero pterigio
    body = ''
    extra = ('<path d="M%d,%d L%d,%d L%d,%d Z" fill="%s" stroke="%s" stroke-width="1.5" clip-path="url(#CLIP)"/>'
             % (510 - 30, 262, 510, 262 - 100, 510 + 30, 262, SKIN, SKIN_D))
    f, p = top_finger(510, 262, hw=46, nail_len=140, free_len=16, extra=extra)
    body += f
    body += leader(512, 205, 598, 150, 'pelle saldata', 'start', 13)
    body += text(604, 173, 'alla lamina', 13, 'start', 600)
    body += text(598, 215, 'non toccare:', 13.5, 'start', 800, ERR)
    body += text(598, 235, 'medico', 13.5, 'start', 800, ERR)
    b += frame(390, 20, 350, 300, 'Vero pterigio', body=body)
    b += stop_sign(390 + 350 - 26, 45, 13)
    b += text(W / 2, 342, 'Il pterigio vero è un disturbo, non una pellicina.', 14.5, weight=700, fill=ACC2)
    return svg(W, H + 6, b, 'Cuticola normale da rimuovere e vero pterigio da non toccare')


@figx('opacizzazione-zone.svg')
def buff_zones():
    W, H = 760, 410
    b = text(20, 38, 'Dove opacizzare', 20, 'start', 800, ACC2)
    cx, yc, hw = 190, 330, 82
    ys = yc - 220
    yt = ys - 34
    zones = ''
    # 4 bordo libero, 3 centro, 2 lati, 1 base (disegnati in quest'ordine)
    zones += '<rect x="%d" y="%d" width="%d" height="%d" fill="%s" opacity=".55" clip-path="url(#CLIP)"/>' % (cx - hw - 6, yt - 10, 2 * hw + 12, ys - yt + 14, YEL)
    zones += '<rect x="%d" y="%d" width="%d" height="%d" fill="#9ed8a8" opacity=".55" clip-path="url(#CLIP)"/>' % (cx - hw + 26, ys + 4, 2 * hw - 52, yc - ys - 40)
    for sx in (-1, 1):
        x0 = cx - hw - 6 if sx < 0 else cx + hw - 26
        zones += '<rect x="%d" y="%d" width="32" height="%d" fill="#8cc2e6" opacity=".6" clip-path="url(#CLIP)"/>' % (x0, ys + 4, yc - ys - 30)
    zones += '<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="#f2a65a" stroke-width="30" opacity=".6" clip-path="url(#CLIP)"/>' % (
        cx - hw - 4, yc - 52, cx, yc - 2, cx + hw + 4, yc - 52)
    f, p = finger_nail(cx, yc, hw=hw, nail_len=220, free_len=34, shape='tonda', smile=10, finger_len=60, lunula=False, extra=zones)
    b += '<g>%s</g>' % f
    # frecce di direzione
    b += arrow(cx, yc - 70, cx, ys + 20, ACC2, 2.2)
    b += arrow(cx - 30, yc - 80, cx - 30, ys + 40, ACC2, 1.8)
    b += arrow(cx + 30, yc - 80, cx + 30, ys + 40, ACC2, 1.8)
    # numeri e legenda
    nums = [(1, cx + 52, yc - 40, '#f2a65a', 'Zona cuticolare', 'archetti piccoli lungo la curva'),
            (2, cx + hw - 10, ys + 120, '#8cc2e6', 'Lati', 'lima inclinata, mai la pelle'),
            (3, cx - 52, ys + 80, '#9ed8a8', 'Centro', 'dalla base verso la punta'),
            (4, cx - 40, yt + 14, YEL, 'Bordo libero', 'anche lo spessore del bordo')]
    for k, (n, nx, ny, col, lab, sub) in enumerate(nums):
        b += '<circle cx="%d" cy="%d" r="12" fill="%s" stroke="%s" stroke-width="2"/>' % (nx, ny, col, INK)
        b += text(nx, ny + 5, str(n), 13, weight=800)
        ly = 96 + k * 60
        b += '<circle cx="345" cy="%d" r="12" fill="%s" stroke="%s" stroke-width="2"/>' % (ly - 5, col, INK)
        b += text(345, ly, str(n), 13, weight=800)
        b += text(366, ly, lab, 15, 'start', 800)
        b += text(366, ly + 19, sub, 13, 'start', fill=MUTED)
    # riquadro grana
    gx, gy = 560, 64
    b += '<rect x="%d" y="%d" width="180" height="236" rx="16" fill="%s"/>' % (gx, gy, PANEL)
    b += text(gx + 90, gy + 30, 'Grana', 16, weight=800)
    for k, (g, ok, c1, c2) in enumerate([('100', False, '#5b4a44', '#8a7469'), ('180', True, '#8a7469', '#c3ad9f'), ('240', True, '#c3ad9f', '#ece1d8')]):
        yy = gy + 74 + k * 58
        b += tool_file(gx + 66, yy, 0, 92, 20, c1, c2)
        b += text(gx + 66, yy + 30, g, 14, weight=800)
        b += mark(gx + 148, yy, ok, 13)
    b += mtext(560, 336, ['Leggera, pochi passaggi,', 'nessuna zona lucida'], 15, 'start', 800, ACC2)
    return svg(W, H, arrow_defs() + b, 'Zone da opacizzare: base, lati, centro e bordo libero; grane adatte')


def light_nail(cx, yc, kind):
    extra = ''
    if kind == 'lucida':
        extra = ('<path d="M%d,%d Q%d,%d %d,%d" stroke="#fff" stroke-width="12" fill="none" stroke-linecap="round" opacity=".95" clip-path="url(#CLIP)"/>'
                 % (cx - 14, yc - 40, cx - 20, yc - 90, cx - 8, yc - 130))
    elif kind == 'opaca':
        extra = '<rect x="%d" y="%d" width="120" height="200" fill="#efe2e6" opacity=".55" clip-path="url(#CLIP)"/>' % (cx - 60, yc - 190)
    else:
        extra = ('<rect x="%d" y="%d" width="120" height="200" fill="#efe2e6" opacity=".45" clip-path="url(#CLIP)"/>'
                 '<ellipse cx="%d" cy="%d" rx="18" ry="40" fill="#ec7f9c" opacity=".8" clip-path="url(#CLIP)"/>'
                 '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#c9627f" stroke-width="3" stroke-linecap="round"/>'
                 '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#c9627f" stroke-width="3" stroke-linecap="round"/>'
                 % (cx - 60, yc - 190, cx, yc - 80, cx - 8, yc - 112, cx - 10, yc - 46, cx + 8, yc - 110, cx + 10, yc - 44))
    return top_finger(cx, yc, hw=38, nail_len=130, free_len=14, extra=extra)


@figx('opacizzazione-controllo.svg')
def buff_check():
    W, H = 940, 330
    b = ''
    T = [('Ancora lucida', False, 'ripassa'), ('Opaca uniforme', True, 'pronta'), ('Troppo limata', False, 'sottile: calore')]
    for i, (t, ok, sub) in enumerate(T):
        x = 20 + i * 304
        cx = x + (130 if i == 2 else 160)
        body = ''
        f, p = light_nail(cx, 268, ['lucida', 'opaca', 'troppo'][i])
        body += f
        body += rays(x + 20, 70, cx - 40, 120, 3, 0, 24)
        if i == 2:
            # piccola sezione laterale: lamina più sottile al centro
            sx, sy = x + 200, 150
            body += '<rect x="%d" y="%d" width="88" height="96" rx="10" fill="#fff"/>' % (sx - 6, sy - 40)
            body += text(sx + 38, sy - 20, 'sezione', 12.5, weight=700, fill=MUTED)
            body += '<rect x="%d" y="%d" width="76" height="18" fill="#f0c3ad"/>' % (sx, sy + 14)
            body += '<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d L%d,%d L%d,%d Z" fill="%s" stroke="%s" stroke-width="1.4"/>' % (
                sx, sy, sx + 20, sy, sx + 38, sy + 11, sx + 56, sy, sx + 76, sy, sx + 76, sy + 14, sx, sy + 14, NAIL, NAIL_S)
            body += arrow(sx + 38, sy - 14, sx + 38, sy + 6, ERR, 1.6)
            body += text(sx + 38, sy + 48, 'più sottile', 12.5, weight=700, fill=ERR)
        b += frame(x, 20, 290, 290, t, ok=ok, sub=('✓ ' if ok else '✗ ') + sub, body=body)
    return svg(W, H, arrow_defs() + b, 'Controllo con luce radente: lamina ancora lucida, opaca uniforme, troppo limata')


def lens(cx, cy, r, inner, label=''):
    c = uid('l')
    s = '<defs><clipPath id="%s"><circle cx="%.1f" cy="%.1f" r="%.1f"/></clipPath></defs>' % (c, cx, cy, r)
    s += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#fff"/>' % (cx, cy, r)
    s += '<g clip-path="url(#%s)">%s</g>' % (c, inner)
    s += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" stroke-width="5"/>' % (cx, cy, r, INK)
    return s


@figx('primer-acido-vs-senza.svg')
def primers():
    W, H = 760, 370
    b = ''
    for i in range(2):
        x = 20 + i * 370
        cx, cy, r = x + 118, 190, 100
        surf = cy + 12
        inner = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (cx - r, cy - r, 2 * r, r + 32, PROD)
        if i == 0:
            pts = 'M%.1f,%.1f ' % (cx - r, surf)
            xx = cx - r
            while xx < cx + r:
                pts += 'L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f ' % (xx + 10, surf, xx + 16, surf + 16, xx + 22, surf)
                xx += 26
            pts += 'L%.1f,%.1f L%.1f,%.1f Z' % (cx + r, cy + r, cx - r, cy + r)
            inner += '<path d="%s" fill="%s" stroke="%s" stroke-width="1.5"/>' % (pts, NAIL, NAIL_S)
        else:
            inner += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" stroke="%s" stroke-width="1.5"/>' % (cx - r, surf, 2 * r, r, NAIL, NAIL_S)
            inner += '<rect x="%.1f" y="%.1f" width="%.1f" height="9" fill="%s"/>' % (cx - r, surf - 9, 2 * r, YEL)
            for k in range(14):
                inner += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#c9a54a" stroke-width="2"/>' % (cx - r + 6 + k * 16, surf - 7, cx - r + 12 + k * 16, surf - 2)
        for k in range(4):
            inner += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1" opacity=".5"/>' % (cx - r, surf + 26 + k * 18, cx + r, surf + 26 + k * 18, NAIL_S)
        inner += text(cx, cy - 46, 'prodotto', 14, weight=700, fill='#41708a')
        inner += text(cx, cy + 74, 'lamina', 14, weight=700, fill=ACC2)
        body = lens(cx, cy, r, inner)
        lx = x + 232
        if i == 0:
            body += leader(cx + 32, surf + 12, lx, 140, 'microfori', 'start', 13.5)
            body += mtext(lx, 196, ['asciutto =', 'bianco gessoso'], 13.5, 'start', 600)
            body += warn_tri(lx + 10, 262, 1.1, ERR)
            body += text(lx + 28, 267, 'corrosivo', 13.5, 'start', 800, ERR)
        else:
            body += leader(cx + 40, surf - 5, lx, 140, 'effetto', 'start', 13.5)
            body += text(lx + 6, 163, 'biadesivo', 13.5, 'start', 600)
            body += mtext(lx, 206, ['attivo circa', '20 minuti'], 13.5, 'start', 600)
            body += timer(lx + 16, 262, '')
        b += frame(x, 20, 350, 330, 'Primer acido' if i == 0 else 'Primer senza acido', body=body)
    return svg(W, H, b, 'Sezione al microscopio: il primer acido incide la lamina, quello senza acido fa da biadesivo')


@figx('primer-quantita.svg')
def primer_amount():
    W, H = 940, 330
    b = ''
    # 1 scarica il pennello
    x = 20
    body = bottle(x + 110, 270, '#f4e3a4', 'primer', 70, 96)
    body = body.replace('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="%s"/>' % (x + 110 - 15.4, 270 - 96 - 26, 30.8, 26, INK), '')
    body += '<rect x="%d" y="%d" width="40" height="12" rx="3" fill="#fff" stroke="%s" stroke-width="1.6"/>' % (x + 90, 270 - 108, MUTED)
    body += tool_brush(x + 128, 154, -60, 90, '#f4e3a4')
    body += arrow(x + 150, 128, x + 168, 150)
    body += drop_c(x + 112, 186, '#e7c95a', s=0.7) + drop_c(x + 124, 204, '#e7c95a', s=0.55)
    b += frame(x, 20, 290, 290, 'Scarica il pennello', 1, sub='quasi asciutto', body=body, subcol=INK)
    # 2 giusto
    x = 324
    extra = ''
    cx, yc = x + 130, 250
    f, p = top_finger(cx, yc, hw=46, nail_len=150, free_len=14, finger_len=10)
    prim = ('<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Z" fill="#f6e39a" opacity=".75" stroke="#d9b44a" stroke-width="1.2"/>'
            % (cx - 32, yc - 142, cx - 32, yc - 70, cx, yc - 40, cx + 32, yc - 70, cx + 32, yc - 142))
    body = f + prim
    body += dim(cx, yc - 40, cx, yc - 5, '', 'right')
    body += dashed(cx + 4, yc - 22, x + 200, yc - 60, MUTED, 1, '3 3')
    body += text(x + 204, yc - 70, '≥ 1 mm', 14, 'start', 800, ACC2)
    body += text(x + 204, yc - 52, 'dalla pelle', 12.5, 'start', 600, ACC2)
    b += frame(x, 20, 290, 290, 'Solo sulla lamina', 2, ok=True, sub='piccoli tocchi, lontano dalla pelle', body=body)
    # 3 troppo
    x = 628
    cx = x + 145
    yc = 250
    f, p = top_finger(cx, yc, hw=46, nail_len=150, free_len=14, finger_len=10)
    flood = ('<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="#f2b45a" opacity=".7"/>'
             % (cx - 62, yc - 160, cx - 64, yc - 30, cx, yc + 26, cx + 64, yc - 30, cx + 62, yc - 160, cx, yc - 170, cx - 62, yc - 160))
    body = f + flood + drop_c(cx - 66, yc - 8, '#f2b45a') + drop_c(cx + 68, yc - 20, '#f2b45a')
    body += leader(cx + 60, yc - 40, x + 250, yc - 170, 'sulla pelle', 'middle', 13, fill=ERR)
    b += frame(x, 20, 290, 290, 'Troppo primer', ok=False, sub='meno adesione, pelle a rischio', body=body)
    return svg(W, H, arrow_defs() + b, 'La quantità giusta di primer: pennello quasi asciutto, solo sulla lamina, lontano dalla pelle')



# ================================================================= MODULO TIP
HATCH_ID = 'hatchB'


def hatch_defs(col=ACC, op=.55):
    return ('<defs><pattern id="%s" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
            '<line x1="0" y1="0" x2="0" y2="7" stroke="%s" stroke-width="2.2" opacity="%s"/></pattern></defs>' % (HATCH_ID, col, op))


def tip_top(cx, ys, hw, L, well, op=1.0, hatch=True, ang=0, stop=True, outline=TIP_S):
    """Tip visto dall'alto: ys = punto d'arresto, L = corpo oltre l'arresto, well = incavo verso la cuticola."""
    yt = ys - L
    body = ('M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z'
            % (cx - hw, ys + well, cx - hw, yt + hw * 0.5, cx - hw, yt, cx, yt, cx + hw, yt, cx + hw, yt + hw * 0.5,
               cx + hw, ys + well, cx, ys + well + 26, cx - hw, ys + well))
    s = '<path d="%s" fill="%s" fill-opacity="%.2f" stroke="%s" stroke-width="1.6"/>' % (body, TIPC, op, outline)
    if hatch and well > 0:
        c = uid('t')
        s += '<defs><clipPath id="%s"><path d="%s"/></clipPath></defs>' % (c, body)
        s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#%s)" clip-path="url(#%s)"/>' % (cx - hw - 2, ys, 2 * hw + 4, well + 30, HATCH_ID, c)
    if stop:
        s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2.2"/>' % (cx - hw, ys, cx + hw, ys, outline)
    if ang:
        s = rot(ang, cx, ys + well, s)
    return s


def tip_side(x, y, ang=0, well=46, L=120, glue=False):
    """Tip di profilo: arresto in (x, y) (y = superficie della lamina), corpo verso destra."""
    t = ('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" '
         'fill="%s" stroke="%s" stroke-width="1.5"/>'
         % (x - well, y - 1, x - well, y - 3.5, x, y - 5, x + L * 0.6, y - 6, x + L, y - 2, x + L, y + 4,
            x + L * 0.6, y + 2, x, y + 6, x, y, x - well, y - 1, TIPC, TIP_S))
    if glue:
        t += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="#5aa9dc" stroke-width="3" fill="none" stroke-linecap="round"/>' % (
            x - well + 6, y + 1, x - well / 2, y + 3, x - 4, y + 1)
    return rot(ang, x, y, t) if ang else t


def finger_front(cx, cy, hw=52, curve=22):
    """Sezione frontale del dito (vista dal bordo libero): restituisce svg e la quota della lamina al centro."""
    s = ('<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
         % (cx - hw - 22, cy, cx - hw - 26, cy + 70, cx + hw + 26, cy + 70, cx + hw + 22, cy,
            cx + hw + 18, cy - curve - 18, cx - hw - 18, cy - curve - 18, cx - hw - 22, cy, SKIN, SKIN_D))
    s += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="7" stroke-linecap="round"/>'
          % (cx - hw, cy - 4, cx, cy - 2 * curve - 4, cx + hw, cy - 4, NAIL_S))
    for sx in (-1, 1):
        s += ('<path d="M%.1f,%.1f q%.1f,-14 %.1f,-4" fill="%s" stroke="%s" stroke-width="1.5"/>'
              % (cx + sx * (hw + 24), cy + 2, -sx * 10, -sx * 22, SKIN, SKIN_D))
    return s


@figx('tip-anatomia.svg')
def tip_anat():
    W, H = 760, 370
    b = hatch_defs()
    b += text(20, 38, 'Com\'è fatto un tip', 20, 'start', 800, ACC2)
    cx, ys = 120, 230
    b += tip_top(cx, ys, 50, 160, 70)
    b += leader(cx - 12, ys + 40, 230, 262, 'Incavo (well)', 'start', 14)
    b += leader(cx + 30, ys, 230, 222, 'Punto d\'arresto', 'start', 14)
    b += leader(cx + 22, ys + 60, 230, 300, 'Zona di contatto', 'start', 14)
    b += text(236, 318, '(sotto l\'incavo)', 12.5, 'start', fill=MUTED)
    b += leader(cx + 10, ys - 90, 230, 130, 'Corpo del tip', 'start', 14)
    b += text(120, 60, 'dall\'alto', 13, weight=700, fill=MUTED)
    # vista di profilo
    b += '<rect x="400" y="64" width="340" height="250" rx="16" fill="%s"/>' % PANEL
    b += text(570, 92, 'di profilo', 13, weight=700, fill=MUTED)
    t = ('<path d="M430,176 L430,172 L540,168 L540,160 Q640,158 720,172 L720,180 Q640,170 548,176 L540,184 L540,178 Z" '
         'fill="%s" stroke="%s" stroke-width="1.8"/>' % (TIPC, TIP_S))
    b += t
    b += '<rect x="430" y="178" width="110" height="9" fill="url(#%s)"/>' % HATCH_ID
    b += '<rect x="430" y="178" width="110" height="9" fill="none" stroke="%s" stroke-dasharray="3 3"/>' % MUTED
    b += arrow(600, 222, 545, 186)
    b += mtext(604, 236, ['gradino: si appoggia', 'al bordo libero'], 12.5, 'start', 600)
    b += leader(480, 172, 470, 130, 'incavo sottile', 'middle', 13)
    b += leader(484, 186, 470, 222, 'zona di contatto', 'middle', 12.5)
    # curva a C
    b += ('<path d="M424,294 Q464,262 504,294" fill="none" stroke="%s" stroke-width="7" stroke-linecap="round"/>' % TIP_S)
    b += text(516, 284, 'Curva a C', 13, 'start', 700)
    b += text(516, 300, '(vista dalla punta)', 12, 'start', fill=MUTED)
    b += text(W / 2, 352, 'L\'incavo copre al massimo metà unghia.', 15, weight=800, fill=ACC2)
    return svg(W, H, arrow_defs() + b, 'Le parti del tip: incavo, punto d\'arresto, zona di contatto, corpo e curva a C')


@figx('tip-misura-errori.svg')
def tip_size():
    W, H = 940, 330
    b = hatch_defs()
    data = [('Troppo stretto', False, -16, 'lati scoperti: crepe'), ('Giusto', True, 0, 'da solco a solco'),
            ('Troppo largo', False, 16, 'preme sulla pelle: dolore')]
    for i, (t, ok, dw, sub) in enumerate(data):
        x = 20 + i * 304
        cx, cy = x + 145, 170
        hw = 52
        body = finger_front(cx, cy, hw)
        th = hw + dw
        k = 22 * th / hw
        # tip sopra la lamina (vista frontale)
        body += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="9" stroke-linecap="round" opacity=".95"/>'
                 % (cx - th, cy - 12 + (abs(dw) * 0.9 if dw > 0 else 0), cx, cy - 2 * k - 14, cx + th, cy - 12 + (abs(dw) * 0.9 if dw > 0 else 0), TIPC))
        body += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="1.4"/>'
                 % (cx - th, cy - 16 + (abs(dw) * 0.9 if dw > 0 else 0), cx, cy - 2 * k - 18, cx + th, cy - 16 + (abs(dw) * 0.9 if dw > 0 else 0), TIP_S))
        if dw < 0:
            for sx in (-1, 1):
                body += arrow(cx + sx * 74, cy - 56, cx + sx * (hw - 4), cy - 14, ERR, 2)
            body += text(cx, 92, 'lati scoperti', 13, weight=700, fill=ERR)
        elif dw > 0:
            for sx in (-1, 1):
                body += '<circle cx="%.1f" cy="%.1f" r="13" fill="%s" opacity=".55"/>' % (cx + sx * (hw + 18), cy - 4, ERR)
            body += text(cx, 92, 'sulla pelle', 13, weight=700, fill=ERR)
        else:
            body += dim(cx - hw, 96, cx + hw, 96, 'solco – solco', 'above', OK)
            body += leader(cx + 20, cy - 52, cx + 90, cy - 70, 'tip', 'start', 13)
            body += leader(cx + 36, cy - 26, cx + 96, cy - 36, 'unghia', 'start', 13)
        body += text(cx, 252, 'vista dalla punta', 12.5, fill=MUTED, style='italic')
        b += frame(x, 20, 290, 290, t, ok=ok, sub=sub, body=body)
    return svg(W, H, arrow_defs() + b, 'Misura del tip vista dalla punta: troppo stretto, giusto, troppo largo')


@figx('tip-adattare.svg')
def tip_fit():
    W, H = 760, 330
    b = hatch_defs()
    # 1 lima i lati del tip
    x = 20
    cx = x + 150
    body = tip_top(cx, 190, 56, 120, 60)
    body += '<path d="M%d,%d L%d,%d" stroke="%s" stroke-width="2" stroke-dasharray="6 4"/>' % (cx + 44, 70, cx + 44, 270, OK)
    body += '<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="%s" opacity=".25"/>' % (cx + 44, 76, cx + 56, 80, cx + 56, 250, cx + 44, 250, ERR)
    body += tool_file(cx + 74, 170, 90, 150, 18)
    body += arrow(cx + 102, 120, cx + 102, 210, MUTED, 1.6, True)
    body += leader(cx + 50, 130, cx - 10, 100, 'solo plastica', 'end', 13, fill=ACC2)
    b += frame(x, 20, 350, 290, 'Lima i lati del tip', 1, sub='prima di incollare', body=body, subcol=INK)
    # 2 accorcia l'incavo
    x = 390
    cx, yc = x + 130, 270
    body = ''
    f, p = top_finger(cx, yc, hw=46, nail_len=160, free_len=10, finger_len=20)
    body += f
    ys = p['y_s'] - 10
    body += tip_top(cx, ys, 50, 70, 130, op=0.55, hatch=False)
    half = yc - 3 - 80
    body += ('<path d="M%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="%s" opacity=".3"/>'
             % (cx - 50, half - 6, cx, half + 18, cx + 50, half - 6, cx + 50, ys + 130, cx, ys + 156, cx - 50, ys + 130, ERR))
    body += '<path d="M%d,%d Q%d,%d %d,%d" stroke="%s" stroke-width="2.4" stroke-dasharray="7 5" fill="none"/>' % (cx - 50, ys + 130, cx, ys + 156, cx + 50, ys + 130, ERR)
    body += '<path d="M%d,%d Q%d,%d %d,%d" stroke="%s" stroke-width="3" fill="none"/>' % (cx - 50, half - 6, cx, half + 18, cx + 50, half - 6, OK)
    body += tool_scissors(cx + 56, half + 4, 0, 0.8)
    body += text(cx + 112, half - 40, 'max', 13, 'start', 800, OK)
    body += text(cx + 112, half - 22, 'metà unghia', 13, 'start', 800, OK)
    body += text(cx + 112, ys + 150, 'troppo', 13, 'start', 800, ERR)
    body += text(cx + 112, ys + 168, 'lungo', 13, 'start', 800, ERR)
    b += frame(x, 20, 350, 290, 'Accorcia l\'incavo', 2, sub='segue la curva della cuticola', body=body, subcol=INK)
    return svg(W, H, arrow_defs() + b, 'Adattare il tip: limare i lati e accorciare l\'incavo a metà unghia')


@figx('tip-incollaggio-45.svg')
def tip_glue():
    W, H = 940, 310
    b = ''
    T = ['Appoggia a 45°', 'Abbassa lentamente', 'Tieni fermo']
    for i, t in enumerate(T):
        x = 20 + i * 228
        fx, fy = x + 34, 190
        body = finger_side(fx, fy, L=82, free=14)
        sx = fx + 96
        ang = [42, 18, 0][i]
        body += tip_side(sx, fy + 1, ang, glue=(i == 0))
        if i == 0:
            body += dashed(sx, fy + 1, sx + 80, fy + 1, MUTED, 1.2, '4 4')
            body += arc_angle(sx, fy + 1, 40, 0, 42, '45°', lx=sx + 58, ly=fy + 36)
            body += leader(sx - 24, fy - 30, sx - 70, fy - 80, 'colla', 'end', 13)
        elif i == 1:
            body += ('<path d="M%.1f,%.1f A70,70 0 0 0 %.1f,%.1f" fill="none" stroke="%s" stroke-width="2.2" marker-end="url(#ar)"/>'
                     % (sx + 52, fy + 52, sx + 70, fy + 12, ACC2))
            for k in range(3):
                body += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#fff" stroke="#5aa9dc" stroke-width="1.4"/>' % (sx - 52 - k * 12, fy - 10 - k * 10, 4 - k * 0.6)
            body += arrow(sx - 50, fy - 30, sx - 92, fy - 62)
            body += text(sx - 70, fy - 72, 'aria fuori', 13, 'middle', 700, ACC2)
        else:
            body += thumb(sx - 24, fy - 30, 180, 0.8)
            body += timer(x + 118, 82, '5–10 s')
        b += frame(x, 20, 216, 270, t, i + 1, body=body)
    # riquadro errore
    x = 704
    fx, fy = x + 40, 180
    body = finger_side(fx, fy, L=70, free=14)
    sx = fx + 84
    body += tip_side(sx, fy - 3, 0)
    body += '<ellipse cx="%.1f" cy="%.1f" rx="13" ry="3" fill="#fff" stroke="#5aa9dc" stroke-width="1.4"/>' % (sx - 22, fy - 2)
    body += arrow(sx - 10, fy - 70, sx - 10, fy - 20)
    body += leader(sx - 22, fy - 2, sx + 10, fy + 50, 'bolla', 'start', 13, fill=ERR)
    b += frame(x, 20, 216, 270, 'Appoggiato piatto', ok=False, sub='giù di colpo = bolle', body=body)
    return svg(W, H, arrow_defs() + b, 'Incollare il tip: appoggio a 45 gradi, discesa lenta, tenuta 5–10 secondi; errore: tip appoggiato di colpo')


@figx('tip-errori-applicazione.svg')
def tip_errors():
    W, H = 940, 320
    b = hatch_defs()
    T = [('Bolla', 'togli e riapplica'), ('Fuori asse', 'l\'unghia cresce storta'), ('Inclinato', 'punta che scende')]
    for i, (t, sub) in enumerate(T):
        x = 20 + i * 304
        cx, yc = x + 145, 255
        body = ''
        if i < 2:
            f, p = top_finger(cx, yc, hw=40, nail_len=110, free_len=6, finger_len=14)
            body += f
            ys = p['y_s'] - 4
            body += tip_top(cx, ys, 43, 78, 55, op=0.6, ang=(10 if i == 1 else 0), hatch=False)
            if i == 0:
                body += '<circle cx="%.1f" cy="%.1f" r="12" fill="#fff" opacity=".95" stroke="#cfd8de"/>' % (cx + 8, ys + 30)
                body += leader(cx + 12, ys + 30, cx + 90, ys - 30, 'bolla', 'start', 13.5, fill=ERR)
            else:
                body += dashed(cx, yc + 10, cx, 64, OK, 1.8)
                body += dashed(cx, ys + 60, cx + (ys + 60 - 64) * math.tan(math.radians(10)), 64, ERR, 1.8)
                body += text(cx - 10, 80, 'asse del dito', 12.5, 'end', 700, OK)
                body += text(cx + 40, 80, 'tip', 12.5, 'start', 700, ERR)
        else:
            fx, fy = x + 26, 180
            body += finger_side(fx, fy, L=84, free=12)
            sx = fx + 96
            body += tip_side(sx, fy + 1, 14)
            body += dashed(sx, fy + 1, sx + 130, fy + 1, OK, 1.8)
            body += text(sx + 70, fy - 12, 'linea giusta', 12.5, 'middle', 700, OK)
            body += arrow(sx + 112, fy + 6, sx + 112, fy + 26, ERR, 2)
        b += frame(x, 20, 290, 285, t, ok=False, sub=sub, body=body)
    return svg(W, H, arrow_defs() + b, 'Tre errori di applicazione del tip: bolla, fuori asse, inclinato')


@figx('tip-taglio.svg')
def tip_cut():
    W, H = 760, 330
    b = hatch_defs()
    # 1 taglio perpendicolare
    x = 20
    cx, yc = x + 130, 312
    body = ''
    f, p = top_finger(cx, yc, hw=38, nail_len=100, free_len=6, finger_len=20)
    body += f
    ys = p['y_s'] - 4
    body += tip_top(cx, ys, 41, 120, 45, op=0.6, hatch=False)
    cut = ys - 70
    body += dashed(cx - 66, cut, cx + 66, cut, ERR, 2, '7 5')
    body += tool_tipcutter(cx, cut, -90, 1.0)
    body += dim(cx + 60, cut, cx + 60, cut + 20, '', 'left')
    body += mtext(cx + 72, cut + 18, ['+1–2 mm', 'per limare'], 12.5, 'start', 700, ACC2)
    body += text(cx - 72, cut + 4, 'taglio', 12.5, 'end', 700, ERR)
    b += frame(x, 20, 350, 290, 'Taglio perpendicolare', ok=True, body=body)
    # 2 lunghezza
    x = 390
    cx, yc = x + 120, 300
    body = ''
    f, p = top_finger(cx, yc, hw=38, nail_len=140, free_len=70, shape='squoval', free=TIPC, finger_len=20)
    body += f
    yb0, yb1 = yc - 3, p['y_s']
    body += '<path d="M%d,%d q-12,0 -12,10 L%d,%d q0,10 -10,10 q10,0 10,10 L%d,%d q0,10 12,10" fill="none" stroke="%s" stroke-width="2"/>' % (
        cx - 56, yb1, cx - 68, (yb0 + yb1) / 2 - 10, cx - 68, yb0 - 10, ACC2)
    body += text(cx - 84, (yb0 + yb1) / 2 + 5, 'letto', 13.5, 'end', 800, ACC2)
    body += '<path d="M%d,%d q12,0 12,10 L%d,%d q0,10 10,10 q-10,0 -10,10 L%d,%d q0,10 -12,10" fill="none" stroke="%s" stroke-width="2"/>' % (
        cx + 56, p['y_t'], cx + 68, (p['y_t'] + yb1) / 2 - 10, cx + 68, yb1 - 10, OK)
    body += mtext(cx + 86, (p['y_t'] + yb1) / 2, ['max', '½ letto'], 13.5, 'start', 800, OK)
    b += frame(x, 20, 350, 290, 'Lunghezza equilibrata', ok=True, body=body)
    b += text(W / 2, 334, 'Taglia solo a colla asciutta.', 14.5, weight=800, fill=ERR)
    return svg(W, H + 14, arrow_defs() + b, 'Taglio del tip: tagliatip perpendicolare e lunghezza massima di metà letto ungueale')


def blend_section(x, y, w, state):
    """Sezione ingrandita: lamina (sotto) + fine dell'incavo del tip; state = 'prima', 'lima', 'dopo', 'ko'."""
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="40" fill="#f0c3ad"/>' % (x, y + 22, w)
    lam_top = y
    if state == 'ko':
        s += ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
              % (x, y, x + w * 0.42, y, x + w * 0.42 + 34, y + 12, x + w * 0.42 + 68, y, x + w, y, x + w, y + 22, x, y + 22, NAIL, NAIL_S))
    else:
        s += '<rect x="%.1f" y="%.1f" width="%.1f" height="22" fill="%s" stroke="%s" stroke-width="1.5"/>' % (x, y, w, NAIL, NAIL_S)
    e = x + w * 0.42  # fine dell'incavo
    if state == 'prima':
        s += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>' % (
            x + w, y - 14, e, y - 14, e, y, x + w, y, TIPC, TIP_S)
    elif state == 'lima':
        s += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>' % (
            x + w, y - 14, e + 40, y - 14, e, y, x + w, y, TIPC, TIP_S)
    elif state == 'dopo':
        s += '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>' % (
            x + w, y - 14, e + 70, y - 14, e + 30, y - 12, e - 6, y, x + w, y, TIPC, TIP_S)
    else:
        s += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>' % (
            x + w, y - 14, e + 70, y - 14, e + 68, y, x + w, y, TIPC, TIP_S)
    s += text(x + 8, y + 16, 'lamina', 12.5, 'start', 700, ACC2)
    s += text(x + w - 8, y - 22, 'tip', 12.5, 'end', 700, MUTED)
    return s, e


@figx('tip-fusione-step.svg')
def tip_blend():
    W, H = 940, 330
    b = ''
    T = [('Prima', None, 'il gradino si sente'), ('Lima piatta solo sul tip', None, 'grana 180–240'), ('Dopo: liscio', True, 'nessuno scalino'),
         ('Lamina limata', False, 'sottile e sensibile')]
    for i, (t, ok, sub) in enumerate(T):
        x = 20 + i * 228
        body = ''
        sx, sy = x + 10, 190
        sec, e = blend_section(sx, sy, 196, ['prima', 'lima', 'dopo', 'ko'][i])
        body += sec
        if i == 0:
            body += arrow(e - 20, sy - 60, e - 2, sy - 10)
            body += text(e - 24, sy - 68, 'gradino', 13, 'middle', 700, ACC2)
        elif i == 1:
            body += tool_file(e + 24, sy - 14, -19, 100, 14)
            body += arrow(e - 10, sy - 44, e + 64, sy - 70, ACC2, 1.8, True)
        elif i == 2:
            body += text(e + 10, sy - 50, 'superficie continua', 12.5, 'middle', 700, OK)
        else:
            body += arrow(e + 34, sy - 50, e + 34, sy + 4, ERR, 2)
            body += text(e + 34, sy - 58, 'avvallamento', 12.5, 'middle', 700, ERR)
        b += frame(x, 20, 216, 290, t, (i + 1) if i < 3 else None, ok=ok if i == 3 else None, sub=sub, body=body,
                   subcol=ERR if i == 3 else INK)
        if i == 2:
            b += mark(x + 192, 45, True, 13)
    return svg(W, H, arrow_defs() + b, 'Fusione del tip in sezione: dal gradino alla superficie liscia, senza limare la lamina')


def overlay_profile(ox, oy, L=170, free=26, ext=130, apex_h=28, prod=True, apex_at=None, tip=True):
    """Profilo: dito + lamina + (tip) + prodotto. Restituisce svg e punti."""
    s = finger_side(ox, oy, L=L, free=free)
    xe = ox + L
    xn = xe + free           # fine unghia naturale
    xb = xn + ext            # punta
    if tip:
        s += ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.4"/>'
              % (xn - 40, oy - 1, xn, oy - 2, xn + ext * 0.6, oy - 1, xb, oy + 3, xb, oy + 7, xn, oy + 6, TIPC, TIP_S))
    pts = {}
    if prod:
        xa = ox + 14
        ax = apex_at if apex_at is not None else xe - 6
        top = 'M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (
            xa, oy - 1, (xa + ax) / 2, oy - apex_h, ax, oy - apex_h, (ax + xb) / 2 + 20, oy - apex_h, xb, oy - 4)
        if tip:
            s += '<path d="%s L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.6" opacity=".92"/>' % (
                top, xb, oy - 1, xa, oy - 1, PROD, PROD_S)
        else:
            s += '<path d="%s L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.6" opacity=".92"/>' % (
                top, xb, oy + 5, xn, oy + 6, xn, oy - 1, xa, oy - 1, PROD, PROD_S)
        pts = dict(xa=xa, ax=ax, ah=oy - apex_h)
    pts.update(xe=xe, xn=xn, xb=xb, oy=oy, ox=ox)
    return s, pts


@figx('tip-overlay-sezione.svg')
def tip_overlay():
    W, H = 760, 310
    b = text(20, 38, 'Copertura in gel sul tip (sezione)', 20, 'start', 800, ACC2)
    s, p = overlay_profile(150, 190, L=200, free=24, ext=200, apex_h=34)
    b += s
    xn, xe, oy = p['xn'], p['xe'], p['oy']
    b += dashed(xn, oy - 70, xn, oy + 40, MUTED, 1.4, '5 4')
    b += text(xn + 6, oy + 58, 'fine unghia naturale', 12.5, 'middle', 600, MUTED)
    b += '<circle cx="%.1f" cy="%.1f" r="5" fill="%s"/>' % (xe, oy + 6, ERR)
    b += leader(xe, oy + 6, xe - 80, oy + 70, 'punto di stress', 'end', 13, fill=ERR)
    b += text(p['xa'] + 40, 120, 'Zona 3 sottile', 13.5, 'middle', 800)
    b += text(p['ax'], 112, 'Zona 2 apex', 13.5, 'middle', 800, ACC2)
    b += arrow(p['ax'], 118, p['ax'], p['ah'] - 2)
    b += text(p['xb'] - 50, 140, 'Zona 1 ≈ 1–1,5 mm', 13.5, 'middle', 800)
    b += dim(p['ox'] + 2, oy - 26, p['xa'] + 2, oy - 26, '', 'above')
    b += text(p['ox'] - 10, oy - 40, '≈ 1 mm dalla pelle', 12.5, 'middle', 700, ACC2)
    b += leader(p['xb'] - 30, oy + 4, p['xb'] - 10, oy + 50, 'tip', 'start', 13)
    return svg(W, H, arrow_defs() + b, 'Sezione della copertura in gel sul tip: sottile alla cuticola, apex sopra il punto di stress, sottile in punta')


@figx('tip-gel-step.svg')
def tip_gel_steps():
    labels = ['Primer solo sull\'unghia', 'Base + lampada', 'Perla in zona 2', 'Capovolgi', 'Controlla il profilo', 'Lima, top, olio']

    def nail_tip():
        f, p = top_finger(0, 0, hw=34, nail_len=100, free_len=6, finger_len=8)
        ys = p['y_s'] - 4
        return f + tip_top(0, ys, 36, 70, 40, op=0.6, hatch=False), ys

    def d(i, x, y):
        s = ''
        cx, yb = x + 145, y + 176
        if i in (0, 1, 2, 5):
            g, ys = nail_tip()
            ox = cx - (40 if i == 1 else 0)
            sc = 0.66
            if i == 0:
                g += tool_brush(16, -40, -50, 70, '#f4e3a4')
                g += mark(64, ys - 40, False, 14)
                g += text(84, ys - 34, 'tip', 18, 'start', 700, ERR)
            elif i == 2:
                g += bead(0, ys + 16, 20, PROD, PROD_S)
                g += arrow(0, ys + 40, 0, ys + 74, ACC2, 2.4)
                g += arrow(0, ys - 8, 0, ys - 50, ACC2, 2.4)
            elif i == 5:
                g += tool_file(64, ys - 20, -70, 110, 16)
            s += scaled(ox, yb, sc, g)
            if i == 1:
                s += lamp(cx + 70, yb, 100)
                s += timer(x + 30, y + 70, '')
            if i == 5:
                s += bottle(x + 46, yb, '#f0eaf6', 'top', 34, 50)
                s += drop_c(x + 240, yb - 40, YEL)
                s += text(x + 240, yb - 2, 'olio', 12.5, 'middle', 700, MUTED)
        elif i == 3:
            sp, p = overlay_profile(0, 0, L=90, free=14, ext=70, apex_h=22, tip=True)
            s += scaled(x + 128, y + 116, 0.62, '<g transform="rotate(180 60 30)">%s</g>' % sp)
            s += drop_c(x + 150, y + 150, PROD_S, s=0.7)
            s += text(x + 252, y + 80, '5–30 s', 14, 'middle', 800, ACC2)
            s += text(x + 120, y + 70, 'unghia verso il basso', 12.5, 'middle', 600, MUTED)
        else:
            sp, p = overlay_profile(0, 0, L=90, free=14, ext=70, apex_h=22, tip=True)
            sp += '<circle cx="%.1f" cy="%.1f" r="5" fill="%s"/>' % (p['xe'], p['oy'] + 6, ERR)
            s += scaled(x + 92, y + 120, 0.68, sp)
            s += eye(x + 262, y + 98, 180, 1.1)
            s += text(x + 130, y + 70, 'sottile – spesso – sottile', 12.5, 'middle', 600, MUTED)
        return s
    return steps_fig('Copertura in gel sul tip', labels, 3, 290, 190, d, 'Copertura in gel sul tip in sei passaggi')


# ================================================================= MODULO CARTINA
def form_shape(cx, ys, w=80, h=130, hole=46, hole_d=48, grid=True, center=True, notch=None, cut_tab=False):
    """Cartina vista dall'alto: ys = altezza del bordo libero; foro verso il basso."""
    if cut_tab:
        d = 'M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (
            cx - w, ys + 36, cx - w, ys - h, cx + w, ys - h, cx + w, ys + 36, cx + hole, ys + 36, cx + hole, ys) + \
            ' M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (cx + hole, ys, cx - hole, ys, cx - hole, ys + 36, cx + hole, ys + 36)
        d = 'M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (
            cx - w, ys + 36, cx - w, ys - h, cx + w, ys - h, cx + w, ys + 36, cx + hole, ys + 36, cx + hole, ys, cx - hole, ys, cx - hole, ys + 36)
    else:
        nd = notch if notch else 0
        d = ('M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f A%.1f,%.1f 0 0 0 %.1f,%.1f Z'
             % (cx - w, ys + 36, cx - w, ys - h, cx + w, ys - h, cx + w, ys + 36, cx + hole, ys + 36, hole, hole_d + nd, cx - hole, ys + 36))
    s = '<path d="%s" fill="%s" stroke="%s" stroke-width="1.4"/>' % (d, FORM, FORM_S)
    if grid:
        for k in range(1, 5):
            yy = ys - k * 26 + 6
            if yy > ys - h + 4:
                s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s"/>' % (cx - w + 8, yy, cx + w - 8, yy, FORM_S)
    if center:
        s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-dasharray="4 4" stroke-width="1.4"/>' % (cx, ys - h, cx, ys - 8, ACC2)
    return s


def form_side(x, y, ang, L=120):
    """Cartina di profilo: parte dal bordo libero (x, y) verso destra, inclinata di ang (gradi, + = verso il basso)."""
    return rot(ang, x, y, '<rect x="%.1f" y="%.1f" width="%.1f" height="5" rx="2" fill="%s" stroke="%s"/>' % (x - 6, y + 5, L, FORM, FORM_S))


@figx('cartina-step.svg')
def form_steps():
    W, H = 940, 340
    b = ''
    T = [('Stacca e curva', ''), ('Adatta l\'apertura', ''), ('Infila in asse', 'niente spazi'), ('Chiudi le alette', '')]
    for i, (t, sub) in enumerate(T):
        x = 20 + i * 228
        cx = x + 108
        body = ''
        if i == 0:
            body += ('<path d="M%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="%s" stroke="%s" stroke-width="1.4"/>'
                     % (cx - 70, 200, cx, 170, cx + 70, 200, cx + 70, 110, cx, 80, cx - 70, 110, FORM, FORM_S))
            for k in range(1, 4):
                body += '<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="%s"/>' % (cx - 62, 110 + k * 22, cx, 80 + k * 22, cx + 62, 110 + k * 22, FORM_S)
            body += dashed(cx, 84, cx, 168, ACC2, 1.4, '4 4')
            body += thumb(cx - 74, 156, 90, 0.9) + thumb(cx + 74, 156, -90, 0.9)
            body += ('<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="%s" stroke-width="2.2" marker-end="url(#ar)"/>'
                     % (cx - 60, 250, cx, 222, cx + 60, 250, ACC2))
            body += text(cx, 272, 'curva come l\'unghia', 12.5, 'middle', 600, ACC2)
        elif i == 1:
            body += form_shape(cx, 170, 80, 110, 40, 30)
            body += ('<path d="M%d,%d A%d,%d 0 0 0 %d,%d" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="5 4"/>'
                     % (cx + 50, 206, 50, 46, cx - 50, 206, ERR))
            body += tool_scissors(cx + 40, 180, -35, 0.9)
            body += text(cx, 268, 'segui il bordo libero', 12.5, 'middle', 600, ACC2)
        elif i == 2:
            yc = 262
            f, p = top_finger(cx, yc, hw=32, nail_len=100, free_len=6, finger_len=8)
            ys = p['y_s'] - 6
            body += form_shape(cx, ys, 84, 96, 34, 40, center=False)
            body += f
            body += dashed(cx, ys - 120, cx, yc + 20, ACC2, 1.8, '6 4')
            body += text(cx + 46, ys - 40, 'asse', 12.5, 'start', 700, ACC2)
        else:
            # vista dal basso del polpastrello
            body += '<rect x="%d" y="64" width="80" height="196" rx="38" fill="%s" stroke="%s" stroke-width="1.5"/>' % (cx - 40, SKIN, SKIN_D)
            body += '<path d="M%d,214 q20,6 40,0 M%d,224 q20,6 40,0" stroke="%s" stroke-width="1.5" fill="none"/>' % (cx - 20, cx - 20, SKIN_D)
            body += ('<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="%s" stroke="%s" stroke-width="1.4" opacity=".96"/>'
                     % (cx - 92, 84, cx - 40, 70, cx + 22, 130, cx - 30, 146, FORM, FORM_S))
            body += ('<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="%s" stroke="%s" stroke-width="1.4" opacity=".96"/>'
                     % (cx + 92, 84, cx + 40, 70, cx - 22, 130, cx + 30, 146, FORM, FORM_S))
            body += text(cx, 172, 'unisci sotto il', 12.5, 'middle', 700, ACC2)
            body += text(cx, 188, 'polpastrello', 12.5, 'middle', 700, ACC2)
            body += mark(cx + 62, 219, False, 11)
            body += text(cx, 280, 'non sulla nocca', 12.5, 'middle', 700, ERR)
            sub = 'vista dal basso'
        b += frame(x, 20, 216, 300, t, i + 1, sub=sub, body=body, subcol=INK)
    return svg(W, H, arrow_defs() + b, 'Posizionare la cartina in quattro passaggi: curva, apertura, asse, alette')


@figx('cartina-livello.svg')
def form_level():
    W, H = 940, 310
    b = ''
    T = [('Troppo bassa', False, 14, 'l\'allungamento cade'), ('In livello', True, 0, 'prosegue la lamina'),
         ('Troppo alta', False, -14, 'punta all\'insù (ski-jump)')]
    for i, (t, ok, ang, sub) in enumerate(T):
        x = 20 + i * 304
        fx, fy = x + 70, 160
        body = finger_side(fx, fy, L=110, free=8)
        sx = fx + 118
        body += form_side(sx - 4, fy + 1, ang, 140)
        body += dashed(fx + 20, fy + 1, x + 290, fy + 1, OK, 1.8, '7 5')
        if ang:
            body += arrow(x + 250, fy + 1, x + 250, fy + 1 + (36 if ang > 0 else -36), ERR, 2)
        b += frame(x, 20, 290, 270, t, ok=ok, sub=sub, body=body)
    return svg(W, H, arrow_defs() + b, 'Livello della cartina di profilo: troppo bassa, in livello, troppo alta')


@figx('cartina-adattata.svg')
def form_adapt():
    W, H = 940, 370
    b = ''
    T = [('Unghia corta', 'linguetta dritta'), ('Unghia larga', 'allarga il foro'), ('Iponichio lungo', 'incavo più profondo'),
         ('Unghia curva', 'piega di più')]
    for i, (t, sub) in enumerate(T):
        x = 20 + i * 228
        cx = x + 108
        body = ''
        if i == 0:
            body += form_shape(cx, 200, 84, 120, 36, 0, cut_tab=True)
            body += '<rect x="%d" y="200" width="72" height="60" fill="%s" opacity=".55" stroke="%s" stroke-dasharray="4 3"/>' % (cx - 36, NAIL, NAIL_S)
            body += text(cx, 236, 'unghia', 12.5, 'middle', 700, ACC2)
            body += leader(cx + 30, 200, cx + 60, 100, 'bordo dritto', 'middle', 12.5)
        elif i == 1:
            body += form_shape(cx, 200, 84, 120, 56, 46)
            body += ('<path d="M%d,%d A%d,%d 0 0 0 %d,%d" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="5 4"/>'
                     % (cx + 40, 236, 40, 40, cx - 40, 236, MUTED))
            body += ('<path d="M%d,%d A%d,%d 0 0 0 %d,%d" fill="%s" fill-opacity=".45" stroke="%s" stroke-width="1.5"/>'
                     % (cx + 56, 236, 56, 46, cx - 56, 236, NAIL, NAIL_S))
            body += arrow(cx - 30, 222, cx - 52, 222, ACC2, 1.6) + arrow(cx + 30, 222, cx + 52, 222, ACC2, 1.6)
            body += tool_scissors(cx + 62, 150, -30, 0.7)
        elif i == 2:
            body += form_shape(cx, 200, 84, 120, 44, 46, notch=34)
            body += ('<path d="M%d,%d A%d,%d 0 0 0 %d,%d" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="5 4"/>'
                     % (cx + 44, 236, 44, 46, cx - 44, 236, MUTED))
            body += '<ellipse cx="%d" cy="%d" rx="30" ry="16" fill="#d96f86" opacity=".7"/>' % (cx, 190)
            body += leader(cx + 18, 186, cx + 64, 120, 'iponichio', 'middle', 12.5)
        else:
            cy = 200
            body += finger_front(cx, cy, 50, 34)
            body += ('<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="%s" stroke-width="8" stroke-linecap="round"/>'
                     % (cx - 66, cy + 16, cx, cy - 2 * 34 + 2, cx + 66, cy + 16, FORM))
            body += leader(cx - 30, cy - 24, cx - 60, 140, 'unghia', 'middle', 12.5)
            body += text(cx, 106, 'vista dalla punta', 12.5, 'middle', 600, MUTED)
            body += leader(cx + 50, cy + 2, cx + 70, 140, 'cartina', 'middle', 12.5)
        b += frame(x, 20, 216, 290, t, sub=sub, body=body, subcol=INK)
    return svg(W, H - 40, arrow_defs() + b, 'Quattro modi di adattare la cartina: unghia corta, larga, iponichio lungo, unghia curva')


@figx('cartina-ritaglio-step.svg')
def form_trim():
    W, H = 940, 290
    b = ''
    T = ['Prova a secco', 'Segna il contatto', 'Ritaglia poco', 'Riprova']
    for i, t in enumerate(T):
        x = 20 + i * 228
        cx = x + 108
        body = ''
        notch = 30 if i == 3 else 0
        body += form_shape(cx, 170, 84, 100, 40, 40, notch=notch, grid=False)
        if i in (0, 3):
            body += ('<path d="M%d,%d A%d,%d 0 0 0 %d,%d" fill="%s" stroke="%s" stroke-width="1.4"/>'
                     % (cx + 40, 206, 40, 40, cx - 40, 206, SKIN, SKIN_D))
            body += '<ellipse cx="%d" cy="%d" rx="22" ry="10" fill="#d96f86" opacity=".7"/>' % (cx, 170 + (0 if i == 0 else -6))
        if i == 0:
            body += ('<path d="M%d,%d l10,-14 l-2,10 l10,-12" fill="none" stroke="%s" stroke-width="3" stroke-linejoin="round"/>'
                     % (cx + 26, 168, ERR))
            body += text(cx, 252, 'preme: dolore', 12.5, 'middle', 700, ERR)
        elif i == 1:
            body += '<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="%s" stroke-width="2.4"/>' % (cx - 26, 172, cx, 146, cx + 26, 172, INK)
            body += tool_pencil(cx + 24, 168, -40, 70)
        elif i == 2:
            body += '<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="5 4"/>' % (cx - 26, 172, cx, 146, cx + 26, 172, ERR)
            body += tool_scissors(cx + 22, 166, -40, 0.8)
            body += text(cx, 252, 'poco per volta', 12.5, 'middle', 700, ACC2)
        else:
            body += text(cx, 252, 'tocca senza premere', 12.5, 'middle', 700, OK)
        b += frame(x, 20, 216, 255, t, i + 1, ok=(True if i == 3 else None), body=body)
    return svg(W, H, arrow_defs() + b, 'Ritagliare la cartina per un iponichio lungo: prova, segna, ritaglia, riprova')


@figx('zone-spessori-sezione.svg')
def zone_thick():
    W, H = 940, 370
    b = text(20, 38, 'Dove il prodotto è spesso e dove è sottile', 20, 'start', 800, ACC2)
    b += '<rect x="20" y="60" width="580" height="290" rx="16" fill="%s"/>' % PANEL
    b += text(310, 88, 'Sezione longitudinale (di profilo)', 15, weight=700)
    s, p = overlay_profile(140, 220, L=190, free=20, ext=160, apex_h=36, tip=False)
    b += s
    xa, ax, xb, xe, oy = p['xa'], p['ax'], p['xb'], p['xe'], p['oy']
    b += '<circle cx="%.1f" cy="%.1f" r="5" fill="%s"/>' % (xe, oy + 6, ERR)
    b += leader(xe, oy + 6, xe + 10, oy + 104, 'punto di stress', 'middle', 13, fill=ERR)
    for lab, xx in (('3', xa + 40), ('2', ax), ('1', xb - 60)):
        b += '<circle cx="%.1f" cy="122" r="13" fill="%s"/>' % (xx, ACC2) + text(xx, 127, lab, 14, weight=800, fill='#fff')
    b += arrow(ax, 140, ax, p['ah'] - 3) + text(ax + 20, 150, 'apex', 13.5, 'start', 800, ACC2)
    b += dim(p['ox'] + 2, oy - 18, xa + 2, oy - 18, '', 'above')
    b += text(p['ox'] - 4, oy - 32, '≈ 1 mm dalla pelle', 12.5, 'end', 700, ACC2)
    b += dim(xb + 14, oy - 5, xb + 14, oy + 6, '', 'right')
    b += text(xb - 4, oy + 34, '≈ 1–1,5 mm', 13, 'middle', 800, ACC2)
    # carta di credito
    b += '<rect x="%.1f" y="%.1f" width="40" height="26" rx="4" fill="#cfe0f0" stroke="%s"/>' % (xb - 70, oy + 46, PROD_S)
    b += '<rect x="%.1f" y="%.1f" width="40" height="6" fill="%s"/>' % (xb - 70, oy + 52, PROD_S)
    b += mtext(xb - 24, oy + 56, ['come una carta', 'di credito'], 12, 'start', 600, MUTED)
    # sezione trasversale
    b += '<rect x="620" y="60" width="300" height="290" rx="16" fill="%s"/>' % PANEL
    b += text(770, 88, 'Sezione trasversale', 15, weight=700)
    b += text(770, 106, '(vista dalla punta)', 12.5, fill=MUTED)
    cx, cy = 770, 250
    b += ('<path d="M%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="%s" stroke="%s" stroke-width="1.6"/>'
          % (cx - 110, cy, cx, cy - 150, cx + 110, cy, cx + 100, cy + 2, cx, cy - 104, cx - 100, cy + 2, PROD, PROD_S))
    b += ('<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="%s" stroke-width="7" stroke-linecap="round"/>'
          % (cx - 100, cy + 6, cx, cy - 98, cx + 100, cy + 6, NAIL_S))
    b += dim(cx, cy - 52, cx, cy - 76, '', 'right')
    b += text(cx + 10, cy - 104, 'centro più spesso', 13, 'start', 700, ACC2)
    b += mtext(cx, cy + 40, ['lati sottili e uguali'], 13.5, 'middle', 700)
    b += arrow(cx - 70, cy + 22, cx - 100, cy + 2, MUTED, 1.4) + arrow(cx + 70, cy + 22, cx + 100, cy + 2, MUTED, 1.4)
    return svg(W, H, arrow_defs() + b, 'Spessori della ricostruzione in sezione longitudinale e trasversale')


@figx('apex-controllo-viste.svg')
def apex_views():
    W, H = 940, 320
    b = ''
    T = [('Profilo', 'apex sopra il punto di stress'), ('Fronte', 'uguale a destra e sinistra'), ('Alto + luce', 'riflesso continuo')]
    for i, (t, sub) in enumerate(T):
        x = 20 + i * 304
        body = ''
        if i == 0:
            s, p = overlay_profile(0, 0, L=120, free=14, ext=80, apex_h=26, tip=False)
            s += '<circle cx="%.1f" cy="%.1f" r="5" fill="%s"/>' % (p['xe'], 6, ERR)
            body += scaled(x + 100, 180, 0.8, s)
            body += dashed(x + 100 + p['xe'] * 0.8, 110, x + 100 + p['xe'] * 0.8, 186, ERR, 1.3, '4 4')
        elif i == 1:
            cx, cy = x + 145, 200
            body += ('<path d="M%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="%s" stroke="%s" stroke-width="1.6"/>'
                     % (cx - 90, cy, cx, cy - 116, cx + 90, cy, cx + 82, cy + 2, cx, cy - 80, cx - 82, cy + 2, PROD, PROD_S))
            body += dim(cx - 90, cy + 20, cx - 70, cy + 20, '', 'below') + dim(cx + 70, cy + 20, cx + 90, cy + 20, '', 'below')
            body += text(cx, cy + 26, '=', 18, 'middle', 800, ACC2)
            body += ('<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="%s" stroke-width="7" stroke-linecap="round"/>'
                     % (cx - 80, cy + 4, cx, cy - 78, cx + 80, cy + 4, NAIL_S))
        else:
            cx, yc = x + 145, 232
            extra = ('<path d="M%d,%d L%d,%d" stroke="#fff" stroke-width="9" stroke-linecap="round" opacity=".95" clip-path="url(#CLIP)"/>'
                     % (cx, yc - 30, cx, yc - 170))
            f, p = top_finger(cx, yc, hw=36, nail_len=100, free_len=50, shape='squoval', free=PROD, plate='#f3c6d3', extra=extra, finger_len=4)
            body += f
            body += desk_lamp(x + 50, 90, 0.8)
        b += frame(x, 20, 290, 280, t, sub=sub, body=body, subcol=INK)
        b += eye(x + 30, 46, 0, 1.0)
    return svg(W, H, arrow_defs() + b, 'Controllo dell\'apex da tre punti di vista: profilo, fronte, alto con luce')


def horiz_finger(x, y, s=1.0, **kw):
    """finger_nail ruotato con la punta verso destra; (x, y) = posizione della base dell'unghia."""
    f, p = finger_nail(0, 0, **kw)
    return '<g transform="translate(%.1f,%.1f) rotate(90) scale(%.2f)">%s</g>' % (x, y, s, f), p


@figx('lunghezza-proporzioni.svg')
def length_prop():
    W, H = 760, 340
    b = text(20, 38, 'La regola della metà', 20, 'start', 800, ACC2)
    bx, by = 200, 190
    L = 220
    f, p = horiz_finger(bx, by, 1.0, hw=56, nail_len=L, free_len=0, shape='tonda', finger_len=90)
    b += f
    xs = bx + L  # linea del sorriso
    b += '<path d="M%d,%d q0,-12 10,-12 L%d,%d q10,0 10,-10 q0,10 10,10 L%d,%d q10,0 10,12" fill="none" stroke="%s" stroke-width="2"/>' % (
        bx, 112, bx + L / 2 - 10, 100, xs - 10, 100, ACC2)
    b += text(bx + L / 2, 84, 'letto ungueale = 1', 14, 'middle', 800, ACC2)
    b += '<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Z" fill="%s" stroke="%s" stroke-width="1.6"/>' % (
        xs - 4, 136, xs + L * 0.5 - 20, 136, xs + L * 0.5, 190, xs + L * 0.5 - 20, 244, xs - 4, 244, FREE, NAIL_S)
    b += text(xs + L * 0.22, 195, 'bordo libero', 12.5, 'middle', 700, ACC2)
    for frac, lab, col, ok in ((1 / 3, '1/3', MUTED, None), (0.5, '1/2', OK, True), (0.85, '', ERR, False)):
        xx = xs + L * frac
        b += dashed(xx, 120, xx, 262, col, 2, '6 5')
        b += text(xx, 284, lab, 14, 'middle', 800, col)
    b += mtext(xs + L * 0.85 + 8, 140, ['troppo per', 'iniziare'], 13, 'start', 800, ERR)
    b += text(xs + L * 0.5, 302, 'massimo consigliato', 12.5, 'middle', 700, OK)
    b += mark(xs + L * 0.5, 106, True, 12)
    return svg(W, H, b, 'Proporzioni: il bordo libero arriva al massimo a circa metà della lunghezza del letto ungueale')


@figx('apex-lunghezza.svg')
def apex_len():
    W, H = 760, 300
    b = ''
    T = [('Corta: apex leggero', 50, 18), ('Lunga: apex più alto', 130, 32)]
    for i, (t, ext, ah) in enumerate(T):
        x = 20 + i * 370
        s, p = overlay_profile(0, 0, L=120, free=10, ext=ext, apex_h=ah, tip=False)
        s += '<circle cx="%.1f" cy="%.1f" r="5" fill="%s"/>' % (p['xe'], 6, ERR)
        sc = 0.8
        body = scaled(x + 110, 170, sc, s)
        xe = x + 110 + p['xe'] * sc
        if i == 1:
            body += arrow(xe, 230, x + 110 + p['xb'] * sc, 230, ACC2, 1.8, True)
            body += text((xe + x + 110 + p['xb'] * sc) / 2, 252, 'leva più lunga', 12.5, 'middle', 700, ACC2)
        body += dashed(xe, 90, xe, 176, ERR, 1.4, '4 4')
        b += frame(x, 20, 350, 260, t, body=body)
    return svg(W, H, arrow_defs() + b, 'Unghia corta e unghia lunga: l\'apex cresce e resta sopra il punto di stress')


@figx('curva-c-percentuali.svg')
def ccurve_pct():
    W, H = 760, 310
    b = text(20, 38, 'Curva a C in percentuale di cerchio', 20, 'start', 800, ACC2)
    for i, (f, lab) in enumerate([(0.30, '≈30% bassa'), (0.40, '≈40% salone'), (0.50, '≈50% gara')]):
        cx, cy, r = 140 + i * 240, 170, 70
        b += '<circle cx="%d" cy="%d" r="%d" fill="none" stroke="#d9c9c4" stroke-width="2" stroke-dasharray="5 5"/>' % (cx, cy, r)
        a0, a1 = 270 - 180 * f, 270 + 180 * f
        p0 = (cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0)))
        p1 = (cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1)))
        b += ('<path d="M%.1f,%.1f A%d,%d 0 0 1 %.1f,%.1f" fill="none" stroke="%s" stroke-width="13" stroke-linecap="round"/>'
              % (p0[0], p0[1], r, r, p1[0], p1[1], ACC))
        b += text(cx, 272, lab, 16, weight=800)
    b += text(W / 2, 300, 'Segui sempre la curva naturale della cliente.', 14, weight=600, fill=MUTED)
    return svg(W, H, b, 'Curva a C del 30, 40 e 50 per cento di un cerchio')


def c_arc(cx, cy, hw=80, k=38, crack=False, col=PROD, stroke=PROD_S):
    s = ('<path d="M%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="%s" stroke="%s" stroke-width="1.6"/>'
         % (cx - hw, cy, cx, cy - 2 * k - 20, cx + hw, cy, cx + hw - 8, cy + 2, cx, cy - 2 * k + 6, cx - hw + 8, cy + 2, col, stroke))
    if crack:
        s += '<path d="M%d,%d l6,-8 l-4,-6 l7,-8" fill="none" stroke="%s" stroke-width="2.4"/>' % (cx + hw - 16, cy - 4, ERR)
    return s


@figx('curva-c-pinching-step.svg')
def pinch_steps():
    W, H = 940, 330
    b = ''
    # 1
    x = 20
    cx, cy = x + 145, 210
    body = c_arc(cx, cy, 80, 30)
    body += thumb(cx - 96, cy - 14, 90, 0.9) + thumb(cx + 96, cy - 14, -90, 0.9)
    body += arrow(cx - 120, cy - 60, cx - 96, cy - 40, ACC2, 2) + arrow(cx + 120, cy - 60, cx + 96, cy - 40, ACC2, 2)
    body += text(cx, 110, 'vista dalla punta', 12.5, 'middle', 600, MUTED)
    body += text(cx, 262, 'sull\'allungamento, non sulla lamina', 12.5, 'middle', 600, ACC2)
    b += frame(x, 20, 290, 290, 'Pressione uguale ai lati', 1, body=body)
    # 2
    x = 324
    body = timer(x + 125, 110, '')
    body += '<circle cx="%d" cy="110" r="30" fill="none" stroke="%s" stroke-width="2"/>' % (x + 125, ACC2)
    body += text(x + 30, 178, 'acrilico:', 14, 'start', 800)
    body += text(x + 30, 198, 'opaco ma ancora morbido', 13.5, 'start', 600)
    body += text(x + 30, 236, 'gel:', 14, 'start', 800)
    body += text(x + 30, 256, 'dopo una flash cure', 13.5, 'start', 600)
    b += frame(x, 20, 290, 290, 'Il momento giusto', 2, body=body)
    # 3
    x = 628
    cx = x + 110
    body = c_arc(cx, 200, 80, 34) + mark(cx, 150, True, 14)
    body += '<rect x="%d" y="96" width="100" height="90" rx="12" fill="#fff"/>' % (x + 180)
    body += c_arc(x + 230, 160, 38, 14, True)
    body += mark(x + 262, 112, False, 11)
    body += mtext(x + 230, 206, ['troppo tardi:', 'crepe'], 12.5, 'middle', 700, ERR)
    body += text(cx, 262, 'curva simmetrica', 13, 'middle', 700, OK)
    b += frame(x, 20, 290, 290, 'Controlla dal davanti', 3, body=body)
    return svg(W, H, arrow_defs() + b, 'Pinching passo passo: pressione uguale ai lati, momento giusto, controllo frontale')


@figx('tut-gel-flip.svg')
def gel_flip():
    W, H = 760, 300
    b = ''
    T = ['Perla in zona 2', 'Capovolgi', 'Controlla e polimerizza']
    for i, t in enumerate(T):
        x = 20 + i * 245
        body = ''
        s, p = overlay_profile(0, 0, L=110, free=10, ext=60, apex_h=(8 if i == 0 else 22), tip=False)
        if i == 0:
            s += bead(p['xe'] - 20, -24, 16, PROD, PROD_S)
            body += scaled(x + 82, 190, 0.7, s)
        elif i == 1:
            body += scaled(x + 40, 150, 0.7, '<g transform="rotate(180 70 0)">%s</g>' % s)
            body += drop_c(x + 104, 186, PROD_S, s=0.7)
            body += text(x + 50, 205, '5–30 s', 15, 'middle', 800, ACC2)
            body += text(x + 115, 244, 'unghia verso il basso', 12.5, 'middle', 600, MUTED)
        else:
            s += '<circle cx="%.1f" cy="%.1f" r="5" fill="%s"/>' % (p['xe'], 6, ERR)
            body += scaled(x + 82, 200, 0.7, s)
            body += lamp(x + 180, 140, 70)
        b += frame(x, 20, 230, 260, t, i + 1, body=body)
    return svg(W, H, arrow_defs() + b, 'Capovolgere la mano: la gravità porta il gel verso l\'apex')


@figx('tut-gel-zona1.svg')
def gel_zone1():
    W, H = 760, 340
    b = ''
    for i, (t, ok, sub) in enumerate([('Lati che proseguono i solchi', True, ''), ('Lati a ventaglio: sembra larga', False, '')]):
        x = 20 + i * 370
        cx, yc = x + 150, 334
        body = ''
        f, p = top_finger(cx, yc, hw=36, nail_len=90, free_len=6, finger_len=20)
        ys = p['y_s'] - 6
        body += form_shape(cx, ys, 110, 130, 38, 44, center=False)
        spread = 0 if ok else 22
        L = 110
        body += ('<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="%s" stroke="%s" stroke-width="1.6" opacity=".9"/>'
                 % (cx - 38, ys + 6, cx - 38 - spread, ys - L, cx + 38 + spread, ys - L, cx + 38, ys + 6, PROD, PROD_S))
        body += f
        col = OK if ok else ERR
        for sx in (-1, 1):
            body += dashed(cx + sx * 40, yc - 20, cx + sx * (40 + spread * 1.3), ys - L - 30, col, 2, '6 4')
        if ok:
            body += dashed(cx - 60, ys - L, cx + 80, ys - L, ACC2, 2, '3 3')
            body += text(cx + 84, ys - L + 5, 'lunghezza scelta', 12.5, 'start', 700, ACC2)
        b += frame(x, 20, 350, 300, t, ok=ok, sub=sub or None, body=body)
    return svg(W, H, b, 'Zona 1 in gel: lati dritti che proseguono i solchi laterali, non a ventaglio')


def dappen(cx, yb, liquid=True, powder=False):
    s = ('<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="#f4f1f8" stroke="%s" stroke-width="2"/>'
         % (cx - 44, yb - 60, cx + 44, yb - 60, cx + 30, yb, cx - 30, yb, MUTED))
    if liquid:
        s += '<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="#cfe6f7"/>' % (cx - 39, yb - 44, cx + 39, yb - 44, cx + 28, yb - 4, cx - 28, yb - 4)
    if powder:
        s += '<path d="M%d,%d Q%d,%d %d,%d L%d,%d L%d,%d Z" fill="#ffffff" stroke="#ddd"/>' % (
            cx - 40, yb - 44, cx, yb - 56, cx + 40, yb - 44, cx + 28, yb - 4, cx - 28, yb - 4)
        s += dust(cx, yb - 30, 10, 18, '#e2d8dc')
    return s


@figx('acrilico-pennello-carico.svg')
def acrylic_load():
    W, H = 940, 300
    b = ''
    T = [('Immergi nel monomero', ''), ('Scarica sul bordo', ''), ('Tocca la polvere', ''), ('Perla pronta', 'lucida e bombata')]
    for i, (t, sub) in enumerate(T):
        x = 20 + i * 228
        cx = x + 100
        body = ''
        if i == 0:
            body += dappen(cx, 240) + tool_brush(cx + 6, 200, -70, 90, '#f3eee6')
        elif i == 1:
            body += dappen(cx, 240) + tool_brush(cx + 54, 172, -30, 80, '#d8e8f4')
            body += drop_c(cx + 30, 196, '#86bfe0', s=0.7)
            body += arrow(cx + 90, 140, cx + 64, 168)
        elif i == 2:
            body += dappen(cx, 240, liquid=False, powder=True) + tool_brush(cx + 24, 172, -50, 90, '#d8e8f4')
        else:
            body += tool_brush(cx + 10, 170, -20, 110, '#f3eee6')
            body += bead(cx - 12, 166, 18, '#ffffff', NAIL_S)
            body += timer(x + 40, 92, '3–5 s')
        b += frame(x, 20, 216, 250, t, i + 1, sub=sub or None, body=body, subcol=INK)
    b += text(W / 2, 292, 'Guanti, aspiratore, niente monomero sulla pelle.', 14, weight=700, fill=ERR)
    return svg(W, H + 6, b, 'Come si carica il pennello per l\'acrilico: immergi, scarica, tocca la polvere, perla pronta')


@figx('perla-zone-acrilico.svg')
def acrylic_beads():
    W, H = 940, 360
    b = text(20, 38, 'Dove appoggiare le tre perle', 20, 'start', 800, ACC2)
    for k, (r, lab) in enumerate([(14, 'grande'), (11, 'media'), (8, 'piccola')]):
        lx = 640 + k * 100
        b += bead(lx, 30, r, '#ffffff', NAIL_S) + text(lx + 20, 35, lab, 12.5, 'start', 600, MUTED)
    T = [('Zona 1', 'perla grande sul bordo', 22, '#ffffff'), ('Zona 2', 'perla media al centro', 19, '#f6d6df'),
         ('Zona 3', 'piccola e più umida', 12, '#f6d6df')]
    for i, (t, sub, r, col) in enumerate(T):
        x = 20 + i * 304
        cx, yc = x + 145, 320
        body = ''
        f, p = top_finger(cx, yc, hw=36, nail_len=120, free_len=6, finger_len=20)
        ys = p['y_s'] - 6
        body += form_shape(cx, ys, 100, 140, 38, 44)
        body += f
        if i == 0:
            body += bead(cx, ys - 30, r, col)
        elif i == 1:
            body += bead(cx, ys + 34, r, col)
        else:
            body += bead(cx, yc - 34, r, col)
            body += '<path d="%s" fill="none" stroke="%s" stroke-width="1.6" stroke-dasharray="4 3"/>' % (epo_curve(p, -16), ACC2)
            body += leader(cx + 30, yc - 22, cx + 80, yc - 80, '≈1 mm', 'start', 13)
        b += frame(x, 60, 290, 280, t, sub=sub, body=body, subcol=INK)
    return svg(W, H, b, 'Le tre perle dell\'acrilico: zona 1 sul bordo, zona 2 al centro, zona 3 piccola vicino alla cuticola')



# ================================================================= MODULO LIMATURA
def shape_nail(cx, yc, shape, hw=34, nail_len=90, free_len=60, s=1.0, extra='', finger_len=20, plate=NAIL, free=FREE):
    f, p = finger_nail(0, 0, hw=hw, nail_len=nail_len, free_len=free_len, shape=shape, smile=8, finger_len=finger_len,
                       extra=extra, plate=plate, free=free)
    return '<g transform="translate(%.1f,%.1f) scale(%.3f)">%s</g>' % (cx, yc, s, f), p


def file_bar(x, y, ang, l=120, w=16):
    return tool_file(x, y, ang, l, w)


@figx('forme-scelta-dita.svg')
def shapes_fingers():
    W, H = 940, 360
    b = ''
    rows = [('Dito corto', 'e largo', 46, 70, [('quadrata', False, 'accorcia'), ('ovale', True, 'allunga'), ('mandorla', True, 'slancia')]),
            ('Dito lungo', 'e sottile', 30, 104, [('quadrata', True, 'equilibra'), ('squoval', True, 'equilibra'), ('stiletto', None, 'molto lunga')])]
    for r, (l1, l2, hw, nl, items) in enumerate(rows):
        y0 = 20 + r * 170
        b += '<rect x="20" y="%d" width="900" height="158" rx="16" fill="%s"/>' % (y0, PANEL)
        b += mtext(36, y0 + 72, [l1, l2], 16, 'start', 800, ACC2)
        for k, (sh, ok, eff) in enumerate(items):
            bx = 260 + k * 230
            yy = y0 + 84
            fl = 50 if sh in ('quadrata', 'squoval') else 64
            f, p = horiz_finger(bx - 40, yy, 0.62, hw=hw, nail_len=nl, free_len=fl, shape=sh, finger_len=60)
            b += f
            name = {'quadrata': 'Quadrata', 'ovale': 'Ovale', 'mandorla': 'Mandorla', 'squoval': 'Squoval', 'stiletto': 'Stiletto'}[sh]
            b += text(bx - 22, y0 + 32, name, 14.5, 'start', 800)
            if ok is None:
                b += excl(bx - 38, y0 + 27, 11)
            else:
                b += mark(bx - 38, y0 + 27, ok, 11)
            b += text(bx + 10, y0 + 146, eff, 13, 'middle', 700, OK if ok else (ERR if ok is False else WARN))
    return svg(W, H, b, 'La stessa forma su dita diverse: come cambia l\'effetto su dita corte e larghe o lunghe e sottili')


@figx('forme-resistenza.svg')
def shapes_strength():
    W, H = 940, 260
    b = text(20, 34, 'Dalla più resistente alla più delicata', 20, 'start', 800, ACC2)
    order = [('squoval', 'Squoval'), ('tonda', 'Tonda'), ('ovale', 'Ovale'), ('quadrata', 'Quadrata'), ('mandorla', 'Mandorla'),
             ('ballerina', 'Ballerina'), ('stiletto', 'Stiletto')]
    for k, (sh, name) in enumerate(order):
        cx = 90 + k * 128
        fl = 40 if sh in ('quadrata', 'squoval', 'tonda') else 64
        f, p = shape_nail(cx, 150, sh, 34, 70, fl, 0.75, finger_len=6)
        b += f
        b += text(cx, 196, name, 14, weight=800)
    b += ('<defs><linearGradient id="gres" x1="0" x2="1"><stop offset="0" stop-color="%s"/><stop offset=".5" stop-color="#e8c25a"/>'
          '<stop offset="1" stop-color="%s"/></linearGradient></defs>' % (OK, ERR))
    b += '<rect x="40" y="210" width="860" height="14" rx="7" fill="url(#gres)"/>'
    b += text(40, 250, 'uso intenso delle mani', 13.5, 'start', 700, OK)
    b += text(900, 250, 'serve lunghezza e struttura', 13.5, 'end', 700, ERR)
    return svg(W, H + 14, b, 'Forme dell\'unghia ordinate dalla più resistente alla più delicata')


def step3(title_list, draw, desc, W=940, H=310, oks=(None, None, None)):
    b = ''
    for i, t in enumerate(title_list):
        x = 20 + i * 304
        body = draw(i, x)
        b += frame(x, 20, 290, H - 40, t, i + 1, ok=oks[i], body=body)
    return svg(W, H, arrow_defs() + b, desc)


@figx('quadrata-step.svg')
def square_steps():
    def d(i, x):
        cx, yc = x + 145, 270
        s = ''
        if i < 2:
            f, p = shape_nail(cx, yc, 'quadrata', 38, 100, 70, 1.0, finger_len=10)
            s += f
            yt = yc - 170
            s += dashed(cx, yt - 20, cx, yc + 10, ACC2, 1.4, '5 4')
            if i == 0:
                s += file_bar(cx, yt - 8, 0, 150, 16)
                s += text(cx + 60, yt + 30, '90°', 13, 'start', 800, ACC2)
                s += '<path d="M%d,%d l0,-12 l12,0" fill="none" stroke="%s" stroke-width="1.6"/>' % (cx + 4, yt + 14, ACC2)
            else:
                s += file_bar(cx + 50, yt + 40, 90, 140, 16)
                for sx in (-1, 1):
                    s += dashed(cx + sx * 38, yt - 20, cx + sx * 38, yc - 20, OK, 2, '6 4')
        else:
            sp, p = overlay_profile(0, 0, L=110, free=10, ext=80, apex_h=22, tip=False)
            s += scaled(x + 90, 150, 0.75, sp)
            s += dashed(x + 90 + p['xn'] * 0.75 - 10, 156, x + 90 + p['xb'] * 0.75 + 10, 156, OK, 2, '6 4')
            s += mark(x + 145, 196, True, 12)
            s += '<rect x="%d" y="214" width="180" height="70" rx="10" fill="#fff"/>' % (x + 56)
            s += ('<path d="M%d,%d L%d,%d Q%d,%d %d,%d Z" fill="%s" stroke="%s" stroke-width="1.4"/>'
                  % (x + 80, 236, x + 210, 240, x + 150, 268, x + 80, 244, PROD, PROD_S))
            s += mark(x + 222, 228, False, 10)
            s += text(x + 146, 280, '"pancia" sotto', 12.5, 'middle', 700, ERR)
        return s
    return step3(['Punta dritta', 'Lati paralleli', 'Arco inferiore dritto'], d,
                 'La quadrata: punta dritta, lati paralleli, arco inferiore dritto')


@figx('ovale-step.svg')
def oval_steps():
    def d(i, x):
        cx, yc = x + 145, 270
        s = ''
        sh = 'quadrata' if i < 2 else 'ovale'
        f, p = shape_nail(cx, yc, sh, 38, 100, 70, 1.0, finger_len=10)
        s += f
        yt = yc - 170
        if i == 0:
            s += dashed(cx, yt - 20, cx, yc + 10, ACC2, 1.4, '5 4')
            s += '<circle cx="%d" cy="%d" r="6" fill="%s"/>' % (cx, yt + 2, ERR)
            s += leader(cx + 4, yt + 2, cx + 70, yt + 24, 'centro', 'start', 13)
        elif i == 1:
            s += '<circle cx="%d" cy="%d" r="6" fill="%s"/>' % (cx, yt + 2, ERR)
            s += file_bar(cx - 44, yt + 10, 45, 120, 14)
            s += arrow(cx - 34, yt + 34, cx - 10, yt + 8)
            s += text(cx - 92, yt - 22, '45°', 14, 'end', 800, ACC2)
            s += text(cx + 60, yt + 70, 'una sola', 12.5, 'start', 700, ACC2)
            s += text(cx + 60, yt + 86, 'direzione', 12.5, 'start', 700, ACC2)
        else:
            # curva della cuticola riportata in punta
            s += ('<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="5 4"/>'
                  % (cx - 42, yt + 26, cx, yt - 22, cx + 42, yt + 26, ACC2))
            s += leader(cx + 30, yt + 10, cx + 50, yt + 60, 'specchio', 'start', 12.5)
            s += text(cx + 56, yt + 80, 'della cuticola', 12, 'start', 600)
        return s
    return step3(['Segna il centro', 'Dal lato al centro', 'Arco morbido'], d,
                 'Ovale: segna il centro, lima dal lato verso il centro a 45 gradi, chiudi con un arco morbido', oks=(None, None, True))


@figx('stiletto-step.svg')
def stiletto_steps():
    def d(i, x):
        cx, yc = x + 145, 270
        s = ''
        if i < 2:
            f, p = shape_nail(cx, yc, 'quadrata', 38, 100, 80, 1.0, finger_len=10)
            s += f
            yt = yc - 180
            s += dashed(cx, yt - 16, cx, yc + 10, ACC2, 1.4, '5 4')
            if i == 1:
                ys = yc - 100
                for sx in (-1, 1):
                    s += dashed(cx + sx * 38, ys, cx, yt, ERR, 2, '6 4')
                s += text(cx, yt - 22, 'stesso angolo', 12.5, 'middle', 700, ACC2)
        else:
            f1, _ = shape_nail(x + 85, 220, 'mandorla', 30, 80, 70, 0.9, finger_len=6)
            f2, _ = shape_nail(x + 205, 220, 'stiletto', 30, 80, 80, 0.9, finger_len=6)
            s += f1 + f2
            s += text(x + 85, 248, 'Mandorla', 13, 'middle', 800) + text(x + 205, 248, 'Stiletto', 13, 'middle', 800)
            s += text(x + 115, 272, 'arco inferiore sempre dritto', 12.5, 'middle', 600, MUTED)
        return s
    return step3(['Parti dalla quadrata', 'Stesso angolo', 'Arrotonda o appuntisci'], d,
                 'Mandorla e stiletto: dai lati verso l\'asse con lo stesso angolo', oks=(None, None, True))


@figx('ballerina-step.svg')
def ballerina_steps():
    def d(i, x):
        cx, yc = x + 145, 280
        s = ''
        sh = 'quadrata' if i < 2 else 'ballerina'
        f, p = shape_nail(cx, yc, sh, 36, 90, 100, 1.0, finger_len=10)
        s += f
        yt = yc - 190
        s += dashed(cx, yt - 14, cx, yc + 10, ACC2, 1.4, '5 4') if i < 2 else ''
        if i == 1:
            ys = yc - 90
            for sx in (-1, 1):
                s += dashed(cx + sx * 36, ys - 10, cx + sx * 18, yt, ERR, 2, '6 4')
            s += dashed(cx - 50, yt + 2, cx + 50, yt + 2, ACC2, 2, '3 3')
            s += text(cx + 54, yt + 6, 'taglio', 12.5, 'start', 700, ACC2)
            s += text(cx - 60, ys - 40, 'fermati', 12.5, 'end', 700, ERR)
            s += text(cx - 60, ys - 24, 'prima', 12.5, 'end', 700, ERR)
        elif i == 2:
            s += file_bar(cx, yt - 10, 0, 120, 14)
            s += text(cx + 70, yt + 30, '90°', 13, 'start', 800, ACC2)
        return s
    return step3(['Quadrata lunga', 'Restringi i lati', 'Punta dritta'], d,
                 'Ballerina: lati che si restringono e punta dritta', oks=(None, None, True))


def op_hand_file(cx, cy):
    """Mano dell'operatrice che tiene la lima (vista di lato, schematica)."""
    st = 'fill="%s" stroke="%s" stroke-width="1.5"' % (SKIN, SKIN_D)
    s = '<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" %s/>' % (cx - 170, cy + 70, cx - 110, cy + 20, cx - 80, cy + 60, cx - 150, cy + 112, st)
    s += '<ellipse cx="%d" cy="%d" rx="62" ry="38" transform="rotate(-18 %d %d)" %s/>' % (cx - 78, cy + 14, cx - 78, cy + 14, st)
    s += '<rect x="%d" y="%d" width="74" height="20" rx="10" transform="rotate(-6 %d %d)" %s/>' % (cx - 62, cy + 10, cx - 62, cy + 20, st)
    s += tool_file(cx + 30, cy, 0, 230, 20)
    for k in range(3):
        s += '<rect x="%d" y="%d" width="%d" height="18" rx="9" %s/>' % (cx - 96 + k * 8, cy - 24 - k * 3, 100 - k * 14, st)
    s += '<ellipse cx="%d" cy="%d" rx="14" ry="10" %s/>' % (cx + 8, cy - 14, st)
    return s


@figx('lima-presa.svg')
def file_grip():
    W, H = 760, 350
    b = ''
    body = op_hand_file(x := 20 + 190, 150)
    body += leader(x - 20, 124, x + 40, 84, 'presa leggera', 'start', 13.5)
    body += leader(x - 120, 200, x - 70, 262, 'polso morbido', 'start', 13.5)
    body += arrow(x + 70, 196, x + 150, 196, MUTED, 1.6, True)
    body += text(x + 110, 220, 'muovi il braccio', 12.5, 'middle', 600, MUTED)
    b += frame(20, 20, 350, 310, 'La lima', 1, body=body)
    # 2 dito della cliente
    x = 390
    cx, yc = x + 130, 230
    body = '<rect x="%d" y="%d" width="190" height="60" rx="20" fill="#e9dff2" stroke="#b9a6cf"/>' % (cx - 95, yc + 10)
    body += text(cx + 40, yc + 62, 'supporto', 12.5, 'middle', 700, '#6b4fa0')
    f, p = top_finger(cx, yc, hw=34, nail_len=110, free_len=40, shape='squoval', finger_len=40)
    body += f
    for sx in (-1, 1):
        body += '<ellipse cx="%d" cy="%d" rx="20" ry="30" fill="%s" stroke="%s" stroke-width="1.5"/>' % (cx + sx * 66, yc - 20, '#efc0a4', SKIN_D)
    body += arrow(cx - 70, yc - 54, cx - 82, yc - 80, ACC2, 1.8)
    body += leader(cx + 70, yc - 20, cx + 116, yc - 34, 'tieni', 'start', 12.5)
    body += text(cx + 122, yc - 13, 'ai lati', 12.5, 'start', 600)
    body += text(cx - 82, yc - 104, 'tira la pelle', 12.5, 'middle', 700, ACC2)
    body += text(cx - 82, yc - 88, 'del solco', 12.5, 'middle', 700, ACC2)
    # riquadro errore
    body += '<rect x="%d" y="70" width="84" height="104" rx="10" fill="#fff"/>' % (x + 252)
    g, _ = top_finger(0, 0, hw=34, nail_len=90, free_len=20, finger_len=10)
    g += '<ellipse cx="6" cy="-60" rx="28" ry="32" fill="#efc0a4" stroke="%s" stroke-width="1.5"/>' % SKIN_D
    body += scaled(x + 294, 160, 0.55, g)
    body += mark(x + 322, 86, False, 10)
    b += frame(x, 20, 350, 310, 'Il dito della cliente', 2, body=body)
    return svg(W, H, arrow_defs() + b, 'Presa della lima e del dito della cliente durante la limatura')


@figx('limatura-sequenza.svg')
def file_sequence():
    labels = ['Lunghezza', 'Lati', 'Punta', 'Superficie', 'Zona cuticolare', 'Sotto il bordo']
    subs = ['100/180', 'piatta, parallela', 'una direzione', 'segui la curva', 'sfuma a zero', 'pulisci']

    def d(i, x, y):
        s = ''
        cx, yb = x + 120, y + 178
        if i in (0, 1, 2, 4):
            g, p = finger_nail(0, 0, hw=34, nail_len=90, free_len=60, shape='squoval' if i != 2 else 'ovale', smile=8, finger_len=6)
            yt = -150
            if i == 0:
                g += tool_file(0, yt - 10, 0, 130, 16)
            elif i == 1:
                g += tool_file(48, yt + 60, 90, 130, 16)
            elif i == 2:
                g += tool_file(-40, yt + 10, 45, 110, 14)
                g += arrow(-70, yt + 50, -14, yt + 4, ACC2, 2.6)
            else:
                g += tool_file(30, -40, -60, 90, 14)
                g += '<path d="%s" fill="none" stroke="%s" stroke-width="3" stroke-dasharray="5 4"/>' % (epo_curve(p, -16), ACC2)
            s += scaled(cx, yb, 0.62, g)
        elif i == 3:
            sp, p = overlay_profile(0, 0, L=110, free=10, ext=70, apex_h=22, tip=False)
            s += scaled(x + 70, y + 140, 0.62, sp)
            s += ('<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="%s" stroke-width="2.2" marker-end="url(#ar)"/>'
                  % (x + 80, y + 116, x + 140, y + 92, x + 200, y + 118, ACC2))
        else:
            # vista dal basso: polpastrello e bordo libero
            s += '<rect x="%d" y="%d" width="70" height="120" rx="34" fill="%s" stroke="%s" stroke-width="1.5"/>' % (cx - 35, y + 76, SKIN, SKIN_D)
            s += '<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="%s" stroke="%s" stroke-width="1.5"/>' % (
                cx - 42, y + 92, cx - 42, y + 62, cx, y + 54, cx + 42, y + 62, cx + 42, y + 92, cx, y + 80, cx - 42, y + 92, FREE, NAIL_S)
            s += rot(-20, cx + 30, y + 74, tool_file(cx + 60, y + 74, 0, 100, 14))
            s += text(cx - 66, y + 160, 'dal basso', 12, 'end', 600, MUTED)
        s += text(x + 260, y + 30, subs[i], 12.5, 'end', 700, MUTED)
        return s
    return steps_fig('La sequenza di limatura', labels, 3, 290, 190, d, 'La sequenza di limatura in sei passaggi')


@figx('limatura-arco-profilo.svg')
def file_arcs():
    W, H = 760, 310
    b = text(20, 38, 'Il profilo dopo la limatura', 20, 'start', 800, ACC2)
    s, p = overlay_profile(150, 170, L=190, free=16, ext=150, apex_h=32, tip=False)
    b += s
    xa, ax, xb, xe, oy, xn = p['xa'], p['ax'], p['xb'], p['xe'], p['oy'], p['xn']
    b += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="4" stroke-linecap="round"/>'
          % (ax, oy - 32, (ax + xb) / 2 + 20, oy - 32, xb, oy - 4, ACC2))
    b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="4" stroke-linecap="round"/>' % (xn, oy + 6, xb, oy + 5, OK)
    b += '<circle cx="%.1f" cy="%.1f" r="5" fill="%s"/>' % (xe, oy + 6, ERR)
    b += leader(ax, oy - 32, ax - 30, 80, 'apex', 'middle', 14)
    b += text(xb - 40, 112, 'arco superiore', 14, 'middle', 800, ACC2)
    b += text(xb - 40, oy + 34, 'arco inferiore dritto', 14, 'middle', 800, OK)
    b += leader(xe, oy + 6, xe - 70, oy + 90, 'punto di stress', 'end', 13, fill=ERR)
    # errore
    b += '<rect x="560" y="200" width="180" height="96" rx="12" fill="%s"/>' % PANEL
    s2, p2 = overlay_profile(0, 0, L=80, free=8, ext=60, apex_h=10, tip=False)
    b += scaled(640, 248, 0.6, s2)
    b += mark(724, 216, False, 10)
    b += text(650, 288, 'apex limato via', 13, 'middle', 800, ERR)
    return svg(W, H, b, 'Profilo dopo la limatura: arco superiore dall\'apex alla punta e arco inferiore dritto')


@figx('controllo-4-viste.svg')
def check4():
    W, H = 940, 350
    b = ''
    T = [('Dall\'alto', 'simmetria'), ('Di profilo', 'apex'), ('Dal davanti', 'curva a C'), ('Dal basso', 'pulizia del bordo')]
    for i, (t, sub) in enumerate(T):
        x = 20 + i * 228
        cx = x + 108
        body = ''
        if i == 0:
            f, p = shape_nail(cx, 270, 'ovale', 34, 90, 70, 1.0, finger_len=10)
            body += f + dashed(cx, 90, cx, 280, ACC2, 1.6, '5 4')
        elif i == 1:
            sp, p = overlay_profile(0, 0, L=100, free=10, ext=70, apex_h=22, tip=False)
            sp += '<circle cx="%.1f" cy="6" r="5" fill="%s"/>' % (p['xe'], ERR)
            body += scaled(x + 76, 190, 0.66, sp)
        elif i == 2:
            body += c_arc(cx, 210, 74, 32)
            body += ('<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="%s" stroke-width="6" stroke-linecap="round"/>'
                     % (cx - 66, 214, cx, 146, cx + 66, 214, NAIL_S))
        else:
            body += '<rect x="%d" y="140" width="76" height="150" rx="36" fill="%s" stroke="%s" stroke-width="1.5"/>' % (cx - 38, SKIN, SKIN_D)
            body += ('<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
                     % (cx - 46, 170, cx - 46, 100, cx, 86, cx + 46, 100, cx + 46, 170, cx, 150, cx - 46, 170, FREE, NAIL_S))
            body += mark(cx + 62, 120, True, 11)
        b += frame(x, 20, 216, 310, t, sub=sub, body=body, subcol=INK)
        b += eye(x + 26, 46, 0, 0.9)
    return svg(W, H, b, 'Le quattro viste del controllo finale: alto, profilo, davanti, basso')


def free_edge_path(cx, ys, hw, tip_x, tip_y):
    return ('<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.8"/>'
            % (cx - hw, ys, cx - hw, ys - 50, tip_x - hw * 0.55, tip_y, tip_x, tip_y, tip_x + hw * 0.55, tip_y, cx + hw, ys - 50, cx + hw, ys, FREE, NAIL_S))


@figx('simmetria-asse.svg')
def symmetry():
    W, H = 760, 350
    b = ''
    for i, (t, ok) in enumerate([('Punta centrata', True), ('Punta spostata', False)]):
        x = 20 + i * 370
        cx, yc = x + 160, 300
        body = ''
        f, p = top_finger(cx, yc, hw=40, nail_len=120, free_len=0, finger_len=20)
        ys = p['y_s'] + 4
        shift = 0 if ok else 22
        body += free_edge_path(cx, ys, 40, cx + shift, ys - 100) + f
        body += dashed(cx, ys - 120, cx, yc + 10, ACC2, 1.6, '5 4')
        yy = ys - 40
        lw = 40 if ok else 32
        rw = 40 if ok else 46
        body += dim(cx - lw, yy, cx, yy, '', 'above', OK if ok else ERR)
        body += dim(cx, yy, cx + rw, yy, '', 'above', OK if ok else ERR)
        body += text(cx, yy - 16, '=' if ok else '≠', 20, 'middle', 800, OK if ok else ERR)
        if not ok:
            body += arrow(cx + 110, ys - 70, cx + 50, ys - 60, ERR, 2)
            body += text(cx + 114, ys - 74, 'lima qui', 13, 'start', 800, ERR)
            body += '<circle cx="%d" cy="%d" r="5" fill="%s"/>' % (cx + shift, ys - 100, ERR)
        b += frame(x, 20, 350, 310, t, ok=ok, body=body)
    return svg(W, H, arrow_defs() + b, 'Simmetria rispetto all\'asse del dito: punta centrata e punta spostata')


def hand_top(x0, yb, nails):
    """Mano vista dall'alto: nails = lista di (forma, lunghezza bordo libero) per pollice→mignolo."""
    s = '<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Z" fill="%s" stroke="%s" stroke-width="1.5"/>' % (
        x0 + 40, yb + 60, x0 + 40, yb - 10, x0 + 160, yb - 30, x0 + 300, yb - 10, x0 + 300, yb + 60, SKIN, SKIN_D)
    pos = [(x0 + 30, yb + 10, -38, 0.5), (x0 + 96, yb - 40, -6, 0.5), (x0 + 160, yb - 56, 0, 0.5), (x0 + 224, yb - 46, 5, 0.5), (x0 + 284, yb - 18, 12, 0.46)]
    tips = []
    for k, ((sh, fl), (fx, fy, ang, sc)) in enumerate(zip(nails, pos)):
        g, p = finger_nail(0, 0, hw=34, nail_len=80, free_len=fl, shape=sh, smile=8, finger_len=150)
        s += '<g transform="translate(%d,%d) rotate(%d) scale(%.2f)">%s</g>' % (fx, fy - 40, ang, sc, g)
        a = math.radians(ang)
        ty = -80 - fl
        tips.append((fx - ty * sc * math.sin(a), fy - 40 + ty * sc * math.cos(a)))
    return s, tips


@figx('mano-uniformita.svg')
def hand_uniform():
    W, H = 940, 400
    b = ''
    for i, (t, ok) in enumerate([('Uniformi', True), ('Lunghezze e forme diverse', False)]):
        x = 20 + i * 460
        nails = [('ovale', 46)] * 5 if ok else [('ovale', 46), ('ovale', 46), ('ovale', 80), ('quadrata', 40), ('ovale', 46)]
        hs, tips = hand_top(x + 60, 250, nails)
        body = hs
        if ok:
            pts = ' '.join('%.1f,%.1f' % tp for tp in tips[1:])
            body += '<polyline points="%s" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="6 4"/>' % (pts, OK)
        else:
            for k in (2, 3):
                tx, ty = tips[k]
                body += '<circle cx="%.1f" cy="%.1f" r="24" fill="none" stroke="%s" stroke-width="3"/>' % (tx, ty + 14, ERR)
        b += frame(x, 20, 440, 290, t, ok=ok, body=body)
    # pugno
    b += '<rect x="250" y="322" width="440" height="66" rx="14" fill="%s"/>' % PANEL
    b += text(266, 360, 'Pugno:', 15, 'start', 800, ACC2)
    for k in range(4):
        cx = 360 + k * 66
        b += ('<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="%s" stroke-width="8" stroke-linecap="round"/>'
              % (cx - 28, 372, cx, 336, cx + 28, 372, ACC))
    b += text(680, 382, 'curve allineate', 12, 'end', 600, MUTED)
    return svg(W, H, b, 'Uniformità della mano: lunghezza, forma e curva coerenti su tutte le dita')


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
