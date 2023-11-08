def check_prime(x):
    if x == 2:
        return True
    elif x > 2:
        for i in range(2, (x-1)):
            if x % i == 0:
                return False
        return True
    else:
        return False

def f(n):
    count = 0
    x = 2
    while True:
        if check_prime(x):
            count += 1
            if count == n:
                return x
        x += 1

result = f(5)
print(result)