def f(d,v):
    count = 0
    for key in d:
        if d[key] != v:
            count += 1
        else:
            count = count
    return count

if __name__ == '__main__':
    d1 = {
        'a' : True,
        'b' : False,
        'c' : True,
        'd' : True,
        'e' : True
    }
    v1 = True
    d2 = d1
    v2 = False
    print(f(d1,v1))
    print(f(d2,v2))