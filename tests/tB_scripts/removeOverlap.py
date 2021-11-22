import typedBot as tB

tB.newPage(200, 100)

p = tB.BezierPath()
p.oval(tB.Box(5, 5, 70, 70))
p.rect(tB.Box(25, 25, 70, 70))
tB.fill(tB.Color(0, 0, 0, 0.3))
tB.stroke(tB.Color(0, 0, 0, 0))
tB.drawPath(p)
p.removeOverlap()
tB.translate(tB.Point(100, 0))
tB.drawPath(p)
