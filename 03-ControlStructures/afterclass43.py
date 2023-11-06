def fibon(x):
    if x == 1:
        return 0
    if x == 2:
        return 1
    if x > 2:
        return fibon(x-1) + fibon(x-2)
 
def fibon20():
    for i in range(1,21):
        print(fibon(i), end=' ')

fibon20()