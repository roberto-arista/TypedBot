import typedBot as tB
tB.newPage(200, 200)
tB.linearGradient(
    tB.Point(100, 100),                         # startPoint
    tB.Point(200, 200),                         # endPoint
    [tB.Color(1, 0, 0), tB.Color(0, 0, 1), tB.Color(0, 1, 0)],  # colors
    [0, .2, 1]                          # locations
)
tB.rect(tB.Box(0, 0, 200, 200))
