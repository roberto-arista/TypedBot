import noteBot as nB
nB.newPage(300, 300)
with nB.savedState():
    nB.fill(1, 0, 0)
    nB.translate(150, 150)
    nB.rect(0, 0, 100, 100)
    with nB.savedState():
        nB.rotate(45)
        nB.fill(0, 1, 0)
        nB.rect(0, 0, 100, 100)
nB.rect(0, 0, 100, 100)
