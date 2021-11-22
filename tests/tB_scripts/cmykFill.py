import typedBot as tB
tB.newPage(100, 100)
for x in range(10):
    for y in range(10):
        tB.cmykFill(tB.CMYKColor(x / 10, 1 - y / 10, y / 10, 0))
        tB.rect(tB.Box(x*10, y*10, 5, 10))
        tB.cmykFill(tB.CMYKColor(x / 10, 1 - y / 10, y / 10, 0.2))
        tB.rect(tB.Box(x*10 + 5, y*10, 5, 5))
        tB.cmykFill(tB.CMYKColor(x / 10, 1 - y / 10, y / 10, 0, 0.55))
        tB.rect(tB.Box(x*10 + 5, y*10 + 5, 5, 5))
