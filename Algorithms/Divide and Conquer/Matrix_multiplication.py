import numpy as np

# Initialize the matrices
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
z = np.zeros((2, 2))

print("The first matrix is:")
print(x)
print("\nThe second matrix is:")
print(y)

# Strassen's Algorithm calculation
m1 = (x[0, 0] + x[1, 1]) * (y[0, 0] + y[1, 1])
m2 = (x[1, 0] + x[1, 1]) * y[0, 0]
m3 = x[0, 0] * (y[0, 1] - y[1, 1])
m4 = x[1, 1] * (y[1, 0] - y[0, 0])
m5 = (x[0, 0] + x[0, 1]) * y[1, 1]
m6 = (x[1, 0] - x[0, 0]) * (y[0, 0] + y[0, 1])
m7 = (x[0, 1] - x[1, 1]) * (y[1, 0] + y[1, 1])

# Combine the results into matrix z
z[0, 0] = m1 + m4 - m5 + m7
z[0, 1] = m3 + m5
z[1, 0] = m2 + m4
z[1, 1] = m1 - m2 + m3 + m6

print("\nProduct achieved using Strassen's algorithm:")
print(z)



