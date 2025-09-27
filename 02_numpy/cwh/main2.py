import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# indexing and slicing

flat = arr.flatten()
print(flat[4])  # indexing
print(flat[2:5])
print(flat[:5])
print(flat[0::2])  # every second element

# slicing returns a view not a copy unlike lists in python (which returns a copy)
# this is done by numpy to avoid unnecessary copies, making operations faster and saving memory

b = flat[3:7]
b[0] = 444
print(flat)


# but i want a copy

b = flat[1:3].copy()
b[0] = 22878
print(flat)

# fancy idexing

indexes = [0, 1, 2, 5]
arr = np.array([x for x in range(100)])

selected = arr[indexes]
selected[0] = 2381

# boolean masking
mask = arr > 80
print(arr[mask])
