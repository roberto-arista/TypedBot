import noteBot as nB
nB.newPage(200, 200)

nB.newPath()
nB.moveTo(nB.Point(20, 20))
nB.lineTo(nB.Point(20, 100))
nB.lineTo(nB.Point(100, 100))
nB.lineTo(nB.Point(100, 180))
nB.curveTo(nB.Point(150, 180), nB.Point(180, 150), nB.Point(180, 100))
nB.lineTo(nB.Point(180, 20))
nB.closePath()

nB.moveTo(nB.Point(40, 40))
nB.lineTo(nB.Point(160, 40))
nB.curveTo(nB.Point(160, 65), nB.Point(145, 80), nB.Point(120, 80))
nB.lineTo(nB.Point(40, 80))
nB.closePath()

nB.fill(nB.Color(0.5, 0, 0))
nB.stroke(nB.Color(0, 0, 0, 0))
nB.strokeWidth(10)
nB.drawPath()
