import re


room_regex = re.compile("([a-z\-]*)-([0-9]*)\[([a-z]{5})\]")


def letter_histogram(name):
    histogram = {}
    for c in name:
        if c == '-':
            continue
        if c in histogram:
            histogram[c] += 1
        else:
            histogram[c] = 1
    return histogram


def checksum_from_histogram(hist):
    items = list(hist.items())
    items.sort(key=lambda tup: ord(tup[0]))
    items.sort(key=lambda tup: tup[1], reverse=True)
    return "".join([tup[0] for tup in items[:5]])


def contribution(entry):
    match = room_regex.match(entry)
    room = match.group(1)
    sector_id = match.group(2)
    checksum = match.group(3)

    if checksum == checksum_from_histogram(letter_histogram(room)):
        return int(sector_id)
    else:
        return 0


if __name__ == '__main__':
    with open("day4.in") as f:
        lines = f.read().split('\n')

    if lines[-1] == "":
        lines = lines[:-1]

    total = 0

    for line in lines:
        total += contribution(line)

    print(total)

