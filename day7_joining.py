import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.vstack((a, b))
print(result)


print("##################--------1 Vertical stack with 2D arrays")

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6]
])

result = np.vstack((a, b))

print(result)



print("##################--------2 Horizontal stack (hstack)")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.hstack((a, b))

print(result)


print("##################--------3 Horizontal stack with 2D arrays")


a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

result = np.hstack((a, b))

print(result)





print("##################--------4 Real ML example (feature engineering)")

#Real ML example (feature engineering)
#Age    Salary
#25     50000
#30     60000

age = np.array([25, 30]).reshape(-1,1)
print(age)
salary = np.array([50000, 60000]).reshape(-1,1)
print(salary)
experience = np.array([2, 5]).reshape(-1,1)
print(experience)


data = np.hstack((age, salary, experience))

print(data)




print("##################--------5 Another real example (adding new rows)")

data = np.array([
    [25, 50000],
    [30, 60000]
])

new_row = np.array([[35, 70000]])

updated = np.vstack((data, new_row))

print(updated)


np.concatenate((a, b), axis=0)  # like vstack
np.concatenate((a, b), axis=1)  # like hstack


