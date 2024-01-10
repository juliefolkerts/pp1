def f(d):
    count = 0
    lst_value = list(d.values())
    total = sum(lst_value)
    average = total/len(lst_value)
    for x in lst_value:
        if x > average:
            count += 1
    return count
    



if __name__ == '__main__':
    print(f({'LO':150,'2':150,'3':150}))