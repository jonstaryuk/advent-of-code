from sys import stdin

from day10 import solve2


key = stdin.readline().strip()

inputs = [f'{key}-{i}' for i in range(128)]
hashes = [bytes.fromhex(solve2(s)) for s in inputs]
print(sum(bin(byte).count('1') for s in hashes for byte in s))

n = len(hashes)
used = [[bit == '1' for byte in s for bit in bin(byte)[2:].zfill(8)] for s in hashes]
explored = [[False] * n for _ in range(n)]


def explore(i, j, r):
    explored[i][j] = True

    for k, l in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)):
        if 0 <= k < n and 0 <= l < n and used[k][l] and not explored[k][l]:
            explore(k, l, r)


r = 0
for i in range(n):
    for j in range(n):
        if used[i][j] and not explored[i][j]:
            explore(i, j, r)
            r += 1

print(r)
