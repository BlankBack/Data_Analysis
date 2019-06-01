
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")

file_path = "./starbucks_store_worldwide.csv"

df = pd.read_csv(file_path)
df = df[df["Country"] == "CN"]

# 使用matplotlib呈现出中国每个城市的店铺数量
# 准备数据
data1 = df.groupby(by = "City").count()["Brand"].sort_values(ascending=False)[:25]

_x = data1.index
_y = data1.values

# 画图
plt.figure(figsize=(20,8),dpi=80)

plt.barh(range(len(_x)),_y,height=0.3,color="green")

plt.yticks(range(len(_x)),_x,fontproperties=my_font)
plt.show()

# 使用matplotlib呈现出店铺总数排名前10的国家
