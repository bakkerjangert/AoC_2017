with open('input.txt') as f:
    lines = f.read().splitlines()

string = lines[0]

offset = len(string) // 2

answer = 0

for i in range(len(string) // 2):
    if string[i] == string[i + offset]:
        answer += int(string[i])

print(f'The answer = {answer * 2}')
