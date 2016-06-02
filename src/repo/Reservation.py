class Reservation(object):
    def __init__(self, username, journeyname):
        self.username = username
        self.journeyname = journeyname

    def __str__(self, *args, **kwargs):
        return "user=" + self.username + ", journey= " + self.journeyname

    def getusername(self):
        return self.username

    def getjourney(self):
        return self.journeyname
