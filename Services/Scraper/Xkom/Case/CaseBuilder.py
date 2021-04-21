from .CaseFactory import CaseFactory
from ..XkomConstants import XkomConstants
from ..XkomBuilder import XkomBuilder

class CaseBuilder(XkomBuilder):
    def __init__(self, name, specifications, soup, offer):
        XkomBuilder.__init__(self, soup)
        self.name = name
        self.specifications = specifications
        self.offer = offer
        
    def setName(self):
        return self.name
    
    def setOffer(self):
        return self.offer
        
    def setCabinetType(self):
        cabinet_type = self.specifications.get(XkomConstants.CASE_CABINET_TYPE.value)
        return cabinet_type
        
    def setSidePanel(self):
        side_panel = self.specifications.get(XkomConstants.CASE_SIDE_PANEL.value)
        return side_panel

    def setImage(self):
        image = self.getImage()
        return image

    def build(self):
        return CaseFactory.createCase(self)
