with open('input.txt') as f:
    lines = f.read().splitlines()


def find_uniques(lsts):
    uniques = []
    for line in lsts:
        if line[0] not in uniques:
            uniques.append(line[0])
    return uniques

def increase_step(lsts, bot):
    sequences = []
    for line in lsts:
        if line[0] == bot:
            sequences.append(line[1:])
    return sequences

def values(lsts, uniques, bots):
    values = {}
    for bot in uniques:
        sub_bots = []
        for line in lsts:
            if line[0] == bot:
                for sub_bot in line:
                    sub_bots.append(sub_bot)
        sub_bots = tuple(set(sub_bots))
        value = 0
        for sub_bot in sub_bots:
            value += bots[sub_bot][0]
        values[bot] = value
    return values



bots = {}
start_bot = 'eqgvf'

for line in lines:
    val = line.split('(')[1]
    val = int(val.split(')')[0])
    lst = []
    try:
        lst = line.split('-> ')[1]
        lst = lst.split(', ')
    except IndexError:
        pass
    bots[line.split()[0]] = (val, tuple(lst))

sequences = []

for bot in bots.keys():
    prop = bots[bot]
    if len(prop[1]) == 0:  # End of line; reconstruct
        sequence = []
        search_bot = bot
        while search_bot != start_bot:
            for k, v in bots.items():
                if search_bot in v[1]:
                    sequence.append(search_bot)
                    search_bot = k
                    break
        sequence.append(search_bot)
        sequences.append(tuple(reversed(sequence)))

sequences = sorted(sequences)
sequences_org = sequences.copy()
# sequences = increase_step(sequences, start_bot)

cur_bot = start_bot
diff = 0

while True:
    sequences = increase_step(sequences, cur_bot)
    uniques = find_uniques(sequences)
    print(uniques)
    val = values(sequences, uniques, bots)
    check_val = tuple(set(list(val.values())))
    print(check_val)
    if len(check_val) == 1:
        # Cur bot is deviating
        print(f'The answer is {bots[cur_bot][0] - diff}')
        exit()
    if diff == 0:
        if list(val.values()).count(check_val[0]) == 1:
            diff = check_val[0] - check_val[1]
        else:
            diff = check_val[1] - check_val[0]
    if list(val.values()).count(check_val[0]) == 1:
        dev_val = check_val[0]
    else:
        dev_val = check_val[1]
    for k, v in val.items():
        if v == dev_val:
            cur_bot = k
            break


