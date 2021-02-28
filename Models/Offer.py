from .Product import Product

class Offer():
    def __init__(self, builder):
        self.shop = builder.setShop()
        self.link = builder.setLink()
        self.original_price = builder.setOriginalPrice()
        self.current_price = builder.setCurrentPrice()
