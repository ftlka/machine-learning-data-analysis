import numpy as np
from scipy.optimize import minimize
from matplotlib import pyplot as plt
from scipy.optimize import differential_evolution


def func(x):
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)


def h(x):
    return func(x).astype(int)


# gets stuck in local extremums
first_method = minimize(func, [30], method='BFGS')

# did not get stuck, small amount of iterations but lots of nfev
second_method = differential_evolution(func, [(1, 30)])

# bfgs of int function
second_func_bfgs = minimize(h, [30], method='BFGS')
print(second_func_bfgs)

# dif evolution of int function
second_func_dif_ev = differential_evolution(h, [(1, 30)])


x_range = np.arange(1, 30.1, 0.01)
y_range = np.array(func(x_range))
y_int_range = np.array(h(x_range))

plt.plot(x_range, y_range, color='r')
plt.plot(x_range, y_int_range, color='b')

plt.show()
