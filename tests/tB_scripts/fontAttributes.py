import os
import typedBot as tB
tB.newPage(50, 50)
characters = "Aa今"
glyphNames = ["A", "a", "zzz"]
for fontName in ["Helvetica", "../data/MutatorSans.ttf"]:
    print(fontName)
    print(tB.font(fontName))
    tB.fontSize(50)
    for char in characters:
        print(tB.fontContainsCharacters(char))
    for glyphName in glyphNames:
        print(tB.fontContainsGlyph(glyphName))
    print(os.path.basename(tB.fontFilePath()))
    print(tB.listFontGlyphNames()[:6])
    print(tB.fontAscender())
    print(tB.fontDescender())
    print(tB.fontXHeight())
    print(tB.fontCapHeight())
    print(tB.fontLeading())
    print(tB.fontLineHeight())
    print()

for i in range(4):
    print(tB.font("../data/MutatorSans.ttc", fontNumber=i))
    print(os.path.basename(tB.fontFilePath()), tB.fontFileFontNumber())
    assert tB.fontFileFontNumber() == i

print()
for fontName in ["Courier", "Courier-Bold", "Courier-Oblique"]:
    tB.font(fontName)
    print(fontName, os.path.basename(tB.fontFilePath()), tB.fontFileFontNumber())
