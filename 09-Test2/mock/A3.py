def f(arr):
    count = 0
    for row in arr:
        count += row[0]
        count -= row[1]
    return count
arr = [[3,0],[6,1]]
print(f(arr))
