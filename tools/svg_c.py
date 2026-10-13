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
    for i in range(4):
        x = 20 + i * 218
        cx, yc, hw, d = x + 103, 262, 38, 24
        ys = yc - 108
        yl = smile_lat(ys, d)
        top = ys - 56
        extra = tip_fill(cx, ys, hw, d, top) if i == 3 else ''
        f, p = nail(cx, yc, hw=hw, nail_len=108, free_len=56, plate='#f6c9d4', free='#f6c9d4', extra=extra, finger_len=30)
        body = f
        if i == 0:
            body += dot(cx, ys, 6, '#fff', NAIL_S)
            body += arr(cx + 50, ys - 30, cx + 10, ys - 4, DARK, 1.8)
        elif i == 1:
            body += dot(cx, ys, 4, '#fff', '#d9a8b6')
            body += dot(cx - hw + 3, yl, 6, '#fff', NAIL_S) + dot(cx + hw - 3, yl, 6, '#fff', NAIL_S)
            body += dashed(cx - hw - 14, yl, cx + hw + 14, yl, ACC2, 1.6)
            for sx in (-1, 1):
                body += arr(cx + sx * (hw + 14), yc - 30, cx + sx * (hw + 14), yl + 4, DARK, 1.8)
        elif i == 2:
            pts = smile_pts(cx, ys, hw, d, 24, 0)
            left, right = pts[:13], pts[12:]
            body += '<path d="%s" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>' % smooth_d(left)
            body += '<path d="%s" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>' % smooth_d(right[::-1])
            body += '<path d="%s" fill="none" stroke="%s" stroke-width="1" />' % (smooth_d(pts), WHITE_S)
            off = [(px, py - 16) for px, py in pts]
            body += carr(smooth_d(off[1:11]), DARK, 1.8) + carr(smooth_d(off[13:23][::-1]), DARK, 1.8)
            body += dot(cx - hw, yl, 4, '#fff', NAIL_S) + dot(cx + hw, yl, 4, '#fff', NAIL_S)
        else:
            body += carr('M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f' % (cx + 46, top + 34, cx + 52, top - 4, cx + 18, top - 4), DARK, 1.8)
        b += frame(x, 55, 205, 280, heads[i], num=i + 1, body=body, cap=caps[i], capcol=INK)
    return svg(900, 345, defs() + b, 'French dipinto con il metodo dei punti guida in quattro passaggi')


def bb_grad(gid, stops):
    s = '<linearGradient id="%s" x1="0" y1="1" x2="0" y2="0">' % gid
    for off, col, op in stops:
        s += '<stop offset="%s" stop-color="%s" stop-opacity="%s"/>' % (off, col, op)
    return s + '</linearGradient>'


BB_BASE = '#f6c9d4'


@figx('baby-boomer-step.svg')
def bboom_steps():
    gdefs = '<defs>%s%s</defs>' % (
        bb_grad('bbs1', [(0, '#ffffff', 0), (.42, '#ffffff', 0), (.78, '#fdf8f9', 1), (1, '#ffffff', 1)]),
        bb_grad('bbs2', [(0, '#f3a9bd', .0), (1, '#f3a9bd', .0)]))
    b = title('Baby boomer in gel')
    heads = ['Bianco sulla punta', 'Sfuma verso l\'alto', 'Cover sopra + apex', 'Top: niente linee']
    caps = ['strato sottile', 'colpi brevi, fino a metà', 'il bianco "affiora"', 'sfumatura morbida']
    for i in range(4):
        x = 20 + i * 218
        cx, yc, hw = x + 103, 262, 38
        nl, fl = 108, 62
        ys = yc - nl
        top = ys - fl
        if i == 0:
            extra = '<rect x="%.1f" y="%.1f" width="%d" height="%.1f" fill="#fdfafa" clip-path="url(#CLIP)"/>' % (cx - 60, top - 10, 120, ys - 18 - top + 10)
            extra += '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" clip-path="url(#CLIP)"/>' % (cx - 60, ys - 18, cx + 60, ys - 18, WHITE_S)
        else:
            extra = '<rect x="%.1f" y="%.1f" width="%d" height="%.1f" fill="url(#bbs1)" clip-path="url(#CLIP)"/>' % (cx - 60, top - 2, 120, yc - top)
        if i >= 2:
            extra += '<rect x="%.1f" y="%.1f" width="%d" height="%.1f" fill="#f19bb4" opacity=".22" clip-path="url(#CLIP)"/>' % (cx - 60, top - 10, 120, yc - top + 20)
        f, p = nail(cx, yc, hw=hw, nail_len=nl, free_len=fl, shape='mandorla', plate=BB_BASE, free=BB_BASE, extra=extra, finger_len=30)
        body = f
        if i == 1:
            body += brush_flat(cx + 30, ys + 30, -40, 60)
            for k, dx in enumerate((-22, -4, 14)):
                body += arr(cx + dx - 6, ys + 12, cx + dx - 6, ys - 16, DARK, 1.8)
        elif i == 2:
            # profilo in miniatura con apex (riquadro in basso a destra)
            ox, oy = x + 118, 268
            mini = box(ox - 10, oy - 34, 92, 50, '#fff', '#d8c8c4', 8)
            mini += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="3" stroke-linecap="round"/>' % (ox, oy + 6, ox + 72, oy + 6, NAIL_S)
            mini += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="#f6b8c9" stroke="%s" stroke-width="1.2"/>' % (
                ox + 2, oy + 5, ox + 20, oy - 14, ox + 36, oy - 14, ox + 54, oy - 14, ox + 72, oy + 2, ox + 72, oy + 6, NAIL_S)
            mini += arr(ox + 36, oy - 30, ox + 36, oy - 17, ACC2, 1.4)
            body += mini + text(ox + 6, oy - 18, 'apex', 12.5, 'start', 800, ACC2)
        elif i == 3:
            body += gloss(cx, top + 30, ys + 40, 5) + sparkle(cx + 16, top + 40, 6)
        b += frame(x, 55, 205, 280, heads[i], num=i + 1, body=body, cap=caps[i], capcol=INK, hsize=14.5)
    return svg(900, 345, defs() + gdefs + b, 'Baby boomer in gel in quattro passaggi: bianco, sfumatura, cover con apex, top')


@figx('sfumatura-errori.svg')
def bboom_errors():
    gdefs = '<defs>%s%s</defs>' % (
        bb_grad('sfg', [(0, '#ffffff', 0), (.4, '#ffffff', 0), (.8, '#fdf8f9', 1), (1, '#ffffff', 1)]),
        '<linearGradient id="sfp" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="%s"/><stop offset=".55" stop-color="%s"/><stop offset="1" stop-color="#ffffff"/></linearGradient>' % (BB_BASE, BB_BASE))
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
            f, p = nail(cx, yc, hw=hw, nail_len=nl, free_len=fl, shape='mandorla', plate=BB_BASE, free=BB_BASE, extra=extra, finger_len=30)
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
    b += leader(xa + 80, yb - 22, xa + 60, 112, 'Prodotto trasparente', 'middle')
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
    tb, ey = 222, 284

    def client(x):
        s = '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3"/>' % (x + 14, tb, x + 336, tb, GREY)
        s += '<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Z" fill="%s" stroke="%s" stroke-width="1.5"/>' % (
            x + 30, tb - 1, x + 30, tb - 30, x + 172, tb - 34, x + 178, tb - 1, x + 30, tb - 1, SKIN, SKIN_D)
        s += '<path d="M%d,%d Q%d,%d %d,%d" stroke="%s" stroke-width="6" fill="none" stroke-linecap="round"/>' % (x + 100, tb - 34, x + 140, tb - 38, x + 170, tb - 28, ACC)
        return s

    # --- pannello sinistro: dotting
    x = 20
    body = client(x)
    dx = x + 162
    body += dotter(dx, tb - 42, -90, 48, 5)
    # mano dell'operatrice: dorso, dita che tengono il dotter, mignolo appoggiato al tavolo
    body += '<path d="M%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="%s" stroke="%s" stroke-width="1.5"/>' % (
        dx + 6, 128, dx + 60, 108, dx + 150, 116, dx + 156, 152, dx + 90, 170, dx + 8, 154, SKIN, SKIN_D)
    body += '<rect x="%d" y="%d" width="18" height="%d" rx="9" fill="%s" stroke="%s" stroke-width="1.5"/>' % (dx + 80, 150, tb - 150, SKIN, SKIN_D)
    body += '<path d="M%d,%d Q%d,%d %d,%d" fill="%s"/>' % (dx + 66, 158, dx + 89, 170, dx + 112, 158, SKIN)
    body += '<ellipse cx="%d" cy="%d" rx="12" ry="9" fill="%s" stroke="%s" stroke-width="1.5"/>' % (dx + 8, 140, SKIN, SKIN_D)
    body += arr(dx - 20, 112, dx - 20, 160, DARK, 2.2)
    body += text(x + 24, 104, 'Dotter', 14, 'start', 800) + text(x + 24, 121, 'verticale,', 14, 'start', 800)
    body += text(x + 24, 140, 'senza premere', 13, 'start', 600, MUTED)
    body += leader(dx + 89, tb - 4, dx + 60, 246 - 5, 'Mignolo appoggiato', 'middle', 13.5)
    for k in range(5):
        body += '<circle cx="%d" cy="%d" r="7" fill="%s"/>' % (x + 36 + k * 22, ey, FUCHSIA)
    body += mark(x + 150, ey, True, 11)
    for k, r in enumerate([4, 9, 6, 11, 5]):
        body += '<circle cx="%d" cy="%d" r="%d" fill="%s"/>' % (x + 202 + k * 22, ey, r, FUCHSIA)
    body += mark(x + 318, ey, False, 11)
    b += frame(x, 55, 350, 290, 'Dotting', body=body, cap='ricarica a ogni punto', capcol=INK)
    # --- pannello destro: striping
    x = 390
    body = client(x)
    body += '<path d="M%d,%d Q%d,%d %d,%d" stroke="%s" stroke-width="3" fill="none"/>' % (x + 104, tb - 41, x + 125, tb - 44, x + 146, tb - 43, FUCHSIA)
    body += brush_liner(x + 148, tb - 42, -24, 120)
    body += text(x + 24, 100, 'Trascina, non spingere', 14, 'start', 800)
    body += text(x + 24, 119, 'pressione costante', 13, 'start', 600, MUTED)
    body += arr(x + 40, 146, x + 128, 146, DARK, 2.2)
    body += text(x + 84, 166, 'verso di te', 12.5, fill=MUTED, style='italic')
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
    for i in range(5):
        x = 20 + i * 194
        cx, cy = x + 90, 150
        body = ''
        if i == 0:
            body += plate_disc(cx, cy)
            body += '<path d="M%.1f,%.1f q11,16 0,24 q-11,-8 0,-24 z" fill="%s"/>' % (cx + 4, cy - 18, FUCHSIA)
            body += ic_bottle(cx + 52, cy - 48, 0.9, FUCHSIA, INK)
        elif i == 1:
            # vista di lato: piastra piatta, raschietto inclinato a 45°
            py = cy + 40
            body += '<rect x="%.1f" y="%.1f" width="150" height="9" rx="3" fill="#dfe3e8" stroke="%s" stroke-width="1.5"/>' % (cx - 75, py, GREY_D)
            for k in range(5):
                body += '<path d="M%.1f,%.1f l4,4 l4,-4" fill="none" stroke="%s" stroke-width="1.2"/>' % (cx - 60 + k * 14, py, GREY_D)
            body += '<path d="M%.1f,%.1f q10,-9 20,0 z" fill="%s"/>' % (cx + 2, py, FUCHSIA)
            body += rot(45, cx, py, '<rect x="%.1f" y="%.1f" width="84" height="8" rx="2" fill="#c9ccd1" stroke="%s"/>' % (cx - 84, py - 8, GREY_D))
            body += '<path d="M%.1f,%.1f A34,34 0 0 1 %.1f,%.1f" fill="none" stroke="%s" stroke-width="1.8" stroke-dasharray="3 3"/>' % (
                cx - 34, py, cx - 24, py - 24, ACC2)
            body += text(cx - 54, py - 12, '45°', 15, weight=800, fill=ACC2)
            body += arr(cx - 40, py + 34, cx + 50, py + 34, DARK, 2)
        elif i == 2:
            body += plate_disc(cx, cy + 34, 40, False)
            body += stamp_pattern(cx, cy + 34, GREY_D)
            body += stamper(cx - 4, cy - 12, 12, 34)
            body += carr('M%.1f,%.1f A40,40 0 0 1 %.1f,%.1f' % (cx - 46, cy - 6, cx + 44, cy - 6), DARK, 2)
        elif i == 3:
            f, p = nail(cx, cy + 78, hw=26, nail_len=70, free_len=22, plate=FUCHSIA, free=FUCHSIA, shape='squoval', finger_len=20)
            body += f
            body += stamper(cx + 4, cy - 14, -16, 30)
            body += carr('M%.1f,%.1f A44,44 0 0 1 %.1f,%.1f' % (cx - 52, cy - 22, cx + 52, cy - 22), DARK, 2)
        else:
            f, p = nail(cx, cy + 78, hw=26, nail_len=70, free_len=22, plate=FUCHSIA, free=FUCHSIA, shape='squoval', finger_len=20,
                        extra='<g clip-path="url(#CLIP)">%s</g>' % stamp_pattern(cx, cy + 22))
            body += f + gloss(cx, cy - 4, cy + 50, 4) + sparkle(cx + 18, cy - 4, 6)
        b += frame(x, 55, 180, 250, None, num=i + 1, body=body, cap=caps[i], capcol=INK)
    b += label_box(310, 316, 380, 30, 'Lavora veloce: lo smalto asciuga in pochi secondi', YEL_BG, YEL_S, '#7a5a12', 14)
    return svg(1000, 356, defs() + b, 'Stamping in cinque passaggi: smalto sulla piastra, raschia a 45°, rotola il tampone, posa rotolando, sigilla con top')


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
    names = ['Classico', 'A V', 'Micro', 'Reverse', 'Colorato', 'Doppio']
    for i, nm in enumerate(names):
        cx = 92 + i * 163
        b += '<rect x="%d" y="52" width="150" height="248" rx="16" fill="%s"/>' % (cx - 75, PANEL)
        yc, hw, nl, fl = 218, 32, 92, 72
        ys, top = yc - nl, yc - nl - fl
        plate = NUDE if i == 3 else '#f6c9d4'
        extra = ''
        if i == 0:
            extra = tip_fill(cx, ys, hw, 22, top)
        elif i == 1:
            vp = 'M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (cx - hw - 6, ys - 26, cx, ys + 12, cx + hw + 6, ys - 26, cx + hw + 6, top - 20, cx - hw - 6, top - 20)
            extra = '<path d="%s" fill="#fff" stroke="%s" clip-path="url(#CLIP)"/>' % (vp, WHITE_S)
        elif i == 2:
            out = nail_outline(cx, yc, ys, top, hw, 'mandorla')
            rc = uid('r')
            extra = ('<defs><clipPath id="%s"><rect x="%.1f" y="%.1f" width="120" height="%.1f"/></clipPath></defs>'
                     '<g clip-path="url(#CLIP)"><g clip-path="url(#%s)"><path d="%s" fill="none" stroke="#fff" stroke-width="16"/><path d="%s" fill="none" stroke="%s" stroke-width="1"/></g></g>'
                     % (rc, cx - 60, top - 10, ys - 26 - top + 10, rc, out, out, WHITE_S))
        elif i == 3:
            extra = reverse_cres(cx, yc, hw, 5, 16, ACC2)
        elif i == 4:
            extra = tip_fill(cx, ys, hw, 22, top, FUCHSIA, None)
        else:
            extra = tip_fill(cx, ys, hw, 22, top)
            pts = smile_pts(cx, ys + 12, hw, 22)
            extra += '<path d="M%s" fill="none" stroke="%s" stroke-width="3.5" clip-path="url(#CLIP)"/>' % (' L'.join('%.1f,%.1f' % q for q in pts), GOLD)
        f, p = nail(cx, yc, hw=hw, nail_len=nl, free_len=fl, shape='mandorla', plate=plate, free=plate, extra=extra, finger_len=34)
        pc = uid('k')
        b += '<defs><clipPath id="%s"><rect x="%d" y="52" width="150" height="248" rx="16"/></clipPath></defs><g clip-path="url(#%s)">%s</g>' % (pc, cx - 75, pc, f)
        b += text(cx, 286, nm, 16, weight=800)
    return svg(1000, 310, b, 'Sei varianti del french: classico, a V, micro, reverse, colorato e doppio')


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
        b += arr(bx + 70 + k * 0, oy - 5, ox + 58, oy + 26, DARK, 1.6) if False else ''
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
    b += label_box(20, 176, 150, 52, 'Quale prodotto?', ACC2, ACC2, '#fff', 16, 800, 12)
    rows = [('Semipermanente', 'Soak-off 10–15 min', 'soak'), ('Soft gel / BIAB', 'Assottiglia + soak-off 10–30 min', 'soak'),
            ('Acrilico', 'Assottiglia + soak-off 20–30 min', 'soak'), ('Polygel', 'Leggi la scheda tecnica', 'doc'),
            ('Hard gel', 'File-off: lascia un velo', 'file')]
    for k, (prod, out, ic) in enumerate(rows):
        yy = 58 + k * 60
        b += '<path d="M170,202 C200,202 196,%d 226,%d" fill="none" stroke="%s" stroke-width="2"/>' % (yy + 22, yy + 22, MUTED)
        b += label_box(230, yy, 180, 44, prod, '#fff', '#e5d6d2', INK, 15, 700)
        b += arr(414, yy + 22, 452, yy + 22, DARK, 2)
        col = ACC2 if ic == 'soak' else (WARN if ic == 'doc' else INK)
        b += label_box(458, yy, 320, 44, out, PANEL, PANEL, col if ic != 'soak' else INK, 15, 700)
        if ic == 'soak':
            b += ic_foil_finger(820, yy + 22, 1.0)
        elif ic == 'doc':
            b += ic_doc(820, yy + 22, 1.0, False, WARN)
        else:
            b += ic_file(820, yy + 22, 1.0)
    b += label_box(160, 358, 580, 32, 'Tempi indicativi: segui sempre le istruzioni del produttore', YEL_BG, YEL_S, '#7a5a12', 14)
    return svg(900, 400, defs() + b, 'Albero di scelta del metodo di rimozione per semipermanente, soft gel, acrilico, polygel e hard gel')


@figx('rimozione-soakoff-step.svg')
def soak_steps():
    b = title('Soak-off passo passo')
    caps = [['Togli il top', 'e assottiglia'], ['Olio', 'sulla pelle'], ['Cotone', '+ acetone'], ['Avvolgi', 'e aspetta'], ['Spingi, non', 'fare leva'], ['Buffer morbido', '+ olio']]
    for i in range(6):
        x = 20 + i * 162
        cx, yc = x + 75, 232
        body = ''
        if i == 3:
            body += '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5"/>' % (
                cx - 40, yc + 40, cx - 40, yc - 92, cx, yc - 140, cx + 40, yc - 92, cx + 40, yc + 40, FOIL, FOIL_S)
            for k in range(4):
                body += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="#f3f5f7" stroke-width="3"/>' % (cx - 30, yc - 84 + k * 30, cx + 30, yc - 66 + k * 30)
            body += ic_stopwatch(x + 118, 100, 1.0)
            body += text(x + 118, 136, '10–15\'', 13.5, weight=800, fill=ACC2)
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
                body += file_tool(cx + 26, yc - 118, -60, 96, 15)
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
                body += text(cx - 46, yc - 138, 'verso la punta', 12, weight=600, fill=MUTED) if False else ''
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
            body += '<g transform="translate(%.1f,%.1f) rotate(-60)"><rect x="0" y="-4" width="110" height="8" rx="3" fill="#9aa3ad"/><path d="M0,-4 L-16,-1 L-16,3 L0,4 Z" fill="#6f7983"/></g>' % (cx + 6, yc - 100)
        elif i == 2:
            extra = '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="#f4dfe5" clip-path="url(#CLIP)"/>' % (cx - 50, yc - 30, cx + 50, yc - 30, cx + 50, yc - 160)
            f, p = nail(cx, yc, hw=34, nail_len=110, free_len=30, plate='#e98fae', free='#e98fae', finger_len=24, extra=extra)
            body += f
            # pezzo di prodotto staccato tirato da due dita
            body += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="#e98fae" stroke="%s" stroke-width="1.5"/>' % (
                cx + 6, yc - 60, cx + 40, yc - 120, cx + 58, yc - 136, cx + 70, yc - 122, cx + 40, yc - 90, cx + 30, yc - 40, NAIL_S)
            body += '<ellipse cx="%.1f" cy="%.1f" rx="14" ry="20" fill="%s" stroke="%s" stroke-width="1.5" transform="rotate(30 %.1f %.1f)"/>' % (cx + 74, yc - 140, SKIN, SKIN_D, cx + 74, yc - 140)
            body += '<ellipse cx="%.1f" cy="%.1f" rx="13" ry="18" fill="%s" stroke="%s" stroke-width="1.5" transform="rotate(-40 %.1f %.1f)"/>' % (cx + 50, yc - 152, SKIN, SKIN_D, cx + 50, yc - 152)
            body += arr(cx + 78, yc - 100, cx + 92, yc - 160, ERR, 2.2)
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
    cases = [('Crepa nel prodotto', 'Ripara in salone', OK, GREEN_BG), ('Sollevamento', ['Elimina tutto', 'e ricostruisci'], OK, GREEN_BG),
             (['Rotta oltre il', 'bordo libero'], ['Accorcia e', 'ricostruisci'], WARN, YEL_BG), ('Rottura nel letto', ['Non coprire:', 'medico'], ERR, RED_BG)]
    for i, (t, out, col, bg) in enumerate(cases):
        x = 20 + i * 218
        cx, yc = x + 103, 244
        extra = ''
        plate, free, fl = GELP, GELP, 30
        if i == 0:
            pass
        elif i == 1:
            extra = '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="#faf6f7" stroke="#8f8388" stroke-width="1.5" stroke-dasharray="4 3" clip-path="url(#CLIP)"/>' % (
                cx - 40, yc - 20, cx + 10, yc - 34, cx + 30, yc - 12, cx - 10, yc + 10, cx - 40, yc - 20)
        elif i == 2:
            fl = 6
        elif i == 3:
            extra = '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="2.4" fill="none" clip-path="url(#CLIP)"/>' % (
                cx - 34, yc - 60, cx - 14, yc - 74, cx + 2, yc - 60, cx + 18, yc - 78, cx + 36, yc - 66, INK)
        f, p = nail(cx, yc, hw=34, nail_len=100, free_len=fl, plate=plate, free=free, extra=extra, finger_len=24)
        body = f
        if i == 0:
            body += zigzag(cx - 26, yc - 106, 6, 9, 5)
        elif i == 2:
            ys = yc - 100
            body += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="1.5" transform="rotate(-18 %.1f %.1f)"/>' % (
                cx + 40, ys - 14, cx + 70, ys - 14, cx + 66, ys - 32, cx + 44, ys - 32, GELP, NAIL_S, cx + 55, ys - 23)
            body += zigzag(cx - 34, ys - 6, 7, 10, 4, NAIL_S, 2)
        elif i == 3:
            body += ic_drop(cx + 6, yc - 40, 0.8, ERR, '#8e2a20')
        body += label_box(x + 18, 264, 170, 50, out, bg, col, col, 14.5, 800, 12, 2)
        b += frame(x, 55, 205, 270, None, body=body)
        tl = t if isinstance(t, list) else [t]
        for k, l in enumerate(tl):
            b += text(cx, 82 + k * 18, l, 15, weight=800)
    return svg(900, 340, defs() + b, 'Cosa si è rotto: crepa nel prodotto, sollevamento, rottura oltre il bordo libero, rottura nel letto ungueale')


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
            body += file_tool(cx + 30, yc - 138, -14, 100, 15)
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
    b += text(654, 372, '1–2 dita =', 14.5, 'start', 800) + text(654, 391, 'abitudini, struttura di quel dito', 14, 'start', 600, MUTED)
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
    for i in range(2):
        ok = i == 1
        x = 20 + i * 370
        body = ''
        lcx = x + 175
        # lampada stilizzata
        body += '<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Z" fill="#f4f1f8" stroke="#8a7d9e" stroke-width="2"/>' % (
            lcx - 110, 112, lcx - 110, 96, lcx, 74, lcx + 110, 96, lcx + 110, 112)
        for k in range(5):
            body += '<rect x="%d" y="108" width="16" height="6" rx="2" fill="#9a6be0"/>' % (lcx - 88 + k * 40)
        py = 250
        body += '<rect x="%d" y="%d" width="300" height="14" fill="%s" stroke="%s"/>' % (x + 25, py, PLATE_SEC, NAIL_S)
        body += '<rect x="%d" y="%d" width="300" height="14" fill="%s"/>' % (x + 25, py + 14, BED)
        if not ok:
            top = py - 76
            body += '<rect x="%d" y="%d" width="300" height="%d" fill="#c2577a" opacity=".9"/>' % (x + 25, top, py - top)
            body += '<rect x="%d" y="%d" width="300" height="%d" fill="#e9a6bc"/>' % (x + 25, top + 26, py - top - 26)
            rng = random.Random(11)
            for k in range(70):
                body += '<circle cx="%.1f" cy="%.1f" r="1.6" fill="#fff" opacity=".85"/>' % (x + 30 + rng.uniform(0, 290), top + 32 + rng.uniform(0, 40))
            wav = ' '.join('q8,-6 16,0' for _ in range(19))
            body += '<path d="M%d,%d %s" fill="none" stroke="%s" stroke-width="3"/>' % (x + 25, top, wav, INK)
            for k in range(6):
                rx = x + 50 + k * 50
                body += carr('M%d,%d L%d,%d' % (rx, 120, rx, top + 14), '#9a6be0' if True else DARK, 2.4)
            for k in range(6):
                ux = x + 50 + k * 50
                body += '<path d="M%d,%d a7,6 0 0 1 14,0 Z" fill="%s"/><line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.3"/>' % (
                    ux - 7, top + 18, INK, ux, top + 18, ux, top + 24, INK)
            body += leader(x + 300, top - 2, x + 300, 150, 'superficie dura', 'middle', 13)
            body += leader(x + 120, top + 50, x + 120, 300, 'gel ancora liquido sotto', 'middle', 13, fill=ERR)
        else:
            t1 = py - 26
            t2 = t1 - 26
            body += '<rect x="%d" y="%d" width="300" height="26" fill="#c2577a"/>' % (x + 25, t1)
            body += '<rect x="%d" y="%d" width="300" height="26" fill="#cf6a8b"/>' % (x + 25, t2)
            body += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#fff" stroke-width="1.5" stroke-dasharray="4 3"/>' % (x + 25, t1, x + 325, t1)
            for k in range(6):
                rx = x + 50 + k * 50
                body += carr('M%d,%d L%d,%d' % (rx, 120, rx, py - 2), '#9a6be0', 2.4)
            body += text(x + 175, 300, 'due strati sottili, polimerizzati uno alla volta', 13, weight=700, fill=OK)
        cap = 'Strati sottili: la luce arriva in fondo' if ok else 'Strato spesso: i pigmenti fanno ombra'
        b += frame(x, 55, 350, 285, None, ok=ok, body=body, cap=cap)
    return svg(760, 355, defs() + b, 'Grinze: in uno strato spesso i pigmenti fermano la luce, la superficie indurisce e sotto resta gel liquido; con strati sottili la luce arriva in fondo')


@figx('ingiallimento-cause.svg')
def yellowing():
    b = title('Ingiallimento: le cause')
    cx, yc = 450, 236
    f, p = nail(cx, yc, hw=40, nail_len=110, free_len=40, plate='#efd98f', free='#f2e2a6', finger_len=30)
    b += f
    items = [(ic_lamp, 'Lampada non abbinata', 150, 96, dict(q=True)), (None, 'Top non polimerizzato', 150, 168, None),
             (ic_brush_dirty, 'Pennello contaminato', 150, 240, {}), (ic_sun, 'Sole / lettini', 640, 96, {}),
             (ic_cig, 'Fumo', 640, 168, {}), (None, 'Detersivi e creme', 640, 240, None)]
    for k, (fn, lab, x, y, kw) in enumerate(items):
        ix = x - 40 if x < 450 else x - 26
        if k == 1:
            ic = ic_bottle(ix, y, 0.95, '#f4f1ec', INK) + ic_stopwatch(ix + 20, y + 10, 0.55)
        elif k == 5:
            ic = ic_bottle(ix, y, 0.95, '#7fb3d5', '#4f86a8')
        else:
            ic = fn(ix, y, 1.0, **kw)
        b += '<circle cx="%d" cy="%d" r="26" fill="%s"/>' % (ix, y, PANEL) + ic
        if x < 450:
            b += text(x - 6, y + 5, lab, 14.5, 'start', 700)
        else:
            b += text(x + 8, y + 5, lab, 14.5, 'start', 700)
    b += label_box(150, 276, 280, 30, 'Subito → prodotto / lampada', '#fff', '#e5d6d2', INK, 14, 700)
    b += label_box(470, 276, 280, 30, 'Dopo settimane → abitudini', '#fff', '#e5d6d2', INK, 14, 700)
    return svg(900, 320, defs() + b, 'Cause dell\'ingiallimento: lampada, top non polimerizzato, pennello contaminato, sole, fumo, detersivi e creme')


@figx('diagnosi-flusso.svg')
def diag_flow():
    b = title('Diagnosi in 5 domande')
    qs = [('Dove?', 'base, lati, punta'), ('Quante dita?', 'tutte o 1–2'), ('Quando?', 'subito o dopo'), ('Cosa ho fatto?', 'rileggi la scheda'), (['Cosa ha fatto', 'la cliente?'], 'abitudini, traumi')]
    for k, (q, sub) in enumerate(qs):
        cx = 92 + k * 165
        cy = 112
        b += '<circle cx="%d" cy="%d" r="34" fill="%s"/>' % (cx, cy, ACC2) + text(cx, cy + 9, str(k + 1), 26, weight=800, fill='#fff')
        if k < 4:
            b += arr(cx + 40, cy, cx + 124, cy, DARK, 2.2)
        ql = q if isinstance(q, list) else [q]
        for j, l in enumerate(ql):
            b += text(cx, 172 + j * 19, l, 16, weight=800)
        b += text(cx, 172 + len(ql) * 19, sub, 13, fill=MUTED)
        iy = 252
        b += '<circle cx="%d" cy="%d" r="30" fill="%s"/>' % (cx, iy, PANEL)
        if k == 0:
            fx = '<rect x="%d" y="%d" width="40" height="14" fill="%s" opacity=".6"/>' % (cx - 20, iy - 2, Z_BASE)
            fx = '<path d="M%.1f,%.1f q11,-10 22,0 l0,-30 q-11,-10 -22,0 z" fill="%s"/>' % (cx - 11, iy + 16, GELP)
            b += fx + '<path d="M%.1f,%.1f q11,-10 22,0 l0,-7 q-11,-10 -22,0 z" fill="%s" opacity=".8"/>' % (cx - 11, iy + 16, Z_BASE)
            b += '<path d="M%.1f,%.1f q11,-10 22,0 l0,-30 q-11,-10 -22,0 z" fill="none" stroke="%s" stroke-width="1.5"/>' % (cx - 11, iy + 16, NAIL_S)
        elif k == 1:
            b += mini_hand(cx - 2, iy - 12, 0.42, (0, 1, 2, 3, 4))
        elif k == 2:
            b += ic_calendar(cx, iy + 2, 1.0)
        elif k == 3:
            b += ic_doc(cx, iy, 1.0)
        else:
            b += ic_house(cx, iy, 1.0)
    b += arr(806, 112, 822, 112, DARK, 2.2) if False else ''
    b += label_box(250, 296, 400, 34, 'Poi: una correzione alla volta', YEL_BG, YEL_S, '#7a5a12', 15, 800)
    return svg(900, 340, defs() + b, 'Le cinque domande della diagnosi: dove, quante dita, quando, cosa ho fatto, cosa ha fatto la cliente')


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
