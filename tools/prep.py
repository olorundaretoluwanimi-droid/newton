#!/usr/bin/env python3
"""raw/* → assets/<name>.jpg for the page: longest side capped, pale scans (maps, patents, ads, documents) auto-contrasted
so they never read as blank white panels. Run with the library's Python (PIL): .venv/Scripts/python.exe tools/prep.py"""
import os, glob
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(os.path.join(D, 'assets'), exist_ok=True)
CAP = {'sanborn': 3400, 'pano1907': 3300, 'birdseye1868': 3600, 'patent': 2400}
PALE = ('sanborn', 'patent', 'ad', 'birdseye', 'ww1_maytag', 'pano1907')
for f in sorted(glob.glob(os.path.join(D, 'raw', '*'))):
    name, ext = os.path.splitext(os.path.basename(f))
    if ext.lower() not in ('.jpg', '.jpeg', '.png', '.tif', '.tiff'): continue
    out = os.path.join(D, 'assets', name + '.jpg')
    if os.path.exists(out) and os.path.getmtime(out) > os.path.getmtime(f): continue
    im = Image.open(f).convert('RGB')
    cap = next((v for k, v in CAP.items() if name.startswith(k)), 2600)
    if max(im.size) > cap: im.thumbnail((cap, cap), Image.LANCZOS)
    if name.startswith(PALE): im = ImageOps.autocontrast(im, cutoff=(1, 0.5))
    im.save(out, quality=90); print(name, im.size)
