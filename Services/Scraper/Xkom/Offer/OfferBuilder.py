from .OfferFactory import OfferFactory
from ..XkomConstants import XkomConstants

class OfferBuilder():
    def __init__(self, shop, link, specifications, soup):
        self.shop = shop
        self.link = link
        self.specifications = specifications
        self.soup = soup

    def setShop(self):
        return self.shop

    def setLink(self):
        return self.link

    def setOriginalPrice(self):
        original_price = self.getProductOriginalPrice(self.soup)
        if original_price == "":
            return 0
        return self.getProductConvertedPrice(original_price)

    def setCurrentPrice(self):
        current_price = self.getProductCurrentPrice(self.soup)
        return self.getProductConvertedPrice(current_price)

    def build(self):
        return OfferFactory.createOffer(self)

    def getProductOriginalPrice(self, soup):
        if self.isProductDiscounted(soup) is not False:
            return self.scrapeOriginalPrice(soup)
        return ""

    def isProductDiscounted(self, soup):
        product_hot_discount = soup.find("div", {"class" : "sc-8c7p9j-3 hRCsfd"})
        product_discount = soup.find("span", {"class" : "sc-8c7p9j-3 gBBxGG"})

        if product_discount is not None or product_hot_discount is not None:
            return True

        return False

    def scrapeOriginalPrice(self, soup):
        product_hot_discount = soup.find("div", {"class" : "sc-8c7p9j-3 hRCsfd"})
        product_discount = soup.find("span", {"class" : "sc-8c7p9j-3 gBBxGG"})
        if product_discount is not None:
            return product_discount.text
        if product_hot_discount is not None:
            return product_hot_discount.text
        return ""

    def getProductCurrentPrice(self, soup):
        product_hot_price= soup.find("div", {"class" : "sc-8c7p9j-2 ldCRmd"})
        product_price = soup.find("div", {"class" : "u7xnnm-4 jFbqvs"})

        if product_price is not None:
            return product_price.text
        return product_hot_price.text

    def getProductConvertedPrice(self, price):
        index = str(price).find(",")
        converted_price = price[0:index]
        return converted_price.replace(" ", "")