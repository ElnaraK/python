N = int(input())
nums = list(map(int, input().split(maxsplit=N)))
for i in range(0, N//2):
    c = nums[i]
    nums[i] = nums[N-i-1]
    nums[N-i-1] = c

for i in range(0, N):
    print(nums[i])