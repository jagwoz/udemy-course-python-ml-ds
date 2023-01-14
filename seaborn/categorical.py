import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np


dataset = sb.load_dataset('tips')
print(dataset.head())

# sb.barplot(x='sex', y='total_bill', data=dataset, estimator=np.mean)  # default estimator is mean
# plt.savefig('plots_categorical/image_barplot.png')

# sb.countplot(x='time', data=dataset)
# plt.savefig('plots_categorical/image_countplot.png')

# sb.boxplot(x='day', y='total_bill', data=dataset, hue='smoker')
# plt.savefig('plots_categorical/image_boxplot.png')

# sb.violinplot(x='day', y='total_bill', data=dataset, hue='smoker', split=True)
# plt.savefig('plots_categorical/image_violinplot.png')

# sb.stripplot(x='day', y='total_bill', data=dataset, jitter=True, hue='sex')
# plt.savefig('plots_categorical/image_stripplot.png')

sb.violinplot(x='day', y='total_bill', data=dataset)
sb.swarmplot(x='day', y='total_bill', data=dataset, color='black')
plt.savefig('plots_categorical/image_swarmplot.png')

# factorplot with kind=
