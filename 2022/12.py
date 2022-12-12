import heapq

raw = open('12.in').read()
lines = raw.rstrip().split('\n')


map = [list(l) for l in lines]


def indices_of(c):
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell == c:
                yield i, j


s = next(indices_of('S'))
e = next(indices_of('E'))


def dirs(pos, cost):
    pi, pj = pos
    src = map[pi][pj].replace('S', 'a').replace('E', 'z')

    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni = pi + di
        nj = pj + dj
        if not (0 <= ni < len(map) and 0 <= nj < len(map[0])):
            continue

        dest = map[ni][nj].replace('S', 'a').replace('E', 'z')
        if ord(dest) <= ord(src) + 1:
            yield (cost + 1, (ni, nj))


def explore(pq, dst, explored):
    cost, pos = heapq.heappop(pq)

    if pos in explored:
        return
    explored.add(pos)

    for cost, pos in dirs(pos, cost):
        if pos == dst:
            return cost

        heapq.heappush(pq, (cost, pos))


def search(start):
    pq = [(0, start)]
    explored = set()
    while pq:
        found = explore(pq, e, explored)
        if found:
            return found


print(search(s))

starts = list(indices_of('a')) + [s]
print(min((search(x) or 1e100) for x in starts))
