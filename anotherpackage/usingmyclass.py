import myclass
from myclass.myclass import mysimpleclass

class anotherclass(mysimpleclass):
    def print(self):
        print(self.myclassvariable)

ac = anotherclass()
ac.print()
