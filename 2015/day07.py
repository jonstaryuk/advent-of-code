from sys import stdin


def compute(formulas, k):
    f = formulas[k]

    if type(f) is int:
        return f
    elif len(f) == 1:
        src = f[0]
        result = (int(src) if src.isnumeric() else compute(formulas, src)) & 0xffff
    elif len(f) == 2:
        src = f[1]
        result = ~(compute(formulas, src) & 0xffff) & 0xffff
    else:
        a, op, b = f
        a = int(a) if a.isnumeric() else compute(formulas, a)
        b = int(b) if b.isnumeric() else compute(formulas, b)
        a, b = a & 0xffff, b & 0xffff

        if op == 'AND':
            result = a & b
        elif op == 'OR':
            result = a | b
        elif op == 'LSHIFT':
            result = a << b
        elif op == 'RSHIFT':
            result = a >> b
        else:
            raise ValueError(op)

    assert type(result) is int
    formulas[k] = result
    return result


def read(lines):
    formulas = {}

    for line in lines:
        l = line.split()
        dest = l[-1]
        formulas[dest] = l[:-2]

    return formulas


def solve(lines):
    formulas = read(lines)
    return compute(formulas, "a")


def solve2(lines):
    formulas = read(lines)
    a = compute(formulas, "a")
    formulas = read(lines)
    formulas["b"] = a
    return compute(formulas, "a")


if __name__ == '__main__':
    lines = stdin.readlines()
    print(solve2(lines))
