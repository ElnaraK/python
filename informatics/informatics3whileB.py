N = int(input())
x = 2
while x <= N:
    if N % x == 0:
        print(x)
        break
    x = x + 1
