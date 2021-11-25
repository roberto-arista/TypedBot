import typedBot as tB

tB.newPage(600, 100)
p1 = tB.BezierPath()
p1.oval(tB.Box(5, 5, 70, 70))
p2 = tB.BezierPath()
p2.rect(tB.Box(25, 25, 70, 70))
tB.fill(tB.Color(0, 0, 0, 0.3))
tB.stroke(tB.Color(0, 0, 0, 1))

tB.drawPath(p1)
tB.drawPath(p2)

pUnion = p1 | p2
pIntersection = p1 & p2
pXor = p1 ^ p2
pDiff1 = p1 % p2
pDiff2 = p2 % p1

for p in [pUnion, pIntersection, pXor, pDiff1, pDiff2]:
    tB.translate(tB.Point(100, 0))
    tB.drawPath(p)
