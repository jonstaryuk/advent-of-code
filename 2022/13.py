from functools import cmp_to_key
from itertools import zip_longest

raw = open('13.in').read()
lines = raw.rstrip().split('\n')

pairs = []
for i in range(0, len(lines), 3):
    pairs.append((eval(lines[i]), eval(lines[i+1])))


def compare(a, b):
    if type(a) is int and type(b) is int:
        return a - b

    if type(a) is list and type(b) is list:
        for x, y in zip_longest(a, b):
            if x is None:
                return -1
            if y is None:
                return 1

            cmp = compare(x, y)
            if cmp != 0:
                return cmp

        return 0

    if type(a) is int and type(b) is list:
        return compare([a], b)

    if type(a) is list and type(b) is int:
        return compare(a, [b])


def correct_indices(pairs):
    for i, (a, b) in enumerate(pairs):
        if compare(a, b) < 0:
            yield i + 1


def decoder_key(pairs):
    packets = [packet for pair in pairs for packet in pair]
    packets += [[[2]], [[6]]]
    result = sorted(packets, key=cmp_to_key(compare))
    return (result.index([[2]]) + 1) * (result.index([[6]]) + 1)


print(sum(correct_indices(pairs)))
print(decoder_key(pairs))
