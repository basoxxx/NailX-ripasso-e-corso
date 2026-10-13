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
    for mid, col in (('ar', ACC2), ('arw', MUTED), ('ag', DARK), ('are', ERR), ('aro', OK)):
        m += ('<marker id="%s" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
              '<path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker>' % (mid, col))
    return '<defs>%s</defs>' % m


def _mid(col):
    return {ACC2: 'ar', MUTED: 'arw', DARK: 'ag', ERR: 'are', OK: 'aro'}.get(col, 'ag')


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
            body += dashed(cx - hw - 4, ycl, cx - hw - 4, yl, MUTED, 1.4) + dashed(cx + hw + 4, ycl, cx + hw + 4, yl, MUTED, 1.4)
            body += arr(cx + hw + 20, yl, cx + hw + 20, ys, ACC2, 1.5, True) + text(cx + hw + 27, (yl + ys) / 2 + 5, 'd', 14, 'start', 800, ACC2)
            body += arr(cx + hw + 20, ycl, cx + hw + 20, yc - 3, ACC2, 1.5, True) + text(cx + hw + 27, (ycl + yc - 3) / 2 + 5, 'd', 14, 'start', 800, ACC2)
        b += frame(x, 55, 225, 290, t, ok=ok, body=body, cap=sub, capcol=OK if ok else ERR)
    return svg(760, 360, defs() + b, 'Smile line piatta, corretta (ripete la curva della cuticola) e troppo profonda')


@figx('french-punti-guida.svg')
def french_dots():
    b = title('French dipinto: metodo dei punti guida')
    heads = ['Punto centrale', 'Punti laterali', 'Collega', 'Riempi e sigilla']
    caps = ['il più basso della curva', 'alla stessa altezza', 'lato → centro', 'anche lo spessore della punta']
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
            body += brush_flat(cx + 8, ys - 6, -55, 70)
            for k, dx in enumerate((-22, -4, 14)):
                body += arr(cx + dx - 6, ys + 12, cx + dx - 6, ys - 16, DARK, 1.8)
        elif i == 2:
            # profilo in miniatura con apex
            ox, oy = x + 132, 92
            mini = box(ox - 8, oy - 26, 76, 44, '#fff', '#e5d6d2', 8)
            mini += '<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="3" stroke-linecap="round"/>' % (ox, oy + 6, ox + 60, oy + 6, NAIL_S)
            mini += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Q%.1f,%.1f %.1f,%.1f L%.1f,%.1f Z" fill="#f6b8c9" stroke="%s" stroke-width="1.2"/>' % (
                ox + 2, oy + 5, ox + 18, oy - 14, ox + 30, oy - 14, ox + 46, oy - 14, ox + 60, oy + 2, ox + 60, oy + 6, NAIL_S)
            mini += arr(ox + 30, oy - 26 + 2, ox + 30, oy - 16, ACC2, 1.4)
            body += mini + text(ox + 30, oy + 34, 'apex', 12.5, weight=700, fill=ACC2)
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
    cases = [('Graduale', True, 'passaggio morbido'), ('Si vede la linea', False, 'bianco coprente, poco sfumato'),
             ('Troppo bianco', False, 'sembra un french sbavato'), ('Gobba sulla punta', False, 'strati spessi sovrapposti')]
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
            pts = [(x + 46, 189), (x + 80, 180), (x + 120, 176), (x + 150, 172), (x + 168, 160), (x + 180, 162), (x + 186, 182)]
            body += sec + product(pts, 190, end_x=x + 182, end_y=196, fill='url(#sfp)', stroke=NAIL_S) + fd
            body += '<circle cx="%.1f" cy="%.1f" r="20" fill="none" stroke="%s" stroke-width="2.2" stroke-dasharray="4 3"/>' % (x + 172, 166, ERR)
            body += text(x + 103, 120, 'vista di profilo', 13, fill=MUTED, style='italic')
        b += frame(x, 55, 205, 260, t, ok=ok, body=body, cap=sub, capcol=OK if ok else ERR, hsize=14.5)
    return svg(900, 330, defs() + gdefs + b, 'Sfumatura del baby boomer: corretta e tre errori tipici')


@figx('incapsulato-sezione.svg')
def encaps():
    b = title('Incapsulato: com\'è fatto dentro')
    x0, y = 70, 210
    sec, fd, p = section(x0, y, L=280, F=40, body_h=70)
    xs, xt = p['xs'], p['xt']
    b += sec
    # 1 base sottile
    base = [(x0 + 6, y - 0.5), (x0 + 60, y - 5), (xs, y - 6), (xt + 10, y - 5)]
    b += product(base, y, end_x=xt + 12, end_y=y + 6)
    # 3 prodotto trasparente con apex in zona 2 (sopra il punto di stress)
    clear = [(x0 + 8, y - 6), (x0 + 70, y - 22), (x0 + 160, y - 40), (xs - 10, y - 44), (xs + 50, y - 36), (xt + 70, y - 18), (xt + 100, y - 6)]
    b += product(clear, y - 5, end_x=xt + 100, end_y=y + 6, fill='#eef7fc', stroke=PROD_S, extra=' opacity=".95"')
    # base disegnata di nuovo come linea per vederla sotto il trasparente
    b += '<path d="%s" fill="none" stroke="%s" stroke-width="1.5" stroke-dasharray="5 3"/>' % (smooth_d(base), PROD_S)
    # 2 decorazione piatta
    for k, gx in enumerate([x0 + 110, x0 + 140, x0 + 190, x0 + 215, xs + 20]):
        b += '<path d="M%.1f,%.1f l7,-4 l7,4 l-7,4 Z" fill="%s" stroke="%s" stroke-width="1"/>' % (gx, y - 9, GOLD, GOLD_S)
    fxc = x0 + 168
    b += '<ellipse cx="%.1f" cy="%.1f" rx="15" ry="3.2" fill="#f7a8c4" stroke="%s"/>' % (fxc, y - 9, ACC) + '<ellipse cx="%.1f" cy="%.1f" rx="4" ry="2" fill="%s"/>' % (fxc, y - 9, GOLD)
    # 5 top lucido
    topl = [(x + 0, yy - 3) for x, yy in clear]
    b += '<path d="%s" fill="none" stroke="#7fb0cc" stroke-width="2.5"/>' % smooth_d(clear)
    b += '<path d="%s" fill="none" stroke="#fff" stroke-width="1.5" opacity=".9"/>' % smooth_d([(px, py + 3) for px, py in clear[1:5]])
    b += fd
    # punto di stress
    b += stress_tri(xs, y + 9)
    ax = xs - 10
    b += arr(ax, y - 86, ax, y - 50, ACC2, 2)
    # richiami
    b += leader(x0 + 40, y - 3, 540, 88, 'Base / builder sottile')
    b += leader(x0 + 147, y - 9, 540, 126, 'Decorazione piatta')
    b += leader(x0 + 240, y - 28, 540, 164, 'Prodotto trasparente')
    b += leader(ax, y - 88, 540, 50 + 152, 'Apex sopra la decorazione')
    b += leader(xt + 60, y - 22, 540, 240, 'Top lucido')
    b += text(xs, y + 34, 'punto di stress', 12.5, weight=700, fill=ACC2)
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
    # --- pannello sinistro: dotting
    x = 20
    body = ''
    tb = 214
    body += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3"/>' % (x + 14, tb, x + 345, tb, GREY)
    # dito della cliente di profilo (unghia verso l'alto)
    body += '<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Z" fill="%s" stroke="%s" stroke-width="1.5"/>' % (
        x + 150, tb - 2, x + 150, tb - 30, x + 245, tb - 34, x + 250, tb - 2, x + 150, tb - 2, SKIN, SKIN_D)
    body += '<path d="M%d,%d Q%d,%d %d,%d" stroke="%s" stroke-width="5" fill="none" stroke-linecap="round"/>' % (x + 180, tb - 33, x + 215, tb - 38, x + 244, tb - 28, ACC)
    # mano dell'operatrice (stilizzata) + mignolo appoggiato
    hx, hy = x + 120, 112
    body += '<path d="M%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" fill="%s" stroke="%s" stroke-width="1.5"/>' % (
        hx - 70, hy + 10, hx - 30, hy - 30, hx + 70, hy - 12, hx + 86, hy + 16, hx + 30, hy + 40, hx - 60, hy + 40, SKIN, SKIN_D)
    body += '<rect x="%d" y="%d" width="16" height="%d" rx="8" fill="%s" stroke="%s" stroke-width="1.5"/>' % (hx - 46, hy + 26, tb - hy - 26, SKIN, SKIN_D)
    body += dotter(x + 213, tb - 46, -90, 96, 5)
    body += '<circle cx="%d" cy="%d" r="11" fill="%s" stroke="%s" stroke-width="1.4"/>' % (hx + 72, hy + 18, SKIN, SKIN_D)
    body += arr(x + 236, 90, x + 236, 140, DARK, 2)
    body += text(x + 246, 104, 'Dotter', 14, 'start', 700) + text(x + 246, 121, 'verticale', 14, 'start', 700)
    body += leader(hx - 38, tb - 10, x + 40, 250 - 6, 'Mignolo appoggiato', 'start', 13.5)
    # esempi
    ey = 288
    for k in range(5):
        body += '<circle cx="%d" cy="%d" r="7" fill="%s"/>' % (x + 40 + k * 22, ey, FUCHSIA)
    body += mark(x + 160, ey, True, 11)
    rng = [4, 9, 6, 11, 5]
    for k, r in enumerate(rng):
        body += '<circle cx="%d" cy="%d" r="%d" fill="%s"/>' % (x + 200 + k * 22, ey, r, FUCHSIA)
    body += mark(x + 320, ey, False, 11)
    b += frame(x, 55, 350, 290, 'Dotting', body=body, cap='ricarica a ogni punto', capcol=INK)
    # --- pannello destro: striping
    x = 390
    body = ''
    body += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3"/>' % (x + 14, tb, x + 345, tb, GREY)
    body += '<path d="M%d,%d L%d,%d Q%d,%d %d,%d L%d,%d Z" fill="%s" stroke="%s" stroke-width="1.5"/>' % (
        x + 60, tb - 2, x + 60, tb - 30, x + 155, tb - 34, x + 160, tb - 2, x + 60, tb - 2, SKIN, SKIN_D)
    body += '<path d="M%d,%d Q%d,%d %d,%d" stroke="%s" stroke-width="5" fill="none" stroke-linecap="round"/>' % (x + 90, tb - 33, x + 125, tb - 38, x + 154, tb - 28, ACC)
    body += brush_liner(x + 126, tb - 40, -35, 110)
    body += arr(x + 150, tb - 60, x + 96, tb - 60, DARK, 2.2)
    body += text(x + 190, 98, 'Trascina,', 14, 'start', 700) + text(x + 190, 115, 'non spingere', 14, 'start', 700)
    body += text(x + 190, 140, 'Pressione', 14, 'start', 700, MUTED) + text(x + 190, 157, 'costante', 14, 'start', 700, MUTED)
    body += text(x + 125, tb + 22, 'verso di te', 12.5, fill=MUTED, style='italic')
    body += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3" stroke-linecap="round"/>' % (x + 30, ey, x + 140, ey, FUCHSIA)
    body += mark(x + 160, ey, True, 11)
    wob = [(x + 200 + k * 6, ey + (3.5 if k % 2 else -3.5) * (1 if k % 3 else 0.4)) for k in range(19)]
    body += '<path d="%s" fill="none" stroke="%s" stroke-width="3" stroke-linecap="round"/>' % (smooth_d(wob), FUCHSIA)
    body += mark(x + 330, ey, False, 11)
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


def stamper(cx, cy, ang=0):
    """Tampone: manico + testa morbida arrotondata (testa verso il basso)."""
    return rot(ang, cx, cy, '<rect x="%.1f" y="%.1f" width="22" height="46" rx="5" fill="%s"/>' % (cx - 11, cy - 62, ACC2)
               + '<path d="M%.1f,%.1f L%.1f,%.1f Q%.1f,%.1f %.1f,%.1f Z" fill="#f3e9ee" stroke="#c9b3bd" stroke-width="1.5"/>' % (
                   cx - 20, cy - 18, cx + 20, cy - 18, cx, cy + 14, cx - 20, cy - 18))


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
            body += plate_disc(cx, cy + 6)
            body += '<path d="M%.1f,%.1f q8,4 18,-2 l2,10 q-10,5 -20,0 z" fill="%s" opacity=".9"/>' % (cx + 26, cy + 6, FUCHSIA)
            # raschietto inclinato a 45°
            body += rot(-45, cx - 6, cy - 14, '<rect x="%.1f" y="%.1f" width="70" height="12" rx="2" fill="#c9ccd1" stroke="%s"/>' % (cx - 41, cy - 20, GREY_D))
            body += '<path d="M%.1f,%.1f A30,30 0 0 0 %.1f,%.1f" fill="none" stroke="%s" stroke-width="1.8" stroke-dasharray="3 3"/>' % (cx + 28, cy - 14, cx + 15, cy - 35, ACC2)
            body += text(cx + 42, cy - 36, '45°', 14, weight=800, fill=ACC2)
            body += arr(cx - 46, cy + 66, cx + 34, cy + 66, DARK, 2)
        elif i == 2:
            body += plate_disc(cx, cy + 34, 40, False)
            body += stamp_pattern(cx, cy + 34, GREY_D)
            body += stamper(cx - 4, cy - 10, 12)
            body += carr('M%.1f,%.1f A40,40 0 0 1 %.1f,%.1f' % (cx - 46, cy - 6, cx + 44, cy - 6), DARK, 2)
        elif i == 3:
            f, p = nail(cx, cy + 110, hw=30, nail_len=90, free_len=36, plate=FUCHSIA, free=FUCHSIA, shape='squoval', finger_len=30)
            body += f
            body += stamper(cx + 4, cy - 44, -18)
            body += carr('M%.1f,%.1f A44,44 0 0 1 %.1f,%.1f' % (cx - 50, cy - 70, cx + 48, cy - 70), DARK, 2)
        else:
            f, p = nail(cx, cy + 110, hw=30, nail_len=90, free_len=36, plate=FUCHSIA, free=FUCHSIA, shape='squoval', finger_len=30,
                        extra='<g clip-path="url(#CLIP)">%s</g>' % stamp_pattern(cx, cy + 10))
            body += f + gloss(cx, cy - 18, cy + 60, 4) + sparkle(cx + 18, cy - 20, 6)
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
        hi.append((x, yb - t * (1 - u * u) ** 0.7))
    return '<path d="M%s Z" fill="%s"/>' % (' L'.join('%.1f,%.1f' % q for q in lo + hi[::-1]), col)


@figx('french-varianti.svg')
def french_variants():
    b = title('Varianti del french')
    names = ['Classico', 'A V', 'Micro', 'Reverse', 'Colorato', 'Doppio']
    for i, nm in enumerate(names):
        cx = 92 + i * 163
        yc, hw, nl, fl = 228, 32, 96, 74
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
                     '<g clip-path="url(#CLIP)"><g clip-path="url(#%s)"><path d="%s" fill="none" stroke="#fff" stroke-width="13"/></g></g>'
                     % (rc, cx - 60, top - 10, ys - 26 - top + 10, rc, out))
        elif i == 3:
            extra = reverse_cres(cx, yc, hw, 5, 20, ACC2)
        elif i == 4:
            extra = tip_fill(cx, ys, hw, 22, top, FUCHSIA, None)
        else:
            extra = tip_fill(cx, ys, hw, 22, top)
            pts = smile_pts(cx, ys + 12, hw, 22)
            extra += '<path d="M%s" fill="none" stroke="%s" stroke-width="3.5" clip-path="url(#CLIP)"/>' % (' L'.join('%.1f,%.1f' % q for q in pts), GOLD)
        f, p = nail(cx, yc, hw=hw, nail_len=nl, free_len=fl, shape='mandorla', plate=plate, free=plate, extra=extra, finger_len=34)
        b += f
        b += text(cx, 290, nm, 16, weight=800)
    return svg(1000, 305, b, 'Sei varianti del french: classico, a V, micro, reverse, colorato e doppio')


@figx('reverse-french-step.svg')
def reverse_steps():
    b = title('Reverse french')
    heads = ['Base + colore', 'Arco dal centro', 'Margine dalla pelle', 'Top opaco + lucido']
    caps = ['due strati sottili', 'poi verso i lati', None, 'mezzaluna lucida']
    for i in range(4):
        x = 20 + i * 218
        cx, yc, hw = x + 103, 268, 40
        nl, fl = 120, 40
        body = ''
        if i in (0, 1, 3):
            extra = ''
            if i >= 1:
                extra = reverse_cres(cx, yc, hw, 5, 22, ACC2)
            if i == 3:
                rng = random.Random(9)
                extra += '<g clip-path="url(#CLIP)">' + ''.join('<circle cx="%.1f" cy="%.1f" r="1" fill="#d9a99a"/>' % (cx + rng.uniform(-42, 42), yc - rng.uniform(40, 170)) for _ in range(90)) + '</g>'
                extra += '<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" stroke="#fff" stroke-width="3" fill="none" opacity=".9" stroke-linecap="round"/>' % (cx - 22, yc - 32, cx, yc - 44, cx + 20, yc - 34)
            f, p = nail(cx, yc, hw=hw, nail_len=nl, free_len=fl, shape='tonda', plate=NUDE, free=NUDE, extra=extra, finger_len=30)
            body += f
            if i == 1:
                y0 = cut_y(cx, yc, hw, cx) - 5 - 11
                body += arr(cx - 4, y0 - 26, cx - 34, y0 - 34, DARK, 1.8) + arr(cx + 4, y0 - 26, cx + 34, y0 - 34, DARK, 1.8)
                body += dot(cx, y0 - 22, 4.5, '#fff', ACC2)
                body += brush_liner(cx + 6, y0 - 10, -60, 70)
        else:
            # zoom sulla zona cuticolare
            zx, zy = x + 18, 92
            z = ''
            zc = uid('z')
            z += '<defs><clipPath id="%s"><rect x="%d" y="%d" width="170" height="120" rx="10"/></clipPath></defs>' % (zc, zx, zy)
            inner = '<rect x="%d" y="%d" width="170" height="120" fill="%s"/>' % (zx, zy, NUDE)
            ccx, base = zx + 85, zy + 150
            # arco della cuticola ingrandito
            arcpts = [(ccx + dx, base - 70 + (dx / 95.0) ** 2 * -40 + 40) for dx in range(-110, 111, 10)]
            skin = 'M%s L%.1f,%.1f L%.1f,%.1f Z' % (' L'.join('%.1f,%.1f' % q for q in arcpts), ccx + 110, zy + 140, ccx - 110, zy + 140)
            cres_lo = [(px, py - 12) for px, py in arcpts]
            cres_hi = [(px, py - 12 - 26 * max(0, 1 - ((px - ccx) / 110.0) ** 2)) for px, py in arcpts]
            inner += '<path d="M%s Z" fill="%s"/>' % (' L'.join('%.1f,%.1f' % q for q in cres_lo + cres_hi[::-1]), ACC2)
            inner += '<path d="%s" fill="%s" stroke="%s" stroke-width="2"/>' % (skin, SKIN, SKIN_D)
            z += '<g clip-path="url(#%s)">%s</g>' % (zc, inner)
            z += '<rect x="%d" y="%d" width="170" height="120" rx="10" fill="none" stroke="%s" stroke-width="1.5"/>' % (zx, zy, MUTED)
            my = base - 70 + 40
            z += arr(ccx + 30, my - 15, ccx + 30, my - 1, DARK, 1.6, True)
            z += text(ccx + 40, my - 4, '≈ 1 mm', 14, 'start', 800, INK)
            z += mark(zx + 152, zy + 18, True, 11)
            body += z
            # esempio sbagliato
            ex, ey = x + 18, 228
            w2 = box(ex, ey, 170, 66, '#fff', '#efc4bd', 10)
            ec = uid('z')
            inner2 = '<rect x="%d" y="%d" width="170" height="66" fill="%s"/>' % (ex, ey, NUDE)
            a2 = [(ex + 85 + dx, ey + 52 - 22 * (1 - (dx / 110.0) ** 2)) for dx in range(-110, 111, 10)]
            inner2 += '<path d="M%s L%.1f,%.1f L%.1f,%.1f Z" fill="%s" stroke="%s" stroke-width="2"/>' % (' L'.join('%.1f,%.1f' % q for q in a2), ex + 195, ey + 80, ex - 25, ey + 80, SKIN, SKIN_D)
            inner2 += '<path d="M%s Z" fill="%s" opacity=".95"/>' % (' L'.join('%.1f,%.1f' % q for q in [(px, py + 8) for px, py in a2] + [(px, py - 16) for px, py in a2[::-1]]), ACC2)
            w2 += '<defs><clipPath id="%s"><rect x="%d" y="%d" width="170" height="66" rx="10"/></clipPath></defs><g clip-path="url(#%s)">%s</g>' % (ec, ex, ey, ec, inner2)
            w2 += mark(ex + 152, ey + 16, False, 11) + text(ex + 10, ey + 20, 'tocca la pelle', 13, 'start', 800, ERR)
            body += w2
        b += frame(x, 55, 205, 260, heads[i], num=i + 1, body=body, cap=caps[i], capcol=INK, hsize=14.5)
    return svg(900, 330, defs() + b, 'Reverse french in quattro passaggi con margine di circa 1 mm dalla pelle')


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
