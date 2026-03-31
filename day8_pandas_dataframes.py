import pandas as pd

print("##################--------1     Create DataFrame from dictionary")
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "salary": [50000, 60000, 70000]
}

df = pd.DataFrame(data)
print(df)

print("##################--------2     basic info")
print(df.shape)     # (rows, columns)
print(df.columns)
print(df.dtypes)


print("##################--------3     select column")
print(df["age"])

print("##################--------4     Select multiple columns")
print(df[["name", "salary"]])

print("##################--------5     Select rows")
print(df.iloc[0])     # first row
print(df.iloc[0:2])   # first 2 rows


print("##################--------6     Filtering rows")
print(df[df["age"] > 28])


print("##################--------7     Add new column")
df["bonus"] = df["salary"] * 0.1
print(df)

print("##################--------8     Summary statistics")
print(df.describe())


