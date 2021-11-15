#!/usr/bin/env python3

# ------ #
# Canvas #
# ------ #

# -- Modules -- #
from typing import Dict
from pathlib import Path

from AppKit import NSPDFDocument
import drawBot as dB
from fontTools.misc.transform import Transform

from .structures import Box, Point

# -- Constants -- #
ORIGIN = Point(0, 0)

# -- Pages -- #
def newPage(width: float, height: float):
    dB.newPage(width, height)

def newPageDefault(size: str):
    assert size in set(['10x14', '10x14Landscape', 'A0', 'A0Landscape', 'A1', 'A1Landscape',
                        'A2', 'A2Landscape', 'A3', 'A3Landscape', 'A4', 'A4Landscape',
                        'A4Small', 'A4SmallLandscape', 'A5', 'A5Landscape', 'B4', 'B4Landscape',
                        'B5', 'B5Landscape', 'Executive', 'ExecutiveLandscape', 'Folio', 'FolioLandscape',
                        'Ledger', 'LedgerLandscape', 'Legal', 'LegalLandscape', 'Letter', 'LetterLandscape',
                        'LetterSmall', 'LetterSmallLandscape', 'Quarto', 'QuartoLandscape',
                        'Statement', 'StatementLandscape', 'Tabloid', 'TabloidLandscape'])
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
    for name, (wdt, hgt) in dB.sizes():
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
    dB.savedState()

# -- Transformations -- #
def printInstructions():
    dB.saveImage('*')

def savePDF(path: Path, multipage: bool = True):
    assert(path.suffix.lower() == '.pdf')
    dB.saveImage(f'{path}', multipage=multipage)

def savePNG(path: Path, imageResolution: float = 72,
                        antiAliasing: bool = True,
                        multipage: bool = False,
                        imagePNGGamma: float,
                        imagePNGInterlaced,
                        imageColorSyncProfileData):
    assert(path.suffix.lower() == '.png')
    dB.saveImage(f'{path}', imageResolution, antiAliasing, multipage, imagePNGGamma, imagePNGInterlaced, imageColorSyncProfileData)

def saveJPG(path: Path, imageResolution: float = 72,
                        antiAliasing: bool = True,
                        multipage: bool = False,
                        imageJPEGCompressionFactor: float,
                        imageJPEGProgressive: bool,
                        imageFallbackBackgroundColor: Union[NSColor, Color]
                        imageColorSyncProfileData: NSData):
    assert(path.suffix.lower() == '.jpg')
    dB.saveImage(f'{path}', imageResolution, antiAliasing, multipage, imageJPEGCompressionFactor, imageJPEGProgressive, imageFallbackBackgroundColor, imageColorSyncProfileData)

def saveTIF(path: Path, imageResolution: float = 72,
                        antiAliasing: bool = True,
                        multipage: bool = False,
                        imageTIFFCompressionMethod,
                        imageColorSyncProfileData)
    assert(path.suffix.lower() in ['.tif', '.tiff'])
    dB.saveImage(f'{path}', imageResolution, antiAliasing, multipage, imageJPEGCompressionFactor, imageJPEGProgressive, imageFallbackBackgroundColor, imageColorSyncProfileData)

def saveSVG(path: Path, multipage: bool = False)
    assert(path.suffix.lower() == '.svg')
    dB.saveImage(f'{path}', multipage)

def saveGIF(path: Path, imageResolution: float = 72,
                        antiAliasing: bool = True,
                        multipage: bool = False,
                        imageGIFDitherTransparency: bool,
                        imageGIFRGBColorTable: NSData,
                        imageColorSyncProfileData: NSData,
                        imageGIFLoop: bool)
    assert(path.suffix.lower() == '.gif')
    dB.saveImage(f'path', imageResolution, antiAliasing, multipage, imageGIFDitherTransparency, imageGIFRGBColorTable, imageColorSyncProfileData, imageGIFLoop)

def saveBMP(path: Path, imageResolution: float = 72,
                        antiAliasing: bool = True,
                        multipage: bool = False):
    assert(path.suffix.lower() == '.bmp')
    dB.saveImage(path, imageResolution, antiAliasing, multipage)

def saveMP4(path, ffmpegCodec: str = 'libx264',
                  imageResolution: float = 72,
                  antiAliasing: bool = True,
                  imagePNGGamma: float,
                  imagePNGInterlaced: bool,
                  imageColorSyncProfileData: NSData):
    assert(path.suffix.lower() == '.mp4')
    dB.saveImage(path, ffmpegCodec, imageResolution, antiAliasing, imagePNGGamma, imagePNGInterlaced, imageColorSyncProfileData)

def saveBMP(path: Path, imageResolution: float = 72,
                        antiAliasing: bool = True,
                        multipage: bool = False):
    assert(path.suffix.lower() == '.icns')
    dB.saveImage(path, imageResolution, antiAliasing, multipage)

def printImage(pdf: Optional[Path] = None):
    if isinstance(pdf, Path):
        pdf = f'{pdf}'
    dB.printImage(pdf)

def pdfImage() -> NSPDFDocument:
    return dB.pdfImage()
