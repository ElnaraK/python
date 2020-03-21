nums = list(map(float, input().split(maxsplit=2)))

def power(a,n):
    c = 1
    for i in range(0,int(n)):
        c = c*a
    return c

print(power(nums[0],nums[1]))