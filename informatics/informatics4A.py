N = int(input())
nums = list(map(int, input().split(maxsplit=N)))
for i in range(0, N, 2):
    print(nums[i], end=' ')