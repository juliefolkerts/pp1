def different(n1, n2, n3):
    if (n1 != n2 and n2 != n3 and n1 != n3):
        return True
    else:
        return False
    
n1 = int(input('Enter first number:\n'))
n2 = int(input('Enter second number:\n'))
n3 = int(input('Enter third number:\n'))


if different(n1, n2, n3):
    print(f'Numbers {n1}, {n2} and {n3} are different.') #why is this not printing?
