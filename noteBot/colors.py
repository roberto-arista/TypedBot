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
def fill(color: Color):
    dB.fill(*color)

def stroke(color: Color):
    dB.stroke(*color)

def linearGradient(startPt: Point, endPoint: Point,
                   colors: List[Color], locations=List[float]):
    dB.linearGradient(startPt, endPoint, [tuple(c) for c in colors], locations)

def radialGradient(startPoint: Point, endPoint: Point,
                   colors=List[Color], locations=List[float],
                   startRadius: Optional[float] = 0, endRadius: Optional[float] = 100):
    dB.radialGradient(startPoint=startPoint, endPoint=endPoint,
                      colors=[tuple(c) for c in colors], locations=locations,
                      startRadius=startRadius, endRadius=endRadius)

def shadow(offset: Point, blur: Optional[float], color: Optional[Color]):
    dB.shadow(offset=offset, blur=blur, color=color)

def cmykFill(color: CMYKColor):
    dB.cmykFill(*color)

def cmykStroke(color: CMYKColor):
    dB.cmykStroke(*color)

def cmykLinearGradient(startPoint: Point, endPoint: Point, colors: List[CMYKColor], locations: List[float]):
    dB.cmykLinearGradient(startPoint, endPoint, [tuple(c) for c in colors], locations)

def cmykRadialGradient(startPoint: Point, endPoint: Point, colors: List[CMYKColor], locations: List[float], startRadius: float = 0, endRadius: float = 100):
    dB.cmykRadialGradient(startPoint, endPoint, [tuple(c) for c in colors], locations, startRadius, endRadius)

def cmykShadow(offset: float, blur: float = 0, color: CMYKColor = CMYK_TRANSPARENT):
    dB.cmykShadow(offset, blur, color)

def blendMode(operation: str):
    assert operation in ['normal', 'multiply', 'screen', 'overlay', 'darken', 'lighten', 'colorDodge', 'colorBurn', 'softLight', 'hardLight', 'difference', 'exclusion', 'hue', 'saturation', 'color', 'luminosity', 'clear', 'copy', 'sourceIn', 'sourceOut', 'sourceAtop', 'destinationOver', 'destinationIn', 'destinationOut', 'destinationAtop', 'xOR', 'plusDarker', 'plusLighter']
    dB.blendMode(operation)

def resetBlendMode():
    dB.blendMode(None)

def colorSpace(colorSpace: str):
    assert colorSpace in ['genericRGB', 'adobeRGB1998', 'sRGB', 'genericGray', 'genericGamma22Gray']
    dB.colorSpace(colorSpace)

def resetColorSpace():
    dB.colorSpace(None)

def listColorSpaces() -> List[str]:
    return dB.listColorSpaces()
