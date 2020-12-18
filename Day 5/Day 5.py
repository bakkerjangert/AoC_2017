with open('input.txt') as f:
    lines = f.read().splitlines()

instructions = []

for line in lines:
    instructions.append(int(line))


i = 0
step = 0
while 0 <= i < len(instructions):
    step += 1
    val = instructions[i]
    instructions[i] += 1
    i += val

print(f'the answer is {step}')


