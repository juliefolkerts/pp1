def lottery():
    for i in range(1, 50, 7):
        for j in range(i, i + 7):
            print(j, end=' ')
        print()

lottery()