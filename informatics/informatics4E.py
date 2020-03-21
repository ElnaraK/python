N = int(input())
nums = list(map(int, input().split(maxsplit=N)))
for i in range(0, N-1):
    if nums[i+1] > 0 and nums[i] > 0:
        print("YES")
        break
    elif nums[i+1] < 0 and nums[i] < 0:
        print("YES")
        break
    elif i == N-2:
        print("NO")