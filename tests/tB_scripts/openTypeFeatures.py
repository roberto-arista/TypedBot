import typedBot as tB

tB.newPage(200, 200)

# ['liga', 'dlig', 'tnum', 'pnum', 'titl', 'onum', 'lnum']

tB.font("HoeflerText-Regular")
tB.fontSize(20)
print(tB.listOpenTypeFeatures())

tB.text("Hoefler Fact #123", tB.Point(20, 170))

tB.resetFeatures()

tB.openTypeFeatures(dlig=True)
tB.text("Hoefler Fact #123", tB.Point(20, 140))

tB.openTypeFeatures(lnum=True)
tB.text("Hoefler Fact #123", tB.Point(20, 110))

tB.openTypeFeatures(liga=False)
tB.text("Hoefler Fact #123", tB.Point(20, 80))

tB.openTypeFeatures(liga=True, resetFeatures=False)
tB.text("Hoefler Fact #123", tB.Point(20, 50))

tB.openTypeFeatures(liga=False, resetFeatures=True)
tB.text("Hoefler Fact #123", tB.Point(20, 20))
