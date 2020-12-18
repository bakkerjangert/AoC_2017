banks = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]

# banks = [0, 2, 7, 0]

config = [tuple(banks)]

cycle = 0

while True:
    cycle += 1
    val = max(banks)
    index = banks.index(max(banks))
    banks[index] = 0
    for i in range(val):
        index += 1
        if index > len(banks) - 1:
            index = 0
        banks[index] += 1
    if tuple(banks) in config:
        print(f'solution found at {cycle} cycles')
        break
    config.append(tuple(banks))

for line in config:
    print(line)