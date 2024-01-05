import matplotlib.pyplot as plt

dic = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

cities = list(dic.keys())
temps = list(dic.values())

plt.bar(cities,temps)
plt.xlabel('cities')
plt.ylabel('Temps')

plt.show()
