def f(arr):
    arr1d = []
    for row in range(0,len(arr)):
        for i in range(len(arr[row])):
            arr1d.append(arr[row][i])
    return arr1d

arr= [
    [2,3],
    [1,5]
]

print(f(arr))
