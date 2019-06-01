
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 统计出911数据中不同月份不同类型的电话的次数的变化情况
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")

file_path = "./911.csv"
df = pd.read_csv(file_path)

# 把时间字符串转换为时间类型并设置成索引
df["timeStamp"] = pd.to_datetime(df["timeStamp"])
df.set_index("timeStamp",inplace=True)
# 统计出911数据中不同月份电话次数的变化情况
count_by_month = df.resample("M").count()