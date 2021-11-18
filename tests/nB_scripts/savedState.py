import noteBot as nB
nB.newPage(200, 200)
nB.stroke(0, 0, 1)
nB.strokeWidth(5)
with nB.savedState():
    nB.fill(1, 0, 0)
    nB.translate(100, 100)
    nB.rect(0, 0, 100, 100)
nB.rect(0, 0, 100, 100)
with nB.savedState():
    nB.fill(0, 1, 0)
    nB.translate(100, 0)
    nB.rect(0, 0, 100, 100)
nB.rect(0, 100, 100, 100)
