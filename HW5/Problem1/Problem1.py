# -*- coding: cp1251 -*-
# Игра писалась без учета того что ее будут ломать, так что никаких проверок вводных данных нет
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
           posx = iin("Введите X (0 - " + str(size-1) + ") для коробля с " + str(level) + " палубами: ")
           posy = iin("Введите X (0 - " + str(size-1) + ") для коробля с " + str(level) + " палубами: ")
           if level!=1:
               rotation = iin("Поворот корабля (1 - up, 2 - right, 3 - down, 4 - left): ")
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
    print("Генерация поля ИИ...")
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
    print("Сгенерирвано.")
    return aifield

def step(px, py):
    if aifield[py][px] == 0:
        print("Клетка пуста. ")
    else:
        aifield[py][px] = 0
        shipsnear = False
        for i in range(py-1, py+1):
            for j in range(px-1, px+2):
                if (i>=0 and i < fieldsize) and (j>=0 and j < fieldsize): 
                    if aifield[i][j] == 0: shipsnear = True
        if shipsnear: print("Ранен")
        else: print("Убит")
    print("")
    print("Ход ИИ")
    px = random.randint(0, fieldsize-1)
    py = random.randint(0, fieldsize-1)
    crd = [px, py]
    while crd in crds:
        px = random.randint(0, fieldsize-1)
        py = random.randint(0, fieldsize-1)
        crd = [px, py]
    crds.append(crd)
    if field[py][px] == 0: 
        print("ИИ не попал (" + str(px) + ", " + str(py) + ")")
    else: 
        print("ИИ попал (" + str(px) + ", " + str(py) + ")")
        field[py][px] = 0
        for i in range(fieldsize):
            print(field[i])




fieldsize = iin("Введите размер игрового поля: ")
level = iin("Уровень: ") # Для уровня 1 будет 1 однопалубный корабль, для уровня 3 будет 1 трехпалубный, 2 двухпалубных, 3 однопалубных и т. д.
tlevel = level

templist = [0 for i in range(fieldsize)]

field = generatefield(fieldsize, level)
aifield = generateaifield(fieldsize, level)

print("Ваше поле: ")
printfield(field)
print()
printfield(aifield)



crds = []
while not(victory(field)) and not(victory(aifield)):

    print("")
    print("Ход игрока ")
    crdx = iin("X: ")
    crdy = iin("Y: ")
    step(crdx, crdy)
    



if victory(aifield) and victory(field): print("Ничья")
elif victory(field): print("Игрок проиграл")
elif victory(aifield): print("Игрок выиграл")