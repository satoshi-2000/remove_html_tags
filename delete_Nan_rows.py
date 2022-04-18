import pandas as pd

mylist = ["A","B","C"]
values = [1,2]
df = pd.DataFrame(data=[mylist,values])
print(df)
"""
   0  1     2
0  A  B     C
1  1  2  None
"""

isnull_index = df.isnull().any(axis=1)
print(isnull_index)
"""
0    False
1     True
dtype: bool
"""
notnull_index = [not i for i in isnull_index ]
print(notnull_index)
# [True, False]

print(df[isnull_index])
"""
   0  1     2
1  1  2  None
"""

print(df[notnull_index])
"""
   0  1  2
0  A  B  C
"""
