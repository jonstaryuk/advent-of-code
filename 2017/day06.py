from sys import stdin


def snapshot(m):
    return '-'.join([str(x) for x in m])


def solve(m):
    m = [int(x) for x in m]
    seen = set(snapshot(m))
    rounds = 0

    while True:
        val = max(m)
        i = m.index(val)
        m[i] = 0
        while val > 0:
            i = (i + 1) % len(m)
            m[i] += 1
            val -= 1

        rounds += 1
        oldlen = len(seen)
        seen.add(snapshot(m))
        if len(seen) == oldlen:
            return (rounds, m)


def solve2(m):
    _, m = solve(m)
    start = snapshot(m)
    rounds = 0

    while True:
        val = max(m)
        i = m.index(val)
        m[i] = 0
        while val > 0:
            i = (i + 1) % len(m)
            m[i] += 1
            val -= 1

        rounds += 1
        if snapshot(m) == start:
            return rounds


if __name__ == '__main__':
    m = stdin.read().strip().split()
    print(solve2(m))
