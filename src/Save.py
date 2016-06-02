import os

from src.repo.Buy import Buy
from src.repo.Reservation import Reservation


class Save(object):
    def __init__(self, list, ftodel):
        super().__init__()
        self.ftodel = ftodel
        self.list = list

    def checkreservationorbuy(self):
        num = int(input("want to reserv - 1 or buy - 2, anothoer - 3 : "))
        if num == 3:
            self.breaksaveclass()
        number = self.whichline()
        self.findstringtosave(number)
        if num == 1:
            self.fname = "reserv.txt"
            reservation = Reservation(self.getusername(), self.a)
            self.savetofile(reservation.getusername(), reservation.getjourney(), "")
        if num == 2:
            self.fname = "buy.txt"
            buy = Buy(self.getusername(), self.a, self.forhowmany())
            self.savetofile(buy.getusername(), buy.getjourney(), buy.getforhowmany())
            self.deletefromfile()

    def breaksaveclass(self):
        from src import UserInter
        obj = UserInter()
        obj.checkwhatuser()

    def getusername(self):
        self.username = input("Give me yourname: ")
        return self.username

    def whichline(self):
        print("which you want to reserv od buy")
        number = int(input())
        return number - 1

    def findstringtosave(self, number):
        try:
            self.a = self.list[number]
            return self.a
        except IndexError:
            print("once again")
            return self.findstringtosave(self.list)

    def forhowmany(self):
        self.howmany = input("for how many: ")
        return self.howmany

    def deletefromfile(self):
        file = open(os.path.join("data", self.ftodel), "r")
        lines = file.readlines()
        file.close()
        file = open(os.path.join("data", self.ftodel), "w")
        for line in lines:
            word = line.split(';')
            secondword = str(self.a).split()
            if word[0] != secondword[0]:
                file.write(line)
        file.close()

    def savetofile(self, first, second, third):
        file = open(os.path.join("data", self.fname), "a")
        file.write(str(first) + ";" + str(second) + ";" + str(third) + "\n")
        file.close()
