def lucky_sum(a, b, c):
    s = 0
    for i in (a, b, c):
        if i != 13:
            s += i
        else:
            break

    return s