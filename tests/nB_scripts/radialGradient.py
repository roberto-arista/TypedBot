import noteBot as nB
nB.newPage(200, 200)
nB.radialGradient(
    nB.Point(0, 0),                                              # startPoint
    nB.Point(200, 200),                                          # endPoint
    [nB.Color(1, 0, 0), nB.Color(0, 0, 1), nB.Color(0, 1, 0)],   # colors
    [0, .2, 1],                                                  # locations
    0,                                                           # startRadius
    200                                                          # endRadius
)
nB.rect(nB.Box(0, 0, 200, 200))
