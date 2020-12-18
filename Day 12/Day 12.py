with open('input.txt') as f:
    lines = f.read().splitlines()

data = {}

for line in lines:
    start = line.split()[0]
    targets = line.split('-> ')[1]
    targets = targets.split(', ')
    data[line.split()[0]] = targets

opened = ['0']
closed = []

while len(opened) > 0:
    for item in opened:
        lst = data[item]
        for goal in lst:
            if goal not in opened and goal not in closed:
                opened.append(goal)
        opened.remove(item)
        closed.append(item)

print(f'The answer is {len(closed)}')
