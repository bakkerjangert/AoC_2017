with open('input.txt') as f:
    lines = f.read().splitlines()


def rotate(string):
    rotated_string = None
    if len(string) == 5:
        rotated_string = string[3] + string[0] + string[2] + string[4] + string[1]
    elif len(string) == 11:
        rotated_string = string[8] + string[4] + string[0] + string[3] + string[9] + string[5] + string[1] + string[7] + string[10] + string[6] + string[2]
    else:
        print(f'Error, len string cannot be rotated')
        exit()
    return rotated_string


def mirror(string):
    mirrored_string = None
    if len(string) == 5:
        mirrored_string = string[1] + string[0] + string[2] + string[4] + string[3]
    elif len(string) == 11:
        mirrored_string = string[2] + string[1] + string[0] + string[3] + string[6] + string[5] + string[4] + string[7] + string[10] + string[9] + string[8]
    else:
        print(f'Error, len string cannot be rotated')
        exit()
    return mirrored_string


data = {}

grid = ['.#.',
        '..#',
        '###']

for line in grid:
    print(line)

# string = grid[0] + '/' + grid[1] + '/' + grid[2]
# print(f'\n{string}\n')
# string = mirror(string)
# print(f'\n{string}\n')
# string = string.split('/')
# for line in string:
#     print(line)


for line in lines:
    val = line.split(' => ')[0]
    val_mir = mirror(val)
    out = line.split(' => ')[1]
    if val not in data:
        data[val] = out
    if val_mir not in data:
        data[val_mir] = out
    for i in range(3):
        val = rotate(val)
        val_mir = rotate(val_mir)
        if val not in data:
            data[val] = out
        if val_mir not in data:
            data[val_mir] = out

# for k, v in data.items():
#     print(f'{k} --> {v}')


for i in range(18):
    new_grid = []
    if len(grid) % 2 == 0:
        length = len(grid) // 2
        print(length)
        for y in range(length):
            new_grid.append([])
            for x in range(length):
                search_string = grid[y * 2][x * 2] + grid[y * 2][x * 2 + 1] + '/' + grid[y * 2 + 1][x * 2] + grid[y * 2 + 1][x * 2 + 1]
                new_grid[-1].append(data[search_string])
        grid.clear()
        for y in range(length):
            string_0 = ''
            string_1 = ''
            string_2 = ''
            for x in range(length):
                string_0 += new_grid[y][x][:3]
                string_1 += new_grid[y][x][4:7]
                string_2 += new_grid[y][x][8:]
            grid.append(string_0)
            grid.append(string_1)
            grid.append(string_2)
    elif len(grid) % 3 == 0:
        length = len(grid) // 3
        for y in range(length):
            new_grid.append([])
            for x in range(length):
                search_string = grid[y * 3][x * 3] + grid[y * 3][x * 3 + 1] + grid[y * 3][x * 3 + 2] + '/'\
                                + grid[y * 3 + 1][x * 3] + grid[y * 3 + 1][x * 3 + 1] + grid[y * 3 + 1][x * 3 + 2] + '/'\
                                + grid[y * 3 + 2][x * 3] + grid[y * 3 + 2][x * 3 + 1] + grid[y * 3 + 2][x * 3 + 2]
                new_grid[-1].append(data[search_string])
        grid.clear()
        for y in range(length):
            string_0 = ''
            string_1 = ''
            string_2 = ''
            string_3 = ''
            # ..../..../..../....
            for x in range(length):
                string_0 += new_grid[y][x][:4]
                string_1 += new_grid[y][x][5:9]
                string_2 += new_grid[y][x][10:14]
                string_3 += new_grid[y][x][15:]
            grid.append(string_0)
            grid.append(string_1)
            grid.append(string_2)
            grid.append(string_3)
    print('')
    for line in grid:
        print(line)

answer = 0
for line in grid:
    answer += line.count('#')

print(f'The answer is {answer}')