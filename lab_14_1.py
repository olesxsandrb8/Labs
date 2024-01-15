import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x * np.sin(5 * x)

x_values = np.linspace(-2, 5, 1000)

y_values = func(x_values)

plt.plot(x_values, y_values, label='Y(x) = x*sin(5*x)', color='blue', linestyle='-', linewidth=2)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Графік функції Y(x) = x*sin(5*x)')

plt.legend()

plt.grid(True)
plt.show()
