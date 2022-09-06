num = float(input("Enter number: "))
spltdnum = int(str(num).split('.')[1])

sum = 0

while spltdnum>9:
    sum += spltdnum % 10
    spltdnum = spltdnum // 10
sum += spltdnum

print(sum)

# Еще один из вариантов решения задачи:
# Можно было превратить число в String и сложить все элементы
# от 2 до последнего (таким образом "0" и "." пропускаются, а остальные слаживаются)
# но мне показалось это слишком простым)