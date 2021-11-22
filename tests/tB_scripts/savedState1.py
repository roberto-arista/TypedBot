import typedBot as tB
tB.newPage(300, 300)
with tB.savedState():
    tB.fill(tB.Color(1, 0, 0))
    tB.translate(tB.Point(150, 150))
    tB.rect(tB.Box(0, 0, 100, 100))
    with tB.savedState():
        tB.rotate(45)
        tB.fill(tB.Color(0, 1, 0))
        tB.rect(tB.Box(0, 0, 100, 100))
tB.rect(tB.Box(0, 0, 100, 100))
