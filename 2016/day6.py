import collections


def most_frequent_item(data):
    return collections.Counter(data).most_common(1)[0][0]


def columnwise_most_common(lines):
    letters = [most_frequent_item(column) for column in zip(*lines)]
    return "".join(letters)


if __name__ == '__main__':
    with open("day6.in") as f:
        lines = f.read().split('\n')
        if lines[-1] == "":
            lines = lines[:-1]
    print(columnwise_most_common(lines))
