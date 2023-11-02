def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a = 0
        b = 1
        for i in range(3, n+1):
            a, b = b, a + b
        return b
    
result = f(9)
print(result)








#def f(n):
    #if n <= 0:
        #return 0
    #elif n == 1:
        #return 1
    #else:
        #return f(n - 1) + f(n - 2)
    
#result = f(9)
#print(result)