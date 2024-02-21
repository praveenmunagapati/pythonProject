
# inheritance

class base:
    somevar = 10
    def __init__(self):
        print(" i am a  base")


class derived (base):
    def __init__(self):
        print(" i am a  derived")
        self.anothervar = self.somevar

    def printme(self):
        print(self.somevar)
        print(self.anothervar)

dev = derived()
dev.printme()



class me:
    mymoney = 10
    def __init__(self):
        print(" i am me")


class myfriend (me):
    def __init__(self):
        print(" i am a  myfriend")
        self.myfriendmoney = self.mymoney

    def printme(self):
        print(self.mymoney)

class myfriendfriend (myfriend):
    def __init__(self):
        print(" i am a  myfriendfriend")
        self.myfriendfriendmoney = self.mymoney

    def printme(self):
        print(self.mymoney)

myfriendfriendobject = myfriendfriend()
myfriendfriendobject.printme()



class A:
    class_a_var = 15
    def __init__(self):
        print("i am A")


class B:
    class_b_var = 20
    def __init__(self):
        print("i am B")


class C (A,B):
    def __init__(self):
        print("i am C")
        self.total = self.class_a_var + self.class_b_var

    def printtotal(self):
        print('totatl is ', self.total)


cobject = C()
cobject.printtotal()


class Total:
    def __init__(self):
        self.total = 0
class Add(Total):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.total = self.a + self.b
    def printtotal(self):
        print('add is ' ,self.total)

class Mul(Total):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.total = self.a * self.b
    def printtotal(self):
        print('mul is ' ,self.total)

class Div(Total):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.total = self.a / self.b
    def printtotal(self):
        print('div is ' ,self.total)



add = Add(5,6)
add.printtotal()
mul = Mul(5,6)
mul.printtotal()
div = Div(5,6)
div.printtotal()


class Numbers:
    def __init__(self):
        self.alist = [1,2,3,4,5,6,7,8,9]

class Sumofelements(Numbers):
    def __init__(self):
        super().__init__()
        self.total  = sum(self.alist)

class Noofelements(Numbers):
    def __init__(self):
        super().__init__()
        self.nolements = len(self.alist)

class Mean(Sumofelements,Noofelements):
    def __init__(self):
        super().__init__()
        self.mean = self.total / self.nolements

    def printmean(self):
        print(self.mean)
meanofalist = Mean()
meanofalist.printmean()

#https://chat.openai.com/share/72925310-29fa-4c7b-a9e2-e0a2698c46c6