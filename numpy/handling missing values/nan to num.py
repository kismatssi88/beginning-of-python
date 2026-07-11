import numpy as np
num = np.array([1, 2, np.nan, 4, np.nan, 6])
print(np.isnan(num))
clear = np.nan_to_num(num,nan =10)
print(clear)