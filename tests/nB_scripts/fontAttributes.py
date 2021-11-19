import os
import noteBot as nB
nB.newPage(50, 50)
characters = "Aa今"
glyphNames = ["A", "a", "zzz"]
for fontName in ["Helvetica", "../data/MutatorSans.ttf"]:
    print(fontName)
    print(nB.font(fontName))
    nB.fontSize(50)
    for char in characters:
        print(nB.fontContainsCharacters(char))
    for glyphName in glyphNames:
        print(nB.fontContainsGlyph(glyphName))
    print(os.path.basename(nB.fontFilePath()))
    print(nB.listFontGlyphNames()[:6])
    print(nB.fontAscender())
    print(nB.fontDescender())
    print(nB.fontXHeight())
    print(nB.fontCapHeight())
    print(nB.fontLeading())
    print(nB.fontLineHeight())
    print()

for i in range(4):
    print(nB.font("../data/MutatorSans.ttc", fontNumber=i))
    print(os.path.basename(nB.fontFilePath()), nB.fontFileFontNumber())
    assert nB.fontFileFontNumber() == i

print()
for fontName in ["Courier", "Courier-Bold", "Courier-Oblique"]:
    nB.font(fontName)
    print(fontName, os.path.basename(nB.fontFilePath()), nB.fontFileFontNumber())
