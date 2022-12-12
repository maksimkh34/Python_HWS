# -*- coding: cp1251 -*-
# ���� �������� ��� ����� ���� ��� �� ����� ������, ��� ��� ������� �������� ������� ������ ���
import random

def victory(field_):
    for i in range(len(field_)):
        for j in range(len(field_)):
            if field_[i][j] != 0: 
                return False
    return True


def iin(text):
    return int(input(text))

def generatefield(size, level):
    field = [[0 for x in range(size)] for y in range(size)]

    tlevel = level
    while level!=0:
        for n in range(tlevel - level + 1):
           posx = iin("������� X (0 - " + str(size-1) + ") ��� ������� � " + str(level) + " ��������: ")
           posy = iin("������� X (0 - " + str(size-1) + ") ��� ������� � " + str(level) + " ��������: ")
           if level!=1:
               rotation = iin("������� ������� (1 - up, 2 - right, 3 - down, 4 - left): ")
               for i in range(level):
                   field[posy][posx] = level
                   if rotation == 1: posy -= 1
                   elif rotation == 2: posx += 1
                   elif rotation == 3: posy += 1
                   elif rotation == 4: posx -= 1
           else:
               field[posy][posx] = 1
        level-=1
    return field

def printfield(field):
    for i in range(len(field)):
        print(field[i])

def generateaifield(size, level):
    print("")
    print("��������� ���� ��...")
    level = tlevel
    aifield = [[0 for x in range(size)] for y in range(size)]
    occd = [] 
    while level!=0:
        imposrot = [] 
        pospos = True 
        posship = False
        for n in range(tlevel - level + 1):
            posx = random.randint(0, size-1)
            posy = random.randint(0, size-1)
            pos = [posx, posy]
            while pos in occd:
                posx = random.randint(0, size-1)
                posy = random.randint(0, size-1)
                pos = [posx, posy]
            occd.append(pos)
            if level!=1:
                while not(posship):
                    rotation = random.randint(1, 4)
                    while rotation in imposrot:
                        rotation = random.randint(1, 4)
                        if len(imposrot)==4: 
                            posx = random.randint(0, size-1)
                            posy = random.randint(0, size-1)
                            pos = [posx, posy]
                            while pos in occd:
                                posx = random.randint(0, size-1)
                                posy = random.randint(0, size-1)
                                pos = [posx, posy]
                            occd.append(pos)
                            imposrot = []
                    imposrot.append(rotation)

                    if rotation == 1:
                        if posy-(level-1)>=0:
                            pospos=True
                            for i in range(posy-level+1, posy+1):
                                if aifield[i][posx] != 0:
                                    pospos=False
                        else: pospos=False

                    if rotation == 3:
                        if posy+(level-1) < size:
                            pospos=True
                            for i in range(posy, posy+level):
                                if aifield[i][posx] != 0: 
                                    pospos=False
                        else: pospos=False

                    if rotation == 2:
                        if posx+(level-1) < size:
                            pospos=True
                            for i in range(posx, posx+level):
                                if aifield[posy][i] != 0: 
                                    pospos=False
                        else: pospos=False

                    if rotation == 4:
                        if posx-(level-1)>=0:
                            pospos=True
                            for i in range(posx-level+1, posx+1):
                                if aifield[posy][i] != 0: 
                                    pospos=False
                        else: pospos=False

                    if pospos:
                        if rotation == 4:
                            for i in range(posx-level+1, posx+1):
                                aifield[posy][i] = level
                                occd.append([i, posy])

                        if rotation == 2:
                            for i in range(posx, posx+level):
                                aifield[posy][i] = level
                                occd.append([i, posy])

                        if rotation == 3:
                            for i in range(posy, posy+level):
                                aifield[i][posx] = level
                                occd.append([posx, i])

                        if rotation == 1:
                            for i in range(posy-level+1, posy+1):
                                aifield[i][posx] = level
                                occd.append([posx, i])
                        posship = True
                    else: 
                        if len(imposrot) == 4:
                            posx = random.randint(0, size-1)
                            posy = random.randint(0, size-1)
                            pos = [posx, posy]
                            while pos in occd:
                                posx = random.randint(0, size-1)
                                posy = random.randint(0, size-1)
                                pos = [posx, posy]
                            occd.append(pos)
                            imposrot = []
            else:
                aifield[posy][posx] = 1
                posship = True
            posship = False
        level-=1
    print("")
    print("������������.")
    return aifield

def step(px, py):
    if aifield[py][px] == 0:
        print("������ �����. ")
    else:
        aifield[py][px] = 0
        shipsnear = False
        for i in range(py-1, py+1):
            for j in range(px-1, px+2):
                if (i>=0 and i < fieldsize) and (j>=0 and j < fieldsize): 
                    if aifield[i][j] == 0: shipsnear = True
        if shipsnear: print("�����")
        else: print("����")
    print("")
    print("��� ��")
    px = random.randint(0, fieldsize-1)
    py = random.randint(0, fieldsize-1)
    crd = [px, py]
    while crd in crds:
        px = random.randint(0, fieldsize-1)
        py = random.randint(0, fieldsize-1)
        crd = [px, py]
    crds.append(crd)
    if field[py][px] == 0: 
        print("�� �� ����� (" + str(px) + ", " + str(py) + ")")
    else: 
        print("�� ����� (" + str(px) + ", " + str(py) + ")")
        field[py][px] = 0
        for i in range(fieldsize):
            print(field[i])




fieldsize = iin("������� ������ �������� ����: ")
level = iin("�������: ") # ��� ������ 1 ����� 1 ������������ �������, ��� ������ 3 ����� 1 ������������, 2 ������������, 3 ������������ � �. �.
tlevel = level

templist = [0 for i in range(fieldsize)]

field = generatefield(fieldsize, level)
aifield = generateaifield(fieldsize, level)

print("���� ����: ")
printfield(field)
print()
printfield(aifield)



crds = []
while not(victory(field)) and not(victory(aifield)):

    print("")
    print("��� ������ ")
    crdx = iin("X: ")
    crdy = iin("Y: ")
    step(crdx, crdy)
    



if victory(aifield) and victory(field): print("�����")
elif victory(field): print("����� ��������")
elif victory(aifield): print("����� �������")