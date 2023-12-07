def bubblesort(arr):
    x = len(arr)
    for i in range(0, x):
        for j in range(0, x-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

a = [6,3,8,0,4,9,8,6,7,34]
bubblesort(a)

print(f'sorted: {a}')