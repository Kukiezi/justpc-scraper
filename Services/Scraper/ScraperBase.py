import logging

from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from Requests.RequestFactory import RequestFactory
from Services.Scraper.Xkom.XkomConstants import XkomConstants
from Models.Product import Product
import traceback

class ScraperBase(ABC):

    BASE_URL = "https://www.x-kom.pl"
    request = RequestFactory.createRequest()
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d] %(message)s",
        datefmt='%m/%d/%Y %I:%M:%S %p'
    )
    """
    Template method.
    products_links is a list of lists. Contains list of lists of product links for specific category
    """

    def scrape(self):
        logging.info("Starting scraping HTML from all pages")
        html_array = self.getHtmlFromAllPagesToArray()
        products = []

        for html in html_array:
            products_links = self.getProductLinksFromPage(html)
            logging.info("Scraping batch of {0} products".format(len(products_links)))
            for link in products_links:
                    product = self.scrapeProduct(str(link))
                    if isinstance(product, Product):
                        products.append(product)

        logging.info("Scraped total of {0}".format(str(len(products))))
        return products

    def scrapeProduct(self, relative_url):
        try:
            url = self.BASE_URL + str(relative_url)
            response = self.request.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            return self.getProductData(soup, url)
        except Exception as e:
            logging.error("Product with link {0} failed to scrape with exception: {1}".format(url, e))
            traceback.print_exc()

    @abstractmethod
    def getUrl(self):
        pass

    @abstractmethod
    def getHtmlFromAllPagesToArray(self):
        pass

    @abstractmethod
    def setUrl(self, url):
        pass

    @abstractmethod
    def getBaseUrl(self):
        pass

    @abstractmethod
    def getProductLinksFromPage(self, soup):
        pass

    @abstractmethod
    def getProductData(self, soup, url):
        pass
