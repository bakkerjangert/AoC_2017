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

def rcv(string, data, snd_lst):
    val_1 = snd_lst[0]
    del snd_lst[0]
    reg = string.split()[-1]
    data[reg] = val_1
    return data, snd_lst

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

data_0 = data.copy()
data_1 = data.copy()
data_1['p'] = 1

index_val_0 = 0
index_val_1 = 0

snd_0_1 = []
snd_1_0 = []

idle_0 = False
idle_1 = False

answer = 0

while 0 <= index_val_0 < len(lines):
    # Prog 0
    if not 0 <= index_val_0 < len(lines):
        idle_0 = True
    else:
        string_0 = lines[index_val_0]
        if 'snd' in string_0:
            snd_0_1.append(snd(string_0, data_0))
        elif 'set' in string_0:
            data_0 = set(string_0, data_0)
        elif 'add' in string_0:
            data_0 = add(string_0, data_0)
        elif 'mul' in string_0:
            data_0 = mul(string_0, data_0)
        elif 'mod' in string_0:
            data_0 = mod(string_0, data_0)
        elif 'rcv' in string_0:
            # Update!
            if len(snd_1_0) == 0:
                idle_0 = True
            else:
                idle_0 = False
                temp = rcv(string_0, data_0, snd_1_0)
                data_0 = temp[0]
                snd_1_0 = temp[1]
        elif 'jgz' in string_0:
            index_val_0 = jgz(string_0, data_0, index_val_0)
        if 'jgz' not in string_0 and not idle_0:
            index_val_0 += 1
    # Prog 1
    if not 0 <= index_val_1 < len(lines):
        idle_1 = True
    else:
        string_1 = lines[index_val_1]
        if 'snd' in string_1:
            answer += 1
            snd_1_0.append(snd(string_1, data_1))
        elif 'set' in string_1:
            data_1 = set(string_1, data_1)
        elif 'add' in string_1:
            data_1 = add(string_1, data_1)
        elif 'mul' in string_1:
            data_1 = mul(string_1, data_1)
        elif 'mod' in string_1:
            data_1 = mod(string_1, data_1)
        elif 'rcv' in string_1:
            # Update!
            if len(snd_0_1) == 0:
                idle_1 = True
            else:
                idle_1 = False
                temp = rcv(string_1, data_1, snd_0_1)
                data_1 = temp[0]
                snd_0_1 = temp[1]
        elif 'jgz' in string_1:
            index_val_1 = jgz(string_1, data_1, index_val_1)
        if 'jgz' not in string_1 and not idle_1:
            index_val_1 += 1
    # Check if both are idle
    if idle_0 and idle_1:
        break

print(f'The answer is {answer}')
