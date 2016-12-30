import itertools


def possible_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


if __name__ == '__main__':
    with open("day3.in") as f:
        raw = f.read()
    lines = raw.split('\n')

    triangles = [[int(x) for x in line.split()] for line in lines]
    print(len([tri for tri in triangles if possible_triangle(*tri)]))

    # Transpose and chain
    chain = list(itertools.chain(*zip(*triangles)))
    new_triangles = [(chain[i], chain[i+1], chain[i+2]) for i in range(0, len(chain), 3)]
    print(len([tri for tri in new_triangles if possible_triangle(*tri)]))
