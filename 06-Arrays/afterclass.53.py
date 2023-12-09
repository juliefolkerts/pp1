def identity_matrix(n):
    arr = []
    for i in range(0,n):
        row = [0]*n
        row[i] = 1
        arr.append(row)
    return arr

for row in identity_matrix(3):
    for value in row:
        print(value, end=' ')
    print()
print('')
for row in identity_matrix(5):
    for value in row:
        print(value, end=' ')
    print()
print('')
for row in identity_matrix(8):
    for value in row:
        print(value, end=' ')
    print()

