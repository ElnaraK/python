def reverse3(nums):
    for i in range(len(nums)//2):
        c = nums[i]
        nums[i] = nums[len(nums)-1-i]
        nums[len(nums)-1-i] = c
    return nums