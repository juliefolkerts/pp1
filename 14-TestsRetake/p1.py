def f(n):
    lst = list(str(n))
    odds = []
    for nr in lst:
        if int(nr)%2 != 0:
            odds.append(int(nr))
    result = -1
    if odds:
        result = max(odds)-min(odds)
    return result




if __name__ == '__main__':
    print(f(468888))