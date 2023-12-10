with open('int.txt', 'w') as file:
    current_int = 1
    for current_int in range(1,51):
        file.write(f'{str(current_int)}\n')

with open('int.txt', 'r') as file:
    print(file.read())