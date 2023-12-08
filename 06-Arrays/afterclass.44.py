import matplotlib.pyplot as plt

x = []
y = []

for n in range(-100,101):
    x = x + [n]

for n in x:
    y = y + [(n**2) -3]

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x) = x^2 - 3')
plt.grid(True)
plt.show()

