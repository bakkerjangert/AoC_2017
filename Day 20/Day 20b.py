with open('input.txt') as f:
    lines = f.read().splitlines()

class Particle(object):
    def __init__(self, instruction):
        pos = instruction.split('<')[1]
        pos = pos.split('>')[0]
        pos = pos.split(',')
        self.pos = list(map(int, pos))
        vel = instruction.split('<')[2]
        vel = vel.split('>')[0]
        vel = vel.split(',')
        self.vel = list(map(int, vel))
        acc = instruction.split('<')[3]
        acc = acc.split('>')[0]
        acc = acc.split(',')
        self.acc = list(map(int, acc))

    def update(self):
        for i in range(3):
            self.vel[i] += self.acc[i]
            self.pos[i] += self.vel[i]

data = {}
pos_lst = []
del_lst = []

for i in range(len(lines)):
    data[i] = Particle(lines[i])
    pos_lst.append(tuple(data[i].pos))

for step in range(1000):
    pos_lst.clear()
    del_lst.clear()
    for index, part in data.items():
        part.update()
        pos_lst.append(part.pos)
    for index, part in data.items():
        if pos_lst.count(part.pos) > 1:
            # collision
            del_lst.append(index)
    for index in del_lst:
        del data[index]
    print(f'{len(data)}')

print(f'\nThe answer is {len(data)}')