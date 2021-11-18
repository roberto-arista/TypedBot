import noteBot as nB

nB.newPage(200, 200)
nB.cmykLinearGradient(
    nB.Point(100, 100),                         # startPoint
    nB.Point(200, 200),                         # endPoint
    [nB.CMYKColor(1, 0, 0, 1, 1), nB.CMYKColor(0, 0, 1, 0, 1), nB.CMYKColor(0, 1, 0, .2, 1)],    # cmyk colors
    [0, .2, 1]                          # locations
)
nB.rect(nB.Box(0, 0, 200, 200))
