import numpy as np

data = np.array([10, 20, 30, 40])
print(np.sum(data))


print("##################--------1")
data = np.array([10, 20, 30, 40])
print(np.mean(data))


print("##################--------2")
data = np.array([10, 5, 30, 2])
print(np.min(data))

print("##################--------3")
data = np.array([10, 5, 30, 2])
print(np.max(data))


print("##################--------4 Standard deviation")
data = np.array([10, 20, 30, 40])
print(np.std(data))


print("##################--------5 Variance = standard deviation²")
data = np.array([10, 20, 30, 40])
print(np.var(data))

print("##################--------6 Middle value")
data = np.array([10, 20, 30, 40, 50])
print(np.median(data))


print("##################--------7 Students × subjects")
scores = np.array([
    [80, 90, 85],
    [70, 60, 75],
    [88, 92, 95]
])

print(np.sum(scores))

print("##################--------7 Column sums")
print(np.sum(scores, axis=0))

print("##################--------7 Row sums")
print(np.sum(scores, axis=1))

print("##################--------7 Mean per column")
print(np.mean(scores, axis=0))

print("##################--------7 Mean per row")
print(np.mean(scores, axis=1))
