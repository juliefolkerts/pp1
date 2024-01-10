def f(x,y,digit):
    count = 0
    arr = list(range(x,y+1))
    dig = str(digit)
    strarr = []
    for x in arr:
        for i in range(len(str(x))):
            strarr.append(str(str(x)[i]))
    for i in range(0,len(strarr)):
        if strarr[i] == dig:
            count+=1
    return count

print(f(100,105,6))
    




