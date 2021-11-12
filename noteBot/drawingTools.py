#!/usr/bin/env python3

# ------------ #
# DrawingTools #
# ------------ #

# -- Modules -- #
import drawBot as dB
from fontTools.misc.transform import Transform
from structures import Box, Color, Point
from collections.abc import Iterable
from typing import List, Optional, Dict


# -- Primitives -- #
def rect(box: Box):
    dB.rect(*box)

def oval(box: Box):
    dB.oval(*box)

def line(pt1: Point, pt2: Point):
    dB.line(pt1, pt2)

def polygon(*points: Iterable[Point], close: bool = True):
    dB.polygon(*points, close=close)


# -- Path Properties -- #
def strokeWidth(value: float):
    dB.strokeWidth(value)

def miterLimit(value: float):
    dB.miterLimit(value)

def lineJoin(value: float):
    dB.lineJoin(value)

def lineCap(value: float):
    dB.lineCap(value)

def lineDash(*values: Iterable[float]):
    dB.lineDash(*values)

# -- Colors -- #
def fill(color: Optional[Color]):
    if not color:
        dB.fill(color)
    else:
        dB.fill(*color)

def stroke(color: Optional[Color]):
    if not color:
        dB.stroke(color)
    else:
        dB.stroke(*color)

def linearGradient(startPt: Point, endPoint: Point,
                   colors: List[Color], locations=List[float]):
    dB.linearGradient(
        startPt=startPt,
        endPoint=endPoint,
        colors=colors,
        locations=locations,
    )

def radialGradient(startPoint: Point, endPoint: Point,
                   colors=List[Color], locations=List[float],
                   startRadius: Optional[float] = 0, endRadius: Optional[float] = 100):
    dB.radialGradient(startPoint=startPoint, endPoint=endPoint,
                      colors=colors, locations=locations,
                      startRadius=startRadius, endRadius=endRadius)

def shadow(offset: Point, blur: Optional[float], color: Optional[Color]):
    dB.shadow(offset=offset, blur=blur, color=color)

def blendMode(operation: Optional[str]):
    assert operation in [None, 'normal', 'multiply', 'screen', 'overlay', 'darken', 'lighten', 'colorDodge', 'colorBurn', 'softLight', 'hardLight', 'difference', 'exclusion', 'hue', 'saturation', 'color', 'luminosity', 'clear', 'copy', 'sourceIn', 'sourceOut', 'sourceAtop', 'destinationOver', 'destinationIn', 'destinationOut', 'destinationAtop', 'xOR', 'plusDarker', 'plusLighter']
    dB.blendMode(operation)

def colorSpace(colorSpace: Optional[str]):
    assert colorSpace in [None, 'genericRGB', 'adobeRGB1998', 'sRGB', 'genericGray', 'genericGamma22Gray']
    dB.colorSpace(colorSpace)

def listColorSpaces() -> List[str]:
    return dB.listColorSpaces()


# -- Pages -- #
def newPage(width: float, height: float):
    dB.newPage(width, height)

def newPageDefault(size: str):
    assert size in set(['10x14', '10x14Landscape', 'A0', 'A0Landscape', 'A1', 'A1Landscape',
                        'A2', 'A2Landscape', 'A3', 'A3Landscape', 'A4', 'A4Landscape',
                        'A4Small', 'A4SmallLandscape', 'A5', 'A5Landscape', 'B4', 'B4Landscape',
                        'B5', 'B5Landscape', 'Executive', 'ExecutiveLandscape', 'Folio', 'FolioLandscape',
                        'Ledger', 'LedgerLandscape', 'Legal', 'LegalLandscape', 'Letter', 'LetterLandscape',
                        'LetterSmall', 'LetterSmallLandscape', 'Quarto', 'QuartoLandscape',
                        'Statement', 'StatementLandscape', 'Tabloid', 'TabloidLandscape'])
    dB.newPage(size)

def newDrawing():
    dB.newDrawing()

def endDrawing():
    dB.endDrawing()

def getSize(defaultSize: str) -> Box:
    wdt, hgt = dB.sizes(defaultSize)
    return Box(x=0, y=0, wdt=wdt, hgt=hgt)

def getAllSizes() -> Dict[str, Box]:
    allSizes = {}
    for name, (wdt, hgt) in dB.sizes():
        allSizes[name] = Box(x=0, y=0, wdt=wdt, hgt=hgt)
    return allSizes

def width() -> float:
    return dB.width()

def height() -> float:
    return dB.height()

def pageCount() -> int:
    return dB.pageCount()

def pages() -> int:
    return dB.pages()

def frameDuration(seconds: float):
    dB.frameDuration(seconds)

def linkURL(url: str, box: Box):
    dB.linkURL(url=url, xywh=box)

def linkRect(name: str, box: Box):
    dB.linkRect(name=name, xywh=box)

def linkDestination(name: str, pt: Point):
    dB.linkDestination(name=name, xy=pt)


# -- Transformations -- #
origin = Point(0, 0)

def translate(pt: Point):
    dB.translate(x=pt.x, y=pt.y)

def rotate(angle: float, center: Point = origin):
    dB.rotate(angle, center)

def scale(x: float, y: float, center: Point = origin):
    dB.scale(x, y, center=center)

def skew(angle1: float, angle2: float = 0, center: Point = origin):
    dB.skew(angle1, angle2, center)

def transform(t: Transform):
    dB.transform(*t)

def savedState():
    dB.savedState()
