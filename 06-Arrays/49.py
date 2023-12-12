arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
def f(arr):
    for i in range(0, len(arr)):
        for j in range(0,len(arr[i])):
            arr[i][j] = (i+1)*(j+1)
    return arr

print(f(arr))