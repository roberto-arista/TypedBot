import noteBot as nB
nB.newPage(200, 200)
nB.stroke(0)
nB.strokeWidth(10)
nB.fill(1, 0.3, 0)
nB.polygon((40, 40), (40, 160))
nB.polygon((60, 40), (60, 160), (130, 160))
nB.polygon((100, 40), (160, 160), (160, 40), close=False)
