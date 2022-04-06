#!/usr/bin/env python3

# ---------- #
# Structures #
# ---------- #

# -- Modules -- #
from dataclasses import astuple, dataclass
from enum import Enum


# -- Structures + Enumerations -- #
class Alignment(Enum):
    left = "left"
    center = "center"
    right = "right"


class LineCap(Enum):
    round = "round"
    butt = "butt"
    square = "square"


class LineJoin(Enum):
    round = "round"
    miter = "miter"
    bevel = "bevel"


class Underline(Enum):
    single = "single"
    double = "double"
    thick = "thick"


# class OTFeature(AutoName):
#     c2pc = auto()
#     c2sc = auto()
#     calt = auto()
#     case = auto()
#     cpsp = auto()
#     cswh = auto()
#     dlig = auto()
#     frac = auto()
#     liga = auto()
#     lnum = auto()
#     onum = auto()
#     ordn = auto()
#     pnum = auto()
#     rlig = auto()
#     sinf = auto()
#     smcp = auto()
#     ss01 = auto()
#     ss02 = auto()
#     ss03 = auto()
#     ss04 = auto()
#     ss05 = auto()
#     ss06 = auto()
#     ss07 = auto()
#     ss08 = auto()
#     ss09 = auto()
#     ss10 = auto()
#     ss11 = auto()
#     ss12 = auto()
#     ss13 = auto()
#     ss14 = auto()
#     ss15 = auto()
#     ss16 = auto()
#     ss17 = auto()
#     ss18 = auto()
#     ss19 = auto()
#     ss20 = auto()
#     subs = auto()
#     sups = auto()
#     swsh = auto()
#     titl = auto()
#     tnum = auto()


@dataclass
class Color:
    r: float
    g: float
    b: float
    a: float = 1

    def __getitem__(self, index) -> float:
        return astuple(self)[index]

    def __iter__(self):
        return iter(astuple(self))


@dataclass
class CMYKColor:
    c: float
    m: float
    y: float
    k: float
    a: float = 1

    def __getitem__(self, index) -> float:
        return astuple(self)[index]

    def __iter__(self):
        return iter(astuple(self))


@dataclass
class Box:
    x: float
    y: float
    wdt: float
    hgt: float

    def __iter__(self):
        return iter(astuple(self))


@dataclass
class Point:
    x: float
    y: float

    def __iter__(self):
        return iter(astuple(self))


# -- Recurrent Colors -- #
WHITE = Color(r=1, g=1, b=1, a=1)
BLACK = Color(r=0, g=0, b=0, a=1)
TRANSPARENT = Color(r=0, g=0, b=0, a=0)
