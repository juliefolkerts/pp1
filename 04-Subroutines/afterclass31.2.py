def f(x, y):
    count = 0
    for i in range(x, y+1):
        if i < 0 and (i%2==0):
            count += 1
    return count

result = f(-1, 11)
print(result)