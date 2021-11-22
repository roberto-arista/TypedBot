import typedBot as tB
tB.newPage(200, 200)
tB.radialGradient(
    tB.Point(0, 0),                                              # startPoint
    tB.Point(200, 200),                                          # endPoint
    [tB.Color(1, 0, 0), tB.Color(0, 0, 1), tB.Color(0, 1, 0)],   # colors
    [0, .2, 1],                                                  # locations
    0,                                                           # startRadius
    200                                                          # endRadius
)
tB.rect(tB.Box(0, 0, 200, 200))
