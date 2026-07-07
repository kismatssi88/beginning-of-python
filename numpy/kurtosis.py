import numpy as np
num =np.array([10, 20, 30, 40, 50])
frequency = np.array([1, 6, 7, 4, 5])
kurtosis = np.sum(frequency * (num - np.mean(num))**4) / (np.sum(frequency) * np.std(num)**4) - 3                   
print(kurtosis)