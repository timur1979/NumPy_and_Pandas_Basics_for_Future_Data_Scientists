import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, 11.0, 6, 8])
print(s)

s.index = ['Person 1', 'Person 2', 'Person 3', 'Person 4', 'Person 5', 'Person 6']
print(s)


# Accessing a single element using .loc (index labels)
s.loc['Person 2']
print(s.loc['Person 2'])

# Accessing a single element using .iloc (positonal index)
s.iloc[0]  # Accessing the first element of the series
print(s.iloc[0])


# Taking a slice, using .loc
# Note that the slice is inclusive of the last element, unlike numeric indexing in Python
s.loc['Person 2':'Person 5']
print(s.loc['Person 2':'Person 5'])



# Taking a slice, using .iloc
# Note that the slice is **exclusive** of the last element, like all numeric indexing in Python
s.iloc[0:3]
print(s.iloc[0:3])



s.loc['Person 1'] = -50
print(s)

s.iloc[0] = 7000  # Setting the first element of the first row
print(s)


# You can do this, but get in the habit of using .iloc (or better yet, .loc), for reasons that will be discussed later.
s[0] = 5000
print(s)
