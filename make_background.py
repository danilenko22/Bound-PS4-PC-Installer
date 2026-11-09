"""Generates assets/banner.png: original abstract artwork (no game assets).

Low-poly shards framing a bright sky, a red ribbon and distant blocks, in a warm palette.
Deterministic (fixed seed) so every build produces the same image.
"""
import math
import random
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1280, 480
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent / "assets" / "banner.png")
BG = (20, 22, 28)
rng = random.Random(7)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)
sky_top, sky_bottom = (246, 236, 222), (226, 196, 168)
for y in range(H):
    d.line([(0, y), (W, y)], fill=lerp(sky_top, sky_bottom, y / H))

# Distant city of blocks
for _ in range(420):
    x = rng.uniform(250, 1050)
    y = rng.uniform(H * 0.66, H * 0.86)
    w, h = rng.uniform(10, 34), rng.uniform(5, 14)
    shade = rng.choice([(196, 150, 128), (176, 120, 104), (210, 172, 150), (160, 104, 96)])
    d.rectangle([x, y, x + w, y + h], fill=shade)
img = img.filter(ImageFilter.GaussianBlur(1.2))
d = ImageDraw.Draw(img)

# Red ribbon: a gently curved band across the frame
ribbon = []
for i in range(41):
    t = i / 40
    x = -80 + t * (W + 160)
    y = H * 0.95 - t * H * 0.75 + math.sin(t * math.pi) * 40
    ribbon.append((x, y))
top = [(x, y - 16) for x, y in ribbon]
bottom = [(x, y + 16) for x, y in reversed(ribbon)]
d.polygon(top + bottom, fill=(214, 58, 44))
d.line(top, fill=(240, 96, 72), width=3)

# Shards framing the opening (left and right walls, top lip)
palette = [(120, 84, 86), (146, 104, 98), (176, 132, 118), (98, 66, 72), (198, 160, 140), (138, 76, 70)]


def shard(cx, cy, size):
    n = rng.randint(3, 5)
    base = rng.uniform(0, math.tau)
    pts = []
    for k in range(n):
        a = base + k * math.tau / n + rng.uniform(-0.4, 0.4)
        r = size * rng.uniform(0.55, 1.15)
        pts.append((cx + math.cos(a) * r, cy + math.sin(a) * r * rng.uniform(0.6, 1.2)))
    color = rng.choice(palette)
    d.polygon(pts, fill=color)
    hi = lerp(color, (255, 236, 220), 0.25)
    d.line(pts[:2], fill=hi, width=2)


for _ in range(140):
    side = rng.random()
    if side < 0.42:
        cx, cy = rng.uniform(-60, W * 0.24), rng.uniform(-40, H + 40)
    elif side < 0.84:
        cx, cy = rng.uniform(W * 0.76, W + 60), rng.uniform(-40, H + 40)
    else:
        cx, cy = rng.uniform(0, W), rng.uniform(-60, H * 0.16)
    shard(cx, cy, rng.uniform(40, 120))

# A few loose fragments floating in the opening
for _ in range(14):
    shard(rng.uniform(W * 0.3, W * 0.7), rng.uniform(H * 0.2, H * 0.7), rng.uniform(6, 16))

# Fade the bottom into the UI background
fade = Image.new("RGB", (W, H), BG)
mask = Image.new("L", (W, H))
md = ImageDraw.Draw(mask)
for y in range(H):
    t = max(0.0, (y - H * 0.55) / (H * 0.45))
    md.line([(0, y), (W, y)], fill=int(255 * t ** 1.6))
img = Image.composite(fade, img, mask)

# Title
font_path = Path(r"C:\Windows\Fonts\seguisb.ttf")
if font_path.exists():
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(str(font_path), 120)
    text = "B O U N D"
    tw = d.textlength(text, font=font)
    x, y = (W - tw) / 2, H * 0.62
    d.text((x + 4, y + 5), text, font=font, fill=(0, 0, 0))
    d.text((x, y), text, font=font, fill=(245, 236, 224))

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print("banner:", OUT)
