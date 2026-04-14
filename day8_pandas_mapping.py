import pandas as pd
import numpy as np


my_list = ['cat', 'dog', '', 'rabbit']

list(map(len, my_list))
print(list(map(len, my_list)))


list(map(lambda x: x.upper(), my_list))
print(list(map(lambda x: x.upper(), my_list)))



s = pd.Series(['cat', 'dog', np.nan, 'rabbit'])
print(s)

# na_action='ignore' will ignore the NaN values, not passing them to the function
s.map(len, na_action='ignore')
print(s.map(len, na_action='ignore'))

# instead of passing a function, you can pass a dictionary
a = s.map({'cat': 'kitten', 'dog': 'puppy'})
print(a)


# you can also pass a formatting string
a = s.map('I am a {}'.format)
print(a)

# ignore the NaN values
a = s.map('I am a {}'.format, na_action='ignore')
print(a)
