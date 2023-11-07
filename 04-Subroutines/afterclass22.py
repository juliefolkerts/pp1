def month(n):
    if n == 1:
        n = 'January'
    elif n == 2:
        n = 'Febuary'
    elif n == 3:
        n = 'March'
    else:
        return 'I only know the first three months'
    return n

n = int(input('Enter month number:\n'))
print(f'The name of month {n} is {month(n)}')