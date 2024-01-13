f = open('input.txt', 'r')

parenlevel = 0
i = 0
for line in f:
    for c in line:
            if c == '(':
                    parenlevel += 1
            elif c == ')':
                    parenlevel -= 1
            i += 1
            if parenlevel == -1:
                print "Entered basement, position is", i
