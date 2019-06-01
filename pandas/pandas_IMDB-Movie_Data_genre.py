
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

file_path = "./IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)

# print(df["Genre"])

# 统计分类的列表
temp_list = df["Genre"].str.split(",").tolist()     # [[],[],[],[]]
# print(temp_list)

gener_lsit = list(set([i for j in temp_list for i in j]))

# 构造全为0的数组
zero_df = pd.DataFrame(np.zeros((df.shape[0],len(gener_lsit))),columns=gener_lsit)
# print(zero_df)

# 给每个电影出现分类的位置赋值1
for i in range(df.shape[0]):
    zero_df.loc[i,temp_list[i]] = 1

print(zero_df.head(3))

# 统计每个分类的电影的数量和

gener_count = zero_df.sum(axis=0)
# gener_count1 = zero_df.sum(axis=1)
# print(gener_count1)

# 排序
gener_count = gener_count.sort_values()
print(gener_count)

# 画图
plt.figure(figsize=(20,8),dpi=82)
_x = gener_count.index
_y = gener_count.values
plt.bar(range(len(_x)),_y)
plt.xticks(range(len(_x)),_x)
plt.show()