data = input("Input: ")

templist = data.split(" ")
indexlist = []
numslist = []

n = int(templist[0])

for i in range(1, len(templist)):
    indexlist.append(int(templist[i]))

for i in range(-n, n+1):
    numslist.append(i)

for i in range (0, len(indexlist)):
    print(numslist[indexlist[i]])

