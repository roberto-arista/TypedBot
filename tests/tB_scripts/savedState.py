import typedBot as tB
tB.newPage(200, 200)
tB.stroke(tB.Color(0, 0, 1))
tB.strokeWidth(5)

with tB.savedState():
    tB.fill(tB.Color(1, 0, 0))
    tB.translate(tB.Point(100, 100))
    tB.rect(tB.Box(0, 0, 100, 100))
tB.rect(tB.Box(0, 0, 100, 100))

with tB.savedState():
    tB.fill(tB.Color(0, 1, 0))
    tB.translate(tB.Point(100, 0))
    tB.rect(tB.Box(0, 0, 100, 100))
tB.rect(tB.Box(0, 100, 100, 100))
