def f(arr):
    if arr[0] != arr[1] and arr[0] != arr[2]:
        result = arr[0]
    for i in range(1,len(arr)):
        if arr[0] != arr[1] and arr[0] != arr[2]:
            result = arr[0]
        else:
            if arr[i] != arr[0]:
                result = arr[i]
    return result

if __name__ == '__main__':
    arr = [7,7,7,7,7,7,7,7,5]
    arr2 = [7,5,7,7]
    print(f(arr))
    print(f(arr2))