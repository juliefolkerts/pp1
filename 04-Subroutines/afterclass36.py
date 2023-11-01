def f(detector):
    count = 0
    for digit in str(detector):
        if digit == '+':
            count += 1
    if count >= 3:
        return True

result = f('+-++-+--+')
print(result)