import typedBot as tB
tB.newDrawing()
tB.newPage(200, 200)

testData = [
    (tB.Box(25, 25, 50, 50),  "rotate", (20,),      tB.Point(25, 25)),
    (tB.Box(125, 25, 50, 50), "skew",   (10, 10),   tB.Point(175, 25)),
    (tB.Box(25, 125, 50, 50), "scale",  (1.2, 1.4), tB.Point(25, 175)),
]

for box, operation, args, center in testData:
    tB.fill(tB.Color(0, 0, 0, 1))
    bez = tB.BezierPath()
    bez.rect(box)
    tB.drawPath(bez)
    with tB.savedState():
        tB.fill(tB.Color(1, 0, 0, 0.5))
        bez = tB.BezierPath()
        bez.rect(box)
        getattr(bez, operation)(*args, center=center)
        tB.drawPath(bez)
