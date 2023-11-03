def f(expression):
    first_number = int(expression[0])
    result = first_number
    for i in range(1,(len(expression)), 2): #shouldn't it be (len(expression)+1), because you want to include the last character aswell?
        operator = expression[i]
        number = int(expression[i+1])
        if operator == '+':
            result += number
        elif operator == '-':
            result -= number
    return result

awnser = f('2+3-4+5-0')
print(awnser)
        

