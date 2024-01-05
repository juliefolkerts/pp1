eur = [15.90,38.47,4.07,132.70,9.15]

eur_pln = lambda x: x*4.5
result = list(map(eur_pln,eur))
for j in result:
    print(j)