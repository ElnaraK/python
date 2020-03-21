import math
x = int(input())
c = 0
for i in range(1, int(math.sqrt(x))+1):
    if math.sqrt(x) == int(math.sqrt(x)) and i == math.sqrt(x):
        c = c + 1
    elif x % i == 0:
        c = c + 2
print(c)
