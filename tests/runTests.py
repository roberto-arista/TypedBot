#!/usr/bin/env python3

# --------- #
# Run Tests #
# --------- #

# -- Modules -- #
import drawBot as dB
# import noteBot as nB

from pathlib import Path
from importlib import import_module
from PIL import Image

# -- Constants -- #

# -- Objects, Functions, Procedures -- #
def runScriptAndSaveImage(path: Path) -> str:
    try:
        dB.newDrawing()
        print(f"RUNNING: {dBScript}")
        import_module(f'{dBScript.parent}.{dBScript.stem}')
        dB.saveImage(dBScript.with_suffix('.png'))
        dB.endDrawing()
    except Exception as error:
        return f'{error}'
    return ""

def compareImages(path1: Path, path2: Path) -> bool:
    im1 = Image.open(path1)
    im2 = Image.open(path2)
    return im1.get_data() == im2.get_data()


# -- Variables -- #
noteBotScriptsFolder = Path('nB_scripts')
drawBotScriptsFolder = Path('dB_scripts')

# -- Instructions -- #
if __name__ == '__main__':

    for nbScript, dBScript in zip(noteBotScriptsFolder.glob('*.py'), drawBotScriptsFolder.glob('*.py')):
        assert nbScript.name == dBScript.name, 'mismatch in the scripts folders'
        runScriptAndSaveImage(path=nbScript)
        runScriptAndSaveImage(path=dBScript)
        res = compareImages(nbScript.with_suffix('.png'), dBScript.with_suffix('.png'))
