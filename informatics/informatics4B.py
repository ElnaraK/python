N = int(input())
nums = list(map(int, input().split(maxsplit=N)))
for i in range(0, N):
    if nums[i] % 2 == 0:
        print(nums[i])