def f(password):
    password = password.lower()
    lengt_password = int(len(password))
    for i in password:
        frequency = password.count(i)
        if frequency > 1:
            lengt_password = (lengt_password - frequency + 1)
        else:
            lengt_password = lengt_password
    if lengt_password >= 6:
        return True
    else:
        return False

result = f('1234BB')
print(result)
    
        