#!/usr/bin/env python3
"""Entry for make.fun bounty 'Sum up 20 November's world news in one image'.

Writes one image to /output/entry.png: a front-page-style summary of
Friday 20 November 2026, built from that day's verified headlines
(ICJ Myanmar genocide ruling; Shenzhen Trump-Xi-Putin declaration;
Asian market sell-off + Anthropic slides after debut; Crimea Bridge strike;
Houthi missiles in Riyadh; Senate Iran war-powers vote).

The image itself is stored in this repository as entry.png.b64 (base64),
so the whole entry is plain text; this program decodes it and writes the
PNG to the required output path. It runs offline and is deterministic:
every run writes the same bytes.
"""
import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png.b64")
DST = "/output/entry.png"

with open(SRC, "r", encoding="ascii") as f:
    data = base64.b64decode(f.read())

os.makedirs(os.path.dirname(DST), exist_ok=True)
with open(DST, "wb") as f:
    f.write(data)
print(f"Wrote {DST} ({len(data)} bytes)")
