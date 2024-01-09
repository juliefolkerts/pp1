import matplotlib.pyplot as plt
import numpy as np

temps = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

x = list(temps.keys())
y = list(temps.values()) #how do I use map() for this?

plt.bar(x,y)
plt.xlabel('cities')
plt.ylabel('temps')
plt.show()