"""
    function is a block code which performs a pertivuler task

        def function_name(parameters):
                statements1
                statements2
                statements3
                statements4
                statements5
                return

"""


def factorial(number=0):
    if number == 0:
        return 1
    else:
        sum = 1
        for i in range(1, number + 1):
            sum = sum * i
        return sum


result = factorial()
print(result)

result = factorial(5)
print(result)

a = 0
b = 1
c = a + b
print(a, end='\t')
print(b, end='\t')
print(c, end='\t')
a = b
b = c
c = a + b
print(c, end='\t')
a = b
b = c
c = a + b
print(c, end='\t')
a = b
b = c
c = a + b
print(c, end='\t')
a = b
b = c
c = a + b
print(c, end='\t')
a = b
b = c
c = a + b
print(c, end='\t')
a = b
b = c
c = a + b
print(c, end='\t')

while c <= 10000:
    a = b
    b = c
    c = a + b
    print(c, end='\t')


def fabinacci(number=100):
    a = 0
    b = 1
    c = a + b
    print(a, end='\t')
    while c <= number:
        a = b
        b = c
        c = a + b
        print(c, end='\t')


print()
result = fabinacci(5)
print()
print(result)


# recursion


def printinfinite(number):
    print(number)
    printinfinite(number + 1)


#printinfinite(1)
def factorialrecursive(number=0):

    if number == 0:
        return 1
    else:
        number = number * factorialrecursive(number-1)
        return number


result = factorialrecursive(5)
print(result)

result = factorialrecursive(number=5)
print(result)

def func(a = 0, b = 4,c = 6):
    print(a+b+c)

func(c=2,b=85,a=6)

def func(a = 0, b = 4,c = 6,*varg):
    print(a+b+c+sum(varg))

func(55,54,545,6,45,98,21,2,232,454,89,5)


