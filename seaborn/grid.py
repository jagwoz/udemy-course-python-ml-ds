import seaborn as sb
import matplotlib.pyplot as plt


dataset = sb.load_dataset('iris')
print(dataset.head())

print(dataset['species'].unique())

# pg = sb.PairGrid(dataset)
# pg.map_diag(sb.boxplot)
# pg.map_upper(sb.kdeplot)
# pg.map_lower(sb.rugplot)

# plt.savefig('plots_grid/pairgrid.png')


dataset = sb.load_dataset('tips')
fg = sb.FacetGrid(data=dataset, col='time', row='smoker')
fg.map(sb.histplot, 'total_bill')

plt.savefig('plots_grid/facetgrid.png')