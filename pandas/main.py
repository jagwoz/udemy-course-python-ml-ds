import pandas as pd
import numpy as np


labels = ['l1', 'l2', 'l3']
vales = np.arange(3)

series = pd.Series(data=vales, index=labels)  # can positional (values, labels)
print(series)

dict_series = {key: labels.index(key) for key in labels}
series = pd.Series(dict_series)  # from dict
print(series)

functions = pd.Series(data=[sum, print, lambda x:x**2])
print(functions[2](3))

series_2 = pd.Series(data=vales, index=['l1', 'l2', 'l4'])
final_series = series + series_2
print(final_series)
