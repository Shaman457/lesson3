import math
x = float(input())
p=math.pi
if 1<x and x<3.2:
    y= -1*((1.4+x)/math.log(x))
    print(y)
elif 0<x and x<=1:
    y = x**2-0.75
    print(y)
elif x<=0:
    y1 = pow(math.cos(x**2), 3)
    y2 = pow(math.sin(x**2), 3)
    y = y1 - y2
    print(y)
else:
    print("EROR")