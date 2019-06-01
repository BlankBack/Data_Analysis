
"""
1、读取文件
现在假设我们有一个组关于狗的名字的统计数据，那么为了观察这组数据的情况，我们应该怎么做呢？
数据来源：https://www.kaggle.com/new-york-city/nyc-dog-names/data

"""
import pandas as pd
import numpy as np
import string

# 读取CSV的文件
df = pd.read_csv("../dogNames2.csv")
# print(df)

# pandas之DataFrame
# p1 = pd.DataFrame(np.arange(12).reshape(3, 4),index=list(string.ascii_uppercase[:3]),columns=list(string.ascii_uppercase[-4:]))
# print(p1)
#
# d1 = {"name":["xiaoming", "xiaohong"], "age":[20, 32],"tel":[10086, 10010]}
# t1 = pd.DataFrame(d1,index=list('ab'))
# print(t1)
# print(type(t1))
#
# t2 = [{"name":"xiaohong", "age":18, "tel":10086},{"name":"xiaogang", "tel":10006},{"name":"xiaoming", "age":14}]
# print(t2)
# print(pd.DataFrame(t2))

# print(df.head())
# # print(df.info())

# DataFrame中排序的方法
df = df.sort_values(by="Count_AnimalName",ascending=False)

# print(df.tail(10))
print(df.head(5))


