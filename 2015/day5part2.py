def contains_repeated_letter_pairs(string):
    has_one = False
    pairs = []
    for i in range(len(string) - 1):
        pairs.append([string[i] + string[i + 1], i, i + 1])
    for pair1 in pairs:
        for pair2 in pairs:
            if pair1[0] == pair2[0] and \
               pair1[1] not in [pair2[1], pair2[2]] and \
               pair1[2] not in [pair2[1], pair2[2]]:
                return True
    return False


def contains_sandwich(string):
    for i in range(len(string) - 3):
        if string[i] == string[i + 2]:
            return True


def is_nice(string):
    return contains_repeated_letter_pairs(string) and contains_sandwich(string)


if __name__ == '__main__':
    f = open('in5', 'r')

    nice_lines = 0
    for line in f:
        if is_nice(line):
            nice_lines += 1

    print "Nice lines:", nice_lines
