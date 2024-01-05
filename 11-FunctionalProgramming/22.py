arr = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),("Jackson","Peter"),("Johnson","Rick"),("Lewis","Terry"),("Clarke","Robin")]

display_name = lambda name: f'{name[1].upper()}, {name[0]}'
result = list(map(display_name,arr))
for person in result:
    print(person)