from src import Open


class DisplayRes(object):
    def __init__(self):
        self.reservlist = Open.openreser()
        self.buylist = Open.openbuy()

    def printreserv(self):
        for reserv in self.reservlist:
            print(reserv)

    def printbuy(self):
        for buy in self.buylist:
            print(buy)