def f(arr):
    for x in range(0,len(arr)):
        if arr[x] < 10:
            arr[x] = '   ' + str(arr[x])
        elif 100 > arr[x] > 9:
            arr[x] = '  ' + str(arr[x])
        else:
            arr[x] = ' ' + str(arr[x])
    return '|'.join(map(str, arr))


upperline = '-'*41
lowerline = '-'*41
arr = [1,23,5,382,1,17,4,906]
print(upperline)
print(f'|{f(arr)}|')
print(lowerline)


