def make_bricks(small, big, goal):
    b = min(big, goal // 5)
    return goal - (b * 5) <= small