num = int(input("Enter number: "))

numlist = []

while(num>0):
    numlist.append(int(num%2))
    num = int(num//2)

strnum = ""

for i in range(0, int(len(numlist))):
    strnum += str(numlist[len(numlist) - 1 - i])

print(strnum)
