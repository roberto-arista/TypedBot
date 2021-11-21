import noteBot as nB

nB.newPage(200, 200)

s = nB.FormattedString()
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

nB.textBox(s, nB.Box(20, 0, 200, 190))
