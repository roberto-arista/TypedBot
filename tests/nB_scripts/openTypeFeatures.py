import noteBot as nB

nB.newPage(200, 200)

# ['liga', 'dlig', 'tnum', 'pnum', 'titl', 'onum', 'lnum']

nB.font("HoeflerText-Regular")
nB.fontSize(20)
print(nB.listOpenTypeFeatures())

nB.text("Hoefler Fact #123", nB.Point(20, 170))

nB.resetFeatures()

nB.openTypeFeatures(dlig=True)
nB.text("Hoefler Fact #123", nB.Point(20, 140))

nB.openTypeFeatures(lnum=True)
nB.text("Hoefler Fact #123", nB.Point(20, 110))

nB.openTypeFeatures(liga=False)
nB.text("Hoefler Fact #123", nB.Point(20, 80))

nB.openTypeFeatures(liga=True, resetFeatures=False)
nB.text("Hoefler Fact #123", nB.Point(20, 50))

nB.openTypeFeatures(liga=False, resetFeatures=True)
nB.text("Hoefler Fact #123", nB.Point(20, 20))
