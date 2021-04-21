from Models.ProcessorCooler import ProcessorCooler

class ProcessorCoolerFactory:

    @staticmethod
    def createProcessorCooler(builder):
        return ProcessorCooler(builder)
