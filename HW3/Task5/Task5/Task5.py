fib1 = 0
fib2 = 1

k = int(input("Enter k: "))

plist = []

for i in range(0, k-1):
    fib1, fib2 = fib2, fib1 + fib2
    plist.append(fib2)

mlist = []

for i in range(0, len(plist)):
    j = len(plist) - i
    if(i%2==0): mlist.append(-plist[j - 1])
    else: mlist.append(plist[j - 1])

templist = [1, 0, 1]

list1 = mlist + templist + plist

print(list1)