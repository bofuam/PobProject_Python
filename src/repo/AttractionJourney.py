from src.repo.Journey import Journey


class AttractionJourney(Journey):

    def __init__(self, name, hotel, place, price, attractions):
        Journey.__init__(self, name, hotel, place, price)
        self.attractions = attractions

    def __str__(self, *args, **kwargs):
        return self.name + " " + self.hotel + " " + self.place + " " + self.price + " " + self.attractions

    def strtosave(self):
        return self.name + ";" + self.hotel + ";" + self.place + ";" + self.price + ";" + self.attractions
