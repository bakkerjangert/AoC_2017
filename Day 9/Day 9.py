with open('input.txt') as f:
    lines = f.read().splitlines()

string = lines[0]

while '<' in string:
    start_index = string.find('<')
    sub_string = string[start_index:]
    shift = start_index
    while True:
        end_index = sub_string.find('>')
        i_count = 0
        end_min = end_index - 1
        while sub_string[end_min] == '!':
            i_count += 1
            end_min -= 1
        try:
            if i_count % 2 == 1:
                sub_string = sub_string[:end_index] + 'X' + sub_string[end_index + 1:]
                continue
        except ZeroDivisionError:
            pass
        chars = end_index - 1
        string = string[:start_index] + '[' + 'X' * chars + ']' + string[shift + end_index + 1:]
        break

i = 0
for j in range(len(string) // 100):
    print(string[i: i + 100])
    i += 100
print(string[i:])
print(f'opens = {string.count("{")}, closed = {string.count("}")}')

lvl = 0
count = 0
for char in string:
    if char == '{':
        lvl += 1
        count += lvl
    elif char == '}':
        lvl -= 1

print(f'The answer is {count}')


