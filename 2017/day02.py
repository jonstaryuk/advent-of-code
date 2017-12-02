from itertools import permutations
from sys import stdin


def solve(lines):
    return sum(max(line) - min(line) for line in lines)


def solve2(lines):
    return sum(x // y for line in lines for x, y in permutations(line, 2) if x % y == 0)


if __name__ == '__main__':
    lines = [[int(x) for x in line.split()] for line in stdin.readlines()]
    print(solve2(lines))
