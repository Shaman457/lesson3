import math
x = float(input())
# p=math.pi
if x>(-math.pi) and x<math.pi/4:
    d = pow(math.cos(x-math.pi), 2)
    y = -1*d
    print(y)
elif x >= math.pi/4 and x<=1:
    y = math.sqrt(abs(x+1))
    print(y)
elif x>1:
    y = 1/(x-1)
    print(y)
else:
    print("EROR")