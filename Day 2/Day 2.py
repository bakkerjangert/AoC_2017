with open('input.txt') as f:
    lines = f.read().splitlines()

sheet = []
checksum = 0

for line in lines:
    sheet.append(list(map(int, line.split())))
    line_min = min(sheet[-1])
    line_max = max(sheet[-1])
    dif = line_max - line_min
    checksum += dif

print(f'The answer is {checksum}')

