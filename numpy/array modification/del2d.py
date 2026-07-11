import numpy as np
num = np.array([[1, 2,3], [3,5, 4], [5, 6,8]])
num2 = np.delete(num ,2, axis=1)
print(num2)