from sys import stdin


def dist(x, y):
    return (abs(x) + abs(y) + abs(x + y)) // 2


def solve(steps):
    x, y = 0, 0
    max_dist = 0

    for step in steps:
        if step == 'n':
            y -= 1
        elif step == 'ne':
            y -= 1
            x += 1
        elif step == 'se':
            x += 1
        elif step == 's':
            y += 1
        elif step == 'sw':
            x -= 1
            y += 1
        elif step == 'nw':
            x -= 1

        max_dist = max(max_dist, dist(x, y))

    print(dist(x, y))
    print(max_dist)


if __name__ == '__main__':
    steps = stdin.read().strip().split(',')
    solve(steps)
