def make_chocolate(small, big, goal):
    c = goal-big*5
    if 5*big<=goal:
        if c<=small:
            return c
        elif c>small:
            return -1
    else:
        k = goal-(goal//5*5)
        if k<=small:
            return k
        elif k>small:
            return -1
