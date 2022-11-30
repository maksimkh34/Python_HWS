SYS_DELMTR = 16
num = int(input("Enter number: "))
result = ""
nresult = ""
while num>0:
    op = num%SYS_DELMTR
    if (op>=10):
        if(op==10): result += "a"
        if(op==11): result += "b"
        if(op==12): result += "c"
        if(op==13): result += "d"
        if(op==14): result += "e"
        if(op==15): result += "f"
        if(op==16): result += "g"
    else: result += str(op)
    num = int(num/SYS_DELMTR);

size = len(result)
for i in range(size):
    nresult += result[size-i-1]
print(nresult)
