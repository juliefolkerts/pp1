def f(arr):
    for i in range(0,len(arr)):
        for j in range(0, len(arr[i])):
            arr[i][j] = arr[j][i]
arr = [[1,2],[3,4],[5,6]]
print(f(arr))