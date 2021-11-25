from pathlib import Path
import typedBot as tB
from typedBot import Point

tB.newPage(500, 500)
imagePath = Path("tests/data/drawBot.pdf")
w, h = tB.imageSize(imagePath)
tB.save()
factor = 250 / w
tB.scale(factor, factor)
tB.image(imagePath, Point(0, 0))
tB.restore()

imagePath = Path("tests/data/drawBot.png")
w, h = tB.imageSize(imagePath)
tB.save()
factor = 250 / w
tB.scale(factor, factor)
tB.image(imagePath, Point(w, 0))
tB.restore()

imagePath = Path("tests/data/drawBot.jpg")
w, h = tB.imageSize(imagePath)
tB.save()
factor = 250 / w
tB.scale(factor, factor)
tB.image(imagePath, Point(0, h))
tB.restore()

imagePath = Path("tests/data/drawBot.bmp")
w, h = tB.imageSize(imagePath)
tB.save()
factor = 250 / w
tB.scale(factor, factor)
tB.image(imagePath, Point(w, h))
tB.restore()
