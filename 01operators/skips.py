
"""
break
continue

"""

number = 100
temp = 0
sum = 0
# while True:
#     sum = temp + sum
#     temp += 2
#     print(sum)
# print(sum)

while True:
    sum = temp + sum
    temp += 2
    if(temp > number):
        break
print(sum)
number = 100
temp = 0
sum = 0
#continue
while True:
    if(temp > number):
        break
    if(temp%2==0):
        sum = temp + sum
        temp += 1
    else:
        temp += 1
        continue


print(sum)


infinite = 1
#break
while True :
    print(infinite)
    if infinite == 198:
        break
    infinite +=1

#continue

for i in [1,2,3,4,5,6,7,8,9,10]:
    if(i == 5):
        continue
    print(i)


