
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((2,4)),index=["A","B"],columns=list("abcd"))
df2 = pd.DataFrame(np.zeros((3,3)),index=["A","B","C"],columns=list("xyz"))
df3 = pd.DataFrame(np.arange(9).reshape((3,3)),columns=list("fax"))
print(df1)
print('*' * 100)
print(df2)
print('*' * 100)
print(df3)
print('*' * 100)
# 默认为inner并集补全
# 按照交集，NAN补全
print(df1.merge(df3,how="outer"))
print(df1.merge(df3,how="left"))    # 按照左边为准补全
print(df1.merge(df3,how="right"))   # 按照右边为准补全



