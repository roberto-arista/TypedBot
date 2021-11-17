#!/usr/bin/env python3

# ---- #
# Text #
# ---- #

# -- Modules -- #
from typing import Union, Optional, List, Tuple
from copy import deepcopy
from pathlib import Path

import drawBot as dB
from drawBot.context.baseContext import FormattedString as FS
from AppKit import NSMutableAttributedString, NSSize

from .structures import Color, CMYKColor, Alignment, OTFeature
from .structures import Underline, Tab, Point, Box


# -- Constants -- #
DrawbotTxt = Union[str, FormattedString]
FeaturesList = List[Tuple[OTFeature, bool]]


# -- Drawing Text -- #
def text(txt: DrawbotTxt, point: Point, align: Alignment = Alignment.left):
    dB.text(txt, point, align)

def textBox(txt: DrawbotTxt,
            box: Box,
            align: Alignment = Alignment.left) -> Optional[DrawbotTxt]:
    return dB.textBox(txt, box, align)

def textSize(txt: DrawbotTxt,
             align: Optional[Alignment] = None,
             width: Optional[float] = None,
             height: Optional[float] = None):
    dB.textSize(txt, align, width, height)

def textOverflow():
    pass

def textBoxBaselines():
    pass

def textBoxCharacterBounds():
    pass

def installedFonts(characters: Optional[str] = None) -> List[str]:
    return dB.installedFonts(characters)

def installFont(path: Path):
    dB.installFont(path=f'{path}')

def uninstallFont(path: Path):
    dB.installFont(f'{path}')


# -- Text Properties -- #
def font(fontNameOrPath: Union[str, Path],
         fontSize: Optional[float] = None,
         fontNumber: int = 0):
    fontNameOrPath = f'{fontNameOrPath}' if isinstance(fontNameOrPath, Path) else fontNameOrPath
    dB.font(fontNameOrPath, fontSize, fontNumber)

def fallbackFont(fontNameOrPath: Union[str, Path],
                 fontNumber: int = 0):
    fontNameOrPath = f'{fontNameOrPath}' if isinstance(fontNameOrPath, Path) else fontNameOrPath
    dB.fallbackFont(fontNameOrPath, fontNumber)

def fontSize(fontSize: float):
    dB.fontSize(fontSize)

def lineHeight(value: float):
    dB.lineHeight(value)

def tracking(value: float):
    dB.tracking(value)

def baselineShift(value: float):
    dB.baselineShift(value)

def underline(value: Underline):
    dB.underline(value)

def url(value: str):
    dB.url(value)

def hyphenation(value: bool):
    dB.hyphenation(value)

def tabs(*tabs: List[Tab]):
    dB.tabs(*tabs)

def language(language: str):
    dB.language(language)

def listLanguages(self) -> List[str]:
    return dB.listLanguages()

def openTypeFeatures(**features: FeaturesList):
    dB.openTypeFeatures(**features)

def resetFeatures():
    dB.openTypeFeatures(resetFeatures=True)

def listOpenTypeFeatures(fontNameOrPath: Optional[Union[str, Path]] = None):
    fontNameOrPath = f'{fontNameOrPath}' if isinstance(fontNameOrPath, Path) else fontNameOrPath
    dB.listOpenTypeFeatures(fontNameOrPath)

def fontVariations(*args, **axes):
    pass

def listFontVariations(fontNameOrPath: Optional[Union[str, Path]] = None) -> List:
    fontNameOrPath = f'{fontNameOrPath}' if isinstance(fontNameOrPath, Path) else fontNameOrPath
    return dB.listFontVariations(fontNameOrPath)

def listNamedInstances(fontNameOrPath: Optional[Union[str, Path]] = None) -> List[str]:
    fontNameOrPath = f'{fontNameOrPath}' if isinstance(fontNameOrPath, Path) else fontNameOrPath
    return dB.listNamedInstances(fontNameOrPath)


# -- Formatted String -- #
class FormattedString(FS):

    def __init__(self, txt: Union[str, FS] = "",
                       font: Optional[str] = None,
                       fontSize: float = 10,
                       fallbackFont: Optional[str] = None,
                       fill: Color = Color(r=0, g=0, b=0, a=1),
                       cmykFill: CMYKColor = CMYKColor(c=0, m=0, y=0, k=0, a=0),
                       stroke: Color = Color(r=0, g=0, b=0, a=0),
                       cmykStroke: CMYKColor = CMYKColor(c=0, m=0, y=0, k=0, a=0),
                       strokeWidth: float = 1,
                       align=Alignment.left,
                       lineHeight: float = 12,
                       tracking: float = 0,
                       baselineShift: float = 0,
                       openTypeFeatures=None,
                       tabs: List[Tab] = [],
                       language: Optional[str] = None,
                       indent: float = 0,
                       tailIndent: float = 0,
                       firstLineIndent: float = 0,
                       paragraphTopSpacing: float = 0,
                       paragraphBottomSpacing: float = 0):
        super().__init__(txt, font, fontSize, fallbackFont, fill, cmykFill, stroke, cmykStroke, strokeWidth, align, lineHeight, tracking, baselineShift, openTypeFeatures, tabs, language, indent, tailIndent, firstLineIndent, paragraphTopSpacing, paragraphBottomSpacing)

    def __add__(self, txt: DrawbotTxt):
        self.append(txt)

    def __getitem__(self, index: int) -> str:
        return super().__getitem__(index)

    def __len__(self) -> int:
        return len(super().__len__())

    def __repr__(self) -> str:
        return f"{super()}"

    def font(self, fontNameOrPath: str, fontSize: float = None, fontNumber: int = 0):
        super().font(fontNameOrPath, fontSize, fontNumber)

    def fallbackFont(self, fontNameOrPath: str, fontNumber: int = 0):
        super().fallbackFont(fontNameOrPath, fontNumber)

    def fontSize(self, fontSize: float):
        super().fontSize(fontSize)

    def fill(self, clr: Color):
        super().fill(*clr)

    def stroke(self, clr: Color):
        super().fill(*clr)

    def cmykFill(self, clr: CMYKColor):
        super().cmykFill(*clr)

    def cmykStroke(self, clr: CMYKColor):
        super().cmykStroke(*clr)

    def strokeWidth(self, strokeWidth: float):
        super().strokeWidth(strokeWidth)

    def align(self, align: Alignment):
        super().align(align)

    def lineHeight(self, lineHeight: float):
        super().lineHeight(lineHeight)

    def tracking(self, tracking: float):
        super().tracking(tracking)

    def baselineShift(self, baselineShift: float):
        super().baselineShift(baselineShift)

    def underline(self, underline: float):
        super().underline(underline)

    def url(self, url: str):
        super().url(url)

    def openTypeFeatures(self, features: FeaturesList):
        pass

    def resetFeatures(self):
        super().openTypeFeatures(resetFeatures=True)

    def listOpenTypeFeatures(self, fontNameOrPath: Optional[str] = None, fontNumber: int = 0) -> List[str]:
        return super().listOpenTypeFeatures(fontNameOrPath, fontNumber)

    def fontVariations(self, *args, **axes):
        pass

    def listFontVariations(self, fontNameOrPath: Optional[str] = None, fontNumber: int = 0) -> List[str]:
        return super().listFontVariations(fontNameOrPath, fontNumber)

    def listNamedInstances(self, fontNameOrPath: Optional[str] = None, fontNumber: int = 0) -> List[str]:
        return super().listNamedInstances(fontNameOrPath, fontNumber)

    def tabs(self, tabs: List[Tab]):
        pass

    def indent(self, indent: float):
        super().indent(indent)

    def tailIndent(self, indent: float):
        super().tailIndent(indent)

    def firstLineIndent(self, indent: float):
        super().firstLineIndent(indent)

    def paragraphTopSpacing(self, value: float):
        super().paragraphTopSpacing(value)

    def paragraphBottomSpacing(self, value: float):
        super().paragraphBottomSpacing(value)

    def language(self, language: str):
        super().language(language)

    def size(self) -> NSSize:
        return super().size()

    def getNSObject(self) -> NSMutableAttributedString:
        return super().getNSObject()

    def copy(self) -> FormattedString:
        return deepcopy(self)

    def fontContainsCharacters(self, characters: str) -> bool:
        return super().fontContainsCharacters(characters)

    def fontContainsGlyph(self, glyphName: str) -> bool:
        return super().fontContainsGlyph(glyphName)

    def fontFilePath(self) -> str:
        return super().fontFilePath()

    def fontFileFontNumber(self) -> int:
        return super().fontFileFontNumber()

    def listFontGlyphNames(self) -> List[str]:
        return super().listFontGlyphNames()

    def fontAscender(self) -> float:
        return super().fontAscender()

    def fontDescender(self) -> float:
        return super().fontDescender()

    def fontXHeight(self) -> float:
        return super().fontXHeight()

    def fontCapHeight(self) -> float:
        return super().fontCapHeight()

    def fontLeading(self) -> float:
        return super().fontLeading()

    def fontLineHeight(self) -> float:
        return super().fontLineHeight()

    def appendGlyph(self, *glyphNames: List[str]):
        super().appendGlyph(*glyphNames)
