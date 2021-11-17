#!/usr/bin/env python3

# ------ #
# Shapes #
# ------ #

# -- Modules -- #
from __future__ import annotations
from typing import Optional, List, Union, Tuple
from copy import deepcopy

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

def polygon(*points: List[Point], close: bool = True):
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

def qCurveTo(*points: List[Point]):
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
    dB.lineJoin(value)

def lineCap(value: LineCap):
    dB.lineCap(value)

def lineDash(*values: List[float]):
    dB.lineDash(*values)


# -- BezierPath -- #
class BezierPath(BP):

    def __init__(self, path: Optional[BP] = None, glyphSet: Optional[List[str]] = None):
        super().__init__(path=path, glyphSet=glyphSet)

    def moveTo(self, point: Point):
        super().moveTo(point)

    def lineTo(self, point: Point):
        super().lineTo(point)

    def curveTo(self, *points: List[Point]):
        super().curveTo(*points)

    def qCurveTo(self, *points: List[Point]):
        super().qCurveTo(*points)

    def closePath(self):
        super().closePath()

    def beginPath(self, identifier: Optional[str] = None):
        super().beginPath()

    def addPoint(point, segmentType=None, smooth=False, name=None, identifier=None, **kwargs):
        super().addPoint()

    def endPath(self):
        super().endPath()

    def addComponent(self, glyphName: str, transformation: Transform):
        super().addComponent(glyphName, transformation)

    def drawToPen(self, pen):   # here a swift protocol would be great
        super().drawToPen(pen)

    def drawToPointPen(self, pointPen):   # idem
        super().drawToPointPen(pointPen)

    def arc(center, radius, startAngle, endAngle, clockwise):
        super().arc(center, radius, startAngle, endAngle, clockwise)

    def arcTo(self, point1: Point, point2: Point, radius: float):
        super().arcTo(point1, point2, radius)

    def rect(self, box: Box):
        super().rect(*box)

    def oval(self, box: Box):
        super().oval(*box)

    def line(self, point1: Point, point2: Point):
        super().line(point1, point2)

    def polygon(self, *points: List[Point], close: bool = False):
        super().polygon(*points, close=close)

    def text(self, txt: Union[FormattedString, str],
                   offset: Point,
                   font: Optional[str] = 'LucidaGrande',
                   fontSize: float = 10):
        super().text(txt, offset, font, fontSize)

    def textBox(self, txt: Union[FormattedString, str],
                      box: Box,
                      font: Optional[str] = 'LucidaGrande',
                      fontSize: float = 10,
                      align: Alignment = Alignment.left,
                      hyphenation: bool = False):
        super().textBox(txt, box, font, fontSize, f'{align}', hyphenation)

    def getNSBezierPath(self) -> NSBezierPath:
        return super().getNSBezierPath()

    def setNSBezierPath(self, path: NSBezierPath):
        super().setNSBezierPath(path)

    def pointInside(self, point: Point):
        super().pointInside(xy=point)

    def bounds(self) -> Box:
        x, y, wdt, hgt = super().bounds()
        return Box(x=x, y=y, wdt=wdt, hgt=hgt)

    def controlPointBounds(self) -> Box:
        x, y, wdt, hgt = super().controlPointBounds()
        return Box(x=x, y=y, wdt=wdt, hgt=hgt)

    def optimizePath(self):
        super().optimizePath()

    def copy(self) -> BezierPath:
        return deepcopy(self)

    def reverse(self):
        super().reverse()

    def appendPath(self, otherPath: BezierPath):
        super().appendPath(otherPath)

    def translate(self, point: Point):
        super().translate(*point)

    def rotate(self, angle: float, center: Point = Point(0, 0)):
        super().rotate(angle, center)

    def scale(self, center: Point = Point(0, 0)):
        super().scale()

    def skew(self, angle1: float, angle2: float = 0, center: Point = Point(0, 0)):
        super().skew(angle1, angle2, center)

    def transform(self, matrix: Transform, center: Point = Point(0, 0)):
        super().transform(matrix, center)

    def union(other: BezierPath):
        super().union(other.super())

    def removeOverlap(self):
        super().removeOverlap()

    def difference(other: BezierPath):
        super().difference(other.super())

    def intersection(other: BezierPath):
        super().intersection(other.super())

    def xor(other: BezierPath):
        super().xor(other.super())

    def intersectionPoints(self, other: Optional[BezierPath]):
        super().intersectionPoints(other.super() if other else None)

    def expandStroke(self, width: float,
                           lineCap: LineCap = LineCap.round,
                           lineJoin: LineJoin = LineJoin.round,
                           miterLimit: float = 10):
        super().expandStroke()

    @property
    def points(self) -> Tuple[Point, ...]:
        return tuple(Point(*pt) for pt in super().points)

    @property
    def onCurvePoints(self) -> Tuple[Point, ...]:
        return tuple(Point(*pt) for pt in super().onCurvePoints)

    @property
    def offCurvePoints(self) -> Tuple[Point, ...]:
        return tuple(Point(*pt) for pt in super().offCurvePoints)

    @property
    def contours(self) -> Tuple[BC]:
        return super().contours

    @property
    def svgClass(self) -> str:
        return super().svgClass

    @property
    def svgID(self) -> str:
        return super().svgID

    @property
    def svgLink(self) -> str:
        return super().svgLink
