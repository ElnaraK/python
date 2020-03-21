def has22(nums):
    if len(nums) < 2:
        return False
    else:
        for i in range(len(nums) - 1):
            if nums[i] == 2 and nums[i + 1] == 2:
                return True
            elif i == len(nums) - 2:
                return False

