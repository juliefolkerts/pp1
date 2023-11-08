def f(name):
    words = name.split()
    for i in words:
        acronym = ''.join(i[0])
    return acronym

result = f("For Your Info")
print(result)

