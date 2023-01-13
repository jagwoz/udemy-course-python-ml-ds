import pandas as pd

df = pd.DataFrame({
    'a': [0, 1, 2, 3],
    'b': [2, 2, 2, 5],
    'c': [4, 3, 2, 1]
    #  'd': ['xx', 'xxx', 'x', 'xxxx']
})

print(df['b'].unique())
print(df['b'].nunique())  # number

print(df['b'].value_counts())
print(type(df['b'].value_counts()))

print(df[df['c'] > 1])
print(df['c'] > 1)
print(df[(df['c'] > 1) & (df['b'] == 2)])

print(df['a'].sum())
print(df['a'].apply(lambda x: x*2))
# print(df['d'].apply(len))

print(df)
print(df.drop(0))  # /inplace=True
# print(df.drop(['a', 'd'], axis=1))
print(df.columns)
print(df.index)

print(df)
print(df.sort_values('c'))
print(df.sort_values(3, axis=1))

print(df.pivot_table(values='c', index='a', columns='b'))