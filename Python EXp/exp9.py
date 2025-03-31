# import numpy as np

# # Creating arrays
# arr_1D = np.array([1, 2, 3, 4, 5])
# arr_2D = np.array([[1, 2, 3], [4, 5, 6]])
# arr_3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# print("1D Array:\n", arr_1D)
# print("2D Array:\n", arr_2D)
# print("3D Array:\n", arr_3D)

# # Reshaping the 1D array to 2D
# reshaped_arr = arr_1D.reshape(5, 1)
# print("\nReshaped 1D to 2D:\n", reshaped_arr)

# # Slicing (Extracting part of the array)
# print("\nSlicing 2D Array (First row):\n", arr_2D[0, :])
# print("Slicing 3D Array (First element of each sub-array):\n", arr_3D[:, 0, 0])

# # Indexing
# print("\nElement at row 1, column 2 in 2D array:", arr_2D[1, 2]) 

# import numpy as np

# # Creating two 1D arrays
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])

# # Element-wise operations
# print("Addition:\n", arr1 + arr2)          # [5 7 9]
# print("Subtraction:\n", arr1 - arr2)       # [-3 -3 -3]
# print("Multiplication:\n", arr1 * arr2)    # [4 10 18]
# print("Division:\n", arr1 / arr2)          # [0.25 0.4 0.5]

# # Dot product (1D)
# dot_product = np.dot(arr1, arr2)
# print("\nDot Product:", dot_product)  # (1*4 + 2*5 + 3*6) = 32

# # Cross product (1D)
# cross_product = np.cross(arr1, arr2)
# print("Cross Product:\n", cross_product)  # [-3 6 -3]

import numpy as np

# Creating an array
data = np.array([10, 20, 30, 40, 50])

# Statistical calculations
print("Mean:", np.mean(data))                     # 30.0
print("Median:", np.median(data))                 # 30.0
print("Standard Deviation:", np.std(data))        # 14.14
print("Variance:", np.var(data))                  # 200.0

# Correlation coefficient
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
corr_coeff = np.corrcoef(matrix)
print("\nCorrelation Coefficients:\n", corr_coeff)