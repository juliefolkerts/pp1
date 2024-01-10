def f(fnc,res):
    lst = list(filter(fnc,res))
    result = max(lst)-min(lst)
    return result

if __name__ == '__main__':
    fnc1 = lambda x: x> 50
    res = [95,90,20,50,70]
    print(f(fnc1,res))
    fnc2 = lambda x: x>30 and x<90
    print(f(fnc2,res))
