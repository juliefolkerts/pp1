def f(n):
    answer = -1
    lst = list(str(n))
    odds = []
    for nr in lst:
        if int(nr)%2 !=0:
            odds.append(int(nr))
    if odds:
        answer = max(odds)-min(odds)
    return answer

if __name__ == '__main__':
    print(f(4488620))