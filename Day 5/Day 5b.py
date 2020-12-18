with open('input.txt') as f:
    lines = f.read().splitlines()

instructions = []

for line in lines:
    instructions.append(int(line))

instructions = [0, 3,  0,  1,  -3]

i = 0
step = 0
jump = 0
while 0 <= i < len(instructions):
    step += 1
    if jump < 3:
        jump = instructions[i]
        instructions[i] += 1
    else:
        jump = instructions[i]
        instructions[i] -= 1
        print(f'\n-----\n{instructions[:10]}')
    i += jump

    print(f'Jump {jump} steps to row {i + 1}')

print(f'the answer is {step}')
print(instructions)


