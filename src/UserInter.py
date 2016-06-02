import sys

from src import Open
from src.AddNewJou import AddNewJou
from src.DisplayRes import DisplayRes
from src.Save import Save


class UserInter(object):
    def __init__(self):
        self.relaxeslist = Open.openrel()
        self.attrlist = Open.openattr()
        self.displ = DisplayRes()

    def printwhattosee(self):
        number = int(input("1-relax, 2-attractions, 3-add new, 4- see reserv, 5- see buy:  "))
        return number

    def printrelax(self):
        print("name: hotel: place: price: golf: pool:")
        i = 1
        for real in self.relaxeslist:
            sys.stdout.write(str(i) + ": ")
            sys.stdout.write(str(real) + "\n")
            i += 1
        save = Save(self.relaxeslist, "relax.txt")
        save.checkreservationorbuy()

    def printattraction(self):
        print("name: hotel: place: price: attractions:")
        i = 1
        for attr in self.attrlist:
            sys.stdout.write(str(i) + ": ")
            sys.stdout.write(str(attr) + "\n")
            i += 1
        save = Save(self.attrlist, "attr.txt")
        save.checkreservationorbuy()


    def checkwhatuser(self):
        number = self.printwhattosee()
        if number == 1:
            self.printrelax()
        if number == 2:
            self.printattraction()
        if number == 3:
            add = AddNewJou()
            add.check()
        if number == 4:
            self.displ.printreserv()
        if number == 5:
            self.displ.printbuy()
