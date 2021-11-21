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

from .structures import Color, CMYKColor, Alignment
from .structures import Underline, Point, Box
from .shapes import BezierPath


# -- Drawing Text -- #
def text(txt, point: Point, align: Alignment = Alignment.left):
    if isinstance(txt, FormattedString):
        dB.text(txt.wrapped, point, align.name)
    else:
        dB.text(txt, point, align.name)

def textBox(txt, box: Box,
            align: Alignment = Alignment.left) -> str:
    if isinstance(txt, FormattedString):
        overflow = dB.textBox(txt.wrapped, box, align.name)
    else:
        overflow = dB.textBox(txt, box, align.name)
    return "" if not overflow else overflow

def textSize(txt: str,
             align: Optional[Alignment] = None,
             width: Optional[float] = None,
             height: Optional[float] = None):
    dB.textSize(txt, align.name if align else None, width, height)

def textOverflow(txt: str, box: Box, align: Alignment = Alignment.left) -> str:
    if isinstance(txt, FormattedString):
        overflow = dB.textOverflow(txt.wrapped, box, align.name)
    else:
        overflow = dB.textOverflow(txt, box, align.name)
    return "" if not overflow else overflow

def textBoxBaselines(txt: str, bounds: Union[Box, BezierPath], align: Alignment = Alignment.left) -> List[Point]:
    return [Point(*pp) for pp in dB.textBoxBaselines(txt, bounds, align)]

def textBoxCharacterBounds(txt: str, bounds: Union[Box, BezierPath], align: Alignment = Alignment.left) -> List[Box]:
    return [Box(*pp) for pp in dB.textBoxBaselines(txt, bounds, align)]

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

def tabs(*tabs: Tuple[float, Alignment]):
    dB.tabs(*[(tt, aa.name) for (tt, aa) in tabs])

def language(language: str):
    dB.language(language)

def listLanguages(self) -> List[str]:
    return dB.listLanguages()

def openTypeFeatures(**features: bool):
    dB.openTypeFeatures(**features)

def resetFeatures():
    dB.openTypeFeatures(resetFeatures=True)

def listOpenTypeFeatures(fontNameOrPath: Optional[Union[str, Path]] = None) -> List[str]:
    fontNameOrPath = f'{fontNameOrPath}' if isinstance(fontNameOrPath, Path) else fontNameOrPath
    return dB.listOpenTypeFeatures(fontNameOrPath)

def resetVariations():
    dB.fontVariations(None)

def fontVariations(**axes: float):
    dB.fontVariations(**axes)

def listFontVariations(fontNameOrPath: Optional[Union[str, Path]] = None) -> List:
    fontNameOrPath = f'{fontNameOrPath}' if isinstance(fontNameOrPath, Path) else fontNameOrPath
    return dB.listFontVariations(fontNameOrPath)

def listNamedInstances(fontNameOrPath: Optional[Union[str, Path]] = None) -> List[str]:
    fontNameOrPath = f'{fontNameOrPath}' if isinstance(fontNameOrPath, Path) else fontNameOrPath
    return dB.listNamedInstances(fontNameOrPath)


# -- Formatted String -- #
class FormattedString:

    """
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
    paragraphBottomSpacing: float = 0
    """

    def __init__(self, txt: Union[str, FS] = "", **kwargs):
        self.wrapped = dB.FormattedString(txt, **kwargs)

    def __add__(self, txt: str):
        self.wrapped.append(txt)

    def __getitem__(self, index: Union[int, slice]) -> str:
        return self.wrapped.__getitem__(index)

    def __len__(self) -> int:
        return self.wrapped.__len__()

    def __repr__(self) -> str:
        return f"{self.wrapped}"

    def append(self, txt, **kwargs):
        self.wrapped.append(txt, **kwargs)

    def font(self, fontNameOrPath: str, fontSize: float = None, fontNumber: int = 0):
        self.wrapped.font(fontNameOrPath, fontSize, fontNumber)

    def fallbackFont(self, fontNameOrPath: str, fontNumber: int = 0):
        self.wrapped.fallbackFont(fontNameOrPath, fontNumber)

    def fontSize(self, fontSize: float):
        self.wrapped.fontSize(fontSize)

    def fill(self, clr: Color):
        self.wrapped.fill(*clr)

    def stroke(self, clr: Color):
        self.wrapped.stroke(*clr)

    def cmykFill(self, clr: CMYKColor):
        self.wrapped.cmykFill(*clr)

    def cmykStroke(self, clr: CMYKColor):
        self.wrapped.cmykStroke(*clr)

    def strokeWidth(self, strokeWidth: float):
        self.wrapped.strokeWidth(strokeWidth)

    def align(self, align: Alignment):
        self.wrapped.align(align.name)

    def lineHeight(self, lineHeight: float):
        self.wrapped.lineHeight(lineHeight)

    def tracking(self, tracking: float):
        self.wrapped.tracking(tracking)

    def baselineShift(self, baselineShift: float):
        self.wrapped.baselineShift(baselineShift)

    def underline(self, underline: float):
        self.wrapped.underline(underline)

    def url(self, url: str):
        self.wrapped.url(url)

    def openTypeFeatures(self, **features: bool):
        self.wrapped.openTypeFeatures(**features)

    def resetFeatures(self):
        self.wrapped.openTypeFeatures(resetFeatures=True)

    def listOpenTypeFeatures(self, fontNameOrPath: Optional[str] = None, fontNumber: int = 0) -> List[str]:
        return self.wrapped.listOpenTypeFeatures(fontNameOrPath, fontNumber)

    def resetVariations(self):
        self.wrapped.fontVariations(resetVariations=True)

    def fontVariations(self, **axes: float):
        self.wrapped.fontVariations()

    def listFontVariations(self, fontNameOrPath: Optional[str] = None, fontNumber: int = 0) -> List[str]:
        return self.wrapped.listFontVariations(fontNameOrPath, fontNumber)

    def listNamedInstances(self, fontNameOrPath: Optional[str] = None, fontNumber: int = 0) -> List[str]:
        return self.wrapped.listNamedInstances(fontNameOrPath, fontNumber)

    def tabs(self, *tabs: Tuple[float, Alignment]):
        self.wrapped.tabs(*[(tt, aa.name) for (tt, aa) in tabs])

    def indent(self, indent: float):
        self.wrapped.indent(indent)

    def tailIndent(self, indent: float):
        self.wrapped.tailIndent(indent)

    def firstLineIndent(self, indent: float):
        self.wrapped.firstLineIndent(indent)

    def paragraphTopSpacing(self, value: float):
        self.wrapped.paragraphTopSpacing(value)

    def paragraphBottomSpacing(self, value: float):
        self.wrapped.paragraphBottomSpacing(value)

    def language(self, language: str):
        self.wrapped.language(language)

    def size(self) -> NSSize:
        return self.wrapped.size()

    def getNSObject(self) -> NSMutableAttributedString:
        return self.wrapped.getNSObject()

    def copy(self): # -> FormattedString:
        return deepcopy(self)

    def fontContainsCharacters(self, characters: str) -> bool:
        return self.wrapped.fontContainsCharacters(characters)

    def fontContainsGlyph(self, glyphName: str) -> bool:
        return self.wrapped.fontContainsGlyph(glyphName)

    def fontFilePath(self) -> str:
        return self.wrapped.fontFilePath()

    def fontFileFontNumber(self) -> int:
        return self.wrapped.fontFileFontNumber()

    def listFontGlyphNames(self) -> List[str]:
        return self.wrapped.listFontGlyphNames()

    def fontAscender(self) -> float:
        return self.wrapped.fontAscender()

    def fontDescender(self) -> float:
        return self.wrapped.fontDescender()

    def fontXHeight(self) -> float:
        return self.wrapped.fontXHeight()

    def fontCapHeight(self) -> float:
        return self.wrapped.fontCapHeight()

    def fontLeading(self) -> float:
        return self.wrapped.fontLeading()

    def fontLineHeight(self) -> float:
        return self.wrapped.fontLineHeight()

    def appendGlyph(self, *glyphNames: List[str]):
        self.wrapped.appendGlyph(*glyphNames)
