from functools import reduce
from sys import stdin


def run(s, lengths, i, skip):
    for length in lengths:
        end = min(i + length, len(s))
        sublist = s[i:end]
        l1 = len(sublist)

        extra = (i + length) - (len(s))
        if extra > 0:
            sublist += s[:extra]
            l2 = len(s[:extra])
        sublist.reverse()

        s[i:end] = sublist[:l1]
        if extra > 0:
            s[:extra] = sublist[l1:l1 + l2]

        i = (i + length + skip) % len(s)
        skip += 1

    return i, skip


def solve(input_):
    lengths = [int(x) for x in input_.split(',')]
    s = [x for x in range(256)]

    run(s, lengths, 0, 0)

    return s[0] * s[1]


def solve2(input_):
    lengths = [ord(x) for x in input_] + [17, 31, 73, 47, 23]
    s = [x for x in range(256)]
    i, skip = 0, 0

    for _ in range(64):
        i, skip = run(s, lengths, i, skip)

    blocks = [s[i:i + 16] for i in range(0, len(s), 16)]
    dense = [reduce(lambda x, y: x ^ y, block) for block in blocks]
    return bytes(dense).hex()


if __name__ == '__main__':
    print(solve2(stdin.read().strip()))
