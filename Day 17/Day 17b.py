def run(data, steps, start):
    val = max(data) + 1
    index = (start + steps) % len(data) + 1
    data.insert(index, val)
    return data, index


puzzle_input = 369

data = [0, 1]
start = 1
step = 1
steps = 50000000 - step
found_val = [1]
for i in range(steps):
    length = step + 1
    if (puzzle_input + start) % length == 0:
        # next value found
        start = 1
        found_val.append(step + 1)
        step += 1
        print(found_val[-1])
    else:
        start = (puzzle_input + start) % length + 1  # after insertion start position + 1
        step += 1

