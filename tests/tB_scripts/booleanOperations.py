import typedBot as tB

tB.newPage(600, 100)
p1 = tB.BezierPath()
p1.oval(tB.Box(5, 5, 70, 70))
p2 = tB.BezierPath()
p2.rect(tB.Box(25, 25, 70, 70))
tB.fill(tB.Color(r=0, g=0, b=0, a=0.3))
tB.stroke(tB.Color(r=0, g=0, b=0, a=1))

tB.drawPath(p1)
tB.drawPath(p2)

pUnion = p1.union(p2)
pIntersection = p1.intersection(p2)
pXor = p1.xor(p2)
pDiff1 = p1.difference(p2)
pDiff2 = p2.difference(p1)

for p in [pUnion, pIntersection, pXor, pDiff1, pDiff2]:
    tB.translate(tB.Point(x=100, y=0))
    tB.drawPath(p)
