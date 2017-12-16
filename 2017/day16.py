from itertools import count
from sys import stdin


p = [chr(x) for x in range(ord('a'), ord('p') + 1)]
moves = stdin.read().strip().split(',')


def dance():
    global p

    for move in moves:
        if move[0] == 's':
            n = int(move[1:])
            p = p[-n:] + p[:-n]
        else:
            if move[0] == 'x':
                a, b = [int(x) for x in move[1:].split('/')]
            elif move[0] == 'p':
                a, b = [p.index(x) for x in move[1:].split('/')]
            z = p[a]
            p[a] = p[b]
            p[b] = z


dance()
print(''.join(p))

p.sort()
known = {}
for i in count():
    if tuple(p) in known:
        inverted = {v: k for k, v in known.items()}
        print(''.join(inverted[1000000000 % i]))
        break

    known[tuple(p)] = i

    dance()
