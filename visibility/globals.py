# import random
#
# anyvar = 90
# def randome(anyvar1 = 15):
#     global anyvar
#     anyvar1 = anyvar
#     return anyvar1
#
# print(randome(56))
# print(anyvar)
#
#
# varbar = 20
# def foo():
#
#     varr = varbar
#     print(varbar)
# foo()
# print(varbar)



z= 10 #global variable




class glob:
    def __init__(self):
        global z
        z = 80
        self.a = z
        self.z = z

    def print(self):
        print(self.a)
        print(self.z)

a = glob()
a.print()

def foo():
    global z
    sum = z
    print(sum)

foo()