import noteBot as nB

black = nB.Color(0, 0, 0)

f = nB.FormattedString()
f.fontSize(40)
f.font("Helvetica")
f.align(nB.Alignment.left)
f.append("left\n")
f.align(nB.Alignment.center)
f.append("center\n")
f.font("Times")
f.align(nB.Alignment.right)
f.append("right\n")

_, height = f.size()
x, y = nB.width() * .25, 200

with nB.savedState():
    nB.stroke(black)
    nB.line(nB.Point(x, 0), nB.Point(x, 1000))


nB.text(f, nB.Point(x, y))
y += height
nB.text(f, nB.Point(x, y), align=nB.Alignment.left)
y += height
nB.text(f, nB.Point(x, y), align=nB.Alignment.center)
y += height
nB.text(f, nB.Point(x, y), align=nB.Alignment.right)

x, y = nB.width() * .75, 200
with nB.savedState():
    nB.stroke(black)
    nB.line(nB.Point(x, 0), nB.Point(x, 1000))

b = nB.BezierPath()
b.text(f)
b.text(f, offset=nB.Point(0, height),     align=nB.Alignment.left)
b.text(f, offset=nB.Point(0, height * 2), align=nB.Alignment.center)
b.text(f, offset=nB.Point(0, height * 3), align=nB.Alignment.right)
nB.translate(nB.Point(x, y))
nB.fill(nB.Color(1, 0, 0))
nB.drawPath(b)
