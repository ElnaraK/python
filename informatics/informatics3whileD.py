N = int(input())
while N != 0:
    if N == 1:
        print("YES")
        break
    N = N / 2
if N == 0:
    print("NO")
