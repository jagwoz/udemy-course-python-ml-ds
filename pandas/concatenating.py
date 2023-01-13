import pandas as pd

df_1 = pd.DataFrame({
    'A': [0, 1, 2, 3],
    'B': [4, 5, 6, 7]
}, index=[0, 1, 2, 3])

df_2 = pd.DataFrame({
    'C': [0, 1, 2, 3],
    'D': [4, 5, 6, 7]
}, index=[4, 5, 6, 7])

df_3 = pd.concat([df_1, df_2])
print(df_3)

df_4 = pd.concat([df_1, df_2], axis=1)
print(df_4)

