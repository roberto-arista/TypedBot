import typedBot as tB

tB.newPage(200, 200)

s = tB.FormattedString()
s.font("HoeflerText-Regular")
s.fontSize(20)

s.append("Hoefler Fact #123\n")

s.resetFeatures()

s.openTypeFeatures(dlig=True)
s.append("Hoefler Fact #123\n")

s.openTypeFeatures(lnum=True)
s.append("Hoefler Fact #123\n")

s.openTypeFeatures(liga=False)
s.append("Hoefler Fact #123\n")

s.openTypeFeatures(liga=False, dlig=True, resetFeatures=True)
s.append("Hoefler Fact #123\n")

s.append("Hoefler Fact #123\n", openTypeFeatures=dict(liga=False, resetFeatures=True))

s.append("Hoefler Fact #123\n", openTypeFeatures=dict(dlig=True, resetFeatures=False))

tB.textBox(s, tB.Box(20, 0, 200, 190))
