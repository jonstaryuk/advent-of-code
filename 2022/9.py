raw = open('9.in').read()
lines = raw.rstrip().split('\n')


DIRS = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0),
}


def follow(head, tail):
    hx, hy = head
    tx, ty = tail

    vx, vy = hx - tx, hy - ty
    if abs(vx) > 1 or abs(vy) > 1:
        if vx == 0 or vy == 0:
            # Horizontal or vertical
            tx += vx // 2
            ty += vy // 2
        elif abs(vx) < abs(vy):
            # Diagonal for vertical
            tx += vx
            ty += vy // 2
        elif abs(vx) > abs(vy):
            # Diagonal for horizontal
            tx += vx // 2
            ty += vy
        else:
            # Diagonal for diagonal (for multiple knots)
            tx += vx // 2
            ty += vy // 2

    return (hx, hy), (tx, ty)


# def debug(knots):
#     print(list(enumerate(knots)))
#     for j in range(6-1, -1, -1):
#         for i in range(6):
#             if (i, j) in knots:
#                 c = knots.index((i, j))
#             else:
#                 c = "."
#             print(c, end="")
#         print("")
#     print("")


def simulate(n_knots):
    knots = [(0, 0) for _ in range(n_knots)]
    tail_visited = set()

    for line in lines:
        dir, steps = line.split()
        for _ in range(int(steps)):
            hx, hy = knots[0]
            dx, dy = DIRS[dir]
            knots[0] = hx + dx, hy + dy
            for k in range(n_knots - 1):
                knots[k], knots[k+1] = follow(knots[k], knots[k+1])
                if k == n_knots - 2:
                    tail_visited.add(knots[k+1])
    return len(tail_visited)


print(simulate(2))
print(simulate(10))
