def f(n):
    if n == 0:
        return ''
    for i in range(1,n+1):
        txt = i * '*'
    end = '/'.join(txt)
    return end

result = f(4)
print(result)