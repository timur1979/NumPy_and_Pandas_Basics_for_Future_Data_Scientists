# Importing pandas
import pandas as pd
import numpy as np

# Creating a DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)
print(df)


# Extracting a single column by name
df['Name']
print(df['Name'])


print(type(df['Name']))

print(df.Age)

# Extracting a DataFrame with multiple selected columns
df[['Name', 'City']]
print(df[['Name', 'City']])

df.index = ['Person 1', 'Person 2', 'Person 3', 'Person 4']
print(df)


# Extracting rows by label through loc
df.loc['Person 1']
print(df.loc['Person 1'])

# Extracting rows by integer location through iloc
df.iloc[0]  # Extracts the first row
print(df.iloc[0])


# Accessing a cell
df.loc['Person 1', 'Age']
print(df.loc['Person 1', 'Age'])


# Modifying a cell
print(df)
df.loc['Person 1', 'Age'] += 100
print(df)

df['Name'].str.upper()
print(df['Name'].str.upper())

# Modifying a whole column
df['Name'] = df['Name'].str.upper()
print(df)


# Adding a new column
df['Country'] = ['USA', 'France', 'Germany', 'UK']
print(df)



print(df)

# Adding a new column
df['Profession'] = ['Engineer', 'Doctor', 'Artist', 'Scientist']
print(df)

# Dropping a column
df = df.drop('Age', axis=1)
print(df)


# Why doesn't this drop the 'Profession' column?
df.drop('Profession', axis=1)
print(df.drop('Profession', axis=1))


# Dropping a row
df = df.drop('Person 1', axis=0) # axis=0 is the default but specifying it here for clarity
print(df)

