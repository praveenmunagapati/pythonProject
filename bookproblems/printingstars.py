"""

*****
****
***
**
*

12345
1234
123
12
1
"""
positions = [1,2,3,4,5]

for i in positions:
    print(i)

for i in range(1,6,1):
    print(i)

for i in range(1,6,1):
    for j in range(1,i,1):
        print(j)


for i in range(1,6,1):
    for j in range(1,i,1):
        print(j)
    print(end="\n")

for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(j,end="\t")
    print(end="\n")


for i in range(1,6,1).__reversed__():
    for j in range(1,i+1,1):
        print(j,end="\t")
    print(end="\n")

for i in range(5,0,-1):
    for j in range(1,i+1,1):
        print(j,end="\t")
    print(end="\n")

for i in range(1,6,1).__reversed__():
    for j in range(1,i+1,1):
        print(" * ",end="\t")
    print(end="\n")

n = 10
for i in range(1,n,1).__reversed__():
    for j in range(1,i+1,1):
        print(" * ",end="\t")
    print(end="\n")

for i in range(1,n,1).__reversed__():
    print(i * " * ")


"""
task 
https://leetcode.com/problems/two-sum/description/

"""