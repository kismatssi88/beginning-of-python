import numpy as np
num = np.array([[1, 2, 3], [4, 5, 6]])
result = num.flatten()
result2 = num.ravel()
print("Flattened array:", result)
print("Raveled array:", result2)