#!/usr/bin/env python3

# ------ #
# Images #
# ------ #

# -- Modules -- #
from pathlib import Path
from typing import Optional, Tuple

import drawBot as dB
import drawBot.context.tools.imageObject.ImageObject as IM

from .structures import Point, Color, Box


# -- Drawing Images -- #
def image(path: Path, point: Point, alpha: float = 1, pageNumber: Optional[int] = None):
    if isinstance(path, Path):
        path = f'{path}'
    dB.image(path, point, alpha, pageNumber)

# -- Image Properties -- #
def imageSize(path: Path, pageNumber: Optional[int] = None) -> Tuple[float, float]:
    if isinstance(path, Path):
        path = f'{path}'
    return dB.imageSize(path, pageNumber)

def imagePixelColor(path: Path, point: Point) -> Color:
    return Color(*dB.imagePixelColor(path, point))

def imageResolution(path: Path) -> float:
    if isinstance(path, Path):
        path = f'{path}'
    return dB.imageResolution(path)

def numberOfPages(path: Path):
    if isinstance(path, Path):
        path = f'{path}'

# -- Image Object -- #
class ImageObject(IM):

    def __init__(self, path: Optional[Path] = None):
        super().__init__(path)

    def size() -> Tuple[float, float]:
        return super().size()

    def offset() -> Point:
        return super().offset()

    def clearFilters():
        super().clearFilters()

    def open(path: Path):
        if isinstance(path, Path):
            path = f'{path}'
        super().open(path)

    def copy(self):
        pass

    def boxBlur(self, radius: float = 0):
        super().boxBlur(radius)

    def discBlur(self, radius: float = 0):
        super().discBlur(radius)

    def gaussianBlur(self, radius: float = 0):
        super().gaussianBlur(radius)

    def maskedVariableBlur(self, mask: Optional[ImageObject] = None, radius: float = 0):
        super().maskedVariableBlur(mask, radius)

    def motionBlur(self, radius: float = 0, angle: float = 0):
        super().motionBlur(radius, angle)

    def noiseReduction(self, noiseLevel: float = 0, sharpness: float = 0):
        super().noiseReduction(noiseLevel, sharpness)

    def zoomBlur(self, center: Optional[Point] = None, amount: float = 0):
        super().zoomBlur(center, amount)

    def colorClamp(self, minComponents: Optional[Box] = None, maxComponents: Optional[Box] = None):
        super().colorClamp(minComponents, maxComponents)

    def colorControls(self, saturation=None, brightness=None, contrast=None):
        pass

    def colorMatrix(self, RVector=None, GVector=None, BVector=None, AVector=None, biasVector=None):
        pass

    def colorPolynomial(self, redCoefficients=None, greenCoefficients=None, blueCoefficients=None, alphaCoefficients=None):
        pass

    def exposureAdjust(self, EV=None):
        pass

    def gammaAdjust(self, power=None):
        pass

    def hueAdjust(self, angle=None):
        pass

    def linearToSRGBToneCurve(self):
        pass

    def SRGBToneCurveToLinear(self):
        pass

    def temperatureAndTint(self, neutral=None, targetNeutral=None):
        pass

    def toneCurve(self, point0=None, point1=None, point2=None, point3=None, point4=None):
        pass

    def vibrance(self, amount=None):
        pass

    def whitePointAdjust(self, color=None):
        pass

    def colorCrossPolynomial(self, redCoefficients=None, greenCoefficients=None, blueCoefficients=None):
        pass

    def colorInvert(self):
        pass

    def colorMap(self, gradientImage=None):
        pass

    def colorMonochrome(self, color=None, intensity=None):
        pass

    def colorPosterize(self, levels=None):
        pass

    def falseColor(self, color0=None, color1=None):
        pass

    def maskToAlpha(self):
        pass

    def maximumComponent(self):
        pass

    def minimumComponent(self):
        pass

    def photoEffectChrome(self):
        pass

    def photoEffectFade(self):
        pass

    def photoEffectInstant(self):
        pass

    def photoEffectMono(self):
        pass

    def photoEffectNoir(self):
        pass

    def photoEffectProcess(self):
        pass

    def photoEffectTonal(self):
        pass

    def photoEffectTransfer(self):
        pass

    def sepiaTone(self, intensity=None):
        pass

    def vignette(self, radius=None, intensity=None):
        pass

    def vignetteEffect(self, center=None, intensity=None, radius=None):
        pass

    def additionCompositing(self, backgroundImage=None):
        pass

    def colorBlendMode(self, backgroundImage=None):
        pass

    def colorBurnBlendMode(self, backgroundImage=None):
        pass

    def colorDodgeBlendMode(self, backgroundImage=None):
        pass

    def darkenBlendMode(self, backgroundImage=None):
        pass

    def differenceBlendMode(self, backgroundImage=None):
        pass

    def divideBlendMode(self, backgroundImage=None):
        pass

    def exclusionBlendMode(self, backgroundImage=None):
        pass

    def hardLightBlendMode(self, backgroundImage=None):
        pass

    def hueBlendMode(self, backgroundImage=None):
        pass

    def lightenBlendMode(self, backgroundImage=None):
        pass

    def linearBurnBlendMode(self, backgroundImage=None):
        pass

    def linearDodgeBlendMode(self, backgroundImage=None):
        pass

    def luminosityBlendMode(self, backgroundImage=None):
        pass

    def maximumCompositing(self, backgroundImage=None):
        pass

    def minimumCompositing(self, backgroundImage=None):
        pass

    def multiplyBlendMode(self, backgroundImage=None):
        pass

    def multiplyCompositing(self, backgroundImage=None):
        pass

    def overlayBlendMode(self, backgroundImage=None):
        pass

    def pinLightBlendMode(self, backgroundImage=None):
        pass

    def saturationBlendMode(self, backgroundImage=None):
        pass

    def screenBlendMode(self, backgroundImage=None):
        pass

    def softLightBlendMode(self, backgroundImage=None):
        pass

    def sourceAtopCompositing(self, backgroundImage=None):
        pass

    def sourceInCompositing(self, backgroundImage=None):
        pass

    def sourceOutCompositing(self, backgroundImage=None):
        pass

    def sourceOverCompositing(self, backgroundImage=None):
        pass

    def subtractBlendMode(self, backgroundImage=None):
        pass

    def bumpDistortion(self, center=None, radius=None, scale=None):
        pass

    def bumpDistortionLinear(self, center=None, radius=None, angle=None, scale=None):
        pass

    def circleSplashDistortion(self, center=None, radius=None):
        pass

    def circularWrap(self, center=None, radius=None, angle=None):
        pass

    def droste(self, insetPoint0=None, insetPoint1=None, strands=None, periodicity=None, rotation=None, zoom=None):
        pass

    def displacementDistortion(self, displacementImage=None, scale=None):
        pass

    def glassDistortion(self, texture=None, center=None, scale=None):
        pass

    def glassLozenge(self, point0=None, point1=None, radius=None, refraction=None):
        pass

    def holeDistortion(self, center=None, radius=None):
        pass

    def pinchDistortion(self, center=None, radius=None, scale=None):
        pass

    def stretchCrop(self, size=None, cropAmount=None, centerStretchAmount=None):
        pass

    def torusLensDistortion(self, center=None, radius=None, width=None, refraction=None):
        pass

    def twirlDistortion(self, center=None, radius=None, angle=None):
        pass

    def vortexDistortion(self, center=None, radius=None, angle=None):
        pass

    def aztecCodeGenerator(self, size, message=None, correctionLevel=None, layers=None, compactStyle=None):
        pass

    def QRCodeGenerator(self, size, message=None, correctionLevel=None):
        pass

    def code128BarcodeGenerator(self, size, message=None, quietSpace=None):
        pass

    def checkerboardGenerator(self, size, center=None, color0=None, color1=None, width=None, sharpness=None):
        pass

    def constantColorGenerator(self, size, color=None):
        pass

    def lenticularHaloGenerator(self, size, center=None, color=None, haloRadius=None, haloWidth=None, haloOverlap=None, striationStrength=None, striationContrast=None, time=None):
        pass

    def PDF417BarcodeGenerator(self, size, message=None, minWidth=None, maxWidth=None, minHeight=None, maxHeight=None, dataColumns=None, rows=None, preferredAspectRatio=None, compactionMode=None, compactStyle=None, correctionLevel=None, alwaysSpecifyCompaction=None):
        pass

    def randomGenerator(self, size):
        pass

    def starShineGenerator(self, size, center=None, color=None, radius=None, crossScale=None, crossAngle=None, crossOpacity=None, crossWidth=None, epsilon=None):
        pass

    def stripesGenerator(self, size, center=None, color0=None, color1=None, width=None, sharpness=None):
        pass

    def sunbeamsGenerator(self, size, center=None, color=None, sunRadius=None, maxStriationRadius=None, striationStrength=None, striationContrast=None, time=None):
        pass

    def crop(self, rectangle=None):
        pass

    def lanczosScaleTransform(self, scale=None, aspectRatio=None):
        pass

    def perspectiveCorrection(self, topLeft=None, topRight=None, bottomRight=None, bottomLeft=None):
        pass

    def perspectiveTransform(self, topLeft=None, topRight=None, bottomRight=None, bottomLeft=None):
        pass

    def straightenFilter(self, angle=None):
        pass

    def gaussianGradient(self, size, center=None, color0=None, color1=None, radius=None):
        pass

    def linearGradient(self, size, point0=None, point1=None, color0=None, color1=None):
        pass

    def radialGradient(self, size, center=None, radius0=None, radius1=None, color0=None, color1=None):
        pass

    def circularScreen(self, center=None, width=None, sharpness=None):
        pass

    def CMYKHalftone(self, center=None, width=None, angle=None, sharpness=None, GCR=None, UCR=None):
        pass

    def dotScreen(self, center=None, angle=None, width=None, sharpness=None):
        pass

    def hatchedScreen(self, center=None, angle=None, width=None, sharpness=None):
        pass

    def lineScreen(self, center=None, angle=None, width=None, sharpness=None):
        pass

    def areaAverage(self, extent=None):
        pass

    def areaHistogram(self, extent=None, count=None, scale=None):
        pass

    def rowAverage(self, extent=None):
        pass

    def columnAverage(self, extent=None):
        pass

    def histogramDisplayFilter(self, height=None, highLimit=None, lowLimit=None):
        pass

    def areaMaximum(self, extent=None):
        pass

    def areaMinimum(self, extent=None):
        pass

    def areaMaximumAlpha(self, extent=None):
        pass

    def areaMinimumAlpha(self, extent=None):
        pass

    def sharpenLuminance(self, sharpness=None):
        pass

    def unsharpMask(self, radius=None, intensity=None):
        pass

    def blendWithAlphaMask(self, backgroundImage=None, maskImage=None):
        pass

    def blendWithMask(self, backgroundImage=None, maskImage=None):
        pass

    def bloom(self, radius=None, intensity=None):
        pass

    def comicEffect(self):
        pass

    def convolution3X3(self, weights=None, bias=None):
        pass

    def convolution5X5(self, weights=None, bias=None):
        pass

    def convolution7X7(self, weights=None, bias=None):
        pass

    def convolution9Horizontal(self, weights=None, bias=None):
        pass

    def convolution9Vertical(self, weights=None, bias=None):
        pass

    def crystallize(self, radius=None, center=None):
        pass

    def depthOfField(self, point0=None, point1=None, saturation=None, unsharpMaskRadius=None, unsharpMaskIntensity=None, radius=None):
        pass

    def edges(self, intensity=None):
        pass

    def edgeWork(self, radius=None):
        pass

    def gloom(self, radius=None, intensity=None):
        pass

    def heightFieldFromMask(self, radius=None):
        pass

    def hexagonalPixellate(self, center=None, scale=None):
        pass

    def highlightShadowAdjust(self, highlightAmount=None, shadowAmount=None):
        pass

    def lineOverlay(self, noiseLevel=None, sharpness=None, edgeIntensity=None, threshold=None, contrast=None):
        pass

    def pixellate(self, center=None, scale=None):
        pass

    def pointillize(self, radius=None, center=None):
        pass

    def shadedMaterial(self, shadingImage=None, scale=None):
        pass

    def spotColor(self, centerColor1=None, replacementColor1=None, closeness1=None, contrast1=None, centerColor2=None, replacementColor2=None, closeness2=None, contrast2=None, centerColor3=None, replacementColor3=None, closeness3=None, contrast3=None):
        pass

    def spotLight(self, lightPosition=None, lightPointsAt=None, brightness=None, concentration=None, color=None):
        pass

    def affineClamp(self, transform=None):
        pass

    def affineTile(self, transform=None):
        pass

    def eightfoldReflectedTile(self, center=None, angle=None, width=None):
        pass

    def fourfoldReflectedTile(self, center=None, angle=None, acuteAngle=None, width=None):
        pass

    def fourfoldRotatedTile(self, center=None, angle=None, width=None):
        pass

    def fourfoldTranslatedTile(self, center=None, angle=None, acuteAngle=None, width=None):
        pass

    def glideReflectedTile(self, center=None, angle=None, width=None):
        pass

    def kaleidoscope(self, count=None, center=None, angle=None):
        pass

    def opTile(self, center=None, scale=None, angle=None, width=None):
        pass

    def parallelogramTile(self, center=None, angle=None, acuteAngle=None, width=None):
        pass

    def perspectiveTile(self, topLeft=None, topRight=None, bottomRight=None, bottomLeft=None):
        pass

    def sixfoldReflectedTile(self, center=None, angle=None, width=None):
        pass

    def sixfoldRotatedTile(self, center=None, angle=None, width=None):
        pass

    def triangleTile(self, center=None, angle=None, width=None):
        pass

    def twelvefoldReflectedTile(self, center=None, angle=None, width=None):
        pass

    def accordionFoldTransition(self, targetImage=None, bottomHeight=None, numberOfFolds=None, foldShadowAmount=None, time=None):
        pass

    def barsSwipeTransition(self, targetImage=None, angle=None, width=None, barOffset=None, time=None):
        pass

    def copyMachineTransition(self, targetImage=None, extent=None, color=None, time=None, angle=None, width=None, opacity=None):
        pass

    def disintegrateWithMaskTransition(self, targetImage=None, maskImage=None, time=None, shadowRadius=None, shadowDensity=None, shadowOffset=None):
        pass

    def dissolveTransition(self, targetImage=None, time=None):
        pass

    def flashTransition(self, targetImage=None, center=None, extent=None, color=None, time=None, maxStriationRadius=None, striationStrength=None, striationContrast=None, fadeThreshold=None):
        pass

    def modTransition(self, targetImage=None, center=None, time=None, angle=None, radius=None, compression=None):
        pass

    def pageCurlTransition(self, targetImage=None, backsideImage=None, shadingImage=None, extent=None, time=None, angle=None, radius=None):
        pass

    def pageCurlWithShadowTransition(self, targetImage=None, backsideImage=None, extent=None, time=None, angle=None, radius=None, shadowSize=None, shadowAmount=None, shadowExtent=None):
        pass

    def rippleTransition(self, targetImage=None, shadingImage=None, center=None, extent=None, time=None, width=None, scale=None):
        pass

    def swipeTransition(self, targetImage=None, extent=None, color=None, time=None, angle=None, width=None, opacity=None):
        pass

