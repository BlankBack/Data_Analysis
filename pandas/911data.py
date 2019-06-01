
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager

"""
现在我们有2015到2017年25万条911的紧急电话的数据，
请统计出出这些数据中不同类型的紧急情况的次数，
如果我们还想统计出不同月份不同类型紧急电话的次数的变化情况，
应该怎么做呢？
数据来源：https://www.kaggle.com/mchirico/montcoalert/data
"""
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")

file_path = "./911.csv"
df = pd.read_csv(file_path)

# print(df.head(10))
# print(df.info())
# # 其中lat、lng为经纬度
# 获取分类情况
# print(df["title"].str.split(": "))

temp_list = df["title"].str.split(": ").tolist()
cate_list = list(set([i[0] for i in temp_list ]))
# print(cate_list)

# 构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(cate_list))),columns=cate_list)

# 赋值
for cate in cate_list:
    zeros_df[cate][df["title"].str.contains(cate)] = 1
    # print(zeros_df)

sum_ret = zeros_df.sum(axis=0)
print(sum_ret)
# 画图
# plt.figure(figsize=(20,8),dpi=80)
