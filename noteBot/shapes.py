#!/usr/bin/env python3

# ------ #
# Shapes #
# ------ #

# -- Modules -- #
from __future__ import annotations
from typing import Optional, List, Union, Tuple

from .structures import Point, Box, Alignment, LineCap, LineJoin
from .text import FormattedString

from AppKit import NSBezierPath
from fontTools.misc.transform import Transform
import drawBot as dB
from drawBot.context.baseContext import BezierPath as BP
from drawBot.context.baseContext import BezierContour as BC


# -- Primitives -- #
def rect(box: Box):
    dB.rect(*box)

def oval(box: Box):
    dB.oval(*box)

def line(pt1: Point, pt2: Point):
    dB.line(pt1, pt2)

def polygon(*points: Point, close: bool = True):
    dB.polygon(*points, close=close)


# -- Drawing Paths -- #
def newPath():
    dB.newPath()

def moveTo(point: Point):
    dB.moveTo(point)

def lineTo(point: Point):
    dB.lineTo(point)

def curveTo(point1: Point, point2: Point, point3: Point):
    dB.curveTo(point1, point2, point3)

def qCurveTo(*points: Point):
    dB.qCurveTo(*points)

def arc(center: Point, radius: float, startAngle: float, endAngle: float, clockwise: bool):
    dB.arc(center, radius, startAngle, endAngle, clockwise)

def arcTo(point1: Point, point2: Point, radius: float):
    dB.arcTo(point1, point2, radius)

def closePath():
    dB.closePath()

def drawPath(path: Optional[BezierPath] = None):
    dB.drawPath(path)

def clipPath(path: Optional[BezierPath] = None):
    dB.clipPath(path)


# -- Path Properties -- #
def strokeWidth(value: float):
    dB.strokeWidth(value)

def miterLimit(value: float):
    dB.miterLimit(value)

def lineJoin(value: LineJoin):
    dB.lineJoin(value.name)

def lineCap(value: LineCap):
    dB.lineCap(value.name)

def lineDash(*values: float):
    dB.lineDash(*values)


# -- BezierPath -- #
class BezierPath:

    def __init__(self, path: Optional[BP] = None, glyphSet: Optional[List[str]] = None):
        self.wrapped = dB.BezierPath(path, glyphSet)

    def __add__(self, otherPath: BezierPath):
        new = self.copy()
        new.appendPath(otherPath)
        return new

    def __iadd__(self, otherPath: BezierPath):
        self.appendPath(otherPath)
        return self

    def __mod__(self, otherPath: BezierPath):
        return self.difference(otherPath)
    __rmod__ = __mod__

    def __imod__(self, otherPath: BezierPath):
        result = self.difference(otherPath)
        self.setNSBezierPath(result.getNSBezierPath())
        return self

    def __or__(self, otherPath: BezierPath):
        return self.union(otherPath)
    __ror__ = __or__

    def __ior__(self, otherPath: BezierPath):
        result = self.union(otherPath)
        self.setNSBezierPath(result.getNSBezierPath())
        return self

    def __and__(self, otherPath: BezierPath):
        return self.intersection(otherPath)
    __rand__ = __and__

    def __iand__(self, otherPath: BezierPath):
        result = self.intersection(otherPath)
        self.setNSBezierPath(result.getNSBezierPath())
        return self

    def __xor__(self, otherPath: BezierPath):
        return self.xor(otherPath)
    __rxor__ = __xor__

    def __ixor__(self, otherPath: BezierPath):
        result = self.xor(otherPath)
        self.setNSBezierPath(result.getNSBezierPath())
        return self

    def moveTo(self, point: Point):
        self.wrapped.moveTo(point)

    def lineTo(self, point: Point):
        self.wrapped.lineTo(point)

    def curveTo(self, *points: List[Point]):
        self.wrapped.curveTo(*points)

    def qCurveTo(self, *points: Point):
        self.wrapped.qCurveTo(*points)

    def closePath(self):
        self.wrapped.closePath()

    def beginPath(self, identifier: Optional[str] = None):
        self.wrapped.beginPath()

    def addPoint(self, point, segmentType=None, smooth=False, name=None, identifier=None, **kwargs):
        self.wrapped.addPoint()

    def endPath(self):
        self.wrapped.endPath()

    def addComponent(self, glyphName: str, transformation: Transform):
        self.wrapped.addComponent(glyphName, transformation)

    def drawToPen(self, pen):   # here a swift protocol would be great
        self.wrapped.drawToPen(pen)

    def drawToPointPen(self, pointPen):   # idem
        self.wrapped.drawToPointPen(pointPen)

    def arc(self, center, radius, startAngle, endAngle, clockwise):
        self.wrapped.arc(center, radius, startAngle, endAngle, clockwise)

    def arcTo(self, point1: Point, point2: Point, radius: float):
        self.wrapped.arcTo(point1, point2, radius)

    def rect(self, box: Box):
        self.wrapped.rect(*box)

    def oval(self, box: Box):
        self.wrapped.oval(*box)

    def line(self, point1: Point, point2: Point):
        self.wrapped.line(point1, point2)

    def polygon(self, *points: List[Point], close: bool = False):
        self.wrapped.polygon(*points, close=close)

    def text(self, txt: Union[FormattedString, str],
                   offset: Point = Point(0, 0),
                   font: Optional[str] = 'LucidaGrande',
                   fontSize: float = 10,
                   align=Alignment.left):
        if isinstance(txt, FormattedString):
            self.wrapped.text(txt.wrapped, offset=offset, font=font, fontSize=fontSize, align=align.name)
        else:
            self.wrapped.text(txt, offset=offset, font=font, fontSize=fontSize, align=align.name)

    def textBox(self, txt: Union[FormattedString, str],
                      box: Box,
                      font: Optional[str] = 'LucidaGrande',
                      fontSize: float = 10,
                      align: Alignment = Alignment.left,
                      hyphenation: bool = False):
        self.wrapped.textBox(txt, box, font, fontSize, f'{align}', hyphenation)

    def getNSBezierPath(self) -> NSBezierPath:
        return self.wrapped.getNSBezierPath()

    def setNSBezierPath(self, path: NSBezierPath):
        self.wrapped.setNSBezierPath(path)

    def pointInside(self, point: Point) -> bool:
        return self.wrapped.pointInside(point)

    def bounds(self) -> Box:
        x, y, wdt, hgt = self.wrapped.bounds()
        return Box(x=x, y=y, wdt=wdt, hgt=hgt)

    def controlPointBounds(self) -> Box:
        x, y, wdt, hgt = self.wrapped.controlPointBounds()
        return Box(x=x, y=y, wdt=wdt, hgt=hgt)

    def optimizePath(self):
        self.wrapped.optimizePath()

    def copy(self) -> BezierPath:
        new = BezierPath()
        new.wrapped = self.wrapped.copy()
        return new

    def reverse(self):
        self.wrapped.reverse()

    def appendPath(self, otherPath: BezierPath):
        self.wrapped.appendPath(otherPath)

    def translate(self, point: Point):
        self.wrapped.translate(*point)

    def rotate(self, angle: float, center: Point = Point(0, 0)):
        self.wrapped.rotate(angle, center)

    def scale(self, x: float, y: float, center: Point = Point(0, 0)):
        self.wrapped.scale(x, y)

    def skew(self, angle1: float, angle2: float = 0, center: Point = Point(0, 0)):
        self.wrapped.skew(angle1, angle2, center)

    def transform(self, matrix: Transform, center: Point = Point(0, 0)):
        self.wrapped.transform(matrix, center)

    def removeOverlap(self):
        self.wrapped.removeOverlap()

    # boolean operations
    def union(self, other: BezierPath):
        self.wrapped.union(other.wrapped)

    def difference(self, other: BezierPath):
        self.wrapped.difference(other.wrapped)

    def intersection(self, other: BezierPath):
        self.wrapped.intersection(other.wrapped)

    def xor(self, other: BezierPath):
        self.wrapped.xor(other.wrapped)

    def intersectionPoints(self, other: Optional[BezierPath]):
        self.wrapped.intersectionPoints(other.wrapped if other else None)

    def expandStroke(self, width: float,
                           lineCap: LineCap = LineCap.round,
                           lineJoin: LineJoin = LineJoin.round,
                           miterLimit: float = 10):
        self.wrapped.expandStroke(width, lineCap.name, lineJoin.name, miterLimit)

    @property
    def points(self) -> Tuple[Point, ...]:
        return tuple(Point(*pt) for pt in self.wrapped.points)

    @property
    def onCurvePoints(self) -> Tuple[Point, ...]:
        return tuple(Point(*pt) for pt in self.wrapped.onCurvePoints)

    @property
    def offCurvePoints(self) -> Tuple[Point, ...]:
        return tuple(Point(*pt) for pt in self.wrapped.offCurvePoints)

    @property
    def contours(self) -> Tuple[BC]:
        return self.wrapped.contours

    @property
    def svgClass(self) -> str:
        return self.wrapped.svgClass

    @property
    def svgID(self) -> str:
        return self.wrapped.svgID

    @property
    def svgLink(self) -> str:
        return self.wrapped.svgLink
