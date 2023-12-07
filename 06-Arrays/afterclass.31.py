
def f(arr):
    newarr = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                break
        else:
            newarr.append(arr[i])
    return newarr

arr = [2,3,2,5,8,1,9,8]

print(f'unique items:{f(arr)}')