import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 4), ['a', 'b', 'c', 'd', 'e'], ['z', 'y', 'x', 'w'])
print(df)
df = pd.DataFrame(np.random.randn(20).reshape(5,4), ['a', 'b', 'c', 'd', 'e'], ['z', 'y', 'x', 'w'])
print(df)

# print(df['z'])
df['new'] = df['y'] + df['z']

df.drop('w', axis=1, inplace=True)
df.drop('a', inplace=True)
print(df)

# print(df.loc['b'])
# print(df.iloc[2])
print(df.loc[['c', 'd'], ['y', 'x']])
