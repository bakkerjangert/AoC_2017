judge_a = 783
judge_b = 325

# Test
# judge_a = 65
# judge_b = 8921

factor_a = 16807
factor_b = 48271

divider = 2147483647

answer = 0

for i in range(40000000):
    judge_a = (judge_a * factor_a) % divider
    judge_b = (judge_b * factor_b) % divider
    bin_a = '{0:b}'.format(judge_a)
    bin_b = '{0:b}'.format(judge_b)
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

print(f'The answer is {answer}')

