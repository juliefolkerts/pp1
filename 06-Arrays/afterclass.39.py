def f(arr):
    evennum = []
    oddnum = []
    for x in arr:
        if x % 2 == 0:
            evennum.append(x)
        else:
            oddnum.append(x)
    evennum.extend(oddnum)
    return evennum

arr =[7,3,8,5,2]
print(f(arr))