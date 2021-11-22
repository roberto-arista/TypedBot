import typedBot as tB

tB.newPage(200, 200)

tB.font("Skia")
tB.fontSize(30)

tB.resetVariations()

variations = tB.listFontVariations()
for axisTag in sorted(variations):
    data = variations[axisTag]
    # we're rounding the values so we don't trip over small differences between OSes
    data['defaultValue'] = round(data['defaultValue'], 3)
    data['minValue'] = round(data['minValue'], 3)
    data['maxValue'] = round(data['maxValue'], 3)
    data['name'] = str(data['name'])
    print(axisTag, [(k, data[k]) for k in sorted(data)])

tB.text("Hello Q", tB.Point(20, 170))
tB.fontVariations(wght=0.6)
tB.text("Hello Q", tB.Point(20, 140))
tB.fontVariations(wght=2.4)
tB.text("Hello Q", tB.Point(20, 110))

tB.fontVariations(wdth=1.29)
tB.text("Hello Q", tB.Point(20, 80))

tB.resetVariations()
tB.fontVariations(wdth=0.6)
tB.text("Hello Q", tB.Point(20, 50))

tB.fontVariations(wght=2.8,)
tB.text("Hello Q", tB.Point(20, 20))
