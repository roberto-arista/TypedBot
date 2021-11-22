import typedBot as tB

tB.newPage(200, 200)
tB.cmykRadialGradient(
    tB.Point(0, 0),               # startPoint
    tB.Point(200, 200),           # endPoint
    [tB.CMYKColor(1, 0, 0, 1),    # colors
     tB.CMYKColor(0, 0, 1, 0),
     tB.CMYKColor(0, 1, 0, .2)],
    [0, .2, 1],                   # locations
    0,                            # startRadius
    200                           # endRadius
)
tB.rect(tB.Box(0, 0, 200, 200))
