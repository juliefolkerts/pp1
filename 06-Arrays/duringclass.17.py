arr = [[0,0,0],[0,0,0],[0,0,0]]

for x in range(0,3):
    for y in range(0,3):
        if x == y:
            arr[x][y] = 1

arr2D = arr
for row in arr2D:
    print(''.join(map(str, row)))