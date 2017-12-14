from itertools import count
from sys import stdin


def run(layers, scanners, delay=0):
    last = max(layers.keys())

    pos = -delay
    while pos <= last:
        for l in range(last + 1):
            s, forward = scanners[l]
            r = layers[l]

            if pos == l and s == 1:
                yield l * layers[l]

            if forward and r != 0:
                s += 1
                if s >= r:
                    forward = False
            elif r != 0:
                s -= 1
                if s <= 1:
                    forward = True

            scanners[l] = (s, forward)

        pos += 1


def solve(lines):
    info = [line.split(': ') for line in lines]
    layers = {int(l): int(r) for l, r in info}
    last = max(layers.keys())
    layers.update({i: 0 for i in range(last) if i not in layers})

    scanners = {l: (int(layers[l] != 0), True) for l in layers.keys()}
    print(sum(run(layers, scanners)))

    for delay in count():
        scanners = {l: (int(layers[l] != 0), True) for l in layers.keys()}
        runner = run(layers, scanners, delay)
        try:
            next(runner)
        except StopIteration:
            print(delay)
            exit(0)


if __name__ == '__main__':
    solve(stdin.readlines())
