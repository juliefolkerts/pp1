def f(text):
    result = ''
    for i in range(0, len(text)):
        result += text[i]+ '-'
    return result

result = f('UE')
print(result)