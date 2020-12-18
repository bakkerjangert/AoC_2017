with open('input.txt') as f:
    lines = f.read().splitlines()

answer = 0

for line in lines:
    lst = line.split()
    for i in range(len(lst)):
        lst[i] = sorted(lst[i])
        valid = True
    for item in lst:
        if lst.count(item) > 1:
            valid = False
            break
    if valid:
        answer += 1

print(f'The answer is {answer}')
