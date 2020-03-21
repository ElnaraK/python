def xor(x, y):
    if x == y:
        return 0
    else:
        return 1

nums = list(map(int, input().split(maxsplit=2)))
print(int(xor(nums[0], nums[1])))