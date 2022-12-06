from sys import stdin

data = stdin.read().strip()


# 1

for i in range(len(data)-3):
    w = data[i:i+4]
    if len(set(w)) == 4:
        print(i+4)
        break


# 2

for i in range(len(data)-13):
    w = data[i:i+14]
    if len(set(w)) == 14:
        print(i+14)
        break
