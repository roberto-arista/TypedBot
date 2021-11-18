import noteBot as nB
nB.newPage(200, 200)

nB.newPath()
nB.moveTo((20, 20))
nB.lineTo((20, 100))
nB.lineTo((100, 100))
nB.lineTo((100, 180))
nB.curveTo((150, 180), (180, 150), (180, 100))
nB.lineTo((180, 20))
nB.closePath()

nB.moveTo((40, 40))
nB.lineTo((160, 40))
nB.curveTo((160, 65), (145, 80), (120, 80))
nB.lineTo((40, 80))
nB.closePath()

nB.fill(0.5, 0, 0)
nB.stroke(None)
nB.strokeWidth(10)
nB.drawPath()
