with open('input.txt') as f:
    grid = f.read().splitlines()

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

directions = ['N', 'E', 'S', 'W']
direction = 'S'  # Look at puzzle input
pos = [grid[0].index('|'), 0]

answer = ''
steps = 1
while True:
    # determine next pos:
    if direction == 'N':
        pos[1] -= 1
    elif direction == 'E':
        pos[0] += 1
    elif direction == 'S':
        pos[1] += 1
    elif direction == 'W':
        pos[0] -= 1
    char = grid[pos[1]][pos[0]]
    steps += 1
    if char == 'T':  # Last entry, see puzzle input
        answer += char
        break
    elif char in letters:
        answer += char
    elif char == '+':
        if direction == 'N' or direction == 'S':
            if grid[pos[1]][pos[0] + 1] == '-':
                direction = 'E'
            else:
                direction = 'W'
        else:
            if grid[pos[1] + 1][pos[0]] == '|':
                direction = 'S'
            else:
                direction = 'N'
    else:
        pass

print(f'The answer is {answer}')
print(f'The answer to part 2 is {steps}')