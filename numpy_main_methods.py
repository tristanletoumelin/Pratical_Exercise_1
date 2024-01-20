import numpy as np

# One-dimensional array
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array: np.array([1, 2, 3, 4, 5])")
print(arr_1d)

# Matrix
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array: np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])")
print(arr_2d)

# Specific arrays
zeros_array = np.zeros((3, 3))  # 3x3 matrix of zeros
ones_array = np.ones((2, 4))    # 2x4 matrix of ones
identity_matrix = np.eye(3)     # 3x3 identity matrix
random_array = np.random.rand(2, 2)  # 2x2 matrix of random numbers between 0 and 1

print("\nZeros Array: np.zeros((3, 3))")
print(zeros_array)
print("\nOnes Array: np.ones((2, 4))")
print(ones_array)
print("\nIdentity Matrix: np.eye(3)")
print(identity_matrix)
print("\nRandom Array: np.random.rand(2, 2)")
print(random_array)

arr_a = np.array([[1, 2], [3, 4]])
arr_b = np.array([[5, 6], [7, 8]])

# Operations on arrays
add_result = np.add(arr_a, arr_b)
sub_result = np.subtract(arr_a, arr_b)
mul_result = np.multiply(arr_a, arr_b)

print("\nAddition Result: np.add(arr_a, arr_b)")
print(add_result)
print("\nSubtraction Result: np.subtract(arr_a, arr_b)")
print(sub_result)
print("\nMultiplication Result: np.multiply(arr_a, arr_b)")
print(mul_result)

# Statistical operations
mean_value = np.mean(arr_a)  # Mean
sum_value = np.sum(arr_a)    # Sum of all elements
min_value = np.min(arr_a)    # Minimum
max_value = np.max(arr_a)    # Maximum

print("\nMean Value: np.mean(arr_a)")
print(mean_value)
print("Sum Value: np.sum(arr_a)")
print(sum_value)
print("Minimum Value: np.min(arr_a)")
print(min_value)
print("Maximum Value: np.max(arr_a)")
print(max_value)
