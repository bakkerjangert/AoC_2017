import sympy

# Note --> See part_2.txt

b = 106700
c = 123700
delta = 17

numbers = []
for i in range(b, c + delta, delta):
    numbers.append(i)

# print(f'{len(numbers)}, {numbers[-1]}')

answer = 0
for number in numbers:
    if not sympy.isprime(number):
        answer += 1

print(f'The answer is {answer}')
