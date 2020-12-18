state = 'A'
steps = 12172063
data = [0]
index = 0


def move_left(index):
    if index == 0:
        data.insert(0, 0)
    else:
        index -= 1
    return index


def move_right(index):
    if index == len(data) - 1:
        data.append(0)
    index += 1
    return index


for step in range(steps):
    if step % 10000 == 0:
        print(f'Currently at {round(step / steps * 100, 2)}%')
    if state == 'A':
        if data[index] == 0:
            data[index] = 1
            index = move_right(index)
            state = 'B'
        else:
            data[index] = 0
            index = move_left(index)
            state = 'C'

    elif state == 'B':
        if data[index] == 0:
            data[index] = 1
            index = move_left(index)
            state = 'A'
        else:
            data[index] = 1
            index = move_left(index)
            state = 'D'

    elif state == 'C':
        if data[index] == 0:
            data[index] = 1
            index = move_right(index)
            state = 'D'
        else:
            data[index] = 0
            index = move_right(index)
            state = 'C'

    elif state == 'D':
        if data[index] == 0:
            data[index] = 0
            index = move_left(index)
            state = 'B'
        else:
            data[index] = 0
            index = move_right(index)
            state = 'E'

    elif state == 'E':
        if data[index] == 0:
            data[index] = 1
            index = move_right(index)
            state = 'C'
        else:
            data[index] = 1
            index = move_left(index)
            state = 'F'

    elif state == 'F':
        if data[index] == 0:
            data[index] = 1
            index = move_left(index)
            state = 'E'
        else:
            data[index] = 1
            index = move_right(index)
            state = 'A'

print(f'The answer = {data.count(1)}')
