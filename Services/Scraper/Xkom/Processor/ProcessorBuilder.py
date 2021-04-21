from .ProcessorFactory import ProcessorFactory
from ..XkomConstants import XkomConstants
from ..XkomBuilder import XkomBuilder

class ProcessorBuilder(XkomBuilder):
    def __init__(self, name, specifications, soup, offer):
        XkomBuilder.__init__(self, soup)
        self.name = name
        self.specifications = specifications
        self.offer = offer
        
    def setName(self):
        return self.name
    
    def setOffer(self):
        return self.offer

    def setSeries(self):
        series = self.specifications.get(XkomConstants.PROCESSOR_SERIES.value)
        return series

    def setCores(self):
        cores = self.specifications.get(XkomConstants.PROCESSOR_CORES.value)
        index = cores.find(" ")
        cores_int = cores[0:index]
        return int(cores_int)
        
    def setCoreClock(self):
        core_clock = self.getProcessorBaseClockFromString(self.specifications.get(XkomConstants.PROCESSOR_CLOCK.value))
        return core_clock

    def setBoostClock(self):
        boost_clock = self.getProcessorBoostClockFromString(self.specifications.get(XkomConstants.PROCESSOR_CLOCK.value))
        return boost_clock

    def setSocket(self):
        socket = self.specifications.get(XkomConstants.PROCESSOR_SOCKET.value)
        return socket

    def setIntegratedGraphics(self):
        integrated_graphic = self.specifications.get(XkomConstants.PROCESSOR_INTEGRATED_GRAPHIC.value)
        return integrated_graphic

    def setCacheMemory(self):
        cache_memory = self.specifications.get(XkomConstants.PROCESSOR_CACHE_MEMORY.value)
        return cache_memory

    def setIncludesCooler(self):
        includes_cooler = self.specifications.get(XkomConstants.PROCESSOR_INCLUDES_COOLER.value)
        return includes_cooler

    def setImage(self):
        image = self.getImage()
        return image

    def build(self):
        return ProcessorFactory.createProcessor(self)

    # this method retrieves base clock GHz from string which is HTML
    # base_clock = processor_base[0:index_to_finish_substring + 3], + 3 happens to assure GHz is also returned as it has 3 characters
    def getProcessorBaseClockFromString(self, processor_base):
        if processor_base is None:
            return ""
        index_to_finish_substring = str(processor_base).find("GHz")
        base_clock = processor_base[0 : index_to_finish_substring + 3]
        return base_clock

    # this method retrieves boost clock GHz from string which is HTML
    # boost_clock = string_after_base_clock[2:index_to_finish_substring + 3],
    # 2happens to assure " " and ( are not added intro result
    #+ 3 happens to assure GHz is also returned as it has 3 characters
    def getProcessorBoostClockFromString(self, processor_base):
        if processor_base is None:
            return ""
        index_to_start_substring = str(processor_base).find("GHz")
        string_after_base_clock = processor_base[index_to_start_substring + 3 : len(processor_base)]
        if (self.isBoostClockAvaliable(string_after_base_clock) is False):
            return ""
        index_to_finish_substring = str(string_after_base_clock).find("GHz")
        boost_clock = string_after_base_clock[2:index_to_finish_substring + 3]
        return boost_clock
   
    def isBoostClockAvaliable(self, string):
        if (str(string).find("GHz") is not None):
            return True
        return False
