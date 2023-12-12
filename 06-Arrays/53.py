def f(arr):
    newarr = []
    for j in range(0,len(arr[0])):
        row = []
        for i in range(0,len(arr)):
            row.append(arr[i][j])
        newarr.append(row)
    return newarr
arr = [[1,2],[3,4],[5,6]]
print(f(arr))