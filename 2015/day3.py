f = open('in3', 'r')

i = 0
x_santa, y_santa = 0, 0
x_robot, y_robot = 0, 0
houses_served = [(0, 0)]  # Will be a list of (x, y) tuples
for line in f:
    for c in line:
        if i % 2 == 0:  # It's santa
            if c == '^':
                y_santa += 1
                i += 1
            elif c == 'v':
                y_santa -= 1
                i += 1
            elif c == '>':
                x_santa += 1
                i += 1
            elif c == '<':
                x_santa -= 1
                i += 1
        else:  # It's the robot
            if c == '^':
                y_robot += 1
                i += 1
            elif c == 'v':
                y_robot -= 1
                i += 1
            elif c == '>':
                x_robot += 1
                i += 1
            elif c == '<':
                x_robot -= 1
                i += 1


        if (x_santa, y_santa) not in houses_served:
            houses_served.append((x_santa, y_santa))

        if (x_robot, y_robot) not in houses_served:
            houses_served.append((x_robot, y_robot))

print "Houses served:", len(houses_served)
