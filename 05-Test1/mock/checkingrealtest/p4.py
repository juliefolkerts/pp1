def f(n):
    n = str(n)
    result = ''
    for i in range(0, len(str(n))):
        if int(n[i]) % 2 == 0: #is even
            result += n[i] + '++'
        else:
            result += n[i] +  '+'
    if int(n[-1]) % 2 == 0:
        return result[:-2]
    else:
        return result[:-1]


endresult = f(1)
print(endresult)