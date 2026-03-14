import numpy as np

a = np.array([1, 2, 3])
result = a + 10
print(result)


print("##################--------1 broadcasting with multiplication")
a = np.array([2, 4, 6])
result = a * 3
print(result)


print("##################--------1 Broadcasting between 1D and 2D arrays")

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

vector = np.array([10, 20, 30])

result = matrix + vector

print(result)



print("##################--------1 Column broadcasting")

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

column = np.array([
    [10],
    [20]
])

result = matrix + column

print(result)




print("##################--------1 Broadcasting with subtraction")

data = np.array([100, 120, 140])

mean = np.mean(data)

result = data - mean

print(result)


print("##################--------1 Broadcasting for scaling dataset")
#age   salary
#25    50000
#30    60000
#35    70000

data = np.array([
    [25, 50000],
    [30, 60000],
    [35, 70000]
])

scale = np.array([1, 0.001])
print(scale)
result = data * scale

print(result)






