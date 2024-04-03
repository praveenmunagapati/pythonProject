import re
str = "ram@A2024"


matchsmall = re.findall("[a-z]+",str)
print(matchsmall)

matchcap = re.findall("[A-Z]+",str)
print(matchcap)

matchdisigts = re.findall("[0-9]+",str)
print(matchdisigts)

matchspc = re.findall("[@,#&!]+",str)
print(matchspc)
if(len(matchsmall)==0):
    print("needs small alphabets")
elif(len(matchcap)==0):
    print("needs  capital alphabets")
elif(len(matchdisigts)==0):
    print("needs numbers ")
elif(len(matchspc)==0):
    print("needs special charactors ")
else:
    print("good password")

