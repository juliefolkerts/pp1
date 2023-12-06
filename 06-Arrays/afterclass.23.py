numbers = [-15, 8, -31, 47, -2, 19]

minnum = float('inf')
maxnum = float('-inf')

for x in numbers:
    if x > maxnum:
        maxnum = x
    if x < minnum:
        minnum = x

print(f'maximum value:{maxnum}')
print(f'minimum value:{minnum}')