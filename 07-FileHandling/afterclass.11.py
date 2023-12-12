with open("numbers.txt", "w") as file:
    file.write('11\n')
    file.write('9\n')
    file.write('23\n')
    file.write('7\n')
    file.write('2\n')

with open('numbers.txt', 'r') as file:
    content = file.read()
    print(content)

with open("numbers.txt", 'r') as file:
    numbers = []
    for line in file:
        numbers.append(int(line.strip()))

sum_numbers = sum(numbers)

print(f'Numbers:{' '.join(map(str, numbers))}')
print(f'Sum:{sum_numbers}')