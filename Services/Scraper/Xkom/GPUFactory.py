from Models.GPU import GPU

class GPUFactory:

    @staticmethod
    def createGPU(builder):
        return GPU(builder)
