from sys import stdin
from collections import defaultdict


lines = stdin.readlines()

dirsize = defaultdict(int)
dirs = ['/']
for line in lines:
    line = line.rstrip()
    if line == '$ cd /':
        dirs = ['/']
    elif line == '$ cd ..':
        dirs.pop()
    elif line.startswith('$ cd '):
        dirs.append(line[len('$ cd '):])
    elif line == '$ ls':
        pass
    elif line.startswith('dir '):
        pass
    else:
        size, name = line.split()
        for i in range(1, len(dirs)+1):
            dirsize['/'.join(dirs[:i])] += int(size)

print(sum(x for x in dirsize.values() if x <= 100000))

unused = 70000000-dirsize['/']
need_to_free = 30000000-unused
print(min(x for x in dirsize.values() if x >= need_to_free))
