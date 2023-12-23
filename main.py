a = 0
b = 1
c = a+b

#1 interation
print(a)
print(b)
print(c)

#2 interation
a = b
b = c
c= a+b
print(c)
#3 interation

a = b
b = c
c= a+b
print(c)
#4 interation

a = b
b = c
c= a+b
print(c)
#5 interation

a = b
b = c
c= a+b
print(c)
#6 interation

a = b
b = c
c= a+b
print(c)

limit = input("enter number of fab to display  : ")
limit = int(limit)
print(limit)
print(type(limit))

while limit > 0:
    a = b
    b = c
    c = a + b
    print(c)
    limit = limit - 1
