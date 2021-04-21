from .XkomConstants import XkomConstants

class XkomBuilder():
    def __init__(self, soup):
        self.soup = soup
        
    def getImage(self):
        image_span = self.soup.find("span", {"class" : XkomConstants.PROCESSOR_IMAGE_SPAN.value})
        if image_span is not None:
            image_src = image_span.find("img", {"class" : XkomConstants.PROCESSOR_IMAGE.value})["src"]
            return image_src
        return "" 

