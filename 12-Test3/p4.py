def f(fnc,prods):
    arr = list(map(fnc,prods))
    result = ','.join(arr)
    return result

if __name__=='__main__':
    fnc1 = lambda x: 'id:'+x[:2]
    prods=['water','cheese','tomato']
    print(f(fnc1,prods))
    fnc2=lambda x:(x[0]+x[-1]).upper()
    print(f(fnc2,prods))