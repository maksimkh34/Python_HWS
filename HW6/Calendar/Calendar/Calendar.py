# -*- coding: cp1251 -*-

def getdate(str_):
    result = ""
    for i in range(16):
        result += str_[i]
    return result

def fwrite(text):
    file_ = open('data.txt', 'a', encoding="utf-8")
    file_.write(text)
    file_.close()

def getevent(str_):
    result = ""
    for i in range(17, len(str_)):
        result += str_[i]
    return result

def getdata():
    x = []
    f = open("data.txt", "r", encoding="utf-8")
    x = f.readlines()
    f.close()
    return x

def rewrite(_data):
    file_ = open('data.txt', 'w', encoding="utf-8")
    for i in range(len(_data)):
        file_.write(_data[i])
    file_.close()

cds = getdata()

if cds == []:
    temp = input("������ �� �������������. ������ ������� ����� �������? (��/���) ")
    if temp == "��": choise = 2
    else: exit()
else:
    choise = int(input("����������� (1), �������� (2), ��� �������� (3)?: "))



while choise != 0:
    if choise == 1:
        date_ = input("������� ���� � ����� (DD.MM.YYYY.HH.MM): ")
        eventexist = False
        for i in range(len(cds)):
            if date_ == getdate(cds[i]):
                print("������� �� " + date_ + ": " + getevent(cds[i]))
                eventexist = True
        if not(eventexist):
            print("�� ���� ���� ������ �� �������������.")
    if choise == 2:
        date_ = input("������� ���� � ����� (DD.MM.YYYY.HH.MM): ")
        ivent_ = input("������� �������: ")
        wr = date_ + ":" + ivent_ + "\n"
        fwrite(wr)
    if choise == 3:
        date_ = input("������� ���� � ����� (DD.MM.YYYY.HH.MM): ")
        eventexist = False
        for i in range(len(cds)):
            if date_ == getdate(cds[i]):
                newevent = input("����� ������� ����� �������������? ")
                ncds = cds
                ncds[i] = cds[i].replace(getevent(cds[i]), newevent)
                rewrite(ncds)
                eventexist = True
        if not(eventexist): print("�� ���� ���� ������ �� �������������")
    cds = getdata()
    choise = int(input("����������� (1), �������� (2), ��� �������� (3)?: "))

print("������ ���������. ")
exit()