from sys import stdin


def solve(lines):
    reg = {}
    max_value = 0

    for line in lines:
        inst = line.split()

        r = inst[0]

        amount = int(inst[2])
        if inst[1] == 'dec':
            amount = -amount

        a = reg.get(inst[4], 0)
        op = inst[5]
        b = int(inst[6])

        satisfied = (
            op == '>' and a > b or
            op == '>=' and a >= b or
            op == '<' and a < b or
            op == '<=' and a <= b or
            op == '==' and a == b or
            op == '!=' and a != b
        )

        if satisfied:
            reg[r] = reg.get(r, 0) + amount

        if reg.get(r, 0) > max_value:
            max_value = reg[r]

    print(max(reg.values()))
    print(max_value)


if __name__ == '__main__':
    solve(stdin.readlines())
