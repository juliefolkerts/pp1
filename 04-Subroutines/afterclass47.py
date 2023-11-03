def f(text):
    if len(text) == 1:
        return text[0]
    for i in range(1, len(text)):
        result = (text[i],'-')
    return result

end_result = f('Univesity')
print(end_result)
    #use join function and split function**