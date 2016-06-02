class Journey(object):
    name = ""
    hotel = ""
    place = ""
    price = 0

    def __init__(self, name, hotel, place, price):
        self.name = name
        self.hotel = hotel
        self.place = place
        self.price = price

    def __str__(self, *args, **kwargs):
        return super().__str__(*args, **kwargs)

    def getname(self):
        return self.name

    def __repr__(self, *args, **kwargs):
        return super().__repr__(*args, **kwargs)

# def make_journey(name, hotel, place, price):
#     journey = Journey(name, hotel, place, price)
#     return journey
