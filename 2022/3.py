from collections import Counter
from sys import stdin

# 1

acc = 0
for line in stdin:
    items = list(line.strip())
    left, right = items[:len(items)//2], items[len(items)//2:]
    t = next(x for x in left if x in right)
    if t.lower() == t:
        acc += ord(t) - ord('a') + 1
    else:
        acc += ord(t) - ord('A') + 27

print(acc)


# 2

acc = 0
g = []
for i, line in enumerate(stdin):
    g.append(line.strip())
    if i % 3 == 2:
        for x in g[0]:
            if x in g[1] and x in g[2]:
                t = x
                break
        if t.lower() == t:
            acc += ord(t) - ord('a') + 1
        else:
            acc += ord(t) - ord('A') + 27
        g = []


print(acc)
