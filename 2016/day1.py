NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


def block_distance(x, y=None):
    if type(x) == tuple:
        return abs(x[0]) + abs(x[1])
    return abs(x) + abs(y)


def parse_moves(moves):
    x, y = 0, 0
    face = NORTH
    grid = [[0 for i in range(2000)] for i in range(2000)]
    spot_visited_twice = None

    for move in moves:
        if move[0] == 'L':
            face -= 1
            if face == -1:
                face = 3
        else:
            assert move[0] == 'R'
            face = (face + 1) % 4

        steps = int(move[1:])

        dx, dy = 0, 0
        if face == NORTH:
            dy = 1
        elif face == SOUTH:
            dy = -1
        elif face == EAST:
            dx = 1
        else:
            assert face == WEST
            dx = -1

        for i in range(steps):
            x += dx
            y += dy
            grid[x][y] += 1
            if spot_visited_twice is None and grid[x][y] > 1:
                spot_visited_twice = (x, y)

    return (block_distance(x, y), block_distance(spot_visited_twice))


if __name__ == '__main__':
    with open("day1.in", "r") as f:
        raw = f.read()
    moves = raw.split(", ")

    print(parse_moves(moves))
