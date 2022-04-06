#!/usr/bin/env python3

# --------- #
# Run Tests #
# --------- #

# -- Modules -- #
from importlib import import_module
from pathlib import Path

from drawBot import _drawBotDrawingTool as dB
from PIL import Image, ImageChops
from pytest import mark, param

import typedbot as tB

# -- Test Parameters -- #
TESTS_FOLDER = Path("tests")

data = [
    param("centeredTransformBezierPath.py"),
    param("booleanOperations.py"),
    param("booleanOperations2.py"),
    param("centeredTransform.py"),
    param("cmykFill.py"),
    param("cmykLinearGradient.py"),
    param("cmykRadialGradient.py"),
    param("fill.py"),
    param("fontPath.py"),
    param("fontVariations.py"),
    param("fontVariations2.py"),
    param("image.py"),
    param("image2.py"),
    param("image3.py"),
    param("image4.py"),
    param("imageHTTP.py"),
    param("imagePixelColor.py"),
    param("line.py"),
    param("linearGradient.py"),
    param("openTypeFeatures_kern.py"),
    param("openTypeFeatures.py"),
    param("openTypeFeatures2.py"),
    param("oval.py"),
    param("path.py"),
    param("pathWithCounter.py"),
    param("polygon.py"),
    param("radialGradient.py"),
    param("rect.py"),
    param("removeOverlap.py"),
    param("save.py"),
    param("save1.py"),
    param("savedState.py"),
    param("savedState1.py"),
    param("shapes.py"),
    param("text.py"),
    param("text2.py"),
]

# -- Helpers -- #
def runScriptAndSaveImage(path: Path, annotated: bool = False):
    mod = tB if annotated else dB
    mod.newDrawing()
    import_module(f"{path.parent.name}.{path.stem}")
    if annotated:
        imgPath = TESTS_FOLDER / "images" / f"{path.stem}_tB.png"
        mod.savePNG(imgPath)
    else:
        imgPath = TESTS_FOLDER / "images" / f"{path.stem}_dB.png"
        mod.saveImage(imgPath)
    mod.endDrawing()
    return imgPath


def compareImages(path1: Path, path2: Path) -> bool:
    im1 = Image.open(path1)
    im2 = Image.open(path2)
    diff = ImageChops.difference(im1, im2)
    return False if diff.getbbox() else True


# -- Tests -- #
@mark.parametrize("name", data)
def test_comparison(name):
    tBScript = TESTS_FOLDER / "tB_scripts" / name
    dBScript = TESTS_FOLDER / "dB_scripts" / name
    assert tBScript.exists()
    assert dBScript.exists()
    tB_path = runScriptAndSaveImage(path=tBScript, annotated=True)
    dB_path = runScriptAndSaveImage(path=dBScript)
    assert compareImages(tB_path, dB_path)
