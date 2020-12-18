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

def add(string, data):
    reg = string[4]
    val = string.split()[-1]
    if val[-1].isdigit():
        val = int(val)
    else:
        val = data[val]
    data[reg] += val
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

def mod(string, data):
    reg = string[4]
    val = string.split()[-1]
    if val[-1].isdigit():
        val = int(val)
    else:
        val = data[val]
    data[reg] = data[reg] % val
    return data

def jgz(string, data, index_val):
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
    if val_1 > 0:
        index_val += val_2
    else:
        index_val += 1
    return index_val

def snd(string, data):
    val_1 = string.split()[-1]
    if val_1[-1].isdigit():
        val_1 = int(val_1)
    else:
        val_1 = data[val_1]
    freq = val_1
    return freq

def rcv(string, data, freq):
    val_1 = string.split()[-1]
    if val_1[-1].isdigit():
        val_1 = int(val_1)
    else:
        val_1 = data[val_1]
    if val_1 != 0:
        print(f'The answer is {freq}')
        exit()
    else:
        pass
    return None

data = {}
sound_frequency = 0
index_val = 0
for line in lines:
    val_1 = line.split()[1]
    if not val_1[-1].isdigit():
        data[val_1] = 0
    val_2 = line.split()[-1]
    if not val_2[-1].isdigit():
        data[val_2] = 0

while 0 <= index_val < len(lines):
    string = lines[index_val]
    if 'snd' in string:
        sound_frequency = snd(string, data)
    elif 'set' in string:
        data = set(string, data)
    elif 'add' in string:
        data = add(string, data)
    elif 'mul' in string:
        data = mul(string, data)
    elif 'mod' in string:
        data = mod(string, data)
    elif 'rcv' in string:
        rcv(string, data, sound_frequency)
    elif 'jgz' in string:
        index_val = jgz(string, data, index_val)
    if 'jgz' not in string:
        index_val += 1
