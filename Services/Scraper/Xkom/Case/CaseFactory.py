from Models.Case import Case

class CaseFactory:

    @staticmethod
    def createCase(builder):
        return Case(builder)
