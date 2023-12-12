
def f(arr):
    count = 0
    i = 0
    while i < len(arr):
        if (int(arr[i]) % 2) == 0:
            count += 1
        else:
            count = count
        i += 1
    return count

arr = [34,7,19,4,21,8]
print(f(arr))