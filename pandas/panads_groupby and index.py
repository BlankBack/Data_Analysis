
import pandas as pd
import numpy as np
"""
现在我们有一组关于全球星巴克店铺的统计数据，
如果我想知道美国的星巴克数量和中国的哪个多，
或者我想知道中国每个省份星巴克的数量的情况，那么应该怎么办？
思路：遍历一遍，每次加1 ？？？
数据来源：https://www.kaggle.com/starbucks/store-locations/data
"""

file_path = "./starbucks_store_worldwide.csv"

df = pd.read_csv(file_path)

# print(df.head(1))
# print(df.info())

# grouped = df.groupby(by="Country")
# print(grouped)
#  DataFrameGroupBy 可以进行遍历，可以调用聚合方法
# country_count = grouped["Brand"].count()
# print(country_count["US"])
# print(country_count["CN"])

# 统计中国每个省份星巴克的数量

# china_data = df[df["Country"] == "CN"]
#
# grouped = china_data.groupby(by="State/Province").count()["Brand"]
# print(grouped)

# 数据按照多个条件进行分组,返回Series
# grouped = df["Brand"].groupby(by=[df["Country"],df["State/Province"]]).count()
# print(grouped)
# print(type(grouped))

# 数据按照多个条件进行分组,返回DataFrame
grouped = df[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count()
# print(grouped)

# 索引的方法和属性
print(grouped.index)
