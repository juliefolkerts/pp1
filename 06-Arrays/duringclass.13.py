thisarray = [34,7,19,4,21,8]
def f():
    count = 0
    x = 0
    while 0 <= x < len(thisarray):
        if ((thisarray[x]) % 2 == 0):
            count += 1
        x += 1
    return count
    
print(f())