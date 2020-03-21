def string_match(a, b):
    shorter = min(len(a), len(b))
    count = 0

    for i in range(shorter - 1):
        substr_a = a[i:i + 2]
        substr_b = b[i:i + 2]
        if substr_a == substr_b:
            count = count + 1

    return count