import os

from src.repo.AttractionJourney import AttractionJourney
from src.repo.Buy import Buy
from src.repo.RelaxJourney import RelaxJourney
from src.repo.Reservation import Reservation


def openrel():
    with open(os.path.join("data", "relax.txt")) as f:
        relaxeslist = []
        for line in f:
            words = line.split(';')
            if len(words) < 6:
                return relaxeslist
            relaxone = RelaxJourney(words[0], words[1], words[2], words[3], words[4], words[5])
            relaxeslist.append(relaxone)
        return relaxeslist

def openattr():
    with open(os.path.join("data", "attr.txt")) as f:
        attrlist = []
        for line in f:
            words = line.split(';')
            if len(words) < 5:
                return attrlist
            attrctionone = AttractionJourney(words[0], words[1], words[2], words[3], words[4])
            attrlist.append(attrctionone)
        return attrlist

def openreser():
    with open(os.path.join("data", "reserv.txt")) as f:
        reservlist = []
        for line in f:
            words = line.split(';')
            if len(words) < 2:
                return reservlist
            reserv = Reservation(words[0], words[1])
            reservlist.append(reserv)
        return reservlist

def openbuy():
    with open(os.path.join("data", "buy.txt")) as f:
        buylist = []
        for line in f:
            words = line.split(';')
            if len(words) < 3:
                return buylist
            buy = Buy(words[0], words[1], words[2])
            buylist.append(buy)
        return buylist
