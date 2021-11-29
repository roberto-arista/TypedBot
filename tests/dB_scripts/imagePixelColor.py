import drawBot as dB

canvasSize = 400
dB.newPage(canvasSize, canvasSize)

bands = 4
bandWidth = canvasSize / bands

dB.fontSize(10)

for i in range(bands):
    x = i * bandWidth
    for j in range(bands):
        y = j * bandWidth
        r = i / bands
        g = j / bands
        b = 0.5
        dB.fill(r, g, b)
        dB.rect(x, y, bandWidth, bandWidth)
        dB.fill(0)
        dB.text(f"{r},{g},{b}", (x + 3, y + 5))
