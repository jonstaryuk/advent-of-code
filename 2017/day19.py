from sys import stdin


m = stdin.readlines()

pos = [0, m[0].index('|')]  # row, column
vector = [1, 0]  # vertical, horizontal
letters = []
steps = 0


def getchar(row, col):
    try:
        return m[row][col]
    except IndexError:
        return ' '


while True:
    here = m[pos[0]][pos[1]]

    if here not in ('+', '-', '|', ' '):
        letters.append(here)

    nxt = [sum(x) for x in zip(pos, vector)]
    there = m[nxt[0]][nxt[1]]

    if vector[0] and there == '|' or vector[1] and there == '-':
        # Going in same direction
        pos = nxt
        steps += 1
    elif vector[0] and there == '-' or vector[1] and there == '|':
        # Step over the bridge
        pos = [sum(x) for x in zip(nxt, vector)]
        steps += 2
    elif there == '+':
        # Change direction
        possibilities = [
            [nxt[0] + 1, nxt[1]],
            [nxt[0] - 1, nxt[1]],
            [nxt[0], nxt[1] + 1],
            [nxt[0], nxt[1] - 1],
        ]

        pos = next(p for p in possibilities if getchar(p[0], p[1]) != ' ' and p != pos)
        i = possibilities.index(pos)
        if i == 0:
            vector = [1, 0]
        elif i == 1:
            vector = [-1, 0]
        elif i == 2:
            vector = [0, 1]
        else:
            assert i == 3
            vector = [0, -1]

        steps += 2
    elif there == ' ':
        # Reached the end
        steps += 1
        break
    elif there not in ('|', '-', '+'):
        # Encountered a letter
        pos = nxt
        steps += 1
    else:
        print('wat?', pos, here, vector, there)
        break


print(''.join(letters))
print(steps)
