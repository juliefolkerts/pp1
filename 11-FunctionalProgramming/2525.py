temps = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}


cities = list(filter(lambda x: temps[x]>0,temps))
print(f'Cities with positive temperatures: {' '.join(cities)}')