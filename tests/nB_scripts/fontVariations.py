import noteBot as nB

nB.newPage(200, 200)

nB.font("Skia")
nB.fontSize(30)

nB.resetVariations()

variations = nB.listFontVariations()
for axisTag in sorted(variations):
    data = variations[axisTag]
    # we're rounding the values so we don't trip over small differences between OSes
    data['defaultValue'] = round(data['defaultValue'], 3)
    data['minValue'] = round(data['minValue'], 3)
    data['maxValue'] = round(data['maxValue'], 3)
    data['name'] = str(data['name'])
    print(axisTag, [(k, data[k]) for k in sorted(data)])

nB.text("Hello Q", nB.Point(20, 170))
nB.fontVariations(wght=0.6)
nB.text("Hello Q", nB.Point(20, 140))
nB.fontVariations(wght=2.4)
nB.text("Hello Q", nB.Point(20, 110))

nB.fontVariations(wdth=1.29)
nB.text("Hello Q", nB.Point(20, 80))

nB.resetVariations()
nB.fontVariations(wdth=0.6)
nB.text("Hello Q", nB.Point(20, 50))

nB.fontVariations(wght=2.8,)
nB.text("Hello Q", nB.Point(20, 20))
