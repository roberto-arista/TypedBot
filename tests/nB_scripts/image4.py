import pathlib
import noteBot as nB
nB.newPage(500, 500)
imagePath = "../data/nB.pdf"
w, h = nB.imageSize(imagePath)
nB.save()
nB.scale(250 / w)
nB.image(imagePath, (0, 0))
nB.restore()

imagePath = "../data/nB.png"
w, h = nB.imageSize(imagePath)
nB.save()
nB.scale(250 / w)
nB.image(imagePath, (w, 0))
nB.restore()

imagePath = "../data/nB.jpg"
w, h = nB.imageSize(imagePath)
nB.save()
nB.scale(250 / w)
nB.image(imagePath, (0, h))
nB.restore()

imagePath = "../data/nB.bmp"
w, h = nB.imageSize(imagePath)
nB.save()
nB.scale(250 / w)
nB.image(pathlib.Path(imagePath), (w, h))  # verify that pathlib.Path objects work
nB.restore()
