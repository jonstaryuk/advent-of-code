from sys import stdin


n = int(stdin.read().strip())

buf = [0]
pos = 0
for val in range(1, 2017 + 1):
    pos = (pos + n + 1) % val
    buf.insert(pos, val)

print(buf[buf.index(2017) + 1])

pos = 0
for val in range(1, 50000000 + 1):
    pos = (pos + n + 1) % val
    if pos == 0:
        answer = val

print(answer)
