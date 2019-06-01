
import numpy as np
from matplotlib import pyplot as plt

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

t_uk = np.loadtxt(uk_file_path,delimiter=",",dtype="int")

# 选择喜欢书比500000小的数据
t_uk = t_uk[t_uk[:,1] < 500000]

# 取评论的数据
print(t_uk)
t_uk_comments = t_uk[:,-1]
t_uk_like = t_uk[:,1]

# 绘图
plt.figure(figsize=(20,8),dpi=80)

plt.scatter(t_uk_like, t_uk_comments)

plt.show()