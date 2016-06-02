from src.repo.Reservation import Reservation


class Buy(Reservation):
    def __init__(self, username, journeyname, howmany):
        super().__init__(username, journeyname)
        self.howmany = howmany

    def __str__(self, *args, **kwargs):
        return super().__str__(*args, **kwargs) + ", for: " + self.howmany

    def getforhowmany(self):
        return self.howmany