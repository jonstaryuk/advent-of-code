from sys import stdin


def solve(s):
    total = 0

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            total += int(s[i])
    if s[0] == s[-1]:
        total += int(s[0])

    return total


def solve_halfway(s):
    total = 0
    n = len(s)
    half = n // 2

    for i in range(n - 1):
        if s[i] == s[(i + half) % n]:
            total += int(s[i])

    if s[-1] == s[half - 1]:
        total += int(s[-1])

    return total


def test():
    assert solve('1122') == 3
    assert solve('1111') == 4
    assert solve('1234') == 0
    assert solve('91212129') == 9

    assert solve_halfway('1212') == 6


if __name__ == '__main__':
    # test()
    s = stdin.read().strip()
    print(solve_halfway(s))
