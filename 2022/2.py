from sys import stdin

# 1

SHSC = {'X': 1, 'Y': 2, 'Z': 3}
OCSC = {
    ('A', 'X'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,

    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,

    ('C', 'X'): 6,
    ('C', 'Y'): 0,
    ('C', 'Z'): 3,
}

acc = 0
for line in stdin:
    opps, mine = line.strip().split()
    acc += SHSC[mine] + OCSC[(opps, mine)]

print(acc)


# 2

SHSC = {'X': 1, 'Y': 2, 'Z': 3}
OCSC = {
    ('A', 'X'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,

    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,

    ('C', 'X'): 6,
    ('C', 'Y'): 0,
    ('C', 'Z'): 3,
}
INSTTOSCORE = {'X': 0, 'Y': 3, 'Z': 6}

acc = 0
for line in stdin:
    opps, oc = line.strip().split()
    mine = next(k[1] for k, v in OCSC.items() if k[0]
                == opps and v == INSTTOSCORE[oc])
    acc += SHSC[mine] + OCSC[(opps, mine)]

print(acc)
