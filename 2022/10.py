raw = open('10.in').read()
lines = raw.rstrip().split('\n')

c = 0
x = 1
acc = 0
crt = ["." for _ in range(240)]


def cycle():
    global c, x, acc, crt
    if c == 20 or (c - 20) % 40 == 0:
        acc += c * x
    crt[c-1] = "#" if (c-1) % 40 in (x-1, x, x+1) else "."


for line in lines:
    c += 1
    cycle()
    if line.startswith("addx"):
        c += 1
        cycle()
        _, v = line.split()
        x += int(v)

print(acc)

for i in range(0, 240, 40):
    print("".join(crt[i:i+40]))
