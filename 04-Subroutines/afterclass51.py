def sum(n):
    count = 0
    for i in range(0, n):
        if (i % 1 == 0) and (i >= 0):
            count += i
    return count

result = sum(6)
print(result)
#try it wih recursion

