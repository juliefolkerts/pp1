def create_2d_arr(x,y):
    row = []
    for k in range(0,x):
        row.append(0)
        k += 1
    arr = []
    for j in range(0,y):
        arr.append(row)
    return arr

print(create_2d_arr(3,5))

for row in create_2d_arr(3,5):
    for value in row:
        print(value, end=' ')
    print()