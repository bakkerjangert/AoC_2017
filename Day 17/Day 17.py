def run(data, steps, start):
    val = max(data) + 1
    index = (start + steps) % len(data) + 1
    data.insert(index, val)
    return data, index


puzzle_input = 369

data = [0]
start = 0

for i in range(2017):
    temp_val = run(data, puzzle_input, start)
    data = temp_val[0]
    start = temp_val[1]

print(data[start+1])



