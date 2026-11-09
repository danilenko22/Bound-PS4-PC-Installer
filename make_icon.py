"""Generates assets/app.ico: a neutral geometric icon (no game artwork)."""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

out = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent / "assets" / "app.ico")
size = 256
img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
d.rounded_rectangle([8, 8, size - 8, size - 8], radius=48, fill=(20, 22, 28, 255))
gold = (224, 160, 58, 255)
cx, cy = size // 2, size // 2
for i, r in enumerate((92, 64, 36)):
    pts = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
    if i % 2 == 0:
        d.polygon(pts, outline=gold, width=10)
    else:
        d.polygon(pts, fill=(232, 232, 236, 255))
d.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], fill=gold)
out.parent.mkdir(parents=True, exist_ok=True)
img.save(out, sizes=[(256, 256), (64, 64), (48, 48), (32, 32), (16, 16)])
print("icon:", out)
