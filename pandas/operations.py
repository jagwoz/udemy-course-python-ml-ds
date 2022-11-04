import pandas as pd
import numpy as np


data = {
    'group': ['g1', 'g2', 'g1', 'g1', 'g2', 'g3', 'g3'],
    'values1': np.arange(7) * 2,
    'values2': np.arange(7) ** 2
}

df = pd.DataFrame(data)
print(df)

df_group = df.groupby('group').sum()
print(df_group)

print(df.groupby('group').describe()['values1'])

print(df.groupby('group').describe().transpose())



print(df)