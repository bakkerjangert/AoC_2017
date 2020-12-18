with open('input.txt') as f:
    lines = f.read().splitlines()

string = lines[0]

answer = 0

for i in range(len(string)):
    if string[i] == string[i - 1]:
        answer += int(string[i])

print(f'The answer = {answer}')
