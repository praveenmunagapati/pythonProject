# matrix addition
# 2  by 2 matrix
# formula is to map one to one index of 2d list.
# and add them to create a new matrix
matrixa = [[1, 2], [3, 4]]
matrixb = [[5, 6], [7, 8]]
matrixr = [[0, 0], [0, 0]]
# matrix addition
# need two loops
print(matrixa)
print(matrixb)
# prints 1d matrix
# for i in matrixa:
#     print(i)

# prints individual values
# for i in matrixa:
#     for j in i:
#         print(j)
#

# #now lets add them
# for i,j in matrixa,matrixb:
#     for k,l in i,j:
#         print(k,l)

# print(len(matrixa))
# print(len(matrixb))
#
# for i in range(len(matrixa)):
#     print(matrixa[i])
#
# for i in range(len(matrixa)):
#     for j in range(len(matrixa)):
#         print(matrixa[j])
#
# for i in range(len(matrixa)):
#     for j in range(len(i)):
#         matrixr[j] = matrixa[j] + matrixb[j]
#
# print(matrixr)

# for i in matrixa:
#     print(i)
#     print(type(i))
# for i in matrixa:
#     for j in i:
#         print(j)
# for i,j in matrixa,matrixb:
#     for k,l in i,j:
#         print(k,l)

# for i,j in matrixa,matrixb:
#     print(i)
#     print(j)

# print(sum(matrixa[0][0]+matrixb[0][0]))
# print(sum(matrixa[0][1]+matrixb[0][1]))
# print(sum(matrixa[1][0]+matrixb[1][0]))
# print(sum(matrixa[1][1]+matrixb[1][1]))
print(matrixa[0][0] + matrixb[0][0])
print(matrixa[0][1] + matrixb[0][1])
print(matrixa[1][0] + matrixb[1][0])
print(matrixa[1][1] + matrixb[1][1])

matrixr[0][0] = matrixa[0][0] + matrixb[0][0]
matrixr[0][1] = matrixa[0][1] + matrixb[0][1]
matrixr[1][0] = matrixa[1][0] + matrixb[1][0]
matrixr[1][1] = matrixa[1][1] + matrixb[1][1]

print(matrixr)
matrixr = [[0, 0], [0, 0]]

for i in range(len(matrixa)):
    for j in range(len(matrixb)):
        matrixr[i][j] = matrixa[i][j] + matrixb[i][j]

print(matrixr)

matrixa = [[1, 2], [3, 4]]
matrixb = [[5, 6], [7, 8]]
matrixr = [[0, 0], [0, 0]]

# mat add
for i in range(len(matrixa)):
    for j in range(len(matrixb)):
        matrixr[i][j] = matrixa[i][j] + matrixb[i][j]

print(matrixr)

matrixa = [[1, 2],
           [3, 4]]
matrixb = [[5, 6],
           [7, 8]]
matrixr = [[0, 0], [0, 0]]

# mat mul
matrixr[0][0] = matrixa[0][0] * matrixb[0][0] + matrixa[0][1] * matrixb[1][0]
matrixr[0][1] = matrixa[0][0] * matrixb[0][1] + matrixa[0][1] * matrixb[1][1]
matrixr[1][0] = matrixa[1][0] * matrixb[0][0] + matrixa[1][1] * matrixb[1][0]
matrixr[1][1] = matrixa[1][0] * matrixb[0][1] + matrixa[1][1] * matrixb[1][1]
"""
        0 =   0 , 0 , 1 , 2
        1 =   0 , 1 , 1 , 3
        2 =   2 , 0 , 3 , 2
        3 =   2 , 1 , 3 , 3
"""
print(matrixr)

