import noteBot as nB
nB.newPage(200, 200)

nB.newPath()
nB.moveTo(nB.Point(20, 20))
nB.lineTo(nB.Point(20, 100))
nB.lineTo(nB.Point(100, 100))
nB.lineTo(nB.Point(100, 180))
nB.curveTo(nB.Point(150, 180), nB.Point(180, 150), nB.Point(180, 100))
nB.lineTo(nB.Point(180, 50))
nB.qCurveTo(nB.Point(180, 20), nB.Point(150, 20))

nB.fill(nB.Color(1, 0, 0))
nB.stroke(nB.Color(0, 0, 0))
nB.strokeWidth(10)
nB.drawPath()

nB.closePath()

nB.fill(nB.Color(0, 0, 0, 0))
nB.stroke(nB.Color(1, 1, 1, 1))
nB.translate(nB.Point(40, 15))
nB.scale(0.7, 0.7)
nB.lineCap(nB.LineCap.round)
nB.lineJoin(nB.LineJoin.round)

nB.drawPath()
