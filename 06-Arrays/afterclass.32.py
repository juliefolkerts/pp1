def occurs(number, array):
    if number in array:
        result = True
    else:
        result = False
    return result

array = [15, 38, 7, 23, 14]
number = 23

print(f'number:{array}')
print(f'number:{number}')
if occurs(number, array) ==True:
    print(f'number {number} appears in array')
else:
    print(f'number: {number} does not appear in array')
