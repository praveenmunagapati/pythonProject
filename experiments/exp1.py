"""
conditions

"""

"""
syntax if condition :
            statement1
            statement2
            statement3
"""

a = 10
b = 25

if a > b :
    print(" a is big")

if a < b :
    print(" a is big")


c = 15

if a > b:
    if a > c :
        print("a is big")

if b > a:
    if b > c :
        print("b is big")

if c > a:
    if c > b :
        print("c is big")

# else
a = 105
b = 80
c = 200
if a > b:
    if a > c :
        print("a is big")
    else:
        print("c is big")
else:
    if b > c:
        print("b is big")


if a > b and a > c :
    print("a is big")
if b > a and b > c :
    print("b is big")
if c > b and c > a :
    print("c is big")

if a > b and a > c :
    print("a is big")
else:
    if b > a and b > c :
        print("b is big")
    else:
        if c > b and c > a :
            print("c is big")

#elif
if a > b and a > c :
    print("a is big")
elif b > a and b > c :
    print("b is big")
elif c > b and c > a :
    print("c is big")

