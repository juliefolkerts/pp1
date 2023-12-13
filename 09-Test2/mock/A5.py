def f(password):
    result = False
    arr_password = list(password)
    if 12 >= len(arr_password) >= 4:
        if '_' in arr_password:
            if str(password) == str(password).lower():
                result = True
            else:
                result = False
    return result

password = 'abcd_iii'
print(f(password))