import seaborn as sb
import matplotlib.pyplot as plt


dataset = sb.load_dataset('tips')
# print(dataset.head())

# sb.displot(dataset['total_bill'], kde=True)
# plt.savefig('plots/image_displot.png')

# sb.jointplot(data=dataset, x='total_bill', y='tip', kind='hex')
# sb.jointplot(data=dataset, x='total_bill', y='tip', kind='reg')
# plt.savefig('plots/image_joinplot_reg.png')

# sb.pairplot(dataset, hue='sex')
# plt.savefig('plots/image_pairplot.png')

sb.rugplot(dataset['total_bill'])
plt.savefig('plots/image_rugplot.png')