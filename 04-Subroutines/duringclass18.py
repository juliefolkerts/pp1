def numbers(n):
    result = ""
    for i in range(1, n+1):
        result += str(i)+" "
    return result

print(f'Numbers <1,15>: {numbers(15)}')
print(f'Numbers <1,7>: {numbers(7)}')