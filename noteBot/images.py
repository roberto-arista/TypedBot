#!/usr/bin/env python3

# ------ #
# Images #
# ------ #

# -- Modules -- #
from pathlib import Path
from typing import Optional

import drawBot as dB

from .structures import Point

# -- Objects, Functions, Procedures -- #
def image(path: Path, point: Point, alpha: float = 1, pageNumber: Optional[int] = None):
    if isinstance(path, Path):
        path = f'{path}'
    dB.image(path, point, alpha, pageNumber)
