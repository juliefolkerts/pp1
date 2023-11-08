def f(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    a = 0
    b = 1
    for i in range(3, n+1):
        a, b = b, a+b
    return b

result = f(5)
print(result)