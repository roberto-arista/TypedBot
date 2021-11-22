import typedBot as tB
tB.newDrawing()
tB.newPage(200, 200)

def rotateScale(r: float, s: float, center: tB.Point):
    tB.rotate(r, center=center)
    tB.scale(s, s, center=center)


testData = [
    (tB.Box(25, 25, 50, 50),   tB.rotate,     (20,),      tB.Point(25, 25)),
    (tB.Box(125, 25, 50, 50),  tB.skew,       (10, 10),   tB.Point(175, 25)),
    (tB.Box(25, 125, 50, 50),  tB.scale,      (1.2, 1.4), tB.Point(25, 175)),
    (tB.Box(125, 125, 50, 50), rotateScale,   (20, 0.8),  tB.Point(175, 175)),
]

for box, operation, args, center in testData:
    tB.fill(tB.Color(0, 0, 0, 1))
    tB.rect(box)

    with tB.savedState():
        tB.fill(tB.Color(1, 0, 0, 0.5))
        operation(*args, center=center)
        tB.rect(box)
