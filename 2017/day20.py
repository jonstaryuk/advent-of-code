from sys import stdin


class Vector:

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def dist(self):
        return sum(abs(x) for x in (self.x, self.y, self.z))


class Particle:

    def __init__(self, pos, vel, acc):
        self.pos, self.vel, self.acc = pos, vel, acc
        self.accelerating_away = None

    def move(self):
        prev_dist = self.pos.dist()
        prev_velocity = self.vel.dist()

        self.vel += self.acc
        self.pos += self.vel

        self.accelerating_away = self.pos.dist() >= prev_dist and self.vel.dist() >= prev_velocity


particles = [line.split(', ') for line in stdin.readlines()]
particles = [Particle(*(Vector(*map(int, coords.strip('\npva=<>').split(','))) for coords in particle)) for particle in particles]

print(min(enumerate(particles), key=lambda tup: (tup[1].acc.dist(), tup[1].vel.dist(), tup[1].pos.dist()))[0])

while not all(p.accelerating_away for p in particles):
    positions = {}

    for p in particles:
        p.move()
        positions[p.pos] = positions.get(p.pos, 0) + 1

    particles = [p for p in particles if positions[p.pos] == 1]

print(len(particles))
