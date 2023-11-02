def f(sentence):
    no_spaces = ""
    for char in sentence:
        if char != " ":
            no_spaces += char
    return no_spaces

result = f('Hello there, how are you?')
print(result)