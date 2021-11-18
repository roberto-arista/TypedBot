import noteBot as nB
nB.newPage(100, 100)
for x in range(10):
    for y in range(10):
        nB.cmykFill(nB.CMYKColor(x / 10, 1 - y / 10, y / 10, 0))
        nB.rect(nB.Box(x*10, y*10, 5, 10))
        nB.cmykFill(nB.CMYKColor(x / 10, 1 - y / 10, y / 10, 0.2))
        nB.rect(nB.Box(x*10 + 5, y*10, 5, 5))
        nB.cmykFill(nB.CMYKColor(x / 10, 1 - y / 10, y / 10, 0, 0.55))
        nB.rect(nB.Box(x*10 + 5, y*10 + 5, 5, 5))
