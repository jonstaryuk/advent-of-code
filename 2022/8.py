import itertools
from sys import stdin


trees = [[int(x) for x in list(l.strip())] for l in stdin.readlines()]
h, w = len(trees), len(trees[0])
all_trees = list(itertools.product(range(h), range(w)))


def look(pos, dir):
    i, j = pos
    di, dj = dir

    while True:
        i += di
        j += dj
        if not (0 <= i < h and 0 <= j < w):
            break
        yield (i, j)


DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def visible(trees, pos):
    i, j = pos

    if i == 0 or j == 0 or i == h-1 or j == w-1:
        return True

    for dir in DIRECTIONS:
        if all(trees[a][b] < trees[i][j] for a, b in look((i, j), dir)):
            return True
    return False


print(len(set(pos for pos in all_trees if visible(trees, pos))))


def score(trees, pos):
    i, j = pos
    own_height = trees[i][j]

    total = 1
    for dir in DIRECTIONS:
        subtotal = 0
        for a, b in look(pos, dir):
            subtotal += 1
            if trees[a][b] >= own_height:
                break
        total *= subtotal

    return total


print(max(score(trees, pos) for pos in all_trees))
