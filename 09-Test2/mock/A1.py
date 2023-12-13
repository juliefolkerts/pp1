def f(n):
    def perfect_sq(num): #first check if the number is a perfect square(otherwise it isn't fibonacci)
        sqroot = int(num**0.5)
        if sqroot**2 == num:
            result = True
        else:
            result = False
        return result
    num = 5 * n**2 + 4 #this is the formula to check if a number is in the fibonacci sequence
    num2 = 5 * n**2 - 4 #one of these needs to be true
    if perfect_sq(num) == True or perfect_sq(num2) == True: 
        result = True #check if it is perfect square AND if the formula works
    else:
        result = False
    return result

