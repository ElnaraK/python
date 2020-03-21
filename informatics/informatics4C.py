N = int(input())
c = 0
nums = list(map(int, input().split(maxsplit=N)))
for i in range(0, N):
    if nums[i] > 0:
        c = c+1
print(c)