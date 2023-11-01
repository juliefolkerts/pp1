def f(n1, n2, n3):
    if n1 < 0 or n2 < 0 or n3 < 0:
        return True
    else: 
        return False
    
n1 = int(input('Enter numbre 1:\n'))
n2 = int(input('ENter number 2:\n'))
n3 = int(input('Enter number 3:\n'))

print(f(n1, n2, n3))