import numpy as np



print("==============>1")
#Create sample arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a)
print(b)


print("==============>2")
#Addition of arrays
result = a + b
print(result)


print("==============>3")
#Subtraction
result = b - a
print(result)


print("==============>4")
#Multiplication
result = a * b
print(result)


print("==============>5")
#Division
result = b / a
print(result)

print("==============>6")
#Operations with scalars
#NumPy applies operations to every element.
a = np.array([1, 2, 3])
print(a + 10)


print("==============>7")
#Power operations
a = np.array([1, 2, 3, 4])
print(a ** 2)

print("==============>8")
#Basic statistics
data = np.array([10, 20, 30, 40, 50])

print(np.mean(data))
print(np.sum(data))
print(np.min(data))
print(np.max(data))


print("==============>9")
#Square root
data = np.array([1, 4, 9, 16])
print(np.sqrt(data))



print("==============>10")
#Filtering arrays (very important)
a = np.array([2, 4, 6, 8, 10])
result = a[a > 5]
print(result)


print("==============>11")
#Operations on 2D arrays
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print(a + b)




print("==============>12")
#Matrix multiplication
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print(a @ b)


print("==============>13")
#Absolute values
a = np.array([-1, -5, 3])
print(np.abs(a))


