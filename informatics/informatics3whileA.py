import math
N = int(input())
x = 1
while x <= N:
    if math.sqrt(x) == int(math.sqrt(x)):
        print(x)
    x = x+1
