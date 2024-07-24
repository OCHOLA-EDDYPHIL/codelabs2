import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 10, 400)  # From 1 to 10, to avoid log(0)
x_exp = np.linspace(0, 10, 400)  # Exponential function starts at 0

# Linear Function
plt.figure(figsize=(10, 6))
plt.plot(x, x, label='Linear: $f(x) = x$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Linear Function')
plt.legend()
plt.grid(True)
plt.show()

# Logarithmic Function
plt.figure(figsize=(10, 6))
plt.plot(x, np.log(x), label='Logarithmic: $f(x) = \log(x)$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Logarithmic Function')
plt.legend()
plt.grid(True)
plt.show()

# Exponential Function
plt.figure(figsize=(10, 6))
plt.plot(x_exp, 2**x_exp, label='Exponential: $f(x) = 2^x$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Exponential Function')
plt.legend()
plt.grid(True)
plt.show()

# Linearithmic Function
plt.figure(figsize=(10, 6))
plt.plot(x, x * np.log(x), label='Linearithmic: $f(x) = x \log(x)$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Linearithmic Function')
plt.legend()
plt.grid(True)
plt.show()

# Quadratic Function
plt.figure(figsize=(10, 6))
plt.plot(x, x**2, label='Quadratic: $f(x) = x^2$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Quadratic Function')
plt.legend()
plt.grid(True)
plt.show()
