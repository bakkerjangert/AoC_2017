with open('input.txt') as f:
    lines = f.read().splitlines()

def swing(string, data):
    val = -int(string)
    data = data[val:] + data[:val]
    return data


def exchange(string, data):
    val_a = int(string.split('/')[0])
    val_b = int(string.split('/')[1])
    prog_a = data[val_a]
    prog_b = data[val_b]
    if val_a < val_b:
        data = data[:val_a] + prog_b + data[val_a + 1: val_b] + prog_a + data[val_b + 1:]
    else:
        data = data[:val_b] + prog_a + data[val_b + 1: val_a] + prog_b + data[val_a + 1:]
    return data


def partner(string, data):
    prog_a = string.split('/')[0]
    prog_b = string.split('/')[1]
    val_a = data.index(prog_a)
    val_b = data.index(prog_b)
    if val_a < val_b:
        data = data[:val_a] + prog_b + data[val_a + 1: val_b] + prog_a + data[val_b + 1:]
    else:
        data = data[:val_b] + prog_a + data[val_b + 1: val_a] + prog_b + data[val_a + 1:]
    return data



instructions = lines[0].split(',')

string = 'abcdefghijklmnop'

strings = [string]
iteration = 0
while True:
    iteration += 1
    for instruction in instructions:
        if instruction[0] == 's':
            string = swing(instruction[1:], string)
        elif instruction[0] == 'x':
            string = exchange(instruction[1:], string)
        elif instruction[0] == 'p':
            string = partner(instruction[1:], string)
    if string in strings:
        print(f'Repetition after {iteration} iterations')
        print(string)
        break
    strings.append(string)

index = 1000000000 % len(strings)
print(strings[index])




