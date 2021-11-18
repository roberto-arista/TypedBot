import noteBot as nB
nB.newPage(500, 500)
imagePath = "../data/nB.jpg"
w, h = nB.imageSize(imagePath)
nB.scale(250 / w)
nB.image(imagePath, (0, 0))
nB.image(imagePath, (w, 0), alpha=0.5)
nB.image(imagePath, (0, h), alpha=0.25)
nB.image(imagePath, (w, h), alpha=0.75)
