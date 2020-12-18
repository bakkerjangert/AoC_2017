with open('input.txt') as f:
    lines = f.read().splitlines()

acc = 9999999999
answer = None

# Slowest accelerating particle will stay closest in the end --> Minimum absolute value of acceleration is the answer

for i in range(len(lines)):
    string = lines[i]
    string = string.split('a=')[-1]
    string = string[1:-1]
    vals = string.split(',')
    cur_acc = 0
    for val in vals:
        cur_acc += abs(int(val))
    if cur_acc < acc:
        answer = i
        acc = cur_acc

print(f'The answer is {answer}')