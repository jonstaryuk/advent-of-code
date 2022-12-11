raw = open('11.in').read()
lines = raw.rstrip().split('\n')

monkeys = {}

for i, line in enumerate(lines + [""]):
    if i % 7 == 0:
        m = int(line[7:].rstrip(":"))
    elif i % 7 == 1:
        items = list(map(int, line.split(": ")[1].split(", ")))
    elif i % 7 == 2:
        op = line.split("= ")[1]
    elif i % 7 == 3:
        divisor = int(line.split("by ")[1])
    elif i % 7 == 4:
        true_dest = int(line.split()[-1])
    elif i % 7 == 5:
        false_dest = int(line.split()[-1])
    elif i % 7 == 6:
        monkeys[m] = [
            [{1: item} for item in items],
            op,
            divisor,
            true_dest,
            false_dest,
            0,
        ]

divisors = {data[2] for data in monkeys.values()}
for data in monkeys.values():
    for item in data[0]:
        for d in divisors:
            item[d] = item[1] % d


def turn(m):
    global monkeys
    items, op, divisor, true_dest, false_dest, inspect_count = monkeys[m]
    for item in items:
        for d in divisors:
            old = item[d]  # local var used in eval
            item[d] = eval(op) % d
        if item[divisor] == 0:
            monkeys[true_dest][0].append(item)
        else:
            monkeys[false_dest][0].append(item)
        monkeys[m][-1] += 1
    monkeys[m][0] = []


def run(n_rounds):
    for round in range(n_rounds):
        for m in range(len(monkeys)):
            turn(m)


run(10000)

# print(*[(m, data[-1]) for m, data in monkeys.items()], sep="\n")
top = sorted(data[-1] for data in monkeys.values())[-2:]
print(top, top[0] * top[1])
