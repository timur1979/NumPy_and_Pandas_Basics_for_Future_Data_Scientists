import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)

print("##################--------1 With custom index")
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)

print("##################--------2 Access elements")
s = pd.Series([1, 2, 3, 4])

print(s * 2)
print(s + 10)

print("##################--------3 Filtering")
print(s[s > 2])


print("##################--------4 slicing")

s = pd.Series([10, 20, 30, 40, 50], index=["a", "b", "c", "d", "e"])
print(s)

print(s[1:4])

print("##################--------5 Label-based slicing")
print(s["b":"d"])

print("##################--------6 Using .iloc (position-based — safest)")
print(s.iloc[1:4])

print("##################--------7 Using .loc (label based)")
print(s.loc["b":"d"])


print("##################--------8 Step slicing")
print(s[::2])


print("##################--------8 Reverse slicing")
print(s[::-1])

print("##################--------9 Boolean slicing")
print(s[s > 25])

print("##################--------10 Multiple conditions")
print(s[(s > 20) & (s < 50)])


print("##################--------11 Select specific labels")
print(s[["a", "c", "e"]])
