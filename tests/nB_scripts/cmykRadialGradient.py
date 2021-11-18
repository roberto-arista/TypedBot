import noteBot as nB
nB.newPage(200, 200)
nB.cmykRadialGradient(
    (0, 0),                         # startPoint
    (200, 200),                         # endPoint
    [(1, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, .2)],    # colors
    [0, .2, 1],                         # locations
    0,                                  # startRadius
    200                                 # endRadius
)
nB.rect(0, 0, 200, 200)
