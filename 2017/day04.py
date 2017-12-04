from sys import stdin


def solve(lines):
    return len(list(line for line in lines if len(set(line.split())) == len(line.split())))


def solve2(lines):
    lines = [[''.join(sorted(word)) for word in line.split()] for line in lines]
    return len(list(line for line in lines if len(set(line)) == len(line)))


if __name__ == '__main__':
    lines = stdin.readlines()
    print(solve2(lines))
