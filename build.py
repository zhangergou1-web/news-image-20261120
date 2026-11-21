#!/usr/bin/env python3
"""Draft generator for make.fun bounty 'Sum up 20 November's world news in one image'.
Builds a 1024x1024 front-page-style PNG. Stories verified from 2026-11-20 news
searches (oneturn.news, simplelife.news, appistos.gr, clearviewpolitics, The Register AU).
Regenerated Sat 2026-11-21 morning with Friday's closing numbers (Nasdaq -5.2%,
Anthropic -8.5% after debut) before submitting; deadline Sun 2026-11-22 08:00 CST (00:00 UTC).
Bounty rules (from the 19 Nov edition page): PNG/JPEG <= 1 MiB, <= 1024x1024;
entry is a program at main.py/main.ts in a public GitHub repo created after the
competition opens, OSI license, transcripts uploaded with submission.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

def font(size, bold=False):
    cands = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
    ]
    for c in cands:
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

img = Image.new("RGB", (W, H), "#f7f3ea")
d = ImageDraw.Draw(img)

# ---- masthead ----
d.rectangle([0, 0, W, 150], fill="#111111")
d.text((48, 26), "THE WORLD IN ONE DAY", font=font(54, True), fill="#f7f3ea")
d.text((48, 96), "FRIDAY, 20 NOVEMBER 2026", font=font(26, True), fill="#e8b23a")
d.text((W - 48, 100), "6 STORIES", font=font(24, True), fill="#f7f3ea", anchor="ra")

stories = [
    ("1", "COURTS", "World Court: Myanmar committed genocide", "The ICJ rules against Myanmar over the Rohingya — the first genocide finding against a state in the court's 80-year history.", "#8c2f2f"),
    ("2", "SUMMIT", "Trump, Xi & Putin sign nuclear declaration", "Three leaders meet in Shenzhen; nuclear war 'must never be fought.'", "#1f3a5f"),
    ("3", "MARKETS", "Sell-off sweeps Asia and Wall Street", "Nikkei -5.1%, Nasdaq -5.2%, S&P -3.7%; Anthropic -8.5% after its +17% debut.", "#14532d"),
    ("4", "UKRAINE", "Third strike on Crimea Bridge in four days", "Rail halted; Russian strikes damage embassies in Kyiv; Poland probes airspace.", "#7c4a12"),
    ("5", "GULF", "Houthi missiles hit Riyadh's finance district", "Missiles damage the PIF tower and other buildings in Riyadh.", "#4a2b6b"),
    ("6", "AMERICA", "Senate rejects limits on Iran war powers", "The 51–48 vote leaves the nine-month Iran war unchecked; the Pentagon puts its cost at $48.3 billion.", "#0f5257"),
]

# ---- lead story ----
x, y, w, h = 48, 178, 928, 210
d.rectangle([x, y, x + w, y + h], fill=stories[0][4])
d.text((x + 28, y + 18), "1  ·  THE HAGUE — WORLD COURT", font=font(22, True), fill="#e8b23a")
lines = wrap(d, stories[0][2], font(40, True), w - 56)
yy = y + 52
for ln in lines:
    d.text((x + 28, yy), ln, font=font(40, True), fill="white")
    yy += 46
deck = wrap(d, stories[0][3], font(21), w - 56)
yy += 4
for ln in deck:
    d.text((x + 28, yy), ln, font=font(21), fill="#f3e2e2")
    yy += 27

# ---- grid: 5 stories, two columns (last row one wide) ----
gx, gy = 48, 412
cw, ch, gap = 452, 168, 24
positions = [(gx, gy), (gx + cw + gap, gy),
             (gx, gy + ch + gap), (gx + cw + gap, gy + ch + gap),
             (gx, gy + 2 * (ch + gap))]
for (num, tag, head, deck, color), (px, py) in zip(stories[1:], positions):
    ww = w if num == "6" else cw
    d.rectangle([px, py, px + ww, py + ch], fill="white", outline="#d8d2c4", width=2)
    d.rectangle([px, py, px + 10, py + ch], fill=color)
    d.text((px + 26, py + 14), f"{num}  ·  {tag}", font=font(19, True), fill=color)
    lines = wrap(d, head, font(26, True), ww - 52)
    yy = py + 44
    for ln in lines[:2]:
        d.text((px + 26, yy), ln, font=font(26, True), fill="#111111")
        yy += 32
    dl = wrap(d, deck, font(18), ww - 52)
    for ln in dl[:2]:
        d.text((px + 26, yy), ln, font=font(18), fill="#444444")
        yy += 23

# ---- footer ----
fy = 412 + 2 * (ch + gap) + ch + 24
d.rectangle([0, fy, W, H], fill="#111111")
d.text((48, fy + 7), "Six stories that defined the day — courts, summits, markets and war.",
       font=font(20), fill="#f7f3ea")

img.save(OUT, optimize=True)
print(OUT, img.size, os.path.getsize(OUT), "bytes")
