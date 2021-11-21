import noteBot as nB
nB.newPage(200, 200)
nB.stroke(nB.Color(0, 0, 1))
nB.strokeWidth(5)

with nB.savedState():
    nB.fill(nB.Color(1, 0, 0))
    nB.translate(nB.Point(100, 100))
    nB.rect(nB.Box(0, 0, 100, 100))
nB.rect(nB.Box(0, 0, 100, 100))

with nB.savedState():
    nB.fill(nB.Color(0, 1, 0))
    nB.translate(nB.Point(100, 0))
    nB.rect(nB.Box(0, 0, 100, 100))
nB.rect(nB.Box(0, 100, 100, 100))
