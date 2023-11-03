def power(x, n):
    # Base case: x^0 is 1
    if n == 0:
        return 1
    # Recursive case: x^n = x * x^(n-1)
    else:
        return x * power(x, n - 1)

result = power(5, 3)
print(result)


#Tip: x**n =  x * x**n-1