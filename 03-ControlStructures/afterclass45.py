def primenumbers(N):
    for i in range(2, int(N*0.5)):
        if N % i == 0:
            return False
    return True

def reeksprimes():
    num = 2
    if primenumbers(num):
        print(num, end=' ')
        num += 1

result = primenumbers(int(4))
print(result)
