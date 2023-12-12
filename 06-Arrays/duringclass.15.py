

def a(arr):
    sum = arr[0][0] + arr[1][2]
    return sum

def b(arr):
    sum = 0
    for i in range(0,len(arr)):
        sum += arr[i][1]
    return sum

def c(arr):
    sum = 0
    for i in range(0, len(arr[-1])):
        sum += arr[1][i]
    return sum
arr = [[1,3,5],[8,7,2]]
print(a(arr))
print(b(arr))
print(c(arr))