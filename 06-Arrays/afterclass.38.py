def f(arr):
    num = int(input('Enternumber:\n'))
    count = 0
    for x in arr:
        if x > num:
            count += 1
        else:
            count = count
    return count

arr =[7,3,8,5,2]
print(f(arr))