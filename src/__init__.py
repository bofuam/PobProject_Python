from src import Open
from src.UserInter import UserInter
def doaction():
    ob = UserInter()
    ob.checkwhatuser()

if __name__ == '__main__':
    while True:
        doaction()
        if int(input("Zakonczyc? 0 - end")) == 0:
            break


