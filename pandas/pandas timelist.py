
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager

"""
用pandas处理时间序列
生成一段时间范围：
pd.date_range(start=None,end=None,periods=None,freq='D')
periods表示时间段，表示时间的个数,数据类型为datetime64,freq表示频率，D为天,M为月

"""
# data1 = pd.date_range(start="20171230", end="20180131", freq="10D")
# print(data1)
#
# print("*" * 100)
#
# data2 = pd.date_range(start="20171230", periods=10, freq="M")
# print(data2)

"""
统计出911数据中不同月份电话次数的变化情况
统计出911数据中不同月份不同类型的电话的次数的变化情况
"""
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")

file_path = "./911.csv"
df = pd.read_csv(file_path)

df["timeStamp"] = pd.to_datetime(df["timeStamp"])
df.set_index("timeStamp",inplace=True)
# 统计出911数据中不同月份电话次数的变化情况
count_by_month = df.resample("M").count()
# print(count_by_month)

# 画图
_x = count_by_month.index
_y = count_by_month.values

_x = [i.strftime("%Y%m%d") for i in _x]

plt.figure(figsize=(20,8),dpi=80)

plt.plot(range(len(_x)),_y)

plt.xticks(range(len(_x)),_x,rotation=45)

plt.show()

# 统计出911数据中不同月份不同类型的电话的次数的变化情况










