#single line
"""
multi
    line
        comment
"""

# python interpreted

"""

:keywords
    False      await      else       import     pass
    None       break      except     in         raise
    True       class      finally    is         return
    and        continue   for        lambda     try
    as         def        from       nonlocal   while
    assert     del        global     not        with
    async      elif       if         or         yield


"""

# datatypes
# boolean
# True , False

#numbers

# variable

# int variable = value or varible;
# container = value or container
# rules

""" what not to do

nos 
no numbers at start of variable name
no spaces between varible name
no special characters other than underscore (_)
"""

# none type
none = None # value must be initialise in order to make memory f0r variable in ram
print(none)
print(type(none))
print(id(none))
#print(None + None) # just a place holder

# boolean for decisions
boolean = True
print(boolean)
print(type(boolean))
print(id(boolean))

boolean = False
print(boolean)
print(type(boolean))
print(id(boolean))

# numbers

numbers = 10
print(numbers)
print(type(numbers))
print(id(numbers))
numbers = -10
print(numbers)
print(type(numbers))
print(id(numbers))

precisenumbers = 10.50
print(precisenumbers)
print(type(precisenumbers))
print(id(precisenumbers))
precisenumbers = -10.50
print(precisenumbers)
print(type(precisenumbers))
print(id(precisenumbers))

precisenumbers = -10.5046545454546465 #  no double
print(precisenumbers)
print(type(precisenumbers))
print(id(precisenumbers))

#no upperbound or lowerbound
nosizelimitnumbers = 1065975634853478658962347562478893762358974635368975634786378658926
print(nosizelimitnumbers)
print(type(nosizelimitnumbers))
print(id(nosizelimitnumbers))

nosizelimitnumbers = -1065975634853478658962347562478893762358974635368975634786378658926
print(nosizelimitnumbers)
print(type(nosizelimitnumbers))
print(id(nosizelimitnumbers))


# complex numbers

imagianrynumber = 5 + 8j
print(imagianrynumber)
print(type(imagianrynumber))
print(id(imagianrynumber))

# compound types

#strings
singlecharator = 'r'
print(singlecharator)
print(type(singlecharator))
print(id(singlecharator))
name = "ram"
print(name)
print(type(name))
print(id(name))
paragraphs = """ 
            print(imagianrynumber)
            print(type(imagianrynumber))
            print(id(imagianrynumber))
        """
print(paragraphs)
print(type(paragraphs))
print(id(paragraphs))

# array starts with index 0
name = "ram"
print(name[0])
print(name[1])
print(name[2])
# print(name[4])
# print(name[-1])

# primitive compound types

"""
list        []
tuple       ()
set         {}
dictionary {}
"""

#mutable types

numbers = [1,2,3,4,5,6]# dec and init
print(numbers)
numbers = list([1,2])
print(numbers)
print(numbers[0])
print(numbers[1])
print(numbers[-1])#from end
print(numbers[-2])

#sets
# duplicates not allowed

noduplicates = {1,2,3,3,4,4,5,6}# dec and init
print(noduplicates)
print(list(noduplicates)[0])

# dictionary
index = "age"
value = 50
keyvalue = {index:value,"name":"ram"}
print(keyvalue)
print(keyvalue['age'])
print(keyvalue['name'])


#immutable
#tuple
wontchange = ("ram",20,"sita")
print(wontchange)
print(wontchange[0])
print(wontchange[1])
print(wontchange[2])

# operators
# arhthematic
# + - / * %
a = 10
b = 15
result = a+b
print(result)
c = 26
#operator precedence
result = a + b + c#left to right for + - operators
# minus -
result = a-b
print(result)
# multiplication *
result = a*b
print(result)
# division /
result = a/b
print(result)

# modulus %
a = 10
b = 15
result = a%b # will give a value bcuz its smaller than b
print(result)
a = 110
b = 15
result = a%b # will give reminder
print(result)

# no inc dec operators
# exponent **
a = 25
print(a ** 2) # 25  * 25 = 625

#relational operators

# < , >, <= , >= , == ,!=

a = 10
b = 15
result = a > b
print(result)
print(type(result))

result = a < b
print(result)
print(type(result))

result = a >= b
print(result)
print(type(result))

result = a <= b
print(result)
print(type(result))

result = a == b
print(result)
print(type(result))

result = a != b
print(result)
print(type(result))

# logical operators

# and or not
#AND # if both expressions are true then it is true
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#Or # if both expressions are false it is false
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# not # true to false , false to true
print(not True)
print(not False)

# bitwise
# & | ~ ^ << >>

a = 10
b = 15
result = a & b
print(bin(a))
print(bin(b))
print(bin(result))
print(result)

a = 100
b = 15
result = a & b
print(bin(a))
print(bin(b)) #0b1111 => 0b00001111 & 0b1100100
print(bin(result))
print(result)

a = 100
b = 15
result = a | b
print(bin(a))
print(bin(b)) #0b1111 => 0b00001111 & 0b1100100
print(bin(result))
print(result)

a = 100
b = 15
result = a ^ b
print(bin(a))
print(bin(b)) #0b1111 => 0b00001111 & 0b1100100
print(bin(result))
print(result)


# compliment operator
print(~2)
print(~-3)
print(~(~2))

a = 10
print(a<<2)# multiply by 2 power n
print(a>>2)# divide by 2 power n


#control statements
"""
syntax if condition:
            statement1
            statement2
            statement3
rest of statements
"""

if True:
    print("this will excecute")
    print("this also will excecute")

print(" i am not part of if ")

if True:
    print("this will excecute")
    print("this also will excecute")
    if False:
        print("this will not excecute")
        print("this also will not excecute")

print(" i am not part of if ")


"""
if else
syntax
    if  condition:
            statement1
            statement2
            statement3
    else :
            statement1
            statement2
            statement3  
            
rest of statements
"""

a = 10

if a>=0:
    print("a is positive")
else:
    print("a is negative")

a = -10

if a>=0:
    print("a is positive")
else:
    print("a is negative")

"""
elif
syntax
    if  condition:
            statement1
            statement2
            statement3
    elif condition :
            statement1
            statement2
            statement3  
    elif condition :
            statement1
            statement2
            statement3  

"""

current_signal = "green"
if current_signal == "red":
    print("walk on zebra")
    print("stop engine")
elif current_signal == "orange":
    print("start engine")
elif current_signal == "green":
    print("go go go")


current_signal = "red"
if current_signal == "red":
    print("walk on zebra")
    print("stop engine")
elif current_signal == "orange":
    print("start engine")
elif current_signal == "green":
    print("go go go")


current_signal = "orange"
if current_signal == "red":
    print("walk on zebra")
    print("stop engine")
elif current_signal == "orange":
    print("start engine")
elif current_signal == "green":
    print("go go go")

"""
while 

syntax 
    while condition:
            statement1
            statement2
            statement3  

"""

while False:
    print("catch me if you can")
"""
while True:
    print("oops!")
    """
start = 0
stop = 100
step = 10

while start < stop:
    print(start)
    start+=step

while False:
    print("catch me if you can")
else:
    print("no while for you")

"""
for 

    for container in container:
                statement1
                statement2
                statement3 

"""

simple_list = [1,1.0,"ram",6+8j]

for i in simple_list:
    print(i)



for i in simple_list:
    print(i)
else:
    print("simple list completed")

"""
jumps

break 

continue

"""

i = 0

while True:
    print(i)
    if i == 5:
        print("skipped")
        i += 1
        continue
    if i >=100:
        break
    i+=1