import pandas as pd

df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie']
})

print(df1)

df2 = pd.DataFrame({
    'id': [1, 2, 4],
    'score': [85, 90, 95]
})

print(df2)


#innner join
print("inner join")
merge_inner = pd.merge(df1, df2, on='id')
print(merge_inner)


#left join
print("left join")
merge_left = pd.merge(df1, df2, on='id', how='left')
print(merge_left)


#right join
print("right join")
merge_right = pd.merge(df1, df2, on='id', how='right')
print(merge_right)

#outer join
print("outer join")
merge_outer = pd.merge(df1, df2, on='id', how='outer')
print(merge_outer)


#join() — index-based joining
print("join")
df1 = df1.set_index('id')
df2 = df2.set_index('id')

join_ex = df1.join(df2, how='left')
#Same result as left merge, but based on index.
print(join_ex)



#concat() — stacking data
print("concat, Vertical (rows):")
conc_ex = pd.concat([df1, df2])
print(conc_ex)

print("concat, Horizontal (columns):")
conc_ex = pd.concat([df1, df2], axis=1)
print(conc_ex)
