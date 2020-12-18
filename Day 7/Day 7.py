with open('input.txt') as f:
    lines = f.read().splitlines()

bots = []
tops = []

for line in lines:
    bots.append(line.split()[0])
    try:
        lst = line.split('-> ')[1]
        lst = lst.split(', ')
        for item in lst:
            tops.append(item)
    except IndexError:
        pass

for bot in bots:
    if tops.count(bot) == 0:
        print(f'bottom bot found --> {bot}')
