import noteBot as nB
nB.newPage(200, 200)
for i in range(14):
    f = i / 14.0
    nB.fill(nB.Color(f, 1 - f, 0))
    nB.rect(nB.Box(10, 10, 50, 50))
    nB.translate(nB.Point(10, 10))
