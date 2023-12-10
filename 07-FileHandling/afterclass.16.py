def f():
    filename = input('Enter file name:')
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            count += 1
    return count

result = f()
print(f'Number of lines:{result}')