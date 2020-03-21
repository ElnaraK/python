def sum67(nums):
    bool = True
    s = 0
    for n in nums:
        if n == 6:
            bool = False
        if bool:
            s += n
            continue
        if n == 7:
            bool = True
    return s