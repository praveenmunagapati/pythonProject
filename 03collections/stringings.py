#stringd

iamastring = "ram"
print(type(iamastring))
print(iamastring)
iamastring = "rAm"

print(iamastring.casefold())
print(iamastring.count('r'))
print(iamastring.lower())
print(iamastring.upper())


తెలుగు  = 15
print(తెలుగు )
#string slicing
iamastring = "abc123"
print(iamastring[:])
print(iamastring[0:])
print(iamastring[1:])
print(iamastring[2:])
print(iamastring[3:])
iamastring = "abc123"
print(iamastring)
print(iamastring[:1])
print(iamastring[:2])
print(iamastring[:2])
print(iamastring[:-1])
print(iamastring[:-2])

# formating


print("1\n3")
print("1\t3")
print("1\r3")
print("1\\3")
print("1\*3")
print("1\"3")
print("1"+"\v"+"3")

#format
a = 10
b = 20
print(a,b)
print("a is " + str(a) +str(b))

print("a is {} and b is {}".format(a,b))
print("a is {0} and b is {1}".format(a,b))
print("a is {1} and b is {0}".format(a,b))
a = 10
b = 20.36
print("a is {} and b is {}".format(a,b))

print("a is %d and b is %f"%(a,b))











