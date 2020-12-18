with open('input.txt') as f:
    lines = f.read().splitlines()

registers = {}

for line in lines:
    reg_1 = line.split()[0]
    reg_2 = line.split()[4]
    for reg in (reg_1, reg_2):
        if reg not in list(registers.keys()):
            registers[reg] = 0

for line in lines:
    check_reg_val = registers[line.split()[4]]
    check_val = int(line.split()[-1])
    check = line.split()[5]
    if check == '==':
        if check_reg_val == check_val:
            if line.split()[1] == 'inc':
                registers[line.split()[0]] += int(line.split()[2])
            else:
                registers[line.split()[0]] -= int(line.split()[2])
    elif check == '!=':
        if check_reg_val != check_val:
            if line.split()[1] == 'inc':
                registers[line.split()[0]] += int(line.split()[2])
            else:
                registers[line.split()[0]] -= int(line.split()[2])
    elif check == '<=':
        if check_reg_val <= check_val:
            if line.split()[1] == 'inc':
                registers[line.split()[0]] += int(line.split()[2])
            else:
                registers[line.split()[0]] -= int(line.split()[2])
    elif check == '>=':
        if check_reg_val >= check_val:
            if line.split()[1] == 'inc':
                registers[line.split()[0]] += int(line.split()[2])
            else:
                registers[line.split()[0]] -= int(line.split()[2])
    elif check == '<':
        if check_reg_val < check_val:
            if line.split()[1] == 'inc':
                registers[line.split()[0]] += int(line.split()[2])
            else:
                registers[line.split()[0]] -= int(line.split()[2])
    elif check == '>':
        if check_reg_val > check_val:
            if line.split()[1] == 'inc':
                registers[line.split()[0]] += int(line.split()[2])
            else:
                registers[line.split()[0]] -= int(line.split()[2])

print(f'The answer is {max(list(registers.values()))}')