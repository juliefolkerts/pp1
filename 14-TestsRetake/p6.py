def f(fnc,res):
    lst = list(filter(fnc,res))
    result = max(lst)-min(lst)
    return result
