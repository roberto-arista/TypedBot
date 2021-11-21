import noteBot as nB

nB.newPage(200, 100)

p = nB.BezierPath()
p.oval(nB.Box(5, 5, 70, 70))
p.rect(nB.Box(25, 25, 70, 70))
nB.fill(nB.Color(0, 0, 0, 0.3))
nB.stroke(nB.Color(0, 0, 0, 0))
nB.drawPath(p)
p.removeOverlap()
nB.translate(nB.Point(100, 0))
nB.drawPath(p)
