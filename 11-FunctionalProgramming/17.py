employees = ["SMITH Lucy","JONES Janet","LEE Jerry","JACKSON Peter","JOHNSON Rick","LEWIS Terry","CLARKE Robin"]

start_J = lambda surname: surname[0] == 'J'
result = list(filter(start_J,employees))

for person in result:
    print(person)