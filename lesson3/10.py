import math
x = int(input())
p = math.pi
if abs(x)<2:
    y = x-pow(math.e, x)
elif x<=-2:
    y = math.log(x**2)
elif x>=2:
    y = pow(math.sin(x), 2)
else:
    print("EROR")
print(y)