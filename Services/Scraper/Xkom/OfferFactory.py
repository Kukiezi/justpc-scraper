from Models.Offer import Offer

class OfferFactory:

    @staticmethod
    def createOffer(builder):
        return Offer(builder)
