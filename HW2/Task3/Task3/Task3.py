num = int(input("Enter k: "))

mylist = []

for i in range(1, num+1):
    mylist.append(float((1 + 1 / i) ** i))

print(mylist)