import math
x = int(input())
p = math.pi
if 1<=x:
    y = pow(math.e, -1*abs(x))
elif abs(x)<1:
    y = math.log(math.sqrt(1-x**2))
elif x<=-1:
    y = math.artan(x)
else:
    print("EROR")
print(y)