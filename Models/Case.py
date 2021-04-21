from .Product import Product

class Case(Product):
    def __init__(self, builder):
        self.name = builder.setName()
        self.cabinet_type = builder.setCabinetType()
        self.side_panel = builder.setSidePanel()
        self.image = builder.setImage()
        self.offer = builder.setOffer()

    def print(self):
        print("nazwa: " + str(self.name) +
        ", taktowanie: " + str(self.cabinet_type) +
        ", image: " + str(self.image))
