def f(n):
    endresult = []
    for i in range(1, n + 1):
        endresult.append(str(i))
    return ''.join(endresult)

result = f(11)
print(result)