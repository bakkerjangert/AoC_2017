goal = 325489

# Directions
# 0 -->  ->
# 1 -->  ^^
# 2 -->  <--
# 3 -->  vv

x = 0
y = 0

x_max = 0
x_min = 0
y_max = 0
y_min = 0

dir = 0

value = 1

while True:
    # print(f'Value {value} at x = {x} and y = {y}')
    if dir == 0:
        x += 1
        if x > x_max:
            x_max = x
            dir += 1
    elif dir == 1:
        y += 1
        if y > y_max:
            y_max = y
            dir += 1
    elif dir == 2:
        x -= 1
        if x < x_min:
            x_min = x
            dir += 1
    elif dir == 3:
        y -= 1
        if y < y_min:
            y_min = y
            dir = 0
    value += 1
    if value == goal:
        break

print(f'the answer = {abs(x) + abs(y)}')
