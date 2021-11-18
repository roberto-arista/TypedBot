import os
import drawBot as dB
dB.newPage(50, 50)
characters = "Aa今"
glyphNames = ["A", "a", "zzz"]
for fontName in ["Helvetica", "../data/MutatorSans.ttf"]:
    print(fontName)
    print(dB.font(fontName))
    print(fontName)
    dB.fontSize(50)
    for char in characters:
        print(dB.fontContainsCharacters(char))
    for glyphName in glyphNames:
        print(dB.fontContainsGlyph(glyphName))
    print(os.path.basename(dB.fontFilePath()))
    print(dB.listFontGlyphNames()[:6])
    print(dB.fontAscender())
    print(dB.fontDescender())
    print(dB.fontXHeight())
    print(dB.fontCapHeight())
    print(dB.fontLeading())
    print(dB.fontLineHeight())
    print()

for i in range(4):
    print(dB.font("../data/MutatorSans.ttc", fontNumber=i))
    print(dB.fontFilePath())
    print(os.path.basename(dB.fontFilePath()), dB.fontFileFontNumber())
    assert dB.fontFileFontNumber() == i

print()
for fontName in ["Courier", "Courier-Bold", "Courier-Oblique"]:
    dB.font(fontName)
    print(fontName, os.path.basename(dB.fontFilePath()), dB.fontFileFontNumber())
