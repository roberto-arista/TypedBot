import drawBot
drawBot.newPage(200, 200)
drawBot.stroke(0, 0, 1)
drawBot.strokeWidth(5)
drawBot.save()
drawBot.fill(1, 0, 0)
drawBot.translate(100, 100)
drawBot.rect(0, 0, 100, 100)
drawBot.restore()
drawBot.rect(0, 0, 100, 100)
drawBot.save()
drawBot.fill(0, 1, 0)
drawBot.translate(100, 0)
drawBot.rect(0, 0, 100, 100)
drawBot.restore()
drawBot.rect(0, 100, 100, 100)
