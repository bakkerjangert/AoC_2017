with open('input.txt') as f:
    lines = f.read().splitlines()

grid = {}

for line in lines:
    index = int(line.split(':')[0])
    length = int(line.split(': ')[1])
    grid[index] = (0, length, 1)

max_pos = max(list(grid.keys()))
print(max_pos)

caught = []

for time in range(max_pos + 1):
    try:
        if grid[time][0] == 0:
            caught.append(time)
    except KeyError:
        pass
    print(f'\n-----')
    for k, v in grid.items():
        if v[0] == 0:
            grid[k] = (1, v[1], 1)
        elif v[0] == v[1] - 1:
            grid[k] = (v[0] - 1, v[1], -1)
        else:
            grid[k] = (v[0] + v[2], v[1], v[2])
        print(grid[k])
print(caught)

answer = 0
for item in caught:
    answer += item * grid[item][1]

print(f'The answer = {answer}')