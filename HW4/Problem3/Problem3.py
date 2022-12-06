import random

def findmin(list_a):
    minf = list_a[0]
    index = 0
    for i in range(1, len(list_a)):
        if list_a[i] < minf:
            minf = list_a[i]
            index = i
    return index

list1 = []
list2 = []

for i in range(30):
    list1.append(random.randint(1, 50))

print(list1)

for i in range(len(list1)):
    f = findmin(list1)
    list2.append(list1[f])
    list1.pop(f)

print(list2)