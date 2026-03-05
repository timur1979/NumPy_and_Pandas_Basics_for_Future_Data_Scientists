import numpy as np

data = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(data.shape)

#Total Number of Elements
print(data.size)

print(data.dtype)



data = data.astype(float)
print(data.dtype)

#Memory Usage (advanced but useful). Shows memory used in bytes.
print(data.nbytes)
