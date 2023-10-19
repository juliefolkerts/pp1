first_number = int(input('Enter first number:\n'))
second_number = int(input('Enter second number:\n'))
if first_number < second_number:
    print(f'Numbers in ascending order: {first_number}, {second_number}')
elif second_number < first_number:
    print(f'Numbers in ascending order: {second_number}, {first_number}')
else:
    print('Numbers have the same value')
