from sys import stdin


def gen(n, x, fac, crit):
    i = 0
    while i < n:
        x *= fac
        x %= 2147483647
        if crit is None or x % crit == 0:
            yield x & 0xFFFF
            i += 1


F1, F2 = 16807, 48271
start1, start2 = [int(line.split()[-1]) for line in stdin.readlines()]

stream = zip(gen(40000000, start1, F1, None), gen(40000000, start2, F2, None))
print(sum(1 for a, b in stream if a == b))

stream = zip(gen(5000000, start1, F1, 4), gen(5000000, start2, F2, 8))
print(sum(1 for a, b in stream if a == b))
