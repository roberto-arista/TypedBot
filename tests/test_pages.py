#!/usr/bin/env python3

# -------------- #
# Canvas Outputs #
# -------------- #

# -- Modules -- #
import drawBot as dB
import typedBot as tB
from pytest import param, mark

paperSizes = ['10x14', '10x14Landscape', 'A0', 'A0Landscape', 'A1', 'A1Landscape',
              'A2', 'A2Landscape', 'A3', 'A3Landscape', 'A4', 'A4Landscape',
              'A4Small', 'A4SmallLandscape', 'A5', 'A5Landscape', 'B4', 'B4Landscape',
              'B5', 'B5Landscape', 'Executive', 'ExecutiveLandscape', 'Folio', 'FolioLandscape',
              'Ledger', 'LedgerLandscape', 'Legal', 'LegalLandscape', 'Letter', 'LetterLandscape',
              'LetterSmall', 'LetterSmallLandscape', 'Quarto', 'QuartoLandscape',
              'Statement', 'StatementLandscape', 'Tabloid', 'TabloidLandscape']

# -- Tests -- #
@mark.parametrize('name', [param(nn) for nn in paperSizes])
def test_defaultSize(name):
    dB.newDrawing()
    dB.newPage(name)

    tB.newDrawing()
    tB.newPageDefault(name)

    assert (dB.width(), dB.height()) == (tB.width(), tB.height())

    dB.endDrawing()
    tB.endDrawing()

def test_getAllSizes():
    tBSizes = tB.getAllSizes()
    dBSizes = dB.sizes()
    assert tBSizes.keys() == dBSizes.keys()
    for key in tBSizes.keys():
        tBBox = tBSizes[key]
        assert tuple([tBBox.wdt, tBBox.hgt]) == dBSizes[key]

def test_getSize():
    paperSize = 'A4'
    paperBox = tB.getSize(paperSize)
    assert tuple([paperBox.wdt, paperBox.hgt]) == dB.sizes(paperSize)

def test_width():
    dB.newPage(100, 100)
    tB.newPage(100, 100)
    assert dB.width() == tB.width()

def test_height():
    dB.newPage(100, 100)
    tB.newPage(100, 100)
    assert dB.height() == tB.height()

def test_pageCount():
    dB.newDrawing()
    tB.newDrawing()
    for ii in range(50):
        dB.newPage(100, 100)
        tB.newPage(100, 100)
    assert dB.pageCount() == tB.pageCount()
    dB.endDrawing()
    tB.endDrawing()
