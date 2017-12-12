from sys import stdin


class Node:
    def __init__(self):
        self.discovered = False
        self.neighbors = set()


def dfs_count(graph, v):
    if graph[v].discovered:
        return 0

    graph[v].discovered = True

    return 1 + sum(dfs_count(graph, u) for u in graph[v].neighbors)


def solve(lines):
    graph = {}

    for line in lines:
        info = line.split(maxsplit=2)

        v = int(info[0])
        if v not in graph:
            graph[v] = Node()

        graph[v].neighbors.update({int(x) for x in info[2].split(', ')})

    print(dfs_count(graph, 0))

    components = [dfs_count(graph, v) for v in graph]
    print(1 + len([n for n in components if n > 0]))


if __name__ == '__main__':
    solve(stdin.readlines())
