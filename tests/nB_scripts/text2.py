import noteBot as nB

f = nB.FormattedString()
f.fontSize(40)
f.font("Helvetica")
f.align("left")
f.append("left\n")
f.align("center")
f.append("center\n")
f.font("Times")
f.align("right")
f.append("right\n")

_, height = f.size()
x, y = nB.width() * .25, 200

with nB.savedState():
    nB.stroke(0)
    nB.line((x, 0), (x, 1000))


nB.text(f, (x, y))
y += height
nB.text(f, (x, y), align="left")
y += height
nB.text(f, (x, y), align="center")
y += height
nB.text(f, (x, y), align="right")

x, y = nB.width() * .75, 200
with nB.savedState():
    nB.stroke(0)
    nB.line((x, 0), (x, 1000))

b = nB.BezierPath()
b.text(f)
b.text(f, offset=(0, height), align="left")
b.text(f, offset=(0, height * 2), align="center")
b.text(f, offset=(0, height * 3), align="right")
nB.translate(x, y)
nB.fill(1, 0, 0)
nB.drawPath(b)
