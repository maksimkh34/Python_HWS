import random

a = int(input())
b = int(input())

list1 = [ [0]*a for i in range(b) ]

for i in range(b):
    for j in range(a):
        list1[i][j] = random.randint(1, 11)

listav = []

for i in range(b):
    summ = 0
    for j in range(a):
        summ += list1[i][j]
    listav.append(summ/a)
print(list1)
print(listav)