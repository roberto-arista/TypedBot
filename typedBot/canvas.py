#!/usr/bin/env python3

# ------ #
# Canvas #
# ------ #


# -- Modules -- #
import os
from pathlib import Path
from typing import Dict, Optional, Union

from AppKit import NSColor, NSData, PDFDocument
from drawBot import _drawBotDrawingTool as dB
from fontTools.misc.transform import Transform

from .structures import WHITE, Box, Color, Point

# -- Constants -- #
ORIGIN = Point(0, 0)


# -- Pages -- #
def newPage(width: float, height: float):
    dB.newPage(width, height)


def newPageDefault(size: str):
    assert size in set(
        [
            "10x14",
            "10x14Landscape",
            "A0",
            "A0Landscape",
            "A1",
            "A1Landscape",
            "A2",
            "A2Landscape",
            "A3",
            "A3Landscape",
            "A4",
            "A4Landscape",
            "A4Small",
            "A4SmallLandscape",
            "A5",
            "A5Landscape",
            "B4",
            "B4Landscape",
            "B5",
            "B5Landscape",
            "Executive",
            "ExecutiveLandscape",
            "Folio",
            "FolioLandscape",
            "Ledger",
            "LedgerLandscape",
            "Legal",
            "LegalLandscape",
            "Letter",
            "LetterLandscape",
            "LetterSmall",
            "LetterSmallLandscape",
            "Quarto",
            "QuartoLandscape",
            "Statement",
            "StatementLandscape",
            "Tabloid",
            "TabloidLandscape",
        ]
    )
    dB.newPage(size)


def newDrawing():
    dB.newDrawing()


def endDrawing():
    dB.endDrawing()


def getSize(defaultSize: str) -> Box:
    wdt, hgt = dB.sizes(defaultSize)
    return Box(x=0, y=0, wdt=wdt, hgt=hgt)


def getAllSizes() -> Dict[str, Box]:
    allSizes = {}
    for name, (wdt, hgt) in dB.sizes().items():
        allSizes[name] = Box(x=0, y=0, wdt=wdt, hgt=hgt)
    return allSizes


def width() -> float:
    return dB.width()


def height() -> float:
    return dB.height()


def pageCount() -> int:
    return dB.pageCount()


def pages() -> int:
    return dB.pages()


def frameDuration(seconds: float):
    dB.frameDuration(seconds)


def linkURL(url: str, box: Box):
    dB.linkURL(url=url, xywh=box)


def linkRect(name: str, box: Box):
    dB.linkRect(name=name, xywh=box)


def linkDestination(name: str, pt: Point):
    dB.linkDestination(name=name, xy=pt)


# -- Transformations -- #
class SavedStateContextManager:
    def __enter__(self):
        save()
        return self

    def __exit__(self, type, value, traceback):
        restore()


def translate(pt: Point):
    dB.translate(x=pt.x, y=pt.y)


def rotate(angle: float, center: Point = ORIGIN):
    dB.rotate(angle, center)


def scale(x: float, y: float, center: Point = ORIGIN):
    dB.scale(x, y, center=center)


def skew(angle1: float, angle2: float = 0, center: Point = ORIGIN):
    dB.skew(angle1, angle2, center)


def transform(t: Transform):
    dB.transform(*t)


def savedState():
    return SavedStateContextManager()


def save():
    dB.save()


def restore():
    dB.restore()


# -- Transformations -- #
def printInstructions():
    dB.saveImage("*")


def savePDF(path: Path, multipage: bool = True):
    assert path.suffix.lower() == ".pdf"
    dB.saveImage(os.fspath(path), multipage=multipage)


def savePNG(
    path: Path,
    imageResolution: float = 72,
    antiAliasing: bool = True,
    multipage: bool = False,
    imagePNGGamma: float = None,
    imagePNGInterlaced=None,
    imageColorSyncProfileData=None,
):
    assert path.suffix.lower() == ".png"
    kwargs = dict(
        imageResolution=imageResolution,
        antiAliasing=antiAliasing,
        multipage=multipage,
        # imagePNGGamma=imagePNGGamma,
        # imagePNGInterlaced=imagePNGInterlaced,
        # imageColorSyncProfileData=imageColorSyncProfileData,
    )
    dB.saveImage(os.fspath(path), **kwargs)


def saveJPG(
    path: Path,
    imageResolution: float = 72,
    antiAliasing: bool = True,
    multipage: bool = False,
    imageJPEGCompressionFactor: float = 1.0,
    imageJPEGProgressive: bool = True,
    imageFallbackBackgroundColor: Union[NSColor, Color] = WHITE,
    imageColorSyncProfileData: Optional[NSData] = None,
):
    assert path.suffix.lower() == ".jpg"
    dB.saveImage(
        os.fspath(path),
        imageResolution,
        antiAliasing,
        multipage,
        imageJPEGCompressionFactor,
        imageJPEGProgressive,
        imageFallbackBackgroundColor,
        imageColorSyncProfileData,
    )


def saveTIF(
    path: Path,
    imageResolution: float = 72,
    antiAliasing: bool = True,
    multipage: bool = False,
    imageTIFFCompressionMethod: Optional[str] = None,
    imageColorSyncProfileData: Optional[NSData] = None,
):
    assert path.suffix.lower() in [".tif", ".tiff"]
    dB.saveImage(
        os.fspath(path), imageResolution, antiAliasing, multipage, imageTIFFCompressionMethod, imageColorSyncProfileData
    )


def saveSVG(path: Path, multipage: bool = False):
    assert path.suffix.lower() == ".svg"
    dB.saveImage(os.fspath(path), multipage)


def saveGIF(
    path: Path,
    imageResolution: float = 72,
    antiAliasing: bool = True,
    multipage: bool = False,
    imageGIFDitherTransparency: bool = False,
    imageGIFRGBColorTable: Optional[NSData] = None,
    imageColorSyncProfileData: Optional[NSData] = None,
    imageGIFLoop: bool = True,
):
    assert path.suffix.lower() == ".gif"
    dB.saveImage(
        os.fspath(path),
        imageResolution,
        antiAliasing,
        multipage,
        imageGIFDitherTransparency,
        imageGIFRGBColorTable,
        imageColorSyncProfileData,
        imageGIFLoop,
    )


def saveBMP(path: Path, imageResolution: float = 72, antiAliasing: bool = True, multipage: bool = False):
    assert path.suffix.lower() == ".bmp"
    dB.saveImage(os.fspath(path), imageResolution, antiAliasing, multipage)


def saveMP4(
    path,
    ffmpegCodec: str = "libx264",
    imageResolution: float = 72,
    antiAliasing: bool = True,
    imagePNGGamma: Optional[float] = None,
    imagePNGInterlaced: bool = True,
    imageColorSyncProfileData: Optional[NSData] = None,
):
    assert path.suffix.lower() == ".mp4"
    dB.saveImage(
        os.fspath(path),
        ffmpegCodec,
        imageResolution,
        antiAliasing,
        imagePNGGamma,
        imagePNGInterlaced,
        imageColorSyncProfileData,
    )


def saveICNS(path: Path, imageResolution: float = 72, antiAliasing: bool = True, multipage: bool = False):
    assert path.suffix.lower() == ".icns"
    dB.saveImage(os.fspath(path), imageResolution, antiAliasing, multipage)


def printImage(pdfPath: Optional[Path] = None):
    dB.printImage(f"{pdfPath}")


def pdfImage() -> PDFDocument:
    return dB.pdfImage()
