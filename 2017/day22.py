from sys import stdin


def build_grid(lines):
    initial = [[c == '#' for c in line.strip()] for line in reversed(lines)]
    n = len(initial)
    mid = n // 2

    return {(col - mid, row - mid): initial[row][col] for row in range(n) for col in range(n)}


RIGHT, LEFT = (1, 0), (-1, 0)
UP, DOWN = (0, 1), (0, -1)


def turn(direction):
    global facing

    for _ in range(3 if direction == LEFT else 1):
        if facing == RIGHT:
            facing = DOWN
        elif facing == DOWN:
            facing = LEFT
        elif facing == LEFT:
            facing = UP
        elif facing == UP:
            facing = RIGHT


def burst():
    global x, y

    infected = grid.get((x, y), False)
    turn(RIGHT if infected else LEFT)
    grid[x, y] = not(infected)

    x += facing[0]
    y += facing[1]

    return not(infected)


CLEAN, WEAKENED, INFECTED, FLAGGED = 1, 2, 3, 4


def evolved_burst():
    global x, y

    state = grid.get((x, y), CLEAN)

    if state == CLEAN:
        turn(LEFT)
        state = WEAKENED
    elif state == INFECTED:
        turn(RIGHT)
        state = FLAGGED
    elif state == FLAGGED:
        turn(RIGHT)
        turn(RIGHT)
        state = CLEAN
    elif state == WEAKENED:
        state = INFECTED
    else:
        raise ValueError(state)

    grid[x, y] = state

    x += facing[0]
    y += facing[1]

    return state == INFECTED


original = stdin.readlines()

grid = build_grid(original)
x, y, facing = 0, 0, UP
print(sum(int(burst()) for _ in range(10000)))

grid = {key: INFECTED if value else CLEAN for key, value in build_grid(original).items()}
x, y, facing = 0, 0, UP
print(sum(int(evolved_burst()) for _ in range(10000000)))
