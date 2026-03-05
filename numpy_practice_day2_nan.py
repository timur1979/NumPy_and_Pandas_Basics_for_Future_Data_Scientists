import numpy as np

data = np.array([1, 2, np.nan, 4, 5])

print(data)

print(data.dtype)


data = np.array([1, 2, np.nan, 4, np.nan])
result = np.isnan(data)
print(result)



print("==============>1")
#Count missing values
data = np.array([10, 20, np.nan, 40, np.nan, 60])
print(np.isnan(data))
missing_count = np.isnan(data).sum()
print("Missing values:", missing_count)

print("==============>2")
#Remove NaN values
data = np.array([1, 2, np.nan, 4, np.nan])
clean_data = data[~np.isnan(data)]
print(clean_data)


print("==============>3")
#Replace NaN with a number
data = np.array([10, 20, np.nan, 40])
data[np.isnan(data)] = 0
print(data)

print("==============>4")
#Replace NaN with mean value (very common in ML)
data = np.array([10, 20, np.nan, 40, 50])
print(np.nanmean(data))
mean_value = np.nanmean(data)
data[np.isnan(data)] = mean_value
print(data)

print("==============>5")
#NaN in 2D arrays (datasets)
#Age   Salary
#25    50000
#NaN   60000
#30    NaN
data = np.array([
    [25, 50000],
    [np.nan, 60000],
    [30, np.nan]
])
print(np.isnan(data))


print("==============>6")
#Count NaN per column
data = np.array([
    [25, 50000],
    [np.nan, 60000],
    [30, np.nan]
])

print(np.isnan(data).sum(axis=0))
#column 1 → 1 missing
#column 2 → 1 missing


print("==============>7")
#Important rule: NaN comparisons
print(np.nan == np.nan)

