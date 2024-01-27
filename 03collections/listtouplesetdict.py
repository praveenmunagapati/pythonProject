#list

simplelist = [] # empty list
print(type(simplelist))
print(simplelist)

#crud
# create
simplelist.append(5) # add element 5
print(simplelist)
simplelist.append(15) # add element 15
simplelist.append(50) # add element 50
simplelist.append(55) # add element 55
print(simplelist)

# read
for i in simplelist:
    print(i) # reading one by one

# update

simplelist.insert(0,10)
print(simplelist)
#
# key = input(" enter which element you want to replace : ")
# key = int(key)
# index = 0
# for i in simplelist:
#
#     if i == key:
#         simplelist[index] = -1
#     index+=1
#
# print(simplelist)
# print(enumerate(simplelist))#enumerate

# del simplelist[0]
# print(simplelist)
#
# del simplelist
# print(simplelist)


# tuple

# immutable

tuplers = ()

print(type(tuplers))
print(tuplers)

tuplers.__add__((1, 2, 3, 4, 5, 6))# noooooooooo
#create
tuplers+=(10, 2, 3, 4, 5, 6)
print(tuplers)
#read

for i in tuplers:
    print(i)

#update
# no update for you

#delete
# del tuplers
# print(tuplers)


#set

aset = {} #convention with symbol
aset = set() # constructor

print(type(aset))


#create
aset.add(2)
print(aset)
aset.add(20)
print(aset)
aset.add(12)
print(aset)

#read

for i in aset:
    print(i)

#update

aset.pop()
print(aset)
aset.update([56])
print(aset)
aset.remove(56)
print(aset)

aset.clear()
print(aset)

# del aset
#
# print(aset)

#dictionary

adictionary = {}

#create
adictionary.update({"a":10})
print(adictionary)
adictionary.update({"b":20})
print(adictionary)

#read

for i in adictionary.keys():
    print(adictionary[i])

#update
for i in adictionary.keys():
    if i == 'a':
        adictionary[i] = 56

print(adictionary)


#delete
#
# del adictionary['a']
# print(adictionary)
#
# del adictionary
# print(adictionary)


list = [1,2,5,6,4]

if 5 in list:
    print("exist")