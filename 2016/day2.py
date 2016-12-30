NUMBER_GRID = [[0, 0, 0, 0, 0],
               [0, 1, 2, 3, 0],
               [0, 4, 5, 6, 0],
               [0, 7, 8, 9, 0],
               [0, 0, 0, 0, 0]]

HEX_GRID = [[0, 0,  0,  0,  0, 0, 0],
            [0, 0,  0,  1,  0, 0, 0],
            [0, 0,  2,  3,  4, 0, 0],
            [0, 5,  6,  7,  8, 9, 0],
            [0, 0, 10, 11, 12, 0, 0],
            [0, 0,  0, 13,  0, 0, 0],
            [0, 0,  0,  0,  0, 0, 0]]


def deltas(direction):
    dx, dy = 0, 0

    if direction == 'U':
        dy = -1
    elif direction == 'D':
        dy = 1
    elif direction == 'R':
        dx = 1
    elif direction == 'L':
        dx = -1
    else:
        raise RuntimeError("Unknown direction " + direction)

    return (dx, dy)


def parse(lines, starting_coordinates, grid=NUMBER_GRID):
    row, col = starting_coordinates

    for line in lines:
        for c in line:
            dx, dy = deltas(c)

            try:
                row += dy
                col += dx
            except IndexError:
                continue

            if grid[row][col] == 0:
                row -= dy
                col -= dx


        yield grid[row][col]


if __name__ == '__main__':
    with open("day2.in") as f:
        raw = f.read()
    lines = raw.split('\n')

    if lines[-1] == "":
        lines = lines[:-1]

    for n in parse(lines, (2, 2), NUMBER_GRID):
        print(n)

    print()

    for n in parse(lines, (3, 1), HEX_GRID):
        print(n)
