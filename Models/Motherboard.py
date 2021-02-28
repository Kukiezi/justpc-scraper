from .Product import Product

class Motherboard(Product):
    def __init__(self, builder):
        self.name = builder.setName()
        self.socket = builder.setSocket()
        self.format = builder.setFormat()
        self.memory_max = builder.setMemoryMax()
        self.memory_slots = builder.setMemorySlots()
        self.memory_speed = builder.setMemorySpeed()
        self.chipset = builder.setChipset()
        self.offer = builder.setOffer()
        self.image = builder.setImage()

    def print(self):
        print("nazwa: " + str(self.name) +
        ", socket: " + str(self.socket) +
        ", format: " + str(self.format) +
        ", maksymalna pamięć: " + str(self.memory_max) +
        ", sloty pamięci: " + str(self.memory_slots) +
        ", chipset: " + str(self.chipset) +
        ", prędkość pamięci: " + str(self.memory_speed))
