#!/usr/bin/env python3
"""Illustrazioni del gruppo C (moduli decorazioni, manutenzione, problemi, professione). Uso: python3 tools/svg_c.py [nome.svg ...]"""
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
PROD, PROD_S = '#e3f0f7', '#9cc3d8'      # prodotto trasparente in sezione
PROD2 = '#c4def0'                        # prodotto nuovo (refill)
WHITE_S = '#cfcfcf'                      # bordo del bianco french
FUCHSIA = '#c2185b'
DARK = '#555555'                         # frecce grigio scuro
GOLD, GOLD_S = '#e2b93b', '#a8841c'
NUDE = '#f2cfc4'
PLATE_SEC = '#eaa3b7'                    # lamina in sezione
BED = '#f7c6d2'                          # letto ungueale in sezione
GREY, GREY_D = '#9aa3ad', '#6f7983'
FOIL, FOIL_S = '#d9dde2', '#9aa3ad'
YEL_BG, YEL_S = '#fff6d6', '#e3c86a'
GREEN_BG, RED_BG = '#e6f3ec', '#fbe7e4'
WOOD, WOOD_S = '#e0bf8f', '#b8956a'


# ================================================================= primitive di supporto
def defs():
    """Marcatori per le frecce: bordeaux (ar), grigio (arw), grigio scuro (ag), rosso (are), verde (aro)."""
    m = ''
    for mid, col in (('ar', ACC2), ('arw', MUTED), ('ag', DARK), ('are', ERR), ('aro', OK), ('arwn', WARN), ('arv', '#9a6be0')):
        m += ('<marker id="%s" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
              '<path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker>' % (mid, col))
    # ombra morbida per le schede bianche delle infografiche
    m += ('<filter id="cSh" x="-10%" y="-10%" width="120%" height="130%"><feDropShadow dx="0" dy="2" stdDeviation="2.5" '
          'flood-color="#5a2a3a" flood-opacity=".12"/></filter>')
    return '<defs>%s</defs>' % m


def _mid(col):
    return {ACC2: 'ar', MUTED: 'arw', DARK: 'ag', ERR: 'are', OK: 'aro', WARN: 'arwn', '#9a6be0': 'arv'}.get(col, 'ag')


def arr(x1, y1, x2, y2, col=DARK, w=2.2, both=False, dash=''):
    m = _mid(col)
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s"%s marker-end="url(#%s)"%s/>'
            % (x1, y1, x2, y2, col, w, (' marker-start="url(#%s)"' % m) if both else '', m,
               (' stroke-dasharray="%s"' % dash) if dash else ''))


def carr(d, col=DARK, w=2.2, both=False, dash=''):
    """Freccia lungo un path qualsiasi."""
    m = _mid(col)
    return ('<path d="%s" fill="none" stroke="%s" stroke-width="%s"%s marker-end="url(#%s)"%s/>'
            % (d, col, w, (' marker-start="url(#%s)"' % m) if both else '', m, (' stroke-dasharray="%s"' % dash) if dash else ''))


def title(s):
    return text(20, 38, s, 20, 'start', 800, ACC2)


def numc(x, y, n, r=14):
    return ('<circle cx="%.1f" cy="%.1f" r="%d" fill="%s"/>' % (x, y, r, ACC2)
            + text(x, y + 5.5, str(n), 15, weight=800, fill='#fff'))


def frame(x, y, w, h, head=None, num=None, ok=None, body='', cap=None, capcol=None, sub=None, hsize=15):
    """Pannello rosa: numero in alto a sinistra, titolo, ✓/✗ in alto a destra, didascalia in basso (1–2 righe)."""
    pc = uid('k')
    s = '<defs><clipPath id="%s"><rect x="%d" y="%d" width="%d" height="%d" rx="16"/></clipPath></defs>' % (pc, x, y, w, h)
    s += '<rect x="%d" y="%d" width="%d" height="%d" rx="16" fill="%s"/>' % (x, y, w, h, PANEL)
    s += '<g clip-path="url(#%s)">%s</g>' % (pc, body)
    if num is not None:
        s += numc(x + 25, y + 25, num)
    if head:
        if num is not None:
            s += text(x + 47, y + 30, head, hsize, 'start', 700)
        else:
            s += text(x + w / 2 - (12 if ok is not None else 0), y + 30, head, hsize, weight=700)
    if ok is not None:
        s += mark(x + w - 24, y + 25, ok, 13)
    if cap:
        lines = cap if isinstance(cap, (list, tuple)) else [cap]
        yy = y + h - 14 - (len(lines) - 1) * 17 - (17 if sub else 0)
        col = capcol or (OK if ok else ERR if ok is False else INK)
        for k, l in enumerate(lines):
            s += text(x + w / 2, yy + k * 17, l, 14, weight=700, fill=col)
    if sub:
        s += text(x + w / 2, y + h - 13, sub, 12.5, fill=MUTED, style='italic')
    return s


def dashed(x1, y1, x2, y2, col=MUTED, w=1.5, dash='5 4'):
    return '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s" stroke-dasharray="%s"/>' % (
        x1, y1, x2, y2, col, w, dash)


def dot(x, y, r=4.5, col=ACC2, stroke='#fff'):
    return '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" stroke="%s" stroke-width="1.5"/>' % (x, y, r, col, stroke)


def poly(pts, fill='none', stroke=INK, w=1.5, close=True, extra=''):
    d = 'M' + ' L'.join('%.1f,%.1f' % p for p in pts) + (' Z' if close else '')
    return '<path d="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>' % (d, fill, stroke, w, extra)


def smooth_d(pts):
    """Path liscio (Catmull-Rom → Bézier) che passa per i punti."""
    d = 'M%.1f,%.1f' % pts[0]
    for i in range(len(pts) - 1):
        p0 = pts[i - 1] if i > 0 else pts[i]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < len(pts) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += ' C%.1f,%.1f %.1f,%.1f %.1f,%.1f' % (c1 + c2 + p2)
    return d


def scaled(x, y, s, body):
    return '<g transform="translate(%.1f,%.1f) scale(%.3f)">%s</g>' % (x, y, s, body)


def rot(ang, cx, cy, body):
    return '<g transform="rotate(%.1f %.1f %.1f)">%s</g>' % (ang, cx, cy, body)


def box(x, y, w, h, fill='#fff', stroke='#e5d6d2', rx=10, sw=1.5):
    return '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%d" fill="%s" stroke="%s" stroke-width="%s"/>' % (x, y, w, h, rx, fill, stroke, sw)


def label_box(x, y, w, h, lines, fill='#fff', stroke='#e5d6d2', col=INK, size=14, weight=700, rx=10, sw=1.5):
    s = box(x, y, w, h, fill, stroke, rx, sw)
    lines = lines if isinstance(lines, (list, tuple)) else [lines]
    y0 = y + h / 2 - (len(lines) - 1) * size * 0.62 + size * 0.36
    for k, l in enumerate(lines):
        s += text(x + w / 2, y0 + k * size * 1.24, l, size, weight=weight, fill=col)
    return s


# ---------------------------------------------------------------- unghia vista dall'alto
def cut_y(cx, yc, hw, x):
    """Quota della linea della cuticola (piega prossimale) disegnata da finger_nail, in funzione di x."""
    u = (x - cx) / (hw + 4.0)
    return yc - 3 - 25 * u * u


def smile_pts(cx, ys, hw, d, n=24, ext=6):
    """Punti di una smile line: centro in ys (verso la punta), lati più in basso di d."""
    pts = []
    for k in range(n + 1):
        x = cx - hw - ext + (2 * hw + 2 * ext) * k / n
        u = (x - cx) / float(hw)
        pts.append((x, ys + d * u * u))
    return pts


def smile_lat(ys, d):
    """Quota della smile line ai bordi dell'unghia."""
    return ys + d


def tip_fill(cx, ys, hw, d, top, fill='#ffffff', stroke=WHITE_S, sw=1.2):
    """Zona bianca (o colorata) sopra la smile line, da passare come extra (ritagliata con CLIP)."""
    pts = smile_pts(cx, ys, hw, d)
    p = 'M' + ' L'.join('%.1f,%.1f' % q for q in pts) + ' L%.1f,%.1f L%.1f,%.1f Z' % (cx + hw + 6, top - 20, cx - hw - 6, top - 20)
    s = '<path d="%s" fill="%s" clip-path="url(#CLIP)"/>' % (p, fill)
    if stroke:
        s += '<path d="%s" fill="none" stroke="%s" stroke-width="%s" clip-path="url(#CLIP)"/>' % (
            'M' + ' L'.join('%.1f,%.1f' % q for q in pts), stroke, sw)
    return s


def nail(cx, yc, **kw):
    d = dict(hw=36, nail_len=110, free_len=55, shape='squoval', smile=0, plate=NAIL, free=NAIL, finger_len=40, lunula=False)
    d.update(kw)
    return finger_nail(cx, yc, **d)


def gloss(cx, y1, y2, w=4):
    """Riflesso lucido obliquo."""
    return ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="#fff" stroke-width="%d" fill="none" stroke-linecap="round" opacity=".85"/>'
            % (cx - 12, y2, cx - 16, (y1 + y2) / 2, cx - 8, y1, w))


def sparkle(cx, cy, r=7):
    return ('<path d="M%.1f,%.1f L%.1f,%.1f M%.1f,%.1f L%.1f,%.1f" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/>'
            % (cx - r, cy, cx + r, cy, cx, cy - r, cx, cy + r))


def brush_flat(x, y, ang=0, l=90, bristle='#eadbb8', handle=GREY):
    """Pennello piatto: punta delle setole in (x, y), manico verso ang (gradi)."""
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f)"><path d="M0,-7 L16,-6 L16,6 L0,7 Z" fill="%s" stroke="#bfa979"/>'
            '<rect x="16" y="-6" width="11" height="12" fill="#c9ccd1"/>'
            '<rect x="27" y="-4.5" width="%d" height="9" rx="4.5" fill="%s"/></g>' % (x, y, ang, bristle, l, handle))


def brush_liner(x, y, ang=0, l=100, bristle='#3b2a30', handle='#4b3a40'):
    """Pennello liner (setole lunghe e sottili): punta in (x, y)."""
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f)"><path d="M0,0 Q10,-3 24,-3 L24,3 Q10,3 0,0 Z" fill="%s"/>'
            '<rect x="24" y="-4" width="10" height="8" fill="#c9ccd1"/>'
            '<rect x="34" y="-3.5" width="%d" height="7" rx="3.5" fill="%s"/></g>' % (x, y, ang, bristle, l, handle))


def dotter(x, y, ang=-90, l=110, r=5):
    """Dotter: sfera in (x, y), manico verso ang."""
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f)"><rect x="0" y="-1.5" width="26" height="3" fill="#8f979f"/>'
            '<rect x="26" y="-5" width="%d" height="10" rx="5" fill="%s"/></g>' % (x, y, ang, l, ACC)
            + '<circle cx="%.1f" cy="%.1f" r="%d" fill="#b5bcc4" stroke="#7d8792"/>' % (x, y, r))


def stick(x, y, ang=0, l=110):
    """Bastoncino d'arancio: punta in (x, y)."""
    return ('<g transform="translate(%.1f,%.1f) rotate(%.1f)"><path d="M0,-2 L18,-6 L%d,-6 L%d,6 L18,6 L0,2 Z" fill="%s" stroke="%s"/></g>'
            % (x, y, ang, l, l, WOOD, WOOD_S))


def file_tool(x, y, ang=0, l=120, w=18):
    return tool_file(x, y, ang, l, w)


# ---------------------------------------------------------------- sezione laterale (punta a destra)
def section(x0, y, L=220, F=60, fold=True, body_h=60, bed=True):
    """Dito in sezione: x0 = punto della cuticola (fine della piega prossimale), y = superficie della lamina,
    L = lunghezza del letto (fino al punto di stress), F = bordo libero naturale. Restituisce (svg_sotto, svg_piega, punti)."""
    xs = x0 + L
    s = ('<path d="M%.1f,%.1f L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
         % (x0 - 70, y + 4, xs - 6, y + 7, xs + 6, y + 8, xs + 30, y + 16, xs + 30, y + body_h * 0.55,
            xs + 30, y + body_h, xs - 10, y + body_h, xs - 30, y + body_h, x0 - 70, y + body_h, SKIN, SKIN_D))
    if bed:
        s += '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s"/>' % (
            x0 - 30, y + 6, xs - 4, y + 6, xs + 4, y + 7, xs, y + 12, x0 - 30, y + 12, BED)
    s += '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.2"/>' % (
        x0 - 40, y, xs + F, y, xs + F + 3, y + 3, xs + F, y + 6, x0 - 40, y + 6, PLATE_SEC, NAIL_S)
    fd = ''
    if fold:
        fd = ('<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s"/>'
              '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="1.5"/>'
              % (x0 - 70, y - 22, x0 - 14, y - 22, x0 + 4, y - 20, x0, y + 0.5, x0 - 70, y + 0.5, SKIN,
                 x0 - 70, y - 22, x0 - 14, y - 22, x0 + 4, y - 20, x0, y + 0.5, SKIN_D))
    return s, fd, dict(x0=x0, y=y, xs=xs, xt=xs + F)


def product(pts, y, end_x=None, end_y=None, fill=PROD, stroke=PROD_S, sw=1.6, extra=''):
    """Strato di prodotto: pts = profilo superiore (da sinistra a destra) sopra la superficie y."""
    d = smooth_d(pts)
    x_end = end_x if end_x is not None else pts[-1][0]
    yb = end_y if end_y is not None else y
    d += ' L%.1f,%.1f L%.1f,%.1f Z' % (x_end, yb, pts[0][0], y)
    return '<path d="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>' % (d, fill, stroke, sw, extra)


def stress_tri(x, y, s=7):
    """Triangolino bordeaux che indica il punto di stress (sotto la lamina)."""
    return '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s"/>' % (x, y, x - s, y + s * 1.5, x + s, y + s * 1.5, ACC2)


# ---------------------------------------------------------------- icone
def ic_calendar(x, y, s=1.0, col=ACC2):
    return scaled(x, y, s, '<rect x="-16" y="-14" width="32" height="30" rx="4" fill="#fff" stroke="%s" stroke-width="2"/>'
                  '<rect x="-16" y="-14" width="32" height="9" rx="3" fill="%s"/>'
                  '<line x1="-9" y1="-18" x2="-9" y2="-10" stroke="%s" stroke-width="2.5" stroke-linecap="round"/>'
                  '<line x1="9" y1="-18" x2="9" y2="-10" stroke="%s" stroke-width="2.5" stroke-linecap="round"/>'
                  '<g fill="%s"><rect x="-10" y="0" width="5" height="4"/><rect x="-2" y="0" width="5" height="4"/><rect x="6" y="0" width="5" height="4"/>'
                  '<rect x="-10" y="7" width="5" height="4"/><rect x="-2" y="7" width="5" height="4"/></g>' % (col, col, col, col, MUTED))


def ic_phone(x, y, s=1.0):
    return scaled(x, y, s, '<rect x="-10" y="-18" width="20" height="36" rx="4" fill="%s"/>'
                  '<rect x="-7.5" y="-13" width="15" height="24" rx="1.5" fill="#dfe9f2"/>'
                  '<circle cx="0" cy="14.5" r="1.8" fill="#fff"/>' % INK)


def ic_drop(x, y, s=1.0, col='#f1d27a', stroke='#c9a54a'):
    return scaled(x, y, s, '<path d="M0,-16 C6,-6 12,0 12,7 A12,12 0 0 1 -12,7 C-12,0 -6,-6 0,-16 Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
                  '<path d="M-5,4 Q-5,10 0,12" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/>' % (col, stroke))


def ic_glove(x, y, s=1.0, col='#7fb3d5'):
    b = '<path d="M-13,18 L-13,-2 Q-17,-6 -14,-10 L-8,-4 L-8,-16 Q-8,-20 -5,-20 Q-2,-20 -2,-16 L-2,-20 Q-2,-24 1,-24 Q4,-24 4,-20 L4,-18 Q4,-21 7,-21 Q10,-21 10,-17 L10,-12 Q10,-15 13,-15 Q16,-15 16,-11 L16,8 Q16,14 12,18 Z" fill="%s" stroke="#4f86a8" stroke-width="1.5" stroke-linejoin="round"/>' % col
    b += '<rect x="-15" y="16" width="33" height="7" rx="2" fill="#4f86a8"/>'
    return scaled(x, y, s, b)


def ic_camera(x, y, s=1.0, col=INK):
    return scaled(x, y, s, '<rect x="-18" y="-10" width="36" height="24" rx="5" fill="%s"/>'
                  '<rect x="-8" y="-15" width="14" height="7" rx="2" fill="%s"/>'
                  '<circle cx="0" cy="2" r="8" fill="#dfe9f2" stroke="#fff" stroke-width="2"/>'
                  '<circle cx="11" cy="-5" r="2" fill="#f1d27a"/>' % (col, col))


def ic_doc(x, y, s=1.0, pen=False, col=ACC2):
    b = ('<path d="M-13,-17 L6,-17 L13,-10 L13,17 L-13,17 Z" fill="#fff" stroke="%s" stroke-width="2" stroke-linejoin="round"/>'
         '<path d="M6,-17 L6,-10 L13,-10" fill="none" stroke="%s" stroke-width="1.6"/>' % (col, col))
    for k in range(4):
        b += '<line x1="-8" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.8"/>' % (-7 + k * 6, 8 if k < 3 else 2, -7 + k * 6, MUTED)
    if pen:
        b += '<g transform="translate(10,8) rotate(40)"><rect x="-2.5" y="-16" width="5" height="18" rx="1.5" fill="%s"/><path d="M-2.5,2 L0,7 L2.5,2 Z" fill="%s"/></g>' % (ACC, INK)
    return scaled(x, y, s, b)


def ic_lens(x, y, s=1.0, col=ACC2):
    return scaled(x, y, s, '<circle cx="-4" cy="-4" r="11" fill="#eef6fb" stroke="%s" stroke-width="3"/>'
                  '<line x1="4" y1="4" x2="15" y2="15" stroke="%s" stroke-width="5" stroke-linecap="round"/>' % (col, col))


def ic_heart(x, y, s=1.0, col=ERR):
    return scaled(x, y, s, '<path d="M0,15 C-18,2 -16,-14 -6,-14 C-2,-14 0,-10 0,-8 C0,-10 2,-14 6,-14 C16,-14 18,2 0,15 Z" fill="%s"/>'
                  '<path d="M-4,-1 L4,-1 M0,-5 L0,3" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/>' % col)


def ic_bubble(x, y, s=1.0, col=ACC):
    return scaled(x, y, s, '<path d="M-17,-13 Q-17,-17 -13,-17 L13,-17 Q17,-17 17,-13 L17,5 Q17,9 13,9 L-2,9 L-10,17 L-9,9 L-13,9 Q-17,9 -17,5 Z" fill="%s"/>'
                  '<circle cx="-7" cy="-4" r="2.2" fill="#fff"/><circle cx="0" cy="-4" r="2.2" fill="#fff"/><circle cx="7" cy="-4" r="2.2" fill="#fff"/>' % col)


def ic_stopwatch(x, y, s=1.0, col=ACC2):
    return scaled(x, y, s, '<circle cx="0" cy="3" r="14" fill="#fff" stroke="%s" stroke-width="2.5"/>'
                  '<rect x="-4" y="-17" width="8" height="5" rx="1.5" fill="%s"/>'
                  '<path d="M0,3 L0,-6 M0,3 L6,6" stroke="%s" stroke-width="2.2" stroke-linecap="round"/>' % (col, col, col))


def ic_sun(x, y, s=1.0):
    b = '<circle cx="0" cy="0" r="9" fill="#f5c542"/>'
    for k in range(8):
        a = math.radians(k * 45)
        b += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#f5c542" stroke-width="3" stroke-linecap="round"/>' % (
            13 * math.cos(a), 13 * math.sin(a), 18 * math.cos(a), 18 * math.sin(a))
    return scaled(x, y, s, b)


def ic_cig(x, y, s=1.0):
    return scaled(x, y, s, '<rect x="-20" y="-3" width="30" height="7" fill="#f4f1ec" stroke="#b9ab98"/>'
                  '<rect x="10" y="-3" width="10" height="7" fill="#e3a35a"/>'
                  '<rect x="-23" y="-3" width="3" height="7" fill="#c0392b"/>'
                  '<path d="M-24,-6 q-4,-6 0,-11 q4,-5 0,-10" stroke="#b5bcc4" stroke-width="2" fill="none"/>')


def ic_bottle(x, y, s=1.0, col='#7fb3d5', cap='#4f86a8', label=''):
    b = ('<rect x="-5" y="-20" width="10" height="7" rx="1.5" fill="%s"/>'
         '<path d="M-9,-13 L9,-13 L11,-7 L11,17 Q11,20 8,20 L-8,20 Q-11,20 -11,17 L-11,-7 Z" fill="%s" stroke="%s" stroke-width="1.2"/>'
         '<rect x="-7" y="-2" width="14" height="10" rx="2" fill="#fff" opacity=".85"/>' % (cap, col, cap))
    return scaled(x, y, s, b)


def ic_brush_dirty(x, y, s=1.0):
    return scaled(x, y, s, brush_flat(-14, 10, -40, 34, '#eadbb8') +
                  '<ellipse cx="-12" cy="9" rx="7" ry="5" fill="#d8b23a" opacity=".85"/>')


def ic_lamp(x, y, s=1.0, q=False):
    b = ('<path d="M-22,10 L-22,-2 Q0,-26 22,-2 L22,10 Z" fill="#f4f1f8" stroke="#8a7d9e" stroke-width="2"/>'
         '<rect x="-25" y="10" width="50" height="5" rx="2.5" fill="#8a7d9e"/>')
    for k in (-8, 0, 8):
        b += '<line x1="%d" y1="-6" x2="%d" y2="8" stroke="#9a6be0" stroke-width="2" opacity=".6" stroke-dasharray="3 3"/>' % (k, k * 1.4)
    if q:
        b += '<circle cx="18" cy="-18" r="9" fill="%s"/>' % WARN + text(18, -13.5, '?', 13, weight=900, fill='#fff')
    return scaled(x, y, s, b)


def ic_can(x, y, s=1.0):
    return scaled(x, y, s, '<rect x="-11" y="-16" width="22" height="32" rx="3" fill="#e46f8f" stroke="%s" stroke-width="1.2"/>'
                  '<ellipse cx="0" cy="-16" rx="11" ry="3" fill="#cfd4da" stroke="%s"/>'
                  '<path d="M-4,-18 q4,-5 8,0" stroke="%s" stroke-width="2" fill="none"/>'
                  '<rect x="-11" y="-4" width="22" height="8" fill="#fff" opacity=".7"/>' % (NAIL_S, GREY_D, GREY_D))


def ic_teeth(x, y, s=1.0):
    b = '<path d="M-18,-6 Q0,-18 18,-6 Q0,14 -18,-6 Z" fill="#e46f8f" stroke="%s" stroke-width="1.5"/>' % NAIL_S
    b += '<path d="M-12,-8 L12,-8 L12,-3 L-12,-3 Z" fill="#fff"/>'
    for k in (-6, 0, 6):
        b += '<line x1="%d" y1="-8" x2="%d" y2="-3" stroke="#e7cfd6" stroke-width="1"/>' % (k, k)
    return scaled(x, y, s, b)


def ic_glue(x, y, s=1.0):
    return scaled(x, y, s, '<path d="M-16,-6 L10,-6 L16,0 L10,6 L-16,6 Q-19,0 -16,-6 Z" fill="#f4f1ec" stroke="#b9ab98" stroke-width="1.4"/>'
                  '<path d="M16,0 L24,0" stroke="%s" stroke-width="3" stroke-linecap="round"/>'
                  '<rect x="-12" y="-3" width="16" height="6" rx="1" fill="%s"/>'
                  '<path d="M26,3 q2,5 0,7 q-2,-2 0,-7 z" fill="#f6e7a8" stroke="#c9a54a" stroke-width=".8"/>' % (GREY_D, ACC))


def ic_plaster(x, y, s=1.0):
    return scaled(x, y, s, '<g transform="rotate(-30)"><rect x="-20" y="-7" width="40" height="14" rx="7" fill="#e8c39e" stroke="#c49a6c" stroke-width="1.2"/>'
                  '<rect x="-7" y="-6" width="14" height="12" fill="#f3dcc3"/>'
                  '<g fill="#c49a6c"><circle cx="-3" cy="-2" r=".9"/><circle cx="3" cy="-2" r=".9"/><circle cx="-3" cy="2" r=".9"/><circle cx="3" cy="2" r=".9"/></g></g>')


def ic_house(x, y, s=1.0, col=ACC2):
    return scaled(x, y, s, '<path d="M-16,-2 L0,-16 L16,-2" fill="none" stroke="%s" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>'
                  '<path d="M-11,-5 L-11,14 L11,14 L11,-5" fill="#fff" stroke="%s" stroke-width="2.5"/>'
                  '<rect x="-4" y="4" width="8" height="10" fill="%s"/>' % (col, col, col))


def ic_map(x, y, s=1.0):
    return scaled(x, y, s, '<path d="M-20,-12 L-7,-16 L7,-12 L20,-16 L20,14 L7,18 L-7,14 L-20,18 Z" fill="#eaf3e6" stroke="%s" stroke-width="1.5"/>'
                  '<path d="M-7,-16 L-7,14 M7,-12 L7,18" stroke="%s" stroke-width="1"/>'
                  '<path d="M3,-10 C-4,-10 -4,-2 3,6 C10,-2 10,-10 3,-10 Z" fill="%s"/><circle cx="3" cy="-5" r="2.3" fill="#fff"/>' % (MUTED, MUTED, ERR))


def ic_flag(x, y, s=1.0):
    return scaled(x, y, s, '<line x1="0" y1="20" x2="0" y2="-20" stroke="%s" stroke-width="3" stroke-linecap="round"/>'
                  '<path d="M0,-20 L22,-14 L0,-6 Z" fill="%s"/>' % (INK, ACC))


def ic_foil_finger(x, y, s=1.0):
    return scaled(x, y, s, '<path d="M-11,18 L-11,-6 Q0,-24 11,-6 L11,18 Z" fill="%s" stroke="%s" stroke-width="1.4"/>'
                  '<path d="M-8,-2 L8,3 M-8,6 L8,11" stroke="#f3f5f7" stroke-width="2"/>' % (FOIL, FOIL_S))


def ic_file(x, y, s=1.0, ang=-35):
    return scaled(x, y, s, rot(ang, 0, 0, '<rect x="-22" y="-5" width="44" height="10" rx="5" fill="#8a7d74"/><rect x="-22" y="0" width="44" height="5" rx="2.5" fill="#d9cfc6"/>'))


def ic_stop(x, y, s=1.0):
    pts = []
    for k in range(8):
        a = math.radians(22.5 + k * 45)
        pts.append((17 * math.cos(a), 17 * math.sin(a)))
    return scaled(x, y, s, poly(pts, ERR, '#fff', 2) + text(0, 4.5, 'STOP', 10.5, weight=900, fill='#fff'))


def ic_thermo(x, y, level, col, s=1.0):
    """Termometro: level 0..1."""
    h = 40
    b = '<rect x="-5" y="-26" width="10" height="%d" rx="5" fill="#fff" stroke="%s" stroke-width="1.6"/>' % (h, GREY_D)
    lh = 6 + (h - 10) * level
    b += '<rect x="-2.5" y="%.1f" width="5" height="%.1f" rx="2" fill="%s"/>' % (12 - lh, lh, col)
    b += '<circle cx="0" cy="17" r="8" fill="%s" stroke="%s" stroke-width="1.6"/>' % (col, GREY_D)
    return scaled(x, y, s, b)


def mini_hand(x, y, s=1.0, marks=(0, 1, 2, 3, 4), col=ERR):
    """Mano stilizzata vista dal dorso (dita verso l'alto); marks = dita con unghia evidenziata (0 = pollice)."""
    b = '<path d="M-30,10 Q-34,48 -10,58 L22,58 Q40,46 36,10 Z" fill="%s" stroke="%s" stroke-width="1.5"/>' % (SKIN, SKIN_D)
    fingers = [(-44, 22, 9, 30, -35), (-21, -6, 8.5, 44, -6), (-3, -14, 8.5, 50, 0), (15, -9, 8.5, 46, 5), (31, 2, 7.5, 34, 12)]
    for i, (fx, fy, fw, fl, ang) in enumerate(fingers):
        fb = ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s" stroke="%s" stroke-width="1.5"/>'
              % (-fw, -fl, 2 * fw, fl + 26, fw, SKIN, SKIN_D))
        nc = col if i in marks else NAIL
        fb += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s" stroke="%s" stroke-width="1"/>' % (
            -fw + 3, -fl + 3, 2 * fw - 6, 13, fw - 3, nc, NAIL_S)
        b += '<g transform="translate(%.1f,%.1f) rotate(%d)">%s</g>' % (fx, fy, ang, fb)
    b += '<path d="M-30,10 Q-34,48 -10,58 L22,58 Q40,46 36,10" fill="%s"/>' % SKIN
    return scaled(x, y, s, b)


# >>> helper C2
# ---------------------------------------------------------------- strumenti e schede "da manuale" (versione rifinita)
SKIN_OP, SKIN_OP_D = '#eebfa5', '#c98e72'   # mano dell'operatrice (tono leggermente diverso dalla cliente)
BERRY = '#9b2c5a'                           # smalto da stamping / decorazioni


def card(x, y, w, h, fill='#fff', stroke='#ead9d4', rx=14, accent=None, ah=6):
    """Scheda bianca con ombra morbida e, se richiesto, banda colorata in alto."""
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%d" fill="%s" stroke="%s" stroke-width="1.2" filter="url(#cSh)"/>' % (
        x, y, w, h, rx, fill, stroke)
    if accent:
        c = uid('cc')
        s += '<clipPath id="%s"><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%d"/></clipPath>' % (c, x, y, w, h, rx)
        s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" clip-path="url(#%s)"/>' % (x, y, w, ah, accent, c)
    return s


def pill(x, y, w, h, label, fill, col, size=13.5, weight=800, stroke=None):
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s"%s/>' % (
        x, y, w, h, h / 2, fill, (' stroke="%s" stroke-width="1.4"' % stroke) if stroke else '')
    return s + text(x + w / 2, y + h / 2 + size * 0.36, label, size, weight=weight, fill=col)


def badge(x, y, n, col=ACC2, r=15, size=15):
    return ('<circle cx="%.1f" cy="%.1f" r="%d" fill="%s" stroke="#fff" stroke-width="2.5" filter="url(#nxShS)"/>' % (x, y, r, col)
            + text(x, y + size * 0.36, str(n), size, weight=800, fill='#fff'))


def capsule(x1, y1, x2, y2, w, fill=SKIN_OP, stroke=SKIN_OP_D):
    """Dito stilizzato: segmento a estremità arrotondate con contorno."""
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.1f" stroke-linecap="round"/>'
            '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.1f" stroke-linecap="round"/>'
            % (x1, y1, x2, y2, stroke, w + 3, x1, y1, x2, y2, fill, w))


def liner(x, y, ang=0, l=96, bristle='#3b2a30', handle='#2f2a2e', load=None):
    """Pennello liner realistico: punta delle setole in (x, y), manico verso ang (gradi).
    Setole affusolate, ghiera metallica con crimpatura, manico sagomato con riflesso."""
    g = '<path d="M0,0 C7,-0.8 17,-3 30,-3.4 L30,3.4 C17,3 7,0.8 0,0 Z" fill="%s"/>' % bristle
    if load:
        g += '<path d="M0,0 C4,-0.6 9,-1.8 13,-2.2 L13,2.2 C9,1.8 4,0.6 0,0 Z" fill="%s"/>' % load
    g += '<path d="M6,-0.6 C14,-1.6 22,-2.4 29,-2.4" stroke="#fff" stroke-width=".8" fill="none" opacity=".35"/>'
    g += '<rect x="29" y="-4.2" width="15" height="8.4" rx="1.5" fill="#9aa3ad"/>'
    g += '<line x1="33" y1="-4.2" x2="33" y2="4.2" stroke="#6f7983" stroke-width=".9"/><line x1="36" y1="-4.2" x2="36" y2="4.2" stroke="#6f7983" stroke-width=".9"/>'
    g += ('<path d="M44,-4.4 C%.1f,-5.8 %.1f,-5.2 %.1f,-3.4 Q%.1f,0 %.1f,3.4 C%.1f,5.2 %.1f,5.8 44,4.4 Z" fill="%s"/>'
          % (44 + l * 0.3, 44 + l * 0.75, 44 + l, 44 + l + 4, 44 + l, 44 + l * 0.75, 44 + l * 0.3, handle))
    g += '<path d="M48,-2.6 C%.1f,-3.8 %.1f,-3.4 %.1f,-2.2" stroke="#fff" stroke-width="1.3" fill="none" opacity=".28" stroke-linecap="round"/>' % (
        44 + l * 0.3, 44 + l * 0.7, 44 + l - 6)
    return '<g transform="translate(%.1f,%.1f) rotate(%.1f)">%s</g>' % (x, y, ang, g)


def flat_brush(x, y, ang=0, l=80, bristle='#eadbb8', handle='#2f2a2e', load=None, w=7):
    """Pennello piatto/sfumatore: bordo delle setole in (x, y)."""
    g = '<path d="M0,-%.1f Q-1,0 0,%.1f L16,%.1f L16,-%.1f Z" fill="%s" stroke="#bfa979" stroke-width=".8"/>' % (w, w, w - 1, w - 1, bristle)
    if load:
        g += '<path d="M0,-%.1f Q-1,0 0,%.1f L5,%.1f L5,-%.1f Z" fill="%s"/>' % (w, w, w - 0.5, w - 0.5, load)
    for k in (-0.5, 0, 0.5):
        g += '<line x1="2" y1="%.1f" x2="15" y2="%.1f" stroke="#fff" stroke-width=".6" opacity=".45"/>' % (k * w, k * (w - 1))
    g += '<path d="M16,-%.1f L30,-5 L30,5 L16,%.1f Z" fill="#9aa3ad"/>' % (w - 1, w - 1)
    g += '<line x1="22" y1="-5.6" x2="22" y2="5.6" stroke="#6f7983" stroke-width=".9"/>'
    g += ('<path d="M30,-5 C%.1f,-6 %.1f,-5 %.1f,-3.4 Q%.1f,0 %.1f,3.4 C%.1f,5 %.1f,6 30,5 Z" fill="%s"/>'
          % (30 + l * 0.3, 30 + l * 0.75, 30 + l, 30 + l + 4, 30 + l, 30 + l * 0.75, 30 + l * 0.3, handle))
    g += '<path d="M34,-3 C%.1f,-4 %.1f,-3.6 %.1f,-2.4" stroke="#fff" stroke-width="1.3" fill="none" opacity=".28" stroke-linecap="round"/>' % (
        30 + l * 0.3, 30 + l * 0.7, 30 + l - 6)
    return '<g transform="translate(%.1f,%.1f) rotate(%.1f)">%s</g>' % (x, y, ang, g)


def dotter2(x, y, ang=-90, l=74, r=4.5, handle=ACC):
    """Dotter: sfera metallica in (x, y), stelo sottile, manico con anelli di presa."""
    g = '<rect x="0" y="-1.3" width="24" height="2.6" fill="#9aa3ad"/>'
    g += '<path d="M24,-2 L32,-4.5 L32,4.5 L24,2 Z" fill="#9aa3ad"/>'
    g += '<rect x="32" y="-4.8" width="%d" height="9.6" rx="4.8" fill="%s"/>' % (l, handle)
    for k in range(4):
        g += '<line x1="%.1f" y1="-4.6" x2="%.1f" y2="4.6" stroke="#fff" stroke-width="1" opacity=".35"/>' % (38 + k * 4, 38 + k * 4)
    g += '<path d="M%.1f,-2.6 L%.1f,-2.6" stroke="#fff" stroke-width="1.3" opacity=".3" stroke-linecap="round"/>' % (56, 28 + l)
    s = '<g transform="translate(%.1f,%.1f) rotate(%.1f)">%s</g>' % (x, y, ang, g)
    s += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#9aa3ad" stroke="#6f7983" stroke-width=".8"/>' % (x, y, r)
    s += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#fff" opacity=".7"/>' % (x - r * 0.35, y - r * 0.35, r * 0.3)
    return s


def file_board(x, y, ang=0, l=110, w=16, grit='#8a7d74', core='#f2ede7'):
    """Lima professionale: anima chiara, due facce abrasive con grana puntinata e punte arrotondate."""
    rng = random.Random(int(l * 7 + w))
    g = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s"/>' % (-l / 2, -w / 2, l, w, w / 2, grit)
    g += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1" fill="%s"/>' % (-l / 2 + 2, -1.2, l - 4, 2.4, core)
    for _ in range(int(l / 2.2)):
        g += '<circle cx="%.1f" cy="%.1f" r=".7" fill="#fff" opacity=".35"/>' % (rng.uniform(-l / 2 + 4, l / 2 - 4), rng.choice([-1, 1]) * rng.uniform(2.5, w / 2 - 1.5))
    return '<g transform="translate(%.1f,%.1f) rotate(%.1f)" filter="url(#nxShS)">%s</g>' % (x, y, ang, g)


def polish_bottle(x, y, s=1.0, col=FUCHSIA, cap='#2f2a2e'):
    """Boccetta di smalto vetro + tappo; (x, y) = centro della base."""
    b = '<rect x="-7" y="-58" width="14" height="24" rx="3" fill="%s"/>' % cap
    b += '<rect x="-5" y="-56" width="2.5" height="19" rx="1.2" fill="#fff" opacity=".25"/>'
    b += '<rect x="-9" y="-36" width="18" height="6" rx="1.5" fill="#d9dde2" stroke="#9aa3ad" stroke-width=".8"/>'
    b += '<path d="M-17,-30 L17,-30 Q21,-30 21,-25 L21,-4 Q21,0 17,0 L-17,0 Q-21,0 -21,-4 L-21,-25 Q-21,-30 -17,-30 Z" fill="%s" stroke="#fff" stroke-width="1"/>' % col
    b += '<path d="M-21,-12 L21,-12 L21,-4 Q21,0 17,0 L-17,0 Q-21,0 -21,-4 Z" fill="#000" opacity=".1"/>'
    b += '<rect x="-16" y="-26" width="4" height="20" rx="2" fill="#fff" opacity=".55"/>'
    return scaled(x, y, s, b)


def flower(cx, cy, r=6, col=BERRY, w=1.6, fill='none'):
    """Fiore a cinque petali (decoro da piastra / stamping)."""
    s = ''
    for k in range(5):
        a = math.radians(-90 + k * 72)
        s += '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s" stroke="%s" stroke-width="%s" transform="rotate(%.1f %.1f %.1f)"/>' % (
            cx + r * 0.62 * math.cos(a), cy + r * 0.62 * math.sin(a), r * 0.42, r * 0.28, fill, col, w,
            k * 72, cx + r * 0.62 * math.cos(a), cy + r * 0.62 * math.sin(a))
    s += '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>' % (cx, cy, r * 0.2, col)
    return s


def flower_pattern(cx, cy, col=BERRY, sc=1.0, w=1.5):
    s = ''
    for dx, dy, r in ((-12, -14, 8), (10, -4, 9), (-8, 14, 7.5), (14, 20, 5.5), (-18, 2, 4.5)):
        s += flower(cx + dx * sc, cy + dy * sc, r * sc, col, w)
    return s


def no_sign(x, y, r=19, w=3):
    """Divieto: cerchio rosso con barra obliqua (da sovrapporre a un'icona)."""
    d = r * 0.7071
    return ('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" stroke-width="%s"/>'
            '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s" stroke-linecap="round"/>'
            % (x, y, r, ERR, w, x - d, y - d, x + d, y + d, ERR, w))


def ic_foil2(x, y, s=1.0):
    """Polpastrello avvolto nella stagnola (soak-off)."""
    b = '<path d="M-13,20 L-13,-4 Q-13,-20 0,-20 Q13,-20 13,-4 L13,20 Z" fill="#d9dde2" stroke="#8d969f" stroke-width="1.3"/>'
    b += '<path d="M-13,6 L-6,2 L-1,8 L6,3 L13,7" fill="none" stroke="#a9b1b9" stroke-width="1.1"/>'
    b += '<path d="M-12,-6 L-4,-9 L3,-4 L12,-8" fill="none" stroke="#a9b1b9" stroke-width="1.1"/>'
    b += '<path d="M-8,-12 Q-9,0 -7,14" stroke="#fff" stroke-width="2.5" fill="none" opacity=".8" stroke-linecap="round"/>'
    b += '<rect x="-14" y="18" width="28" height="7" rx="2" fill="%s" stroke="%s" stroke-width="1"/>' % (SKIN, SKIN_D)
    return scaled(x, y, s, b)


def ic_clock(x, y, s=1.0, col=ACC2):
    b = '<circle cx="0" cy="0" r="9" fill="#fff" stroke="%s" stroke-width="2"/>' % col
    b += '<path d="M0,0 L0,-5.5 M0,0 L4,2.5" stroke="%s" stroke-width="1.8" stroke-linecap="round"/>' % col
    return scaled(x, y, s, b)


def phone_frame(x, y, w, h, inner, land=True):
    """Telefono (vista frontale) con contenuto 'inner' ritagliato nello schermo, griglia dei terzi e messa a fuoco."""
    c = uid('ph')
    sx, sy, sw, sh = x + 10, y + 10, w - 20, h - 20
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="18" fill="#2f2a2e" filter="url(#nxShS)"/>' % (x, y, w, h)
    s += '<clipPath id="%s"><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="9"/></clipPath>' % (c, sx, sy, sw, sh)
    s += '<g clip-path="url(#%s)"><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#f4f1ee"/>%s' % (c, sx, sy, sw, sh, inner)
    for k in (1, 2):
        s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#fff" stroke-width="1" opacity=".75"/>' % (sx + sw * k / 3, sy, sx + sw * k / 3, sy + sh)
        s += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#fff" stroke-width="1" opacity=".75"/>' % (sx, sy + sh * k / 3, sx + sw, sy + sh * k / 3)
    s += '</g>'
    if land:
        s += '<circle cx="%.1f" cy="%.1f" r="3" fill="#4a4448"/>' % (x + 5, y + h / 2)
    return s


def focus_box(cx, cy, r=16, col='#f5c542'):
    s = ''
    for sx in (-1, 1):
        for sy in (-1, 1):
            s += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f" fill="none" stroke="%s" stroke-width="2"/>' % (
                cx + sx * r, cy + sy * (r - 6), cx + sx * r, cy + sy * r, cx + sx * (r - 6), cy + sy * r, col)
    return s


def chevron(x, y, w, h, fill, first=False, tip=14):
    d = 'M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f' % (x, y, x + w - tip, y, x + w, y + h / 2, x + w - tip, y + h, x, y + h)
    d += ' Z' if first else ' L%.1f,%.1f Z' % (x + tip, y + h / 2)
    return '<path d="%s" fill="%s"/>' % (d, fill)


def finger_side(x, y, L=170, col=FUCHSIA, h=34, nail_from=0.55, skin=SKIN, skin_d=SKIN_D):
    """Dito della cliente di profilo appoggiato sul piano y (punta a destra) con unghia smaltata sopra."""
    xe = x + L
    s = ('<path d="M%.1f,%.1f L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
         % (x, y, x, y - h, xe - 40, y - h - 4, xe - 4, y - h + 2, xe, y - h * 0.45, xe + 3, y - 6, xe - 10, y, xe - 30, y, skin, skin_d))
    nx0 = x + L * nail_from
    s += ('<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f L%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1"/>'
          % (nx0, y - h - 1, nx0 + 30, y - h - 7, xe - 14, y - h - 6, xe + 6, y - h + 6, xe + 4, y - h + 9,
             xe - 14, y - h - 1, nx0 + 30, y - h - 2, nx0, y - h + 3, col, NAIL_S))
    s += '<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f" stroke="#fff" stroke-width="1.6" fill="none" opacity=".6" stroke-linecap="round"/>' % (
        nx0 + 10, y - h - 3, nx0 + 30, y - h - 6, xe - 30, y - h - 6, xe - 16, y - h - 4)
    return s, dict(nx0=nx0, xe=xe, top=y - h - 5)
# <<< helper C2


# ================================================================= MODULO 9 – DECORAZIONI
CUT_COL = '#b98a6e'   # arco della cuticola evidenziato


def cut_arc(cx, yc, hw, col=CUT_COL, w=2.6):
    return ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="%s"/>'
            % (cx - hw - 4, yc - 28, cx, yc + 22, cx + hw + 4, yc - 28, col, w))


@figx('smile-line-profondita.svg')
def smile_depth():
    b = title('Quanto è profonda la smile line?')
    cases = [('Piatta', False, 4, 'unghia più larga'), ('Corretta', True, 25, 'ripete la cuticola'),
             ('Troppo profonda', False, 62, 'innaturale')]
    for i, (t, ok, d, sub) in enumerate(cases):
        x = 20 + i * 245
        cx, yc, hw = x + 112, 268, 40
        ys = yc - 110
        f, p = nail(cx, yc, hw=hw, nail_len=110, free_len=58, shape='ovale', extra=tip_fill(cx, ys, hw, d, ys - 58), finger_len=30)
        body = f + cut_arc(cx, yc, hw)
        yl = smile_lat(ys, d)
        body += dashed(cx - hw - 16, yl, cx + hw + 16, yl, ACC2, 1.5)
        body += dot(cx - hw + 1, yl) + dot(cx + hw - 1, yl)
        if ok:
            # due archi "gemelli": stessa profondità sulla smile e sulla cuticola
            ycl = yc - 28
            body += arr(cx + hw + 20, yl, cx + hw + 20, ys, ACC2, 1.5, True) + text(cx + hw + 27, (yl + ys) / 2 + 5, 'd', 14, 'start', 800, ACC2)
            body += arr(cx + hw + 20, ycl, cx + hw + 20, yc - 3, ACC2, 1.5, True) + text(cx + hw + 27, (ycl + yc - 3) / 2 + 5, 'd', 14, 'start', 800, ACC2)
        b += frame(x, 55, 225, 290, t, ok=ok, body=body, cap=sub, capcol=OK if ok else ERR)
    return svg(760, 360, defs() + b, 'Smile line piatta, corretta (ripete la curva della cuticola) e troppo profonda')


@figx('french-punti-guida.svg')
def french_dots():
    b = title('French dipinto: metodo dei punti guida')
    heads = ['Punto centrale', 'Punti laterali', 'Collega', 'Riempi e sigilla']
    caps = ['centro della curva', 'alla stessa altezza', 'lato → centro', 'anche il bordo libero']
    BASE = '#f6cbd6'
    for i in range(4):
        x = 20 + i * 218
        cx, yc, hw, d = x + 103, 278, 38, 24
        ys = yc - 108
        yl = smile_lat(ys, d)
        top = ys - 56
        pts = smile_pts(cx, ys, hw, d, 24, 0)
        extra = tip_fill(cx, ys, hw, d, top) if i == 3 else ''
        f, p = nail(cx, yc, hw=hw, nail_len=108, free_len=56, plate=BASE, free=BASE, extra=extra, finger_len=30)
        body = f
        # linea guida tratteggiata della smile line (dove andrà il bianco)
        if i < 3:
            body += '<path d="%s" fill="none" stroke="%s" stroke-width="1.2" stroke-dasharray="3 4" opacity=".55"/>' % (smooth_d(pts), ACC2)
        if i == 0:
            body += dot(cx, ys, 5.5, '#fff', NAIL_S)
            body += liner(cx + 3, ys + 3, 42, 64, load='#ffffff')
        elif i == 1:
            body += dot(cx, ys, 4, '#fff', NAIL_S)
            body += dashed(cx - hw - 16, yl, cx + hw + 16, yl, ACC2, 1.6)
            body += dot(cx - hw + 2, yl, 5.5, '#fff', NAIL_S) + dot(cx + hw - 2, yl, 5.5, '#fff', NAIL_S)
            body += liner(cx + hw + 1, yl + 3, 48, 52, load='#ffffff')
        elif i == 2:
            left, right = pts[:13], pts[12:]
            part = right[::-1][:8]
            for seg in (left, part):
                body += '<path d="%s" fill="none" stroke="%s" stroke-width="7" stroke-linecap="round" opacity=".35"/>' % (smooth_d(seg), WHITE_S)
                body += '<path d="%s" fill="none" stroke="#fff" stroke-width="5.5" stroke-linecap="round"/>' % smooth_d(seg)
            body += dot(cx, ys, 3.5, '#fff', NAIL_S)
            ex, ey = part[-1]
            body += liner(ex + 2, ey + 3, 50, 56, load='#ffffff')
            off = [(px, py + 18) for px, py in pts]
            body += carr(smooth_d(off[1:11]), DARK, 1.8) + carr(smooth_d(off[23:13:-1]), DARK, 1.8)
        else:
            body += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="#fff" stroke-width="4" stroke-linecap="round"/>' % (cx - hw + 6, top + 1.5, cx + hw - 6, top + 1.5)
            body += carr('M%.1f,%.1f L%.1f,%.1f' % (cx - 26, top - 8, cx + 26, top - 8), DARK, 1.8)
            body += flat_brush(cx + hw - 4, top + 26, 38, 52, '#f4f1ec', load='#ffffff', w=6)
        b += frame(x, 55, 205, 290, heads[i], num=i + 1, body=body, cap=caps[i], capcol=INK)
    return svg(900, 355, defs() + b, 'French dipinto con il metodo dei punti guida in quattro passaggi')


def bb_grad(gid, stops):
    s = '<linearGradient id="%s" x1="0" y1="1" x2="0" y2="0">' % gid
    for off, col, op in stops:
        s += '<stop offset="%s" stop-color="%s" stop-opacity="%s"/>' % (off, col, op)
    return s + '</linearGradient>'


BB_BASE = '#f6c9d4'


@figx('baby-boomer-step.svg')
def bboom_steps():
    g1, g2 = uid('bb'), uid('bb')
    gdefs = '<defs>%s%s</defs>' % (
        bb_grad(g1, [(0, '#ffffff', 0), (.38, '#ffffff', 0), (.72, '#ffffff', .92), (1, '#ffffff', 1)]),
        bb_grad(g2, [(0, '#f4a9be', .45), (.6, '#f4a9be', .18), (1, '#f4a9be', .08)]))
    b = title('Baby boomer in gel')
    heads = ['Bianco sulla punta', 'Sfuma verso il centro', 'Cover sopra + apex', 'Top: niente linee']
    caps = ['strato sottile', 'colpi brevi, fino a metà', 'il bianco "affiora"', 'sfumatura morbida']
    BBB = '#f1bccb'   # base rosa nude, abbastanza scura da far leggere il bianco
    for i in range(4):
        x = 20 + i * 218
        cx, yc, hw = x + 103, 280, 37
        nl, fl = 112, 66
        ys = yc - nl
        top = ys - fl
        if i == 0:
            yw = ys - 14
            extra = '<rect x="%.1f" y="%.1f" width="120" height="%.1f" fill="#ffffff" clip-path="url(#CLIP)"/>' % (cx - 60, top - 10, yw - top + 10)
            extra += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.2" clip-path="url(#CLIP)"/>' % (cx - 60, yw, cx + 60, yw, WHITE_S)
        else:
            extra = '<rect x="%.1f" y="%.1f" width="120" height="%.1f" fill="url(#%s)" clip-path="url(#CLIP)"/>' % (cx - 60, top - 2, yc - top, g1)
        if i >= 2:
            extra += '<rect x="%.1f" y="%.1f" width="120" height="%.1f" fill="url(#%s)" clip-path="url(#CLIP)"/>' % (cx - 60, top - 10, yc - top + 20, g2)
        f, p = nail(cx, yc, hw=hw, nail_len=nl, free_len=fl, shape='mandorla', plate=BBB, free=BBB, extra=extra, finger_len=26)
        body = f
        if i == 0:
            body += flat_brush(cx + 24, ys - 26, 40, 56, '#f4f1ec', load='#ffffff', w=6)
        elif i == 1:
            body += flat_brush(cx + 26, ys + 6, 44, 52, '#f4f1ec', w=6)
            # colpi brevi dal bianco della punta verso il centro dell'unghia, fermandosi a metà
            ym = (top + yc) / 2 + 6
            body += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.4" stroke-dasharray="4 3"/>' % (
                cx - hw + 2, ym, cx + hw - 2, ym, DARK)
            for dx in (-20, -2, 16):
                body += arr(cx + dx - 6, ys - 30, cx + dx - 6, ym - 4, DARK, 1.8)
        elif i == 2:
            ox, oy = x + 116, 280
            mini = box(ox - 10, oy - 36, 92, 52, '#fff', '#d8c8c4', 8)
            mini += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="3" stroke-linecap="round"/>' % (ox, oy + 6, ox + 72, oy + 6, NAIL_S)
            mini += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="#f6b8c9" stroke="%s" stroke-width="1.2"/>' % (
                ox + 2, oy + 5, ox + 20, oy - 14, ox + 36, oy - 14, ox + 54, oy - 14, ox + 72, oy + 2, ox + 72, oy + 6, NAIL_S)
            mini += arr(ox + 36, oy - 30, ox + 36, oy - 17, ACC2, 1.4)
            body += mini + text(ox - 2, oy - 22, 'apex', 12.5, 'start', 800, ACC2)
        elif i == 3:
            body += gloss(cx + 4, top + 30, ys + 40, 4) + sparkle(cx + 14, top + 34, 6)
        b += frame(x, 55, 205, 292, heads[i], num=i + 1, body=body, cap=caps[i], capcol=INK, hsize=14.5)
    return svg(900, 357, defs() + gdefs + b, 'Baby boomer in gel in quattro passaggi: bianco, sfumatura, cover con apex, top')


@figx('sfumatura-errori.svg')
def bboom_errors():
    gdefs = '<defs>%s%s</defs>' % (
        bb_grad('sfg', [(0, '#ffffff', 0), (.4, '#ffffff', 0), (.8, '#fdf8f9', 1), (1, '#ffffff', 1)]),
        '<linearGradient id="sfp" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="%s"/><stop offset=".55" stop-color="%s"/><stop offset="1" stop-color="#ffffff"/></linearGradient>' % ('#f1bccb', '#f1bccb'))
    b = title('Sfumatura: giusta o sbagliata?')
    cases = [('Graduale', True, 'passaggio morbido'), ('Si vede la linea', False, 'bianco poco sfumato'),
             ('Troppo bianco', False, 'french sbavato'), ('Gobba sulla punta', False, 'strati spessi sovrapposti')]
    for i, (t, ok, sub) in enumerate(cases):
        x = 20 + i * 218
        cx, yc, hw = x + 103, 255, 38
        nl, fl = 104, 60
        ys, top = yc - nl, yc - nl - fl
        body = ''
        if i < 3:
            if i == 0:
                extra = '<rect x="%.1f" y="%.1f" width="120" height="%.1f" fill="url(#sfg)" clip-path="url(#CLIP)"/>' % (cx - 60, top - 2, yc - top)
            elif i == 1:
                ym = ys - 10
                extra = '<rect x="%.1f" y="%.1f" width="120" height="%.1f" fill="#ffffff" clip-path="url(#CLIP)"/>' % (cx - 60, top - 20, ym - top + 20)
                extra += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.2" clip-path="url(#CLIP)"/>' % (cx - 60, ym, cx + 60, ym, WHITE_S)
            else:
                pts = [(cx - 60, top - 20), (cx + 60, top - 20)]
                rng = random.Random(4)
                wav = [(cx + 60 - k * 8, yc - 52 + rng.uniform(-9, 9)) for k in range(16)]
                extra = '<path d="M%.1f,%.1f L%.1f,%.1f %s Z" fill="#fefcfc" clip-path="url(#CLIP)"/>' % (
                    pts[0][0], pts[0][1], pts[1][0], pts[1][1], ' '.join('L%.1f,%.1f' % q for q in wav))
                extra += '<path d="M%s" fill="none" stroke="#e9d9dd" stroke-width="2" clip-path="url(#CLIP)"/>' % ' L'.join('%.1f,%.1f' % q for q in wav)
            f, p = nail(cx, yc, hw=hw, nail_len=nl, free_len=fl, shape='mandorla', plate='#f1bccb', free='#f1bccb', extra=extra, finger_len=30)
            body += f
        else:
            sec, fd, pp = section(x + 40, 190, L=100, F=40, body_h=55)
            pts = [(x + 44, 189), (x + 70, 182), (x + 105, 177), (x + 135, 177), (x + 152, 170), (x + 166, 162), (x + 178, 166), (x + 185, 180)]
            body += sec + product(pts, 190, end_x=x + 184, end_y=196, fill='url(#sfp)', stroke=NAIL_S) + fd
            body += '<circle cx="%.1f" cy="%.1f" r="22" fill="none" stroke="%s" stroke-width="2.2" stroke-dasharray="4 3"/>' % (x + 166, 170, ERR)
            body += '<path d="%s" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="5 4"/>' % (smooth_d([(x + 60, 186), (x + 100, 179), (x + 140, 180), (x + 186, 191)]), OK)
            body += text(x + 103, 140, '- - - profilo giusto', 12.5, weight=700, fill=OK)
            body += text(x + 103, 120, 'vista di profilo', 13, fill=MUTED, style='italic')
        b += frame(x, 55, 205, 260, t, ok=ok, body=body, cap=sub, capcol=OK if ok else ERR, hsize=14.5)
    return svg(900, 330, defs() + gdefs + b, 'Sfumatura del baby boomer: corretta e tre errori tipici')


@figx('incapsulato-sezione.svg')
def encaps():
    b = title('Incapsulato: com\'è fatto dentro')
    b += text(20, 62, 'Sezione laterale ingrandita (spessori esagerati per chiarezza)', 13, 'start', fill=MUTED, style='italic')
    y = 222            # superficie della lamina
    xa, xs, xe = 92, 360, 452   # cuticola, punto di stress, fine del prodotto
    # dito
    b += ('<path d="M20,%d L%d,%d C%d,%d %d,%d %d,%d L20,%d Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
          % (y + 10, xs - 10, y + 12, xs + 60, y + 14, xs + 60, y + 78, xs - 20, y + 80, y + 80, SKIN, SKIN_D))
    b += '<rect x="40" y="%d" width="%d" height="5" fill="%s"/>' % (y + 11, xs - 44, BED)
    # lamina
    b += '<path d="M40,%d L%d,%d Q%d,%d %d,%d L40,%d Z" fill="%s" stroke="%s" stroke-width="1.2"/>' % (
        y, xs + 70, y, xs + 76, y + 5, xs + 70, y + 11, y + 11, PLATE_SEC, NAIL_S)
    # base
    base = [(xa + 8, y), (xa + 40, y - 8), (xs + 74, y - 8)]
    b += product(base, y, end_x=xs + 78, end_y=y + 6, fill='#d3e8f4', stroke=PROD_S)
    yb = y - 8
    # prodotto trasparente con apex sopra il punto di stress
    clear = [(xa + 12, yb), (xa + 60, yb - 22), (xa + 150, yb - 46), (xs - 6, yb - 56), (xs + 50, yb - 46), (xe - 18, yb - 22), (xe, yb + 2)]
    b += product(clear, yb, end_x=xe, end_y=y + 8, fill='#eef7fc', stroke=PROD_S)
    # decorazione piatta appoggiata sulla base
    for gx in (xa + 70, xa + 98, xa + 160, xa + 188, xa + 214, xs + 22):
        b += '<path d="M%.1f,%.1f l8,-5 l8,5 l-8,5 Z" fill="%s" stroke="%s" stroke-width="1"/>' % (gx, yb - 5, GOLD, GOLD_S)
    fxc = xa + 132
    b += '<ellipse cx="%.1f" cy="%.1f" rx="17" ry="4" fill="#f7a8c4" stroke="%s"/>' % (fxc, yb - 4, ACC)
    b += '<ellipse cx="%.1f" cy="%.1f" rx="5" ry="2.4" fill="%s"/>' % (fxc, yb - 4, GOLD)
    # top
    topl = [(px, py - 4) for px, py in clear]
    b += '<path d="%s" fill="none" stroke="#5f9cc0" stroke-width="4" stroke-linecap="round"/>' % smooth_d(topl)
    b += '<path d="%s" fill="none" stroke="#fff" stroke-width="1.6" opacity=".95"/>' % smooth_d([(px, py - 4) for px, py in clear[1:5]])
    # piega prossimale
    b += ('<path d="M20,%d L%d,%d Q%d,%d %d,%d L20,%d Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
          % (y - 26, xa - 16, y - 26, xa + 2, y - 22, xa, y, y, SKIN, SKIN_D))
    # punto di stress e apex
    b += stress_tri(xs, y + 13)
    b += text(xs + 14, y + 30, 'punto di stress', 12.5, 'start', 700, ACC2)
    ax, ay = xs - 6, yb - 62
    b += arr(ax, ay - 36, ax, ay - 2, ACC2, 2.2)
    # richiami: sopra (prodotto, apex, top) e sotto (decorazione, base)
    b += ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="122" stroke="%s" stroke-width="1.3"/><circle cx="%.1f" cy="%.1f" r="3.5" fill="%s"/>'
          % (xa + 64, yb - 18, xa + 30, MUTED, xa + 64, yb - 18, ACC2)) + text(xa + 30, 114, 'Prodotto trasparente', 14, weight=600)
    b += text(ax, ay - 44, 'Apex sopra la decorazione', 14, weight=700, fill=ACC2)
    b += leader(xe - 30, yb - 24, 510, 146, 'Top lucido', 'start')
    b += leader(fxc - 34, yb - 5, 150, 330, 'Decorazione piatta', 'middle')
    b += leader(xs + 50, y - 4, 400, 330, 'Base / builder sottile', 'middle')
    # riquadro errore
    bx, by = 520, 262
    eb = box(bx, by, 220, 104, RED_BG, '#efc4bd', 12)
    ex0, ey = bx + 26, by + 64
    eb += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="5" stroke-linecap="round"/>' % (ex0, ey + 3, ex0 + 170, ey + 3, PLATE_SEC)
    eb += product([(ex0, ey), (ex0 + 50, ey - 10), (ex0 + 100, ey - 12), (ex0 + 170, ey - 6)], ey, fill='#eef7fc')
    eb += '<path d="M%.1f,%.1f l10,-12 l14,2 l6,8 Z" fill="%s" stroke="%s"/>' % (ex0 + 82, ey - 6, GOLD, GOLD_S)
    eb += '<circle cx="%.1f" cy="%.1f" r="15" fill="none" stroke="%s" stroke-width="2"/>' % (ex0 + 97, ey - 12, ERR)
    eb += mark(bx + 196, by + 24, False, 12) + text(bx + 16, by + 29, 'Bordo scoperto', 15, 'start', 800, ERR)
    b += eb
    return svg(760, 380, defs() + b, 'Sezione di un incapsulato: base, decorazione piatta, prodotto trasparente con apex sopra, top; errore: bordo scoperto')


@figx('dotting-striping-presa.svg')
def grip():
    b = title('Presa corretta')
    tb, ey = 236, 290

    def client(x, col=FUCHSIA):
        """Piano di lavoro + dito della cliente di profilo (punta verso destra) con unghia smaltata."""
        s = '<rect x="%d" y="%d" width="350" height="8" fill="#d9cfc6"/>' % (x, tb)
        s += '<rect x="%d" y="%d" width="350" height="2.5" fill="#efe7e0"/>' % (x, tb)
        s += ('<path d="M%d,%d L%d,%d C%d,%d %d,%d %d,%d C%d,%d %d,%d %d,%d Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
              % (x - 2, tb, x - 2, tb - 34, x + 120, tb - 40, x + 176, tb - 38, x + 188, tb - 20, x + 192, tb - 6, x + 180, tb, x + 160, tb, SKIN, SKIN_D))
        s += ('<path d="M%d,%d C%d,%d %d,%d %d,%d L%d,%d C%d,%d %d,%d %d,%d Z" fill="%s" stroke="%s" stroke-width="1"/>'
              % (x + 104, tb - 38, x + 130, tb - 47, x + 172, tb - 47, x + 194, tb - 31, x + 194, tb - 26, x + 172, tb - 39, x + 130, tb - 41, x + 106, tb - 33, col, NAIL_S))
        s += '<path d="M%d,%d C%d,%d %d,%d %d,%d" stroke="#fff" stroke-width="1.6" fill="none" opacity=".6" stroke-linecap="round"/>' % (
            x + 118, tb - 42, x + 138, tb - 46, x + 160, tb - 46, x + 174, tb - 42)
        return s

    def hand(gx, gy, ang, pinky, sc=0.62):
        """Mano dell'operatrice vista dal lato del pollice che impugna lo strumento a penna.
        Sistema locale: asse dello strumento lungo +x a partire dal punto di presa (gx, gy), dorso verso -y.
        Restituisce (dietro, davanti): ciò che sta dietro lo strumento e le dita che lo coprono.
        Il mignolo resta disteso fino al piano (pinky = punto d'appoggio, in coordinate assolute)."""
        D, B = gen_svg._digit, gen_svg._blob
        HC, HD, HS = SKIN_OP, '#e2ad93', SKIN_OP_D
        rad = math.radians(ang)
        ca, sa = math.cos(rad), math.sin(rad)

        def T(pts):
            return [(gx + (px * ca - py * sa) * sc, gy + (px * sa + py * ca) * sc) for px, py in pts]

        def W(ws):
            return [w * sc for w in ws]
        back = ''
        # mignolo disteso fino al tavolo
        base = T([(150, 44)])[0]
        mid = ((base[0] + pinky[0]) / 2 + 6, (base[1] + pinky[1]) / 2 - 4)
        back += D([base, mid, (pinky[0] - 4, pinky[1] - 6)], W([15, 13, 11.5]), nail=0, fill=HD, stroke=HS, creases=(1,))
        # anulare ripiegato, medio sotto lo strumento
        back += D(T([(126, 30), (100, 50), (86, 66), (92, 78)]), W([16, 15, 13.5, 12]), nail=0, fill=HD, stroke=HS, creases=(1, 2))
        back += D(T([(96, 18), (62, 30), (34, 30), (14, 24)]), W([17, 15.5, 14, 12.5]), nail=-1, fill=HD, stroke=HS, creases=(1, 2))
        # dorso della mano
        back += B(T([(30, -34), (70, -62), (130, -66), (186, -46), (198, 0), (176, 40), (130, 52), (80, 40), (44, 14)]), HC, HS)
        back += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="%s" stroke-width="1.1" fill="none" opacity=".45"/>' % (
            T([(80, -54)])[0] + T([(116, -64)])[0] + T([(156, -58)])[0] + (HS,))
        front = ''
        # indice sopra lo strumento e pollice davanti
        front += D(T([(112, -50), (70, -48), (36, -30), (6, -14)]), W([18, 16, 14.5, 13]), nail=1, fill=HC, stroke=HS, creases=(1, 2))
        front += D(T([(110, 14), (70, 10), (36, 8), (6, 8)]), W([22, 19, 16, 14]), nail=1, fill=HC, stroke=HS, creases=(2,))
        return back, front

    # --- pannello sinistro: dotting
    x = 20
    body = client(x)
    dx, dy = x + 150, tb - 49
    gy = dy - 52
    hb, hf = hand(dx + 2, dy - 22, -25, (dx + 104, tb - 8), 0.55)
    body += hb + dotter2(dx, dy, -90, 50, 5) + hf
    body += arr(dx - 28, dy - 84, dx - 28, dy - 24, DARK, 2.2)
    body += text(x + 22, 104, 'Dotter', 14.5, 'start', 800) + text(x + 22, 122, 'verticale,', 14.5, 'start', 800)
    body += text(x + 22, 141, 'senza premere', 13, 'start', 600, MUTED)
    body += leader(dx + 104, tb - 2, dx + 60, tb + 24, 'Mignolo appoggiato', 'end', 13.5)
    for k in range(5):
        body += '<circle cx="%d" cy="%d" r="7" fill="%s"/>' % (x + 36 + k * 22, ey, FUCHSIA)
        body += '<circle cx="%.1f" cy="%.1f" r="2" fill="#fff" opacity=".6"/>' % (x + 34 + k * 22, ey - 2)
    body += mark(x + 150, ey, True, 11)
    for k, r in enumerate([4, 9, 6, 11, 5]):
        body += '<circle cx="%d" cy="%d" r="%d" fill="%s"/>' % (x + 202 + k * 22, ey, r, FUCHSIA)
    body += mark(x + 318, ey, False, 11)
    b += frame(x, 55, 350, 290, 'Dotting', body=body, cap='ricarica a ogni punto', capcol=INK)
    # --- pannello destro: striping
    x = 390
    body = client(x)
    sx, sy = x + 150, tb - 47
    body += '<path d="M%d,%d Q%d,%d %d,%d" stroke="%s" stroke-width="4.2" fill="none" stroke-linecap="round" opacity=".25"/>' % (x + 108, tb - 41, x + 128, tb - 46, sx, sy, INK)
    body += '<path d="M%d,%d Q%d,%d %d,%d" stroke="#fff" stroke-width="3.2" fill="none" stroke-linecap="round"/>' % (x + 108, tb - 42, x + 128, tb - 47, sx, sy)
    ang = -22
    rad = math.radians(ang)
    gx, gy = sx + 84 * math.cos(rad), sy + 84 * math.sin(rad)
    hb, hf = hand(sx + 52 * math.cos(rad), sy + 52 * math.sin(rad), ang, (sx + 126, tb - 8))
    body += hb + liner(sx, sy, ang, 116, bristle='#3b2a30', load='#ffffff') + hf
    body += text(x + 22, 106, 'Trascina, non spingere', 14.5, 'start', 800)
    body += text(x + 22, 124, 'pressione costante', 13, 'start', 600, MUTED)
    body += arr(x + 40, 148, x + 120, 148, DARK, 2.2)
    body += text(x + 80, 168, 'verso di te', 12.5, fill=MUTED, style='italic')
    body += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3" stroke-linecap="round"/>' % (x + 30, ey, x + 136, ey, FUCHSIA)
    body += mark(x + 156, ey, True, 11)
    wob = [(x + 196 + k * 6, ey + (3.5 if k % 2 else -3.5) * (1 if k % 3 else 0.4)) for k in range(19)]
    body += '<path d="%s" fill="none" stroke="%s" stroke-width="3" stroke-linecap="round"/>' % (smooth_d(wob), FUCHSIA)
    body += mark(x + 318, ey, False, 11)
    b += frame(x, 55, 350, 290, 'Striping', body=body, cap='mano ferma = linea ferma', capcol=INK)
    return svg(760, 360, defs() + b, 'Presa corretta per dotting (dotter verticale, mignolo appoggiato) e striping (pennello trascinato)')


def plate_disc(cx, cy, r=46, deco=True):
    s = '<circle cx="%.1f" cy="%.1f" r="%d" fill="#dfe3e8" stroke="%s" stroke-width="2"/>' % (cx, cy, r, GREY_D)
    s += '<circle cx="%.1f" cy="%.1f" r="%d" fill="none" stroke="#c4cad1" stroke-width="1"/>' % (cx, cy, r - 6)
    if deco:
        for dx, dy in ((-14, -10), (12, -12), (0, 12)):
            for k in range(5):
                a = math.radians(k * 72)
                s += '<circle cx="%.1f" cy="%.1f" r="3.4" fill="none" stroke="%s" stroke-width="1.3"/>' % (cx + dx + 5 * math.cos(a), cy + dy + 5 * math.sin(a), GREY_D)
    return s


def stamper(cx, cy, ang=0, hl=46):
    """Tampone: manico + testa morbida arrotondata; (cx, cy) = centro della base della testa (verso il basso)."""
    return rot(ang, cx, cy, '<rect x="%.1f" y="%.1f" width="22" height="%d" rx="5" fill="%s"/>' % (cx - 11, cy - 16 - hl, hl + 2, ACC2)
               + '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="#f3e9ee" stroke="#c9b3bd" stroke-width="1.5"/>' % (
                   cx - 20, cy - 16, cx + 20, cy - 16, cx, cy + 14, cx - 20, cy - 16))


def stamp_pattern(cx, cy, col='#ffffff', n=3):
    s = ''
    for dx, dy in ((-8, -14), (8, 2), (-6, 18))[:n]:
        for k in range(5):
            a = math.radians(k * 72)
            s += '<circle cx="%.1f" cy="%.1f" r="3.3" fill="none" stroke="%s" stroke-width="1.6"/>' % (cx + dx + 5 * math.cos(a), cy + dy + 5 * math.sin(a), col)
    return s


@figx('stamping-step.svg')
def stamping():
    b = title('Stamping in 5 passaggi')
    caps = [['Smalto', 'sul disegno'], ['Raschia', 'a 45°'], ['Rotola', 'il tampone'], ['Posa', 'rotolando'], ['Top:', 'sigilla']]
    BASE = '#f6cbd6'

    def plate(cx, cy, r=46, engraved=True, ink=False):
        s = '<circle cx="%.1f" cy="%.1f" r="%d" fill="#9aa3ad" filter="url(#nxShS)"/>' % (cx, cy, r)
        s += '<circle cx="%.1f" cy="%.1f" r="%d" fill="#e4e8ec"/>' % (cx, cy, r - 4)
        s += '<path d="M%.1f,%.1f A%d,%d 0 0 1 %.1f,%.1f" fill="none" stroke="#fff" stroke-width="3" opacity=".8" stroke-linecap="round"/>' % (
            cx - r * 0.62, cy - r * 0.5, r - 9, r - 9, cx + r * 0.1, cy - r * 0.78)
        if engraved:
            s += flower_pattern(cx, cy + 2, '#8d969f', 0.95, 1.3)
        if ink:
            s += flower_pattern(cx, cy + 2, BERRY, 0.95, 1.8)
        return s

    def stamper2(cx, cy, ang=0, inked=False):
        """Tampone in silicone trasparente con manico; (cx, cy) = punto più basso della testa."""
        g = '<rect x="-9" y="-62" width="18" height="34" rx="6" fill="%s"/>' % ACC2
        g += '<rect x="-6" y="-58" width="4" height="26" rx="2" fill="#fff" opacity=".3"/>'
        g += '<path d="M-20,-28 L20,-28 L20,-22 L-20,-22 Z" fill="#6f7983"/>'
        g += '<path d="M-20,-22 L20,-22 Q20,0 0,0 Q-20,0 -20,-22 Z" fill="#e8f1f6" stroke="#a9c4d4" stroke-width="1.4" opacity=".95"/>'
        g += '<path d="M-12,-18 Q-11,-8 -4,-4" stroke="#fff" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
        if inked:
            g += '<g opacity=".9">%s</g>' % ''.join(flower(dx, -9 + dy, 4.2, BERRY, 1.3) for dx, dy in ((-8, -2), (5, 2), (12, -5)))
        return '<g transform="translate(%.1f,%.1f) rotate(%.1f)">%s</g>' % (cx, cy, ang, g)

    for i in range(5):
        x = 20 + i * 194
        cx, cy = x + 90, 162
        body = ''
        if i == 0:
            body += plate(cx - 10, cy + 8, 52)
            body += '<path d="M%.1f,%.1f q12,-8 26,-2 q6,8 -4,12 q-14,4 -22,-10 z" fill="%s"/>' % (cx - 14, cy - 8, BERRY)
            body += '<ellipse cx="%.1f" cy="%.1f" rx="5" ry="2.4" fill="#fff" opacity=".5"/>' % (cx - 2, cy - 7)
            body += polish_bottle(cx + 56, cy - 22, 0.72, BERRY)
        elif i == 1:
            py = cy + 30
            body += '<rect x="%.1f" y="%.1f" width="150" height="10" rx="3" fill="#9aa3ad"/>' % (cx - 75, py)
            for k in range(6):
                body += '<path d="M%.1f,%.1f l4,4 l4,-4" fill="%s" stroke="#6f7983" stroke-width="1"/>' % (cx - 62 + k * 13, py, BERRY if k < 3 else 'none')
            body += '<path d="M%.1f,%.1f q8,-7 20,0 z" fill="%s"/>' % (cx + 4, py, BERRY)
            # raschietto (card) inclinato a 45°
            body += rot(-45, cx + 2, py, '<rect x="%.1f" y="%.1f" width="86" height="7" rx="2" fill="#d9dde2" stroke="#8d969f"/>'
                        '<rect x="%.1f" y="%.1f" width="86" height="2" fill="#fff" opacity=".7"/>' % (cx + 2, py - 7, cx + 2, py - 6))
            body += '<path d="M%.1f,%.1f A30,30 0 0 0 %.1f,%.1f" fill="none" stroke="%s" stroke-width="1.8" stroke-dasharray="3 3"/>' % (
                cx + 32, py, cx + 23, py - 21, ACC2)
            body += text(cx + 40, py - 10, '45°', 15, 'start', 800, ACC2)
            body += arr(cx + 40, py + 34, cx - 40, py + 34, DARK, 2)
        elif i == 2:
            body += plate(cx, cy + 34, 40, True, False)
            body += stamper2(cx - 2, cy - 4, -12, True)
            body += carr('M%.1f,%.1f A44,44 0 0 1 %.1f,%.1f' % (cx - 50, cy - 14, cx + 46, cy - 18), DARK, 2)
        elif i == 3:
            f, p = nail(cx, cy + 78, hw=27, nail_len=72, free_len=22, plate=BASE, free=BASE, shape='squoval', finger_len=22,
                        extra='<g clip-path="url(#CLIP)">%s</g>' % ''.join(flower(cx - 30 + dx, cy + 16 + dy, 6, BERRY, 1.5) for dx, dy in ((8, -4), (24, 10), (6, 24))))
            body += f
            body += stamper2(cx + 10, cy - 18, 18, True)
            body += carr('M%.1f,%.1f A46,46 0 0 1 %.1f,%.1f' % (cx - 52, cy - 44, cx + 50, cy - 48), DARK, 2)
        else:
            f, p = nail(cx, cy + 78, hw=27, nail_len=72, free_len=22, plate=BASE, free=BASE, shape='squoval', finger_len=22,
                        extra='<g clip-path="url(#CLIP)">%s</g>' % flower_pattern(cx + 2, cy + 26, BERRY, 1.05, 1.7))
            body += f + gloss(cx + 2, cy - 10, cy + 50, 4) + sparkle(cx + 20, cy - 6, 6)
            body += flat_brush(cx + 30, cy - 12, -40, 46, '#f4f1ec', w=6)
        b += frame(x, 55, 180, 262, None, num=i + 1, body=body, cap=caps[i], capcol=INK)
    b += '<rect x="290" y="328" width="420" height="32" rx="16" fill="%s" stroke="%s" stroke-width="1.4"/>' % (YEL_BG, YEL_S)
    b += ic_stopwatch(312, 343, 0.62, '#7a5a12')
    b += text(510, 349, 'Lavora veloce: lo smalto asciuga in pochi secondi', 14, weight=800, fill='#7a5a12')
    return svg(1000, 372, defs() + b, 'Stamping in cinque passaggi: smalto sulla piastra, raschia a 45°, rotola il tampone, posa rotolando, sigilla con top')


def reverse_cres(cx, yc, hw, m=5, t=20, col=ACC2, inset=6):
    """Mezzaluna alla base (reverse french): margine m dalla cuticola, spessore t al centro."""
    lo, hi = [], []
    n = 24
    for k in range(n + 1):
        x = cx - hw + inset + (2 * hw - 2 * inset) * k / n
        u = (x - cx) / (hw - inset)
        yb = cut_y(cx, yc, hw, x) - m
        lo.append((x, yb))
        hi.append((x, yb - t * (1 - u * u)))
    return '<path d="M%s Z" fill="%s"/>' % (' L'.join('%.1f,%.1f' % q for q in lo + hi[::-1]), col)


@figx('french-varianti.svg')
def french_variants():
    b = title('Varianti del french')
    names = [('Classico', 'punta bianca a sorriso'), ('A V', 'punta a "V"'), ('Micro', 'linea sottilissima'),
             ('Reverse', 'mezzaluna alla base'), ('Colorato', 'punta colorata'), ('Doppio', 'french + filo')]
    BASE = '#f6cbd6'
    for i, (nm, sub) in enumerate(names):
        x = 18 + i * 162
        cx = x + 75
        b += '<rect x="%d" y="52" width="150" height="282" rx="16" fill="%s"/>' % (x, PANEL)
        yc, hw, nl, fl = 222, 31, 90, 62
        ys, top = yc - nl, yc - nl - fl
        plate = NUDE if i == 3 else BASE
        extra = ''
        if i == 0:
            extra = tip_fill(cx, ys, hw, 22, top)
        elif i == 1:
            vp = 'M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (
                cx - hw - 6, ys - 30, cx, ys + 14, cx + hw + 6, ys - 30, cx + hw + 6, top - 20, cx - hw - 6, top - 20)
            extra = '<path d="%s" fill="#fff" stroke="%s" stroke-width="1.2" stroke-linejoin="round" clip-path="url(#CLIP)"/>' % (vp, WHITE_S)
        elif i == 2:
            out = nail_outline(cx, yc, ys, top, hw, 'mandorla')
            rc = uid('r')
            extra = ('<clipPath id="%s"><rect x="%.1f" y="%.1f" width="120" height="%.1f"/></clipPath>'
                     '<g clip-path="url(#CLIP)"><g clip-path="url(#%s)"><path d="%s" fill="none" stroke="#fff" stroke-width="13"/>'
                     '<path d="%s" fill="none" stroke="%s" stroke-width="1" transform="translate(0,0)"/></g></g>'
                     % (rc, cx - 60, top - 10, ys - 22 - top + 10, rc, out, out, WHITE_S))
        elif i == 3:
            extra = reverse_cres(cx, yc, hw, 5, 15, '#b9466e')
        elif i == 4:
            extra = tip_fill(cx, ys, hw, 22, top, '#c2185b', None)
            extra += '<path d="M%s" fill="none" stroke="#8e1244" stroke-width="1" clip-path="url(#CLIP)"/>' % ' L'.join('%.1f,%.1f' % q for q in smile_pts(cx, ys, hw, 22))
        else:
            extra = tip_fill(cx, ys, hw, 22, top)
            pts = smile_pts(cx, ys + 12, hw, 22)
            extra += '<path d="%s" fill="none" stroke="%s" stroke-width="3.2" clip-path="url(#CLIP)"/>' % (smooth_d(pts), GOLD_S)
            extra += '<path d="%s" fill="none" stroke="%s" stroke-width="1.6" clip-path="url(#CLIP)"/>' % (smooth_d([(px, py - 0.6) for px, py in pts]), GOLD)
        f, p = nail(cx, yc, hw=hw, nail_len=nl, free_len=fl, shape='mandorla', plate=plate, free=plate, extra=extra, finger_len=40)
        pc = uid('k')
        b += '<clipPath id="%s"><rect x="%d" y="52" width="150" height="230"/></clipPath><g clip-path="url(#%s)">%s</g>' % (pc, x, pc, f)
        b += '<line x1="%d" y1="282" x2="%d" y2="282" stroke="#efdcd6"/>' % (x, x + 150)
        b += text(cx, 305, nm, 16, weight=800) + text(cx, 323, sub, 12.5, weight=600, fill=MUTED)
    return svg(1000, 344, b, 'Sei varianti del french: classico, a V, micro, reverse, colorato e doppio')


@figx('reverse-french-step.svg')
def reverse_steps():
    b = title('Reverse french')
    heads = ['Base + colore', 'Arco dal centro', 'Margine dalla pelle', 'Top opaco + lucido']
    caps = ['due strati sottili', 'poi verso i lati', None, 'mezzaluna lucida']
    for i in range(4):
        x = 20 + i * 218
        cx, yc, hw = x + 103, 262, 45
        nl, fl = 124, 34
        body = ''
        if i in (0, 1, 3):
            extra = ''
            if i == 1:
                rc = uid('r')
                extra = ('<defs><clipPath id="%s"><rect x="%.1f" y="%.1f" width="44" height="80"/></clipPath></defs>' % (rc, cx - 22, yc - 90)
                         + '<g clip-path="url(#%s)">%s</g>' % (rc, reverse_cres(cx, yc, hw, 5, 19, ACC2)))
                extra += reverse_cres(cx, yc, hw, 5, 19, 'none').replace('fill="none"', 'fill="none" stroke="%s" stroke-width="1.5" stroke-dasharray="4 3"' % ACC2)
            if i == 3:
                extra = reverse_cres(cx, yc, hw, 5, 19, ACC2)
                rng = random.Random(9)
                extra += '<g clip-path="url(#CLIP)">' + ''.join('<circle cx="%.1f" cy="%.1f" r="1" fill="#c9998a"/>' % (cx + rng.uniform(-42, 42), yc - rng.uniform(46, 170)) for _ in range(110)) + '</g>'
                extra += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="#fff" stroke-width="3" fill="none" opacity=".95" stroke-linecap="round"/>' % (cx - 20, yc - 30, cx, yc - 40, cx + 18, yc - 32)
            f, p = nail(cx, yc, hw=hw, nail_len=nl, free_len=fl, shape='tonda', plate=NUDE, free=NUDE, extra=extra, finger_len=30)
            body += f
            if i == 1:
                yb = cut_y(cx, yc, hw, cx) - 5
                body += carr('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx - 10, yb - 34, cx - 26, yb - 36, cx - 38, yb - 48), DARK, 2)
                body += carr('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx + 10, yb - 34, cx + 26, yb - 36, cx + 38, yb - 48), DARK, 2)
                body += dot(cx, yb - 9, 4.5, '#fff', ACC2)
                body += brush_liner(cx + 1, yb - 12, -78, 70)
        else:
            # zoom sulla zona cuticolare (vista dall'alto)
            zx, zy, zw, zh = x + 18, 96, 170, 112
            zc = uid('z')
            ccx = zx + zw / 2
            skin_top = lambda px: zy + 70 + 26 * ((px - ccx) / 120.0) ** 2 * -1 + 26
            sk = [(px, zy + 96 - 30 * ((px - ccx) / 110.0) ** 2) for px in range(int(zx - 20), int(zx + zw + 21), 6)]
            inner = '<rect x="%d" y="%d" width="%d" height="%d" fill="%s"/>' % (zx, zy, zw, zh, NUDE)
            lo = [(px, py - 16) for px, py in sk]
            hi = [(px, py - 16 - 30 * max(0.0, 1 - ((px - ccx) / 100.0) ** 2)) for px, py in sk]
            inner += '<path d="M%s Z" fill="%s"/>' % (' L'.join('%.1f,%.1f' % q for q in lo + hi[::-1]), ACC2)
            inner += '<path d="M%s L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="2"/>' % (
                ' L'.join('%.1f,%.1f' % q for q in sk), zx + zw + 30, zy + zh + 30, zx - 30, zy + zh + 30, SKIN, SKIN_D)
            z = '<defs><clipPath id="%s"><rect x="%d" y="%d" width="%d" height="%d" rx="10"/></clipPath></defs>' % (zc, zx, zy, zw, zh)
            z += '<g clip-path="url(#%s)">%s</g>' % (zc, inner)
            z += '<rect x="%d" y="%d" width="%d" height="%d" rx="10" fill="none" stroke="%s" stroke-width="1.5"/>' % (zx, zy, zw, zh, MUTED)
            gy = zy + 96
            z += arr(ccx, gy - 15, ccx, gy - 1, DARK, 1.6, True)
            z += label_box(ccx + 8, gy - 26, 62, 22, '≈ 1 mm', '#fff', '#d8c8c4', INK, 13, 800, 6, 1)
            z += mark(zx + zw - 18, zy + 18, True, 11)
            z += text(zx + 10, zy + 22, 'zoom', 12.5, 'start', 600, MUTED, 'italic')
            body += z
            # esempio sbagliato: il colore copre la pelle
            ex, ey, ew, eh = x + 18, 224, 170, 78
            ec = uid('z')
            sk2 = [(px, ey + 62 - 22 * ((px - ex - ew / 2) / 110.0) ** 2) for px in range(int(ex - 20), int(ex + ew + 21), 6)]
            inner2 = '<rect x="%d" y="%d" width="%d" height="%d" fill="%s"/>' % (ex, ey, ew, eh, NUDE)
            inner2 += '<path d="M%s L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="2"/>' % (
                ' L'.join('%.1f,%.1f' % q for q in sk2), ex + ew + 30, ey + eh + 30, ex - 30, ey + eh + 30, SKIN, SKIN_D)
            inner2 += '<path d="M%s Z" fill="%s" opacity=".95"/>' % (' L'.join('%.1f,%.1f' % q for q in [(px, py + 9) for px, py in sk2] + [(px, py - 14) for px, py in sk2[::-1]]), ACC2)
            w2 = '<defs><clipPath id="%s"><rect x="%d" y="%d" width="%d" height="%d" rx="10"/></clipPath></defs><g clip-path="url(#%s)">%s</g>' % (ec, ex, ey, ew, eh, ec, inner2)
            w2 += '<rect x="%d" y="%d" width="%d" height="%d" rx="10" fill="none" stroke="#efc4bd" stroke-width="1.5"/>' % (ex, ey, ew, eh)
            w2 += mark(ex + ew - 18, ey + 18, False, 11) + text(ex + 10, ey + 23, 'tocca la pelle', 13.5, 'start', 800, ERR)
            body += w2
        b += frame(x, 55, 205, 260, heads[i], num=i + 1, body=body, cap=caps[i], capcol=INK, hsize=14.5)
    return svg(900, 330, defs() + b, 'Reverse french in quattro passaggi con margine di circa 1 mm dalla pelle')


# ================================================================= MODULO 10 – MANUTENZIONE
GELP = '#eaa6bc'       # ricostruzione colorata (vista dall'alto)
GELP_S = '#c77b95'


def regrowth(cx, yc, hw, h=26, col=NAIL):
    """Fascia di ricrescita naturale tra la cuticola e il prodotto (extra per finger_nail)."""
    pts_lo = [(cx - hw - 6 + k * (2 * hw + 12) / 20.0, 0) for k in range(21)]
    lo = [(px, cut_y(cx, yc, hw, px) + 4) for px, _ in pts_lo]
    hi = [(px, cut_y(cx, yc, hw, px) - h) for px, _ in pts_lo]
    s = '<path d="M%s Z" fill="%s" clip-path="url(#CLIP)"/>' % (' L'.join('%.1f,%.1f' % q for q in lo + hi[::-1]), col)
    s += '<path d="M%s" fill="none" stroke="%s" stroke-width="1.6" clip-path="url(#CLIP)"/>' % (' L'.join('%.1f,%.1f' % q for q in hi), GELP_S)
    return s


def zigzag(x, y, n=5, dx=9, dy=7, col=INK, w=2.4):
    pts = [(x + k * dx, y + (dy if k % 2 else -dy) * (0.6 + 0.4 * ((k * 7) % 3) / 2.0)) for k in range(n + 1)]
    return '<path d="M%s" fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>' % (' L'.join('%.1f,%.1f' % q for q in pts), col, w)


def ring(x, y, r, col=ACC2, w=2.2, dash=''):
    return '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" stroke-width="%s"%s/>' % (
        x, y, r, col, w, (' stroke-dasharray="%s"' % dash) if dash else '')


def checkbox(x, y, label, size=15):
    return ('<rect x="%.1f" y="%.1f" width="18" height="18" rx="3" fill="#fff" stroke="%s" stroke-width="2"/>' % (x, y - 14, ACC2)
            + text(x + 28, y, label, size, 'start', 600))


@figx('refill-valutazione.svg')
def refill_check():
    b = title('Prima del refill: guarda')
    cx, yc, hw = 150, 318, 56
    extra = regrowth(cx, yc, hw, 30)
    # sollevamento laterale (zona grigio-bianca)
    extra += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="#f4f1f2" opacity=".95" clip-path="url(#CLIP)"/>' % (
        cx + hw + 2, yc - 120, cx + hw - 26, yc - 90, cx + hw + 2, yc - 58, cx + hw + 2, yc - 120)
    # macchia verde sotto il prodotto
    extra += '<ellipse cx="%.1f" cy="%.1f" rx="15" ry="11" fill="#5d9b4f" opacity=".75" clip-path="url(#CLIP)"/>' % (cx - 24, yc - 110)
    f, p = nail(cx, yc, hw=hw, nail_len=180, free_len=62, plate=GELP, free=GELP, extra=extra, finger_len=40)
    b += f
    b += zigzag(cx - 18, yc - 185, 5, 9, 6)
    # richiami
    b += ring(cx + 10, yc - 34, 13) + leader(cx + 23, yc - 34, 300, 300, 'Ricrescita (quanti mm?)')
    b += ring(cx + hw - 6, yc - 90, 15) + leader(cx + hw + 9, yc - 90, 300, 226, 'Sollevamento?')
    b += ring(cx + 5, yc - 185, 17) + leader(cx + 22, yc - 185, 300, 98, 'Crepa?')
    b += ring(cx - 24, yc - 110, 19, ERR, 3) + leader(cx - 5, yc - 110, 300, 162, 'Macchia verde = STOP', fill=ERR)
    # lista di controllo
    bx = 500
    b += box(bx, 56, 380, 176, PANEL, PANEL, 16)
    b += text(bx + 20, 86, 'Controlla ogni unghia', 16, 'start', 800)
    for k, l in enumerate(['Dall\'alto', 'Di profilo', 'Da sotto il bordo libero', 'Dolore / rossore?']):
        b += checkbox(bx + 22, 122 + k * 30, l)
    # esiti
    oy = 262
    b += text(bx, oy, 'Decidi:', 15, 'start', 800, ACC2)
    outs = [(['Refill'], OK, GREEN_BG), (['Refill +', 'riparazione'], WARN, YEL_BG), (['Rimozione', '/ medico'], ERR, RED_BG)]
    for k, (l, col, bg) in enumerate(outs):
        ox = bx + k * 130
        b += label_box(ox, oy + 18, 120, 58, l, bg, col, col, 15, 800, 12, 2.2 if k == 2 else 1.6)
    b += arr(bx + 62, oy - 5, bx + 290, oy - 5, DARK, 1.6, dash='5 4')
    return svg(900, 380, defs() + b, 'Valutazione prima del refill: ricrescita, sollevamenti, crepe, macchie verdi; esiti possibili')


def sec_panel_profile(x0, y, L, F, prod_pts, prod_end, fill=PROD, stroke=PROD_S, extra=''):
    sec, fd, p = section(x0, y, L=L, F=F, body_h=62)
    return sec + product(prod_pts, y, end_x=prod_end[0], end_y=prod_end[1], fill=fill, stroke=stroke) + extra + fd, p


@figx('refill-assottigliare.svg')
def rebalance():
    b = title('Rebalance: di profilo')
    heads = ['Dopo 3 settimane', 'Assottiglia 30–50%', 'Nuovo apex']
    for i in range(3):
        x = 20 + i * 292
        x0, y, L = x + 56, 206, 150
        F = 60 if i == 0 else 40
        xs = x0 + L
        body = ''
        if i == 0:
            g = 28   # ricrescita
            pts = [(x0 + g, y - 3), (x0 + g + 30, y - 16), (xs - 20, y - 30), (xs + 22, y - 40), (xs + 46, y - 28), (xs + F + 2, y - 8)]
            sec, p = sec_panel_profile(x0, y, L, F, pts, (xs + F + 2, y + 6))
            body += sec
            body += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="#f6a7bb" stroke-width="5" stroke-linecap="round"/>' % (x0 + 3, y + 1, x0 + g - 3, y + 1)
            body += leader(x0 + 14, y + 2, x0 + 14, y + 44, 'ricrescita', 'middle', 13)
            body += arr(xs + 22, y - 84, xs + 22, y - 46, ERR, 2.2)
            body += text(xs + 10, y - 92, 'Apex spostato', 14, weight=800, fill=ERR)
        elif i == 1:
            old = [(x0 + 28, y - 3), (x0 + 58, y - 16), (xs - 20, y - 30), (xs + 22, y - 40), (xs + F + 2, y - 12)]
            thin = [(x0 + 28, y - 2), (x0 + 60, y - 8), (xs - 10, y - 14), (xs + 20, y - 15), (xs + F + 2, y - 6)]
            sec, p = sec_panel_profile(x0, y, L, F, thin, (xs + F + 2, y + 6))
            body += sec
            body += '<path d="%s" fill="none" stroke="%s" stroke-width="1.8" stroke-dasharray="5 4"/>' % (smooth_d(old), ERR)
            body += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="#f6a7bb" stroke-width="5" stroke-linecap="round"/>' % (x0 + 3, y + 1, x0 + 25, y + 1)
            body += text(xs - 20, y - 54, 'tolto con la lima', 13, weight=700, fill=ERR)
            body += file_tool(xs - 40, y - 84, -8, 90, 14)
        else:
            thin = [(x0 + 28, y - 2), (x0 + 60, y - 8), (xs - 10, y - 14), (xs + 20, y - 15), (xs + F + 2, y - 6)]
            new = [(x0 + 8, y - 2), (x0 + 40, y - 16), (xs - 30, y - 38), (xs + 2, y - 42), (xs + 30, y - 30), (xs + F + 2, y - 9)]
            sec, fd, p = section(x0, y, L=L, F=F, body_h=62)
            body += sec + product(new, y, end_x=xs + F + 2, end_y=y + 6, fill=PROD2, stroke='#6ea6c8')
            body += '<path d="%s" fill="none" stroke="%s" stroke-width="1.2" stroke-dasharray="3 3"/>' % (smooth_d(thin), PROD_S) + fd
            body += arr(xs, y - 84, xs, y - 48, OK, 2.2) + text(xs - 10, y - 92, 'apex al suo posto', 14, weight=800, fill=OK)
        body += stress_tri(xs, y + 10)
        b += frame(x, 55, 278, 270, heads[i], num=i + 1, ok=(None if i == 0 else (True if i == 2 else None)), body=body,
                   cap=['ricrescita + apex in avanti', 'assottigliato, raccordato', 'apex sopra il punto di stress'][i], capcol=INK)
    b += text(450, 345, 'Il triangolino ▲ indica il punto di stress: l\'apex deve stare sopra di esso.', 13.5, fill=MUTED)
    return svg(900, 356, defs() + b, 'Rebalance di profilo: apex spostato dopo 3 settimane, assottigliamento del 30-50%, nuovo apex sopra il punto di stress')


@figx('refill-gradino.svg')
def refill_step_edge():
    b = title('Raccordo alla base')
    b += text(740, 38, 'zona cuticolare ingrandita, di profilo', 13, 'end', fill=MUTED, style='italic')
    for i in range(2):
        ok = i == 1
        x = 20 + i * 370
        R = x + 350
        py = 200
        body = '<rect x="%d" y="%d" width="350" height="38" fill="%s"/>' % (x, py + 18, SKIN)
        body += '<rect x="%d" y="%d" width="350" height="8" fill="%s"/>' % (x, py + 12, BED)
        body += '<rect x="%d" y="%d" width="350" height="12" fill="%s" stroke="%s" stroke-width="1.2"/>' % (x - 2, py, PLATE_SEC, NAIL_S)
        m0 = x + 86   # inizio del prodotto (dopo il margine)
        if not ok:
            body += '<path d="M%d,%d L%d,%d L%d,%d L%d,%d Z" fill="%s" stroke="%s" stroke-width="1.6"/>' % (x + 136, py, x + 136, py - 30, R + 5, py - 30, R + 5, py, PROD, PROD_S)
            top = [(m0, py), (x + 112, py - 12), (x + 132, py - 32), (x + 150, py - 46), (x + 180, py - 44), (R + 5, py - 42)]
            body += '<path d="%s L%d,%d L%d,%d L%d,%d Z" fill="%s" stroke="#5f9cc0" stroke-width="1.8"/>' % (
                smooth_d(top), R + 5, py - 30, x + 136, py - 30, x + 136, py, PROD2)
            body += ring(x + 146, py - 36, 24, ERR, 2.4)
            body += text(x + 215, 100, 'gobba sopra il gradino', 14, weight=700, fill=ERR)
            body += text(x + 250, py - 10, 'vecchio prodotto', 12.5, weight=600, fill=MUTED)
            body += text(x + 250, py - 50, 'nuovo', 12.5, weight=600, fill='#3f7ea6')
        else:
            old = [(x + 120, py), (x + 160, py - 12), (x + 210, py - 28), (x + 250, py - 30), (R + 5, py - 30)]
            body += product(old, py, end_x=R + 5, end_y=py, fill=PROD, stroke=PROD_S)
            top = [(m0, py), (x + 120, py - 16), (x + 170, py - 34), (x + 230, py - 42), (R + 5, py - 42)]
            body += '<path d="%s L%s Z" fill="%s" stroke="#5f9cc0" stroke-width="1.8"/>' % (
                smooth_d(top), smooth_d(old[::-1])[1:].replace('C', 'C', 1) if False else ' L'.join('%.1f,%.1f' % q for q in old[::-1]) + ' L%d,%d' % (m0, py), PROD2)
            body += text(x + 215, 100, 'superficie continua', 14, weight=700, fill=OK)
            body += text(x + 290, py - 10, 'vecchio', 12.5, weight=600, fill=MUTED)
            body += text(x + 290, py - 50, 'nuovo', 12.5, weight=600, fill='#3f7ea6')
        # piega prossimale (pelle)
        body += '<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Z" fill="%s" stroke="%s" stroke-width="1.6"/>' % (
            x - 2, 150, x + 52, 150, x + 74, 154, x + 76, py, x - 2, py, SKIN, SKIN_D)
        body += arr(x + 77, py - 6, m0 - 1, py - 6, DARK, 1.4, True)
        body += leader(x + 81, py - 8, x + 104, 134, 'margine ≈ 1 mm', 'start', 13)
        cap = 'Raccordo liscio' if ok else 'Gradino: si aggancia e solleva'
        b += frame(x, 55, 350, 230, None, ok=ok, body=body, cap=cap)
    return svg(760, 300, defs() + b, 'Raccordo alla base nel refill: gradino da evitare e raccordo liscio, con margine dalla pelle')


@figx('rimozione-decisione.svg')
def removal_tree():
    b = title('Come si rimuove?')
    rows = [('Semipermanente', 'Soak-off', '10–15 min', 'soak', '#e98fae'),
            ('Soft gel / BIAB', 'Assottiglia + soak-off', '10–30 min', 'soak', '#c9b6e4'),
            ('Acrilico', 'Assottiglia + soak-off', '20–30 min', 'soak', '#9cc3d8'),
            ('Polygel', 'Leggi la scheda tecnica', None, 'doc', '#f6d38a'),
            ('Hard gel', 'File-off: lascia un velo', None, 'file', '#b9a99c')]
    # intestazioni di colonna
    for x, l in ((236, 'PRODOTTO'), (452, 'METODO'), (700, 'TEMPO'), (842, '')):
        b += text(x, 70, l, 12, 'start', 800, MUTED)
    # nodo radice
    ry = 214
    b += '<rect x="20" y="%d" width="150" height="58" rx="14" fill="%s" filter="url(#nxShS)"/>' % (ry - 29, ACC2)
    b += text(95, ry - 3, 'Quale', 16, weight=800, fill='#fff') + text(95, ry + 16, 'prodotto?', 16, weight=800, fill='#fff')
    for k, (prod, meth, t, ic, col) in enumerate(rows):
        yy = 84 + k * 62
        my = yy + 24
        # connettore a gomito
        b += '<path d="M170,%d L186,%d C212,%d 200,%d 228,%d" fill="none" stroke="#cdbcb8" stroke-width="2"/>' % (ry, ry, ry, my, my)
        b += '<circle cx="230" cy="%d" r="3.5" fill="%s"/>' % (my, ACC2)
        # prodotto
        b += card(236, yy, 180, 48, rx=10)
        sc = uid('st')
        b += '<clipPath id="%s"><rect x="236" y="%d" width="180" height="48" rx="10"/></clipPath>' % (sc, yy)
        b += '<rect x="236" y="%d" width="7" height="48" fill="%s" clip-path="url(#%s)"/>' % (yy, col, sc)
        b += text(334, my + 5.5, prod, 15, weight=800)
        b += arr(420, my, 444, my, DARK, 2)
        # metodo + tempo
        b += '<rect x="452" y="%d" width="370" height="48" rx="10" fill="%s"/>' % (yy, PANEL)
        mcol = WARN if ic == 'doc' else INK
        b += text(470, my + 5.5, meth, 15, 'start', 800, mcol)
        if t:
            b += '<rect x="690" y="%d" width="118" height="28" rx="14" fill="#fff" stroke="#e5d6d2"/>' % (my - 14)
            b += ic_clock(707, my, 0.95) + text(721, my + 5, t, 13.5, 'start', 800, ACC2)
        else:
            b += text(749, my + 5, '—', 15, weight=700, fill=MUTED)
        # icona del metodo
        b += '<circle cx="858" cy="%d" r="22" fill="#fff" stroke="#ead9d4"/>' % my
        if ic == 'soak':
            b += ic_foil2(858, my, 0.78)
        elif ic == 'doc':
            b += ic_doc(858, my, 0.8, False, WARN)
        else:
            b += file_board(858, my, -40, 40, 10)
    b += '<rect x="160" y="400" width="580" height="32" rx="16" fill="%s" stroke="%s" stroke-width="1.4"/>' % (YEL_BG, YEL_S)
    b += text(450, 421, 'Tempi indicativi: segui sempre le istruzioni del produttore', 14, weight=700, fill='#7a5a12')
    return svg(900, 446, defs() + b, 'Come si rimuove ogni prodotto: semipermanente, soft gel, acrilico con soak-off; polygel secondo scheda tecnica; hard gel con file-off')


@figx('rimozione-soakoff-step.svg')
def soak_steps():
    b = title('Soak-off passo passo')
    caps = [['Togli il top', 'e assottiglia'], ['Olio', 'sulla pelle'], ['Cotone', '+ acetone'], ['Avvolgi', 'e aspetta'], ['Spingi, non', 'fare leva'], ['Buffer morbido', '+ olio']]
    for i in range(6):
        x = 20 + i * 162
        cx, yc = x + 75, 232
        body = ''
        if i == 3:
            # dito avvolto nella stagnola: pelle sotto, involucro stropicciato sopra
            body += ('<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>'
                     % (cx - 40, yc + 40, cx - 40, yc - 40, cx + 40, yc - 40, cx + 40, yc + 40, SKIN, SKIN_D))
            fp = smooth_d([(cx - 44, yc - 10), (cx - 45, yc - 64), (cx - 34, yc - 104), (cx - 8, yc - 118), (cx + 12, yc - 116),
                           (cx + 36, yc - 102), (cx + 45, yc - 66), (cx + 44, yc - 10)])
            body += '<path d="%s Q%.1f,%.1f %.1f,%.1f Z" fill="#d9dde2" stroke="#8d969f" stroke-width="1.5"/>' % (fp, cx, yc - 2, cx - 46, yc - 10)
            rng = random.Random(7)
            for k in range(4):
                yy = yc - 96 + k * 22
                pts = [(cx - 40 + j * 16, yy + rng.uniform(-5, 5)) for j in range(6)]
                body += '<path d="M%s" fill="none" stroke="#a9b1b9" stroke-width="1.1"/>' % ' L'.join('%.1f,%.1f' % q for q in pts)
            body += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="#fff" stroke-width="4" fill="none" opacity=".8" stroke-linecap="round"/>' % (
                cx - 24, yc - 92, cx - 30, yc - 56, cx - 24, yc - 22)
            body += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="#8d969f" stroke-width="1.5"/>' % (cx - 46, yc - 10, cx, yc - 2, cx + 46, yc - 10)
            body += '<rect x="%.1f" y="88" width="74" height="26" rx="13" fill="#fff" stroke="%s" stroke-width="1.4"/>' % (x + 68, ACC2)
            body += ic_clock(x + 82, 101, 0.85) + text(x + 93, 105.5, '10–15\'', 12.5, 'start', 800, ACC2)
        else:
            plate, free = (FUCHSIA, FUCHSIA) if i in (0, 1, 2) else ((NAIL, FREE) if i == 5 else ('#e98fae', '#e98fae'))
            extra = ''
            if i == 4:
                rng = random.Random(3)
                extra = '<g clip-path="url(#CLIP)">' + ''.join('<path d="M%.1f,%.1f q5,-4 10,0" stroke="#fff" stroke-width="1.6" fill="none" opacity=".8"/>' % (
                    cx - 24 + rng.uniform(0, 40), yc - 120 + rng.uniform(0, 90)) for _ in range(14)) + '</g>'
            f, p = nail(cx, yc, hw=30, nail_len=88, free_len=26, plate=plate, free=free, extra=extra, finger_len=24)
            body += f
            if i == 0:
                body += file_board(cx + 30, yc - 120, -62, 96, 14)
                rng = random.Random(1)
                body += ''.join('<circle cx="%.1f" cy="%.1f" r="1.8" fill="#c48aa0"/>' % (cx - 46 + rng.uniform(0, 30), yc - 150 + rng.uniform(0, 40)) for _ in range(12))
            elif i == 1:
                for sx in (-1, 1):
                    body += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="#fff" stroke-width="3" fill="none" opacity=".9" stroke-linecap="round"/>' % (
                        cx + sx * 40, yc - 70, cx + sx * 46, yc - 30, cx + sx * 30, yc + 4)
                body += ic_drop(cx + 46, yc - 128, 0.9)
            elif i == 2:
                body += '<ellipse cx="%.1f" cy="%.1f" rx="32" ry="38" fill="#ffffff" stroke="#d8d0cc" stroke-width="1.5"/>' % (cx, yc - 74)
                body += '<ellipse cx="%.1f" cy="%.1f" rx="20" ry="22" fill="#e8f3fb"/>' % (cx, yc - 74)
                body += ic_drop(cx + 34, yc - 130, 0.8, '#cfe7f7', '#7fb3d5')
            elif i == 4:
                body += stick(cx - 2, yc - 44, 60, 100)
                body += arr(cx - 46, yc - 70, cx - 46, yc - 130, DARK, 2)
            elif i == 5:
                body += ic_drop(cx + 2, yc - 30, 0.75)
                body += sparkle(cx - 12, yc - 92, 6)
        b += frame(x, 55, 150, 270, None, num=i + 1, body=body, cap=caps[i], capcol=INK)
    return svg(1000, 340, defs() + b, 'Soak-off in sei passaggi: assottiglia, olio sulla pelle, cotone con acetone, avvolgi, spingi senza fare leva, buffer e olio')


@figx('rimozione-errori.svg')
def removal_errors():
    b = title('Rimozione: cosa NON fare')
    heads = [('Fare leva', False), ('Raschiare', False), ('Strappare', False), ('Ammorbidisci', True)]
    caps = ['strappa strati di lamina', 'solchi bianchi', 'porta via la lamina', 'e spingi, senza forzare']
    for i, (t, ok) in enumerate(heads):
        x = 20 + i * 218
        cx, yc = x + 103, 256
        body = ''
        if i == 0:
            x0, y = x + 40, 190
            sec, fd, p = section(x0, y, L=120, F=26, body_h=56)
            body += sec
            # prodotto sollevato con scaglie di lamina attaccate
            body += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>' % (
                x0 + 30, y - 2, x0 + 80, y - 30, x0 + 150, y - 34, x0 + 150, y - 22, x0 + 84, y - 18, x0 + 30, y - 2, '#e98fae', NAIL_S)
            body += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="3" fill="none"/>' % (x0 + 70, y - 14, x0 + 96, y - 22, x0 + 120, y - 21, PLATE_SEC)
            body += fd
            body += tool_pusher(x0 + 92, y - 14, 160, 90)
            body += arr(x0 + 110, y - 40, x0 + 110, y - 80, ERR, 2.2)
        elif i == 1:
            f, p = nail(cx, yc, hw=34, nail_len=110, free_len=30, plate=NAIL, free=FREE, finger_len=24,
                        extra='<g clip-path="url(#CLIP)">' + ''.join('<path d="M%.1f,%.1f l%.1f,-60" stroke="#ffffff" stroke-width="2.4"/>' % (cx - 26 + k * 12, yc - 30, 8) for k in range(5)) + '</g>')
            body += f
            body += '<g transform="translate(%.1f,%.1f) rotate(-60)"><rect x="0" y="-4" width="74" height="8" rx="3" fill="#9aa3ad"/><path d="M0,-4 L-16,-1 L-16,3 L0,4 Z" fill="#6f7983"/></g>' % (cx + 6, yc - 100)
        elif i == 2:
            extra = '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="#f4dfe5" clip-path="url(#CLIP)"/>' % (cx - 50, yc - 30, cx + 50, yc - 30, cx + 50, yc - 160)
            f, p = nail(cx, yc, hw=34, nail_len=110, free_len=30, plate='#e98fae', free='#e98fae', finger_len=24, extra=extra)
            body += f
            # pezzo di prodotto staccato tirato da due dita
            body += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="#e98fae" stroke="%s" stroke-width="1.5"/>' % (
                cx + 6, yc - 60, cx + 40, yc - 120, cx + 58, yc - 136, cx + 70, yc - 122, cx + 40, yc - 90, cx + 30, yc - 40, NAIL_S)
            body += capsule(cx + 112, yc - 176, cx + 66, yc - 136, 15)     # indice
            body += capsule(cx + 120, yc - 120, cx + 72, yc - 126, 15)     # pollice
            body += arr(cx + 62, yc - 98, cx + 94, yc - 114, ERR, 2.2)
        else:
            rng = random.Random(5)
            extra = '<g clip-path="url(#CLIP)">' + ''.join('<path d="M%.1f,%.1f q5,-4 10,0" stroke="#fff" stroke-width="1.6" fill="none" opacity=".8"/>' % (
                cx - 26 + rng.uniform(0, 44), yc - 140 + rng.uniform(0, 100)) for _ in range(14)) + '</g>'
            f, p = nail(cx, yc, hw=34, nail_len=110, free_len=30, plate='#efb3c5', free='#efb3c5', finger_len=24, extra=extra)
            body += f + stick(cx - 4, yc - 52, 62, 70)
            body += arr(cx - 52, yc - 70, cx - 52, yc - 140, OK, 2.2)
        b += frame(x, 55, 205, 255, t, ok=ok, body=body, cap=caps[i], capcol=OK if ok else ERR, hsize=14.5)
    return svg(900, 325, defs() + b, 'Errori nella rimozione: fare leva, raschiare, strappare; corretto: ammorbidire e spingere')


@figx('riparazione-decisione.svg')
def repair_tree():
    b = title('Cosa si è rotto?')
    b += text(880, 38, 'guarda il danno, poi scegli', 13.5, 'end', 600, MUTED, 'italic')
    cases = [(['Crepa nel prodotto'], ['Ripara in salone'], OK, GREEN_BG, 'ok'),
             (['Sollevamento'], ['Elimina tutto', 'e ricostruisci'], OK, GREEN_BG, 'redo'),
             (['Rotta oltre il', 'bordo libero'], ['Accorcia e', 'ricostruisci'], WARN, YEL_BG, 'cut'),
             (['Rottura nel letto'], ['Non coprire:', 'medico'], ERR, RED_BG, 'med')]
    for i, (t, out, col, bg, kind) in enumerate(cases):
        x = 20 + i * 218
        cx, yc = x + 103, 236
        b += card(x, 56, 205, 300)
        for k, l in enumerate(t):
            b += text(cx, 84 + k * 18 - (9 if len(t) == 2 else 0), l, 15, weight=800)
        extra = ''
        fl = 34
        if i == 1:
            # sacca d'aria grigio-argento vicino alla base
            extra = ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="#f4f6f8" opacity=".95" clip-path="url(#CLIP)"/>'
                     % (cx - 34, yc - 30, cx - 10, yc - 56, cx + 22, yc - 40, cx + 40, yc - 26, cx + 6, yc - 6, cx - 30, yc - 6, cx - 34, yc - 30))
            extra += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="#fff" stroke-width="2" clip-path="url(#CLIP)"/>' % (cx - 22, yc - 32, cx - 6, yc - 46, cx + 14, yc - 38)
        elif i == 2:
            fl = 4
        elif i == 3:
            # alone rosso sotto la lamina (letto lesionato)
            extra = '<ellipse cx="%.1f" cy="%.1f" rx="30" ry="14" fill="#d9534f" opacity=".35" clip-path="url(#CLIP)"/>' % (cx + 2, yc - 66)
        f, p = nail(cx, yc, hw=36, nail_len=104, free_len=fl, plate=GELP, free=GELP, extra=extra, finger_len=34, shape='squoval' if i != 2 else 'quadrata')
        c = uid('rk')
        b += '<clipPath id="%s"><rect x="%d" y="56" width="205" height="214"/></clipPath><g clip-path="url(#%s)">%s</g>' % (c, x, c, f)
        ys = yc - 104
        if i == 0:
            crack = [(cx - 30, ys - 14), (cx - 18, ys - 6), (cx - 8, ys - 16), (cx + 4, ys - 4), (cx + 16, ys - 13), (cx + 30, ys - 6)]
            b += poly(crack, 'none', '#fff', 4.5, False, ' stroke-linejoin="round" opacity=".8"') + poly(crack, 'none', INK, 2.2, False, ' stroke-linejoin="round"')
            b += poly([(cx + 4, ys - 4), (cx + 8, ys + 8)], 'none', INK, 1.6, False)
        elif i == 1:
            b += leader(cx + 10, yc - 34, cx + 52, yc - 96, 'aria', 'start', 13, 700, MUTED)
        elif i == 2:
            jag = [(cx - 36, ys - 2), (cx - 24, ys - 9), (cx - 14, ys - 1), (cx - 2, ys - 10), (cx + 10, ys - 2), (cx + 22, ys - 9), (cx + 36, ys - 3)]
            b += poly(jag, 'none', NAIL_S, 2.2, False, ' stroke-linejoin="round"')
            # frammento staccato
            b += rot(-22, cx + 64, ys + 2, poly([(cx + 50, ys + 8), (cx + 58, ys - 2), (cx + 68, ys + 4), (cx + 78, ys - 4), (cx + 78, ys + 12), (cx + 52, ys + 16)], GELP, NAIL_S, 1.5))
        elif i == 3:
            crack = [(cx - 34, yc - 58), (cx - 18, yc - 74), (cx - 4, yc - 60), (cx + 12, yc - 78), (cx + 34, yc - 66)]
            b += poly(crack, 'none', '#fff', 4.5, False, ' stroke-linejoin="round" opacity=".8"') + poly(crack, 'none', INK, 2.4, False, ' stroke-linejoin="round"')
            b += ic_drop(cx + 2, yc - 30, 0.7, ERR, '#8e2a20')
        # freccia verso l'esito
        b += arr(cx, 274, cx, 290, col, 2.4)
        b += '<rect x="%d" y="294" width="181" height="52" rx="12" fill="%s" stroke="%s" stroke-width="1.8"/>' % (x + 12, bg, col)
        # icona dell'esito
        ix, iy = x + 38, 320
        b += '<circle cx="%d" cy="%d" r="14" fill="%s"/>' % (ix, iy, col)
        if kind == 'ok':
            b += '<path d="M%d,%d l4,4 l8,-9" stroke="#fff" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' % (ix - 6, iy)
        elif kind == 'redo':
            b += '<path d="M%d,%d A7,7 0 1 1 %d,%d" stroke="#fff" stroke-width="2.4" fill="none" stroke-linecap="round"/><path d="M%d,%d l1,-6 l5,4 Z" fill="#fff"/>' % (
                ix + 7, iy + 1, ix - 3, iy + 7, ix + 3, iy + 4)
        elif kind == 'cut':
            b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>' % (ix - 7, iy + 6, ix + 7, iy + 6)
            b += '<path d="M%d,%d l0,8 M%d,%d l-4,-4 M%d,%d l4,-4" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>' % (ix, iy - 7, ix, iy + 1, ix, iy + 1)
        else:
            b += '<path d="M%d,%d h8 M%d,%d v8" stroke="#fff" stroke-width="3.2" stroke-linecap="round"/>' % (ix - 4, iy, ix, iy - 4)
        for k, l in enumerate(out):
            b += text(x + 60, 325 + k * 17 - (8.5 if len(out) == 2 else 0), l, 14.5, 'start', 800, col)
    return svg(900, 370, defs() + b, 'Cosa si è rotto: crepa nel prodotto, sollevamento, rottura oltre il bordo libero, rottura nel letto ungueale')


@figx('riparazione-crepa.svg')
def repair_steps():
    b = title('Riparare una crepa')
    heads = ['Crepa', 'Lima finché sparisce', 'Ricostruisci', 'Rifinisci']
    caps = ['in zona di stress', 'anche la linea sottile', 'rifai l\'apex', 'e annota sulla scheda']
    for i in range(4):
        x = 20 + i * 218
        cx, yc = x + 103, 266
        extra = ''
        if i == 1:
            extra = '<ellipse cx="%.1f" cy="%.1f" rx="44" ry="26" fill="#f6dbe4" clip-path="url(#CLIP)"/>' % (cx, yc - 104)
            rng = random.Random(2)
            extra += '<g clip-path="url(#CLIP)">' + ''.join('<circle cx="%.1f" cy="%.1f" r="1.1" fill="#d7a9b8"/>' % (cx + rng.uniform(-38, 38), yc - 104 + rng.uniform(-20, 20)) for _ in range(60)) + '</g>'
        elif i == 2:
            extra = '<ellipse cx="%.1f" cy="%.1f" rx="46" ry="34" fill="%s" opacity=".85" clip-path="url(#CLIP)"/>' % (cx, yc - 104, PROD2)
        f, p = nail(cx, yc, hw=36, nail_len=100, free_len=40, plate=GELP, free=GELP, extra=extra, finger_len=26)
        body = f
        if i == 0:
            body += zigzag(cx - 30, yc - 104, 7, 9, 5)
            body += ring(cx, yc - 104, 40, ERR, 2.2, '4 3')
        elif i == 1:
            body += file_board(cx + 30, yc - 136, -14, 100, 14)
        elif i == 2:
            ox, oy = x + 116, 262
            mini = box(ox - 8, oy - 30, 82, 46, '#fff', '#d8c8c4', 8)
            mini += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="3" stroke-linecap="round"/>' % (ox, oy + 6, ox + 66, oy + 6, NAIL_S)
            mini += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="#6ea6c8" stroke-width="1.2"/>' % (
                ox + 2, oy + 5, ox + 20, oy - 14, ox + 34, oy - 14, ox + 50, oy - 14, ox + 66, oy + 2, ox + 66, oy + 6, PROD2)
            mini += arr(ox + 34, oy - 28, ox + 34, oy - 17, ACC2, 1.4)
            body += mini + text(ox + 2, oy - 17, 'apex', 12, 'start', 800, ACC2)
        else:
            body += gloss(cx, yc - 130, yc - 60, 5) + sparkle(cx + 18, yc - 120, 6)
            body += ic_doc(x + 172, 132, 0.9, True)
        b += frame(x, 55, 205, 260, heads[i], num=i + 1, ok=(True if i == 3 else None), body=body, cap=caps[i], capcol=INK, hsize=14.5)
    return svg(900, 330, defs() + b, 'Riparare una crepa: individua, lima finché sparisce, ricostruisci con apex, rifinisci e annota')


# ================================================================= MODULO 11 – PROBLEMI
Z_BASE, Z_SIDE, Z_TIP, Z_CEN = '#f39a3c', '#efcb2f', '#58aee0', '#8e5ccf'


def zone_badge(x, y, n, col):
    return ('<circle cx="%.1f" cy="%.1f" r="12" fill="%s" stroke="#fff" stroke-width="2"/>' % (x, y, col)
            + text(x, y + 5, str(n), 13.5, weight=800, fill='#fff'))


@figx('lifting-mappa.svg')
def lifting_map():
    b = title('Dove si stacca? Ecco perché')
    cx, yc, hw = 450, 300, 62
    nl, fl = 168, 46
    ys = yc - nl
    xs_ = [cx - hw - 6 + k * (2 * hw + 12) / 24.0 for k in range(25)]
    base_lo = [(px, cut_y(cx, yc, hw, px) + 4) for px in xs_]
    base_hi = [(px, cut_y(cx, yc, hw, px) - 30) for px in xs_]
    extra = '<g clip-path="url(#CLIP)">'
    extra += '<path d="M%s Z" fill="%s" opacity=".55"/>' % (' L'.join('%.1f,%.1f' % q for q in base_lo + base_hi[::-1]), Z_BASE)
    for sx in (-1, 1):
        x0 = cx - hw if sx < 0 else cx + hw - 14
        extra += '<rect x="%.1f" y="%.1f" width="14" height="%.1f" fill="%s" opacity=".6"/>' % (x0, ys - 10, yc - 60 - ys + 10, Z_SIDE)
    extra += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" opacity=".5"/>' % (cx - hw - 6, ys - fl - 20, 2 * hw + 12, fl + 26, Z_TIP)
    extra += '<ellipse cx="%.1f" cy="%.1f" rx="26" ry="19" fill="%s" opacity=".5"/>' % (cx + 4, yc - 100, Z_CEN)
    extra += '<ellipse cx="%.1f" cy="%.1f" rx="9" ry="5" fill="#fff" opacity=".7"/>' % (cx - 4, yc - 108)
    extra += '</g>'
    f, p = nail(cx, yc, hw=hw, nail_len=nl, free_len=fl, plate=GELP, free=GELP, extra=extra, finger_len=40)
    b += f
    b += zone_badge(cx - 20, yc - 26, 1, Z_BASE) + zone_badge(cx + hw - 7, yc - 150, 2, Z_SIDE) + zone_badge(cx - 6, ys - 20, 3, Z_TIP) + zone_badge(cx + 4, yc - 100, 4, Z_CEN)
    # richiami
    def callout(x, y, n, col, head, body, anchor):
        s = zone_badge(x, y - 5, n, col)
        tx = x + 20 if anchor == 'start' else x - 20
        s += text(tx, y, head, 15.5, anchor, 800, INK)
        s += text(tx, y + 20, body, 14, anchor, 400, INK)
        return s
    b += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="1.3"/>' % (cx - 34, yc - 26, 352, 262, MUTED)
    b += callout(340, 262, 1, Z_BASE, 'Base (cuticola)', 'preparazione, pelle, zona 3 spessa', 'end')
    b += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="1.3"/>' % (cx - 16, yc - 100, 352, 160, MUTED)
    b += callout(340, 160, 4, Z_CEN, 'Centro ("a tasca")', 'adesione, perla, botta', 'end')
    b += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="1.3"/>' % (cx + 10, ys - 20, 548, 98, MUTED)
    b += callout(560, 98, 3, Z_TIP, 'Punta (bordo libero)', 'bordo non sigillato, polvere', 'start')
    b += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="1.3"/>' % (cx + hw + 5, yc - 150, 548, 196, MUTED)
    b += callout(560, 196, 2, Z_SIDE, 'Lati (solchi)', 'prodotto nei solchi, limatura', 'start')
    # mani
    b += mini_hand(80, 352, 0.82, (0, 1, 2, 3, 4))
    b += text(124, 372, 'Tutte le dita =', 14.5, 'start', 800) + text(124, 391, 'tecnica / prodotto / lampada', 14, 'start', 600, MUTED)
    b += mini_hand(610, 352, 0.82, (0,))
    b += text(654, 372, '1–2 dita =', 14.5, 'start', 800) + text(654, 391, 'abitudini o struttura del dito', 13.5, 'start', 600, MUTED)
    return svg(900, 420, defs() + b, 'Mappa del sollevamento: base, lati, punta e centro con le cause tipiche; tutte le dita o solo una o due')


@figx('lifting-margine.svg')
def lifting_margin():
    b = title('Il margine dalla pelle')
    for i in range(2):
        ok = i == 0
        x = 20 + i * 245
        py = 196
        body = '<rect x="%d" y="%d" width="235" height="40" fill="%s"/>' % (x, py + 18, SKIN)
        body += '<rect x="%d" y="%d" width="235" height="8" fill="%s"/>' % (x, py + 12, BED)
        body += '<rect x="%d" y="%d" width="240" height="12" fill="%s" stroke="%s" stroke-width="1.2"/>' % (x - 2, py, PLATE_SEC, NAIL_S)
        fold = 'M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Z' % (x - 2, 136, x + 52, 136, x + 76, 140, x + 78, py, x - 2, py)
        if ok:
            pts = [(x + 90, py), (x + 120, py - 14), (x + 170, py - 26), (x + 240, py - 30)]
            body += product(pts, py, end_x=x + 240, end_y=py, fill=PROD2, stroke='#5f9cc0')
            body += '<path d="%s" fill="%s" stroke="%s" stroke-width="1.6"/>' % (fold, SKIN, SKIN_D)
            body += arr(x + 79, py - 8, x + 89, py - 8, DARK, 1.4, True)
            body += leader(x + 84, py - 10, x + 120, 122, '≈ 1 mm', 'start', 14)
        else:
            body += '<path d="%s" fill="%s" stroke="%s" stroke-width="1.6"/>' % (fold, SKIN, SKIN_D)
            pts = [(x + 50, 138), (x + 70, 136), (x + 84, 150), (x + 96, py - 18), (x + 130, py - 24), (x + 180, py - 28), (x + 240, py - 30)]
            body += '<path d="%s L%d,%d L%d,%d Q%d,%d %d,%d Z" fill="%s" stroke="#5f9cc0" stroke-width="1.6"/>' % (
                smooth_d(pts), x + 240, py, x + 78, py, x + 76, 140, x + 50, 138, PROD2)
            body += carr('M%d,%d Q%d,%d %d,%d' % (x + 30, 126, x + 54, 104, x + 80, 116), ERR, 2.2)
        cap = 'Margine libero' if ok else 'Prodotto sulla pelle'
        sub = 'aderisce bene, non tocca la pelle' if ok else 'fa leva quando la pelle si muove'
        b += frame(x, 55, 235, 275, None, ok=ok, body=body, cap=cap, sub=sub)
    # vista dall'alto
    x = 510
    cx, yc, hw = x + 117, 238, 44
    m = 7
    xs_ = [cx - hw + m + k * (2 * hw - 2 * m) / 20.0 for k in range(21)]
    bot = [(px, cut_y(cx, yc, hw, px) - m) for px in xs_]
    prod_d = 'M%.1f,%.1f L%s L%.1f,%.1f Z' % (cx - hw + m, yc - 300, ' L'.join('%.1f,%.1f' % q for q in bot), cx + hw - m, yc - 300)
    extra = '<path d="%s" fill="%s" opacity=".9" clip-path="url(#CLIP)"/>' % (prod_d, PROD2)
    extra += '<path d="%s" fill="none" stroke="%s" stroke-width="1.8" stroke-dasharray="5 4" clip-path="url(#CLIP)"/>' % (prod_d, ACC2)
    f, p = nail(cx, yc, hw=hw, nail_len=108, free_len=24, plate=NAIL, free=FREE, extra=extra, finger_len=30)
    body = f
    body += text(cx, 296, 'stessa distanza da', 13, weight=700, fill=ACC2) + text(cx, 313, 'cuticola e solchi', 13, weight=700, fill=ACC2)
    b += frame(x, 55, 235, 275, 'Margine anche sui lati', body=body, hsize=14.5)
    return svg(760, 345, defs() + b, 'Margine dalla pelle di circa 1 mm: corretto, prodotto sulla pelle, vista dall\'alto con margine uniforme')


@figx('rotture-mappa.svg')
def breaks_map():
    b = title('Dove si rompe?')
    cx, yc, hw = 170, 310, 54
    nl, fl = 150, 70
    ys = yc - nl
    f, p = nail(cx, yc, hw=hw, nail_len=nl, free_len=fl, plate=GELP, free='#f5cdd9', smile=8, finger_len=40)
    b += f
    b += zigzag(cx - 46, ys + 4, 10, 9, 5, ERR, 2.6)
    b += zigzag(cx + hw - 22, ys - 40, 2, 9, 6, ERR, 2.6)
    b += '<path d="M%.1f,%.1f l8,10 l10,-4 l8,8" fill="none" stroke="%s" stroke-width="2.6"/>' % (cx - 22, ys - fl + 2, ERR)
    b += zone_badge(cx - hw - 26, ys + 4, 1, ERR) + zone_badge(cx + hw + 24, ys - 40, 2, ERR) + zone_badge(cx + 40, ys - fl - 6, 3, ERR)
    b += text(cx, 380, 'vista dall\'alto', 13, fill=MUTED, style='italic')
    # profilo
    x0, y = 400, 196
    sec, fd, pp = section(x0, y, L=200, F=90, body_h=62)
    xs = pp['xs']
    b += sec
    thin = [(x0 + 8, y - 2), (x0 + 60, y - 10), (xs - 40, y - 12), (xs, y - 9), (xs + 50, y - 8), (xs + 92, y - 4)]
    b += product(thin, y, end_x=xs + 92, end_y=y + 6, fill=PROD, stroke=PROD_S)
    ideal = [(x0 + 8, y - 2), (x0 + 70, y - 28), (xs - 10, y - 46), (xs + 40, y - 36), (xs + 92, y - 8)]
    b += '<path d="%s" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="6 4"/>' % (smooth_d(ideal), OK)
    b += fd
    b += '<path d="M%.1f,%.1f l-5,6 l6,4 l-5,6" fill="none" stroke="%s" stroke-width="2.6"/>' % (xs + 2, y - 10, ERR)
    b += stress_tri(xs, y + 10)
    b += leader(xs - 10, y - 46, xs + 50, 100, 'qui serviva l\'apex', 'start', 14, fill=OK)
    b += leader(xs - 50, y - 10, x0 + 40, 118, 'zona 2 troppo sottile', 'middle', 14, fill=ERR)
    b += text(xs, y + 36, 'punto di stress', 12.5, weight=700, fill=ACC2)
    b += zone_badge(xs + 24, y - 24, 1, ERR)
    b += text(x0 + 150, y + 74, 'vista di profilo', 13, fill=MUTED, style='italic')
    # legenda
    lx, ly = 400, 296
    b += box(lx, ly - 22, 470, 96, PANEL, PANEL, 14)
    for k, l in enumerate(['Apex assente, basso o spostato', 'Lati troppo sottili / lunghezza eccessiva', 'Bordo non sigillato / trauma']):
        b += zone_badge(lx + 24, ly + k * 28 - 4, k + 1, ERR) + text(lx + 44, ly + k * 28 + 1, l, 14.5, 'start', 600)
    return svg(900, 390, defs() + b, 'Dove si rompe l\'unghia: crepa in zona di stress, angolo laterale, punta; profilo con zona 2 sottile e apex mancante')


@figx('picco-calore-cause.svg')
def heat_causes():
    b = title('Perché scotta?')
    # 1 spessore
    x = 20
    body = ''
    for k, (ok, th, lvl, col, lab) in enumerate([(True, 6, .2, OK, 'Strato sottile'), (False, 24, .9, ERR, 'Strato spesso')]):
        yy = 150 + k * 92
        body += '<rect x="%d" y="%d" width="170" height="10" fill="%s" stroke="%s"/>' % (x + 30, yy, PLATE_SEC, NAIL_S)
        body += '<rect x="%d" y="%d" width="170" height="14" fill="%s"/>' % (x + 30, yy + 10, BED)
        body += '<path d="M%d,%d Q%d,%d %d,%d L%d,%d Z" fill="#f3a9bd" stroke="%s"/>' % (x + 36, yy, x + 110, yy - 2 * th, x + 196, yy, x + 36, yy, NAIL_S)
        body += ic_thermo(x + 232, yy - 6, lvl, col)
        body += mark(x + 266, yy - 18, ok, 11)
        body += text(x + 115, yy + 44, lab, 14, weight=800, fill=col)
    b += frame(x, 55, 285, 290, 'Spessore', num=1, body=body)
    # 2 lamina
    x = 317
    body = ''
    for k, (thin, lab, col) in enumerate([(False, 'Lamina normale', OK), (True, 'Lamina assottigliata', ERR)]):
        yy = 150 + k * 92
        h = 4 if thin else 12
        L0, L1 = x + 30, x + 210
        body += '<rect x="%d" y="%d" width="%d" height="16" fill="%s"/>' % (L0, yy + 12, L1 - L0, BED)
        body += '<rect x="%d" y="%d" width="%d" height="%d" fill="%s" stroke="%s"/>' % (L0, yy + 12 - h, L1 - L0, h, PLATE_SEC, NAIL_S)
        body += '<rect x="%d" y="%d" width="%d" height="10" fill="#f3a9bd" stroke="%s"/>' % (L0, yy + 2 - h, L1 - L0, NAIL_S)
        if k == 0:
            body += text(L1 + 6, yy + 1 - h + 8, 'gel', 12, 'start', 600, MUTED)
            body += text(L1 + 6, yy + 12 - h / 2 + 4, 'lamina', 12, 'start', 600, MUTED)
            body += text(L1 + 6, yy + 26, 'letto', 12, 'start', 600, MUTED)
        for w in range(4):
            wx = L0 + 30 + w * 40
            end = yy + 26 if thin else yy + 2 - h
            body += carr('M%d,%d C%d,%d %d,%d %d,%d' % (wx, yy - 30 - h, wx + 6, yy - 22 - h, wx - 6, end - 10, wx, end), ERR if thin else WARN, 1.8)
        body += text(x + 130, yy + 50, lab, 14, weight=800, fill=col)
    body += text(x + 132, 318, 'frecce = calore che arriva al letto', 12.5, weight=600, fill=MUTED, style='italic')
    b += frame(x, 55, 285, 290, 'Lamina', num=2, body=body)
    # 3 grafico
    x = 614
    body = ''
    ox, oy = x + 46, 270
    body += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.5"/><line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.5"/>' % (
        ox, oy, ox + 210, oy, INK, ox, oy, ox, 96, INK)
    body += text(ox + 105, oy + 20, 'tempo in lampada', 12.5, fill=MUTED)
    body += '<text x="%d" y="%d" font-size="12.5" fill="%s" transform="rotate(-90 %d %d)" text-anchor="middle">temperatura</text>' % (ox - 12, 185, MUTED, ox - 12, 185)
    body += dashed(ox, 136, ox + 210, 136, ERR, 1.6)
    body += text(ox + 208, 129, '≈ 46 °C: dolore', 12.5, 'end', 800, ERR)
    body += '<path d="M%d,%d C%d,%d %d,%d %d,%d C%d,%d %d,%d %d,%d" fill="none" stroke="%s" stroke-width="3"/>' % (
        ox, oy - 4, ox + 18, 110, ox + 34, 100, ox + 48, 104, ox + 70, 120, ox + 110, 210, ox + 200, 236, ERR)
    body += '<path d="M%d,%d C%d,%d %d,%d %d,%d" fill="none" stroke="%s" stroke-width="3"/>' % (ox, oy - 4, ox + 60, 180, ox + 140, 170, ox + 200, 196, OK)
    body += text(ox + 74, 100, 'lampada troppo veloce', 12.5, 'start', 700, ERR)
    body += text(ox + 150, 166, 'adatta', 12.5, 'start', 700, OK)
    body += text(x + 142, 318, 'Flash and pull: togli la mano', 13, weight=700, fill=INK)
    body += text(x + 142, 335, 'qualche secondo', 13, weight=700, fill=INK)
    b += frame(x, 55, 266, 290, 'Lampada e gel', num=3, body=body)
    return svg(900, 360, defs() + b, 'Cause del picco di calore: strato spesso, lamina assottigliata, lampada troppo veloce o gel non abbinato')


@figx('grinze-sezione.svg')
def wrinkles():
    b = title('Perché si formano le grinze')
    V = '#9a6be0'
    for i in range(2):
        ok = i == 1
        x = 20 + i * 370
        body = ''
        L0, L1 = x + 22, x + 262
        lcx = (L0 + L1) / 2
        body += '<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Z" fill="#f4f1f8" stroke="#8a7d9e" stroke-width="2"/>' % (
            lcx - 112, 112, lcx - 112, 96, lcx, 74, lcx + 112, 96, lcx + 112, 112)
        for k in range(5):
            body += '<rect x="%d" y="108" width="16" height="6" rx="2" fill="%s"/>' % (lcx - 88 + k * 40, V)
        body += text(lcx, 96, 'lampada', 12.5, weight=700, fill='#6b4fa0')
        py = 250
        body += '<rect x="%d" y="%d" width="%d" height="14" fill="%s" stroke="%s"/>' % (L0, py, L1 - L0, PLATE_SEC, NAIL_S)
        body += '<rect x="%d" y="%d" width="%d" height="14" fill="%s"/>' % (L0, py + 14, L1 - L0, BED)
        body += text(L1 + 8, py + 11, 'lamina', 12.5, 'start', 600, MUTED)
        rays = [L0 + 24 + k * 48 for k in range(5)]
        if not ok:
            top = py - 80
            body += '<rect x="%d" y="%d" width="%d" height="%d" fill="#c2577a"/>' % (L0, top, L1 - L0, 26)
            body += '<rect x="%d" y="%d" width="%d" height="%d" fill="#eab3c5"/>' % (L0, top + 26, L1 - L0, py - top - 26)
            rng = random.Random(11)
            for k in range(60):
                body += '<circle cx="%.1f" cy="%.1f" r="1.8" fill="#fff" opacity=".9"/>' % (L0 + 6 + rng.uniform(0, L1 - L0 - 12), top + 34 + rng.uniform(0, 40))
            wav = ' '.join('q7.5,-6 15,0' for _ in range(16))
            body += '<path d="M%d,%d %s" fill="none" stroke="%s" stroke-width="3"/>' % (L0, top, wav, INK)
            for rx in rays:
                body += carr('M%d,%d L%d,%d' % (rx, 120, rx, top - 4), V, 2.4)
                body += '<path d="M%d,%d a8,7 0 0 1 16,0 Z" fill="%s"/><line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.5"/>' % (
                    rx - 8, top + 15, INK, rx, top + 15, rx, top + 22, INK)
            body += mtext(L1 + 8, top + 8, ['superficie', 'dura'], 13, 'start', 700, INK)
            body += mtext(L1 + 8, top + 50, ['gel ancora', 'liquido'], 13, 'start', 700, ERR)
            body += text(L0 + 6, top + 22, '', 12)
        else:
            t1 = py - 28
            t2 = t1 - 28
            body += '<rect x="%d" y="%d" width="%d" height="28" fill="#c2577a"/>' % (L0, t1, L1 - L0)
            body += '<rect x="%d" y="%d" width="%d" height="28" fill="#cf6a8b"/>' % (L0, t2, L1 - L0)
            body += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#fff" stroke-width="1.5" stroke-dasharray="4 3"/>' % (L0, t1, L1, t1)
            for rx in rays:
                body += carr('M%d,%d L%d,%d' % (rx, 120, rx, py - 3), V, 2.4)
            body += text(L1 + 8, t2 + 19, 'strato 2', 12.5, 'start', 700, INK)
            body += text(L1 + 8, t1 + 19, 'strato 1', 12.5, 'start', 700, INK)
        cap = 'Strati sottili: la luce arriva in fondo' if ok else 'Strato spesso: i pigmenti fanno ombra'
        b += frame(x, 55, 350, 270, None, ok=ok, body=body, cap=cap)
    b += text(380, 345, 'Ogni strato sottile si polimerizza prima di stendere il successivo.', 13.5, fill=MUTED)
    return svg(760, 355, defs() + b, 'Grinze: in uno strato spesso i pigmenti fermano la luce, la superficie indurisce e sotto resta gel liquido; con strati sottili la luce arriva in fondo')


@figx('ingiallimento-cause.svg')
def yellowing():
    b = title('Ingiallimento: le cause')
    groups = [(20, 'Subito → prodotto / lampada', ACC2, [
        (lambda x, y: ic_lamp(x, y + 3, 0.78, True), 'Lampada non abbinata'),
        (lambda x, y: ic_bottle(x - 3, y, 0.85, '#f4f1ec', INK) + ic_stopwatch(x + 10, y + 9, 0.5), 'Top non polimerizzato'),
        (lambda x, y: ic_brush_dirty(x + 4, y, 1.0), 'Pennello contaminato')]),
        (590, 'Dopo settimane → abitudini', WARN, [
            (lambda x, y: ic_sun(x, y, 0.95), 'Sole / lettini'),
            (lambda x, y: ic_cig(x + 4, y + 4, 0.95), 'Fumo'),
            (lambda x, y: ic_bottle(x, y, 0.85, '#7fb3d5', '#4f86a8'), 'Detersivi e creme')])]
    for gx, head, col, items in groups:
        b += card(gx, 58, 290, 266, accent=col, ah=40)
        b += text(gx + 145, 84, head, 15, weight=800, fill='#fff')
        for k, (ic, lab) in enumerate(items):
            yy = 128 + k * 66
            b += '<circle cx="%d" cy="%d" r="25" fill="%s"/>' % (gx + 46, yy, PANEL) + ic(gx + 46, yy)
            b += text(gx + 84, yy + 5.5, lab, 15, 'start', 700)
            if k < 2:
                b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#f0e4e1" stroke-width="1.2"/>' % (gx + 20, yy + 33, gx + 270, yy + 33)
    # al centro: prima e dopo
    for k, (cx, plate, free, lab, sub) in enumerate([(392, '#f7c9d6', '#fbe3ea', 'appena fatta', 'trasparente, rosata'),
                                                       (508, '#ecd58a', '#f2e2a6', 'ingiallita', 'tono giallo, opaco')]):
        f, p = nail(cx, 222, hw=34, nail_len=96, free_len=34, plate=plate, free=free, finger_len=56)
        c = uid('yc')
        b += '<clipPath id="%s"><rect x="%d" y="70" width="110" height="200"/></clipPath><g clip-path="url(#%s)">%s</g>' % (c, cx - 55, c, f)
        b += text(cx, 294, lab, 14.5, weight=800, fill=INK if k == 0 else WARN) + text(cx, 312, sub, 12.5, fill=MUTED)
    return svg(900, 336, defs() + b, 'Cause dell\'ingiallimento: lampada, top non polimerizzato, pennello contaminato, sole, fumo, detersivi e creme')


@figx('diagnosi-flusso.svg')
def diag_flow():
    b = title('Diagnosi in 5 domande')
    b += text(880, 38, 'nell\'ordine, prima di correggere', 13.5, 'end', 600, MUTED, 'italic')
    qs = [(['Dove?'], ['base', 'lati', 'punta']), (['Quante dita?'], ['tutte', 'o 1–2']), (['Quando?'], ['subito', 'o dopo']),
          (['Cosa ho fatto?'], ['rileggi la scheda']), (['Cosa ha fatto', 'la cliente?'], ['abitudini', 'traumi'])]
    cw, gap, y0, ch = 154, 21, 62, 228
    for k, (q, chips) in enumerate(qs):
        x = 20 + k * (cw + gap)
        cx = x + cw / 2
        b += card(x, y0, cw, ch, accent=ACC2, ah=5)
        b += badge(x + 22, y0 + 26, k + 1, ACC2, 13, 14)
        # icona
        iy = y0 + 72
        b += '<circle cx="%.1f" cy="%.1f" r="34" fill="%s"/>' % (cx, iy, PANEL)
        if k == 0:
            f, p = nail(0, 0, hw=15, nail_len=40, free_len=14, plate=GELP, free=GELP, finger_len=14, extra=(
                '<path d="M-22,-3 Q0,6 22,-3 L22,-14 Q0,-6 -22,-14 Z" fill="%s" opacity=".85" clip-path="url(#CLIP)"/>' % Z_BASE
                + '<rect x="-16" y="-40" width="6" height="30" fill="%s" opacity=".85" clip-path="url(#CLIP)"/>' % Z_SIDE
                + '<rect x="10" y="-40" width="6" height="30" fill="%s" opacity=".85" clip-path="url(#CLIP)"/>' % Z_SIDE
                + '<rect x="-20" y="-60" width="40" height="14" fill="%s" opacity=".8" clip-path="url(#CLIP)"/>' % Z_TIP))
            ic = uid('ic')
            b += '<clipPath id="%s"><circle cx="%.1f" cy="%.1f" r="34"/></clipPath>' % (ic, cx, iy)
            b += '<g clip-path="url(#%s)"><g transform="translate(%.1f,%.1f)">%s</g></g>' % (ic, cx, iy + 30, f)
        elif k == 1:
            b += mini_hand(cx + 1, iy - 6, 0.48, (0, 1, 2, 3, 4))
        elif k == 2:
            b += ic_calendar(cx - 6, iy + 2, 1.05) + ic_clock(cx + 14, iy + 13, 1.0)
        elif k == 3:
            b += ic_doc(cx, iy, 1.1, True)
        else:
            b += ic_house(cx, iy + 1, 1.15)
        # domanda
        ty = y0 + 136
        for j, l in enumerate(q):
            b += text(cx, ty + j * 19, l, 16, weight=800)
        # risposte tipiche come etichette
        cy = y0 + ch - 54
        if len(chips) == 3:
            ws = [46, 40, 48]
            xx = cx - (sum(ws) + 8) / 2
            for j, c in enumerate(chips):
                b += pill(xx, cy + 6, ws[j], 22, c, ('#fde3c8', '#fbf0b8', '#d7ecf8')[j], INK, 12.5, 700)
                xx += ws[j] + 4
        elif len(chips) == 1:
            b += pill(cx - 64, cy + 6, 128, 22, chips[0], '#f6eef0', ACC2, 12.5, 700)
        else:
            b += pill(cx - 56, cy - 6, 112, 22, chips[0], '#f6eef0', ACC2, 12.5, 700)
            b += pill(cx - 56, cy + 20, 112, 22, chips[1], '#f6eef0', ACC2, 12.5, 700)
        if k < 4:
            ax = x + cw + gap / 2
            b += '<circle cx="%.1f" cy="%.1f" r="11" fill="#fff" stroke="%s" stroke-width="1.5"/>' % (ax, iy, ACC2)
            b += '<path d="M%.1f,%.1f l5,5 l-5,5" fill="none" stroke="%s" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>' % (ax - 2, iy - 5, ACC2)
    # conclusione
    b += '<rect x="230" y="306" width="440" height="36" rx="18" fill="%s" stroke="%s" stroke-width="1.4"/>' % (YEL_BG, YEL_S)
    b += '<circle cx="252" cy="324" r="10" fill="%s"/>' % WARN + text(252, 329, '!', 14, weight=900, fill='#fff')
    b += text(460, 329.5, 'Poi: una correzione alla volta', 15, weight=800, fill='#7a5a12')
    return svg(900, 356, defs() + b, 'Le cinque domande della diagnosi: dove, quante dita, quando, cosa ho fatto, cosa ha fatto la cliente')


@figx('diagnosi-scheda.svg')
def diag_card():
    b = title('Annota il difetto')
    cols = [('Data', 64), ('Dito', 100), ('Dove', 140), ('Quando', 116), ('Causa probabile', 196), ('Correzione', 184)]
    x0, y0 = 20, 62
    W = sum(w for _, w in cols)
    b += '<rect x="%d" y="%d" width="%d" height="150" rx="12" fill="#fff" stroke="#e5d6d2" stroke-width="2"/>' % (x0, y0, W)
    b += '<path d="M%d,%d h%d v38 h-%d Z" fill="%s"/>' % (x0, y0 + 12, W, W, ACC) + '<rect x="%d" y="%d" width="%d" height="20" rx="12" fill="%s"/>' % (x0, y0, W, ACC)
    rows = [['12/3', 'Pollice dx', 'Zona di stress', '2 settimane', 'Apex basso', 'Apex più alto'],
            ['12/3', 'Tutte', 'Base', '3 giorni', 'Cuticola sulla lamina', 'Preparazione']]
    xx = x0
    for k, (h, w) in enumerate(cols):
        b += text(xx + 10, y0 + 31, h, 14.5, 'start', 800, '#fff')
        for r, row in enumerate(rows):
            b += text(xx + 10, y0 + 80 + r * 46, row[k], 14.5, 'start', 600, '#3f5a8a', 'italic')
        if k:
            b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#efe3df" stroke-width="1.5"/>' % (xx, y0 + 50, xx, y0 + 150)
        xx += w
    b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#efe3df" stroke-width="1.5"/>' % (x0, y0 + 104, x0 + W, y0 + 104)
    b += ic_camera(60, 262, 1.1)
    b += text(92, 268, '+ foto dall\'alto e di profilo, alla fine del servizio e al refill', 15, 'start', 700)
    return svg(860, 300, defs() + b, 'Esempio di registro dei difetti: data, dito, dove, quando, causa probabile e correzione, con foto')


# ================================================================= MODULO 12 – PROFESSIONE
@figx('consulenza-flusso.svg')
def consult_flow():
    b = title('La consulenza in 5 fasi')
    steps = [(ic_doc, dict(pen=True), ['Informativa', 'e consensi']), (ic_heart, {}, ['Domande', 'sulla salute']),
             (ic_lens, {}, ['Osserva unghie', 'e pelle']), (ic_bubble, {}, ['Abitudini', 'e desideri']),
             (ic_calendar, {}, ['Accordo: servizio,', 'prezzo, refill'])]
    shades = ['#e7a3b9', '#da88a3', '#c96b8c', '#b05276', '#8e3b5a']
    cw, gap = 180, 10
    for k, (fn, kw, lab) in enumerate(steps):
        x = 20 + k * (cw + gap)
        cx = x + cw / 2
        # barra a frecce con il numero di fase
        b += chevron(x, 58, cw + (gap if k < 4 else 0), 34, shades[k], first=(k == 0))
        b += text(cx + 4, 80.5, 'FASE %d' % (k + 1), 13, weight=800, fill='#fff')
        # scheda
        b += card(x, 104, cw - 6 if k < 4 else cw, 126)
        b += '<circle cx="%.1f" cy="146" r="28" fill="%s"/>' % (cx - 3, PANEL) + fn(cx - 3, 146, 1.1, **kw)
        b += text(cx - 3, 196, lab[0], 14.5, weight=800) + text(cx - 3, 214, lab[1], 14.5, weight=800)
    # ramo di arresto dalla fase 3
    x3 = 20 + 2 * (cw + gap) + cw / 2 - 3
    b += arr(x3, 232, x3, 258, ERR, 2.4)
    b += '<rect x="%.1f" y="262" width="250" height="40" rx="20" fill="%s" stroke="%s" stroke-width="1.6"/>' % (x3 - 125, RED_BG, ERR)
    oct_ = [(x3 - 100 + 18 * math.cos(math.radians(22.5 + k * 45)), 282 + 18 * math.sin(math.radians(22.5 + k * 45))) for k in range(8)]
    b += poly(oct_, ERR, '#fff', 2) + text(x3 - 100, 286.5, 'STOP', 12, weight=900, fill='#fff')
    b += text(x3 + 10, 287.5, 'STOP → medico', 16, weight=800, fill=ERR)
    b += text(x3 + 140, 280, 'se ci sono', 14, 'start', 700, ERR) + text(x3 + 140, 297, 'controindicazioni', 14, 'start', 700, ERR)
    b += text(x3 - 140, 280, 'il servizio', 13.5, 'end', 600, MUTED, 'italic') + text(x3 - 140, 297, 'non si fa', 13.5, 'end', 600, MUTED, 'italic')
    return svg(1000, 316, defs() + b, 'La consulenza in cinque fasi: informativa e consensi, salute, osservazione, abitudini e desideri, accordo; stop in caso di controindicazioni')


@figx('consensi-separati.svg')
def consents():
    b = title('Informativa e consensi separati')
    sheets = [('Informativa privacy', 'da consegnare e far leggere', 'OBBLIGATORIA', ACC2, ic_doc),
              ('Dati sulla salute', 'allergie, farmaci, gravidanza', 'CONSENSO', ACC, ic_heart),
              ('Foto e social', 'consenso facoltativo', 'FACOLTATIVO', '#7a6369', ic_camera)]

    def cbox(x, y, label, checked=False):
        s = '<rect x="%d" y="%d" width="18" height="18" rx="4" fill="%s" stroke="%s" stroke-width="2"/>' % (x, y - 14, ACC2 if checked else '#fff', ACC2)
        if checked:
            s += '<path d="M%d,%d l4,4 l7,-8" stroke="#fff" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' % (x + 4, y - 5)
        return s + text(x + 27, y, label, 15, 'start', 700)

    for k, (t, sub, tag, col, ic) in enumerate(sheets):
        x = 24 + k * 292
        w, y0, h = 262, 60, 216
        # foglio con angolo piegato
        b += ('<path d="M%d,%d L%d,%d L%d,%d L%d,%d L%d,%d Z" fill="#fff" stroke="#e0d2ce" stroke-width="1.5" stroke-linejoin="round" filter="url(#cSh)"/>'
              % (x, y0, x + w - 22, y0, x + w, y0 + 22, x + w, y0 + h, x, y0 + h))
        b += '<path d="M%d,%d L%d,%d L%d,%d Z" fill="#f3ebe8" stroke="#e0d2ce" stroke-width="1.5" stroke-linejoin="round"/>' % (x + w - 22, y0, x + w - 22, y0 + 22, x + w, y0 + 22)
        b += '<rect x="%d" y="%d" width="5" height="%d" fill="%s"/>' % (x, y0 + 14, 50, col)
        b += '<circle cx="%d" cy="%d" r="19" fill="%s"/>' % (x + 34, y0 + 38, PANEL) + ic(x + 34, y0 + 38, 0.72)
        b += text(x + 62, y0 + 34, t, 16.5, 'start', 800, ACC2)
        b += text(x + 62, y0 + 53, sub, 13, 'start', 400, MUTED, 'italic')
        b += pill(x + 18, y0 + 72, len(tag) * 8.6 + 18, 20, tag, '#f6eef0', col, 12, 800)
        for j in range(2):
            b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#efe6e3" stroke-width="2"/>' % (x + 18, y0 + 110 + j * 12, x + w - 24 - j * 50, y0 + 110 + j * 12)
        if k == 0:
            b += cbox(x + 18, y0 + 160, 'Ricevuta', True)
        else:
            b += text(x + 18, y0 + 142, 'Acconsento:', 13, 'start', 600, MUTED)
            b += cbox(x + 18, y0 + 166, 'Sì', k == 1) + cbox(x + 92, y0 + 166, 'No')
        b += '<path d="M%d,%d c8,-10 14,6 22,-4 s10,-6 16,2" stroke="%s" stroke-width="1.6" fill="none" opacity=".75"/>' % (x + 70, y0 + 194, '#3f5a8a')
        b += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.3"/>' % (x + 18, y0 + 200, x + w - 18, y0 + 200, MUTED)
        b += text(x + 18, y0 + 196, 'Firma', 12, 'start', 600, MUTED)
    b += '<rect x="608" y="290" width="282" height="36" rx="18" fill="%s" stroke="%s" stroke-width="1.4"/>' % (GREEN_BG, OK)
    b += mark(628, 308, True, 10) + text(758, 313, 'Il no non blocca il servizio', 13.5, weight=800, fill=OK)
    b += text(24, 313, 'Tre fogli distinti: ogni consenso si firma a parte.', 13.5, 'start', 600, MUTED, 'italic')
    return svg(900, 340, defs() + b, 'Informativa privacy e due consensi separati: dati sulla salute, foto e social (facoltativo)')


@figx('aftercare-si-no.svg')
def aftercare_yn():
    b = title('Dopo il servizio')
    yes = [(ic_drop, 'Olio ogni giorno', 'cuticole elastiche, meno lifting'), (ic_glove, 'Guanti per le pulizie', 'acqua e detersivi indeboliscono'),
           (ic_calendar, 'Refill puntuale', 'ogni 3–4 settimane'), (ic_phone, 'Chiama se si stacca', 'non riparare da sola')]
    no = [(ic_can, 'Unghie come attrezzi'), (ic_teeth, 'Mordere, "pizzicare"'), (ic_glue, 'Colla'), (ic_plaster, 'Cerotto'), (ic_bottle, 'Solventi, acetone')]
    # colonna Sì
    b += card(20, 56, 420, 296, accent=OK, ah=44)
    b += '<circle cx="48" cy="78" r="12" fill="#fff"/><path d="M42,78 l4,4 l8,-9" stroke="%s" stroke-width="2.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' % OK
    b += text(70, 85, 'Sì', 19, 'start', 800, '#fff')
    for k, (fn, l, sub) in enumerate(yes):
        y = 132 + k * 60
        b += '<circle cx="64" cy="%d" r="24" fill="%s"/>' % (y, GREEN_BG) + fn(64, y, 0.92)
        b += text(102, y - 2, l, 15.5, 'start', 800) + text(102, y + 17, sub, 13, 'start', 400, MUTED)
        if k < 3:
            b += '<line x1="40" y1="%d" x2="420" y2="%d" stroke="#eef3ef" stroke-width="1.2"/>' % (y + 30, y + 30)
    # colonna No
    b += card(460, 56, 420, 296, accent=ERR, ah=44)
    b += '<circle cx="488" cy="78" r="12" fill="#fff"/><path d="M483,73 l10,10 M493,73 l-10,10" stroke="%s" stroke-width="2.8" stroke-linecap="round"/>' % ERR
    b += text(510, 85, 'No', 19, 'start', 800, '#fff')
    for k, (fn, l) in enumerate(no):
        y = 126 + k * 47
        b += '<circle cx="504" cy="%d" r="20" fill="%s"/>' % (y, RED_BG) + fn(504, y, 0.74) + no_sign(504, y, 20, 2.6)
        b += text(540, y + 5.5, l, 15.5, 'start', 700)
    return svg(900, 368, defs() + b, 'Consigli dopo il servizio: cosa fare (olio, guanti, refill, chiamare) e cosa evitare (attrezzi, mordere, colla, cerotto, solventi)')


@figx('aftercare-cartoncino.svg')
def aftercare_card():
    b = title('Il biglietto post-trattamento')
    for k in range(2):
        x = 30 + k * 365
        b += card(x, 62, 335, 210, rx=14, accent=ACC if k == 0 else None, ah=6)
        b += text(x + 167, 292, 'Fronte' if k == 0 else 'Retro', 13.5, weight=700, fill=MUTED)
    x = 30
    b += '<circle cx="%d" cy="112" r="28" fill="#e9e4e6"/>' % (x + 60) + text(x + 60, 117, 'logo', 13, weight=700, fill=MUTED)
    b += text(x + 104, 108, 'Il tuo prossimo', 17, 'start', 800, ACC2) + text(x + 104, 129, 'appuntamento', 17, 'start', 800, ACC2)
    b += text(x + 30, 190, 'Data', 15, 'start', 700) + '<line x1="%d" y1="192" x2="%d" y2="192" stroke="%s" stroke-width="1.5"/>' % (x + 72, x + 180, MUTED)
    b += text(x + 194, 190, 'Ora', 15, 'start', 700) + '<line x1="%d" y1="192" x2="%d" y2="192" stroke="%s" stroke-width="1.5"/>' % (x + 228, x + 305, MUTED)
    b += ic_calendar(x + 290, 240, 0.9)
    x = 395
    b += text(x + 24, 96, 'I miei 3 consigli per te:', 16, 'start', 800, ACC2)
    for j, l in enumerate(['1. Olio ogni giorno', '2. Guanti per le pulizie', '3. Non usarle come attrezzi']):
        b += text(x + 30, 130 + j * 28, l, 15, 'start', 600)
    b += '<rect x="%d" y="222" width="295" height="32" rx="8" fill="%s"/>' % (x + 20, YEL_BG)
    b += text(x + 167, 243, 'Se qualcosa si stacca, chiamami', 14.5, weight=800, fill='#7a5a12')
    return svg(760, 310, defs() + b, 'Biglietto post-trattamento: fronte con il prossimo appuntamento, retro con tre consigli')


@figx('calcolo-prezzo.svg')
def price_calc():
    b = title('Come nasce il prezzo')
    b += text(880, 38, 'si somma dal basso verso l\'alto', 13.5, 'end', 600, MUTED, 'italic')
    # dal basso: materiali, tempo, spese fisse, margine
    blocks = [('Margine', 'il tuo guadagno per crescere', 56, '#c9b6e4', '#6b4fa0'),
              ('Spese fisse', 'affitto, utenze, assicurazione', 56, '#f6d38a', '#8a6410'),
              ('Tempo × valore orario', 'minuti reali × €/ora', 82, '#e98fae', ACC2),
              ('Materiali', 'prodotti e monouso', 56, '#9cc3d8', '#2f6a8c')]
    x0, w, y = 60, 300, 62
    tops = []
    for k, (l, sub, h, col, dk) in enumerate(blocks):
        b += '<rect x="%d" y="%d" width="%d" height="%d" rx="10" fill="%s" filter="url(#nxShS)"/>' % (x0, y, w, h - 6, col)
        # icona del blocco
        ix, iy = x0 + 26, y + (h - 6) / 2
        b += '<circle cx="%d" cy="%.1f" r="15" fill="#fff" opacity=".9"/>' % (ix, iy)
        if k == 0:
            b += '<path d="M%d,%.1f l7,-8 l5,5 l8,-10" fill="none" stroke="%s" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>' % (ix - 10, iy + 6, dk)
        elif k == 1:
            b += ic_house(ix, iy + 1, 0.62, dk)
        elif k == 2:
            b += ic_stopwatch(ix, iy, 0.7, dk)
        else:
            b += polish_bottle(ix, iy + 13, 0.42, '#5d9cc3', '#2f6a8c')
        tx = x0 + 52
        b += text(tx, iy - 1, l, 16, 'start', 800, INK) + text(tx, iy + 17, sub, 13, 'start', 600, dk)
        tops.append(y)
        y += h
    ybot = y - 6
    # parentesi graffa a destra della colonna
    bx = x0 + w + 14
    mid = (62 + ybot) / 2
    b += '<path d="M%d,62 Q%d,62 %d,74 L%d,%.1f Q%d,%.1f %d,%.1f Q%d,%.1f %d,%.1f L%d,%.1f Q%d,%.1f %d,%.1f" fill="none" stroke="%s" stroke-width="2.4" stroke-linecap="round"/>' % (
        bx, bx + 10, bx + 10, bx + 10, mid - 12, bx + 10, mid, bx + 22, mid, bx + 10, mid, bx + 10, mid + 12,
        bx + 10, ybot - 12, bx + 10, ybot, bx, ybot, MUTED)
    # cartellino del prezzo
    tx0, ty = 430, mid
    b += '<path d="M%d,%.1f L%d,%.1f L%d,%.1f Q%d,%.1f %d,%.1f L%d,%.1f Q%d,%.1f %d,%.1f L%d,%.1f Z" fill="%s" filter="url(#nxShS)"/>' % (
        tx0, ty, tx0 + 34, ty - 40, tx0 + 170, ty - 40, tx0 + 180, ty - 40, tx0 + 180, ty - 30, tx0 + 180, ty + 30, tx0 + 180, ty + 40,
        tx0 + 170, ty + 40, tx0 + 34, ty + 40, ACC2)
    b += '<circle cx="%d" cy="%.1f" r="7" fill="#fff"/>' % (tx0 + 28, ty)
    b += text(tx0 + 106, ty - 6, 'Prezzo', 22, weight=800, fill='#fff') + text(tx0 + 106, ty + 16, 'del servizio', 13, weight=600, fill='#f6d9e3')
    b += text(bx + 40, ty + 10, '=', 30, weight=800, fill=ACC2)
    # confronto con la zona
    b += arr(620, ty, 650, ty, DARK, 2)
    b += card(658, ty - 74, 222, 148)
    b += '<circle cx="769" cy="%.1f" r="28" fill="%s"/>' % (ty - 30, PANEL) + ic_map(769, ty - 30, 1.15)
    b += text(769, ty + 22, 'Poi confronta con', 15, weight=800) + text(769, ty + 42, 'i prezzi della tua zona', 15, weight=800)
    return svg(900, 318, defs() + b, 'Come nasce il prezzo: materiali, tempo per valore orario, spese fisse e margine; poi confronto con la zona')


@figx('agenda-tempi.svg')
def agenda():
    b = title('Un appuntamento in agenda')
    x0, w_min = 36, 7.0   # px per minuto
    segs = [(['Consulenza'], 15, '#c9b6e4'), (['Servizio'], 75, '#e98fae'), (['Consigli', '+ refill'], 10, '#f6d38a'), (['Pulizia e', 'sterilizzazione'], 15, '#9cc3d8')]

    def bar(y, segs):
        c = uid('ag')
        tot = sum(m for _, m, _ in segs) * w_min
        s = '<rect x="%.1f" y="%d" width="%.1f" height="46" rx="10" fill="#fff" filter="url(#cSh)"/>' % (x0, y, tot)
        s += '<clipPath id="%s"><rect x="%.1f" y="%d" width="%.1f" height="46" rx="10"/></clipPath><g clip-path="url(#%s)">' % (c, x0, y, tot, c)
        x = x0
        for l, m, col in segs:
            w = m * w_min
            s += '<rect x="%.1f" y="%d" width="%.1f" height="46" fill="%s" stroke="#fff" stroke-width="3"/>' % (x, y, w, col)
            fs = 14 if len(l) == 1 else 12.5
            y0 = y + 28 if len(l) == 1 else y + 20
            s += mtext(x + w / 2, y0, l, fs, weight=800, lh=1.2)
            x += w
        return s + '</g>'
    for k in range(5):
        tx = x0 + k * 30 * w_min
        b += '<line x1="%.1f" y1="88" x2="%.1f" y2="268" stroke="#f1e7e4" stroke-width="1.2"/>' % (tx, tx)
    b += mark(x0 + 9, 72, True, 11) + text(x0 + 28, 77, 'Giusto: il tempo per pulire è in agenda', 14.5, 'start', 800, OK)
    b += bar(92, segs)
    for k, lab in enumerate(['9:00', '9:30', '10:00', '10:30', '11:00']):
        tx = x0 + k * 30 * w_min
        b += '<line x1="%.1f" y1="142" x2="%.1f" y2="150" stroke="%s" stroke-width="1.5"/>' % (tx, tx, MUTED) + text(tx, 166, lab, 12.5, fill=MUTED)
    segs2 = [(['Consulenza'], 15, '#c9b6e4'), (['Servizio'], 75, '#e98fae'), (['Prossima cliente'], 25, '#d9d2d4')]
    b += mark(x0 + 9, 198, False, 11) + text(x0 + 28, 203, 'Sbagliato: la cliente dopo arriva subito', 14.5, 'start', 800, ERR)
    b += bar(216, segs2)
    xe = x0 + 90 * w_min
    b += '<line x1="%.1f" y1="208" x2="%.1f" y2="270" stroke="%s" stroke-width="3"/>' % (xe, xe, ERR)
    b += text(xe, 290, 'niente tempo per la pulizia', 13.5, 'middle', 700, ERR)
    b += ic_stopwatch(x0 + 10, 286, 0.9) + text(x0 + 28, 292, 'Misura i tuoi tempi reali', 14, 'start', 700)
    return svg(900, 310, defs() + b, 'Agenda: consulenza, servizio, consigli e pulizia; errore: appuntamento successivo senza tempo per la pulizia')


@figx('percorso-apertura.svg')
def opening_path():
    b = title('Aprire l\'attività: il percorso')
    pts = [(80, 150), (240, 230), (400, 150), (560, 230), (720, 150), (870, 230)]
    d = smooth_d([(40, 190)] + pts + [(950, 190)])
    b += '<path d="%s" fill="none" stroke="#efe3df" stroke-width="22" stroke-linecap="round"/>' % d
    b += '<path d="%s" fill="none" stroke="%s" stroke-width="2.5" stroke-dasharray="8 7"/>' % (d, ACC)
    labels = [['Qualifica', 'di estetista'], ['Partita IVA', '+ codice ATECO'], ['Camera di Commercio', '+ Albo artigiani'],
              ['INPS artigiani', '+ INAIL'], ['SCIA', 'al SUAP del Comune'], ['Privacy, tariffe,', 'assicurazione']]
    for k, ((px, py), lab) in enumerate(zip(pts, labels)):
        b += '<circle cx="%d" cy="%d" r="22" fill="%s" stroke="#fff" stroke-width="3"/>' % (px, py, ACC2) + text(px, py + 6.5, str(k + 1), 18, weight=800, fill='#fff')
        up = py < 190
        ly = py - 60 if up else py + 46
        b += text(px, ly, lab[0], 15, weight=800) + text(px, ly + 19, lab[1], 13.5, fill=MUTED)
    b += ic_flag(948, 168, 1.1) + text(948, 120, 'Prima', 14, weight=800, fill=ACC) + text(948, 136, 'cliente', 14, weight=800, fill=ACC)
    b += label_box(300, 300, 400, 30, 'Verifica sempre con commercialista e Comune', YEL_BG, YEL_S, '#7a5a12', 14)
    return svg(1000, 340, defs() + b, 'Percorso per aprire l\'attività: qualifica, partita IVA, Camera di Commercio, INPS e INAIL, SCIA, privacy e assicurazione')


@figx('forfettario-esempio.svg')
def flat_tax():
    b = title('Forfettario: esempio')
    x0, W, y = 40, 820, 92
    w67 = W * 0.67
    b += text(x0, 78, 'Incassi 30.000 €', 17, 'start', 800)
    b += text(x0 + W, 78, '100%', 14, 'end', 700, MUTED)
    c = uid('fb')
    b += '<clipPath id="%s"><rect x="%d" y="%d" width="%d" height="58" rx="12"/></clipPath>' % (c, x0, y, W)
    b += '<g clip-path="url(#%s)" filter="url(#nxShS)"><rect x="%d" y="%d" width="%.1f" height="58" fill="%s"/>' % (c, x0, y, w67, ACC)
    b += '<rect x="%.1f" y="%d" width="%.1f" height="58" fill="#e6dfe1"/>' % (x0 + w67, y, W - w67)
    b += '<rect x="%d" y="%d" width="%d" height="22" fill="#fff" opacity=".12"/></g>' % (x0, y, W)
    b += '<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="#fff" stroke-width="3"/>' % (x0 + w67, y, x0 + w67, y + 58)
    b += text(x0 + w67 / 2, y + 26, '67% = reddito 20.100 €', 18, weight=800, fill='#fff')
    b += text(x0 + w67 / 2, y + 46, 'su questo si calcolano contributi e imposta', 13, weight=600, fill='#fde6ee')
    b += text(x0 + w67 + (W - w67) / 2, y + 26, '33% = 9.900 €', 16, weight=800)
    b += text(x0 + w67 + (W - w67) / 2, y + 46, 'costi forfettari, non tassati', 13, weight=600, fill=MUTED)
    # ramo dal 67%: due voci da pagare
    sx = x0 + w67 / 2
    yb = y + 58
    b += '<path d="M%.1f,%d L%.1f,%d" stroke="%s" stroke-width="2.2"/>' % (sx, yb, sx, yb + 22, ACC2)
    b += dot(sx, yb + 22, 4, ACC2)
    bx1, bx2, bw = x0, x0 + 278, 262
    for bx in (bx1, bx2):
        b += '<path d="M%.1f,%d L%.1f,%d Q%.1f,%d %.1f,%d L%.1f,%d" fill="none" stroke="%s" stroke-width="2.2"/>' % (
            sx, yb + 22, bx + bw / 2 + (10 if bx < sx else -10), yb + 22, bx + bw / 2, yb + 22, bx + bw / 2, yb + 32, bx + bw / 2, yb + 44, ACC2)
        b += '<path d="M%.1f,%d l-6,-8 l12,0 Z" fill="%s"/>' % (bx + bw / 2, yb + 52, ACC2)
    yy = yb + 54
    b += card(bx1, yy, bw, 72, accent=ACC, ah=5)
    b += text(bx1 + bw / 2, yy + 32, 'Contributi INPS', 16, weight=800) + text(bx1 + bw / 2, yy + 54, 'fissi + %', 15, weight=700, fill=ACC2)
    b += card(bx2, yy, bw, 72, accent=ACC, ah=5)
    b += text(bx2 + bw / 2, yy + 32, 'Imposta sostitutiva', 16, weight=800) + text(bx2 + bw / 2, yy + 54, '5% (nuova attività) o 15%', 15, weight=700, fill=ACC2)
    # nota sulle spese reali, sotto la quota forfettaria
    nx = x0 + w67 + 8
    nw = W - w67 - 8
    b += dashed(nx + nw / 2, yb + 4, nx + nw / 2, yy - 2, MUTED, 1.5)
    b += '<rect x="%.1f" y="%d" width="%.1f" height="72" rx="14" fill="%s" stroke="#efc4bd" stroke-width="1.4"/>' % (nx, yy, nw, RED_BG)
    b += mark(nx + 28, yy + 36, False, 13)
    b += text(nx + 50, yy + 32, 'Le spese reali', 15, 'start', 800, ERR) + text(nx + 50, yy + 52, 'non si scaricano', 15, 'start', 800, ERR)
    b += text(450, 318, 'Numeri semplificati, regole 2026: chiedi conferma al commercialista.', 13.5, fill=MUTED, style='italic')
    return svg(900, 334, defs() + b, 'Esempio di regime forfettario: incassi 30.000 euro, reddito 67% pari a 20.100 euro, contributi e imposta')


@figx('foto-set.svg')
def photo_set():
    b = title('Il set fotografico')
    g = uid('lg')
    b += ('<defs><linearGradient id="%s" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff3c4" stop-opacity=".85"/>'
          '<stop offset="1" stop-color="#fff3c4" stop-opacity="0"/></linearGradient>'
          '<linearGradient id="%ss" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d8ecfa"/><stop offset="1" stop-color="#f4faff"/></linearGradient></defs>') % (g, g)
    ty = 266   # piano del tavolo
    # finestra con luce diurna
    b += '<path d="M118,84 L118,250 L470,%d L300,%d Z" fill="url(#%s)"/>' % (ty - 4, ty - 40, g)
    b += '<rect x="28" y="70" width="90" height="190" rx="6" fill="url(#%ss)" stroke="#8d969f" stroke-width="4"/>' % g
    b += '<line x1="73" y1="70" x2="73" y2="260" stroke="#8d969f" stroke-width="3"/><line x1="28" y1="165" x2="118" y2="165" stroke="#8d969f" stroke-width="3"/>'
    b += '<path d="M40,150 L62,86 M84,150 L106,86 M40,248 L62,184 M84,248 L106,184" stroke="#fff" stroke-width="3" opacity=".8"/>'
    b += mark(73, 290, True, 11)
    b += text(73, 316, 'Luce naturale', 14, weight=800) + text(73, 333, 'o fredda', 14, weight=800)
    # tavolo e foglio neutro
    b += '<rect x="150" y="%d" width="420" height="12" rx="3" fill="#cdbfb3"/>' % ty
    b += '<rect x="150" y="%d" width="420" height="4" rx="2" fill="#e3d8ce"/>' % ty
    b += '<rect x="226" y="%d" width="300" height="6" rx="2" fill="#f4f1ee" stroke="#ddd5cf"/>' % (ty - 6)
    # mano della cliente (di profilo) con unghie smaltate
    b += ('<path d="M176,%d L176,%d C196,%d 250,%d 282,%d C304,%d 330,%d 362,%d L430,%d C447,%d 457,%d 455,%d C453,%d 441,%d 420,%d Z" '
          'fill="%s" stroke="%s" stroke-width="1.5"/>' % (ty - 6, ty - 58, ty - 84, ty - 82, ty - 58, ty - 46, ty - 42, ty - 42, ty - 40,
                                                          ty - 40, ty - 30, ty - 18, ty - 8, ty - 6, ty - 6, SKIN, SKIN_D))
    b += '<path d="M226,%d Q254,%d 276,%d" fill="none" stroke="%s" stroke-width="1.2" opacity=".7"/>' % (ty - 74, ty - 80, ty - 66, SKIN_D)
    b += ('<path d="M390,%d C410,%d 442,%d 460,%d L463,%d C447,%d 420,%d 392,%d Z" fill="%s" stroke="%s" stroke-width="1"/>'
          % (ty - 41, ty - 50, ty - 51, ty - 40, ty - 33, ty - 42, ty - 43, ty - 37, FUCHSIA, NAIL_S))
    b += '<path d="M402,%d C416,%d 434,%d 446,%d" stroke="#fff" stroke-width="1.8" fill="none" opacity=".7" stroke-linecap="round"/>' % (ty - 45, ty - 48, ty - 48, ty - 45)
    p2 = dict(top=ty - 48)
    # braccio con telefono
    b += '<rect x="526" y="104" width="9" height="%d" rx="3" fill="#6f7983"/>' % (ty - 104)
    b += '<rect x="512" y="%d" width="38" height="8" rx="3" fill="#565f68"/>' % (ty - 6)
    b += '<rect x="420" y="100" width="114" height="8" rx="3" fill="#6f7983"/>'
    b += '<rect x="440" y="96" width="14" height="22" rx="3" fill="#565f68"/>'
    b += '<rect x="372" y="112" width="104" height="12" rx="4" fill="#2f2a2e"/>'
    b += '<rect x="404" y="124" width="22" height="5" rx="2" fill="#4a4448"/><circle cx="415" cy="127" r="2.4" fill="#9fc6e4"/>'
    # campo inquadrato
    b += '<path d="M415,130 L352,%d L476,%d Z" fill="%s" opacity=".08"/>' % (ty - 46, ty - 46, ACC)
    b += dashed(415, 130, 352, ty - 46, ACC, 1.3, '4 4') + dashed(415, 130, 476, ty - 46, ACC, 1.3, '4 4')
    b += focus_box(415, p2['top'] + 2, 14, '#f5b301')
    # richiami numerati
    calls = [(470, 118, 'Telefono fermo', 'supporto, niente mani'), (415, 190, 'Fuoco sulle unghie', 'tocca lo schermo sull\'unghia'),
             (440, p2['top'] + 4, 'Cuticole pulite, poco olio', 'l\'olio lucido riflette'), (510, ty - 3, 'Sfondo neutro', 'bianco, grigio o beige')]
    for k, (px, py, l, sub) in enumerate(calls):
        ly = 92 + k * 62
        b += '<line x1="%.1f" y1="%.1f" x2="%d" y2="%d" stroke="%s" stroke-width="1.2"/>' % (px, py, 618, ly, MUTED)
        b += '<circle cx="%.1f" cy="%.1f" r="3.5" fill="%s"/>' % (px, py, ACC2)
        b += badge(632, ly, k + 1, ACC2, 13, 14)
        b += text(654, ly + 1, l, 15, 'start', 800) + text(654, ly + 19, sub, 12.5, 'start', 400, MUTED)
    # riquadro errore: luce calda
    bx, by = 156, 58
    b += '<rect x="%d" y="%d" width="196" height="74" rx="12" fill="%s" stroke="#efc4bd" stroke-width="1.4"/>' % (bx, by, RED_BG)
    b += '<circle cx="%d" cy="%d" r="20" fill="#ffb347" opacity=".35"/>' % (bx + 34, by + 32)
    b += '<path d="M%d,%d a11,11 0 1 1 12,0 l0,6 l-12,0 Z" fill="#ffc35a" stroke="#d98a1c" stroke-width="1.2"/>' % (bx + 28, by + 34)
    b += '<rect x="%d" y="%d" width="12" height="7" rx="1.5" fill="#8d969f"/>' % (bx + 28, by + 41)
    b += text(bx + 60, by + 31, 'Luce calda:', 14, 'start', 800, ERR) + text(bx + 60, by + 50, 'colori gialli', 14, 'start', 700, ERR)
    b += mark(bx + 176, by + 18, False, 11)
    return svg(900, 346, defs() + b, 'Set fotografico: luce naturale o fredda, sfondo neutro, telefono fermo, cuticole pulite; da evitare la luce calda')


@figx('foto-angolazioni.svg')
def photo_angles():
    b = title('Tre foto per ogni lavoro')
    heads = ['Dall\'alto', 'Di profilo', 'A tunnel']
    caps = ['simmetria, smile line', 'apex, spessore', 'curva a C']
    for i in range(3):
        x = 20 + i * 292
        px, py, pw, ph = x + 20, 98, 238, 156
        sx, sy, sw, sh = px + 10, py + 10, pw - 20, ph - 20
        inner = ''
        if i == 0:
            inner += '<rect x="%d" y="%d" width="%d" height="%d" fill="#f7f3ef"/>' % (sx, sy, sw, sh)
            for k, (dx, ln) in enumerate([(-66, 74), (-22, 86), (22, 82), (66, 70)]):
                cx = px + pw / 2 + dx
                yc = sy + 22 + ln
                ys = yc - ln + 26
                f, p = nail(cx, yc, hw=15, nail_len=ln - 26, free_len=26, plate='#f6c9d4', free='#f6c9d4', shape='squoval',
                            extra=tip_fill(cx, ys, 15, 10, ys - 26), finger_len=60)
                inner += f
            inner += focus_box(px + pw / 2 - 22, sy + 40, 16)
        elif i == 1:
            inner += '<rect x="%d" y="%d" width="%d" height="%d" fill="#f7f3ef"/>' % (sx, sy, sw, sh)
            sec, fd, pp = section(sx + 60, sy + 74, L=110, F=34, body_h=64)
            yb = sy + 74
            pts = [(sx + 64, yb), (sx + 92, yb - 12), (sx + 140, yb - 24), (sx + 178, yb - 20), (sx + 204, yb - 4)]
            inner += sec + product(pts, yb, end_x=sx + 204, end_y=yb + 6, fill='#f6c9d4', stroke=NAIL_S) + fd
            inner += dot(sx + 146, yb - 24, 4.5, ACC2)
            inner += text(sx + 146, yb - 36, 'apex', 13, weight=800, fill=ACC2)
            inner += focus_box(sx + 146, yb - 12, 16)
        else:
            inner += '<rect x="%d" y="%d" width="%d" height="%d" fill="#f7f3ef"/>' % (sx, sy, sw, sh)
            cx, cy = px + pw / 2, sy + 84
            inner += '<ellipse cx="%.1f" cy="%.1f" rx="62" ry="50" fill="%s" stroke="%s" stroke-width="1.5"/>' % (cx, cy + 30, SKIN, SKIN_D)
            inner += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="#f6c9d4" stroke="%s" stroke-width="1.6"/>' % (
                cx - 60, cy + 8, cx, cy - 58, cx + 60, cy + 8, cx + 52, cy + 10, cx, cy - 44, cx - 52, cy + 10, NAIL_S)
            inner += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="#fff" stroke-width="2" opacity=".7"/>' % (cx - 34, cy - 12, cx - 10, cy - 30, cx + 12, cy - 30)
            inner += dashed(cx - 56, cy + 9, cx + 56, cy + 9, MUTED, 1.3)
            inner += text(cx, cy - 4, 'C', 18, weight=800, fill=ACC2)
            inner += focus_box(cx, cy - 14, 18)
        body = phone_frame(px, py, pw, ph, inner)
        b += frame(x, 55, 278, 262, heads[i], num=i + 1, body=body, cap=caps[i], capcol=INK)
    return svg(900, 332, defs() + b, 'Tre foto per ogni lavoro: dall\'alto, di profilo e a tunnel')


# ================================================================= main
def main():
    names = [a for a in sys.argv[1:] if a.endswith('.svg')]
    todo = [(n, f) for n, f in MINE.items() if not names or n in names]
    for name, f in todo:
        with open(os.path.join(OUT, name), 'w', encoding='utf-8') as fh:
            fh.write(f())
        print('OUT assets/img/%s' % name)
    print('Gruppo C: %d illustrazioni' % len(todo))


if __name__ == '__main__':
    main()
