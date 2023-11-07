def f(n):
    numbers = []
    for i in range(1, n+1):
        numbers.append(str(i))
    end = ''.join(numbers)
    return end 

result = f(11)
print(result)