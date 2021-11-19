import noteBot as nB
nB.newDrawing()
nB.newPage(600, 100)
p1 = nB.BezierPath()
p1.oval(nB.Box(5, 5, 70, 70))
p2 = nB.BezierPath()
p2.rect(nB.Box(25, 25, 70, 70))
nB.fill(nB.Color(0, 0, 0, 0.3))
nB.stroke(nB.Color(0, 0, 0, 1))

nB.drawPath(p1)
nB.drawPath(p2)

pUnion = p1 | p2
pIntersection = p1 & p2
pXor = p1 ^ p2
pDiff1 = p1 % p2
pDiff2 = p2 % p1

for p in [pUnion, pIntersection, pXor, pDiff1, pDiff2]:
    nB.translate(nB.Point(100, 0))
    nB.drawPath(p)
