import typedBot as tB
tB.newPage(200, 200)

tB.newPath()
tB.moveTo(tB.Point(20, 20))
tB.lineTo(tB.Point(20, 100))
tB.lineTo(tB.Point(100, 100))
tB.lineTo(tB.Point(100, 180))
tB.curveTo(tB.Point(150, 180), tB.Point(180, 150), tB.Point(180, 100))
tB.lineTo(tB.Point(180, 20))
tB.closePath()

tB.moveTo(tB.Point(40, 40))
tB.lineTo(tB.Point(160, 40))
tB.curveTo(tB.Point(160, 65), tB.Point(145, 80), tB.Point(120, 80))
tB.lineTo(tB.Point(40, 80))
tB.closePath()

tB.fill(tB.Color(0.5, 0, 0))
tB.stroke(tB.Color(0, 0, 0, 0))
tB.strokeWidth(10)
tB.drawPath()
