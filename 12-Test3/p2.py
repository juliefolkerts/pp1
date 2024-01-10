def f(x,y,digit):
    count = 0
    arr = list(range(x,y+1))
    dig = str(digit)
    strarr = []
    for b in arr:
        for i in range(len(str(b))):
            strarr.append(str(str(b)[i]))
    for i in range(0,len(strarr)):
        if strarr[i] == dig:
            count+=1
    return count


    




