import os

from src.repo.AttractionJourney import AttractionJourney
from src.repo.RelaxJourney import RelaxJourney


class AddNewJou(object):
    def __init__(self):
        super().__init__()

    def whattoadd(self):
        self.number = int(input("add 1-relax, 2 -attraction : "))

    def check(self):
        self.whattoadd()
        if self.number == 1:
            self.readrelax()
        if self.number == 2:
            self.readattraction()

    def readnametoprice(self):
        print("give values: ")
        names = ["name: ", "hotel: ", "place: ", "price: "]
        self.whatusergave = []
        for i in range(0, 4):
            infromuser = input(names[i])
            self.whatusergave.append(infromuser)

    def readrelax(self):
        self.readnametoprice()
        pool = input("Pool: y/n ")
        golf = input("golf: y/n ")
        newrelax = RelaxJourney(self.whatusergave[0], self.whatusergave[1], self.whatusergave[2], self.whatusergave[3],
                                pool, golf)
        self.savetofile("relax.txt", newrelax.strtosave())

    def readattraction(self):
        self.readnametoprice()
        attractions = input("Attractions: ")
        newattraction = AttractionJourney(self.whatusergave[0], self.whatusergave[1], self.whatusergave[2],
                                          self.whatusergave[3], attractions)
        self.savetofile("attr.txt", newattraction.strtosave())

    def savetofile(self, fname, journey):
        file = open(os.path.join("data", fname), "a")
        file.write(journey + "\n")
        file.close()
