def f(name):
    list_of_words = name.split()
    acronym = ''
    for word in list_of_words:
        acronym += word[0]
    return acronym
    

if __name__ == "__main__":
    result = (f('Internet of Things'))
    print(result)
    result = f("For Your Information")
    print(result)
    result = f("Python")
    print(result)
