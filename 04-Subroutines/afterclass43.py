def f(name):
    words = name.split()
    acronym = ''.join(word[0] for word in words)
    return acronym

result = f("For Your Info")
print(result)

