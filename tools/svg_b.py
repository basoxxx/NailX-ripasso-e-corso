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
BED = '#f2a3b6'       # letto ungueale visto in sezione


# ================================================================= definizioni locali (gradienti e texture)
# Vengono inserite una sola volta per figura, solo se usate (vedi svg() qui sotto).
LOCAL_DEFS = {
    'bSkinV': '<linearGradient id="bSkinV" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f9e0d1"/>'
              '<stop offset=".4" stop-color="#f3cdb6"/><stop offset="1" stop-color="#dcab92"/></linearGradient>',
    'bTipG': '<linearGradient id="bTipG" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ddd3c4"/>'
             '<stop offset=".3" stop-color="#fbf8f3"/><stop offset=".7" stop-color="#f3eee6"/><stop offset="1" stop-color="#d6cbbb"/></linearGradient>',
    'bTipV': '<linearGradient id="bTipV" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fbf8f3"/>'
             '<stop offset="1" stop-color="#e2d8c9"/></linearGradient>',
    'bProdV': '<linearGradient id="bProdV" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1f8fd"/>'
              '<stop offset="1" stop-color="#c6dfee"/></linearGradient>',
    'bHandle': '<linearGradient id="bHandle" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a7480"/>'
               '<stop offset=".35" stop-color="#4b3a40"/><stop offset="1" stop-color="#271b20"/></linearGradient>',
    'bFerrule': '<linearGradient id="bFerrule" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4f6f8"/>'
                '<stop offset=".45" stop-color="#bfc7cf"/><stop offset="1" stop-color="#848d96"/></linearGradient>',
    'bGrip': '<linearGradient id="bGrip" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e48aa8"/>'
             '<stop offset="1" stop-color="#a8476a"/></linearGradient>',
    'bForm': '<linearGradient id="bForm" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fbf0c4"/>'
             '<stop offset="1" stop-color="#f1df98"/></linearGradient>',
    'bGlass': '<linearGradient id="bGlass" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9eef3"/>'
              '<stop offset=".25" stop-color="#ffffff"/><stop offset=".75" stop-color="#f7f9fb"/><stop offset="1" stop-color="#dfe5eb"/></linearGradient>',
    'bGritC': '<pattern id="bGritC" width="6" height="6" patternUnits="userSpaceOnUse">'
              '<circle cx="1.2" cy="1.3" r=".95" fill="#000" fill-opacity=".26"/><circle cx="4.2" cy="3.6" r=".9" fill="#fff" fill-opacity=".38"/>'
              '<circle cx="2.4" cy="5" r=".7" fill="#000" fill-opacity=".2"/><circle cx="5.3" cy=".6" r=".6" fill="#fff" fill-opacity=".3"/></pattern>',
    'bGritF': '<pattern id="bGritF" width="4" height="4" patternUnits="userSpaceOnUse">'
              '<circle cx="1" cy="1" r=".5" fill="#000" fill-opacity=".22"/><circle cx="3" cy="2.6" r=".5" fill="#fff" fill-opacity=".35"/>'
              '<circle cx="1.8" cy="3.4" r=".4" fill="#000" fill-opacity=".16"/></pattern>',
    'bKnurl': '<pattern id="bKnurl" width="3" height="3" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
              '<line x1="0" y1="0" x2="0" y2="3" stroke="#4f5860" stroke-width=".7" stroke-opacity=".55"/>'
              '<line x1="0" y1="0" x2="3" y2="0" stroke="#4f5860" stroke-width=".7" stroke-opacity=".55"/></pattern>',
}


def svg(w, h, body, title):
    """Come gen_svg.svg, ma aggiunge (una volta sola) le definizioni locali usate nella figura."""
    used = [k for k in LOCAL_DEFS if 'url(#%s)' % k in body]
    if used:
        body = '<defs>%s</defs>' % ''.join(LOCAL_DEFS[k] for k in used) + body
    return gen_svg.svg(w, h, body, title)


def steps_fig(title, labels, cols, pw, ph, draw, desc, top=60, subs=None):
    """Variante locale di gen_svg.steps_fig (usa svg() locale; sottotitolo opzionale a destra del titolo)."""
    rows = (len(labels) + cols - 1) // cols
    W = 20 + cols * (pw + 14) + 6
    H = top + rows * (ph + 14) + 6
    b = text(20, 38, title, 20, 'start', 800, ACC2)
    for i, lab in enumerate(labels):
        x = 20 + (i % cols) * (pw + 14)
        y = top + (i // cols) * (ph + 14)
        pc = uid('p')
        b += '<defs><clipPath id="%s"><rect x="%d" y="%d" width="%d" height="%d" rx="16"/></clipPath></defs>' % (pc, x, y, pw, ph)
        b += panel(x, y, pw, ph, lab, i + 1, ACC2)
        b += '<g clip-path="url(#%s)">%s</g>' % (pc, draw(i, x, y))
    return svg(W, H, arrow_defs() + b, desc)


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


def callout(px, py, lx, ly, label, anchor='start', size=13, fill=INK, weight=700, sub=None):
    """Richiamo pulito: pallino sul punto (px, py), linea che si ferma al bordo del testo (lx, ly = linea di base)."""
    if anchor == 'middle':
        ey = ly + 5 if py > ly else ly - size - 1
        ex = lx
    else:
        ex = lx - 5 if anchor == 'start' else lx + 5
        ey = ly - size * 0.36
    s = ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.3"/>'
         '<circle cx="%.1f" cy="%.1f" r="3.5" fill="%s" stroke="#fff" stroke-width="1"/>' % (px, py, ex, ey, MUTED, px, py, ACC2))
    if sub and anchor == 'middle' and py > ly:
        s = s.replace('y2="%.1f"' % ey, 'y2="%.1f"' % (ey + size + 4), 1)
    s += text(lx, ly, label, size, anchor, weight, fill)
    if sub:
        s += text(lx, ly + size + 3, sub, 12, anchor, 400, MUTED)
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
    # sagoma unica: dorso, piega dell'eponichio (morbida), letto, polpastrello arrotondato
    s = ('<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f '
         'C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" '
         'fill="url(#bSkinV)" stroke="%s" stroke-width="1.5" stroke-linejoin="round"/>'
         % (x - 110, y - 12, x - 60, y - 15, x - 18, y - 16, x - 4, y - 12,
            x + 6, y - 9, x + 10, y - 4, x + 12, y + 1, xe, y + 6,
            xe + 18, y + 9, xe + 22, y + 46, xe - 4, y + 64,
            xe - 26, y + 80, x - 30, y + 82, x - 110, y + 82, x - 110, y + 82, SKIN_D))
    # pieghe della pelle sul dorso (articolazione) e del polpastrello
    s += ('<path d="M%.1f,%.1f q8,6 4,14 M%.1f,%.1f q8,6 4,14" fill="none" stroke="%s" stroke-width="1.1" opacity=".6"/>'
          % (x - 92, y - 11, x - 84, y - 11, SKIN_D))
    if plate:
        # letto ungueale rosato sotto la lamina
        s += ('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" opacity=".55"/>'
              % (x + 12, y + 5, xe - 2, y + 6, xe - 6, y + 10, x + 12, y + 9, BED))
        s += ('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.3" stroke-linejoin="round"/>'
              % (x + 9, y + 0.5, xe, y + 1, xe, y + 6, x + 11, y + 5, NAIL, NAIL_S))
        if free:
            s += ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.3" stroke-linejoin="round"/>'
                  % (xe, y + 1, xe + free - 1, y + 1 + tip_down, xe + free + 1, y + 3.5 + tip_down, xe + free - 1, y + 6 + tip_down,
                     xe, y + 6, free_col, NAIL_S))
        # riflesso sulla lamina e bordo della piega
        s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#fff" stroke-width="1.2" opacity=".7"/>' % (x + 16, y + 2, xe - 6, y + 2.6)
        s += ('<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="1.5"/>'
              % (x - 4, y - 12, x + 6, y - 9, x + 10, y - 4, x + 12, y + 1, SKIN_D))
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


# ---------------------------------------------------------------- strumenti realistici (varianti locali)
# Stessa firma delle primitive di gen_svg (che restano invariate per gli altri file): qui le ridefiniamo
# con più dettaglio (grana, ghiera, setole, zigrinatura) solo per le figure del gruppo B.
def _g(x, y, ang, s, body):
    return '<g transform="translate(%.1f,%.1f) rotate(%.1f)%s">%s</g>' % (x, y, ang, (' scale(%.2f)' % s) if s != 1 else '', body)


def tool_file(x, y, ang=0, l=150, w=22, c1='#8a7d74', c2='#d9cfc6', grit=None):
    """Lima a due facce vista leggermente di taglio: faccia c1 sopra, c2 sotto, anima chiara, grana visibile.
    (x, y) = centro della lima."""
    g = grit or ('bGritC' if w >= 18 else 'bGritF')
    c = uid('fl')
    r = w * 0.48
    out = 'M%.1f,%.1f h%.1f a%.1f,%.1f 0 0 1 0,%.1f h%.1f a%.1f,%.1f 0 0 1 0,%.1f Z' % (
        -l / 2 + r, -w / 2, l - 2 * r, r, w / 2, w, -(l - 2 * r), r, w / 2, -w)
    s = '<defs><clipPath id="%s"><path d="%s"/></clipPath></defs>' % (c, out)
    s += '<path d="%s" fill="#efe7de"/>' % out
    s += '<g clip-path="url(#%s)">' % c
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (-l / 2, -w / 2, l, w / 2 - 0.9, c1)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#%s)"/>' % (-l / 2, -w / 2, l, w / 2 - 0.9, g)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (-l / 2, 0.9, l, w / 2, c2)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#%s)"/>' % (-l / 2, 0.9, l, w / 2, g)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="1.2" fill="#fff" opacity=".35"/>' % (-l / 2, -w / 2 + 1, l)
    s += '</g><path d="%s" fill="none" stroke="#6d6058" stroke-width=".9" stroke-opacity=".7"/>' % out
    return _g(x, y, ang, 1, s)


def tool_pusher(x, y, ang=0, l=150):
    """Spingicuticole in acciaio: paletta a cucchiaio in (x, y) (estremità a -24), manico zigrinato verso +x."""
    s = '<rect x="14" y="-4.5" width="%.1f" height="9" rx="4.5" fill="#9aa3ad" stroke="#5d666f" stroke-width=".7"/>' % (l - 14)
    s += '<rect x="%.1f" y="-4.5" width="%.1f" height="9" fill="url(#bKnurl)"/>' % (14 + l * 0.22, l * 0.5)
    s += '<rect x="%.1f" y="-4.5" width="1.6" height="9" fill="#5d666f"/><rect x="%.1f" y="-4.5" width="1.6" height="9" fill="#5d666f"/>' % (
        14 + l * 0.22, 14 + l * 0.72)
    s += '<line x1="16" y1="-2.4" x2="%.1f" y2="-2.4" stroke="#fff" stroke-width="1.2" opacity=".55" stroke-linecap="round"/>' % (l - 2)
    s += '<path d="M0,-2.2 L16,-3.4 L16,3.4 L0,2.2 Z" fill="#9aa3ad" stroke="#5d666f" stroke-width=".7"/>'
    s += ('<path d="M1,-2.6 C-6,-4 -14,-11 -21,-10.5 Q-27,0 -21,10.5 C-14,11 -6,4 1,2.6 Z" fill="#9aa3ad" stroke="#4f5860" stroke-width=".9"/>'
          '<path d="M-4,-3 C-10,-6 -16,-8 -20,-7" fill="none" stroke="#fff" stroke-width="1.2" opacity=".7" stroke-linecap="round"/>')
    return _g(x, y, ang, 1, s)


def tool_brush(x, y, ang=0, l=140, bristle=ACC):
    """Pennello: setole (punta a circa -18) con ciuffo e fibre, ghiera metallica, manico laccato affusolato."""
    hl = l + 4
    s = ('<path d="M22,-5 L%.1f,-3.4 Q%.1f,0 %.1f,3.4 L22,5 Z" fill="url(#bHandle)"/>' % (22 + hl, 26 + hl, 22 + hl))
    s += '<line x1="26" y1="-2.6" x2="%.1f" y2="-1.6" stroke="#fff" stroke-width="1.1" opacity=".35" stroke-linecap="round"/>' % (16 + hl)
    s += ('<path d="M8,-6 L24,-5.6 L24,5.6 L8,6 Z" fill="url(#bFerrule)" stroke="#7d868f" stroke-width=".6"/>'
          '<path d="M12,-6 v12 M15,-5.9 v11.8" stroke="#7d868f" stroke-width=".8"/>')
    s += ('<path d="M9,-5.6 C2,-6.4 -8,-5.6 -15,-2.2 Q-20,0 -15,2.2 C-8,5.6 2,6.4 9,5.6 Z" fill="%s" stroke="%s" stroke-opacity=".35" stroke-width=".8"/>'
          % (bristle, INK))
    s += ('<path d="M8,-3 L-10,-1.6 M8,0 L-14,0 M8,3 L-10,1.6" stroke="#fff" stroke-width=".7" opacity=".45"/>'
          '<path d="M8,-4.6 L-6,-3.6" stroke="%s" stroke-opacity=".25" stroke-width=".7"/>' % INK)
    return _g(x, y, ang, 1, s)


def tool_curette(x, y, ang=0, l=130):
    """Curette: cucchiaino affilato in (x, y), manico zigrinato verso +x."""
    s = '<rect x="14" y="-4.5" width="%d" height="9" rx="4.5" fill="#9aa3ad" stroke="#5d666f" stroke-width=".7"/>' % l
    s += '<rect x="%.1f" y="-4.5" width="%.1f" height="9" fill="url(#bKnurl)"/>' % (14 + l * 0.25, l * 0.5)
    s += '<line x1="16" y1="-2.4" x2="%.1f" y2="-2.4" stroke="#fff" stroke-width="1.2" opacity=".55" stroke-linecap="round"/>' % (l + 10)
    s += ('<path d="M16,-2.6 L4,-1.8 Q-4,-6.5 -10,-1.5 Q-11,0 -10,1.5 Q-4,6.5 4,1.8 L16,2.6 Z" fill="#9aa3ad" stroke="#4f5860" stroke-width=".9"/>'
          '<path d="M-8,-1 Q-3,-4 2,-1.6" fill="none" stroke="#fff" stroke-width="1" opacity=".7"/>')
    return _g(x, y, ang, 1, s)


def tool_nipper(x, y, ang=0, s=1.0):
    """Tronchesina per cuticole: becco affilato in (x, y), snodo, molla doppia, manici verso +x."""
    half = ('<path d="M0,-0.6 Q8,-8 24,-8.5 L31,-4 L8,-0.6 Z" fill="F1" stroke="#4f5860" stroke-width=".8"/>'
            '<path d="M34,-3 Q60,-22 108,-21 Q115,-19 113,-14 Q74,-12 37,4 Z" fill="F1" stroke="#4f5860" stroke-width=".8"/>'
            '<path d="M40,-6 Q70,-18 106,-17.5" fill="none" stroke="#fff" stroke-width="1.1" opacity=".5"/>')
    b = half.replace('F1', '#9aa3ad')
    b += '<g transform="scale(1,-1)">%s</g>' % half.replace('F1', '#6f7983')
    b += '<path d="M44,-7 C60,-4 60,4 44,7 M48,-8 C66,-4 66,4 48,8" fill="none" stroke="#c9d0d7" stroke-width="1.8"/>'
    b += '<circle cx="31" cy="0" r="6.5" fill="#6f7983" stroke="#4f5860"/><circle cx="31" cy="0" r="2.2" fill="#e3e8ec"/>'
    b += '<line x1="2" y1="0" x2="26" y2="0" stroke="#e8edf2" stroke-width="1"/>'
    return _g(x, y, ang, s, b)


def tool_tipcutter(x, y, ang=0, s=1.0):
    """Tagliatip a ghigliottina visto dall'alto: lama dritta lungo l'asse y passante per (x, y), manici verso +x."""
    b = ('<path d="M10,-22 L84,-30 Q94,-30 94,-22 L94,-18 L16,-8 Z" fill="url(#bGrip)" stroke="#8e3b5a" stroke-width=".8"/>'
         '<path d="M10,22 L84,30 Q94,30 94,22 L94,18 L16,8 Z" fill="url(#bGrip)" stroke="#8e3b5a" stroke-width=".8"/>'
         '<path d="M20,-6 C34,-2 34,2 20,6" fill="none" stroke="#c9d0d7" stroke-width="2"/>')
    b += '<rect x="-9" y="-34" width="26" height="68" rx="7" fill="#9aa3ad" stroke="#4f5860" stroke-width=".9"/>'
    b += '<rect x="-4" y="-29" width="7" height="58" rx="2" fill="#3d454c"/>'
    b += '<line x1="-0.5" y1="-28" x2="-0.5" y2="28" stroke="#e8edf2" stroke-width="1.6"/>'
    b += '<circle cx="10" cy="-26" r="2.4" fill="#e3e8ec" stroke="#4f5860" stroke-width=".6"/><circle cx="10" cy="26" r="2.4" fill="#e3e8ec" stroke="#4f5860" stroke-width=".6"/>'
    return _g(x, y, ang, s, b)


def tool_scissors(x, y, ang=0, s=1.0):
    """Forbicine da cuticole: lame sottili e curve con punte in (x, y), anelli verso +x."""
    blade = ('<path d="M0,-0.4 Q16,-6.5 36,-5.5 L38,-1 Q18,-2 0,-0.4 Z" fill="F1" stroke="#4f5860" stroke-width=".7"/>'
             '<path d="M39,-3 Q46,-8 51,-12" stroke="F1" stroke-width="4.2" stroke-linecap="round" fill="none"/>'
             '<ellipse cx="60" cy="-15" rx="10" ry="8" fill="none" stroke="F1" stroke-width="4"/>'
             '<ellipse cx="60" cy="-15" rx="10" ry="8" fill="none" stroke="#4f5860" stroke-width=".7" stroke-opacity=".6"/>')
    b = blade.replace('F1', '#9aa3ad')
    b += '<g transform="scale(1,-1)">%s</g>' % blade.replace('F1', '#6f7983')
    b += '<circle cx="38" cy="0" r="3.2" fill="#e3e8ec" stroke="#4f5860" stroke-width=".7"/>'
    return _g(x, y, ang, s, b)


def tool_pencil(x, y, ang=0, l=110):
    """Matita: punta in (x, y)."""
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f)"><path d="M0,0 L16,-6 L16,6 Z" fill="#e8c9a0"/>'
            '<path d="M0,0 L6,-2.3 L6,2.3 Z" fill="%s"/><rect x="16" y="-6" width="%d" height="12" fill="#f0b43c"/>'
            '<rect x="%d" y="-6" width="12" height="12" rx="2" fill="#e88a9c"/></g>' % (x, y, ang, INK, l, 16 + l))


def bottle(cx, yb, liquid='#cfe6f7', label='', w=40, h=56, cap=True):
    """Flacone in vetro con spalle arrotondate, liquido, riflesso ed etichetta; tappo nero zigrinato. yb = base."""
    x0, x1, yt = cx - w / 2, cx + w / 2, yb - h
    sh = min(10, h * 0.2)
    body = ('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f '
            'L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z' % (
                x0, yb - 6, x0, yb, x0 + 6, yb, x1 - 6, yb, x1, yb, x1, yb - 6, x1, yt + sh, x1, yt, x1 - sh, yt,
                x0 + sh, yt, x0, yt, x0, yt + sh))
    c = uid('bt')
    s = '<defs><clipPath id="%s"><path d="%s"/></clipPath></defs>' % (c, body)
    s += '<path d="%s" fill="url(#bGlass)"/>' % body
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" clip-path="url(#%s)"/>' % (x0, yb - h * 0.66, w, h, liquid, c)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="2" fill="#fff" opacity=".6" clip-path="url(#%s)"/>' % (x0, yb - h * 0.66, w, c)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="2" fill="#fff" opacity=".7"/>' % (x0 + w * 0.14, yt + 6, max(3, w * 0.09), h - 14)
    s += '<path d="%s" fill="none" stroke="%s" stroke-width="1.5"/>' % (body, '#8d8a96')
    if cap:
        cw = w * 0.46
        s += '<rect x="%.1f" y="%.1f" width="%.1f" height="5" fill="#cfd5db" stroke="#8d8a96" stroke-width=".8"/>' % (cx - cw / 2 - 2, yt - 5, cw + 4)
        s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="url(#bHandle)"/>' % (cx - cw / 2, yt - 5 - h * 0.48, cw, h * 0.48)
        for k in range(1, 4):
            xx = cx - cw / 2 + k * cw / 4
            s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#fff" stroke-opacity=".18" stroke-width="1"/>' % (xx, yt - 3 - h * 0.48, xx, yt - 7)
    if label:
        s += '<rect x="%.1f" y="%.1f" width="%.1f" height="18" rx="4" fill="#fff" opacity=".9"/>' % (cx - w * 0.38, yb - h * 0.36 - 12, w * 0.76)
        s += text(cx, yb - h * 0.36 + 1.5, label, 12, weight=800, fill=INK)
    return s


def drop_c(cx, cy, col, stroke=None, s=1.0):
    return ('<path d="M%.1f,%.1f q%.1f,%.1f 0,%.1f q%.1f,%.1f 0,%.1f z" fill="%s" stroke="%s"/>'
            % (cx, cy - 10 * s, 8 * s, 12 * s, 19 * s, -8 * s, -7 * s, -19 * s, col, stroke or col))


def desk_lamp(x, y, s=1.0):
    """Lampada da tavolo a braccio snodato; (x, y) = centro della testa (luce verso destra/basso)."""
    return ('<g transform="translate(%.1f,%.1f) scale(%.2f)">'
            '<ellipse cx="-26" cy="100" rx="24" ry="5" fill="#000" opacity=".12"/>'
            '<rect x="-48" y="92" width="44" height="9" rx="4.5" fill="url(#bHandle)"/>'
            '<path d="M-26,94 L-38,42 L-4,2" stroke="#8d969f" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
            '<circle cx="-38" cy="42" r="4" fill="#6f7983"/><circle cx="-26" cy="94" r="3.5" fill="#6f7983"/>'
            '<path d="M-12,-16 L26,-6 Q22,14 14,26 Z" fill="%s" stroke="#6b2a44" stroke-width="1"/>'
            '<path d="M-8,-11 L20,-4" stroke="#fff" stroke-width="1.6" opacity=".45" stroke-linecap="round"/>'
            '<ellipse cx="20" cy="10" rx="5" ry="15" transform="rotate(-18 20 10)" fill="%s"/>'
            '<ellipse cx="20" cy="10" rx="2.5" ry="9" transform="rotate(-18 20 10)" fill="#fff8d6"/></g>'
            % (x, y, s, ACC2, LIGHT))


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
        s += f + tool_brush(x + 12, y - 16, -40, 30, '#e9dccb') + dust(x - 10, y - 4, 9, 14)
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
        cx, yc = x + 100, 236
        body = ''
        extra = ''
        if i == 1:
            extra = ('<ellipse cx="%d" cy="%d" rx="20" ry="44" fill="#ec8aa5" opacity=".75" clip-path="url(#CLIP)"/>'
                     '<ellipse cx="%d" cy="%d" rx="10" ry="30" fill="#e0708c" opacity=".55" clip-path="url(#CLIP)"/>'
                     % (cx, yc - 70, cx, yc - 70))
        if i == 3:
            ring = ''
            for k in range(5):
                ring += ('<ellipse cx="%d" cy="%d" rx="%d" ry="%d" fill="none" stroke="#c9a54a" stroke-width="1.6" opacity=".75" clip-path="url(#CLIP)"/>'
                         % (cx + 2, yc - 78, 6 + k * 5, 8 + k * 6))
            extra = ('<ellipse cx="%d" cy="%d" rx="30" ry="38" fill="#f1d27a" opacity=".35" clip-path="url(#CLIP)"/>' % (cx + 2, yc - 78)) + ring
        f, p = top_finger(cx, yc, hw=38, nail_len=122, free_len=12, finger_len=0, extra=extra)
        body += f
        if i == 0:
            body += '<path d="%s" fill="none" stroke="#fffaf6" stroke-width="10" opacity=".95" clip-path="url(#%s)"/>' % (epo_curve(p, -9), p['clip'])
            body += '<path d="%s" fill="none" stroke="#cdb7ad" stroke-width="1.2" stroke-dasharray="3 3" clip-path="url(#%s)"/>' % (epo_curve(p, -14), p['clip'])
            body += callout(cx + 22, yc - 19, x + 178, yc - 100, 'velo', 'middle', 13, ACC2, sub='di pelle')
        elif i == 1:
            body += callout(cx + 10, yc - 84, x + 170, yc - 160, 'zona sottile', 'middle', 13, ACC2)
        elif i == 2:
            for sx in (-1, 1):
                for k in range(6):
                    body += dust(cx + sx * 40, yc - 40 - k * 16, 3, 4, '#8f817a', k + (3 if sx > 0 else 0))
            body += callout(cx + 42, yc - 92, x + 176, yc - 150, 'polvere', 'middle', 13, ACC2)
        else:
            # polpastrello dell'operatrice che si allontana dopo aver toccato la lamina
            fing = ('<g transform="translate(%d,%d) rotate(-38)">'
                    '<rect x="-20" y="-96" width="40" height="100" rx="20" fill="%s" stroke="%s" stroke-width="1.5"/>'
                    '<path d="M-10,-12 q10,8 20,0 M-12,-20 q12,9 24,0 M-12,-28 q12,9 24,0" fill="none" stroke="%s" stroke-width="1" opacity=".6"/>'
                    '</g>' % (cx + 90, yc - 102, SKIN, SKIN_D, SKIN_D))
            body += fing
            body += arrow(cx + 46, yc - 96, cx + 66, yc - 120, MUTED, 1.8)
            body += callout(cx + 22, yc - 70, x + 186, yc - 52, 'sebo', 'middle', 13, WARN)
            body += text(x + 186, yc - 36, 'impronta', 12, 'middle', 600, MUTED)
        b += frame(x, 20, 216, 285, t, ok=False, sub=sub, body=body, subcol=ERR)
    return svg(W, H, arrow_defs() + b, 'Quattro errori di preparazione che causano sollevamenti: pellicina residua, lamina assottigliata, '
               'polvere nei solchi, dita sulla lamina')


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


def cap_brush(x, y, ang=0, s=1.0, bristle='#f4e3a4'):
    """Pennellino del flacone (tappo-pennello): punta delle setole in (x, y), tappo verso +x."""
    b = ('<rect x="40" y="-9" width="44" height="18" rx="3" fill="url(#bHandle)"/>'
         '<path d="M50,-8 v16 M60,-8 v16 M70,-8 v16" stroke="#fff" stroke-opacity=".16" stroke-width="1.2"/>'
         '<rect x="12" y="-1.8" width="30" height="3.6" fill="#e9edf1" stroke="#9aa3ad" stroke-width=".6"/>'
         '<path d="M14,-3.6 C6,-4 -2,-3 -6,-1 Q-8,0 -6,1 C-2,3 6,4 14,3.6 Z" fill="%s" stroke="%s" stroke-opacity=".4" stroke-width=".7"/>'
         '<path d="M12,-1.4 L-3,-0.4 M12,1.4 L-3,0.4" stroke="#fff" stroke-width=".6" opacity=".6"/>' % (bristle, INK))
    return _g(x, y, ang, s, b)


def nail_inset(p, d=7, top=None):
    """Sagoma della lamina ristretta di d px (margine dalla pelle) per mostrare dove va il prodotto."""
    cx, yc, hw = p['cx'], p['y_c'], p['hw']
    yt = top if top is not None else p['y_t'] + d + 4
    r = hw - d
    return ('M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z'
            % (cx - r, yt + r * 0.5, cx - r, yc - 34 - d * 0.4, cx, yc + 10 - d * 1.6, cx + r, yc - 34 - d * 0.4,
               cx + r, yt + r * 0.5, cx + r, yt, cx, yt, cx - r, yt, cx - r, yt + r * 0.5))


@figx('primer-quantita.svg')
def primer_amount():
    W, H = 940, 330
    b = ''
    # 1 scarica il pennello sul collo del flacone
    x = 20
    bx, byb = x + 104, 258
    body = bottle(bx, byb, '#f4e3a4', 'primer', 76, 100, cap=False)
    nk = byb - 100 - 12
    body += ('<rect x="%d" y="%d" width="34" height="12" rx="2" fill="url(#bGlass)" stroke="#8d8a96" stroke-width="1.4"/>'
             % (bx - 17, nk))
    body += cap_brush(bx + 15, nk - 3, -40, 1.3)
    body += drop_c(bx + 8, nk + 30, '#e7c95a', s=0.6) + drop_c(bx + 2, nk + 50, '#e7c95a', s=0.5)
    body += ('<path d="M%d,%d q-6,26 -26,34" fill="none" stroke="%s" stroke-width="2.2" marker-end="url(#ar)"/>'
             % (bx + 52, nk - 12, ACC2))
    body += text(x + 190, nk + 32, 'strofina', 13, 'start', 700, ACC2)
    body += text(x + 190, nk + 48, 'sul bordo', 13, 'start', 700, ACC2)
    b += frame(x, 20, 290, 290, 'Scarica il pennello', 1, sub='quasi asciutto', body=body, subcol=INK)
    # 2 giusto: velo sottile solo sulla lamina, margine dalla pelle
    x = 324
    cx, yc = x + 122, 240
    f, p = top_finger(cx, yc, hw=44, nail_len=136, free_len=14, finger_len=0)
    body = f
    shape = nail_inset(p, 8)
    body += '<path d="%s" fill="#f6dc7a" fill-opacity=".55" stroke="#c9a54a" stroke-width="1.4" stroke-dasharray="5 3"/>' % shape
    body += cap_brush(cx + 8, yc - 100, -50, 1.25)
    body += dim(cx, yc - 32, cx, yc - 3, '', 'right')
    body += callout(cx + 2, yc - 18, x + 214, yc - 66, '≥ 1 mm', 'start', 14, ACC2, 800)
    body += text(x + 214, yc - 48, 'dalla pelle', 12.5, 'start', 600, ACC2)
    b += frame(x, 20, 290, 290, 'Solo sulla lamina', 2, ok=True, sub='piccoli tocchi, lontano dalla pelle', body=body)
    # 3 troppo: il primer allaga cuticola e solchi
    x = 628
    cx, yc = x + 130, 240
    f, p = top_finger(cx, yc, hw=44, nail_len=136, free_len=14, finger_len=0)
    hw = 44
    flood = ('M%d,%d C%d,%d %d,%d %d,%d C%d,%d %d,%d %d,%d C%d,%d %d,%d %d,%d C%d,%d %d,%d %d,%d '
             'C%d,%d %d,%d %d,%d L%d,%d Q%d,%d %d,%d Z'
             % (cx - hw - 10, yc - 140,
                cx - hw - 14, yc - 110, cx - hw - 8, yc - 70, cx - hw - 16, yc - 30,
                cx - hw - 6, yc + 6, cx - 20, yc + 20, cx, yc + 14,
                cx + 18, yc + 24, cx + hw + 4, yc + 4, cx + hw + 14, yc - 26,
                cx + hw + 8, yc - 70, cx + hw + 16, yc - 108, cx + hw + 10, yc - 140,
                cx + hw + 6, yc - 146, cx + hw - 6, yc - 152, cx + hw - 12, yc - 152,
                cx - hw + 12, yc - 152, cx - hw - 4, yc - 152, cx - hw - 10, yc - 140))
    body = f
    body += '<path d="%s" fill="#f2b45a" fill-opacity=".55" stroke="#d98b2b" stroke-width="1.4"/>' % flood
    body += ('<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".55"/>'
             % (cx - 26, yc - 140, cx - 32, yc - 90, cx - 26, yc - 50))
    body += drop_c(cx - hw - 14, yc + 4, '#f2b45a', '#d98b2b') + drop_c(cx + hw + 14, yc - 6, '#f2b45a', '#d98b2b')
    body += callout(cx + hw + 12, yc - 30, x + 244, yc - 104, 'sulla', 'middle', 13, ERR)
    body += text(x + 244, yc - 88, 'pelle', 13, 'middle', 700, ERR)
    b += frame(x, 20, 290, 290, 'Troppo primer', ok=False, sub='meno adesione, pelle a rischio', body=body)
    return svg(W, H, arrow_defs() + b, 'La quantità giusta di primer: pennello scaricato sul bordo del flacone, velo solo sulla lamina '
               'lontano dalla pelle; errore: primer che allaga cuticola e solchi')


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
    s = '<path d="%s" fill="url(#bTipG)" fill-opacity="%.2f" stroke="%s" stroke-width="1.6"/>' % (body, op, outline)
    s += ('<path d="M%.1f,%.1f L%.1f,%.1f" stroke="#fff" stroke-width="%.1f" stroke-linecap="round" opacity="%.2f"/>'
          % (cx - hw * 0.5, yt + 10, cx - hw * 0.5, ys + well * 0.6, hw * 0.16, 0.75 * op))
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
            x + L * 0.6, y + 2, x, y + 6, x, y, x - well, y - 1, 'url(#bTipV)', TIP_S))
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
    cx, ys = 112, 236
    b += text(cx, 64, 'dall\'alto', 13, weight=700, fill=MUTED)
    b += tip_top(cx, ys, 48, 156, 70)
    b += leader(cx + 8, ys - 90, 212, 128, 'Corpo del tip', 'start', 14)
    b += leader(cx + 34, ys, 212, 218, 'Punto d\'arresto', 'start', 14)
    b += leader(cx - 6, ys + 36, 212, 262, 'Incavo (well)', 'start', 14)
    # vista di profilo (ingrandita)
    b += '<rect x="370" y="56" width="370" height="270" rx="16" fill="%s"/>' % PANEL
    b += text(555, 84, 'di profilo (ingrandito)', 13, weight=700, fill=MUTED)
    sc, ox, oy = 2.2, 516, 160
    prof = ('<path d="M-54,0 L-54,-1.6 Q-30,-3.2 0,-4.2 Q50,-5.4 96,-1.4 L96,3.6 Q50,6.8 2,6 L0,6 L0,0.4 Z" '
            'fill="url(#bTipV)" stroke="%s" stroke-width="0.7" stroke-linejoin="round"/>'
            '<path d="M-40,-1.6 Q0,-3 50,-3.6 Q76,-3 92,-0.8" fill="none" stroke="#fff" stroke-width=".7" opacity=".9"/>'
            '<rect x="-54" y="0.2" width="54" height="2.6" fill="url(#%s)"/>'
            '<rect x="-54" y="0.2" width="54" height="2.6" fill="none" stroke="%s" stroke-width=".5" stroke-dasharray="1.5 1.5"/>'
            % (TIP_S, HATCH_ID, MUTED))
    b += scaled(ox, oy, sc, prof)
    b += callout(ox - 70, oy - 5, 440, 120, 'incavo sottile', 'middle', 13)
    b += callout(ox - 40, oy + 4, 450, 216, 'zona di contatto', 'middle', 13, sub='(si incolla sull\'unghia)')
    b += '<circle cx="%.1f" cy="%.1f" r="9" fill="none" stroke="%s" stroke-width="2"/>' % (ox, oy + 6, ACC2)
    b += callout(ox + 6, oy + 13, 626, 216, 'gradino d\'arresto', 'middle', 13, sub='tocca il bordo libero')
    b += callout(ox + 120, oy - 7, 680, 120, 'corpo', 'middle', 13)
    # curva a C vista dalla punta
    ccx, ccy = 470, 300
    b += ('<path d="M%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="url(#bTipV)" stroke="%s" stroke-width="1.4" stroke-linejoin="round"/>'
          % (ccx - 48, ccy, ccx, ccy - 50, ccx + 48, ccy, ccx + 43, ccy + 2, ccx, ccy - 42, ccx - 43, ccy + 2, TIP_S))
    b += text(530, 292, 'Curva a C', 13.5, 'start', 800)
    b += text(530, 309, '(vista dalla punta)', 12, 'start', fill=MUTED)
    b += text(W / 2, 356, 'L\'incavo copre al massimo metà unghia.', 15, weight=800, fill=ACC2)
    return svg(W, H, arrow_defs() + b, 'Le parti del tip: corpo, punto d\'arresto, incavo e zona di contatto; profilo ingrandito e curva a C')


@figx('tip-misura-errori.svg')
def tip_size():
    W, H = 940, 330
    b = hatch_defs()
    data = [('Troppo stretto', False, 'lati scoperti: crepe'), ('Giusto', True, 'da solco a solco'),
            ('Troppo largo', False, 'preme sulla pelle: dolore')]
    for i, (t, ok, sub) in enumerate(data):
        x = 20 + i * 304
        cx, cy = x + 145, 200
        hw, cv = 60, 24
        body = finger_front(cx, cy, hw, cv)
        apex = cy - 4 - cv
        if i == 0:
            tw = hw - 20
            yn = cy - 4 - cv * (1 - (tw / hw) ** 2)
            cyt = yn - 5
            k = cyt + 11 - cy + cv
            body += c_arc(cx, cyt, tw, k, col='url(#bTipV)', stroke=TIP_S)
            for sx in (-1, 1):
                body += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="9" stroke-linecap="round" opacity=".55"/>'
                         % (cx + sx * (hw - 2), cy - 6, cx + sx * (hw - 10), cy - 18, cx + sx * (tw + 2), yn - 1, ERR))
            body += callout(cx + hw - 8, cy - 14, cx + 70, 112, 'unghia scoperta', 'middle', 12.5, ERR)
        elif i == 1:
            body += c_arc(cx, cy - 11, hw + 4, cv, col='url(#bTipV)', stroke=TIP_S)
            body += dim(cx - hw - 2, 118, cx + hw + 2, 118, '', 'above', OK)
            body += dashed(cx - hw - 2, 122, cx - hw - 2, cy - 4, OK, 1.2, '3 3') + dashed(cx + hw + 2, 122, cx + hw + 2, cy - 4, OK, 1.2, '3 3')
            body += text(cx, 106, 'solco – solco', 13, 'middle', 700, OK)
            body += callout(cx - 30, apex - 9, x + 40, 150, 'tip', 'middle', 12.5)
            body += callout(cx + 34, apex + 6, x + 252, 150, 'unghia', 'middle', 12.5)
        else:
            body += c_arc(cx, cy - 2, hw + 24, cv + 8, col='url(#bTipV)', stroke=TIP_S)
            for sx in (-1, 1):
                body += '<circle cx="%.1f" cy="%.1f" r="14" fill="%s" opacity=".35"/>' % (cx + sx * (hw + 18), cy - 4, ERR)
                body += '<circle cx="%.1f" cy="%.1f" r="14" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="4 3"/>' % (cx + sx * (hw + 18), cy - 4, ERR)
            body += callout(cx + hw + 18, cy - 18, cx + 96, 110, 'sulla pelle', 'middle', 12.5, ERR)
        body += text(cx, 272, 'vista dalla punta', 12.5, fill=MUTED, style='italic')
        b += frame(x, 20, 290, 290, t, ok=ok, sub=sub, body=body)
    return svg(W, H, arrow_defs() + b, 'Misura del tip vista dalla punta: troppo stretto lascia scoperti i lati, giusto da solco a solco, troppo largo preme sulla pelle')


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
    cx, yc = x + 130, 254
    body = ''
    f, p = top_finger(cx, yc, hw=46, nail_len=134, free_len=10, finger_len=0)
    body += f
    ys = p['y_s'] - 10
    body += tip_top(cx, ys, 50, 40, 124, op=0.55, hatch=False)
    half = (p['y_s'] + yc) // 2 + 6
    body += ('<path d="M%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="%s" opacity=".3"/>'
             % (cx - 50, half - 6, cx, half + 18, cx + 50, half - 6, cx + 50, ys + 124, cx, ys + 150, cx - 50, ys + 124, ERR))
    body += '<path d="M%d,%d Q%d,%d %d,%d" stroke="%s" stroke-width="2.4" stroke-dasharray="7 5" fill="none"/>' % (cx - 50, ys + 124, cx, ys + 150, cx + 50, ys + 124, ERR)
    body += '<path d="M%d,%d Q%d,%d %d,%d" stroke="%s" stroke-width="3" fill="none"/>' % (cx - 50, half - 6, cx, half + 18, cx + 50, half - 6, OK)
    body += tool_scissors(cx + 56, half + 4, 0, 0.8)
    body += text(cx + 112, half - 40, 'max', 13, 'start', 800, OK)
    body += text(cx + 112, half - 22, 'metà unghia', 13, 'start', 800, OK)
    body += text(cx + 112, ys + 130, 'troppo', 13, 'start', 800, ERR)
    body += text(cx + 112, ys + 148, 'lungo', 13, 'start', 800, ERR)
    b += frame(x, 20, 350, 290, 'Accorcia l\'incavo', 2, sub='segue la curva della cuticola', body=body, subcol=INK)
    return svg(W, H, arrow_defs() + b, 'Adattare il tip: limare i lati e accorciare l\'incavo a metà unghia')


def press_finger(x, y, s=1.0):
    """Dito dell'operatrice di profilo che preme dall'alto: polpastrello in (x, y), unghia sul lato destro."""
    b = ('<path d="M-17,-92 L-17,-22 Q-17,0 2,0 Q19,0 19,-20 L19,-92 Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
         '<path d="M17,-50 Q23,-49 23,-38 L22,-14 Q21,-6 16,-4 L16,-50 Z" fill="%s" stroke="%s" stroke-width="1.2"/>'
         % (SKIN, SKIN_D, NAIL, NAIL_S))
    return '<g transform="translate(%.1f,%.1f) scale(%.2f)">%s</g>' % (x, y, s, b)


def glue_tip(ang, glue=False, bubble=False):
    """Scena locale: dito di profilo con bordo libero che termina in (0,0) e tip con l'arresto in (0,0)."""
    s = finger_side(-100, 0, L=86, free=14)
    t = ('<path d="M-54,0 L-54,-1.6 Q-30,-3.2 0,-4.2 Q60,-5.4 116,-1 L116,4 Q60,6.8 2,6 L0,6 L0,0.4 Z" '
         'fill="url(#bTipV)" stroke="%s" stroke-width="1.3" stroke-linejoin="round"/>'
         '<path d="M-40,-1.6 Q0,-3 60,-3.6 Q90,-3 110,-0.4" fill="none" stroke="#fff" stroke-width="1.2" opacity=".9"/>' % TIP_S)
    if glue:
        for gx in (-44, -32, -20, -9):
            t += '<ellipse cx="%d" cy="1.2" rx="4.2" ry="2.4" fill="#8fc6ea" stroke="#3d8fc6" stroke-width=".8"/>' % gx
    if bubble:
        t += '<ellipse cx="-26" cy="-0.6" rx="10" ry="2.4" fill="#fff" stroke="#3d8fc6" stroke-width="1.2"/>'
    s += rot(ang, 0, 0, t) if ang else t
    return s


@figx('tip-incollaggio-45.svg')
def tip_glue():
    W, H = 940, 310
    b = ''
    T = ['Appoggia a 45°', 'Abbassa lentamente', 'Tieni fermo']
    sc = 1.45
    for i, t in enumerate(T):
        x = 20 + i * 228
        ox, oy = x + 112, 168

        def P(px, py):
            return ox + px * sc, oy + py * sc
        ang = [45, 22, 0][i]
        body = scaled(ox, oy, sc, glue_tip(ang, glue=(i == 0)))
        if i == 0:
            body += dashed(ox, oy, x + 214, oy, MUTED, 1.2, '4 4')
            body += arc_angle(ox, oy, 54, 0, 45, '', ACC2)
            body += text(x + 196, oy + 34, '45°', 15, 'middle', 800, ACC2)
            gx, gy = P(-30 * 0.707, -30 * 0.707)
            body += leader(gx + 2, gy + 2, x + 150, 98, 'colla nell\'incavo', 'middle', 13)
            body += leader(ox, oy, x + 62, 232, 'arresto sul bordo', 'middle', 12.5)
        elif i == 1:
            ex, ey = P(-54 * math.cos(math.radians(22)), -54 * math.sin(math.radians(22)))
            body += ('<path d="M%.1f,%.1f A%.1f,%.1f 0 0 0 %.1f,%.1f" fill="none" stroke="%s" stroke-width="2.4" marker-end="url(#ar)"/>'
                     % (ex - 6, ey - 16, 54 * sc + 10, 54 * sc + 10, ox - 54 * sc - 4, oy - 12, ACC2))
            for k in range(3):
                body += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#fff" stroke="#3d8fc6" stroke-width="1.4"/>' % (
                    ox - 30 - k * 16, oy - 6 - k * 14, 4.2 - k * 0.8)
            body += text(x + 60, 90, 'l\'aria esce', 13, 'middle', 700, ACC2)
            body += text(x + 60, 106, 'dal retro', 13, 'middle', 700, ACC2)
        else:
            body += press_finger(ox - 34, oy - 7, 1.0)
            body += arrow(ox - 64, oy - 70, ox - 64, oy - 30, ACC2, 2) + arrow(ox - 4, oy - 70, ox - 4, oy - 30, ACC2, 2)
            body += timer(x + 152, 86, '')
            body += text(x + 152, 122, '5–10 s', 14, 'middle', 800, ACC2)
        b += frame(x, 20, 216, 270, t, i + 1, body=body)
    # riquadro errore
    x = 704
    ox, oy = x + 112, 168
    body = scaled(ox, oy, sc, glue_tip(0, bubble=True))
    body += arrow(ox - 40, oy - 82, ox - 40, oy - 20, ERR, 2.4)
    body += arrow(ox + 50, oy - 82, ox + 50, oy - 20, ERR, 2.4)
    body += text(ox + 5, oy - 92, 'giù di colpo', 13, 'middle', 700, ERR)
    body += leader(ox - 38, oy - 1, x + 70, 228, 'bolla d\'aria', 'middle', 13, fill=ERR)
    b += frame(x, 20, 216, 270, 'Appoggiato piatto', ok=False, sub='bolle = sollevamento', body=body)
    return svg(W, H, arrow_defs() + b, 'Incollare il tip: arresto contro il bordo libero a 45 gradi, discesa lenta che fa uscire l\'aria, '
               'pressione per 5–10 secondi; errore: tip appoggiato piatto di colpo che intrappola una bolla')


@figx('tip-errori-applicazione.svg')
def tip_errors():
    W, H = 940, 320
    b = hatch_defs()
    T = [('Bolla', 'togli e riapplica'), ('Fuori asse', 'l\'unghia cresce storta'), ('Inclinato', 'punta che scende')]
    for i, (t, sub) in enumerate(T):
        x = 20 + i * 304
        cx, yc = x + 145, 246
        body = ''
        if i < 2:
            f, p = top_finger(cx, yc, hw=40, nail_len=96, free_len=6, finger_len=0)
            body += f
            ys = p['y_s'] - 4
            body += tip_top(cx, ys, 43, 62, 55, op=0.6, ang=(10 if i == 1 else 0), hatch=False)
            if i == 0:
                body += '<circle cx="%.1f" cy="%.1f" r="12" fill="#fff" opacity=".95" stroke="#cfd8de"/>' % (cx + 8, ys + 30)
                body += leader(cx + 12, ys + 30, cx + 90, ys - 30, 'bolla', 'start', 13.5, fill=ERR)
            else:
                body += dashed(cx, yc + 10, cx, 64, OK, 1.8)
                body += dashed(cx, ys + 60, cx + (ys + 60 - 64) * math.tan(math.radians(10)), 64, ERR, 1.8)
                body += text(cx - 8, 76, 'asse del dito', 12.5, 'end', 700, OK)
                body += text(cx + 36, 76, 'asse del tip', 12.5, 'start', 700, ERR)
        else:
            ox, oy = x + 120, 160
            body += scaled(ox, oy, 1.25, glue_tip(9))
            body += dashed(ox - 20, oy + 1, x + 286, oy + 1, OK, 1.8, '7 5')
            body += text(x + 240, oy - 12, 'linea giusta', 12.5, 'middle', 700, OK)
            ex = ox + 112 * 1.25 * math.cos(math.radians(9))
            body += arrow(ex, oy + 4, ex, oy + 30, ERR, 2.2)
        b += frame(x, 20, 290, 285, t, ok=False, sub=sub, body=body)
    return svg(W, H, arrow_defs() + b, 'Tre errori di applicazione del tip: bolla, fuori asse, inclinato')


@figx('tip-taglio.svg')
def tip_cut():
    W, H = 760, 330
    b = hatch_defs()
    # 1 taglio perpendicolare
    x = 20
    cx, yc = x + 150, 336
    body = ''
    f, p = top_finger(cx, yc, hw=38, nail_len=96, free_len=6, finger_len=20)
    body += f
    ys = p['y_s'] - 4
    body += tip_top(cx, ys, 41, 136, 45, op=0.7, hatch=False)
    cut = ys - 62
    fin = cut + 17
    yt = ys - 136
    body += dashed(cx - 50, cut, cx + 62, cut, ERR, 2, '7 5')
    body += dashed(cx - 50, fin, cx + 62, fin, OK, 1.8, '4 4')
    body += tool_tipcutter(cx, cut, -90, 1.0)
    body += text(cx - 56, cut + 4, 'taglio', 13, 'end', 800, ERR)
    body += text(cx - 56, fin + 6, 'forma finale', 12.5, 'end', 700, OK)
    body += dim(cx + 70, cut, cx + 70, fin, '', 'left')
    body += text(cx + 80, cut - 2, '+1–2 mm', 13, 'start', 800, ACC2)
    body += text(cx + 80, fin + 8, 'per limare', 12.5, 'start', 700, ACC2)
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
    T, U = 28, 20
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="70" fill="url(#bSkinV)"/>' % (x, y + T, w)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="8" fill="%s" opacity=".6"/>' % (x, y + T, w, BED)
    e = x + w * 0.42  # fine dell'incavo
    if state == 'ko':
        s += ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
              % (x, y, e - 6, y, e + 30, y + 17, e + 66, y, x + w, y, x + w, y + T, x, y + T, NAIL, NAIL_S))
    else:
        s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%d" fill="%s" stroke="%s" stroke-width="1.5"/>' % (x, y, w, T, NAIL, NAIL_S)
    for k in range(3):
        s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width=".8" opacity=".35"/>' % (
            x + 4, y + 8 + k * 7, x + w - 4, y + 8 + k * 7, NAIL_S)
    if state == 'prima':
        d = 'M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (x + w, y - U, e, y - U, e, y, x + w, y)
    elif state == 'lima':
        d = 'M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (x + w, y - U, e + 50, y - U, e, y, x + w, y)
    elif state == 'dopo':
        d = 'M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z' % (x + w, y - U, e + 80, y - U, e + 34, y - U + 2, e - 8, y, x + w, y)
    else:
        d = 'M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (x + w, y - U, e + 68, y - U, e + 66, y, x + w, y)
    s += '<path d="%s" fill="url(#bTipV)" stroke="%s" stroke-width="1.5" stroke-linejoin="round"/>' % (d, TIP_S)
    s += text(x + 8, y + 19, 'lamina', 12.5, 'start', 700, ACC2)
    s += text(x + w - 8, y - U - 8, 'tip', 12.5, 'end', 700, MUTED)
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
        sx, sy = x, 178
        sec, e = blend_section(sx, sy, 216, ['prima', 'lima', 'dopo', 'ko'][i])
        body += sec
        if i == 0:
            body += '<circle cx="%.1f" cy="%.1f" r="16" fill="none" stroke="%s" stroke-width="2"/>' % (e, sy - 10, ACC2)
            body += callout(e - 12, sy - 22, e - 30, 106, 'gradino', 'middle', 13, ACC2)
        elif i == 1:
            body += tool_file(e + 52, sy - 30, -21.8, 130, 16)
            body += arrow(e + 8, sy - 58, e + 100, sy - 95, ACC2, 1.8, True)
        elif i == 2:
            body += text(e + 20, sy - 56, 'superficie continua', 12.5, 'middle', 700, OK)
        else:
            body += arrow(e + 30, sy - 60, e + 30, sy + 8, ERR, 2)
            body += text(e + 30, sy - 68, 'avvallamento', 12.5, 'middle', 700, ERR)
        b += frame(x, 20, 216, 290, t, (i + 1) if i < 3 else None, ok=ok if i == 3 else None, sub=sub, body=body,
                   subcol=ERR if i == 3 else INK)
        if i == 2:
            b += mark(x + 192, 45, True, 13)
    return svg(W, H, arrow_defs() + b, 'Fusione del tip in sezione ingrandita: dal gradino alla superficie liscia limando solo il tip, senza assottigliare la lamina')


def overlay_profile(ox, oy, L=170, free=26, ext=130, apex_h=28, prod=True, apex_at=None, tip=True):
    """Profilo: dito + lamina + (tip) + prodotto. Restituisce svg e punti."""
    s = finger_side(ox, oy, L=L, free=free)
    xe = ox + L
    xn = xe + free           # fine unghia naturale
    xb = xn + ext            # punta
    if tip:
        s += ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.4"/>'
              % (xn - 40, oy - 1, xn, oy - 2, xn + ext * 0.6, oy - 1, xb, oy + 3, xb, oy + 7, xn, oy + 6, 'url(#bTipV)', TIP_S))
    pts = {}
    if prod:
        xa = ox + 14
        ax = apex_at if apex_at is not None else xe - 6
        top = 'M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (
            xa, oy - 1, (xa + ax) / 2, oy - apex_h, ax, oy - apex_h, (ax + xb) / 2 + 20, oy - apex_h, xb, oy - 4)
        if tip:
            s += '<path d="%s L%.1f,%.1f L%.1f,%.1f Z" fill="url(#bProdV)" stroke="%s" stroke-width="1.6" opacity=".95"/>' % (
                top, xb, oy - 1, xa, oy - 1, PROD_S)
        else:
            s += '<path d="%s L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="url(#bProdV)" stroke="%s" stroke-width="1.6" opacity=".95"/>' % (
                top, xb, oy + 5, xn, oy + 6, xn, oy - 1, xa, oy - 1, PROD_S)
        s += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" opacity=".85"/>'
              % ((xa + ax) / 2, oy - apex_h * 0.72, ax, oy - apex_h - 1 + 4, (ax + xb) / 2 + 10, oy - apex_h * 0.78))
        pts = dict(xa=xa, ax=ax, ah=oy - apex_h)
    pts.update(xe=xe, xn=xn, xb=xb, oy=oy, ox=ox)
    return s, pts


def zone_badge(x, y, n, label, col=ACC2, sub=None):
    """Numero di zona in un cerchio con etichetta sotto."""
    s = '<circle cx="%.1f" cy="%.1f" r="13" fill="%s" stroke="#fff" stroke-width="2" filter="url(#nxShS)"/>' % (x, y, col)
    s += text(x, y + 5, str(n), 14, weight=800, fill='#fff')
    if label:
        s += text(x, y + 32, label, 13, 'middle', 800, col)
    if sub:
        s += text(x, y + 48, sub, 12, 'middle', 600, MUTED)
    return s


@figx('tip-overlay-sezione.svg')
def tip_overlay():
    W, H = 760, 320
    b = text(20, 38, 'Copertura in gel sul tip (sezione)', 20, 'start', 800, ACC2)
    s, p = overlay_profile(150, 214, L=200, free=24, ext=200, apex_h=34)
    b += s
    xn, xe, oy = p['xn'], p['xe'], p['oy']
    xa, ax, xb = p['xa'], p['ax'], p['xb']
    # zone numerate, tutte sulla stessa riga
    for n, zx, lab, sub in ((3, xa + 50, 'sottile', 'vicino alla cuticola'), (2, ax, 'apex', 'la parte più spessa'),
                           (1, xb - 60, '≈ 0,8–1 mm', 'sottile in punta')):
        b += zone_badge(zx, 76, n, lab, ACC2, sub)
        top_y = oy - (34 if n == 2 else 18 if n == 3 else 10)
        b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.2" stroke-dasharray="3 3"/>' % (zx, 130, zx, top_y, MUTED)
    b += dashed(xn, oy - 30, xn, oy + 46, MUTED, 1.4, '5 4')
    b += text(xn + 8, oy + 62, 'fine unghia naturale', 12.5, 'start', 600, MUTED)
    b += '<circle cx="%.1f" cy="%.1f" r="5" fill="%s"/>' % (xe, oy + 6, ERR)
    b += callout(xe, oy + 6, xe - 70, oy + 80, 'punto di stress', 'middle', 13, ERR)
    b += dim(p['ox'] + 2, oy - 24, xa + 2, oy - 24, '', 'above')
    b += text(p['ox'] - 6, oy - 38, '≈ 1 mm dalla pelle', 12.5, 'middle', 700, ACC2)
    b += callout(xb - 30, oy + 4, xb - 12, oy + 50, 'tip', 'middle', 13)
    return svg(W, H, arrow_defs() + b, 'Sezione della copertura in gel sul tip: zona 3 sottile alla cuticola, zona 2 apex sopra il punto di stress, '
               'zona 1 sottile in punta')


@figx('tip-gel-step.svg')
def tip_gel_steps():
    labels = ['Primer solo sull\'unghia', 'Base + lampada', 'Perla in zona 2', 'Capovolgi', 'Controlla il profilo', 'Lima, top, olio']

    def nail_tip():
        f, p = top_finger(0, 0, hw=34, nail_len=100, free_len=6, finger_len=8)
        ys = p['y_s'] - 4
        return f + tip_top(0, ys, 36, 70, 40, op=0.6, hatch=False), ys

    def d(i, x, y):
        s = ''
        cx, yb = x + 130, y + 176
        sc = 0.66
        if i in (0, 2, 5):
            g, ys = nail_tip()
            if i == 2:
                g += bead(0, ys + 16, 20, PROD, PROD_S)
                g += arrow(0, ys + 40, 0, ys + 74, ACC2, 2.4)
                g += arrow(0, ys - 8, 0, ys - 50, ACC2, 2.4)
            elif i == 5:
                g += tool_file(64, ys - 20, -70, 110, 16)
            s += scaled(cx, yb, sc, g)
            if i == 0:
                s += cap_brush(cx + 6, yb - 50, -22, 1.05)
                s += mark(cx, yb - 104, False, 11)
                s += text(cx + 18, yb - 99, 'no sul tip', 13, 'start', 800, ERR)
                s += mark(cx - 52, yb - 40, True, 11)
            if i == 2:
                s += callout(cx + 12, yb + (ys + 16) * sc, x + 226, y + 130, 'sul punto', 'middle', 12.5, sub='di stress')
            if i == 5:
                s += bottle(x + 46, yb, '#f0eaf6', 'top', 34, 50)
                s += drop_c(x + 236, yb - 44, YEL, '#c9a54a', 1.2)
                s += text(x + 236, yb - 6, 'olio', 12.5, 'middle', 700, MUTED)
        elif i == 1:
            sp, p = overlay_profile(0, 0, L=90, free=14, ext=70, apex_h=5, tip=True)
            s += lamp(x + 186, y + 170, 150, '')
            s += scaled(x + 100, y + 150, 0.62, sp)
            s += callout(x + 100 + 60 * 0.62, y + 150 - 3, x + 70, y + 76, 'base sottile', 'middle', 12.5)
        elif i == 3:
            sp, p = overlay_profile(0, 0, L=90, free=14, ext=70, apex_h=22, tip=True)
            s += scaled(x + 70, y + 104, 0.62, '<g transform="rotate(180 60 0)">%s</g>' % sp)
            s += flip_icon(x + 40, y + 74, 15)
            ax = x + 70 + (120 - p['ax']) * 0.62
            s += arrow(ax, y + 116, ax, y + 150, ACC2, 2.4)
            s += text(ax + 14, y + 144, '5–30 s', 14, 'start', 800, ACC2)
            s += text(x + 145, y + 176, 'unghia verso il basso', 12.5, 'middle', 600, MUTED)
        else:
            sp, p = overlay_profile(0, 0, L=90, free=14, ext=70, apex_h=22, tip=True)
            sp += '<circle cx="%.1f" cy="%.1f" r="5" fill="%s"/>' % (p['xe'], p['oy'] + 6, ERR)
            s += scaled(x + 92, y + 130, 0.68, sp)
            s += eye(x + 262, y + 108, 180, 1.1)
            s += text(x + 130, y + 72, 'sottile – spesso – sottile', 12.5, 'middle', 600, MUTED)
        return s
    return steps_fig('Copertura in gel sul tip', labels, 3, 290, 190, d, 'Copertura in gel sul tip in sei passaggi: primer solo sull\'unghia, '
                     'base e lampada, perla in zona 2, mano capovolta, controllo del profilo, lima, top e olio')


# ================================================================= MODULO CARTINA
def form_shape(cx, ys, w=80, h=130, hole=46, hole_d=48, grid=True, center=True, notch=None, cut_tab=False):
    """Cartina adesiva vista dall'alto: ys = altezza del bordo libero; foro verso il basso.
    Carta sfumata con angoli arrotondati, archi-guida stampati, righello laterale e asse centrale."""
    r = 12
    yb = ys + 36
    top = 'M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f' % (
        cx - w, yb, cx - w, ys - h + r, cx - w, ys - h, cx - w + r, ys - h, cx + w - r, ys - h, cx + w, ys - h, cx + w, ys - h + r, cx + w, yb)
    if cut_tab:
        d = top + ' L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (cx + hole, yb, cx + hole, ys, cx - hole, ys, cx - hole, yb)
    else:
        nd = notch if notch else 0
        d = top + ' L%.1f,%.1f A%.1f,%.1f 0 0 0 %.1f,%.1f Z' % (cx + hole, yb, hole, hole_d + nd, cx - hole, yb)
    c = uid('fm')
    s = '<defs><clipPath id="%s"><path d="%s"/></clipPath></defs>' % (c, d)
    s += '<path d="%s" fill="url(#bForm)" stroke="%s" stroke-width="1.4" filter="url(#nxShS)"/>' % (d, FORM_S)
    p = ''
    if grid:
        for k in range(1, 6):
            yy = ys - k * 24 + 4
            if yy > ys - h + 8:
                p += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="1.1"/>'
                      % (cx - w + 18, yy + 5, cx, yy - 7, cx + w - 18, yy + 5, '#c9ae4e'))
        yy = ys + 30
        while yy > ys - h + 6:
            big = int(round((ys + 30 - yy) / 6)) % 4 == 0
            ln = 9 if big else 5
            p += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#b39639" stroke-width="1"/>' % (cx - w, yy, cx - w + ln, yy)
            p += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#b39639" stroke-width="1"/>' % (cx + w, yy, cx + w - ln, yy)
            yy -= 6
    if center:
        p += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-dasharray="4 4" stroke-width="1.4"/>' % (cx, ys - h, cx, ys - 8, ACC2)
    s += '<g clip-path="url(#%s)">%s</g>' % (c, p)
    return s


def form_side(x, y, ang, L=120):
    """Cartina di profilo: parte dal bordo libero (x, y) verso destra, inclinata di ang (gradi, + = verso il basso)."""
    return rot(ang, x, y, '<rect x="%.1f" y="%.1f" width="%.1f" height="5" rx="2" fill="url(#bForm)" stroke="%s"/>'
               '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#fff" stroke-width="1" opacity=".7"/>'
               % (x - 6, y + 5, L, FORM_S, x - 4, y + 6.2, x + L - 8, y + 6.2))


def pill(x, y, s, size=13, fill=ACC2, anchor='middle'):
    """Etichetta su fondo bianco arrotondato (leggibile sopra disegni)."""
    w = len(s) * size * 0.58 + 12
    x0 = x - w / 2 if anchor == 'middle' else (x - 6 if anchor == 'start' else x - w + 6)
    return ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="#fff" opacity=".92"/>' % (x0, y - size - 1, w, size + 8, (size + 8) / 2)
            + text(x, y + 1, s, size, anchor, 700, fill))


def finger_under(cx, ytop, w=76, L=200):
    """Dito visto dal basso (palmo): polpastrello con impronta e piega dell'articolazione."""
    s = ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s" stroke="%s" stroke-width="1.5"/>'
         % (cx - w / 2, ytop, w, L, w / 2, SKIN, SKIN_D))
    pc = ytop + w * 0.62
    for k in range(4):
        r = 8 + k * 6
        s += ('<path d="M%.1f,%.1f A%.1f,%.1f 0 0 1 %.1f,%.1f" fill="none" stroke="%s" stroke-width="1" opacity=".45"/>'
              % (cx - r, pc + 10, r, r * 0.9, cx + r, pc + 10, SKIN_D))
    return s, pc


@figx('cartina-step.svg')
def form_steps():
    W, H = 940, 340
    b = ''
    T = [('Stacca e curva', ''), ('Adatta l\'apertura', ''), ('Infila in asse', 'niente spazi'), ('Chiudi le alette', 'vista dal basso')]
    for i, (t, sub) in enumerate(T):
        x = 20 + i * 228
        cx = x + 108
        body = ''
        if i == 0:
            # foglio di supporto + cartina che si stacca con l'angolo arricciato
            body += '<rect x="%d" y="70" width="120" height="100" rx="8" fill="#eef1f4" stroke="#b8c0c8" stroke-width="1.2"/>' % (cx - 82)
            body += '<rect x="%d" y="76" width="108" height="88" rx="6" fill="none" stroke="#cfd5db" stroke-dasharray="3 3"/>' % (cx - 76)
            body += rot(-14, cx - 10, 120, form_shape(cx + 4, 128, 46, 50, 22, 18, grid=True, center=False))
            body += ('<path d="M%d,%d L%d,%d L%d,%d Z" fill="#fff" stroke="%s" stroke-width="1.2"/>' % (cx + 44, 92, cx + 58, 120, cx + 30, 108, FORM_S))
            body += ('<path d="M%d,%d q20,-24 40,-10" fill="none" stroke="%s" stroke-width="2" marker-end="url(#ar)"/>' % (cx + 50, 84, ACC2))
            body += text(cx + 84, 104, 'stacca', 12.5, 'middle', 700, ACC2)
            # curva a C vista dalla punta
            body += ('<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="%s" stroke-width="9" stroke-linecap="round"/>'
                     % (cx - 50, 246, cx, 186, cx + 50, 246, FORM_S))
            body += ('<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="#f6e7a8" stroke-width="6" stroke-linecap="round"/>'
                     % (cx - 50, 246, cx, 186, cx + 50, 246))
            body += arrow(cx - 76, 214, cx - 58, 236, ACC2, 2) + arrow(cx + 76, 214, cx + 58, 236, ACC2, 2)
            body += text(cx, 278, 'curva come l\'unghia', 12.5, 'middle', 700, ACC2)
        elif i == 1:
            body += form_shape(cx, 190, 80, 112, 40, 30)
            body += ('<path d="M%d,%d A%d,%d 0 0 0 %d,%d" fill="none" stroke="%s" stroke-width="2.2" stroke-dasharray="6 4"/>'
                     % (cx + 52, 226, 52, 50, cx - 52, 226, ERR))
            body += tool_scissors(cx + 44, 202, -62, 0.95)
            body += text(cx, 270, 'segui il bordo libero', 12.5, 'middle', 700, ACC2)
        elif i == 2:
            yc = 252
            f, p = top_finger(cx, yc, hw=30, nail_len=92, free_len=6, finger_len=0)
            ys = p['y_s'] - 6
            body += form_shape(cx, ys, 84, 84, 32, 40, center=False)
            body += f
            body += dashed(cx, 74, cx, yc + 26, ACC2, 1.8, '6 4')
            body += pill(cx + 48, 104, 'asse', 12.5)
        else:
            # vista dal basso: le alette si chiudono sotto il polpastrello, non sull'articolazione
            fu, pc = finger_under(cx, 84, 74, 260)
            body += form_shape(cx, 84 + 16, 70, 34, 30, 22, grid=False, center=False)
            body += fu
            for sx in (-1, 1):
                body += ('<path d="M%d,%d C%d,%d %d,%d %d,%d L%d,%d C%d,%d %d,%d %d,%d Z" fill="url(#bForm)" stroke="%s" stroke-width="1.3"/>'
                         % (cx + sx * 74, 104, cx + sx * 50, 112, cx + sx * 24, 130, cx - sx * 14, 160,
                            cx - sx * 4, 176, cx + sx * 26, 150, cx + sx * 52, 134, cx + sx * 74, 130, FORM_S))
            body += mark(cx + 60, 160, True, 11)
            body += ('<path d="M%d,%d q%d,6 %d,0 M%d,%d q%d,6 %d,0" fill="none" stroke="%s" stroke-width="1.5"/>'
                     % (cx - 30, 236, 30, 60, cx - 30, 244, 30, 60, SKIN_D))
            body += mark(cx + 60, 240, False, 11)
            body += pill(cx, 204, 'sotto il polpastrello', 12, OK)
            body += pill(cx, 272, 'non sulla nocca', 12.5, ERR)
            body += pill(cx, 300, 'vista dal basso', 12.5, INK)
            sub = None
        b += frame(x, 20, 216, 300, t, i + 1, sub=sub, body=body, subcol=INK)
    return svg(W, H, arrow_defs() + b, 'Posizionare la cartina in quattro passaggi: staccala e curvala, adatta l\'apertura, infilala in asse '
               'sotto il bordo libero, chiudi le alette sotto il polpastrello')


@figx('cartina-livello.svg')
def form_level():
    W, H = 940, 310
    b = ''
    T = [('Troppo bassa', False, 12, 'l\'allungamento cade'), ('In livello', True, 0, 'prosegue la lamina'),
         ('Troppo alta', False, -12, 'punta all\'insù (ski-jump)')]
    sc = 1.25
    for i, (t, ok, ang, sub) in enumerate(T):
        x = 20 + i * 304
        ox, oy = x + 128, 150          # fine del letto (punto di stress) in coordinate del pannello
        L = 100
        g = finger_side(-L, 0, L=L, free=8)
        # parte posteriore della cartina che avvolge il polpastrello
        back = 'M-2,7 C22,9 30,40 14,70'
        g += '<path d="%s" fill="none" stroke="%s" stroke-width="6.5" stroke-linecap="round"/>' % (back, FORM_S)
        g += '<path d="%s" fill="none" stroke="#f6e7a8" stroke-width="4.5" stroke-linecap="round"/>' % back
        # linguetta della cartina + allungamento che ci verrà costruito sopra
        front = ('<path d="M-4,6 L124,6 L124,10.5 L-4,10.5 Z" fill="url(#bForm)" stroke="%s" stroke-width=".9"/>'
                 '<path d="M8,6 L116,6 L116,-2 Q60,-6 8,-2 Z" fill="%s" fill-opacity=".45" stroke="%s" stroke-width="1" stroke-dasharray="3 2"/>'
                 % (FORM_S, PROD, PROD_S))
        g += rot(ang, 8, 6, front) if ang else front
        body = scaled(ox, oy, sc, g)
        body += dashed(ox - 100 * sc, oy + 1, x + 290, oy + 1, OK, 1.8, '7 5')
        if ang:
            ex = ox + 112 * sc
            body += arrow(ex, oy + 1, ex, oy + 1 + (32 if ang > 0 else -32), ERR, 2.2)
        if i == 1:
            body += callout(ox + 60 * sc, oy - 2 * sc, ox + 50, oy - 50, 'allungamento', 'middle', 12.5, '#41708a')
            body += callout(ox + 90 * sc, oy + 9 * sc, ox + 92, oy + 54, 'cartina', 'middle', 12.5)
        b += frame(x, 20, 290, 270, t, ok=ok, sub=sub, body=body)
    b += text(20, 302, 'Linea tratteggiata verde = prolungamento della lamina naturale.', 12.5, 'start', 600, MUTED, 'italic')
    return svg(W, H + 14, arrow_defs() + b, 'Livello della cartina di profilo: troppo bassa (l\'allungamento cade), in livello (prosegue la lamina), '
               'troppo alta (punta all\'insù)')


def ghost(svgs, op=0.5):
    """Disegno 'in trasparenza' (dito sotto la cartina, per mostrare dove va a toccare)."""
    return '<g opacity="%.2f">%s</g>' % (op, svgs)


@figx('cartina-adattata.svg')
def form_adapt():
    W, H = 940, 330
    b = ''
    T = [('Unghia corta', 'linguetta dritta'), ('Unghia larga', 'allarga il foro'), ('Iponichio lungo', 'incavo più profondo'),
         ('Unghia curva', 'piega di più')]
    for i, (t, sub) in enumerate(T):
        x = 20 + i * 228
        cx = x + 108
        body = ''
        if i == 0:
            ys = 172
            body += form_shape(cx, ys, 84, 100, 30, 0, cut_tab=True, center=False)
            f, p = top_finger(cx, ys + 72, hw=30, nail_len=70, free_len=2, shape='quadrata', finger_len=0)
            body += ghost(f, 0.55)
            body += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3"/>' % (cx - 30, ys, cx + 30, ys, OK)
            body += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.3"/>' % (cx + 20, ys, cx + 40, ys - 34, MUTED)
            body += '<circle cx="%d" cy="%d" r="3.5" fill="%s" stroke="#fff"/>' % (cx + 20, ys, ACC2)
            body += pill(cx + 40, ys - 40, 'bordo dritto', 13, OK)
        elif i == 1:
            ys = 172
            body += form_shape(cx, ys, 84, 100, 48, 40, center=False)
            body += ('<path d="M%d,%d A%d,%d 0 0 0 %d,%d" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="5 4"/>'
                     % (cx + 34, ys + 36, 34, 34, cx - 34, ys + 36, MUTED))
            f, p = top_finger(cx, ys + 80, hw=42, nail_len=70, free_len=8, finger_len=0)
            body += ghost(f, 0.55)
            body += arrow(cx - 24, ys + 18, cx - 50, ys + 18, ACC2, 2) + arrow(cx + 24, ys + 18, cx + 50, ys + 18, ACC2, 2)
            body += tool_scissors(cx + 60, ys - 30, -60, 0.8)
            body += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.3"/>' % (cx - 24, ys + 12, cx - 40, ys - 34, MUTED)
            body += pill(cx - 40, ys - 40, 'foro originale', 12, MUTED)
        elif i == 2:
            ys = 156
            body += form_shape(cx, ys, 84, 92, 36, 44, notch=30, center=False)
            body += ('<path d="M%d,%d A%d,%d 0 0 0 %d,%d" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="5 4"/>'
                     % (cx + 36, ys + 36, 36, 44, cx - 36, ys + 36, MUTED))
            f, p = top_finger(cx, ys + 96, hw=32, nail_len=74, free_len=18, finger_len=0)
            hypo = '<ellipse cx="%d" cy="%d" rx="26" ry="11" fill="#e0708c" opacity=".75"/>' % (cx, p['y_s'] - 6)
            body += ghost(f, 0.55) + hypo
            body += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.3"/>' % (cx + 14, p['y_s'] - 8, cx + 46, ys - 46, MUTED)
            body += '<circle cx="%d" cy="%d" r="3.5" fill="%s" stroke="#fff"/>' % (cx + 14, p['y_s'] - 8, ACC2)
            body += pill(cx + 46, ys - 52, 'iponichio', 13)
        else:
            cy = 196
            body += finger_front(cx, cy, 50, 34)
            body += ('<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="%s" stroke-width="9" stroke-linecap="round"/>'
                     % (cx - 64, cy + 16, cx, cy - 2 * 34 + 2, cx + 64, cy + 16, FORM_S))
            body += ('<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="#f6e7a8" stroke-width="6" stroke-linecap="round"/>'
                     % (cx - 64, cy + 16, cx, cy - 2 * 34 + 2, cx + 64, cy + 16))
            body += arrow(cx - 84, cy - 14, cx - 70, cy + 8, ACC2, 2) + arrow(cx + 84, cy - 14, cx + 70, cy + 8, ACC2, 2)
            body += callout(cx - 26, cy - 36, cx - 50, 116, 'unghia', 'middle', 13)
            body += callout(cx + 44, cy - 6, cx + 56, 116, 'cartina', 'middle', 13)
            body += text(cx, 276, 'vista dalla punta', 12.5, 'middle', 600, MUTED, 'italic')
        b += frame(x, 20, 216, 290, t, sub=sub, body=body, subcol=INK)
    return svg(W, H, arrow_defs() + b, 'Quattro modi di adattare la cartina: linguetta dritta per l\'unghia corta, foro più largo, '
               'incavo più profondo per l\'iponichio lungo, cartina più piegata per l\'unghia curva')


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
        if i == 1:
            body += text(cx, 252, 'dove tocca la pelle', 12.5, 'middle', 700, ACC2)
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
    s, p = overlay_profile(150, 236, L=190, free=20, ext=160, apex_h=36, tip=False)
    b += s
    xa, ax, xb, xe, oy = p['xa'], p['ax'], p['xb'], p['xe'], p['oy']
    for n, zx, lab, top in ((3, xa + 44, 'sottile', 18), (2, ax, 'apex', 36), (1, xb - 56, 'sottile', 12)):
        b += zone_badge(zx, 116, n, lab, ACC2)
        b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.2" stroke-dasharray="3 3"/>' % (
            zx, 156, zx, oy - top, MUTED)
    b += '<circle cx="%.1f" cy="%.1f" r="5" fill="%s"/>' % (xe, oy + 6, ERR)
    b += callout(xe, oy + 6, xe + 30, oy + 96, 'punto di stress', 'middle', 13, ERR)
    b += dim(p['ox'] + 2, oy - 18, xa + 2, oy - 18, '', 'above')
    b += text(p['ox'] - 4, oy - 32, '≈ 1 mm dalla pelle', 12.5, 'end', 700, ACC2)
    b += dim(xb + 14, oy - 6, xb + 14, oy + 7, '', 'right')
    b += text(xb + 2, oy + 32, '≈ 0,8–1 mm', 13, 'middle', 800, ACC2)
    # carta di credito
    b += '<rect x="%.1f" y="%.1f" width="40" height="26" rx="4" fill="#cfe0f0" stroke="%s"/>' % (xb - 70, oy + 46, PROD_S)
    b += '<rect x="%.1f" y="%.1f" width="40" height="6" fill="%s"/>' % (xb - 70, oy + 52, PROD_S)
    b += mtext(xb - 24, oy + 56, ['come una carta', 'di credito'], 12, 'start', 600, MUTED)
    # sezione trasversale sul dito
    b += '<rect x="620" y="60" width="300" height="290" rx="16" fill="%s"/>' % PANEL
    b += text(770, 88, 'Sezione trasversale', 15, weight=700)
    b += text(770, 106, '(vista dalla punta)', 12.5, fill=MUTED)
    cx, cy = 770, 256
    pc = uid('zt')
    b += '<defs><clipPath id="%s"><rect x="620" y="60" width="300" height="290" rx="16"/></clipPath></defs>' % pc
    b += '<g clip-path="url(#%s)">%s</g>' % (pc, finger_front(cx, cy, 92, 40))
    b += ('<path d="M%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="url(#bProdV)" stroke="%s" stroke-width="1.6" stroke-linejoin="round"/>'
          % (cx - 96, cy - 2, cx, cy - 2 * 40 - 4 - 40, cx + 96, cy - 2, cx + 92, cy - 4, cx, cy - 2 * 40 - 4, cx - 92, cy - 4, PROD_S))
    b += dim(cx, cy - 46, cx, cy - 62, '', 'right')
    b += text(cx, cy - 78, 'centro più spesso', 13, 'middle', 700, ACC2)
    b += text(cx, 330, 'lati sottili e uguali', 13.5, 'middle', 700)
    b += arrow(cx - 60, 316, cx - 88, cy - 6, MUTED, 1.4) + arrow(cx + 60, 316, cx + 88, cy - 6, MUTED, 1.4)
    return svg(W, H, arrow_defs() + b, 'Spessori della ricostruzione in sezione longitudinale (zone 3, 2, 1) e trasversale (centro più spesso, lati sottili)')


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
            body += scaled(x + 100, 190, 0.8, s)
            axx = x + 100 + p['ax'] * 0.8
            body += arrow(axx, 104, axx, 190 - 26 * 0.8 - 4, ACC2, 2.2)
            body += text(axx, 96, 'apex', 13, 'middle', 800, ACC2)
        elif i == 1:
            cx, cy = x + 145, 214
            body += finger_front(cx, cy, 80, 34)
            body += ('<path d="M%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="url(#bProdV)" stroke="%s" stroke-width="1.6" stroke-linejoin="round"/>'
                     % (cx - 84, cy - 2, cx, cy - 2 * 34 - 4 - 34, cx + 84, cy - 2, cx + 80, cy - 4, cx, cy - 2 * 34 - 4, cx - 80, cy - 4, PROD_S))
            body += dashed(cx, 100, cx, 262, ACC2, 1.4, '5 4')
            body += dim(cx - 84, 116, cx, 116, '', 'above', OK) + dim(cx, 116, cx + 84, 116, '', 'above', OK)
            body += text(cx, 108, '=', 18, 'middle', 800, OK)
        else:
            cx, yc = x + 145, 232
            extra = ('<path d="M%d,%d L%d,%d" stroke="#fff" stroke-width="9" stroke-linecap="round" opacity=".95" clip-path="url(#CLIP)"/>'
                     % (cx, yc - 30, cx, yc - 170))
            f, p = top_finger(cx, yc, hw=36, nail_len=100, free_len=50, shape='squoval', free=PROD, plate='#f3c6d3', extra=extra, finger_len=4)
            body += f
            body += desk_lamp(x + 50, 90, 0.8)
            body += rays(x + 74, 104, x + 108, 128, 3, 0, 16)
        b += frame(x, 20, 290, 280, t, sub=sub, body=body, subcol=INK)
        b += eye(x + 30, 46, 0, 1.0)
    return svg(W, H, arrow_defs() + b, 'Controllo dell\'apex da tre punti di vista: profilo, fronte, alto con luce')


def horiz_finger(x, y, s=1.0, **kw):
    """finger_nail ruotato con la punta verso destra; (x, y) = posizione della base dell'unghia."""
    f, p = finger_nail(0, 0, **kw)
    return '<g transform="translate(%.1f,%.1f) rotate(90) scale(%.2f)">%s</g>' % (x, y, s, f), p


def hbrace(x0, x1, y, up=True, col=ACC2, w=2):
    """Parentesi graffa orizzontale da x0 a x1 (punta verso l'alto se up)."""
    d = -1 if up else 1
    m = (x0 + x1) / 2
    return ('<path d="M%.1f,%.1f q0,%.1f 10,%.1f L%.1f,%.1f q10,0 10,%.1f q0,%.1f 10,%.1f L%.1f,%.1f q10,0 10,%.1f" fill="none" stroke="%s" stroke-width="%s"/>'
            % (x0, y, 10 * d, 10 * d, m - 10, y + 10 * d, 10 * d, -10 * d, -10 * d, x1 - 10, y + 10 * d, -10 * d, col, w))


@figx('lunghezza-proporzioni.svg')
def length_prop():
    W, H = 760, 340
    b = text(20, 38, 'La regola della metà', 20, 'start', 800, ACC2)
    bx, by = 170, 196
    L = 220
    fr = 0.5
    # contorno "troppo lungo" (fantasma) dietro all'unghia
    xs = bx + L
    b += ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="6 5"/>'
          % (xs, by - 46, xs + L * 0.85 - 20, by - 46, xs + L * 0.85 + 4, by, xs + L * 0.85 - 20, by + 46, xs, by + 46, ERR))
    f, p = horiz_finger(bx, by, 1.0, hw=48, nail_len=L, free_len=L * fr, shape='squoval', smile=10, finger_len=110)
    b += f
    b += hbrace(bx - 4, xs, 102)
    b += text((bx + xs) / 2, 74, 'letto ungueale = 1', 14, 'middle', 800, ACC2)
    b += hbrace(xs + 2, xs + L * fr, 102, col=OK)
    b += text(xs + L * fr / 2, 74, 'bordo libero ≤ ½', 14, 'middle', 800, OK)
    for frac, lab, col in ((1 / 3, '1/3', MUTED), (0.5, '1/2', OK), (0.85, '', ERR)):
        xx = xs + L * frac
        b += dashed(xx, 138, xx, 262, col, 2, '6 5')
        if lab:
            b += text(xx, 284, lab, 15, 'middle', 800, col)
    b += mark(xs + L * fr, 124, True, 11)
    b += text(xs + L * 0.5, 304, 'massimo consigliato', 12.5, 'middle', 700, OK)
    b += mtext(xs + L * 0.85 + 10, 150, ['troppo per', 'iniziare'], 13, 'start', 800, ERR)
    b += mark(xs + L * 0.85, 124, False, 11)
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
        body += dashed(xe, 120, xe, 176, ERR, 1.4, '4 4')
        axx = x + 110 + p['ax'] * sc
        body += arrow(axx, 84, axx, 170 - ah * sc - 4, ACC2, 2)
        body += text(axx, 76, 'apex', 13, 'middle', 800, ACC2)
        body += text(xe + 6, 202, 'punto di stress', 12, 'start', 600, ERR) if i == 0 else ''
        b += frame(x, 20, 350, 260, t, body=body)
    return svg(W, H, arrow_defs() + b, 'Unghia corta e unghia lunga: l\'apex cresce e resta sopra il punto di stress')


@figx('curva-c-percentuali.svg')
def ccurve_pct():
    W, H = 760, 330
    b = text(20, 38, 'Curva a C in percentuale di cerchio', 20, 'start', 800, ACC2)
    for i, (f, pct, lab, sub) in enumerate([(0.30, '≈30%', 'bassa', 'unghie piatte'), (0.40, '≈40%', 'salone', 'il riferimento'),
                                             (0.50, '≈50%', 'gara', 'molto stretta')]):
        x = 20 + i * 245
        cx, cy, r = x + 115, 168, 64
        body = '<circle cx="%d" cy="%d" r="%d" fill="#fff" stroke="#d9c9c4" stroke-width="2" stroke-dasharray="5 5"/>' % (cx, cy, r)
        a0, a1 = 270 - 180 * f, 270 + 180 * f
        p0 = (cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0)))
        p1 = (cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1)))
        big = 1 if f > 0.5 else 0
        body += ('<path d="M%d,%d L%.1f,%.1f A%d,%d 0 %d 1 %.1f,%.1f Z" fill="%s" opacity=".10"/>'
                 % (cx, cy, p0[0], p0[1], r, r, big, p1[0], p1[1], ACC))
        body += '<line x1="%d" y1="%d" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.2" stroke-dasharray="3 3"/>' % (cx, cy, p0[0], p0[1], ACC)
        body += '<line x1="%d" y1="%d" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.2" stroke-dasharray="3 3"/>' % (cx, cy, p1[0], p1[1], ACC)
        # sezione dell'unghia ricostruita: lamina + prodotto
        body += ('<path d="M%.1f,%.1f A%d,%d 0 0 1 %.1f,%.1f" fill="none" stroke="%s" stroke-width="14" stroke-linecap="round"/>'
                 % (p0[0], p0[1], r, r, p1[0], p1[1], PROD_S))
        body += ('<path d="M%.1f,%.1f A%d,%d 0 0 1 %.1f,%.1f" fill="none" stroke="#d6ebf6" stroke-width="11" stroke-linecap="round"/>'
                 % (p0[0], p0[1], r, r, p1[0], p1[1]))
        rr = r + 4
        q0 = (cx + rr * math.cos(math.radians(a0)), cy + rr * math.sin(math.radians(a0)))
        q1 = (cx + rr * math.cos(math.radians(a1)), cy + rr * math.sin(math.radians(a1)))
        body += ('<path d="M%.1f,%.1f A%d,%d 0 0 1 %.1f,%.1f" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" opacity=".9"/>'
                 % (q0[0] + 6, q0[1] - 3, rr, rr, cx, cy - rr))
        body += ('<path d="M%.1f,%.1f A%d,%d 0 0 1 %.1f,%.1f" fill="none" stroke="%s" stroke-width="4" stroke-linecap="round"/>'
                 % (cx + (r - 6) * math.cos(math.radians(a0)), cy + (r - 6) * math.sin(math.radians(a0)), r - 6, r - 6,
                    cx + (r - 6) * math.cos(math.radians(a1)), cy + (r - 6) * math.sin(math.radians(a1)), NAIL_S))
        body += '<circle cx="%d" cy="%d" r="3" fill="%s"/>' % (cx, cy, ACC)
        body += text(cx, cy + 40, pct, 24, 'middle', 800, ACC2)
        b += frame(x, 56, 230, 238, '', body=body)
        b += text(cx, 266, lab, 16, weight=800)
        b += text(cx, 284, sub, 12.5, fill=MUTED, style='italic')
    b += text(W / 2, 318, 'Segui sempre la curva naturale della cliente.', 14, weight=600, fill=MUTED)
    return svg(W, H, b, 'Curva a C del 30, 40 e 50 per cento di un cerchio: bassa, da salone, da gara')


def qseg(p0, p1, p2, t0, t1):
    """Tratto [t0, t1] di una curva quadratica (per riflessi che seguono esattamente la forma)."""
    def B(t):
        return tuple((1 - t) ** 2 * p0[k] + 2 * t * (1 - t) * p1[k] + t * t * p2[k] for k in (0, 1))
    c = tuple((1 - t0) * (1 - t1) * p0[k] + (t0 * (1 - t1) + t1 * (1 - t0)) * p1[k] + t0 * t1 * p2[k] for k in (0, 1))
    a, e = B(t0), B(t1)
    return 'M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (a[0], a[1], c[0], c[1], e[0], e[1])


def c_arc(cx, cy, hw=80, k=38, crack=False, col='url(#bProdV)', stroke=PROD_S):
    s = ('<path d="M%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="%s" stroke="%s" stroke-width="1.6" stroke-linejoin="round"/>'
         % (cx - hw, cy, cx, cy - 2 * k - 20, cx + hw, cy, cx + hw - 8, cy + 2, cx, cy - 2 * k + 6, cx - hw + 8, cy + 2, col, stroke))
    s += '<path d="%s" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" opacity=".85"/>' % qseg(
        (cx - hw, cy + 3), (cx, cy - 2 * k - 17), (cx + hw, cy + 3), 0.2, 0.45)
    if crack:
        s += '<path d="M%d,%d l6,-8 l-4,-6 l7,-8" fill="none" stroke="%s" stroke-width="2.4"/>' % (cx + hw - 16, cy - 4, ERR)
    return s


@figx('curva-c-pinching-step.svg')
def pinch_steps():
    W, H = 940, 330
    b = ''
    # 1 pressione uguale ai lati, sull'allungamento (vista dall'alto)
    x = 20
    cx, yc = x + 145, 300
    f, p = top_finger(cx, yc, hw=34, nail_len=96, free_len=74, shape='squoval', free='#eaf4fa', finger_len=0)
    body = f
    ys = p['y_s']
    py = ys - 24
    body += thumb(cx - 52, py, 90, 0.8) + thumb(cx + 52, py, -90, 0.8)
    body += arrow(cx - 96, py - 40, cx - 66, py - 20, ACC2, 2.2) + arrow(cx + 96, py - 40, cx + 66, py - 20, ACC2, 2.2)
    body += dashed(cx - 60, ys + 2, cx + 60, ys + 2, MUTED, 1.2, '3 3')
    body += pill(cx, ys + 30, 'non sulla lamina', 12, ERR)
    body += text(cx, 92, 'stringi qui, sull\'allungamento', 12.5, 'middle', 700, ACC2)
    b += frame(x, 20, 290, 290, 'Pressione uguale ai lati', 1, body=body)
    # 2 il momento giusto
    x = 324
    body = timer(x + 145, 104, '')
    body += '<circle cx="%d" cy="104" r="28" fill="none" stroke="%s" stroke-width="2"/>' % (x + 145, ACC2)
    body += '<rect x="%d" y="152" width="250" height="58" rx="12" fill="#fff"/>' % (x + 20)
    body += bead(x + 50, 181, 13, '#f6e3e9', '#c9b8bf')
    body += text(x + 76, 176, 'acrilico:', 14, 'start', 800)
    body += text(x + 76, 196, 'opaco ma ancora morbido', 13, 'start', 600)
    body += '<rect x="%d" y="218" width="250" height="58" rx="12" fill="#fff"/>' % (x + 20)
    body += ('<path d="M%d,%d Q%d,%d %d,%d Z" fill="#f4f1f8" stroke="#8a7d9e" stroke-width="1.6"/>'
             '<rect x="%d" y="%d" width="36" height="4" rx="2" fill="#8a7d9e"/>'
             '<path d="M%d,%d l-3,8 M%d,%d l0,8 M%d,%d l3,8" stroke="#9a6be0" stroke-width="1.4" opacity=".7"/>'
             % (x + 32, 258, x + 50, 222, x + 68, 258, x + 32, 258, x + 46, 240, x + 50, 240, x + 54, 240))
    body += text(x + 76, 242, 'gel:', 14, 'start', 800)
    body += text(x + 76, 262, 'dopo una flash cure', 13, 'start', 600)
    b += frame(x, 20, 290, 290, 'Il momento giusto', 2, body=body)
    # 3 controlla dal davanti
    x = 628
    cx = x + 104
    body = finger_front(cx, 214, 60, 26)
    body += c_arc(cx, 206, 76, 30) + mark(cx, 140, True, 13)
    body += dashed(cx, 156, cx, 250, OK, 1.4, '5 4')
    body += '<rect x="%d" y="70" width="96" height="104" rx="12" fill="#fff"/>' % (x + 184)
    body += c_arc(x + 232, 136, 36, 12, True)
    body += mark(x + 264, 88, False, 11)
    body += mtext(x + 232, 152, ['troppo tardi:', 'crepe'], 12.5, 'middle', 700, ERR)
    body += text(cx, 284, 'curva simmetrica', 13, 'middle', 700, OK)
    b += frame(x, 20, 290, 290, 'Controlla dal davanti', 3, body=body)
    return svg(W, H, arrow_defs() + b, 'Pinching passo passo: pressione uguale ai lati sull\'allungamento, momento giusto, controllo frontale della curva')


def flip_icon(cx, cy, r=20):
    """Freccia circolare: 'capovolgi la mano'."""
    return ('<path d="M%.1f,%.1f A%.1f,%.1f 0 1 1 %.1f,%.1f" fill="none" stroke="%s" stroke-width="2.6" marker-end="url(#ar)"/>'
            % (cx - r, cy, r, r, cx + r * 0.2, cy + r * 0.98, ACC2))


@figx('tut-gel-flip.svg')
def gel_flip():
    W, H = 760, 300
    b = ''
    T = ['Perla in zona 2', 'Capovolgi', 'Controlla e polimerizza']
    for i, t in enumerate(T):
        x = 20 + i * 245
        body = ''
        if i == 0:
            s, p = overlay_profile(0, 0, L=110, free=10, ext=60, apex_h=6, tip=False)
            s += bead(p['xe'] - 26, -18, 15, PROD, PROD_S)
            body += scaled(x + 92, 196, 0.78, s)
            body += callout(x + 92 + (p['xe'] - 26) * 0.78, 196 - 26 * 0.78, x + 150, 104, 'perla di gel', 'middle', 13,
                            sub='sul punto di stress')
        elif i == 1:
            s, p = overlay_profile(0, 0, L=110, free=10, ext=60, apex_h=22, tip=False)
            body += scaled(x + 60, 150, 0.66, '<g transform="rotate(180 70 0)">%s</g>' % s)
            body += flip_icon(x + 40, 112, 17)
            body += arrow(x + 84, 166, x + 84, 204, ACC2, 2.4)
            body += text(x + 100, 194, '5–30 s', 15, 'start', 800, ACC2)
            body += text(x + 115, 232, 'la gravità forma l\'apex', 12.5, 'middle', 700, ACC2)
            body += text(x + 115, 252, 'unghia verso il basso', 12.5, 'middle', 600, MUTED)
        else:
            s, p = overlay_profile(0, 0, L=110, free=10, ext=60, apex_h=22, tip=False)
            body += lamp(x + 150, 236, 130)
            body += scaled(x + 82, 214, 0.62, s)
            body += eye(x + 34, 88, 20, 1.0)
            body += text(x + 56, 92, 'profilo ok?', 12.5, 'start', 700, ACC2)
        b += frame(x, 20, 230, 260, t, i + 1, body=body)
    return svg(W, H, arrow_defs() + b, 'Capovolgere la mano: perla di gel in zona 2, mano capovolta perché la gravità formi l\'apex, controllo del profilo e lampada')


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
    """Bicchierino dappen in vetro spesso, con monomero o polvere; yb = base."""
    s = '<ellipse cx="%d" cy="%d" rx="40" ry="6" fill="#000" opacity=".1"/>' % (cx, yb + 2)
    s += ('<path d="M%d,%d L%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="url(#bGlass)" stroke="#8d8a96" stroke-width="1.6"/>'
          % (cx - 46, yb - 62, cx + 46, yb - 62, cx + 34, yb - 4, cx + 33, yb, cx + 28, yb, cx - 28, yb, cx - 33, yb, cx - 34, yb - 4))
    s += '<ellipse cx="%d" cy="%d" rx="46" ry="7" fill="#f7f9fb" stroke="#8d8a96" stroke-width="1.4"/>' % (cx, yb - 62)
    if liquid:
        s += '<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="#cfe6f7" opacity=".9"/>' % (cx - 40, yb - 42, cx + 40, yb - 42, cx + 29, yb - 10, cx - 29, yb - 10)
        s += '<ellipse cx="%d" cy="%d" rx="40" ry="5" fill="#e6f3fb" stroke="#9cc7e2" stroke-width="1"/>' % (cx, yb - 42)
    if powder:
        s += '<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="#fbf7f8"/>' % (cx - 40, yb - 44, cx + 40, yb - 44, cx + 29, yb - 10, cx - 29, yb - 10)
        s += ('<path d="M%d,%d Q%d,%d %d,%d Q%d,%d %d,%d" fill="#ffffff" stroke="#e2d8dc" stroke-width="1.2"/>'
              % (cx - 41, yb - 44, cx - 10, yb - 60, cx + 10, yb - 52, cx + 30, yb - 46, cx + 41, yb - 44))
        s += dust(cx, yb - 32, 10, 18, '#e8dfe3')
    s += '<path d="M%d,%d L%d,%d" stroke="#fff" stroke-width="3" opacity=".8" stroke-linecap="round"/>' % (cx - 36, yb - 52, cx - 27, yb - 12)
    return s


def acr_brush(x, y, ang=0, l=120, wet=False, s=1.0):
    """Pennello da acrilico (kolinsky): punta delle setole in (x, y), ventre pieno, ghiera, manico verso +x."""
    bc = '#e9dccb' if not wet else '#d8e8f4'
    b = ('<path d="M50,-5.2 L%.1f,-3.6 Q%.1f,0 %.1f,3.6 L50,5.2 Z" fill="url(#bHandle)"/>' % (50 + l, 54 + l, 50 + l))
    b += '<line x1="54" y1="-2.6" x2="%.1f" y2="-1.8" stroke="#fff" stroke-width="1.1" opacity=".35" stroke-linecap="round"/>' % (44 + l)
    b += ('<path d="M33,-7 L52,-6 L52,6 L33,7 Z" fill="url(#bFerrule)" stroke="#7d868f" stroke-width=".6"/>'
          '<path d="M38,-6.8 v13.6 M42,-6.6 v13.2" stroke="#7d868f" stroke-width=".9"/>')
    b += ('<path d="M34,-6.6 C24,-9 12,-8 4,-3 Q0,0 4,3 C12,8 24,9 34,6.6 Z" fill="%s" stroke="#8a7a68" stroke-width=".8"/>' % bc)
    b += ('<path d="M33,-3.6 C22,-4.6 12,-3.6 5,-1 M33,0 L3,0 M33,3.6 C22,4.6 12,3.6 5,1" fill="none" stroke="#fff" stroke-width=".7" opacity=".6"/>'
          '<path d="M33,-5.4 C22,-7 12,-6 6,-2.4" fill="none" stroke="#8a7a68" stroke-width=".6" opacity=".5"/>')
    return _g(x, y, ang, s, b)


@figx('acrilico-pennello-carico.svg')
def acrylic_load():
    W, H = 940, 300
    b = ''
    T = [('Immergi nel monomero', ''), ('Scarica sul bordo', 'non deve gocciolare'), ('Tocca la polvere', 'si forma la perla'),
         ('Perla pronta', 'lucida e bombata')]
    for i, (t, sub) in enumerate(T):
        x = 20 + i * 228
        cx = x + 100
        body = ''
        if i == 0:
            body += dappen(cx, 218)
            body += acr_brush(cx - 4, 200, -66, 84, wet=True)
            # superficie del liquido davanti alle setole
            body += '<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="#cfe6f7" opacity=".55"/>' % (cx - 40, 176, cx + 40, 176, cx + 29, 208, cx - 29, 208)
            for k in range(3):
                body += '<circle cx="%d" cy="%d" r="%.1f" fill="#fff" stroke="#9cc7e2"/>' % (cx + 6 + k * 7, 188 - k * 7, 2.6 - k * 0.5)
            body += text(cx + 46, 122, 'solo le', 12.5, 'start', 700, ACC2)
            body += text(cx + 46, 138, 'setole', 12.5, 'start', 700, ACC2)
        elif i == 1:
            body += dappen(cx, 218)
            body += acr_brush(cx + 40, 154, -36, 110, wet=True)
            body += drop_c(cx + 34, 180, '#86bfe0', '#3d8fc6', s=0.8)
            body += ('<path d="M%d,%d q-4,18 -26,22" fill="none" stroke="%s" stroke-width="2.2" marker-end="url(#ar)"/>' % (cx + 64, 112, ACC2))
            body += text(cx + 20, 104, 'strofina', 12.5, 'middle', 700, ACC2)
        elif i == 2:
            body += dappen(cx, 218, liquid=False, powder=True)
            body += acr_brush(cx + 6, 164, -44, 110, wet=True)
            body += bead(cx + 2, 168, 9, '#ffffff', '#c9b8bf')
            body += ('<path d="M%d,%d q-30,-4 -38,22" fill="none" stroke="%s" stroke-width="2.2" marker-end="url(#ar)"/>' % (cx - 4, 118, ACC2))
            body += text(cx - 50, 108, 'trascina', 12.5, 'middle', 700, ACC2)
        else:
            body += acr_brush(cx - 6, 176, -24, 130, wet=True)
            body += bead(cx - 18, 182, 17, '#ffffff', '#c9b8bf')
            body += ('<ellipse cx="%d" cy="%d" rx="6" ry="3.5" fill="#fff"/>' % (cx - 24, 174))
            body += timer(x + 40, 92, '3–5 s')
            body += text(cx + 8, 226, 'né secca né colante', 12.5, 'middle', 600, MUTED, 'italic')
        b += frame(x, 20, 216, 250, t, i + 1, sub=sub or None, body=body, subcol=INK)
    b += text(W / 2, 292, 'Guanti, aspiratore, niente monomero sulla pelle.', 14, weight=700, fill=ERR)
    return svg(W, H + 6, arrow_defs() + b, 'Come si carica il pennello per l\'acrilico: immergi nel monomero, scarica sul bordo, '
               'tocca la polvere, perla pronta lucida e bombata')


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
        cx, yc = x + 145, 284
        body = ''
        f, p = top_finger(cx, yc, hw=36, nail_len=110, free_len=6, finger_len=0)
        ys = p['y_s'] - 6
        body += form_shape(cx, ys, 100, 72, 38, 44)
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


def _pro_finger(shape, hw=34, nail_len=86, free_len=50, flen=120, fw=None, plate=NAIL, free=FREE, weak=False):
    """Dito con unghia vista dall'alto, resa "da manuale" (coordinate locali: punta in alto, cuticola in y=0, asse x=0).
    Dito affusolato con polpastrello che sporge ai lati, pieghe laterali, eponichio, lunula, curva a C ombreggiata,
    bordo libero con smile line naturale e riflesso. weak=True segna in rosso i punti fragili della forma."""
    fw = fw or hw * 1.36
    y_s = -nail_len
    y_t = y_s - free_len
    ytip = y_s - hw * 0.30          # polpastrello
    # dito: leggermente più largo alla base, fianchi morbidi, punta arrotondata
    fpath = ('M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f '
             'C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f Z' % (
                 -fw * 1.06, flen,
                 -fw * 1.04, flen * .4, -fw * 1.02, y_s * .2, -fw, y_s * .55,
                 -fw * .98, y_s - hw * .05, -fw * .7, ytip, 0, ytip,
                 fw * .7, ytip, fw * .98, y_s - hw * .05, fw, y_s * .55,
                 fw * 1.02, y_s * .2, fw * 1.04, flen * .4, fw * 1.06, flen,
                 -fw * 1.06, flen))
    s = '<path d="%s" fill="%s" stroke="%s" stroke-width="1.4"/>' % (fpath, SKIN, SKIN_D)
    # pieghe dell'articolazione
    for j, k in enumerate((.62, .74)):
        s += '<path d="M%.1f,%.1f Q0,%.1f %.1f,%.1f" stroke="%s" stroke-width="1.2" fill="none" opacity=".55"/>' % (
            -fw * (.55 - j * .12), flen * k, flen * k + 5, fw * (.55 - j * .12), flen * k, SKIN_D)
    outline = nail_outline(0, 0, y_s, y_t, hw, shape)
    clip = uid('pf')
    sh = uid('pfs')
    s += ('<defs><clipPath id="%s"><path d="%s"/></clipPath>'
          '<linearGradient id="%s" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7a2840" stop-opacity=".28"/>'
          '<stop offset=".2" stop-color="#7a2840" stop-opacity=".04"/><stop offset=".5" stop-color="#7a2840" stop-opacity="0"/>'
          '<stop offset=".8" stop-color="#7a2840" stop-opacity=".05"/><stop offset="1" stop-color="#7a2840" stop-opacity=".3"/></linearGradient></defs>'
          % (clip, outline, sh))
    s += '<path d="%s" fill="%s"/>' % (outline, plate)
    s += '<ellipse cx="0" cy="-12" rx="%.1f" ry="20" fill="#fff" opacity=".5" clip-path="url(#%s)"/>' % (hw * .52, clip)
    if free_len > 0:
        s += ('<path d="M%.1f,%.1f Q0,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" clip-path="url(#%s)"/>'
              % (-hw - 4, y_s + 7, y_s - 9, hw + 4, y_s + 7, hw + 4, y_t - 40, -hw - 4, y_t - 40, free, clip))
        s += ('<path d="M%.1f,%.1f Q0,%.1f %.1f,%.1f" stroke="#e9c3cf" stroke-width="1.6" fill="none" clip-path="url(#%s)"/>'
              % (-hw - 4, y_s + 7, y_s - 9, hw + 4, y_s + 7, clip))
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#%s)" clip-path="url(#%s)"/>' % (-hw, y_t - 4, 2 * hw, -y_t + 8, sh, clip)
    s += ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="#fff" opacity=".45" clip-path="url(#%s)"/>'
          % (-hw * .58, y_t + 8, hw * .18, -y_t - 30, hw * .09, clip))
    s += '<path d="%s" fill="none" stroke="%s" stroke-width="1.6"/>' % (outline, NAIL_S)
    # pieghe laterali ed eponichio
    for sx in (-1, 1):
        s += '<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f" stroke="%s" stroke-width="1.4" fill="none"/>' % (
            sx * (hw + 2), -16, sx * (hw + 4), y_s * .4, sx * (hw + 3), y_s * .8, sx * (hw + 1), y_s + 6, SKIN_D)
    s += ('<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f 0,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s"/>'
          % (-fw * .99, -24, -hw - 6, -24, -hw * .7, 10, 10, hw * .7, 10, hw + 6, -24, fw * .99, -24, fw * 1.0, 26, -fw * 1.0, 26, SKIN))
    s += ('<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f 0,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f" stroke="%s" stroke-width="1.6" fill="none"/>'
          % (-hw - 6, -24, -hw * .9, 2, -hw * .7, 10, 10, hw * .7, 10, hw * .9, 2, hw + 6, -24, SKIN_D))
    s += ('<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f 0,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f" stroke="#fff" stroke-width="2.4" fill="none" opacity=".45"/>'
          % (-hw * .85, -10, -hw * .75, 8, -hw * .55, 15, 15, hw * .55, 15, hw * .75, 8, hw * .85, -10))
    if weak:
        pts = {'quadrata': [(-hw, y_t), (hw, y_t)], 'ballerina': [(-hw * .52, y_t), (hw * .52, y_t)],
               'stiletto': [(0, y_t)], 'mandorla': [(0, y_t)]}.get(shape, [])
        for (px, py) in pts:
            s += '<circle cx="%.1f" cy="%.1f" r="7" fill="%s" fill-opacity=".18" stroke="%s" stroke-width="2"/>' % (px, py, ERR, ERR)
    return s


def _place(x, y, s, inner, ang=0):
    return '<g transform="translate(%.1f,%.1f) rotate(%.1f) scale(%.3f)">%s</g>' % (x, y, ang, s, inner)


@figx('forme-scelta-dita.svg')
def shapes_fingers():
    W, H = 940, 360
    b = ''
    rows = [('Dito corto', 'e largo', dict(hw=40, nail_len=58, flen=64, fw=60), [('quadrata', False, 'accorcia'), ('ovale', True, 'allunga'), ('mandorla', True, 'slancia')]),
            ('Dito lungo', 'e sottile', dict(hw=26, nail_len=90, flen=118, fw=36), [('quadrata', True, 'equilibra'), ('squoval', True, 'equilibra'), ('stiletto', None, 'molto lunga')])]
    FL = {'quadrata': 34, 'squoval': 34, 'ovale': 46, 'mandorla': 52, 'stiletto': 66}
    for r, (l1, l2, geo, items) in enumerate(rows):
        y0 = 20 + r * 170
        b += '<rect x="20" y="%d" width="900" height="158" rx="16" fill="%s"/>' % (y0, PANEL)
        b += mtext(36, y0 + 72, [l1, l2], 16, 'start', 800, ACC2)
        for k, (sh, ok, eff) in enumerate(items):
            bx = 300 + k * 230
            yy = y0 + 88
            s = .72
            fin = _pro_finger(sh, geo['hw'], geo['nail_len'], FL[sh], geo['flen'], geo['fw'])
            b += _place(bx, yy, s, fin, 90)
            # sfumatura della base del dito nel pannello
            gid = uid('fd')
            x0 = bx - geo['flen'] * s - 2
            b += ('<defs><linearGradient id="%s" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fbf2ef"/>'
                  '<stop offset="1" stop-color="#fbf2ef" stop-opacity="0"/></linearGradient></defs>' % gid)
            b += '<rect x="%.1f" y="%.1f" width="46" height="%.1f" fill="url(#%s)"/>' % (x0, yy - geo['fw'] * s * 1.2, geo['fw'] * s * 2.4, gid)
            name = {'quadrata': 'Quadrata', 'ovale': 'Ovale', 'mandorla': 'Mandorla', 'squoval': 'Squoval', 'stiletto': 'Stiletto'}[sh]
            b += text(bx - 4, y0 + 32, name, 14.5, 'start', 800)
            if ok is None:
                b += excl(bx - 20, y0 + 27, 11)
            else:
                b += mark(bx - 20, y0 + 27, ok, 11)
            b += text(bx + 10, y0 + 146, eff, 13, 'middle', 700, OK if ok else (ERR if ok is False else WARN))
    return svg(W, H, b, 'La stessa forma su dita diverse: come cambia l\'effetto su dita corte e larghe o lunghe e sottili')


@figx('forme-resistenza.svg')
def shapes_strength():
    W, H = 940, 300
    b = text(20, 34, 'Dalla più resistente alla più delicata', 20, 'start', 800, ACC2)
    b += ('<circle cx="%d" cy="29" r="7" fill="%s" fill-opacity=".18" stroke="%s" stroke-width="2"/>' % (782, ERR, ERR)
          + text(796, 34, 'punto fragile', 13, 'start', 600, ERR))
    order = [('squoval', 'Squoval'), ('tonda', 'Tonda'), ('ovale', 'Ovale'), ('quadrata', 'Quadrata'), ('mandorla', 'Mandorla'),
             ('ballerina', 'Ballerina'), ('stiletto', 'Stiletto')]
    base = 206
    for k, (sh, name) in enumerate(order):
        cx = 84 + k * 128
        fl = 30 if sh in ('quadrata', 'squoval', 'tonda') else (54 if sh != 'stiletto' else 62)
        b += _place(cx, base, .9, _pro_finger(sh, 30, 66, fl, 36, 42, weak=True))
        b += text(cx, base + 52, name, 14, weight=800)
    # sfumatura della base delle dita
    b += ('<defs><linearGradient id="gfade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
          '<stop offset="1" stop-color="#fff"/></linearGradient></defs>')
    b += '<rect x="0" y="%d" width="%d" height="28" fill="url(#gfade)"/>' % (base + 6, W)
    b += ('<defs><linearGradient id="gres" x1="0" x2="1"><stop offset="0" stop-color="%s"/><stop offset=".5" stop-color="#e8c25a"/>'
          '<stop offset="1" stop-color="%s"/></linearGradient></defs>' % (OK, ERR))
    b += '<rect x="40" y="%d" width="860" height="12" rx="6" fill="url(#gres)"/>' % (base + 62)
    b += '<path d="M40,%d l-12,6 l12,6 Z" fill="%s"/><path d="M900,%d l12,6 l-12,6 Z" fill="%s"/>' % (base + 62, OK, base + 62, ERR)
    b += text(40, base + 98, 'uso intenso delle mani', 13.5, 'start', 700, OK)
    b += text(900, base + 98, 'serve lunghezza e struttura', 13.5, 'end', 700, ERR)
    return svg(W, H + 26, b, 'Forme dell\'unghia ordinate dalla più resistente alla più delicata, con i punti fragili evidenziati')


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
            sc = 0.72
            ox, oy = x + 92, 150
            s += scaled(ox, oy, sc, sp)
            s += dashed(ox + p['xn'] * sc - 30, oy + 5 * sc, ox + p['xb'] * sc + 14, oy + 5 * sc, OK, 2.2, '6 4')
            s += mark(x + 262, oy - 34, True, 12)
            s += pill(ox + p['xb'] * sc - 40, oy + 30, 'sotto: linea dritta', 12.5, OK)
            # errore: pancia sotto l'allungamento
            s += '<rect x="%d" y="196" width="230" height="86" rx="12" fill="#fff"/>' % (x + 40)
            sp2, p2 = overlay_profile(0, 0, L=110, free=10, ext=80, apex_h=22, tip=False)
            sp2 += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="url(#bProdV)" stroke="%s" stroke-width="1.6"/>'
                    % (p2['xn'], 5, (p2['xn'] + p2['xb']) / 2, 34, p2['xb'], 4, PROD_S))
            ic = uid('in')
            s += '<defs><clipPath id="%s"><rect x="%d" y="196" width="230" height="86" rx="12"/></clipPath></defs>' % (ic, x + 40)
            s += '<g clip-path="url(#%s)">%s</g>' % (ic, scaled(x + 100, 222, 0.55, sp2))
            s += ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="4 3"/>'
                  % (x + 100 + p2['xn'] * 0.55, 226, x + 100 + (p2['xn'] + p2['xb']) / 2 * 0.55, 244, x + 100 + p2['xb'] * 0.55, 226, ERR))
            s += mark(x + 254, 212, False, 10)
            s += text(x + 200, 272, '"pancia" sotto', 12.5, 'middle', 700, ERR)
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


def op_hand_file(gx, gy):
    """Mano destra dell'operatrice vista dal lato del pollice che tiene la lima: indice disteso sopra,
    pollice sotto, medio di sostegno, anulare e mignolo raccolti, polso morbido.
    (gx, gy) = punto della lima tra indice e pollice (asse della lima)."""
    D, B = gen_svg._digit, gen_svg._blob
    HC, HD, HS = gen_svg._HAND, gen_svg._HAND_D, gen_svg._HAND_S

    def T(pts):
        return [(gx + x, gy + y) for x, y in pts]
    # avambraccio
    s = D(T([(-250, 196), (-206, 130), (-162, 70)]), [36, 33, 30], nail=0)
    # anulare e mignolo raccolti (dietro)
    s += D(T([(-96, 8), (-66, 14), (-50, 32), (-58, 50)]), [11, 10, 9, 8], nail=0, fill=HD, creases=(1, 2))
    s += D(T([(-104, 22), (-80, 34), (-70, 50), (-80, 62)]), [9.5, 8.5, 7.5, 7], nail=0, fill=HD)
    # medio: sostiene la lima da dietro
    s += D(T([(-92, -14), (-56, -12), (-22, -2), (-2, 16)]), [12, 11, 10, 9], nail=0, fill=HD, creases=(1, 2))
    # pollice sotto la lima (unghia sul lato esterno): la base sparisce sotto il dorso
    s += D(T([(-118, 46), (-74, 40), (-40, 30), (-12, 23)]), [18, 15, 12.5, 10.5], nail=1, creases=(2,))
    # dorso della mano e base del pollice
    s += B(T([(-170, 66), (-176, 20), (-150, -28), (-110, -50), (-74, -48), (-56, -34), (-58, -6), (-78, 18), (-96, 40), (-128, 70)]), HC, HS)
    s += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="%s" stroke-width="1.2" fill="none" opacity=".5"/>' % (
        gx - 140, gy - 30, gx - 112, gy - 46, gx - 82, gy - 44, HS)
    s += tool_file(gx + 60, gy, 0, 210, 20)
    # indice disteso sopra la lima (unghia sul dorso)
    s += D(T([(-90, -38), (-52, -36), (-16, -28), (14, -21)]), [13, 11.2, 9.6, 8.6], nail=-1, creases=(1, 2))
    return s


@figx('lima-presa.svg')
def file_grip():
    W, H = 760, 350
    b = ''
    gx, gy = 205, 164
    body = op_hand_file(gx, gy)
    body += callout(gx + 14, gy - 30, gx + 40, 92, 'indice sopra: presa leggera', 'middle', 13.5)
    body += callout(gx + 4, gy + 22, gx + 50, gy + 80, 'pollice sotto', 'start', 13.5)
    body += callout(gx - 150, gy + 90, gx - 90, 290, 'polso morbido', 'start', 13.5)
    body += arrow(gx + 76, gy + 48, gx + 126, gy + 48, MUTED, 1.8, True)
    body += text(gx + 101, gy + 36, 'muovi il braccio', 12.5, 'middle', 600, MUTED)
    b += frame(20, 20, 350, 310, 'La lima', 1, body=body)
    # 2 dito della cliente
    x = 390
    cx, yc = x + 130, 236
    body = '<rect x="%d" y="%d" width="200" height="56" rx="22" fill="#e9dff2" stroke="#b9a6cf"/>' % (cx - 100, yc + 18)
    body += text(cx + 50, yc + 64, 'supporto', 12.5, 'middle', 700, '#6b4fa0')
    f, p = top_finger(cx, yc, hw=32, nail_len=104, free_len=36, shape='squoval', finger_len=40)
    body += f
    pcl = uid('pc')
    body += '<defs><clipPath id="%s"><rect x="%d" y="20" width="350" height="310" rx="16"/></clipPath></defs>' % (pcl, x)
    for sx in (-1, 1):   # pollici dell'operatrice ai lati del dito (visti dal dorso)
        body += '<g clip-path="url(#%s)">' % pcl + gen_svg._digit([(cx + sx * 130, yc - 26), (cx + sx * 104, yc - 31), (cx + sx * 76, yc - 35), (cx + sx * 54, yc - 37)],
                               [16, 14.5, 12.5, 11], nail=1, view='top', creases=(1, 2)) + '</g>'
    body += arrow(cx - 52, yc - 70, cx - 70, yc - 96, ACC2, 2)
    body += text(cx - 78, yc - 132, 'tira la pelle', 12.5, 'middle', 700, ACC2)
    body += text(cx - 78, yc - 116, 'del solco', 12.5, 'middle', 700, ACC2)
    body += callout(cx + 70, yc - 40, cx + 90, yc - 100, 'ai lati', 'middle', 12.5)
    body += text(cx + 90, yc - 116, 'tieni', 12.5, 'middle', 700)
    # riquadro errore
    body += '<rect x="%d" y="64" width="84" height="158" rx="10" fill="#fff"/>' % (x + 254)
    g, _ = top_finger(0, 0, hw=34, nail_len=90, free_len=20, finger_len=10)
    g += gen_svg._digit([(40, 30), (27, -8), (12, -46)], [27, 25, 22], nail=1, view='top', creases=(1,))
    body += scaled(x + 296, 152, 0.55, g)
    body += mark(x + 324, 80, False, 10)
    body += text(x + 296, 194, 'non sopra', 12, 'middle', 700, ERR)
    body += text(x + 296, 210, 'l\'unghia', 12, 'middle', 700, ERR)
    b += frame(x, 20, 350, 310, 'Il dito della cliente', 2, body=body)
    return svg(W, H, arrow_defs() + b, 'Presa della lima (indice sopra, pollice sotto, polso morbido) e presa del dito della cliente ai lati')


@figx('limatura-sequenza.svg')
def file_sequence():
    labels = ['Lunghezza', 'Lati', 'Punta', 'Superficie', 'Zona cuticolare', 'Sotto il bordo']
    subs = ['100/180', 'piatta, parallela', 'una direzione', 'segui la curva', 'sfuma a zero', 'pulisci']

    def d(i, x, y):
        s = ''
        cx, yb = x + 120, y + 214
        sc = 0.8
        if i == 4:
            cx, yb = x + 130, y + 168
        if i in (0, 1, 2, 4):
            g, p = finger_nail(0, 0, hw=34, nail_len=90, free_len=60 if i != 4 else 22, shape='squoval' if i != 2 else 'ovale',
                               smile=8, finger_len=40)
            yt = -150
            if i == 0:
                g += tool_file(0, yt - 12, 0, 150, 18)
                g += arrow(-54, yt - 38, 54, yt - 38, ACC2, 2.6, True)
            elif i == 1:
                g += tool_file(48, yt + 64, 90, 150, 18)
                g += arrow(76, yt + 10, 76, yt + 118, ACC2, 2.6, True)
            elif i == 2:
                g += tool_file(-44, yt + 14, 45, 120, 16)
                g += arrow(-84, yt + 66, -20, yt + 2, ACC2, 3)
            else:
                g += '<path d="%s" fill="none" stroke="%s" stroke-width="3" stroke-dasharray="6 4"/>' % (epo_curve(p, -16), ACC2)
                g += tool_file(46, -40, -58, 110, 16)
                g += ('<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="%s" stroke-width="2.6" marker-end="url(#ar)"/>'
                      % (-44, -2, -20, 10, 4, 2, ACC2))
            s += scaled(cx, yb, sc, g)
            if i == 4:
                s += text(x + 238, y + 120, 'grana', 12.5, 'middle', 700, MUTED)
                s += text(x + 238, y + 136, 'fine', 12.5, 'middle', 700, MUTED)
        elif i == 3:
            sp, p = overlay_profile(0, 0, L=110, free=10, ext=80, apex_h=22, tip=False)
            s += scaled(x + 110, y + 150, 0.82, sp)
            s += ('<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="%s" stroke-width="2.4" marker-end="url(#ar)"/>'
                  % (x + 104, y + 116, x + 170, y + 92, x + 250, y + 132, ACC2))
        else:
            # vista dal basso: polpastrello, bordo libero in prolungamento e lima che lo pulisce
            ex = ('<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="url(#bTipG)" stroke="%s" stroke-width="1.5"/>'
                  % (cx - 40, y + 118, cx - 40, y + 70, cx, y + 62, cx + 40, y + 70, cx + 40, y + 118, cx, y + 110, cx - 40, y + 118, NAIL_S))
            ex += dust(cx - 14, y + 100, 7, 10, '#a99a92', 3)
            fu, _ = finger_under(cx, y + 100, 70, 160)
            s += ex + fu
            s += tool_file(cx + 18, y + 112, -18, 110, 14)
            s += arrow(cx - 30, y + 140, cx + 40, y + 118, ACC2, 2.2, True)
            s += pill(x + 40, y + 176, 'dal basso', 12, MUTED, 'start')
        s += text(x + 272, y + 31, subs[i], 12.5, 'end', 700, MUTED)
        return s
    return steps_fig('La sequenza di limatura', labels, 3, 290, 190, d, 'La sequenza di limatura in sei passaggi: lunghezza, lati, punta, '
                     'superficie, zona cuticolare, sotto il bordo')


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
    b += callout(ax, oy - 32, ax - 30, 80, 'apex', 'middle', 14, ACC2)
    b += text(xb - 40, 112, 'arco superiore', 14, 'middle', 800, ACC2)
    b += text(xb - 40, oy + 34, 'arco inferiore dritto', 14, 'middle', 800, OK)
    b += callout(xe, oy + 6, xe - 70, oy + 96, 'punto di stress', 'middle', 13, ERR)
    # errore
    b += '<rect x="540" y="176" width="200" height="120" rx="12" fill="%s"/>' % PANEL
    ic = uid('in')
    s2, p2 = overlay_profile(0, 0, L=80, free=8, ext=60, apex_h=8, tip=False)
    b += '<defs><clipPath id="%s"><rect x="540" y="176" width="200" height="120" rx="12"/></clipPath></defs>' % ic
    b += '<g clip-path="url(#%s)">%s</g>' % (ic, scaled(612, 236, 0.66, s2))
    b += mark(722, 194, False, 10)
    b += pill(640, 284, 'apex limato via', 13, ERR)
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
            f, p = shape_nail(cx, 262, 'ovale', 34, 90, 70, 1.0, finger_len=30)
            body += f + dashed(cx, 86, cx, 290, ACC2, 1.6, '5 4')
            yy = 150
            body += dim(cx - 34, yy, cx, yy, '', 'above', OK) + dim(cx, yy, cx + 34, yy, '', 'above', OK)
            body += text(cx, yy - 8, '=', 18, 'middle', 800, OK)
        elif i == 1:
            sp, p = overlay_profile(0, 0, L=100, free=10, ext=70, apex_h=24, tip=False)
            sp += '<circle cx="%.1f" cy="6" r="5" fill="%s"/>' % (p['xe'], ERR)
            sc = 0.68
            ox, oy = x + 66, 200
            body += scaled(ox, oy, sc, sp)
            axx = ox + p['ax'] * sc
            body += arrow(axx, 112, axx, oy - 24 * sc - 4, ACC2, 2.2)
            body += text(axx, 104, 'apex', 13, 'middle', 800, ACC2)
            body += text(x + 108, oy + 80, 'sopra il punto di stress', 12, 'middle', 600, MUTED)
        elif i == 2:
            body += finger_front(cx, 212, 64, 26)
            body += c_arc(cx, 206, 74, 30)
            body += dashed(cx, 120, cx, 262, ACC2, 1.4, '5 4')
            body += text(cx, 284 - 4, 'uguale a destra e sinistra', 12, 'middle', 600, MUTED)
        else:
            ex = ('<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="url(#bTipG)" stroke="%s" stroke-width="1.5"/>'
                  % (cx - 40, 150, cx - 40, 92, cx, 84, cx + 40, 92, cx + 40, 150, cx, 140, cx - 40, 150, NAIL_S))
            fu, _ = finger_under(cx, 128, 72, 140)
            body += ex + fu
            body += mark(cx + 60, 110, True, 11)
            body += pill(cx, 106, 'pulito', 12, OK)
        b += frame(x, 20, 216, 310, t, sub=sub, body=body, subcol=INK)
        b += eye(x + 26, 46, 0, 0.9)
    return svg(W, H, arrow_defs() + b, 'Le quattro viste del controllo finale: dall\'alto la simmetria, di profilo l\'apex, dal davanti la curva a C, '
               'dal basso la pulizia del bordo')


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
    """Mano vista dall'alto (dorso): nails = lista di (forma, lunghezza bordo libero) per pollice→mignolo.
    Le dita escono da sotto il dorso, così le basi non si vedono."""
    pos = [(x0 + 30, yb + 10, -38, 0.5), (x0 + 96, yb - 40, -6, 0.5), (x0 + 160, yb - 56, 0, 0.5), (x0 + 224, yb - 46, 5, 0.5), (x0 + 284, yb - 18, 12, 0.46)]
    tips = []
    s = ''
    for k, ((sh, fl), (fx, fy, ang, sc)) in enumerate(zip(nails, pos)):
        g, p = finger_nail(0, 0, hw=34, nail_len=80, free_len=fl, shape=sh, smile=8, finger_len=150)
        s += '<g transform="translate(%d,%d) rotate(%d) scale(%.2f)">%s</g>' % (fx, fy - 40, ang, sc, g)
        a = math.radians(ang)
        ty = -80 - fl
        tips.append((fx - ty * sc * math.sin(a), fy - 40 + ty * sc * math.cos(a)))
    # dorso della mano con le nocche
    back = ('M%d,%d L%d,%d C%d,%d %d,%d %d,%d C%d,%d %d,%d %d,%d C%d,%d %d,%d %d,%d C%d,%d %d,%d %d,%d L%d,%d Z'
            % (x0 + 60, yb + 80, x0 + 66, yb + 30,
               x0 + 70, yb + 4, x0 + 84, yb - 4, x0 + 100, yb + 2,
               x0 + 126, yb - 8, x0 + 140, yb - 14, x0 + 162, yb - 10,
               x0 + 190, yb - 14, x0 + 206, yb - 8, x0 + 226, yb - 2,
               x0 + 256, yb - 2, x0 + 280, yb + 8, x0 + 296, yb + 26, x0 + 304, yb + 80))
    s += '<path d="%s" fill="%s" stroke="%s" stroke-width="1.5"/>' % (back, SKIN, SKIN_D)
    for kx, ky in ((100, 12), (162, 2), (226, 10)):
        s += '<path d="M%d,%d q8,-5 16,0" fill="none" stroke="%s" stroke-width="1.2" opacity=".55"/>' % (x0 + kx - 8, yb + ky, SKIN_D)
    return s, tips


@figx('mano-uniformita.svg')
def hand_uniform():
    W, H = 940, 410
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
    # pugno visto dal davanti: le curve a C devono stare alla stessa altezza
    b += '<rect x="180" y="322" width="580" height="80" rx="14" fill="%s"/>' % PANEL
    b += text(196, 360, 'Pugno', 15, 'start', 800, ACC2)
    b += text(196, 378, 'dal davanti', 12, 'start', 600, MUTED)
    pc = uid('pg')
    row = ''
    for k in range(4):
        cx = 360 + k * 84
        row += finger_front(cx, 378, 26, 12)
        row += c_arc(cx, 374, 30, 11)
    b += '<defs><clipPath id="%s"><rect x="180" y="322" width="580" height="80" rx="14"/></clipPath></defs>' % pc
    b += '<g clip-path="url(#%s)">%s</g>' % (pc, row)
    b += dashed(316, 352, 650, 352, OK, 1.6, '5 4')
    b += text(744, 372, 'curve allineate', 12.5, 'end', 700, OK)
    return svg(W, H, arrow_defs() + b, 'Uniformità della mano: lunghezza, forma e curva coerenti su tutte le dita; dal davanti le curve a C sono allineate')


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
