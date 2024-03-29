from Models.Processor import Processor
from Models.Motherboard import Motherboard
from Models.ProductTypes import ProductTypes
from .Processor.ProcessorBuilder import ProcessorBuilder
from .Motherboard.MotherboardBuilder import MotherboardBuilder
from .GPU.GPUBuilder import GPUBuilder
from .ProcessorCooler.ProcessorCoolerBuilder import ProcessorCoolerBuilder
from .Case.CaseBuilder import CaseBuilder

class ProductFactory:

    @staticmethod
    def createProduct(name, specifications, soup, product_type, offer):
        if product_type == ProductTypes.PROCESSOR.value:
            return ProcessorBuilder(name, specifications, soup, offer).build()
        if product_type == ProductTypes.MOTHERBOARD.value:
            return MotherboardBuilder(name, specifications, soup, offer).build()
        if product_type == ProductTypes.GPU.value:
            return GPUBuilder(name, specifications, soup, offer).build()
        if product_type == ProductTypes.PROCESSOR_COOLER.value:
            return ProcessorCoolerBuilder(name, specifications, soup, offer).build()
        if product_type == ProductTypes.CASE.value:
            return CaseBuilder(name, specifications, soup, offer).build()
            
        return ProcessorBuilder(name, specifications, soup, offer).build()
