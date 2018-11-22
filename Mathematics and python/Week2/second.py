import numpy as np
from scipy.linalg import solve
from matplotlib import pyplot as plt


def get_y(x):
    return np.sin(x / 5.0) * np.exp(x / 10.0) + 5.0 * np.exp(-x / 2.0)

# original
x_range = np.arange(1, 15.1, 0.01)
y_range = np.array(get_y(x_range))

plt.plot(x_range, y_range, color='r')

# linear
A = np.array([[1, 1], [1, 15]])
y = np.array([get_y(1), get_y(15)])
w0, w1 = solve(A, y)

plt.plot(x_range, w0 + w1*x_range, color='g')

# quadratic
A = np.array([[1, 1, 1,], [1, 8, 8**2], [1, 15, 15**2]])
y = np.array([get_y(1), get_y(8), get_y(15)])
w0, w1, w2 = solve(A, y)

plt.plot(x_range, w0 + w1*x_range + w2 * x_range**2, color='y')

# cubic
A = np.array([
    [1, 1, 1, 1],
    [1, 4, 4**2, 4**3],
    [1, 10, 10**2, 10**3],
    [1, 15, 15**2, 15**3]
])
y = np.array([get_y(1), get_y(4), get_y(10), get_y(15)])
w0, w1, w2, w3 = solve(A, y)

print(round(w0, 2), round(w1, 2), round(w2, 2), round(w3, 2))

plt.plot(x_range, w0 + w1 * x_range + w2 * (x_range**2) + w3 * (x_range**3), color='b')


plt.show()