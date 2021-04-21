from .MotherboardFactory import MotherboardFactory
from ..XkomConstants import XkomConstants
from ..XkomBuilder import XkomBuilder

class MotherboardBuilder():
    def __init__(self, name, specifications, soup, offer):
        XkomBuilder.__init__(self, soup)
        self.name = name
        self.specifications = specifications
        self.offer = offer

    def setName(self):
        return self.name

    def setOffer(self):
        return self.offer

    def setSocket(self):
        socket = self.specifications.get(XkomConstants.MOTHERBOARD_SOCKET.value)
        return socket

    def setFormat(self):
        format = self.specifications.get(XkomConstants.MOTHERBOARD_FORMAT.value)
        return format

    def setOriginalPrice(self):
        original_price = self.getProductOriginalPrice(self.soup)
        return original_price

    def setCurrentPrice(self):
        current_price = self.getProductCurrentPrice(self.soup)
        return current_price

    def setMemoryMax(self):
        memory_max = self.specifications.get(XkomConstants.MOTHERBOARD_MEMORY_MAX.value)
        return memory_max

    def setMemorySlots(self):
        memory_slots = self.specifications.get(XkomConstants.MOTHERBOARD_MEMORY_SLOTS.value)
        return memory_slots

    def setMemorySpeed(self):
        memory_speed = self.specifications.get(XkomConstants.MOTHERBOARD_MEMORY_SPEED.value)
        if self.specifications.get(XkomConstants.MOTHERBOARD_MEMORY_SPEED_OC.value) is not None:
            memory_speed = memory_speed + self.specifications.get(XkomConstants.MOTHERBOARD_MEMORY_SPEED_OC.value)
        return memory_speed

    def setChipset(self):
        chipset = self.specifications.get(XkomConstants.MOTHERBOARD_CHIPSET.value)
        return chipset

    def setImage(self):
        image = self.getImage()
        return image

    def build(self):
        return MotherboardFactory.createMotherboard(self)

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
