# grid.py <asset name> <out.jpg> [step] — overlay a labelled grid (source pixel coordinates) to find ring positions
import sys, os
from PIL import Image, ImageDraw
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
im = Image.open(os.path.join(D, 'assets', sys.argv[1] + '.jpg')).convert('RGB'); step = int(sys.argv[3]) if len(sys.argv) > 3 else 200
dr = ImageDraw.Draw(im)
for gx in range(0, im.width, step): dr.line([(gx, 0), (gx, im.height)], fill=(255, 0, 0), width=2); dr.text((gx + 4, 4), str(gx), fill=(255, 0, 0))
for gy in range(0, im.height, step): dr.line([(0, gy), (im.width, gy)], fill=(0, 0, 255), width=2); dr.text((4, gy + 4), str(gy), fill=(0, 0, 255))
im.thumbnail((1600, 1600)); im.save(sys.argv[2], quality=85)
