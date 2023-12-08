def f(arr):
    for i in range(0,len(arr)):
        row = []
        for j in range(1,6):
            row.append(int((i+1)*j))
        arr[i] = row
    return arr


arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
print(f(arr))

for row in arr:
    for value in row:
        print(value, end=' ')
    print()
        