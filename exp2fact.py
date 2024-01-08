sum = 1
number = 10
for i in range(1,number+1,1):
    sum *=i
print(sum)

sum = 1
number = 10
while number >= 1:
    sum*=number
    number-=1

print(sum)


sum = 1
number = 10
rlist = range(1,number+1,1)
rlist = rlist.__reversed__()
for i in rlist:
    sum *=i
print(sum)