liststr = input("Enter list (nums separated by ' '): ")
list1 = liststr.split(" ")

lenlist = len(list1)

list2 = []

for i in range(0, lenlist//2):
    list2.append(int(list1[i]) * int(list1[lenlist-1-i]))

if(lenlist%2==1):
    list2.append(int(list1[lenlist%2+1]) ** 2)

print(list2)
