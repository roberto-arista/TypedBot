import typedBot as tB
tB.newPage(500, 500)
imagePath = "../data/drawBot.png"
w, h = tB.imageSize(imagePath)
tB.scale(250 / w)
tB.image(imagePath, (0, 0))
tB.image(imagePath, (w, 0), alpha=0.5)
tB.image(imagePath, (0, h), alpha=0.25)
tB.image(imagePath, (w, h), alpha=0.75)
