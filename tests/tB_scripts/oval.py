import typedBot as tB
tB.newPage(200, 200)
for i in range(14):
    f = i / 14.0
    tB.fill(tB.Color(1-f, 1 - f, 0))
    tB.oval(tB.Box(10, 10, 50, 50))
    tB.translate(tB.Point(10, 10))
