import noteBot as nB

nB.newPage(200, 200)
nB.cmykRadialGradient(
    nB.Point(0, 0),               # startPoint
    nB.Point(200, 200),           # endPoint
    [nB.CMYKColor(1, 0, 0, 1),    # colors
     nB.CMYKColor(0, 0, 1, 0),
     nB.CMYKColor(0, 1, 0, .2)],
    [0, .2, 1],                   # locations
    0,                            # startRadius
    200                           # endRadius
)
nB.rect(nB.Box(0, 0, 200, 200))
