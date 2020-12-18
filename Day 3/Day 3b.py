goal = 325489

def sum_adjacent(grid, pos):
    val = 0
    x_0 = pos[0]
    y_0 = pos[1]
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == y == 0 or (x_0 + x) < 0 or (y_0 + y) < 0:
                pass
            else:
                try:
                    val += grid[y_0 + y][x_0 + x]
                except IndexError:
                    pass
    return val


def print_grid(grid):
    print('\n--START--')
    for line in grid:
        print(line)
    print(f'---END---')



# Directions
# 0 -->  ->
# 1 -->  ^^
# 2 -->  <--
# 3 -->  vv

dir = 1

grid = [[1]]

while True:
    # print(f'Value {value} at x = {x} and y = {y}')
    if dir == 0:
        grid.append([])
        for i in range(len(grid[0])):
            grid[-1].append(0)
        for i in range(len(grid[0])):
            pos = (i, len(grid) - 1)
            val = sum_adjacent(grid, pos)
            if val > goal:
                print(f'Answer found --> {val}')
                exit()
            grid[len(grid) - 1][i] = val
        print_grid(grid)
        dir += 1
    elif dir == 1:
        for i in range(len(grid)):
            grid[i].append(0)
        for i in range(len(grid), 0, -1):
            pos = (len(grid[i - 1]) - 1, i - 1)
            val = sum_adjacent(grid, pos)
            if val > goal:
                print(f'Answer found --> {val}')
                exit()
            grid[i - 1][-1] = val
        print_grid(grid)
        dir += 1
    elif dir == 2:
        grid.insert(0, [])
        for i in range(len(grid[1])):
            grid[0].append(0)
        for i in range(len(grid[0]), 0, -1):
            pos = (i - 1, 0)
            val = sum_adjacent(grid, pos)
            if val > goal:
                print(f'Answer found --> {val}')
                exit()
            grid[0][i - 1] = val
        print_grid(grid)
        dir += 1
    elif dir == 3:
        for i in range(len(grid)):
            grid[i].insert(0, 0)
        for i in range(0, len(grid)):
            pos = (0, i)
            val = sum_adjacent(grid, pos)
            if val > goal:
                print(f'Answer found --> {val}')
                exit()
            grid[i][0] = val
        print_grid(grid)
        dir = 0


