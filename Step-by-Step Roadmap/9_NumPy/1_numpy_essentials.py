# ✅ numpy_essentials.py — All NumPy Functions with Examples & Comments


# numpy_essentials.py

import numpy as np

# -------------------------------------------------------
# ✅ 1. Creating Arrays
# -------------------------------------------------------

# From list
arr1 = np.array([1, 2, 3])
print("Array from list:", arr1)

# Multi-dimensional array
arr2 = np.array([[1, 2], [3, 4]])
print("\n2D Array:\n", arr2)

# Array of zeros
zeros = np.zeros((2, 3))
print("\nZeros:\n", zeros)

# Array of ones
ones = np.ones((2, 3))
print("\nOnes:\n", ones)

# Identity matrix
identity = np.eye(3)
print("\nIdentity Matrix:\n", identity)

# Range of values
range_array = np.arange(0, 10, 2)
print("\nArange (0 to 10 step 2):", range_array)

# Linearly spaced array
linspace_array = np.linspace(0, 1, 5)
print("\nLinspace (0 to 1 with 5 points):", linspace_array)

# Random values
rand_uniform = np.random.rand(2, 2)  # Uniform [0,1)
rand_normal = np.random.randn(2, 2)  # Normal distribution
rand_int = np.random.randint(1, 10, (2, 3))  # Random integers

print("\nRandom Uniform:\n", rand_uniform)
print("\nRandom Normal:\n", rand_normal)
print("\nRandom Integers:\n", rand_int)

# -------------------------------------------------------
# ✅ 2. Array Attributes & Inspection
# -------------------------------------------------------

print("\nShape:", arr2.shape)
print("Size:", arr2.size)
print("Data type:", arr2.dtype)
print("Number of dimensions:", arr2.ndim)

# -------------------------------------------------------
# ✅ 3. Reshape, Flatten, Transpose
# -------------------------------------------------------

reshaped = np.arange(1, 7).reshape(2, 3)
flattened = reshaped.flatten()
transposed = reshaped.T

print("\nReshaped:\n", reshaped)
print("Flattened:", flattened)
print("Transposed:\n", transposed)

# -------------------------------------------------------
# ✅ 4. Indexing & Slicing
# -------------------------------------------------------

a = np.array([[10, 20, 30], [40, 50, 60]])

print("\nElement [1,2]:", a[1, 2])  # 60
print("Row 0:", a[0])
print("Column 1:", a[:, 1])
print("Sliced:\n", a[0:2, 1:3])

# -------------------------------------------------------
# ✅ 5. Mathematical Operations
# -------------------------------------------------------

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Element-wise operations
print("\nAddition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Exponent:", x ** 2)

# Universal functions (ufuncs)
print("\nSqrt:", np.sqrt(x))
print("Sin:", np.sin(x))
print("Log:", np.log(x))

# -------------------------------------------------------
# ✅ 6. Aggregate Functions
# -------------------------------------------------------

b = np.array([[1, 2], [3, 4]])

print("\nSum:", np.sum(b))
print("Sum by axis 0 (columns):", np.sum(b, axis=0))
print("Sum by axis 1 (rows):", np.sum(b, axis=1))

print("Mean:", np.mean(b))
print("Median:", np.median(b))
print("Standard Deviation:", np.std(b))
print("Min:", np.min(b))
print("Max:", np.max(b))

# -------------------------------------------------------
# ✅ 7. Boolean Masking & Filtering
# -------------------------------------------------------

arr = np.array([10, 20, 30, 40, 50])

mask = arr > 25
filtered = arr[mask]

print("\nBoolean Mask:", mask)
print("Filtered (arr > 25):", filtered)

# -------------------------------------------------------
# ✅ 8. Array Copy vs View
# -------------------------------------------------------

original = np.array([1, 2, 3])
view = original.view()
copy = original.copy()

original[0] = 99

print("\nOriginal:", original)
print("View (shares data):", view)
print("Copy (independent):", copy)

# -------------------------------------------------------
# ✅ 9. Broadcasting
# -------------------------------------------------------

array1 = np.array([[1], [2], [3]])
array2 = np.array([10, 20, 30])

broadcast_result = array1 + array2
print("\nBroadcasted Addition:\n", broadcast_result)

# -------------------------------------------------------
# ✅ 10. Save and Load Arrays
# -------------------------------------------------------

np.save("my_array.npy", arr1)           # Save to .npy file
loaded_array = np.load("my_array.npy")  # Load it back

print("\nSaved and Loaded Array:", loaded_array)

# -------------------------------------------------------
# ✅ 11. Matrix Operations
# -------------------------------------------------------

matrix_A = np.array([[1, 2], [3, 4]])
matrix_B = np.array([[5, 6], [7, 8]])

# Dot product
dot_product = np.dot(matrix_A, matrix_B)
print("\nDot Product:\n", dot_product)

# Matrix inverse
inverse_A = np.linalg.inv(matrix_A)
print("Inverse of A:\n", inverse_A)

# Determinant
det_A = np.linalg.det(matrix_A)
print("Determinant of A:", det_A)

# Eigenvalues and eigenvectors
eig_vals, eig_vecs = np.linalg.eig(matrix_A)
print("Eigenvalues:", eig_vals)
print("Eigenvectors:\n", eig_vecs)

# -------------------------------------------------------
# ✅ 12. Set Operations
# -------------------------------------------------------

arr_a = np.array([1, 2, 3, 4])
arr_b = np.array([3, 4, 5, 6])

print("\nUnion:", np.union1d(arr_a, arr_b))
print("Intersection:", np.intersect1d(arr_a, arr_b))
print("Set Difference (A - B):", np.setdiff1d(arr_a, arr_b))
print("Symmetric Difference:", np.setxor1d(arr_a, arr_b))


# =========================================================================================

# ✅ Summary – All Key NumPy Functions Covered:
# Task	Function/Method
# Create Arrays	np.array(), np.zeros(), np.ones()
# Array Info	shape, size, dtype, ndim
# Reshape/Flatten	reshape(), flatten(), T
# Indexing & Slicing	a[0:2, 1:3], a[:, 1]
# Arithmetic Ops	+, -, *, /, **
# UFuncs	np.sqrt(), np.log(), np.sin()
# Aggregations	sum(), mean(), std(), max()
# Filtering	Boolean masking: arr[arr > 25]
# Copy vs View	copy(), view()
# Broadcasting	Automatic shape expansion
# Save & Load	np.save(), np.load()
# Matrix Algebra	dot(), inv(), eig(), det()
# Set Operations	union1d(), intersect1d()

# =========================================================================================

