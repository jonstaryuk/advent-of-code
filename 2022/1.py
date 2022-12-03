from sys import stdin

totals = []
acc = 0
for line in stdin:
    line = line.strip()
    if line == '':
        totals.append(acc)
        acc = 0
    else:
        acc += int(line)

print(list(sorted(totals)))
