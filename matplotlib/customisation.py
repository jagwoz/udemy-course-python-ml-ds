import matplotlib.pyplot as plt
import numpy as np


range_v = np.linspace(0, 10, 10)
values = range_v ** 2 + 10

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(4, 4))

axes[0][0].plot(values, range_v, color='#FFAA11', label='y')
axes[0][1].plot(values, range_v, color='purple', linewidth=3, label='y')
axes[0][1].plot(-values, range_v, color='yellow', linewidth=2, label='-y', marker='o',
                markerfacecolor='red', markeredgewidth=1, markeredgecolor='green')
axes[1][0].plot(values, range_v, marker='1', color='blue', ls='dashed', label='y')
axes[1][0].plot(values, -range_v, marker='+', color='black', ls='-', label='y', lw=0.5, markersize=10)
axes[1][1].plot(range_v, values, color='red', lw=4, label='y')
axes[1][1].plot(range_v, values, color='#FFFFFF', lw=2, linestyle='--')
axes[1][1].plot(10 - range_v, values, color='green', lw=2, linestyle='-.', label='10-y')

axes[0][0].set_xlim()

for axes_col in axes:
    for axe in axes_col:
        axe.legend(loc=np.random.randint(0, 9))

plt.tight_layout()
plt.show()

fig.savefig('plots/image_customisation.png')
