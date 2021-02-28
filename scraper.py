import time
from Services.Scraper.Xkom.ScraperXkom import ScraperXkom
from Models.ProductTypes import ProductTypes
from query import insertProcessor, insertMotherboard, insertGPU, inserCPUCooler


processor_url = "/g-5/c/11-procesory.html?per_page=90"
cpu_cooler_url = "/g-5/c/105-chlodzenia-procesorow.html?per_page=90" 
GPU_url = "/g-5/c/345-karty-graficzne.html?per_page=90"
motherboard_url = "/g-5/c/14-plyty-glowne.html?per_page=90"

urls = {
    "/g-5/c/11-procesory.html?per_page=90": ProductTypes.PROCESSOR.value,
    "/g-5/c/345-karty-graficzne.html?per_page=90": ProductTypes.GPU.value,
    "/g-5/c/14-plyty-glowne.html?per_page=90": ProductTypes.MOTHERBOARD.value,
}

def performProcessor():
    scraper = ScraperXkom(processor_url, ProductTypes.PROCESSOR.value)
    products = scraper.scrape()
    for product in products:
        insertProcessor(product)

def performGpu():
    scraper = ScraperXkom(GPU_url, ProductTypes.GPU.value)
    products = scraper.scrape()
    for product in products:
        insertGPU(product)

def performMotherboard():
    scraper = ScraperXkom(motherboard_url, ProductTypes.MOTHERBOARD.value)
    products = scraper.scrape()
    for product in products:
        insertMotherboard(product)

def performCPUCooler():
    scraper = ScraperXkom(cpu_cooler_url, ProductTypes.PROCESSOR_COOLER.value)
    products = scraper.scrape()
    for product in products:
        inserCPUCooler(product)


start = time.time()

performProcessor()
performMotherboard()
performGpu()
performCPUCooler()

end = time.time()
print("Process took total time: {}".format(end - start))

# scraper = ScraperXkom(processor_cooler_url, ProductTypes.PROCESSOR_COOLER.value)
# scraper = ScraperXkom(processor_url, ProductTypes.PROCESSOR.value)
# processors = scraper.scrape()
# product = scraper.scrapeProduct("/p/565208-chlodzenie-procesora-be-quiet-pure-rock-2-czarny-120mm.html")
# product.print()
# product.print()
# for processor in processors:
#     insertGPU(processor)
# product = scraper.scrapeProduct("/p/586239-procesor-intel-core-i9-intel-core-i9-10900k-avengers-edition.html")
# product.print()

