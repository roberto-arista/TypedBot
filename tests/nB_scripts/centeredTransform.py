import noteBot as nB
nB.newDrawing()
nB.newPage(200, 200)

def rotateScale(r: float, s: float, center: nB.Point):
    nB.rotate(r, center=center)
    nB.scale(s, s, center=center)


testData = [
    (nB.Box(25, 25, 50, 50),   nB.rotate,     (20,),      nB.Point(25, 25)),
    (nB.Box(125, 25, 50, 50),  nB.skew,       (10, 10),   nB.Point(175, 25)),
    (nB.Box(25, 125, 50, 50),  nB.scale,      (1.2, 1.4), nB.Point(25, 175)),
    (nB.Box(125, 125, 50, 50), rotateScale,   (20, 0.8),  nB.Point(175, 175)),
]

for box, operation, args, center in testData:
    nB.fill(nB.Color(0, 0, 0, 1))
    nB.rect(box)

    with nB.savedState():
        nB.fill(nB.Color(1, 0, 0, 0.5))
        operation(*args, center=center)
        nB.rect(box)
