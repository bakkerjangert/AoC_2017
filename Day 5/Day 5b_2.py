with open('input.txt') as f:
    lines = f.read().splitlines()

instructions = []

for line in lines:
    instructions.append(int(line))

# instructions = [0, 3,  0,  1,  -3]

i = 0
step = 0
jump = 0
while 0 <= i < len(instructions):
    step += 1
    jump = instructions[i]
    if jump < 3:
        instructions[i] += 1
    else:
        instructions[i] -= 1
    i += jump
    if step % 1000000 == 0:
        print(f'Jump {jump} steps to row {i + 1} at {round((i + 1) / len(instructions) * 100,1)} %')


print(f'the answer is {step}')


