with open('input.txt') as f:
    lines = f.read().splitlines()

walk = lines[0].split(',')

N = 0.
E = 0

max_dist = 0

for choice in walk:
    if choice == 'n':
        N += 1.
    elif choice == 's':
        N -= 1.
    elif choice == 'ne':
        N += 0.5
        E += 1
    elif choice == 'nw':
        N += 0.5
        E -= 1
    elif choice == 'se':
        N -= 0.5
        E += 1
    elif choice == 'sw':
        N -= 0.5
        E -= 1
    else:
        print(f'Error, input not understood')
    cur_dist = abs(E) + abs(N) - 0.5*abs(E)
    if cur_dist > max_dist:
        max_dist = cur_dist


print(f'final position --> N = {N} and E = {E}')
print(f'It takes {abs(E) + abs(N) - 0.5*abs(E)} steps to go home (part 1)')
print(f'The maximum distance away is {max_dist} (part 2)')
