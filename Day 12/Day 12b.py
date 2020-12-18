with open('input.txt') as f:
    lines = f.read().splitlines()


def find_goals(start, data):
    opened = [start]
    closed = []
    while len(opened) > 0:
        for item in opened:
            lst = data[item]
            for goal in lst:
                if goal not in opened and goal not in closed:
                    opened.append(goal)
            opened.remove(item)
            closed.append(item)
    return closed

def remove_items(closed, data):
    for item in closed:
        del data[item]
    return data


data = {}

for line in lines:
    start = line.split()[0]
    targets = line.split('-> ')[1]
    targets = targets.split(', ')
    data[line.split()[0]] = targets

counter = 0
while len(data) != 0:
    counter += 1
    start = min(list(data.keys()))
    closed = find_goals(start, data)
    remove_items(closed, data)
    print(f'after iteration {counter} the data is {len(data)} lines long')


print(f'The answer is {counter}')
