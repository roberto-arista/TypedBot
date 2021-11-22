import typedBot as tB

tB.newPage(200, 200)
tB.cmykLinearGradient(
    tB.Point(100, 100),                         # startPoint
    tB.Point(200, 200),                         # endPoint
    [tB.CMYKColor(1, 0, 0, 1, 1), tB.CMYKColor(0, 0, 1, 0, 1), tB.CMYKColor(0, 1, 0, .2, 1)],    # cmyk colors
    [0, .2, 1]                          # locations
)
tB.rect(tB.Box(0, 0, 200, 200))
