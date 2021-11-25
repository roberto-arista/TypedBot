from pathlib import Path
import drawBot

drawBot.newPage(500, 500)
imagePath = Path("tests/data/drawBot.pdf")
w, h = drawBot.imageSize(f'{imagePath}')
drawBot.save()
drawBot.scale(250 / w)
drawBot.image(f'{imagePath}', (0, 0))
drawBot.restore()

imagePath = Path("tests/data/drawBot.png")
w, h = drawBot.imageSize(f'{imagePath}')
drawBot.save()
drawBot.scale(250 / w)
drawBot.image(f'{imagePath}', (w, 0))
drawBot.restore()

imagePath = Path("tests/data/drawBot.jpg")
w, h = drawBot.imageSize(f'{imagePath}')
drawBot.save()
drawBot.scale(250 / w)
drawBot.image(f'{imagePath}', (0, h))
drawBot.restore()

imagePath = Path("tests/data/drawBot.bmp")
w, h = drawBot.imageSize(f'{imagePath}')
drawBot.save()
drawBot.scale(250 / w)
drawBot.image(f'{imagePath}', (w, h))  # verify that pathlib.Path objects work
drawBot.restore()
