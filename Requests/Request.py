from providers.Factory import Factory
import requests

class Request:

    def get(self, url):
        header_provider = Factory.createHeaderProvider()
        headers = header_provider.getRandomUserAgent()
        response = requests.get(url, headers=headers)
        return response
