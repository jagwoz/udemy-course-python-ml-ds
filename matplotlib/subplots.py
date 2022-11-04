import matplotlib.pyplot as plt
import numpy as np


range_v = np.linspace(0, 10, 10)
values = range_v ** 2 + 10

fig, axes = plt.subplots(nrows=1, ncols=2)

for actual_ax in axes:
    actual_ax.plot(range_v, values, 'g-')
axes[1].plot(values, range_v, 'r*')


plt.tight_layout()
plt.show()
