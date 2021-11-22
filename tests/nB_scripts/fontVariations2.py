import noteBot as nB

nB.newPage(200, 200)
s = nB.FormattedString()

s.font("Skia")
s.fontSize(30)
s.lineHeight(30)
s.resetVariations()

s.append("Hello Q\n")
s.fontVariations(wght=0.6)
s.append("Hello Q\n")
s.fontVariations(wght=2.4)
s.append("Hello Q\n")

s.append("Hello Q\n", fontVariations=dict(wdth=1.29))

s.resetVariations()
s.append("Hello Q\n", fontVariations=dict(wdth=0.6))

s.fontVariations(wght=2.8)
s.append("Hello Q\n")

nB.textBox(s, nB.Box(10, 0, 190, 193))
