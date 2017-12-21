from sys import stdin


def read_image(rows):
    return tuple(tuple(char == '#' for char in row.strip()) for row in rows)


def blocks(image):
    image = tuple(image)
    size = 2 if len(image) % 2 == 0 else 3

    for row_bound in range(0, len(image), size):
        for col_bound in range(0, len(image), size):
            rows = image[row_bound:row_bound + size]
            block = tuple(row[col_bound:col_bound + size] for row in rows)
            yield block


def rotate(array):
    array = tuple(array)
    return tuple(zip(*reversed(array)))


def variations(block):
    for _ in range(4):
        block = rotate(block)
        yield block
        yield reversed(block)
        yield rotate(rotate(rotate(reversed(rotate(block)))))


def translate(block):
    for variation in variations(block):
        if variation in rules:
            return rules[variation]
    raise ValueError('Input block not in rules:', block)


def assemble(blocks):
    blocks = tuple(blocks)
    size_in_blocks = int(len(blocks) ** 0.5)
    size_in_pixels = size_in_blocks * len(blocks[0])

    for block_row in (blocks[i:i + size_in_blocks] for i in range(0, len(blocks), size_in_blocks)):
        for row_pieces in zip(*block_row):
            yield tuple(x for piece in row_pieces for x in piece)


rules = dict((read_image(clause.split('/')) for clause in line.split(' => ')) for line in stdin.readlines())

for n in (5, 18):
    arr = read_image(('.#.', '..#', '###'))

    for _ in range(n):
        arr = tuple(assemble(translate(block) for block in blocks(arr)))

    print(sum(int(x) for row in arr for x in row))
