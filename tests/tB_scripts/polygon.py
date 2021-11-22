import typedBot as tB
tB.newPage(200, 200)
tB.stroke(tB.Color(0, 0, 0))
tB.strokeWidth(10)
tB.fill(tB.Color(1, 0.3, 0))
tB.polygon(tB.Point(40, 40), tB.Point(40, 160))
tB.polygon(tB.Point(60, 40), tB.Point(60, 160), tB.Point(130, 160))
tB.polygon(tB.Point(100, 40), tB.Point(160, 160), tB.Point(160, 40), close=False)
