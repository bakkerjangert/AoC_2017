judge_a = 783
judge_b = 325

# Test
# judge_a = 65
# judge_b = 8921

factor_a = 16807
factor_b = 48271

divider = 2147483647

answer = 0
judge_a_lst = []
judge_b_lst = []
compare = 0
while compare < 5000000:
    if len(judge_a_lst) > 50:
        pass
    else:
        judge_a = (judge_a * factor_a) % divider
        if judge_a % 4 == 0:
            judge_a_lst.append(judge_a)
    if len(judge_b_lst) > 50:
        pass
    else:
        judge_b = (judge_b * factor_b) % divider
        if judge_b % 8 == 0:
            judge_b_lst.append(judge_b)
    if len(judge_a_lst) > 0 and len(judge_b_lst) > 0:
        compare += 1
        if compare % 10000 == 0:
            print(f'At {round(compare/5000000 * 100, 1)}%')
        bin_a = '{0:b}'.format(judge_a_lst[0])
        bin_b = '{0:b}'.format(judge_b_lst[0])
        if len(bin_a) < 16:
            bin_a = '0' * (16 - len(bin_a)) + bin_a
        else:
            bin_a = bin_a[-16:]
        if len(bin_b) < 16:
            bin_b = '0' * (16 - len(bin_b)) + bin_b
        else:
            bin_b = bin_b[-16:]
        if bin_a == bin_b:
            answer += 1
        del judge_a_lst[0]
        del judge_b_lst[0]


print(f'The answer is {answer}')

