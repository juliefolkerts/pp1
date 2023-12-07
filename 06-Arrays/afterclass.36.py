def f(tuple, num):
    count = 0
    for x in range(0, len(tuple)):
        if tuple[x] == num:
            count += 1
    return count

tuple = (50,20,40,50,50,30)
num = 30

print(f'tuple: {tuple}')
print(f'number: {num}')
print(f'occurance: {f(tuple, num)}')