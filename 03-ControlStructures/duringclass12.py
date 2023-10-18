name_1 = input('Enter name first person:')
age_1 = int(input('Enter first person age:'))
name_2 = input('Enter name second person:')
age_2 = int(input('Enter second perosn age:'))
if age_1 >= 18 and age_2 >= 18:
    print(f'Both {name_1} and {name_2} are adults')