#!/usr/bin/env python3

# ------ #
# Colors #
# ------ #

# -- Modules -- #
from typing import Optional, List

import drawBot as dB

from .structures import Color, CMYKColor, Point

# -- Constants -- #
CMYK_TRANSPARENT = CMYKColor(c=0, m=0, y=0, k=0, a=0)

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

def cmykFill(color: CMYKColor):
    dB.cmykFill(*color)

def cmykStroke(color: CMYKColor):
    dB.cmykStroke(*color)

def cmykShadow(offset: float, blur: float = 0, color: CMYKColor = CMYK_TRANSPARENT):
    dB.cmykShadow(offset, blur, color)

def blendMode(operation: Optional[str]):
    assert operation in [None, 'normal', 'multiply', 'screen', 'overlay', 'darken', 'lighten', 'colorDodge', 'colorBurn', 'softLight', 'hardLight', 'difference', 'exclusion', 'hue', 'saturation', 'color', 'luminosity', 'clear', 'copy', 'sourceIn', 'sourceOut', 'sourceAtop', 'destinationOver', 'destinationIn', 'destinationOut', 'destinationAtop', 'xOR', 'plusDarker', 'plusLighter']
    dB.blendMode(operation)

def colorSpace(colorSpace: Optional[str]):
    assert colorSpace in [None, 'genericRGB', 'adobeRGB1998', 'sRGB', 'genericGray', 'genericGamma22Gray']
    dB.colorSpace(colorSpace)

def listColorSpaces() -> List[str]:
    return dB.listColorSpaces()
