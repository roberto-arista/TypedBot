import noteBot as nB
nB.newPage(200, 200)

nB.newPath()
nB.moveTo((20, 20))
nB.lineTo((20, 100))
nB.lineTo((100, 100))
nB.lineTo((100, 180))
nB.curveTo((150, 180), (180, 150), (180, 100))
nB.lineTo((180, 50))
nB.qCurveTo((180, 20), (150, 20))

nB.fill(1, 0, 0)
nB.stroke(0)
nB.strokeWidth(10)
nB.drawPath()

nB.closePath()

nB.fill(None)
nB.stroke(1)
nB.translate(40, 15)
nB.scale(0.7)
nB.lineCap("round")
nB.lineJoin("round")

nB.drawPath()
