import noteBot as nB
nB.newPage(200, 200)
nB.stroke(nB.Color(0, 0, 0))
nB.strokeWidth(10)
nB.fill(nB.Color(1, 0.3, 0))
nB.polygon(nB.Point(40, 40), nB.Point(40, 160))
nB.polygon(nB.Point(60, 40), nB.Point(60, 160), nB.Point(130, 160))
nB.polygon(nB.Point(100, 40), nB.Point(160, 160), nB.Point(160, 40), close=False)
