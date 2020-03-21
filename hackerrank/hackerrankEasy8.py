n = int(input())
A = list(map(int, input().split(maxsplit=n)))
c = max(A)
while max(A) == c:
    A.remove(c)
print(max(A))