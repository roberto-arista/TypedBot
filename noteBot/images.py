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
    strPath = path if not isinstance(path, Path) else f'{path}'
    dB.image(strPath, point, alpha, pageNumber)


# -- Image Properties -- #
def imageSize(path: Path, pageNumber: Optional[int] = None) -> Tuple[float, float]:
    strPath = path if not isinstance(path, Path) else f'{path}'
    return dB.imageSize(strPath, pageNumber)

def imagePixelColor(path: Path, point: Point) -> Color:
    return Color(*dB.imagePixelColor(path, point))

def imageResolution(path: Path) -> float:
    strPath = path if not isinstance(path, Path) else f'{path}'
    return dB.imageResolution(strPath)

def numberOfPages(path: Path) -> int:
    strPath = path if not isinstance(path, Path) else f'{path}'
    return dB.numberOfPages(strPath)


# -- Image Object -- #
class ImageObject(IM):

    def __init__(self, path: Optional[Path] = None):
        super().__init__(path)

    def size(self) -> Tuple[float, float]:
        return super().size()

    def offset(self) -> Point:
        return super().offset()

    def clearFilters(self):
        super().clearFilters()

    def open(self, path: Path):
        strPath = path if not isinstance(path, Path) else f'{path}'
        super().open(strPath)

    def copy(self):
        pass

    def boxBlur(self, radius: float = 0):
        super().boxBlur(radius)

    def discBlur(self, radius: float = 0):
        super().discBlur(radius)

    def gaussianBlur(self, radius: float = 0):
        super().gaussianBlur(radius)

    def maskedVariableBlur(self, mask: ImageObject, radius: float = 0):
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
        super().colorControls(saturation, brightness, contrast)

    def colorMatrix(self, RVector=None, GVector=None, BVector=None, AVector=None, biasVector=None):
        super().colorMatrix(RVector, GVector, BVector, AVector, biasVector)

    def colorPolynomial(self, redCoefficients=None, greenCoefficients=None, blueCoefficients=None, alphaCoefficients=None):
        super().colorPolynomial(redCoefficients, greenCoefficients, blueCoefficients, alphaCoefficients)

    def exposureAdjust(self, EV=None):
        super().exposureAdjust(EV)

    def gammaAdjust(self, power=None):
        super().gammaAdjust(power)

    def hueAdjust(self, angle=None):
        super().hueAdjust(angle)

    def linearToSRGBToneCurve(self):
        super().linearToSRGBToneCurve()

    def SRGBToneCurveToLinear(self):
        super().SRGBToneCurveToLinear()

    def temperatureAndTint(self, neutral=None, targetNeutral=None):
        super().temperatureAndTint(neutral, targetNeutral)

    def toneCurve(self, point0=None, point1=None, point2=None, point3=None, point4=None):
        super().toneCurve(point0, point1, point2, point3, point4)

    def vibrance(self, amount=None):
        super().vibrance(amount)

    def whitePointAdjust(self, color=None):
        super().whitePointAdjust(color)

    def colorCrossPolynomial(self, redCoefficients=None, greenCoefficients=None, blueCoefficients=None):
        super().colorCrossPolynomial(redCoefficients, greenCoefficients, blueCoefficients)

    def colorInvert(self):
        super().colorInvert()

    def colorMap(self, gradientImage=None):
        super().colorMap(gradientImage)

    def colorMonochrome(self, color=None, intensity=None):
        super().colorMonochrome(color, intensity)

    def colorPosterize(self, levels=None):
        super().colorPosterize(levels)

    def falseColor(self, color0=None, color1=None):
        super().falseColor(color0, color1)

    def maskToAlpha(self):
        super().maskToAlpha()

    def maximumComponent(self):
        super().maximumComponent()

    def minimumComponent(self):
        super().minimumComponent()

    def photoEffectChrome(self):
        super().photoEffectChrome()

    def photoEffectFade(self):
        super().photoEffectFade()

    def photoEffectInstant(self):
        super().photoEffectInstant()

    def photoEffectMono(self):
        super().photoEffectMono()

    def photoEffectNoir(self):
        super().photoEffectNoir()

    def photoEffectProcess(self):
        super().photoEffectProcess()

    def photoEffectTonal(self):
        super().photoEffectTonal()

    def photoEffectTransfer(self):
        super().photoEffectTransfer()

    def sepiaTone(self, intensity=None):
        super().sepiaTone(intensity)

    def vignette(self, radius=None, intensity=None):
        super().vignette(radius, intensity)

    def vignetteEffect(self, center=None, intensity=None, radius=None):
        super().vignetteEffect(center, intensity, radius)

    def additionCompositing(self, backgroundImage=None):
        super().additionCompositing(backgroundImage)

    def colorBlendMode(self, backgroundImage=None):
        super().colorBlendMode(backgroundImage)

    def colorBurnBlendMode(self, backgroundImage=None):
        super().colorBurnBlendMode(backgroundImage)

    def colorDodgeBlendMode(self, backgroundImage=None):
        super().colorDodgeBlendMode(backgroundImage)

    def darkenBlendMode(self, backgroundImage=None):
        super().darkenBlendMode(backgroundImage)

    def differenceBlendMode(self, backgroundImage=None):
        super().differenceBlendMode(backgroundImage)

    def divideBlendMode(self, backgroundImage=None):
        super().divideBlendMode(backgroundImage)

    def exclusionBlendMode(self, backgroundImage=None):
        super().exclusionBlendMode(backgroundImage)

    def hardLightBlendMode(self, backgroundImage=None):
        super().hardLightBlendMode(backgroundImage)

    def hueBlendMode(self, backgroundImage=None):
        super().hueBlendMode(backgroundImage)

    def lightenBlendMode(self, backgroundImage=None):
        super().lightenBlendMode(backgroundImage)

    def linearBurnBlendMode(self, backgroundImage=None):
        super().linearBurnBlendMode(backgroundImage)

    def linearDodgeBlendMode(self, backgroundImage=None):
        super().linearDodgeBlendMode(backgroundImage)

    def luminosityBlendMode(self, backgroundImage=None):
        super().luminosityBlendMode(backgroundImage)

    def maximumCompositing(self, backgroundImage=None):
        super().maximumCompositing(backgroundImage)

    def minimumCompositing(self, backgroundImage=None):
        super().minimumCompositing(backgroundImage)

    def multiplyBlendMode(self, backgroundImage=None):
        super().multiplyBlendMode(backgroundImage)

    def multiplyCompositing(self, backgroundImage=None):
        super().multiplyCompositing(backgroundImage)

    def overlayBlendMode(self, backgroundImage=None):
        super().overlayBlendMode(backgroundImage)

    def pinLightBlendMode(self, backgroundImage=None):
        super().pinLightBlendMode(backgroundImage)

    def saturationBlendMode(self, backgroundImage=None):
        super().saturationBlendMode(backgroundImage)

    def screenBlendMode(self, backgroundImage=None):
        super().screenBlendMode(backgroundImage)

    def softLightBlendMode(self, backgroundImage=None):
        super().softLightBlendMode(backgroundImage)

    def sourceAtopCompositing(self, backgroundImage=None):
        super().sourceAtopCompositing(backgroundImage)

    def sourceInCompositing(self, backgroundImage=None):
        super().sourceInCompositing(backgroundImage)

    def sourceOutCompositing(self, backgroundImage=None):
        super().sourceOutCompositing(backgroundImage)

    def sourceOverCompositing(self, backgroundImage=None):
        super().sourceOverCompositing(backgroundImage)

    def subtractBlendMode(self, backgroundImage=None):
        super().subtractBlendMode(backgroundImage)

    def bumpDistortion(self, center=None, radius=None, scale=None):
        super().bumpDistortion(center, radius, scale)

    def bumpDistortionLinear(self, center=None, radius=None, angle=None, scale=None):
        super().bumpDistortionLinear(center, radius, angle, scale)

    def circleSplashDistortion(self, center=None, radius=None):
        super().circleSplashDistortion(center, radius)

    def circularWrap(self, center=None, radius=None, angle=None):
        super().circularWrap(center, radius, angle)

    def droste(self, insetPoint0=None, insetPoint1=None, strands=None, periodicity=None, rotation=None, zoom=None):
        super().droste(insetPoint0, insetPoint1, strands, periodicity, rotation, zoom)

    def displacementDistortion(self, displacementImage=None, scale=None):
        super().displacementDistortion(displacementImage, scale)

    def glassDistortion(self, texture=None, center=None, scale=None):
        super().glassDistortion(texture, center, scale)

    def glassLozenge(self, point0=None, point1=None, radius=None, refraction=None):
        super().glassLozenge(point0, point1, radius, refraction)

    def holeDistortion(self, center=None, radius=None):
        super().holeDistortion(center, radius)

    def pinchDistortion(self, center=None, radius=None, scale=None):
        super().pinchDistortion(center, radius, scale)

    def stretchCrop(self, size=None, cropAmount=None, centerStretchAmount=None):
        super().stretchCrop(size, cropAmount, centerStretchAmount)

    def torusLensDistortion(self, center=None, radius=None, width=None, refraction=None):
        super().torusLensDistortion(center, radius, width, refraction)

    def twirlDistortion(self, center=None, radius=None, angle=None):
        super().twirlDistortion(center, radius, angle)

    def vortexDistortion(self, center=None, radius=None, angle=None):
        super().vortexDistortion(center, radius, angle)

    def aztecCodeGenerator(self, size, message=None, correctionLevel=None, layers=None, compactStyle=None):
        super().aztecCodeGenerator(size, message, correctionLevel, layers, compactStyle)

    def QRCodeGenerator(self, size, message=None, correctionLevel=None):
        super().QRCodeGenerator(size, message, correctionLevel)

    def code128BarcodeGenerator(self, size, message=None, quietSpace=None):
        super().code128BarcodeGenerator(size, message, quietSpace)

    def checkerboardGenerator(self, size, center=None, color0=None, color1=None, width=None, sharpness=None):
        super().checkerboardGenerator(size, center, color0, color1, width, sharpness)

    def constantColorGenerator(self, size, color=None):
        super().constantColorGenerator(size, color)

    def lenticularHaloGenerator(self, size, center=None, color=None, haloRadius=None, haloWidth=None, haloOverlap=None, striationStrength=None, striationContrast=None, time=None):
        super().lenticularHaloGenerator(size, center, color, haloRadius, haloWidth, haloOverlap, striationStrength, striationContrast, time)

    def PDF417BarcodeGenerator(self, size, message=None, minWidth=None, maxWidth=None, minHeight=None, maxHeight=None, dataColumns=None, rows=None, preferredAspectRatio=None, compactionMode=None, compactStyle=None, correctionLevel=None, alwaysSpecifyCompaction=None):
        super().PDF417BarcodeGenerator(size, message, minWidth, maxWidth, minHeight, maxHeight, dataColumns, rows, preferredAspectRatio, compactionMode, compactStyle, correctionLevel, alwaysSpecifyCompaction)

    def randomGenerator(self, size):
        super().randomGenerator(size)

    def starShineGenerator(self, size, center=None, color=None, radius=None, crossScale=None, crossAngle=None, crossOpacity=None, crossWidth=None, epsilon=None):
        super().starShineGenerator(size, center, color, radius, crossScale, crossAngle, crossOpacity, crossWidth, epsilon)

    def stripesGenerator(self, size, center=None, color0=None, color1=None, width=None, sharpness=None):
        super().stripesGenerator(size, center, color0, color1, width, sharpness)

    def sunbeamsGenerator(self, size, center=None, color=None, sunRadius=None, maxStriationRadius=None, striationStrength=None, striationContrast=None, time=None):
        super().sunbeamsGenerator(size, center, color, sunRadius, maxStriationRadius, striationStrength, striationContrast, time)

    def crop(self, rectangle=None):
        super().crop(rectangle)

    def lanczosScaleTransform(self, scale=None, aspectRatio=None):
        super().lanczosScaleTransform(scale, aspectRatio)

    def perspectiveCorrection(self, topLeft=None, topRight=None, bottomRight=None, bottomLeft=None):
        super().perspectiveCorrection(topLeft, topRight, bottomRight, bottomLeft)

    def perspectiveTransform(self, topLeft=None, topRight=None, bottomRight=None, bottomLeft=None):
        super().perspectiveTransform(topLeft, topRight, bottomRight, bottomLeft)

    def straightenFilter(self, angle=None):
        super().straightenFilter(angle)

    def gaussianGradient(self, size, center=None, color0=None, color1=None, radius=None):
        super().gaussianGradient(size, center, color0, color1, radius)

    def linearGradient(self, size, point0=None, point1=None, color0=None, color1=None):
        super().linearGradient(size, point0, point1, color0, color1)

    def radialGradient(self, size, center=None, radius0=None, radius1=None, color0=None, color1=None):
        super().radialGradient(size, center, radius0, radius1, color0, color1)

    def circularScreen(self, center=None, width=None, sharpness=None):
        super().circularScreen(center, width, sharpness)

    def CMYKHalftone(self, center=None, width=None, angle=None, sharpness=None, GCR=None, UCR=None):
        super().CMYKHalftone(center, width, angle, sharpness, GCR, UCR)

    def dotScreen(self, center=None, angle=None, width=None, sharpness=None):
        super().dotScreen(center, angle, width, sharpness)

    def hatchedScreen(self, center=None, angle=None, width=None, sharpness=None):
        super().hatchedScreen(center, angle, width, sharpness)

    def lineScreen(self, center=None, angle=None, width=None, sharpness=None):
        super().lineScreen(center, angle, width, sharpness)

    def areaAverage(self, extent=None):
        super().areaAverage(extent)

    def areaHistogram(self, extent=None, count=None, scale=None):
        super().areaHistogram(extent, count, scale)

    def rowAverage(self, extent=None):
        super().rowAverage(extent)

    def columnAverage(self, extent=None):
        super().columnAverage(extent)

    def histogramDisplayFilter(self, height=None, highLimit=None, lowLimit=None):
        super().histogramDisplayFilter(height, highLimit, lowLimit)

    def areaMaximum(self, extent=None):
        super().areaMaximum(extent)

    def areaMinimum(self, extent=None):
        super().areaMinimum(extent)

    def areaMaximumAlpha(self, extent=None):
        super().areaMaximumAlpha(extent)

    def areaMinimumAlpha(self, extent=None):
        super().areaMinimumAlpha(extent)

    def sharpenLuminance(self, sharpness=None):
        super().sharpenLuminance(sharpness)

    def unsharpMask(self, radius=None, intensity=None):
        super().unsharpMask(radius, intensity)

    def blendWithAlphaMask(self, backgroundImage=None, maskImage=None):
        super().blendWithAlphaMask(backgroundImage, maskImage)

    def blendWithMask(self, backgroundImage=None, maskImage=None):
        super().blendWithMask(backgroundImage, maskImage)

    def bloom(self, radius=None, intensity=None):
        super().bloom(radius, intensity)

    def comicEffect(self):
        super().comicEffect()

    def convolution3X3(self, weights=None, bias=None):
        super().convolution3X3(weights, bias)

    def convolution5X5(self, weights=None, bias=None):
        super().convolution5X5(weights, bias)

    def convolution7X7(self, weights=None, bias=None):
        super().convolution7X7(weights, bias)

    def convolution9Horizontal(self, weights=None, bias=None):
        super().convolution9Horizontal(weights, bias)

    def convolution9Vertical(self, weights=None, bias=None):
        super().convolution9Vertical(weights, bias)

    def crystallize(self, radius=None, center=None):
        super().crystallize(radius, center)

    def depthOfField(self, point0=None, point1=None, saturation=None, unsharpMaskRadius=None, unsharpMaskIntensity=None, radius=None):
        super().depthOfField(point0, point1, saturation, unsharpMaskRadius, unsharpMaskIntensity, radius)

    def edges(self, intensity=None):
        super().edges(intensity)

    def edgeWork(self, radius=None):
        super().edgeWork(radius)

    def gloom(self, radius=None, intensity=None):
        super().gloom(radius, intensity)

    def heightFieldFromMask(self, radius=None):
        super().heightFieldFromMask(radius)

    def hexagonalPixellate(self, center=None, scale=None):
        super().hexagonalPixellate(center, scale)

    def highlightShadowAdjust(self, highlightAmount=None, shadowAmount=None):
        super().highlightShadowAdjust(highlightAmount, shadowAmount)

    def lineOverlay(self, noiseLevel=None, sharpness=None, edgeIntensity=None, threshold=None, contrast=None):
        super().lineOverlay(noiseLevel, sharpness, edgeIntensity, threshold, contrast)

    def pixellate(self, center=None, scale=None):
        super().pixellate(center, scale)

    def pointillize(self, radius=None, center=None):
        super().pointillize(radius, center)

    def shadedMaterial(self, shadingImage=None, scale=None):
        super().shadedMaterial(shadingImage, scale)

    def spotColor(self, centerColor1=None, replacementColor1=None, closeness1=None, contrast1=None, centerColor2=None, replacementColor2=None, closeness2=None, contrast2=None, centerColor3=None, replacementColor3=None, closeness3=None, contrast3=None):
        super().spotColor(centerColor1, replacementColor1, closeness1, contrast1, centerColor2, replacementColor2, closeness2, contrast2, centerColor3, replacementColor3, closeness3, contrast3)

    def spotLight(self, lightPosition=None, lightPointsAt=None, brightness=None, concentration=None, color=None):
        super().spotLight(lightPosition, lightPointsAt, brightness, concentration, color)

    def affineClamp(self, transform=None):
        super().affineClamp(transform)

    def affineTile(self, transform=None):
        super().affineTile(transform)

    def eightfoldReflectedTile(self, center=None, angle=None, width=None):
        super().eightfoldReflectedTile(center, angle, width)

    def fourfoldReflectedTile(self, center=None, angle=None, acuteAngle=None, width=None):
        super().fourfoldReflectedTile(center, angle, acuteAngle, width)

    def fourfoldRotatedTile(self, center=None, angle=None, width=None):
        super().fourfoldRotatedTile(center, angle, width)

    def fourfoldTranslatedTile(self, center=None, angle=None, acuteAngle=None, width=None):
        super().fourfoldTranslatedTile(center, angle, acuteAngle, width)

    def glideReflectedTile(self, center=None, angle=None, width=None):
        super().glideReflectedTile(center, angle, width)

    def kaleidoscope(self, count=None, center=None, angle=None):
        super().kaleidoscope(count, center, angle)

    def opTile(self, center=None, scale=None, angle=None, width=None):
        super().opTile(center, scale, angle, width)

    def parallelogramTile(self, center=None, angle=None, acuteAngle=None, width=None):
        super().parallelogramTile(center, angle, acuteAngle, width)

    def perspectiveTile(self, topLeft=None, topRight=None, bottomRight=None, bottomLeft=None):
        super().perspectiveTile(topLeft, topRight, bottomRight, bottomLeft)

    def sixfoldReflectedTile(self, center=None, angle=None, width=None):
        super().sixfoldReflectedTile(center, angle, width)

    def sixfoldRotatedTile(self, center=None, angle=None, width=None):
        super().sixfoldRotatedTile(center, angle, width)

    def triangleTile(self, center=None, angle=None, width=None):
        super().triangleTile(center, angle, width)

    def twelvefoldReflectedTile(self, center=None, angle=None, width=None):
        super().twelvefoldReflectedTile(center, angle, width)

    def accordionFoldTransition(self, targetImage=None, bottomHeight=None, numberOfFolds=None, foldShadowAmount=None, time=None):
        super().accordionFoldTransition(targetImage, bottomHeight, numberOfFolds, foldShadowAmount, time)

    def barsSwipeTransition(self, targetImage=None, angle=None, width=None, barOffset=None, time=None):
        super().barsSwipeTransition(targetImage, angle, width, barOffset, time)

    def copyMachineTransition(self, targetImage=None, extent=None, color=None, time=None, angle=None, width=None, opacity=None):
        super().copyMachineTransition(targetImage, extent, color, time, angle, width, opacity)

    def disintegrateWithMaskTransition(self, targetImage=None, maskImage=None, time=None, shadowRadius=None, shadowDensity=None, shadowOffset=None):
        super().disintegrateWithMaskTransition(targetImage, maskImage, time, shadowRadius, shadowDensity, shadowOffset)

    def dissolveTransition(self, targetImage=None, time=None):
        super().dissolveTransition(targetImage, time)

    def flashTransition(self, targetImage=None, center=None, extent=None, color=None, time=None, maxStriationRadius=None, striationStrength=None, striationContrast=None, fadeThreshold=None):
        super().flashTransition(targetImage, center, extent, color, time, maxStriationRadius, striationStrength, striationContrast, fadeThreshold)

    def modTransition(self, targetImage=None, center=None, time=None, angle=None, radius=None, compression=None):
        super().modTransition(targetImage, center, time, angle, radius, compression)

    def pageCurlTransition(self, targetImage=None, backsideImage=None, shadingImage=None, extent=None, time=None, angle=None, radius=None):
        super().pageCurlTransition(targetImage, backsideImage, shadingImage, extent, time, angle, radius)

    def pageCurlWithShadowTransition(self, targetImage=None, backsideImage=None, extent=None, time=None, angle=None, radius=None, shadowSize=None, shadowAmount=None, shadowExtent=None):
        super().pageCurlWithShadowTransition(targetImage, backsideImage, extent, time, angle, radius, shadowSize, shadowAmount, shadowExtent)

    def rippleTransition(self, targetImage=None, shadingImage=None, center=None, extent=None, time=None, width=None, scale=None):
        super().rippleTransition(targetImage, shadingImage, center, extent, time, width, scale)

    def swipeTransition(self, targetImage=None, extent=None, color=None, time=None, angle=None, width=None, opacity=None):
        super().swipeTransition(targetImage, extent, color, time, angle, width, opacity)
