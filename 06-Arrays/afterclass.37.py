def a(arr):
    x = max(arr)
    arr.remove(x)
    return max(arr)

arr =[7,3,8,5,2]
print(a(arr))

def b(arr):
    x = max(arr)
    y = min(arr)
    z = x - y
    return z

arr =[7,3,8,5,2]
print(b(arr))

def c(arr):
    sorted_arr = sorted(arr)
    x = len(arr)
    if x % 2 != 0:
        index = x // 2 
        median = sorted_arr[index]
    else:
        index = x // 2
        median = (sorted_arr[index-1] + sorted_arr[index]) / 2
    return median

arr =[7,3,8,5,2]
print(c(arr))

def d(arr):
    x = max(arr)
    y = min(arr)
    z = [y,x]
    return z

arr =[7,3,8,5,2]
print(d(arr))

def e(arr):
    result = '-'.join(map(str, arr))
    return (result)

arr =[7,3,8,5,2]
print(e(arr))
