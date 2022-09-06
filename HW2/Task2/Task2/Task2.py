num = int(input("Enter N: "))

for i in range(1, num+1):
    sum = 1
    for j in range(1, i+1):
        sum = sum * j
    print(sum)