with open('input.txt') as f:
    lines = f.read().splitlines()


def find_nodes(val, lst):
    found = []
    for node in lst:
        if val in node:
            found.append(node)
    return found


data = []

for line in lines:
    val_1 = int(line.split('/')[0])
    val_2 = int(line.split('/')[1])
    data.append((val_1, val_2))

search_val = 0
search_vals = [search_val]
next_ports = [find_nodes(search_val, data)]
ports = []
analysed_ports = set()
answer = 0
len_path = 0
step = 0
while True:
    if len(next_ports) == 0:
        break
    if len(next_ports[-1]) > 0:
        temp_port = next_ports[-1][0]
        temp_ports = tuple(ports + [temp_port])
        if temp_ports not in analysed_ports:
            # Go to next level
            ports.append(temp_port)
            data.remove(temp_port)
            search_val = search_vals[-1]
            if temp_port[0] == search_val:
                search_val = temp_port[1]
            else:
                search_val = temp_port[0]
            search_vals.append(search_val)
            next_ports.append(find_nodes(search_val, data))
        else:
            # Path already analysed
            del next_ports[-1][0]
            pass
    else:
        # Calculate port length
        step += 1
        if len(ports) >= len_path:
            len_path = len(ports)
            cur_answer = 0
            for port in ports:
                for number in port:
                    cur_answer += number
            if cur_answer > answer:
                answer = cur_answer
        analysed_ports.add(tuple(ports))
        # return to previous level
        if len(ports) == 0:
            break
        data.append(ports[-1])
        del ports[-1]
        del search_vals[-1]
        del next_ports[-1]
        if step % 1000 == 0:
            print(f'At step {step}')

print(f'The answer is {answer}')


