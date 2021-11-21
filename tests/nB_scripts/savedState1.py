import noteBot as nB
nB.newPage(300, 300)
with nB.savedState():
    nB.fill(nB.Color(1, 0, 0))
    nB.translate(nB.Point(150, 150))
    nB.rect(nB.Box(0, 0, 100, 100))
    with nB.savedState():
        nB.rotate(45)
        nB.fill(nB.Color(0, 1, 0))
        nB.rect(nB.Box(0, 0, 100, 100))
nB.rect(nB.Box(0, 0, 100, 100))
