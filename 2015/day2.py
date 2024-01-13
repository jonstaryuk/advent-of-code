def surface_area(l, w, h):
    l, w, h = int(l), int(w), int(h)
    return 2*l*w + 2*w*h + 2*h*l

def volume(l, w, h):
    l, w, h = int(l), int(w), int(h)
    return l * w * h

def smallest_side(l, w, h):
    l, w, h = int(l), int(w), int(h)
    s1 = l * w
    s2 = w * h
    s3 = h * l
    return min(s1, s2, s3)

def paper_needed(l, w, h):
    return surface_area(l, w, h) + smallest_side(l, w, h)

def shortest_side_perimeter(l, w, h):
    l, w, h = int(l), int(w), int(h)
    s1p = 2*l + 2*w
    s2p = 2*w + 2*h
    s3p = 2*l + 2*h
    return min(s1p, s2p, s3p)

f = open('in2', 'r')

total_sqft_needed = 0
total_ribbon_needed = 0

for line in f:
    dimensions = line.split('x')
    l, w, h = dimensions[0], dimensions[1], dimensions[2]
    total_sqft_needed += paper_needed(l, w, h)
    total_ribbon_needed += shortest_side_perimeter(l, w, h) + volume(l, w, h)

print "Wrapping paper:", total_sqft_needed
print "Ribbon:", total_ribbon_needed
