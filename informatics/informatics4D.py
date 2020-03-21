N = int(input())
c = 0
nums = list(map(int, input().split(maxsplit=N)))
for i in range(0, N-1):
    if nums[i+1] > nums[i]:
        c = c+1
print(c)