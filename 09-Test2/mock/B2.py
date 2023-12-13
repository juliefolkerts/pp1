def f(d):
    arrd = list(d)
    count = 0
    for i in range(0,len(arrd)):
        if arrd[i] == '+':
            count += 1
        else:
            count -= 1
    return count

if __name__ == '__main__':
    d1 = '+-+++-+---'
    d2 = '+-+++++-'
    print(f(d1))
    print(f(d2))