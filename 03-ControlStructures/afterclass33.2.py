#a.	Read a decimal number from the keyboard.
#b.	Divide the number by 2 and note the remainder.
#c.	Divide the quotient obtained by 2 and note the remainder.
#d.	Repeat the same process till we get 0 as the quotient.
#e.	Write the values of all the remainders starting from the bottom to the top. That will be the required binary number.
def binary(n):
    n = int(n)
    listbin = []
    while n > 0:
        b = n % 2 #b
        listbin.append(str(b)) #because making it into a string, it is possible to join them together
        n = n // 2
    listbin.reverse()
    endresult = ''.join(listbin) #join function only works for strings
    return endresult
    

result = binary(8)
print(result)