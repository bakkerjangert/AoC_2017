with open('input.txt') as f:
    lines = f.read().splitlines()

def set(string, data):
    reg = string[4]
    val = string.split()[-1]
    if val[-1].isdigit():
        val = int(val)
    else:
        val = data[val]
    data[reg] = val
    return data

def sub(string, data):
    reg = string[4]
    val = string.split()[-1]
    if val[-1].isdigit():
        val = int(val)
    else:
        val = data[val]
    data[reg] -= val
    return data

def mul(string, data):
    reg = string[4]
    val = string.split()[-1]
    if val[-1].isdigit():
        val = int(val)
    else:
        val = data[val]
    data[reg] *= val
    return data

def jnz(string, data, index_val):
    val_1 = string[4]
    if val_1[-1].isdigit():
        val_1 = int(val_1)
    else:
        val_1 = data[val_1]
    val_2 = string.split()[-1]
    if val_2[-1].isdigit():
        val_2 = int(val_2)
    else:
        val_2 = data[val_2]
    if val_1 != 0:
        index_val += val_2
    else:
        index_val += 1
    return index_val


data = {}
string = 'abcdefgh'
index_val = 0
for char in string:
    data[char] = 0

answer = 0

while 0 <= index_val < len(lines):
    string = lines[index_val]
    if 'set' in string:
        data = set(string, data)
    elif 'sub' in string:
        data = sub(string, data)
    elif 'mul' in string:
        answer += 1
        data = mul(string, data)
    elif 'jnz' in string:
        index_val = jnz(string, data, index_val)
    if 'jnz' not in string:
        index_val += 1


print(f'The answer is {answer}')
