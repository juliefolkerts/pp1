def f(name):
    words = name.split()
    acronym = ''.join(i[0] for i in words)
    return acronym

result = f("For Your Info")
print(result)

