#!/usr/bin/env python3

# ---------- #
# Structures #
# ---------- #

# -- Modules -- #
from dataclasses import dataclass, astuple
from enum import Enum, auto

class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

class Alignment(AutoName):
    left = auto()
    center = auto()
    right = auto()

class LineCap(AutoName):
    round = auto()

class LineJoin(AutoName):
    round = auto()


@dataclass
class Color:
    r: float
    g: float
    b: float
    a: float

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
