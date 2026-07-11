import numpy as np
num = np.array([1, 2, np.inf, 4, -np.inf, 6])
print(np.isinf(num))
clean = np.nan_to_num(num,posinf = 100, neginf = -100)
print(clean)