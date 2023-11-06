def f():
    correctpin = '0805'
    attempts = 0
    while attempts < 3:
        code = input('Enter code:')
        if code == correctpin:
            return 'correct pincode!'
            break
        else:
            print('incorrect pin')
            attempts += 1

    if attempts == 3:
        print('No more tries')

f()

