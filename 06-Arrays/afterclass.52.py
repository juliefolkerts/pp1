
def f(arr):
    for row in arr:
        row[0], row[-1] = row[-1], row[0]
    return arr

arr = [
    [1,2,3,4,5],
    [1,2,2,2,5],
    [1,3,3,3,4]
]
print(arr)
print(f(arr))