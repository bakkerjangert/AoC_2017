def shift(lst, n):
    return lst[-n:] + lst[:-n]


puzzle_string = '187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216'

# Test
# puzzle_string = ''

puzzle = []
for char in puzzle_string:
    puzzle.append(ord(char))



appendix = [17, 31, 73, 47, 23]
puzzle += appendix

data = []

cur_index = 0
skip_size = 0

for i in range(256):
    data.append(i)

# data = [0, 1, 2, 3, 4]

# Example of reversion
# a[2:4] = a[2:4][::-1]
for round in range(64):
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

dense_hash = []

for i in range(16):
    dense = None
    for j in range(16):
        index_val = j + 16 * i
        if dense is None:
            dense = data[index_val]
        else:
            dense = dense ^ data[index_val]
    dense_hash.append(dense)

hexi = ''

for item in dense_hash:
    val = hex(item)
    if len(val) == 4:
        hexi += val[-2:]
    else:
        hexi += '0' + val[-1]


print(f'the answer = {hexi}')



