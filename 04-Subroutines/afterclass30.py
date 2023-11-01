def f(number, even):
    digit_sum = 0
    for digit in str(number):
        digit = int(digit)
        if (even == True and digit % 2 == 0) or (even == False and digit % 2 != 0):
            digit_sum += digit
    return digit_sum

result = f(3124, True)
print(result)

        


    #for digit in number:
        #if (digit % 2 = 0) 