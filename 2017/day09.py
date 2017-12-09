from sys import stdin


def solve(s):
    score, total, garbage_count = 0, 0, 0
    skip = False
    in_garbage = False

    for c in s:
        if skip:
            skip = False
            continue

        if in_garbage:
            if c == '>':
                in_garbage = False
            elif c == '!':
                skip = True
            else:
                garbage_count += 1
            continue

        elif c == '<':
            in_garbage = True
        elif c == '{':
            score += 1
            total += score
        elif c == '}':
            score -= 1

    print(total)
    print(garbage_count)


if __name__ == '__main__':
    solve(stdin.read())
