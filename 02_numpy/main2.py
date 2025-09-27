import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# indexing and slicing

flat = arr.flatten()
print(flat[4])
print(flat[2:5])
print(flat[:5])
print(flat[0::2])  # every second element

# slicing returns a view not a copy unlike lists in python (which returns a copy)
# this is done by numpy to avoid unnecessary copies, making operations faster and saving memory

b = flat[3:7]
b[0] = 444
print(flat)
