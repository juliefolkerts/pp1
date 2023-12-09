def f(arr):
    arr[0],arr[-1] = arr[-1], arr[0]
    return arr

arr = [
    [1,2,3,4,5],
    [1,2,2,2,5],
    [1,3,3,3,4]
]
print(arr)
print(f(arr))