import rangechecker

number = int(input('Enter number:'))
x = int(2)
y = int(16)

if rangechecker.check_range(number, x, y):
    print(f'Number {number} is in range {x, y}: yes')
else:
    print(f'Number {number} is in range {x, y}: no')