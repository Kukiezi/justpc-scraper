from .ProcessorCoolerFactory import ProcessorCoolerFactory
from ..XkomConstants import XkomConstants
from ..XkomBuilder import XkomBuilder

class ProcessorCoolerBuilder(XkomBuilder):
    def __init__(self, name, specifications, soup, offer):
        XkomBuilder.__init__(self, soup)
        self.name = name
        self.specifications = specifications
        self.offer = offer

    def setName(self):
        return self.name

    def setOffer(self):
        return self.offer

    def setRpm(self):
        rpm = self.getRpm(self.specifications.get(XkomConstants.PROCESSOR_COOLER_RPM.value))
        return rpm

    def setNoise(self):
        noise = self.getNoise(self.specifications.get(XkomConstants.PROCESSOR_COOLER_NOISE.value))
        return noise

    def setCompatibility(self):
        compatiblity = self.specifications.get(XkomConstants.PROCESSOR_COOLER_COMPATIBILITY.value)
        return compatiblity

    def setImage(self):
        image = self.getImage()
        return image

    def build(self):
        return ProcessorCoolerFactory.createProcessorCooler(self)

    def getNoise(self, noise):
        if noise is None:
            return ""
        return noise.replace(",", ".")
        
    def getRpm(self, text):
        if not text[0].isdigit():
            text = self.removeRpmTextStart(text)
        return self.removeRpmFromText(text)

    def removeRpmFromText(self, text):
        return text.replace("obr./min.", "")

    def removeRpmTextStart(self, text):
        return text[3:len(text)]

    