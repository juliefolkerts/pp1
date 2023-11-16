def f(bc):
    x = len(bc)
    if x == 13 and bc[0:3] == '590':
        return True
    return False

result = f('5901234567890')
print(result)