
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")

file_path = "./books.csv"
df = pd.read_csv(file_path)
# # 查看数据
# print(df.head(2))
# print('*' * 100)
# print(df.info())

data1 = df[pd.notnull(df["original_publication_year"])]
# grouped = data1.groupby(by="original_publication_year").count()["title"]

# 不同年份的书平均评分情况
# 去除nan的行
# data1 = df[pd.notnull(df["original_publication_year"])]
#
grouped = data1["average_rating"].groupby(by=data1["original_publication_year"]).mean()
print(grouped)

_x = grouped.index
_y = grouped.values

# 绘制图形大小
plt.figure(figsize=(20,8),dpi=80)

plt.plot(range(len(_x)),_y)

plt.xticks(list(range(len(_x)))[::10],_x[::10].astype(int),rotation=45)
plt.show()
