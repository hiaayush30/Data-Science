import numpy as np

arr = np.array([1, 2, 3, 4, 5])
doubled = arr * 2
print(doubled)

# Creating arrays from scratch

arr1 = np.zeros((2, 3))
arr1 = np.ones((2, 3))
arr1 = np.full((2, 3), 8)
arr1 = np.eye(4)  # 4 X 4 identity matrix  => main diagonal has 1 rest have 0
arr1 = np.arange(1, 10)  # excluding 10 ie go till 9 by adding 1 (default)
arr1 = np.arange(1, 10, 3)
arr1 = np.linspace(0, 100, 5)  # evenly spaced arrays (0 to 100 divided into 5 parts)

# getting info about your numpy array

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2.shape)
print(arr2.size)  # 2*3 elements
print(arr2.ndim)  # dimensions
print(arr2.dtype)

# you can explicitly change the dtype
arr3 = np.array([[1, 2, 3], [4, 5, 6]], dtype="float32")
print(arr3.dtype)
# you can also convert an existing one
arr4 = arr2.astype("float64")
print(arr4.dtype)
# np arrays are strongly typed ie all elements have same datatype

# reshaping and flattening
reshaped = arr2.reshape((3, 2))  # size should remain same (ie total elements)
print(arr2.flatten())


arr9 = np.arange(1, 10)
print(arr.size)
print(arr.dtype)
