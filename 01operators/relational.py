# relational operators
"""

> < >= <= == !=
"""

a = 10
b = 15
result = a > b
print(result)
print(type(result))
result = a < b
print(result)
print(type(result))
a = b
result = a >= b
print(result)
print(type(result))

result = a <= b
print(result)
print(type(result))

result = a == b
print(result)
print(type(result))

string1 = "hi"
string2 = "no"

result = string2 == string1
print(result)
string1 = string2
result = string2 == string1
print(result)

string1 = "hi"
string2 = "no"
result = string2 != string1
print(result)
string1 = string2
result = string2 != string1
print(result)
print(a!=b)

# in keyword

list = [1,2,5,6,87,4,85,9,4,6,4,54]
key = 5
result = key in list
print(result)

key = 51
result = key in list
print(result)


names = ["raju","rani","ram"]

key = "jio"
result = key in names
print(result)

key = "raju"
result = key in names
print(result)

# is keyword
same = list
result = list is same
print(result)
print(id(list))
print(id(same))

same = same + [6]

result = list is same
print(result)
print(id(list))
print(id(same))

print(list)
print(same)

# =

#5 = 8
# rule always make sure you have container
same+=[7]
#short hands

a = 5
b = 6

a,b = b,a
print(a)
print(b)

"""
no terinary
result = True ? True : False
print(result)
"""

