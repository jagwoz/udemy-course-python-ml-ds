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

print(df > 0)
print(df[df > 0])

print(df[df['z'] > 0])  # important

print(df[(df['z'] < 0) & (df['y'] > 0.4)])  # | - or

df.reset_index(inplace=True)
print(df)

new_column = '0.5 0.4 0.1 0.15'.split()
df['new_column'] = new_column
print(df)

new_df = pd.DataFrame({'a': [np.nan, 1.0, 2.0], 'b': [1.0, np.nan, np.nan]})
print(new_df)

for column in new_df:
    new_df[column].fillna(value=new_df[column].mean(), inplace=True)
print(new_df)
