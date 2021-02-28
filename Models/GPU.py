from .Product import Product

class GPU(Product):
    def __init__(self, builder):
        self.name = builder.setName()
        self.chipset = builder.setChipset()
        self.memory = builder.setMemory()
        self.offer = builder.setOffer()
        self.image = builder.setImage()
        self.core_clock = builder.setCoreClock()
        self.boost_clock = builder.setBoostClock()

    def print(self):
        print("nazwa: " + str(self.name) +
        ", chipset: " + str(self.chipset) +
        ", pamięć: " + str(self.memory) +
        ", taktowanie: " + str(self.core_clock) +
        ", boost: " + str(self.boost_clock))
