def f(text):
    if len(text) == 1:
        return text[0]
    else:
        return '-'.join(text[i] for i in range(0, len(text)))

    
result = f('UE')
print(result)