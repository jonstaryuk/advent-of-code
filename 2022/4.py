from sys import stdin

# 1

acc = 0
for line in stdin:
    a, b, c, d = [int(s) for s in line.strip().replace(',', '-').split('-')]
    if a <= c and d <= b or c <= a and b <= d:
        acc += 1

print(acc)


# 2

acc = 0
for line in stdin:
    a, b, c, d = [int(s) for s in line.strip().replace(',', '-').split('-')]
    if a < d and b >= c or c < b and d >= a:
        acc += 1

print(acc)
