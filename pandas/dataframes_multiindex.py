import pandas as pd
import numpy as np

level_2 = [i for i in range(1, 4)] * 3
level_1 = (['l1', 'l2', 'l3'] * 3)
level_1.sort()

indexes = list(zip(level_1, level_2))
indexes = pd.MultiIndex.from_tuples(indexes)

df = pd.DataFrame(np.random.randn(9, 2), indexes, ['c1', 'c2'])
print(df)

print(df.loc['l2'])

print(df.loc['l2'].loc[2])  # [column]

df.index.names = ['group', 'row']
print(df)

print(df.xs(1, level='row'))  # important
