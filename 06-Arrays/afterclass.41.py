def f(arr1, arr2):
    for x in arr1:
        if x not in arr2:
            return False
    return True
arr1 = [1,2,8]
arr2 = [1,2,3,4,5,6]
print(f(arr1, arr2))
