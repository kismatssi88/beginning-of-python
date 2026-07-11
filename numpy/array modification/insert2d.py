import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
arr2 =np.insert(arr,2,7,axis = 0)
print(arr2)
arr3 =np.insert(arr,1,[7,8,9],axis = 0)
print(arr3)