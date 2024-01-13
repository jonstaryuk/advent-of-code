import re
from sys import stdin


def solve(lines):
    total_code, total_string = 0, 0

    for line in lines:
        line = line.rstrip('\n')
        n = len(line)

        total_code += n

        n -= len(re.findall(r'\\\"(?!$)', line))
        n -= len(re.findall(r'\\\\', line))
        n -= len(re.findall(r'\\x[0-9a-fA-F]{2}', line)) * 3
        total_string += n - 2

    return total_code - total_string


def solve2(lines):
    total_orig, total_encoded = 0, 0

    for line in lines:
        line = line.rstrip('\n')
        n = len(line)

        total_orig += n

        n += 2
        n += len(re.findall(r'\"', line))
        n += len(re.findall(r'\\', line))
        total_encoded += n

    return total_encoded - total_orig


if __name__ == '__main__':
    print(solve2(stdin.readlines()))
