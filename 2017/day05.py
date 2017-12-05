from sys import stdin


def solve(inst):
    steps = 0
    i = 0

    while True:
        try:
            offset = inst[i]
        except IndexError:
            return steps

        inst[i] += 1
        i += offset
        steps += 1


def solve2(inst):
    steps = 0
    i = 0

    while True:
        try:
            offset = inst[i]
        except IndexError:
            return steps

        inst[i] += 1 if offset < 3 else -1
        i += offset
        steps += 1


if __name__ == '__main__':
    inst = [int(x) for x in stdin.readlines()]
    print(solve2(inst))
