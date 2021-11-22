from pathlib import Path
import typedBot as tB

tB.newPage(500, 500)
imagePath = Path("../data/drawBot.pdf")
w, h = tB.imageSize(imagePath)
tB.save()
factor = 250 / w
tB.scale(factor, factor)
tB.image(imagePath, tB.Point(0, 0))
tB.restore()

imagePath = Path("../data/drawBot.png")
w, h = tB.imageSize(imagePath)
tB.save()
factor = 250 / w
tB.scale(factor, factor)
tB.image(imagePath, tB.Point(w, 0))
tB.restore()

imagePath = Path("../data/drawBot.jpg")
w, h = tB.imageSize(imagePath)
tB.save()
factor = 250 / w
tB.scale(factor, factor)
tB.image(imagePath, tB.Point(0, h))
tB.restore()

imagePath = Path("../data/drawBot.bmp")
w, h = tB.imageSize(imagePath)
tB.save()
factor = 250 / w
tB.scale(factor, factor)
tB.image(imagePath, tB.Point(w, h))
tB.restore()

