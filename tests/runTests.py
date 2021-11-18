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

# -- Constants -- #

# -- Objects, Functions, Procedures -- #
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


# -- Variables -- #
noteBotScriptsFolder = Path('nB_scripts')
drawBotScriptsFolder = Path('dB_scripts')

# -- Instructions -- #
if __name__ == '__main__':
    for nbScript, dBScript in zip(noteBotScriptsFolder.glob('*.py'), drawBotScriptsFolder.glob('*.py')):
        print(nbScript, dBScript)
        assert nbScript.name == dBScript.name, 'mismatch in the scripts folders'
        runScriptAndSaveImage(path=nbScript, annotated=True)
        runScriptAndSaveImage(path=dBScript)
        if not compareImages(nbScript.with_suffix('.png'), dBScript.with_suffix('.png')):
            f'FAILING: {nbScript.name}'
