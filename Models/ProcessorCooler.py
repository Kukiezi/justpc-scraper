from .Product import Product

class ProcessorCooler(Product):
    def __init__(self, builder):
        self.name = builder.setName()
        self.rpm = builder.setRpm()
        self.noise = builder.setNoise()
        self.compatibility = builder.setCompatibility()
        self.offer = builder.setOffer()
        self.image = builder.setImage()

    def print(self):
        print("nazwa: " + str(self.name) +
        ", rpm: " + str(self.rpm) +
        ", noise: " + str(self.noise) + 
        ", compatibility: " + str(self.compatibility))
