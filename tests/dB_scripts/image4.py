from pathlib import Path
import drawBot

drawBot.newPage(500, 500)
imagePath = Path("../data/drawBot.pdf")
w, h = drawBot.imageSize(imagePath)
drawBot.save()
drawBot.scale(250 / w)
drawBot.image(imagePath, (0, 0))
drawBot.restore()

imagePath = Path("../data/drawBot.png")
w, h = drawBot.imageSize(imagePath)
drawBot.save()
drawBot.scale(250 / w)
drawBot.image(imagePath, (w, 0))
drawBot.restore()

imagePath = Path("../data/drawBot.jpg")
w, h = drawBot.imageSize(imagePath)
drawBot.save()
drawBot.scale(250 / w)
drawBot.image(imagePath, (0, h))
drawBot.restore()

imagePath = Path("../data/drawBot.bmp")
w, h = drawBot.imageSize(imagePath)
drawBot.save()
drawBot.scale(250 / w)
drawBot.image(imagePath, (w, h))  # verify that pathlib.Path objects work
drawBot.restore()
