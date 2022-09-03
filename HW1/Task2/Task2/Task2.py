#  !(x or y or z) == (!x and !y and !z)

x = bool(input("Enter X: "))
y = bool(input("Enter Y: "))
z = bool(input("Enter Z: "))

if not(x or y or z) == (not x and not y and not z):
    print("True")
else:
    print("False")