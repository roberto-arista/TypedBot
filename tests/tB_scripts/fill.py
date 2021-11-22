import typedBot as tB
tB.newPage(100, 100)
tB.fill(tB.Color(.5, .5, .5, .5))
tB.oval(tB.Box(0, 0, 100, 100))
for x in range(10):
    for y in range(10):
        tB.fill(tB.Color(x / 10, 1 - y / 10, y / 10, y / 20 + .5))
        tB.rect(tB.Box(x*10, y*10, 10, 10))
