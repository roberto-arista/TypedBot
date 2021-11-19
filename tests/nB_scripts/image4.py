from pathlib import Path
import noteBot as nB

nB.newPage(500, 500)
imagePath = Path("../data/drawBot.pdf")
w, h = nB.imageSize(imagePath)
nB.save()
factor = 250 / w
nB.scale(factor, factor)
nB.image(imagePath, nB.Point(0, 0))
nB.restore()

imagePath = Path("../data/drawBot.png")
w, h = nB.imageSize(imagePath)
nB.save()
factor = 250 / w
nB.scale(factor, factor)
nB.image(imagePath, nB.Point(w, 0))
nB.restore()

imagePath = Path("../data/drawBot.jpg")
w, h = nB.imageSize(imagePath)
nB.save()
factor = 250 / w
nB.scale(factor, factor)
nB.image(imagePath, nB.Point(0, h))
nB.restore()

imagePath = Path("../data/drawBot.bmp")
w, h = nB.imageSize(imagePath)
nB.save()
factor = 250 / w
nB.scale(factor, factor)
nB.image(imagePath, nB.Point(w, h))
nB.restore()

