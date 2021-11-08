#!/usr/bin/env python3

# ---------- #
# Structures #
# ---------- #

# -- Modules -- #
from dataclasses import dataclass, astuple


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
