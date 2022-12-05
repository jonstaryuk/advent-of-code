from sys import stdin
from itertools import zip_longest

lines = stdin.readlines()


# 1

bound = lines.index('\n')

stacks = list(zip_longest(*lines[:bound-1], fillvalue=""))
stacks = [[x for x in l if x.isalpha()] for l in stacks]
stacks = [list(reversed(x)) for x in stacks if len(x) > 0]

instructions = [[int(s) for s in l.split() if s.isnumeric()]
                for l in lines[bound+1:]]

for n_move, src, dst in instructions:
    for _ in range(n_move):
        c = stacks[src-1].pop()
        stacks[dst-1].append(c)

print("".join([s[-1] for s in stacks]))


# 2

bound = lines.index('\n')

stacks = list(zip_longest(*lines[:bound-1], fillvalue=""))
stacks = [[x for x in l if x.isalpha()] for l in stacks]
stacks = [list(reversed(x)) for x in stacks if len(x) > 0]

instructions = [[int(s) for s in l.split() if s.isnumeric()]
                for l in lines[bound+1:]]

for n_move, src, dst in instructions:
    cs = stacks[src-1][-n_move:]
    stacks[src-1] = stacks[src-1][:-n_move]
    stacks[dst-1] += cs

print("".join([s[-1] for s in stacks]))
