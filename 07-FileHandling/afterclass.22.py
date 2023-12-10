with open('random.txt', 'w') as file:
    import random
    row_count = 0
    for row_count in range(0,51):
        file.write(f'{str(random.randint(100,999))}\n')
        row_count += 1
 
with open('random.txt', 'r') as file:
    print(file.read())