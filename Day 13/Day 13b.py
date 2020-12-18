with open('input.txt') as f:
    lines = f.read().splitlines()

def grid_plus1(grid):
    for k, v in grid.items():
        if v[0] == 0:
            grid[k] = (1, v[1], 1)
        elif v[0] == v[1] - 1:
            grid[k] = (v[0] - 1, v[1], -1)
        else:
            grid[k] = (v[0] + v[2], v[1], v[2])
    return grid

def run(grid):
    max_pos = max(list(grid.keys()))
    for time in range(max_pos + 1):
        try:
            if grid[time][0] == 0:
                return False
        except KeyError:
            pass
        for k, v in grid.items():
            if v[0] == 0:
                grid[k] = (1, v[1], 1)
            elif v[0] == v[1] - 1:
                grid[k] = (v[0] - 1, v[1], -1)
            else:
                grid[k] = (v[0] + v[2], v[1], v[2])
    return True


grid = {}

for line in lines:
    index = int(line.split(':')[0])
    length = int(line.split(': ')[1])
    grid[index] = (0, length, 1)

time = 0

while True:
    time += 1
    grid = grid_plus1(grid)
    # print(grid[0])
    if run(grid.copy()):
        break
    if time % 10000 == 0:
        print(f'running step {time}')

print(f'the answer = {time}')




