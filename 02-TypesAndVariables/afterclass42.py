binary_nr = input('Enter binary number:')
decimal_nr = 0
m = 1
for digit in binary_nr:
    digit = int(digit)
    decimal_nr = decimal_nr + (digit * m)
    m = m * 2
print('Decimal value:', decimal_nr)