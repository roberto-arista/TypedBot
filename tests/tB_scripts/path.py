import typedBot as tB
tB.newPage(200, 200)

tB.newPath()
tB.moveTo(tB.Point(20, 20))
tB.lineTo(tB.Point(20, 100))
tB.lineTo(tB.Point(100, 100))
tB.lineTo(tB.Point(100, 180))
tB.curveTo(tB.Point(150, 180), tB.Point(180, 150), tB.Point(180, 100))
tB.lineTo(tB.Point(180, 50))
tB.qCurveTo(tB.Point(180, 20), tB.Point(150, 20))

tB.fill(tB.Color(1, 0, 0))
tB.stroke(tB.Color(0, 0, 0))
tB.strokeWidth(10)
tB.drawPath()

tB.closePath()

tB.fill(tB.Color(0, 0, 0, 0))
tB.stroke(tB.Color(1, 1, 1, 1))
tB.translate(tB.Point(40, 15))
tB.scale(0.7, 0.7)
tB.lineCap(tB.LineCap.round)
tB.lineJoin(tB.LineJoin.round)

tB.drawPath()
