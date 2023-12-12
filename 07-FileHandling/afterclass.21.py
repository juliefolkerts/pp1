with open('int.txt', 'w') as file:
    for current_int in range(1,51):
        file.write(f'{str(current_int)}\n')

with open('int.txt', 'r') as file:
    print(file.read())


