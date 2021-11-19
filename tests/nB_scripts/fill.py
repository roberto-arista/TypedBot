import noteBot as nB
nB.newPage(100, 100)
nB.fill(nB.Color(.5, .5, .5, .5))
nB.oval(nB.Box(0, 0, 100, 100))
for x in range(10):
    for y in range(10):
        nB.fill(nB.Color(x / 10, 1 - y / 10, y / 10, y / 20 + .5))
        nB.rect(nB.Box(x*10, y*10, 10, 10))
