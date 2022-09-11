strlist = input("Enter nums: ")
templist = strlist.split(' ')

list1 = []

for i in range(0, len(templist)):
    if(float(templist[i])%1!=0):
        list1.append(float('0.' + templist[i].split('.')[1]))
    else:
        list1.append(0)

max = list1[0]
min = list1[0]
for i in range(1, len(list1)):
    if list1[i] > max:
        max = list1[i]
    if list1[i] < min:
        min = list1[i]

print(max-min)