def transpose_matrix(arr):
    newarr = []
    for y in range(0,len(arr[0])):
        newrow = []
        for x in range(0,len(arr)):
            newrow.append(arr[x][y])
        newarr.append(newrow)
    return newarr

arr = [
    [1,2],
    [3,4],
    [5,6]
]
print(transpose_matrix(arr))


