with open('file.txt', 'w') as file:
    num = 1
    for num in range(1,11):
        second_power = num**2
        third_power = num**3
        file.write(f'{num},{second_power},{third_power}\n')
        num += 1

with open('file.txt', 'r') as file:
    print(file.read())