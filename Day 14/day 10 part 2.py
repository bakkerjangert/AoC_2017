def shift(lst, n):
    return lst[-n:] + lst[:-n]

def convert_asscii(string):
    puzzle = []
    for char in string:
        puzzle.append(ord(char))
    appendix = [17, 31, 73, 47, 23]
    return puzzle + appendix

def gen_data(number):
    data = []
    for i in range(number):
        data.append(i)
    return data

def knot(rounds, data, puzzle):
    cur_index = 0
    skip_size = 0
    for round in range(rounds):
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
    return data

def gen_dense_hash(data):
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
    return dense_hash

def gen_hexi(dense_hash):
    hexi = ''
    for item in dense_hash:
        val = hex(item)
        if len(val) == 4:
            hexi += val[-2:]
        else:
            hexi += '0' + val[-1]
    return hexi

def gen_hexi_dict():
    hex_dict = {}
    temp = '0000'
    for i in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'):
        hex_dict[i] = temp[::-1]
        index = 0
        while True:
            if temp[index] == '0':
                temp = temp[:index] + '1' + temp[index + 1:]
                break
            else:
                temp = temp[:index] + '0' + temp[index + 1:]
            index += 1
            if index > 3:
                break
    return hex_dict

def gen_bin_string(hexi, hexi_dict):
    bin_string = ''
    for char in hexi:
        bin_string += hexi_dict[char]
    return bin_string

hexi_dict = gen_hexi_dict()

puzzle_string = '187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216'

puzzle = convert_asscii(puzzle_string)

data = gen_data(256)

data = knot(64, data, puzzle)

dense_hash = gen_dense_hash(data)

hexi = gen_hexi(dense_hash)

bin_string = gen_bin_string(hexi, hexi_dict)

print(f'the answer = {hexi}')



