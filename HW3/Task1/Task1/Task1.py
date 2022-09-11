liststr = input("Enter list (nums separated by ' '): ")
list1 = liststr.split(" ")

sum = 0

for i in range(1, len(list1), 2):
    sum += int(list1[i])

print(f"Sum is: {sum}")