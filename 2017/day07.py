from collections import Counter
from sys import stdin


class Node:
    def __init__(self):
        self.weight, self.children, self.parent = None, None, None
        self.tw = None

    def total_weight(self, tree):
        child_weights = sum(tree[child].total_weight(tree) for child in self.children)
        return self.weight + child_weights


def build_tree(lines):
    tree = {}

    for line in lines:
        line = line.split()

        name = line[0]
        if name not in tree:
            tree[name] = Node()

        n = tree[name]
        n.weight = int(line[1].strip('()'))
        if len(line) > 2:
            n.children = {s.strip(',') for s in line[3:]}
        else:
            n.children = set()

        for child in n.children:
            if child not in tree:
                tree[child] = Node()
            tree[child].parent = name

        tree[name] = n

    return tree


def solve(lines):
    tree = build_tree(lines)
    return [name for name, node in tree.items() if node.parent is None][0]


def find_wrong_weight(tree, node_name):
    node = tree[node_name]
    child_nodes = [tree[child] for child in node.children]
    weights = {n.weight: n.total_weight(tree) for n in child_nodes}
    if len(set(weights.values())) > 1:
        yield [(weight, total) for weight, total in weights.items()]

    for child in node.children:
        yield from find_wrong_weight(tree, child)


def solve2(lines):
    tree = build_tree(lines)
    root = [name for name, node in tree.items() if node.parent is None][0]

    bad_set = list(find_wrong_weight(tree, root))[-1]
    counter = Counter(tup[1] for tup in bad_set)
    weights = [tup[0] for tup in counter.most_common(2)]

    diff = weights[1] - weights[0]
    bad_node_weight = next(tup[0] for tup in bad_set if tup[1] == weights[1])
    return bad_node_weight - diff


if __name__ == '__main__':
    print(solve2(stdin.readlines()))
