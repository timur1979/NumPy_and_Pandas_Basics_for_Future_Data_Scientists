import numpy as np
import pandas as pd

# Read a CSV file
powerball_df = pd.read_csv('./powerball_winners.csv')

# Find it's shape (how many rows and columns)
powerball_df.shape
print(powerball_df.shape)


# Display the first 5 rows
powerball_df.head()
print(powerball_df.head())

# You can specify how many rows
powerball_df.head(2)
print(powerball_df.head(2))

# Display the last 5 rows
powerball_df.tail()
print(powerball_df.tail())


# Get all the column names
powerball_df.columns
print(powerball_df.columns)


print(powerball_df.dtypes)


pd.to_datetime(powerball_df['Draw Date'])
print(pd.to_datetime(powerball_df['Draw Date']))



powerball_df['Draw Date'] = pd.to_datetime(powerball_df['Draw Date'])
print(powerball_df.dtypes)


print(powerball_df.index)

print("1111111")

print(powerball_df.loc[0])


print("2222222")
print(powerball_df.iloc[0])



print("33333333")
# make a copy of the dataframe with the 'Draw Date' as the index
reindexed_df = powerball_df.set_index('Draw Date')


print(reindexed_df) 


