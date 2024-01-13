def new_grid():
    light_grid = []
    for i in range(1000):
        light_grid.append([0 for j in range(1000)])
    return light_grid


def turn_on(p1, p2, grid):
    for y in range(p1[1], p2[1] + 1):
        for x in range(p1[0], p2[0] + 1):
            grid[y][x] = 1


def turn_off(p1, p2, grid):
    for y in range(p1[1], p2[1] + 1):
        for x in range(p1[0], p2[0] + 1):
            grid[y][x] = 0


def toggle(p1, p2, grid):
    for y in range(p1[1], p2[1] + 1):
        for x in range(p1[0], p2[0] + 1):
            if grid[y][x] == 0:
                grid[y][x] = 1
            else:
                grid[y][x] = 0


def parse_instruction(instruction, grid):
    words = instruction.split(' ')
    p2 = [int(num) for num in words[-1].split(',')]
    p1 = [int(num) for num in words[-3].split(',')]
    if words[0] == 'toggle':
        toggle(p1, p2, grid)
    elif words[1] == 'on':
        turn_on(p1, p2, grid)
    elif words[1] == 'off':
        turn_off(p1, p2, grid)


def count_lights(grid):
    count = 0
    for line in grid:
        for light in line:
            if light == 1:
                count += 1
    return count

if __name__ == '__main__':
    f = open('in6', 'r')
    grid = new_grid()
    for line in f:
        parse_instruction(line, grid)
    print count_lights(grid)
