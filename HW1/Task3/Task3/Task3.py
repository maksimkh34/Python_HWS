X = int(input("Enter X: "))
Y = int(input("Enter Y: "))

if X>0:
    if Y>0:
        print("Answer is: 1")
    elif Y<0:
        print("Answer is: 4")
    elif Y==0:
        print("err")
elif X<0:
    if Y>0:
        print("Answer is: 2")
    elif Y<0:
        print("Answer is: 3")
    elif Y==0:
        print("err")
elif X==0:
        print("err")
