def f(arr):
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    result = []
    for key in count:
        if int(count[key]) % 2 != 0:
            result.append(int(key)) 
    return result

arr = [7,7,7,7,4,4,4,5,5]
print(f(arr))
