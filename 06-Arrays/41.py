def f(arr1,arr2):
    result = 0
    for num in arr1:
        if num in arr2:
            result += 1
        else:
            result = result
    if len(arr1) == result:
        return True
    else:
        return False
        

arr1 = [1,2,3]
arr2 = [1,2,3,4,5]
print(f(arr1,arr2))