import typedBot as tB

black = tB.Color(0, 0, 0)

f = tB.FormattedString()
f.fontSize(40)
f.font("Helvetica")
f.align(tB.Alignment.left)
f.append("left\n")
f.align(tB.Alignment.center)
f.append("center\n")
f.font("Times")
f.align(tB.Alignment.right)
f.append("right\n")

_, height = f.size()
x, y = tB.width() * .25, 200

with tB.savedState():
    tB.stroke(black)
    tB.line(tB.Point(x, 0), tB.Point(x, 1000))


tB.text(f, tB.Point(x, y))
y += height
tB.text(f, tB.Point(x, y), align=tB.Alignment.left)
y += height
tB.text(f, tB.Point(x, y), align=tB.Alignment.center)
y += height
tB.text(f, tB.Point(x, y), align=tB.Alignment.right)

x, y = tB.width() * .75, 200
with tB.savedState():
    tB.stroke(black)
    tB.line(tB.Point(x, 0), tB.Point(x, 1000))

b = tB.BezierPath()
b.text(f)
b.text(f, offset=tB.Point(0, height),     align=tB.Alignment.left)
b.text(f, offset=tB.Point(0, height * 2), align=tB.Alignment.center)
b.text(f, offset=tB.Point(0, height * 3), align=tB.Alignment.right)
tB.translate(tB.Point(x, y))
tB.fill(tB.Color(1, 0, 0))
tB.drawPath(b)
