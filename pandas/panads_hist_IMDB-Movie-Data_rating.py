
import pandas as pd
from matplotlib import pyplot as plt

file_path = "./IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)

# print('*' * 100)
# print(df.head(10))
# print('*' * 100)
# print(df.info())

# rating,runtime 分布情况
# 选择图形，队连续数据的统计直方图
# 统计数据，取数据
# runtime_data = df["Runtime (Minutes)"].values
runtime_data = df["Rating"].values


max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

# 计算组数
num_bin_list = [1.6]
i=1.6
while i<=max_runtime:
    i += 0.5
    num_bin_list.append(i)

# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)

# 绘制直方图
plt.hist(runtime_data, num_bin_list)

_x = [min_runtime]
i = min_runtime
while i<=max_runtime+0.5:
    i = i+0.5
    _x.append(i)

# 绘制x轴的刻度
plt.xticks(_x)

# 显示直方图
plt.show()