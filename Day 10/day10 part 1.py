def shift(lst, n):
    return lst[-n:] + lst[:-n]


puzzle = [187, 254, 0, 81, 169, 219, 1, 190, 19, 102, 255, 56, 46, 32, 2, 216]

# puzzle = [3, 4, 1, 5]

data = []

cur_index = 0
skip_size = 0

for i in range(256):
    data.append(i)

# data = [0, 1, 2, 3, 4]

# Example of reversion
# a[2:4] = a[2:4][::-1]

for val in puzzle:
    # print(f'Start --> {data}')
    data = shift(data, -cur_index)
    # print(f'Shift left with {cur_index} --> {data}')
    data[0: val] = data[0: val][::-1]
    # print(f'Inverse {val} positions --> {data}')
    data = shift(data, cur_index)
    cur_index += val + skip_size
    cur_index = cur_index % len(data)
    # print(f'Shift data back again --> {data}')
    # print(f'current position = {cur_index}')
    skip_size += 1
    # print('-----\n')

print(f'The answer = {data[0] * data[1]}')



