import numpy as np
matrix1 = np.array([[1,5, 2], [3,2, 4],[1,2,5]])
matrix2 = np.array([[1,2, 3], [4,5, 6],[7,8,9]])
addition = matrix1 + matrix2
subtraction = matrix1 - matrix2
multiplication = matrix1 * matrix2
determinant1 = np.linalg.det(matrix1)
determinant2 = np.linalg.det(matrix2)
print("Addition:\n", addition)
print("Subtraction:\n", subtraction)
print("Multiplication:\n", multiplication)
print("Determinant of matrix1:", determinant1)
print("Determinant of matrix2:", determinant2)