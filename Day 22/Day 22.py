with open('input.txt') as f:
    lines = f.read().splitlines()



def print_grid(grid):
    print(f'\n---Printing grid---')
    for line in grid:
        print('')
        for char in line:
            print(char, end='')
    print(f'\n{dir} --> {pos}\n')


grid = []
for line in lines:
    grid.append([])
    for char in line:
        grid[-1].append(char)

# 0 = N, 1 = E, 2 = S, 3 = W
dirs = [0, 1, 2, 3]

dir = 0
pos = [len(grid[0]) // 2, len(grid) // 2]

answer = 0

for i in range(10000):
    # Turn and switch infection
    if grid[pos[1]][pos[0]] == '#':
        grid[pos[1]][pos[0]] = '.'
        if dir < 3:
            dir += 1
        else:
            dir = 0
    else:
        answer += 1  # Node becomes infected
        grid[pos[1]][pos[0]] = '#'
        if dir > 0:
            dir -= 1
        else:
            dir = 3
    # Move
    if dir == 0:  # North
        if pos[1] == 0:
            # Add row
            grid.insert(0, [])
            for j in range(len(grid[1])):
                grid[0].append('.')
            # Note position stays at y = 0
        else:
            pos[1] -= 1
    if dir == 1:  # East
        if pos[0] == len(grid[0]) - 1:
            # add column
            for j in range(len(grid)):
                grid[j].append('.')
        pos[0] += 1
    if dir == 2:  # South
        if pos[1] == len(grid) - 1:
            grid.append([])
            for j in range(len(grid[0])):
                grid[-1].append('.')
        pos[1] += 1
    if dir == 3:  # West
        if pos[0] == 0:
            for j in range(len(grid)):
                grid[j].insert(0, '.')
            # Note position stays at x = 0
        else:
            pos[0] -= 1
    # print_grid(grid)

print(f'The answer is {answer}')


