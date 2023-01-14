import seaborn as sb
import matplotlib.pyplot as plt
import scipy


dataset = sb.load_dataset('tips')
dataset2 = sb.load_dataset('flights')
print(dataset2.head())

dataset_corr = dataset.corr(numeric_only=True)

# sb.heatmap(dataset_corr, annot=True, cmap='coolwarm')
# plt.savefig('plots_matrix/heatmap.png')

dataset2 = dataset2.pivot_table(index='month', columns='year', values='passengers')
# sb.heatmap(dataset2, cmap='magma')
# sb.heatmap(dataset2, cmap='magma', linecolor='black', linewidths=2)
# plt.savefig('plots_matrix/heatmap_ds2.png')

sb.clustermap(dataset2, cmap='coolwarm', standard_scale=1)
plt.savefig('plots_matrix/clustermap_ds2.png')
