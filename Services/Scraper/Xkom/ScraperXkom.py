import logging
import traceback
from ..ScraperBase import ScraperBase
from Models.Processor import Processor
from .XkomConstants import XkomConstants
from .ProcessorBuilder import ProcessorBuilder
from .OfferBuilder import OfferBuilder
from bs4 import BeautifulSoup
from .ProductFactory import ProductFactory

product_title_classes = [
    "sc-1bker4h-4 gbILWy",
    "sc-1x6crnh-5 cYILyh",
    "sc-1x6crnh-5 gOwOoL",
    "sc-1bker4h-4 llfiOB",
]

class ScraperXkom(ScraperBase):
    def __init__(self, url, product_type):
        self.url = url
        self.product_type = product_type

    def getBaseUrl(self):
        return str(self.BASE_URL)

    def getUrl(self):
        return f"{self.BASE_URL}{self.url}"

    def getProductType(self):
        return self.product_type

    def setUrl(self, url):
        self.url = url

    def setProductType(self, product_type):
        self.product_type = product_type

    def getProductLinksFromPage(self, soup):
        processors_links = soup.find_all("a", {"class" : "sc-1h16fat-0 dEoadv"})
        links = []
        for link in processors_links:
            links.append(link["href"])
        return links

    def getProductData(self, soup, url):
            product_title = self.getProductTitle(soup)
            specifications = soup.find_all("div", {"class" : "sc-bwzfXH sc-13p5mv-0 cwztyD sc-htpNat gSgMmi"})
            product_specifications = dict()

            for tag in specifications:
                try:
                    product_specifications[self._getVisibleTagText(tag)] = tag.find("div", {"class" : "sc-13p5mv-3 gngmZS"}).text
                except Exception as e:
                    logging.error("Products specification text value was not visible")
            
            # for tag in top_details:
                # if tag.find("span", {"class" : "p7lf0n-2 emBQhb"}).text not in product_specifications:
                    # product_specifications[tag.find("span", {"class" : "p7lf0n-3 dKxbux"}).text] = tag.find("span", {"class" : "p7lf0n-3 dKxbux"}).text
            try:
                offer = OfferBuilder("x-kom", url, product_specifications, soup).build()
                product = ProductFactory.createProduct(product_title.text, product_specifications, soup, self.product_type, offer)
                return product
            except Exception as e:
                logging.error("Exception happend on product: {0} with url: {1}".format(product_title.text, url))
                logging.error("Exception: {0}".format(e))
                traceback.print_exc()
            return None


    def getProductTitle(self, soup):
        product_title = None
        
        for title in product_title_classes:
            product_title = soup.find("h1", {"class" : title})

            if product_title is not None:
                return product_title
        
        raise Exception("No product title found")

    def getHtmlFromAllPagesToArray(self):
        url = self.getUrl()
        response = self.request.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        html_array = []
        processors_html = soup.find("div", {"class" : XkomConstants.PRODUCTS_LISTS_HTML_CLASS.value})
        html_array.append(processors_html)
        next_page_html = processors_html.find_all("a", {"class" : XkomConstants.PRODUCT_PREV_NEXT_PAGE_CLASS.value})

        while (self.isNextPegeHtmlValid(next_page_html) is True):
            for html in next_page_html:
                if (self.isNextPageSpanAvailable(html) is True):
                    url = self.BASE_URL + html["href"]
                    response = self.request.get(url)
                    soup = BeautifulSoup(response.content, "html.parser")
                    processors_html = soup.find("div", {"class" : XkomConstants.PRODUCTS_LISTS_HTML_CLASS.value})
                    html_array.append(processors_html)
            next_page_html = processors_html.find_all("a", {"class" : XkomConstants.PRODUCT_PREV_NEXT_PAGE_CLASS.value})

        return html_array

    def isNextPegeHtmlValid(self, page_html):
        for html in page_html:
            if (html.find("span", {"class" : XkomConstants.PRODUCT_NEXT_PAGE_SPAN.value}) is not None):
                return True
        return False

    def isNextPageSpanAvailable(self, html):
        if (html.find("span", {"class" : XkomConstants.PRODUCT_NEXT_PAGE_SPAN.value}) is not None):
            return True
        return False

    def _getVisibleTagText(self, tag):
        if tag.find("div", {"class" : "sc-13p5mv-1 jSuwtZ"}) is not None:
            return tag.find("div", {"class" : "sc-13p5mv-1 jSuwtZ"}).text

        return tag.find("div", {"class" : "sc-13p5mv-1 bRoFvv"}).text
