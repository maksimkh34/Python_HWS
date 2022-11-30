text = input()

wpoint = False
isdig = True

for i in range(len(text)):
    if(text[i].isdigit() == False):
        if(text[i]=='.' and not(wpoint)): wpoint = True
        else: isdig = False

print(isdig)