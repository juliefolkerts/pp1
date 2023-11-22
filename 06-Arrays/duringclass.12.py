thisarray = [34,7,19,4,21,8]
def f():
    count = 0
    for x in thisarray:
        if x % 2 == 0:
            count += 1
    return count
    
print(f())