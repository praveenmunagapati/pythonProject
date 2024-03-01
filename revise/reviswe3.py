class person:
    def __init__(self):
        self.name = "ram"
        self.age = 25
        self.gender = "male"
    def walk(self):
        pass
    def eat(self):
        pass
    def __str__(self):
        return "person name is {0} and age is {1} HIS GENDER IS {2}".format(self.name,self.age,self.gender)

p = person()
print(p.__str__())


class person:
    def __init__(self):
        self.name = "ram"
        self.age = 25
        self.gender = "male"
    def __init__(self,name , age ,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def walk(self):
        pass

    def eat(self):
        pass

    def __str__(self):
        return "person name is {0} and age is {1} HIS GENDER IS {2}".format(self.name, self.age, self.gender)


p = person("sita",24,"female")
print(p.__str__())

class base:
    def __init__(self):
        self.data = "i am base var"

    def __str__(self):
        return "base data is {0} ".format(self.data)

class derived(base):
    # def __init__(self):
    #     super().__init__()
    #     self.data = "i am derived"
    #
    def __init__(self):
        super().__init__()
        self.data = super().__str__()
    def __str__(self):
        return "derived data is {0} ".format(self.data)

d = derived()
print(d.__str__())


class base:
    def __init__(self):
        self.data = "i am base var"

    def __str__(self):
        return "base data is {0} ".format(self.data)


class single(base):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return "base data is {0} ".format(self.data)

s = single()
print(s.__str__())



class base:
    def __init__(self):
        self.data = "i am base var"

    def __str__(self):
        return "base data is {0} ".format(self.data)


class single(base):
    def __init__(self):
        super().__init__()
        self.sdata = "i am single var"


    def __str__(self):
        return "base data is {0} ".format(self.data)


class multi(single):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "base data is {0} and single data is {1}".format(self.data,self.sdata)

m = multi()
print(m.__str__())