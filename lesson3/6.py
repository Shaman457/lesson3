import math
x = float(input())
p=math.pi
if 0<=x and x<2:
    y = x*math.sqrt(abs(x-5.4))
    print(y)
elif 2<=x and x<8:
    y1=math.atan(x)
    print(y1)
else:
    y = math.log(abs(x-7.8))
    print(y)