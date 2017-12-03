from sys import stdin


def solve(num):
    # Find the ring that contains the number in sub-linear time
    width = 1
    while True:
        width += 2
        ring_max = width ** 2

        if ring_max > num:
            break

    # Get the positions of the ring's corners
    x, y = width // 2, -(width // 2)
    bl = -x, y
    tl = -x, -y
    tr = x, -y
    move = (-1, 0)

    # Go backwards around the ring to reach the number
    for _ in range(ring_max - num):
        x += move[0]
        y += move[1]

        if (x, y) == bl:
            move = (0, 1)
        elif (x, y) == tl:
            move = (1, 0)
        elif (x, y) == tr:
            move = (0, -1)

    return abs(x) + abs(y)


def fill_surrounding_sum(S, x, y, num):
    surroundings = [
        (x+1, y), (x-1, y),
        (x+1, y+1), (x, y+1), (x-1, y+1),
        (x+1, y-1), (x, y-1), (x-1, y-1),
    ]
    total = sum(S.get((a, b), 0) for a, b in surroundings)
    if total > num:
        print(total)
        exit(0)
    S[(x, y)] = total


def solve2(num):
    S = {(0, 0): 1}
    width = 1
    x, y = 0, 0

    while True:
        width += 2

        # Right
        x += 1
        fill_surrounding_sum(S, x, y, num)

        # Up
        for _ in range(width - 2):
            y += 1
            fill_surrounding_sum(S, x, y, num)

        # Left
        for _ in range(width - 1):
            x -= 1
            fill_surrounding_sum(S, x, y, num)

        # Down
        for _ in range(width - 1):
            y -= 1
            fill_surrounding_sum(S, x, y, num)

        # Right
        for _ in range(width - 1):
            x += 1
            fill_surrounding_sum(S, x, y, num)


if __name__ == '__main__':
    raw = stdin.read().strip()
    print(solve2(int(raw)))
