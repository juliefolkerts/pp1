def f(n):
    count = 0
    for digit in n:
        frequencynumber = n.count(digit)
        if frequencynumber > 1: