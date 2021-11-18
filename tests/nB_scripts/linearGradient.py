import noteBot as nB
nB.newPage(200, 200)
nB.linearGradient(
    nB.Point(100, 100),                         # startPoint
    nB.Point(200, 200),                         # endPoint
    [nB.Color(1, 0, 0), nB.Color(0, 0, 1), nB.Color(0, 1, 0)],  # colors
    [0, .2, 1]                          # locations
)
nB.rect(nB.Box(0, 0, 200, 200))
