from .GPUFactory import GPUFactory
from ..XkomConstants import XkomConstants
from ..XkomBuilder import XkomBuilder

class GPUBuilder():
    def __init__(self, name, specifications, soup, offer):
        XkomBuilder.__init__(self, soup)
        self.name = name
        self.specifications = specifications
        self.offer = offer

    def setName(self):
        return self.name

    def setOffer(self):
        return self.offer

    def setChipset(self):
        socket = self.specifications.get(XkomConstants.GPU_CHIPSET.value)
        return socket

    def setMemory(self):
        memory = self.specifications.get(XkomConstants.GPU_MEMORY.value)
        return memory

    def setOriginalPrice(self):
        original_price = self.getProductOriginalPrice(self.soup)
        return original_price

    def setCurrentPrice(self):
        current_price = self.getProductCurrentPrice(self.soup)
        return current_price

    def setImage(self):
        image = self.getImage()
        return image

    def setCoreClock(self):
        core_clock = self.getGPUBaseClockFromString(self.specifications.get(XkomConstants.GPU_CLOCK.value))
        return core_clock

    def setBoostClock(self):
        boost_clock = self.getGPUBoostClockFromString(self.specifications.get(XkomConstants.GPU_CLOCK.value))
        return boost_clock

    def build(self):
        return GPUFactory.createGPU(self)

    # TODO same function as in other models. Remodel to reuse from parent
    def getImage(self):
        image_span = self.soup.find("span", {"class" : XkomConstants.PROCESSOR_IMAGE_SPAN.value})
        if image_span is not None:
            image_src = image_span.find("img", {"class" : XkomConstants.PROCESSOR_IMAGE.value})["src"]
            return image_src
        return ""
        

    def getProductOriginalPrice(self, soup):
        if self.isProductDiscounted(soup) is not False:
            return self.scrapeOriginalPrice(soup)
        return ""

    def isProductDiscounted(self, soup):
        product_hot_discount = soup.find("div", {"class" : "sc-8c7p9j-3 hRCsfd"})
        product_discount = soup.find("div", {"class" : "u7xnnm-3 gAOShm"})

        if product_discount is not None or product_hot_discount is not None:
            return True

        return False

    def scrapeOriginalPrice(self, soup):
        product_hot_discount = soup.find("div", {"class" : "sc-8c7p9j-3 hRCsfd"})
        product_discount = soup.find("div", {"class" : "u7xnnm-3 gAOShm"})
        if product_discount is not None:
            return product_discount.text
        if product_hot_discount is not None:
            return product_hot_discount.text
        return ""

    def getProductCurrentPrice(self, soup):
        product_hot_price= soup.find("div", {"class" : "sc-8c7p9j-2 ldCRmd"})
        product_price = soup.find("div", {"class" : "u7xnnm-4 iVazGO"})

        if product_price is not None:
            return product_price.text
        return product_hot_price.text

    # this method retrieves base clock GHz from string which is HTML
    # base_clock = processor_base[0:index_to_finish_substring + 3], + 3 happens to assure GHz is also returned as it has 3 characters
    def getGPUBaseClockFromString(self, gpu_base):
        if gpu_base is None:
            return ""
        index_to_finish_substring = str(gpu_base).find("MHz")
        base_clock = gpu_base[0 : index_to_finish_substring + 3]
        return base_clock

    # this method retrieves boost clock GHz from string which is HTML
    # boost_clock = string_after_base_clock[2:index_to_finish_substring + 3],
    # 2happens to assure " " and ( are not added intro result
    #+ 3 happens to assure GHz is also returned as it has 3 characters
    def getGPUBoostClockFromString(self, gpu_base):
        if gpu_base is None:
            return ""
        index_to_start_substring = str(gpu_base).find("MHz")
        string_after_base_clock = gpu_base[index_to_start_substring + 3 : len(gpu_base)]
        if (self.isBoostClockAvaliable(string_after_base_clock) is False):
            return ""
        index_to_finish_substring = str(string_after_base_clock).find("MHz")
        boost_clock = string_after_base_clock[2:index_to_finish_substring + 3]
        return boost_clock

    def isBoostClockAvaliable(self, string):
        if (str(string).find("MHz") is not None):
            return True
        return False