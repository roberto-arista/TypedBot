import typedBot as tB
from typedBot import Color, Alignment

black = Color(0, 0, 0)
red = Color(1, 0, 0)

f = tB.FormattedString()
f.fontSize(40)

f.font("Helvetica")
f.align(Alignment.left)
f.append("left\n")

f.align(Alignment.center)
f.append("center\n")

f.font("Times")
f.align(Alignment.right)
f.append("right\n")

_, height = f.size()
x, y = tB.width() * .25, 200

with tB.savedState():
    tB.stroke(black)
    tB.line(tB.Point(x, 0), tB.Point(x, 1000))

tB.text(f, tB.Point(x, y))
y += height
tB.text(f, tB.Point(x, y), align=Alignment.left)
y += height
tB.text(f, tB.Point(x, y), align=Alignment.center)
y += height
tB.text(f, tB.Point(x, y), align=Alignment.right)

x, y = tB.width() * .75, 200
with tB.savedState():
    tB.stroke(black)
    tB.line(tB.Point(x, 0), tB.Point(x, 1000))

b = tB.BezierPath()
b.text(f)
b.text(f, offset=tB.Point(0, height),     align=Alignment.left)
b.text(f, offset=tB.Point(0, height * 2), align=Alignment.center)
b.text(f, offset=tB.Point(0, height * 3), align=Alignment.right)
tB.translate(tB.Point(x, y))
tB.fill(red)
tB.drawPath(b)
