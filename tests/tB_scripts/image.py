import typedBot as tB
from typedBot import Point
from pathlib import Path
import os

tB.newPage(500, 500)
print(os.getcwd())
imagePath = Path("tests/data/drawBot.jpg")
w, h = tB.imageSize(imagePath)
tB.scale(250 / w, 250 / w)
tB.image(imagePath, Point(0, 0))
tB.image(imagePath, Point(w, 0), alpha=0.5)
tB.image(imagePath, Point(0, h), alpha=0.25)
tB.image(imagePath, Point(w, h), alpha=0.75)
