import noteBot as nB
nB.newDrawing()
nB.newPage(200, 200)

def rotateScale(r, s, center):
    nB.rotate(r, center=center)
    nB.scale(s, center=center)


testData = [
    ((25, 25, 50, 50), nB.rotate, (20,), (25, 25)),
    ((125, 25, 50, 50), nB.skew, (10, 10), (175, 25)),
    ((25, 125, 50, 50), nB.scale, (1.2, 1.4), (25, 175)),
    ((125, 125, 50, 50), rotateScale, (20, 0.8), (175, 175)),
]

for r, op, args, center in testData:
    nB.fill(0)
    nB.rect(*r)
    with nB.savedState():
        nB.fill(1, 0, 0, 0.5)
        op(*args, center=center)
        nB.rect(*r)
