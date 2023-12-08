import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

for n in range(0,360):
     x = x + [n]

x_rad = np.radians(x)
y = np.sin(x_rad)

plt.plot(x, y)
plt.xlabel('Angle (degrees)')
plt.ylabel('sin(x)')
plt.title('Graph of y = sin(x)')
plt.grid(True)
plt.show()