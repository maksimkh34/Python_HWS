xp1 = int(input("Enter x(point 1): "))
yp1 = int(input("Enter y(point 1): "))

xp2 = int(input("Enter x(point 2): "))
yp2 = int(input("Enter y(point 2): "))

pointeqs = False

if xp1>xp2:
    bigx = xp1
    smx = xp2
elif xp1<xp2:
    bigx = xp2;
    smx = xp1
elif xp1==xp2:
   pointeqs = True
   if yp1>yp2: 
       dist = yp1-yp2
   elif yp1<yp2: 
       dist = yp2-yp1
   elif yp2==yp1: 
       bigx = 0
       smx = 0

if yp1>yp2:
    bigy = yp1
    smy = yp2
elif yp1<yp2:
    bigy = yp2;
    smy = yp1
elif yp1==yp2:
    dist = bigx - smx
    pointeqs = True

if pointeqs==False:
    xside = bigx - smx
    yside = bigy - smy
    dist = (xside ** 2 + yside ** 2) ** 0.5

print(f"Distance between points is: {round(dist, 2)}")


