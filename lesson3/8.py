import math
y = int(input())
x = int(input())
p = math.pi
if abs(x*y)<1 or x<0:
    z = (x+y)/pow(math.e, x*y)
elif 2<x or y<=0:
    z = -1*pow(math.log(x), 2)
elif 0<y or 0<=x and x<=2:
    z = math.log(math.sqrt(y))
else:
    print("EROR")
print(z)