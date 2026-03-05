import numpy as np

data = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Row 0, column 1 → 2
print(data[0, 1])

#Entire row
print(data[1])

#Entire column
print(data[:, 0])

