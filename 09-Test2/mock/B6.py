import re

def f(t):
    arr = t.split()
    all = re.findall(fr'\d+', t)
    total = 0
    for num in all:
        total += int(num)
    return total

    

if __name__ == '__main__':
    t1 = '11 and 4 is 15'
    t2 = 'Water12, and 3play is not 8'
    print(f(t1))
    print(f(t2))