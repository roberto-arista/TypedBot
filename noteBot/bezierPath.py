#!/usr/bin/env python3

# ---------- #
# BezierPath #
# ---------- #

# -- Modules -- #
from __future__ import annotations
from typing import Optional, List, Union, Tuple
from copy import deepcopy

from structures import Point, Box, Alignment, LineCap, LineJoin

from AppKit import NSBezierPath
from fontTools.misc import Transform
import drawBot as dB
from formattedString import FormattedString


class BezierPath(dB.BezierPath):

    def __init__(path: dB.BezierPath, glyphSet=Optional[List[str]]):
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
    def contours(self) -> Tuple[dB.BezierContour]:
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
