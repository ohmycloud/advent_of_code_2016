from collections import Counter

with open('./06 - Signals and Noise.txt', 'r') as infile:
    noise = infile.read().split('\n')

columns = (''.join(column) for column in zip(*noise))

first_solution = ''
second_solution = ''

for column in columns:
    (most, _), *others, (least, _) = Counter(column).most_common()
    first_solution += most
    second_solution += least

print("The message usually consists of the most frequent letters....")
print("Then it must be:", first_solution)
print("....")
print("Or is it the least frequent letters? I never know....")
print("It might be then", second_solution)