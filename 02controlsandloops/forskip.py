# key = 1
# number = 1
#
#
# for key in {True,False}:
#     print(key)
#
# for key in {True:True,False:False}:
#     print(key)
# key = 1
# for i in [1,2,3,4,5,6,7,8,9,10]:
#     print(str(key) + " X " + str(i) + " = "+ str(key*i))
#     number+=1
#
# key = 1
# for i in [1,2,3,4,5,6,7,8,9,10]:
#     print(str(key) + " X " + str(i) + " = "+ str(key*i))
#     number+=1
# start = 1
# end = 11
# step = 1
# for i in range(start,end,step):
#     print(str(key) + " X " + str(i) + " = "+ str(key*i))
#     number+=1
#
# number = 100
# temp = 0
# sum = 0
# while temp <= number:
#     sum = temp + sum
#     temp += 2
# print(sum)
#

number = 100
step = 2
start = 0
sum = 0
for k in range(start,number+1,step):
    sum+=k
print(sum)

number = 100
step = 2
start = 1
sum = 0
for k in range(start,number+1,step):
    sum+=k
print(sum)