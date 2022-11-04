import matplotlib.pyplot as plt
import numpy as np


range_v = np.linspace(0, 10, 10)
values = range_v ** 2 + 10

plt.subplot(1, 2, 1)
plt.plot(range_v, values)
plt.xlabel('range')
plt.ylabel('values')
plt.title('tittle')

plt.subplot(1, 2, 2)
plt.plot(values, range_v)
plt.xlabel('range')
plt.ylabel('values')
plt.title('tittle')

plt.show()
