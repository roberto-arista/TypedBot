#!/usr/bin/env python3

# --------- #
# Run Tests #
# --------- #

# -- Modules -- #
import drawBot as dB
import noteBot as nB

from pathlib import Path
from importlib import import_module
from PIL import Image, ImageChops


# -- Helpers -- #
def runScriptAndSaveImage(path: Path, annotated: bool = False):
    mod = nB if annotated else dB
    mod.newDrawing()
    print(f"RUNNING: {path}")
    import_module(f'{path.parent}.{path.stem}')

    if annotated:
        mod.savePNG(path.with_suffix('.png'))
    else:
        mod.saveImage(path.with_suffix('.png'))

    mod.endDrawing()

def compareImages(path1: Path, path2: Path) -> bool:
    im1 = Image.open(path1)
    im2 = Image.open(path2)
    diff = ImageChops.difference(im1, im2)
    return False if diff.getbbox() else True


# -- Tests -- #
def runTests():
    for nbScript, dBScript in zip(noteBotScriptsFolder.glob('*.py'), drawBotScriptsFolder.glob('*.py')):
        assert nbScript.name == dBScript.name, 'mismatch in the scripts folders'
        if nbScript.name not in skip:
            runScriptAndSaveImage(path=nbScript, annotated=True)
            runScriptAndSaveImage(path=dBScript)
            assert compareImages(nbScript.with_suffix('.png'), dBScript.with_suffix('.png'))


# -- Variables -- #
noteBotScriptsFolder = Path('nB_scripts')
drawBotScriptsFolder = Path('dB_scripts')

skip = ['imageHTTP.py', 'fontAttributes.py', 'imagePixelColor.py',
        'image.py', 'image2.py', 'image3.py', 'image4.py', 'traceback.py']

# -- Instructions -- #
if __name__ == '__main__':
    runTests()