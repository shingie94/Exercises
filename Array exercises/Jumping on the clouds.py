def jumpingOnClouds(c):
    current = 0
    end = len(c) - 1
    jumps = 0

    while current < end:
        if ((current + 2) <= end) and (c[current + 2] == 0):
            current += 2
            jumps += 1
        elif c[current + 1] == 0:
            current += 1
            jumps += 1

    return jumps
