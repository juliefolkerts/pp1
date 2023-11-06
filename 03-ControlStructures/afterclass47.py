def lottery():
    for i in range(1, 8):
        for j in range(i, 50, 7):
            if j < 10:
                print('',j, end= ' ')
            else:
                print(j, end=' ')
        print()

lottery() 