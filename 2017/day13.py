from itertools import count
from sys import stdin


data = (line.split(': ') for line in stdin.readlines())
layers = {int(d[0]): int(d[1]) for d in data}


def scanner_position(t, l):
    if l not in layers:
        return -1

    height = layers[l]
    span = height * 2 - 2
    offset = t % span
    return (offset if offset < height else span - offset) + 1


def journey(delay=0):
    for t in range(max(layers) + 1):
        yield scanner_position(t + delay, t)


print(sum(l * layers[l] for l, pos in enumerate(journey()) if pos == 1))

for delay in count():
    if not any(pos == 1 for pos in journey(delay)):
        print(delay)
        break
