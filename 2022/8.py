from sys import stdin
from collections import defaultdict
import itertools


lines = stdin.readlines()

trees = [[int(x) for x in list(l.strip())] for l in lines]

h = len(trees)
w = len(trees[0])
visible = set()
for i in range(h):
    for j in range(w):
        if i == 0 or j == 0 or i == h-1 or j == w-1:
            visible.add((i, j))


def score(y, x):
    print("***", y, x)
    me = trees[y][x]
    down = 0
    for i in range(y+1, h):
        print(i, x)
        if trees[i][x] < me:
            down += 1
            print("yes")
        else:
            down += 1
            break
    up = 0
    for i in range(y-1, -1, -1):
        print(i, x)
        if trees[i][x] < me:
            up += 1
            print("yes")
        else:
            up += 1
            print("breaking because", i, x, "ge", me)
            break

    right = 0
    for j in range(x+1, w):
        print(y, j)
        if trees[y][j] < me:
            right += 1
            print("yes")
        else:
            right += 1
            break

    left = 0
    for j in range(x-1, -1, -1):
        print(y, j)
        if trees[y][j] < me:
            left += 1
            print("yes")
        else:
            left += 1
            break

    return down * up * right * left


# for i in range(h):
#     m = trees[i][0]
#     for j in range(w):
#         if m < trees[i][j]:
#             # print(f"{(i, j)} visible because {trees[i][j]} < {m}")
#             visible.add((i, j))
#         m = max(m, trees[i][j])

#     m = trees[i][-1]
#     for j in range(w-1, -1, -1):
#         if m < trees[i][j]:
#             # print(f"{(i, j)} visible because {trees[i][j]} < {m}")
#             visible.add((i, j))
#         m = max(m, trees[i][j])

# trees = list(zip(*trees))
# print(*trees, sep="\n")
# for i in range(w):
#     m = trees[i][0]
#     for j in range(h):
#         if m < trees[i][j]:
#             # print(f"{(j, i)} visible because {trees[i][j]} < {m}")
#             visible.add((j, i))
#         m = max(m, trees[i][j])

#     m = trees[i][-1]
#     for j in range(h-1, -1, -1):
#         if m < trees[i][j]:
#             # print(f"{(i, j)} visible because {trees[i][j]} < {m}")
#             visible.add((j, i))
#         m = max(m, trees[i][j])

# for i in range(h):
#     for j in range(w):
#         if (i, j) in visible:
#             print('*', end='')
#     print()
print(len(visible))

# print(list(itertools.product(h, w)))
for i in range(h):
    for j in range(w):
        print(score(i, j), end="")
    print()

print(max(score(i, j) for i, j in itertools.product(range(h), range(w))))
