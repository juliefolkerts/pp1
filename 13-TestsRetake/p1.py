def f(n):
    n = str(n)
    arr = list(n)
    odds = []
    for nr in arr:
        if int(nr)%2 != 0:
            odds.append(int(nr))
    if odds:
        minimum = min(odds)
        maximum = max(odds)
        result = maximum - minimum
    else:
        result = -1
    return result

if __name__ == '__main__':
    print(f(84693))