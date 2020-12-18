with open('input.txt') as f:
    lines = f.read().splitlines()

sheet = []
checksum = 0

for line in lines:
    sheet.append(list(map(int, line.split())))
    for i in range(len(sheet[-1]) - 1):
        for j in range(i + 1, len(sheet[-1])):
            val_1 = sheet[-1][i]
            val_2 = sheet[-1][j]
            if max(val_1, val_2) % min(val_1, val_2) == 0:
                checksum += max(val_1, val_2) // min(val_1, val_2)

print(f'The answer is {checksum}')

