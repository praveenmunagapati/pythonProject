import visibility.globals

class mysimpleclass:
    myclassvariable = 10
    def getmyclassvariable(self):
        global anyvar
        return self.myclassvariable + anyvar


s = mysimpleclass()
print(s.getmyclassvariable())