def f(arr):
    if arr[0] != arr[1] and arr[0] != arr[2]:
        result = arr[0]
    else:
        for i in range(1,len(arr)):
            if arr[i] != arr[0]:
                result = arr[i]
    return result

if __name__ == "__main__":
    print(f([7,7,7,7,7,5,7,7]))
    print(f([5,7,7,7,7,7]))