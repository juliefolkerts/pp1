def f(detector):
    count = 0
    max_count = 0
    for i in range(0, len(detector)):
        if detector[i] == '+':
            count += 1
            max_count = max(max_count, count)
        elif detector[i] == '-':
            count -= 1
        else:
            count = count
    if max_count < 3:
        return False
    else:
        return True

result = f('+-++-++-+---')
print(result)