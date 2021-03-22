import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 3, 1])
y = np.array([1, 2, 2, 1, 1])
plt.plot(x, y, '-', linewidth=1.5, markersize=10)
plt.axis([0, 4, 0, 4])
plt.title('vjezba')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
