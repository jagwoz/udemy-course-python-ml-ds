import matplotlib.pyplot as plt
import numpy as np


range_v = np.linspace(0, 10, 10)
values = range_v ** 2 + 10

fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.3, 0.3])

axes.plot(range_v, values, 'r*')
axes2.plot(values, range_v)

axes.set_title('first plot')
axes2.set_xlabel('x label')

plt.show()
