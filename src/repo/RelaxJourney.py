from src.repo.Journey import Journey


class RelaxJourney(Journey):
    def __init__(self, name, hotel, place, price, golf, pool):
        Journey.__init__(self, name, hotel, price, place, )
        self.golf = golf
        self.pool = pool

    def __str__(self, *args, **kwargs):
        return self.name + " " + self.hotel + " " + self.place + " " + self.price + " " + self.golf + " " + self.pool

    def strtosave(self):
        return self.name + ";" + self.hotel + ";" + self.place + ";" + self.price + ";" + self.golf + ";" + self.pool
