"""
    concept based on real world entities

    can make your own type

    code reusability


    syntax

    class class_name :
        data members
        functions

"""

class human:
    pass

#object syntax
man = human()

print(man)
print(type(man))

class human:
    def __init__(self):
        print(" i am a  human")

man = human()

class human:
    def __init__(human):
        print(" i am a  human")

man = human()


class human:
    spiecies = None
    def __init__(self,type):
        print(" i am a  human")
        self.spiecies = type
    def printme(self):
        print(self.spiecies)

man = human("home sapians")
man.printme()

class human:
    def __init__(human,type):
        print(" i am a  human")
        human.spiecies = type
    def printme(human):
        print(human.spiecies)

man = human("home sapians")
man.printme()






