import numpy as np

data = np.array([5, 2, 9, 1, 7])

sorted_data = np.sort(data)

print(sorted_data)

print("##################--------1 Sorting in descending order")

data = np.array([5, 2, 9, 1, 7])
sorted_desc = np.sort(data)[::-1]
print(sorted_desc)

print("##################--------2 Sorting a 2D array")

data = np.array([
    [3, 1, 2],
    [9, 5, 7]
])

print(np.sort(data))


print("##################--------3 Sorting by rows or columns (axis)")

data = np.array([
    [3, 1, 2],
    [9, 5, 7]
])

print(np.sort(data, axis=1))

print("Sort by columns (axis=0)", np.sort(data, axis=0))


print("##################--------4 Sorting using indices")


data = np.array([40, 10, 30, 20])

indices = np.argsort(data)

sorted_data = data[indices]

print(sorted_data)


print("##################--------4 Sorting multiple arrays together")
#Age   Salary
#25    50000
#30    60000
#22    45000

age = np.array([25, 30, 22])
salary = np.array([50000, 60000, 45000])

indices = np.argsort(age)

print(age[indices])
print(salary[indices])

