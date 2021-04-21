from Models.Processor import Processor

class ProcessorFactory:

    @staticmethod
    def createProcessor(builder):
        return Processor(builder)
