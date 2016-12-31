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


def parse_room(entry):
    return room_regex.match(entry)


def contribution(match):
    room = match.group(1)
    sector_id = match.group(2)
    checksum = match.group(3)

    if checksum == checksum_from_histogram(letter_histogram(room)):
        return int(sector_id)
    else:
        return 0


def shift(char, amount):
    if char == '-':
        return char
    n = ord(char) - ord('a')
    n = (n + amount) % 26
    return chr(n + ord('a'))


def decrypt_name(match):
    ciph = match.group(1)
    shift_amount = int(match.group(2))
    return ''.join([shift(c, shift_amount) for c in ciph])


if __name__ == '__main__':
    with open("day4.in") as f:
        lines = f.read().split('\n')

    if lines[-1] == "":
        lines = lines[:-1]

    total = 0

    for line in lines:
        match = parse_room(line)
        total += contribution(match)
        if decrypt_name(match) == "northpole-object-storage":
            print("North Pole room sector ID:", match.group(2))

    print("Total:", total)

