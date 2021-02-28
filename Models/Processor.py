from .Product import Product

class Processor(Product):
    def __init__(self, builder):
        self.name = builder.setName()
        self.series = builder.setSeries()
        self.cores = builder.setCores()
        self.core_clock = builder.setCoreClock()
        self.boost_clock = builder.setBoostClock()
        self.socket = builder.setSocket()
        self.integrated_graphics = builder.setIntegratedGraphics()
        self.includes_cooler = builder.setIncludesCooler()
        self.cache_memory = builder.setCacheMemory()
        self.offer = builder.setOffer()
        self.image = builder.setImage()

    def print(self):
        print("nazwa: " + str(self.name) +
        ", seria: " + str(self.series) +
        ", rdzenie: " + str(self.cores) + 
        ", taktowanie: " + str(self.core_clock) +
        ", boost: " + str(self.boost_clock) +
        ", socket: " + str(self.socket) +
        ", grafika zintegrowana: " + str(self.integrated_graphics) +
        ", pamiec podreczna: " + str(self.cache_memory) +
        ", chlodzenie w zestawie: " + str(self.includes_cooler) +
        ", offer url: " + str(self.offer.link) + 
        ", image: " + str(self.image)) 
