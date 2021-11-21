import noteBot as nB
nB.newDrawing()
nB.newPage(200, 200)

testData = [
    (nB.Box(25, 25, 50, 50),  "rotate", (20,),      nB.Point(25, 25)),
    (nB.Box(125, 25, 50, 50), "skew",   (10, 10),   nB.Point(175, 25)),
    (nB.Box(25, 125, 50, 50), "scale",  (1.2, 1.4), nB.Point(25, 175)),
]

for box, operation, args, center in testData:
    nB.fill(nB.Color(0, 0, 0, 1))
    bez = nB.BezierPath()
    bez.rect(box)
    nB.drawPath(bez)
    with nB.savedState():
        nB.fill(nB.Color(1, 0, 0, 0.5))
        bez = nB.BezierPath()
        bez.rect(box)
        getattr(bez, operation)(*args, center=center)
        nB.drawPath(bez)
