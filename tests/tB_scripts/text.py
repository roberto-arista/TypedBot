import typedBot as tB

transparent = tB.Color(0, 0, 0, 0)

tB.newPage(200, 200)
tB.text("hello world", tB.Point(10, 10))
tB.fill(tB.Color(1, 0, 0))
tB.text("foo bar", tB.Point(10, 30))
tB.fill(tB.Color(1, 0, 1))
tB.stroke(tB.Color(0, 1, 0))
tB.strokeWidth(2)
tB.font("Times", 50)
tB.text("foo bar", tB.Point(10, 50))
tB.fill(transparent)
tB.stroke(tB.Color(0, 1, 0))
tB.strokeWidth(1)
tB.line(tB.Point(0, 50), tB.Point(tB.width(), 50))
tB.stroke(transparent)

import drawBot as dB
dB.stroke(None)

tB.fill(tB.Color(0, 1, 1))
tB.fontSize(20)
tB.text("foo bar", tB.Point(tB.width()*.5, 100), align=tB.Alignment.right)
tB.text("foo bar", tB.Point(tB.width()*.5, 120), align=tB.Alignment.center)
tB.text("foo bar", tB.Point(tB.width()*.5, 140), align=tB.Alignment.left)
# test empty text https://github.com/typemytype/drawbot/issues/389
tB.text("", tB.Point(0, 0))
