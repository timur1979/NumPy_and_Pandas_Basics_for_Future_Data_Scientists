import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)

print("##################--------1 Basic reshape")
a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape(2, 3)
print(b)

print("##################--------2 Basic reshape")
a = np.array([1,2,3,4,5,6])
b = a.reshape(3,2)
print(b)

print("##################--------3 Automatic dimension with -1")
a = np.array([1,2,3,4,5,6])
b = a.reshape(2, -1)
print(b)

print("##################--------4 Convert to column vector")
a = np.array([1,2,3,4])
b = a.reshape(-1,1)
print(b)

print("##################--------5 Convert to row vector")

b = a.reshape(1,-1)
print(b)


print("##################--------6 Reshaping 2D arrays")
a = np.array([
    [1,2,3],
    [4,5,6]
])

b = a.reshape(3,2)

print(b)


print("##################--------7 Flatten array (convert to 1D)")

a = np.array([
    [1,2,3],
    [4,5,6]
])

b = a.reshape(-1)

print(b)


print("##################--------8 Using ravel()")

a = np.array([
    [1,2,3],
    [4,5,6]
])

print(a.ravel())




