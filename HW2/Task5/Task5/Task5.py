import random

#listlength = int(input("Enter list length: "))
#nums = input('Enter nums, separating them with " " (spaces): ')
#numslist = nums.split(" ")
numslist = [-5, -1, 0, 1, 10, 164, -3, -9]

for i in range(0, len(numslist)):
    frand = int(random.uniform(0, len(numslist)))
    srand = int(random.uniform(0, len(numslist)))
    temp =  int(numslist[frand])
    numslist[frand] = int(numslist[srand])
    numslist[srand] = temp

print(numslist)