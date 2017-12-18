from collections import deque
from itertools import zip_longest
from sys import stdin


insts = [line.split() for line in stdin.readlines()]


# Part 1

reg = {}


def value(x):
    try:
        return int(x)
    except ValueError:
        return reg.get(x, 0)


i = 0
while 0 <= i < len(insts):
    inst = insts[i]
    op = inst[0]

    if op == 'snd':
        sound = value(inst[1])
    elif op == 'set':
        reg[inst[1]] = value(inst[2])
    elif op == 'add':
        reg[inst[1]] = value(inst[1]) + value(inst[2])
    elif op == 'mul':
        reg[inst[1]] = value(inst[1]) * value(inst[2])
    elif op == 'mod':
        reg[inst[1]] = value(inst[1]) % value(inst[2])
    elif op == 'rcv':
        if value(inst[1]) != 0:
            print(sound)
            break
    elif op == 'jgz':
        if value(inst[1]) > 0:
            i += int(inst[2])
            continue

    i += 1


# Part 2

registers = [{'p': 0}, {'p': 1}]
queue = [deque(), deque()]
sent = [0, 0]
done = [False, False]


def run(p):
    reg = registers[p]

    def value(x):
        try:
            return int(x)
        except ValueError:
            return reg.get(x, 0)

    i = 0
    while 0 <= i < len(insts):
        inst = insts[i]
        op = inst[0]

        if op == 'set':
            reg[inst[1]] = value(inst[2])
        elif op == 'add':
            reg[inst[1]] = value(inst[1]) + value(inst[2])
        elif op == 'mul':
            reg[inst[1]] = value(inst[1]) * value(inst[2])
        elif op == 'mod':
            reg[inst[1]] = value(inst[1]) % value(inst[2])
        elif op == 'jgz':
            if value(inst[1]) > 0:
                i += value(inst[2])
                continue
        elif op == 'snd':
            queue[p].append(value(inst[1]))
            sent[p] += 1
        elif op == 'rcv':
            sender = 1 - p
            while len(queue[sender]) == 0:
                done[p] = True
                yield
            reg[inst[1]] = value(queue[sender].popleft())

        i += 1
        done[p] = False
        yield

    done[p] = True


programs = zip_longest(run(0), run(1))
while not all(done):
    next(programs)

print(sent[1])
