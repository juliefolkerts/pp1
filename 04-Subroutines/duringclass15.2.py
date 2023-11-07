def keypad():
    for i in range(1,10):
        if i % 3 != 0:
            print(i, end=' ')
        else:
            print(i)

keypad()