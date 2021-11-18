import noteBot as nB
nB.newPage(200, 200)
for i in range(14):
    f = i / 14.0
    nB.fill(f, 1 - f, 0)
    nB.rect(10, 10, 50, 50)
    nB.translate(10, 10)
