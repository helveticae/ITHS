import math
import matplotlib.pyplot as plt

f = lambda x: x**2
y = [f(x) for x in range(-5,6)]
x = range(-5,6)

plt.plot(x,y)
plt.show()