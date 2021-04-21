from Models.Motherboard import Motherboard

class MotherboardFactory:

    @staticmethod
    def createMotherboard(builder):
        return Motherboard(builder)
