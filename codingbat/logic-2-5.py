def round_sum(a, b, c):
    s = [int(round(num, -1)) for num in (a, b, c)]
    return sum(s)