# This is a test case derived from https://github.com/typemytype/drawbot/issues/171
# It ensures that rgb values specified in fill() end up in image output without
# being mangled by a color space (within 8-bit resulution).

import typedBot as tB
from PIL import Image
from pathlib import Path

canvasSize = 400
tB.newPage(canvasSize, canvasSize)

# colorSpace("sRGB")
# colorSpace("genericRGB")
# colorSpace("adobeRGB1998")

bands = 4
bandWidth = canvasSize / bands

tB.fontSize(10)

for i in range(bands):
    x = i * bandWidth
    for j in range(bands):
        y = j * bandWidth

        clr = tB.Color(i / bands, j / bands, 0.5)
        tB.fill(clr)
        tB.rect(tB.Box(x, y, bandWidth, bandWidth))
        tB.fill(tB.Color(0, 0, 0, 1))
        tB.text(f"{clr.r},{clr.g},{clr.b}", tB.Point(x + 3, y + 5))

fn = Path("../tempTestData/tmp_imagePixelColor.png")
tB.savePNG(fn)

im = Image.open(fn)

for i in range(bands):
    x = (i + 0.5) * bandWidth
    for j in range(bands):
        y = (j + 0.5) * bandWidth
        r, g, b, a = tB.imagePixelColor(fn, tB.Point(x, y))
        print(" CG:", round(r, 4), round(g, 4), round(b, 4))
        r, g, b, a = im.getpixel((x, canvasSize - y))
        print("PIL:", round(r/255, 4), round(g/255, 4), round(b/255, 4))
        print()
