num = float(input("Enter number: "))
spltdnum = int(str(num).split('.')[1])

sum = 0

while spltdnum>9:
    sum += spltdnum % 10
    spltdnum = spltdnum // 10
sum += spltdnum

print(sum)

# ��� ���� �� ��������� ������� ������:
# ����� ���� ���������� ����� � String � ������� ��� ��������
# �� 2 �� ���������� (����� ������� "0" � "." ������������, � ��������� �����������)
# �� ��� ���������� ��� ������� �������)