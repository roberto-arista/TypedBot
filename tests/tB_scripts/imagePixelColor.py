import typedBot as tB
from typedBot import Color, Box, Point

canvasSize = 400
tB.newPage(canvasSize, canvasSize)

bands = 4
bandWidth = canvasSize / bands

tB.fontSize(10)

for i in range(bands):
    x = i * bandWidth
    for j in range(bands):
        y = j * bandWidth
        r = i / bands
        g = j / bands
        b = 0.5
        tB.fill(Color(r, g, b))
        tB.rect(Box(x, y, bandWidth, bandWidth))
        tB.fill(Color(0, 0, 0))
        tB.text(f"{r},{g},{b}", Point(x + 3, y + 5))
