import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7])
y = x[:]
y[0] = 50
# plt.plot(x, y)

print(x)
