def f(binary_number):
    for digit in binary_number:
        if digit != '0' and digit != '1':
            return False
    return True
        
binary_number = input('Enter number:')

print(f(binary_number))
